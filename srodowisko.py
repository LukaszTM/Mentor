# -*- coding: utf-8 -*-
"""
Środowisko kursu — diagnoza, instalacja w tle, testy powdrożeniowe. (W spec: environment_manager + dependency_installer.)

Zasady:
- Każdy kurs ma własne .venv w katalogu danych użytkownika (srodowiska/<id>/.venv) — zależności kursów nie mieszają się ze sobą
  ani z Pythonem, na którym działa Mentor (w EXE: zapakowany interpreter NIE jest środowiskiem do ćwiczeń).
- Python do venv: najpierw zgodna instalacja systemowa (realne uruchomienie `--version`, nie samo PATH); gdy jej brak — runtime
  python-build-standalone (CPython, licencja PSF) pobierany z GitHub z weryfikacją SHA-256 przypiętą w kodzie; gdy to nie działa —
  link do oficjalnej strony python.org i przycisk „Sprawdź ponownie” (bez udawania, że się udało).
- Pakiety: wyłącznie z pliku lock z sumami kontrolnymi (pip --require-hashes --only-binary), do venv kursu, przez interpreter venv.
- Instalacja działa w wątku roboczym; komunikaty idą kolejką do GUI (tkinter.after). Żadnych poleceń z paczki kursu.
- Testy końcowe uruchamiają prawdziwe procesy (pytest, lokalne API + żądanie HTTP, Selenium z przeglądarką) z limitem czasu
  i sprzątaniem procesów. „GOTOWE” pojawia się dopiero po przejściu testu, nie po samym imporcie biblioteki.
"""

import datetime as dt
import hashlib
import json
import os
import queue
import re
import shutil
import socket
import subprocess
import sys
import tarfile
import tempfile
import threading
import time
import urllib.error
import urllib.request
from pathlib import Path

from program import (KATALOG_DANYCH, KATALOG_LOGOW, KATALOG_POBRANE, KATALOG_PROGRAMOW, KATALOG_RUNTIME, KATALOG_SRODOWISK,
                     KATALOG_ZASOBOW, ZAMROZONY, katalog_kursu, katalog_materialow, meta_kursu)

WINDOWS = sys.platform.startswith("win")
GOTOWE, BRAK, ZLA_WERSJA, BLAD, OPCJONALNE, SPRAWDZANIE, NIE_SPRAWDZONO, POMINIETO = \
    "GOTOWE", "BRAK", "ZŁA WERSJA", "BŁĄD", "OPCJONALNE", "SPRAWDZANIE", "NIE SPRAWDZONO", "POMINIĘTO"

# Runtime Pythona, gdy w systemie nie ma zgodnej wersji: astral-sh/python-build-standalone (CPython, licencja PSF + licencje bibliotek
# w LICENSE.txt archiwum). Suma SHA-256 zweryfikowana 12.11.2026 z plikiem SHA256SUMS tego wydania; archiwum zawiera pip i venv.
RUNTIME = {
    "wersja": "3.12.12", "tag": "20251217",
    "plik": "cpython-3.12.12+20251217-x86_64-pc-windows-msvc-install_only.tar.gz",
    "sha256": "d1833b7d59a60e30ff44e80a5f2b9852d04b962425f91cf7f680cc9621c108b0",
    "rozmiar": 45_813_134, "rozpakowany_mb": 148,
    "url": "https://github.com/astral-sh/python-build-standalone/releases/download/20251217/cpython-3.12.12%2B20251217-x86_64-pc-windows-msvc-install_only.tar.gz",
    "zrodlo": "github.com/astral-sh/python-build-standalone (wydanie 20251217)", "licencja": "PSF License (CPython) — plik LICENSE.txt w archiwum",
    "strona_oficjalna": "https://www.python.org/downloads/windows/",
}
PYTHON_DOMYSLNY = ">=3.11,<3.14"
LIMIT_PIP_S = 20 * 60
LIMIT_POBIERANIA_S = 60
WERSJA_STANU = 1


# ============================================================ narzędzia procesów
def _flagi():
    f = {}
    if WINDOWS:
        f["creationflags"] = subprocess.CREATE_NO_WINDOW
    else:
        f["start_new_session"] = True
    return f


def _env_czysty(extra=None):
    """Środowisko dla procesów potomnych: bez zmiennych zapakowanego Pythona Mentora (PyInstaller ustawia TCL/TK_LIBRARY, _MEIPASS2…)."""
    env = dict(os.environ)
    for k in ("PYTHONHOME", "PYTHONPATH", "PYTHONSTARTUP", "PYTHONEXECUTABLE", "_MEIPASS2", "TCL_LIBRARY", "TK_LIBRARY", "PYTHONDONTWRITEBYTECODE"):
        env.pop(k, None)
    env["PYTHONIOENCODING"] = "utf-8"
    env["PYTHONUTF8"] = "1"
    env["PIP_DISABLE_PIP_VERSION_CHECK"] = "1"
    env["PIP_NO_INPUT"] = "1"
    if extra:
        env.update(extra)
    return env


def _zabij(proc):
    """Zatrzymuje proces i jego dzieci (serwer, przeglądarka, sterownik)."""
    try:
        if proc.poll() is not None:
            return
        if WINDOWS:
            subprocess.run(["taskkill", "/PID", str(proc.pid), "/T", "/F"], capture_output=True, timeout=15, **_flagi())
        else:
            import signal
            try:
                os.killpg(os.getpgid(proc.pid), signal.SIGTERM)
            except ProcessLookupError:
                pass
            try:
                proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                os.killpg(os.getpgid(proc.pid), signal.SIGKILL)
    except (OSError, subprocess.SubprocessError):
        pass
    try:
        proc.wait(timeout=5)
    except (OSError, subprocess.SubprocessError):
        pass


def uruchom(args, timeout=30, cwd=None, wejscie=None, env=None):
    """Uruchamia proces i zwraca (kod, stdout, stderr). Kod -1 = przekroczony czas, -2 = nie dało się uruchomić."""
    try:
        p = subprocess.Popen([str(a) for a in args], cwd=str(cwd) if cwd else None, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, env=_env_czysty(env), **_flagi())
    except OSError as e:
        return -2, "", str(e)
    try:
        out, err = p.communicate(input=(wejscie or "").encode("utf-8") if wejscie is not None else None, timeout=timeout)
    except subprocess.TimeoutExpired:
        _zabij(p)
        out, err = p.communicate()
        return -1, out.decode("utf-8", "replace"), err.decode("utf-8", "replace") + f"\n[przerwano po {timeout} s]"
    return p.returncode, out.decode("utf-8", "replace"), err.decode("utf-8", "replace")


def _log_plik(kurs_id):
    KATALOG_LOGOW.mkdir(parents=True, exist_ok=True)
    return KATALOG_LOGOW / f"srodowisko_{kurs_id}.log"


# ============================================================ wersje
def _wersja_tuple(s):
    m = re.match(r"(\d+)\.(\d+)(?:\.(\d+))?", str(s or ""))
    return (int(m.group(1)), int(m.group(2)), int(m.group(3) or 0)) if m else None


def wersja_spelnia(wersja, spec):
    """Prosty PEP 440 dla ograniczeń typu „>=3.11,<3.14” (porównania major.minor.micro)."""
    v = _wersja_tuple(wersja)
    if not v:
        return False
    for cz in str(spec or "").split(","):
        cz = cz.strip()
        if not cz:
            continue
        m = re.match(r"(>=|<=|==|!=|~=|>|<)\s*([0-9.]+)", cz)
        if not m:
            if re.fullmatch(r"[0-9]+(\.[0-9]+)*", cz):     # goły numer: „3.12” = ta sama linia major.minor
                g = _wersja_tuple(cz)
                if v[:len(g[:2])] != g[:2]:
                    return False
            continue
        op, w = m.group(1), _wersja_tuple(m.group(2))
        wn = w[:2] + (0,) if m.group(2).count(".") < 2 else w
        if op == ">=" and not v >= w: return False
        if op == ">" and not v > w: return False
        if op == "<=" and not v <= w: return False
        if op == "<" and not v < (w if m.group(2).count(".") >= 2 else w[:2] + (0,)): return False
        if op == "==" and not (v[:2] == w[:2] if m.group(2).count(".") < 2 else v == w): return False
        if op == "!=" and (v[:2] == w[:2] if m.group(2).count(".") < 2 else v == w): return False
        if op == "~=" and not (v[:2] == w[:2] and v >= wn): return False
    return True


# ============================================================ wykrywanie Pythona
def sprawdz_pythona(exe, timeout=25):
    """REALNE uruchomienie interpretera. Zwraca {exe, wersja, prefix, base_prefix, venv: bool} albo None."""
    exe = str(exe)
    if not exe or not Path(exe).exists():
        return None
    if "WindowsApps" in exe:     # stub ze Sklepu Windows otwiera Store zamiast uruchomić Pythona
        return None
    kod, out, _ = uruchom([exe, "-I", "-c", "import sys,json;print(json.dumps({'w':'%d.%d.%d'%sys.version_info[:3],'p':sys.prefix,'b':sys.base_prefix,'e':sys.executable}))"], timeout=timeout)
    if kod != 0:
        return None
    try:
        d = json.loads(out.strip().splitlines()[-1])
    except (ValueError, IndexError):
        return None
    return {"exe": d["e"] or exe, "wersja": d["w"], "prefix": d["p"], "base_prefix": d["b"], "venv": d["p"] != d["b"]}


def _kandydaci_pythona():
    k = []
    if WINDOWS:
        kod, out, _ = uruchom(["py", "-0p"], timeout=20)
        if kod == 0:
            for linia in out.splitlines():
                m = re.search(r"([A-Za-z]:\\.*python\.exe)", linia, re.I)
                if m:
                    k.append(m.group(1).strip())
        for nazwa in ("python", "python3"):
            w = shutil.which(nazwa)
            if w:
                k.append(w)
        for baza in (os.environ.get("LOCALAPPDATA", ""), os.environ.get("ProgramFiles", ""), os.environ.get("ProgramFiles(x86)", "")):
            if baza:
                k += [str(p) for p in Path(baza).glob("Programs/Python/Python3*/python.exe")] + [str(p) for p in Path(baza).glob("Python3*/python.exe")]
    else:
        for nazwa in ("python3", "python", "python3.13", "python3.12", "python3.11"):
            w = shutil.which(nazwa)
            if w:
                k.append(w)
    # runtime zarządzany przez Mentora
    for p in KATALOG_RUNTIME.glob("*/python/python.exe"):
        k.append(str(p))
    for p in KATALOG_RUNTIME.glob("*/python/bin/python3"):
        k.append(str(p))
    wynik, widziane = [], set()
    for x in k:
        try:
            r = str(Path(x).resolve())
        except OSError:
            continue
        if r in widziane:
            continue
        widziane.add(r)
        wynik.append(x)
    return wynik


def znajdz_pythony(spec=None, uwzglednij_mentora=False):
    """Lista realnie działających interpreterów (bez venv, bez Pythona zapakowanego w Mentor.exe), od najlepiej dopasowanego."""
    wynik = []
    wlasny = str(Path(sys.executable).resolve()) if ZAMROZONY else None
    for exe in _kandydaci_pythona():
        try:
            if wlasny and str(Path(exe).resolve()) == wlasny:
                continue
        except OSError:
            continue
        info = sprawdz_pythona(exe)
        if not info or info["venv"]:
            continue
        info["zarzadzany"] = str(KATALOG_RUNTIME) in str(Path(exe).resolve())
        info["pasuje"] = wersja_spelnia(info["wersja"], spec or PYTHON_DOMYSLNY)
        wynik.append(info)
    if not uwzglednij_mentora and not ZAMROZONY:
        pass
    wynik.sort(key=lambda i: (not i["pasuje"], i["zarzadzany"], tuple(-x for x in _wersja_tuple(i["wersja"]))))
    return wynik


# ============================================================ narzędzia, przeglądarki
def znajdz_narzedzie(nazwa):
    """{exe, wersja} dla git/claude/codex albo None — przez realne uruchomienie --version."""
    kandydaci = [shutil.which(nazwa)]
    dom = Path.home()
    if nazwa == "git" and WINDOWS:
        kandydaci += [str(p) for p in [Path(os.environ.get("ProgramFiles", "C:/Program Files")) / "Git" / "cmd" / "git.exe",
                                       dom / "AppData" / "Local" / "Programs" / "Git" / "cmd" / "git.exe"]]
    if nazwa == "claude":
        kandydaci += [str(dom / ".local" / "bin" / ("claude.exe" if WINDOWS else "claude")), str(dom / "AppData" / "Roaming" / "npm" / "claude.cmd")]
    for exe in kandydaci:
        if not exe or not Path(exe).exists():
            continue
        kod, out, err = uruchom([exe, "--version"], timeout=20)
        if kod == 0:
            m = re.search(r"(\d+\.\d+(?:\.\d+)?)", out + err)
            return {"exe": exe, "wersja": m.group(1) if m else (out or err).strip()[:30]}
    return None


def znajdz_przegladarke(preferowana="edge"):
    """{nazwa, exe, wersja} dla edge/chrome albo None. Windows: typowe katalogi instalacji; inne systemy: PATH."""
    kolejnosc = [preferowana] + [b for b in ("edge", "chrome") if b != preferowana]
    for b in kolejnosc:
        if WINDOWS:
            if b == "edge":
                sciezki = [Path(os.environ.get("ProgramFiles(x86)", "C:/Program Files (x86)")) / "Microsoft/Edge/Application/msedge.exe",
                           Path(os.environ.get("ProgramFiles", "C:/Program Files")) / "Microsoft/Edge/Application/msedge.exe",
                           Path(os.environ.get("LOCALAPPDATA", "")) / "Microsoft/Edge/Application/msedge.exe"]
            else:
                sciezki = [Path(os.environ.get("ProgramFiles", "C:/Program Files")) / "Google/Chrome/Application/chrome.exe",
                           Path(os.environ.get("ProgramFiles(x86)", "C:/Program Files (x86)")) / "Google/Chrome/Application/chrome.exe",
                           Path(os.environ.get("LOCALAPPDATA", "")) / "Google/Chrome/Application/chrome.exe"]
            for p in sciezki:
                if p.exists():
                    wersja = next((d.name for d in sorted(p.parent.iterdir(), reverse=True) if re.match(r"^\d+\.\d+\.\d+", d.name) and d.is_dir()), "")
                    return {"nazwa": b, "exe": str(p), "wersja": wersja}
        else:
            for n in (["microsoft-edge", "microsoft-edge-stable"] if b == "edge" else ["google-chrome", "chromium", "chromium-browser", "chrome"]):
                w = shutil.which(n)
                if w:
                    kod, out, _ = uruchom([w, "--version"], timeout=15)
                    m = re.search(r"(\d+\.\d+\.\d+)", out)
                    return {"nazwa": b, "exe": w, "wersja": m.group(1) if m else ""}
    if os.environ.get("MENTOR_PRZEGLADARKA") and Path(os.environ["MENTOR_PRZEGLADARKA"]).exists():
        return {"nazwa": preferowana, "exe": os.environ["MENTOR_PRZEGLADARKA"], "wersja": ""}
    return None


# ============================================================ pobieranie z weryfikacją
def pobierz(url, cel, sha256=None, rozmiar=None, postep=None, anuluj=None):
    """Pobiera do cel (najpierw cel.part), weryfikuje SHA-256. Rzuca RuntimeError z czytelnym opisem."""
    cel = Path(cel)
    cel.parent.mkdir(parents=True, exist_ok=True)
    if cel.exists() and sha256 and _sha256(cel) == sha256:
        return cel
    part = cel.with_suffix(cel.suffix + ".part")
    h = hashlib.sha256()
    pobrane = 0
    req = urllib.request.Request(url, headers={"User-Agent": "Mentor/2.7 (Windows; instalator srodowiska kursu)"})
    try:
        with urllib.request.urlopen(req, timeout=LIMIT_POBIERANIA_S) as r, open(part, "wb") as f:
            calk = rozmiar or int(r.headers.get("Content-Length") or 0)
            while True:
                if anuluj is not None and anuluj.is_set():
                    raise RuntimeError("Pobieranie anulowane.")
                b = r.read(1 << 16)
                if not b:
                    break
                f.write(b)
                h.update(b)
                pobrane += len(b)
                if postep:
                    postep(pobrane, calk)
    except urllib.error.URLError as e:
        part.unlink(missing_ok=True)
        raise RuntimeError(f"Brak połączenia lub serwer niedostępny ({getattr(e, 'reason', e)}). Sprawdź internet i kliknij „Ponów”.")
    except (socket.timeout, TimeoutError):
        part.unlink(missing_ok=True)
        raise RuntimeError("Pobieranie przerwane (przekroczony czas). Sprawdź połączenie i kliknij „Ponów”.")
    except OSError as e:
        part.unlink(missing_ok=True)
        if getattr(e, "errno", None) == 28 or "No space" in str(e):
            raise RuntimeError("Brak miejsca na dysku podczas pobierania.")
        raise RuntimeError(f"Nie udało się zapisać pobieranego pliku: {e}")
    if rozmiar and pobrane != rozmiar:
        part.unlink(missing_ok=True)
        raise RuntimeError(f"Pobrano {pobrane} B zamiast {rozmiar} B — pobieranie zerwane. Kliknij „Ponów”.")
    if sha256 and h.hexdigest() != sha256:
        part.unlink(missing_ok=True)
        raise RuntimeError("Suma kontrolna SHA-256 pobranego pliku NIE ZGADZA SIĘ z przypiętą w Mentorze — plik odrzucony. Spróbuj ponownie; jeśli błąd się powtarza, nie używaj tego pliku.")
    os.replace(part, cel)
    return cel


def _sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def wolne_miejsce_mb(katalog):
    try:
        return shutil.disk_usage(str(katalog)).free // (1024 * 1024)
    except OSError:
        return None


def jest_internet(timeout=5):
    for host in (("pypi.org", 443), ("github.com", 443)):
        try:
            with socket.create_connection(host, timeout=timeout):
                return True
        except OSError:
            continue
    return False


# ============================================================ lock
WZORZEC_LOCK = re.compile(r"^([A-Za-z0-9][A-Za-z0-9._-]*)(\[[A-Za-z0-9,._-]*\])?==([A-Za-z0-9.!+*-]+)\s*(;[^\\]*)?\s*(\\)?\s*$")


def sprawdz_lock(tekst):
    """Lock dopuszczamy tylko w postaci: `nazwa==wersja [; marker] \\` + linie `--hash=sha256:...`. Zwraca (pakiety, bledy)."""
    pakiety, bledy, biezacy = [], [], None
    for nr, linia in enumerate(tekst.splitlines(), 1):
        s = linia.strip()
        if not s or s.startswith("#"):
            continue
        if s.startswith("--hash=sha256:"):
            if biezacy is None:
                bledy.append(f"linia {nr}: hash bez pakietu")
            elif not re.match(r"^--hash=sha256:[0-9a-f]{64}\s*(\\)?$", s):
                bledy.append(f"linia {nr}: zły format hasha")
            else:
                biezacy["hashe"] += 1
            continue
        m = WZORZEC_LOCK.match(s)
        if not m:
            bledy.append(f"linia {nr}: niedozwolona składnia (dozwolone tylko nazwa==wersja; marker; --hash): {s[:50]}")
            biezacy = None
            continue
        biezacy = {"nazwa": m.group(1).lower().replace("_", "-"), "wersja": m.group(3), "marker": (m.group(4) or "").strip("; ").strip(), "hashe": 0}
        pakiety.append(biezacy)
    for p in pakiety:
        if p["hashe"] == 0:
            bledy.append(f"pakiet {p['nazwa']} bez --hash")
    return pakiety, bledy


def sciezka_locka_mentora():
    for k in (KATALOG_PROGRAMOW / "zaleznosci" / "requirements.lock", KATALOG_ZASOBOW / "programy" / "zaleznosci" / "requirements.lock",
              Path(__file__).resolve().parent / "programy" / "zaleznosci" / "requirements.lock"):
        if k.exists():
            return k
    return None


def katalog_testow():
    for k in (KATALOG_ZASOBOW / "srodowisko_testy", Path(__file__).resolve().parent / "srodowisko_testy"):
        if k.is_dir():
            return k
    return None


# ============================================================ środowisko kursu
class Srodowisko:
    """Środowisko jednego kursu: katalog, venv, wymagania, stan, diagnoza, plan instalacji, instalacja, testy."""

    def __init__(self, kurs_id, wymagania=None, katalog_kursu_=None):
        self.id = kurs_id
        self.wym = wymagania or {}
        self.katalog_kursu = Path(katalog_kursu_) if katalog_kursu_ else katalog_kursu(kurs_id)
        self.katalog = KATALOG_SRODOWISK / kurs_id
        self.venv = self.katalog / ".venv"
        self.plik_stanu = self.katalog / "stan.json"
        self.log = _log_plik(kurs_id)

    # --- stan -------------------------------------------------------------
    def stan(self):
        try:
            return json.loads(self.plik_stanu.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return {}

    def zapisz_stan(self, **zmiany):
        s = self.stan()
        s.update(zmiany)
        s["wersja_stanu"] = WERSJA_STANU
        s["zapis"] = dt.datetime.now().isoformat(timespec="seconds")
        self.katalog.mkdir(parents=True, exist_ok=True)
        self.plik_stanu.write_text(json.dumps(s, ensure_ascii=False, indent=1), encoding="utf-8")

    def loguj(self, tekst):
        try:
            with open(self.log, "a", encoding="utf-8") as f:
                f.write(f"[{dt.datetime.now():%Y-%m-%d %H:%M:%S}] {tekst.rstrip()}\n")
        except OSError:
            pass

    # --- wymagania ------------------------------------------------------
    def wymaga_srodowiska(self):
        w = self.wym
        return bool(w.get("python") or w.get("pakiety") or w.get("narzedzia_wymagane") or w.get("przegladarka"))

    def spec_pythona(self):
        return self.wym.get("python") or (PYTHON_DOMYSLNY if self.wym.get("pakiety") else None)

    def pakiety_wymagane(self):
        return [p["nazwa"] if isinstance(p, dict) else str(p) for p in self.wym.get("pakiety", [])]

    def modul(self, pakiet):
        return {"pyyaml": "yaml", "beautifulsoup4": "bs4", "pillow": "PIL", "scikit-learn": "sklearn"}.get(pakiet, pakiet.replace("-", "_"))

    def plik_lock(self):
        """(ścieżka, źródło) locka z hashami: lock paczki (po walidacji składni) albo lock Mentora dla zaufanych pakietów."""
        w = self.wym
        if w.get("lock") and self.katalog_kursu:
            kand = self.katalog_kursu / "paczka" / w["lock"]
            if kand.exists():
                pak, bledy = sprawdz_lock(kand.read_text(encoding="utf-8", errors="replace"))
                if not bledy and pak:
                    return kand, "lock paczki kursu"
                self.loguj("lock paczki odrzucony: " + "; ".join(bledy[:5]))
        if set(self.pakiety_wymagane()) - set(p for p in self.pakiety_wymagane() if p in ("pytest", "requests", "selenium", "flask")):
            pass   # pakiety spoza zaufanej listy nie zostaną zainstalowane (raportujemy w diagnozie)
        lm = sciezka_locka_mentora()
        if lm and self.pakiety_wymagane():
            return lm, "lock Mentora (zaufane pakiety)"
        return None, None

    def lock_sha(self):
        p, _ = self.plik_lock()
        return _sha256(p) if p else None

    def python_venv(self):
        p = self.venv / ("Scripts/python.exe" if WINDOWS else "bin/python")
        return p if p.exists() else None

    # --- diagnoza (nic nie instaluje) ----------------------------------------
    def diagnoza(self, biezacy_tydzien=None):
        """Lista pozycji: {klucz, nazwa, status, szczegoly, wymagane, akcja}. Statusy wynikają z realnych uruchomień."""
        poz = []
        st = self.stan()
        w = self.wym
        if biezacy_tydzien is None:
            biezacy_tydzien = st.get("tydzien", 0)     # ostatni znany tydzień ucznia (GUI podaje go zawsze)
        if not self.wymaga_srodowiska():
            poz.append({"klucz": "mentor", "nazwa": "Narzędzia kursu", "status": GOTOWE, "szczegoly": "Kurs działa w samym Mentorze — nie wymaga Pythona, bibliotek ani innych programów.", "wymagane": False})
            self._pozycje_materialow(poz)
            return poz
        spec = self.spec_pythona()
        pyth = znajdz_pythony(spec)
        pasujace = [p for p in pyth if p["pasuje"]]
        if pasujace:
            p = pasujace[0]
            poz.append({"klucz": "python", "nazwa": f"Python {p['wersja']}" + (" (zarządzany przez Mentora)" if p["zarzadzany"] else " (zainstalowany w systemie)"),
                        "status": GOTOWE, "szczegoly": p["exe"], "wymagane": True})
        elif pyth:
            poz.append({"klucz": "python", "nazwa": "Python", "status": ZLA_WERSJA,
                        "szczegoly": f"Znaleziono {', '.join(p['wersja'] for p in pyth[:3])}, a kurs wymaga {spec}. Mentor może pobrać Python {RUNTIME['wersja']} tylko dla tego kursu.", "wymagane": True, "akcja": "python"})
        else:
            poz.append({"klucz": "python", "nazwa": "Python", "status": BRAK, "szczegoly": f"Nie znaleziono działającego Pythona ({spec}). Mentor może pobrać Python {RUNTIME['wersja']} do swojego katalogu (bez uprawnień administratora).", "wymagane": True, "akcja": "python"})
        pv = self.python_venv()
        info_venv = sprawdz_pythona(pv) if pv else None
        if info_venv:
            poz.append({"klucz": "venv", "nazwa": "Środowisko kursu (.venv)", "status": GOTOWE, "szczegoly": f"{self.venv} · Python {info_venv['wersja']}", "wymagane": True})
        elif pv:
            poz.append({"klucz": "venv", "nazwa": "Środowisko kursu (.venv)", "status": BLAD, "szczegoly": "Katalog .venv istnieje, ale interpreter nie uruchamia się — użyj „Napraw środowisko”.", "wymagane": True, "akcja": "venv"})
        else:
            poz.append({"klucz": "venv", "nazwa": "Środowisko kursu (.venv)", "status": BRAK, "szczegoly": f"Zostanie utworzone w {self.venv}", "wymagane": True, "akcja": "venv"})
        # pakiety — realny import w venv
        wersje = {}
        if info_venv and self.pakiety_wymagane():
            wersje = self.wersje_pakietow()
        for pak in self.pakiety_wymagane():
            mod = self.modul(pak)
            wymag = {x["nazwa"]: x for x in w.get("pakiety", []) if isinstance(x, dict)}.get(pak, {})
            if not info_venv:
                poz.append({"klucz": f"pakiet:{pak}", "nazwa": pak, "status": BRAK, "szczegoly": "Najpierw środowisko .venv", "wymagane": True, "akcja": "pakiety"})
            elif wersje.get(mod):
                if wymag.get("wersja") and wymag["wersja"] != wersje[mod]:
                    poz.append({"klucz": f"pakiet:{pak}", "nazwa": pak, "status": ZLA_WERSJA, "szczegoly": f"jest {wersje[mod]}, kurs wymaga {wymag['wersja']}", "wymagane": True, "akcja": "pakiety"})
                else:
                    poz.append({"klucz": f"pakiet:{pak}", "nazwa": pak, "status": GOTOWE, "szczegoly": f"wersja {wersje[mod]} w środowisku kursu", "wymagane": True})
            else:
                poz.append({"klucz": f"pakiet:{pak}", "nazwa": pak, "status": BRAK, "szczegoly": "brak w środowisku kursu" + (" — pakiet spoza zaufanej listy, bez locka z hashami: instalacja ręczna" if pak in self.wym.get("nieobslugiwane", []) else ""),
                            "wymagane": pak not in self.wym.get("nieobslugiwane", []), "akcja": "pakiety"})
        # narzędzia
        for n in w.get("narzedzia_wymagane", []):
            t = znajdz_narzedzie(n)
            poz.append({"klucz": f"narzedzie:{n}", "nazwa": n, "status": GOTOWE if t else BRAK, "szczegoly": (f"{t['exe']} · {t['wersja']}" if t else "nie znaleziono — Mentor nie instaluje tego narzędzia automatycznie"), "wymagane": True})
        for n in w.get("narzedzia_opcjonalne", []):
            nazwa, od = (n["nazwa"], n.get("od_tygodnia")) if isinstance(n, dict) else (n, None)
            t = znajdz_narzedzie(nazwa)
            potrzebne_teraz = od is not None and biezacy_tydzien is not None and biezacy_tydzien >= od
            etykieta = {"git": "Git", "claude": "Claude Code", "codex": "Codex"}.get(nazwa, nazwa) + (f" (od tygodnia {od})" if od is not None else "")
            if t:
                poz.append({"klucz": f"narzedzie:{nazwa}", "nazwa": etykieta, "status": GOTOWE, "szczegoly": f"{t['exe']} · {t['wersja']}", "wymagane": False})
            else:
                poz.append({"klucz": f"narzedzie:{nazwa}", "nazwa": etykieta, "status": BRAK if potrzebne_teraz else OPCJONALNE,
                            "szczegoly": ("potrzebne w tym tygodniu — " if potrzebne_teraz else "opcjonalne teraz — ") + {"git": "oficjalny instalator: https://git-scm.com/download/win (domyślne ustawienia)",
                                                                                                                      "claude": "instalacja wg docs.claude.com (wymaga subskrypcji); Asystent offline/API działa bez niego",
                                                                                                                      "codex": "instalacja wg dokumentacji OpenAI"}.get(nazwa, "zainstaluj wg dokumentacji narzędzia"), "wymagane": False})
        # przeglądarka
        if w.get("przegladarka"):
            b = znajdz_przegladarke(w["przegladarka"])
            od = w.get("przegladarka_od_tygodnia")
            potrzebna_teraz = od is None or biezacy_tydzien is None or biezacy_tydzien >= od
            nazwa_p = {"edge": "Microsoft Edge", "chrome": "Google Chrome"}.get(w["przegladarka"], w["przegladarka"]) + (f" (Selenium od tygodnia {od})" if od is not None else "")
            if b:
                poz.append({"klucz": "przegladarka", "nazwa": {"edge": "Microsoft Edge", "chrome": "Google Chrome"}.get(b["nazwa"], b["nazwa"]), "status": GOTOWE, "szczegoly": f"{b['exe']}" + (f" · {b['wersja']}" if b["wersja"] else ""), "wymagane": True})
            else:
                poz.append({"klucz": "przegladarka", "nazwa": nazwa_p, "status": BRAK if potrzebna_teraz else OPCJONALNE,
                            "szczegoly": ("" if potrzebna_teraz else "jeszcze niepotrzebna — ") + "nie znaleziono — Windows 10/11 ma Edge wbudowany; jeśli go usunięto: https://www.microsoft.com/edge (Mentor nie instaluje przeglądarek)",
                            "wymagane": potrzebna_teraz})
        self._pozycje_materialow(poz)
        # wyniki testów z ostatniego przebiegu
        testy = st.get("testy", {})
        niewazne = st.get("lock_sha") != self.lock_sha() or st.get("kurs_wersja") != (meta_kursu(self.id).get("wersja") if meta_kursu(self.id) else self.wym.get("_wersja"))
        for tid, nazwa in self.lista_testow():
            t = testy.get(tid)
            if t and not niewazne:
                poz.append({"klucz": f"test:{tid}", "nazwa": f"Test: {nazwa}", "status": t["status"], "szczegoly": f"{t.get('szczegoly', '')} ({t.get('data', '')[:16]})", "wymagane": tid != "selenium"})
            else:
                poz.append({"klucz": f"test:{tid}", "nazwa": f"Test: {nazwa}", "status": NIE_SPRAWDZONO, "szczegoly": "zmiana kursu lub bibliotek — uruchom „Sprawdź działanie”" if (t and niewazne) else "uruchom „Sprawdź działanie” po instalacji", "wymagane": tid != "selenium", "akcja": "testy"})
        return poz

    def _pozycje_materialow(self, poz):
        mat = katalog_materialow(self.id)
        for c in self.wym.get("sprawdzenia", []):
            if c.get("kind") == "file_exists" and c.get("path"):
                sc = (mat / c["path"]) if mat else None
                ok = bool(sc and sc.exists())
                poz.append({"klucz": f"plik:{c['path']}", "nazwa": f"Plik kursu: {c['path']}", "status": GOTOWE if ok else BRAK, "szczegoly": str(sc) if ok else "brak w materiałach kursu — zaimportuj paczkę ponownie", "wymagane": True})
        if mat:
            poz.append({"klucz": "materialy", "nazwa": "Materiały kursu", "status": GOTOWE, "szczegoly": str(mat), "wymagane": False})

    def lista_testow(self):
        if not self.wymaga_srodowiska():
            return []
        t = [("python", "interpreter kursu"), ("importy", "import bibliotek"), ("pytest", "pytest (przykładowy test)")]
        pak = set(self.pakiety_wymagane())
        if "requests" in pak or "flask" in pak:
            t.append(("api", "lokalne API + żądanie HTTP"))
        if "selenium" in pak or self.wym.get("przegladarka"):
            t.append(("selenium", "Selenium + przeglądarka"))
        return t

    def wersje_pakietow(self):
        pv = self.python_venv()
        kt = katalog_testow()
        if not pv or not kt:
            return {}
        mods = [self.modul(p) for p in self.pakiety_wymagane()]
        kod, out, _ = uruchom([pv, "-I", str(kt / "probe_pakiety.py"), *mods], timeout=60)
        if kod != 0:
            return {}
        try:
            return {k: v for k, v in json.loads(out.strip().splitlines()[-1]).items() if v}
        except (ValueError, IndexError):
            return {}

    def gotowe(self):
        """True, gdy wszystkie wymagane pozycje (poza testami opcjonalnymi) są GOTOWE wg ostatniej diagnozy zapisanej w stanie."""
        s = self.stan()
        return bool(s.get("gotowe")) and s.get("lock_sha") == self.lock_sha()

    # --- plan instalacji -----------------------------------------------------
    def plan(self, diagnoza=None):
        """Kroki do wykonania: [{id, opis, zrodlo, rozmiar, internet, uprawnienia}] — pokazywane uczniowi PRZED zgodą."""
        d = diagnoza or self.diagnoza()
        st = {p["klucz"]: p for p in d}
        kroki = []
        if not self.wymaga_srodowiska():
            return kroki
        if st.get("python", {}).get("status") in (BRAK, ZLA_WERSJA):
            if WINDOWS:
                kroki.append({"id": "python", "opis": f"Pobranie Pythona {RUNTIME['wersja']} tylko dla kursów Mentora (do {KATALOG_RUNTIME})",
                              "zrodlo": RUNTIME["zrodlo"] + " · " + RUNTIME["licencja"], "rozmiar": f"{RUNTIME['rozmiar'] / 1e6:.1f} MB do pobrania, ok. {RUNTIME['rozpakowany_mb']} MB na dysku",
                              "internet": True, "uprawnienia": "brak (katalog użytkownika)", "sha256": RUNTIME["sha256"]})
            else:
                kroki.append({"id": "python_recznie", "opis": "Zainstaluj Pythona 3.11–3.13 menedżerem pakietów systemu (np. apt install python3) i kliknij „Sprawdź ponownie”.",
                              "zrodlo": "system", "rozmiar": "—", "internet": True, "uprawnienia": "zależnie od systemu"})
        if st.get("venv", {}).get("status") != GOTOWE:
            kroki.append({"id": "venv", "opis": f"Utworzenie osobnego środowiska Pythona dla kursu: {self.venv}", "zrodlo": "python -m venv (wbudowane)", "rozmiar": "ok. 15 MB", "internet": False, "uprawnienia": "brak"})
        brak_pak = [p for p in self.pakiety_wymagane() if st.get(f"pakiet:{p}", {}).get("status") in (BRAK, ZLA_WERSJA) and p not in self.wym.get("nieobslugiwane", [])]
        if brak_pak or st.get("venv", {}).get("status") != GOTOWE:
            lock, zr = self.plik_lock()
            if lock:
                pak, _ = sprawdz_lock(lock.read_text(encoding="utf-8", errors="replace"))
                glowne = [f"{p['nazwa']} {p['wersja']}" for p in pak if p["nazwa"] in self.pakiety_wymagane()]
                kroki.append({"id": "pakiety", "opis": "Instalacja bibliotek do środowiska kursu: " + ", ".join(glowne) + f" (+ {len(pak) - len(glowne)} zależności)",
                              "zrodlo": f"PyPI (pypi.org), {zr}: {len(pak)} pakietów z sumami SHA-256, tylko gotowe pliki wheel", "rozmiar": "ok. 15–25 MB", "internet": True, "uprawnienia": "brak"})
        if self.wym.get("nieobslugiwane"):
            kroki.append({"id": "info_nieobslugiwane", "opis": "Pakiety spoza zaufanej listy (" + ", ".join(self.wym["nieobslugiwane"]) + ") NIE zostaną zainstalowane automatycznie — paczka musi mieć requirements.lock z hashami.",
                          "zrodlo": "—", "rozmiar": "—", "internet": False, "uprawnienia": "—"})
        if st.get("przegladarka", {}).get("status") == BRAK:
            kroki.append({"id": "info_przegladarka", "opis": "Przeglądarka nie została znaleziona — Mentor nie instaluje przeglądarek; zainstaluj Edge/Chrome z oficjalnej strony i kliknij „Sprawdź ponownie”.",
                          "zrodlo": "https://www.microsoft.com/edge", "rozmiar": "—", "internet": True, "uprawnienia": "instalator producenta"})
        testy = [n for _, n in self.lista_testow()]
        if testy:
            kroki.append({"id": "testy", "opis": "Testy końcowe: " + ", ".join(testy) + (". Selenium przy pierwszym uruchomieniu pobiera sterownik przeglądarki (Selenium Manager, ok. 10 MB)." if any(t == "selenium" for t, _ in self.lista_testow()) else "."),
                          "zrodlo": "procesy lokalne w środowisku kursu" + (" + msedgedriver z serwerów Microsoft" if any(t == "selenium" for t, _ in self.lista_testow()) else ""), "rozmiar": "—", "internet": any(t == "selenium" for t, _ in self.lista_testow()), "uprawnienia": "brak"})
        return kroki

    # --- instalacja (w wątku roboczym) ----------------------------------------
    def instaluj(self, kroki_id, kolejka, anuluj, tydzien=None):
        """Wykonuje kroki planu; komunikaty: ("log", txt) ("krok", id, status, txt) ("postep", id, ulamek, txt) ("koniec", wynik)."""
        def log(t):
            self.loguj(t)
            kolejka.put(("log", t))

        def krok(i, status, txt=""):
            kolejka.put(("krok", i, status, txt))

        wynik = {"ok": False, "bledy": [], "kroki": {}}
        try:
            self.katalog.mkdir(parents=True, exist_ok=True)
            log(f"=== Instalacja środowiska kursu „{self.id}” — {dt.datetime.now():%Y-%m-%d %H:%M} ===")
            if any(k in ("python", "pakiety") for k in kroki_id):
                log("Sprawdzam połączenie z internetem…")
                if not jest_internet():
                    raise RuntimeError("Brak połączenia z internetem — pobranie Pythona/bibliotek jest niemożliwe. Lekcje i materiały offline działają; instalację ponów po podłączeniu sieci.")
            wolne = wolne_miejsce_mb(KATALOG_DANYCH)
            if wolne is not None and wolne < 400:
                raise RuntimeError(f"Za mało miejsca na dysku ({wolne} MB wolne; potrzeba ok. 400 MB).")
            python_exe = None
            if "python" in kroki_id:
                krok("python", SPRAWDZANIE)
                python_exe = self._zainstaluj_runtime(kolejka, anuluj, log)
                krok("python", GOTOWE, python_exe)
                wynik["kroki"]["python"] = python_exe
            if anuluj.is_set():
                raise RuntimeError("Anulowano.")
            if "venv" in kroki_id:
                krok("venv", SPRAWDZANIE)
                self._utworz_venv(python_exe, log)
                krok("venv", GOTOWE, str(self.venv))
                wynik["kroki"]["venv"] = str(self.venv)
            if anuluj.is_set():
                raise RuntimeError("Anulowano.")
            if "pakiety" in kroki_id:
                krok("pakiety", SPRAWDZANIE)
                self._zainstaluj_pakiety(kolejka, anuluj, log)
                krok("pakiety", GOTOWE)
                wynik["kroki"]["pakiety"] = True
            if "testy" in kroki_id:
                krok("testy", SPRAWDZANIE)
                wyniki = self.testy(kolejka, anuluj, log, odswiez_stan=False)
                wynik["testy"] = wyniki
                krok("testy", GOTOWE if all(t["status"] in (GOTOWE, POMINIETO) for t in wyniki.values() if t["id"] != "selenium") else BLAD)
            self._odswiez_stan(tydzien)
            wynik["ok"] = True
            log("=== Zakończono ===")
        except RuntimeError as e:
            wynik["bledy"].append(str(e))
            log("BŁĄD: " + str(e))
            self._odswiez_stan(tydzien)
        except Exception as e:  # noqa: BLE001 — wątek roboczy nie może umrzeć po cichu
            wynik["bledy"].append(f"Nieoczekiwany błąd: {type(e).__name__}: {e}")
            log(f"BŁĄD: {type(e).__name__}: {e}")
        kolejka.put(("koniec", wynik))
        return wynik

    def _odswiez_stan(self, tydzien=None):
        d = self.diagnoza(tydzien)
        wymagane = [p for p in d if p.get("wymagane") and not p["klucz"].startswith("test:")]
        testy_wym = [p for p in d if p["klucz"].startswith("test:") and p.get("wymagane")]
        gotowe = bool(wymagane) and all(p["status"] == GOTOWE for p in wymagane) and all(p["status"] == GOTOWE for p in testy_wym)
        py = next((p for p in d if p["klucz"] == "python" and p["status"] == GOTOWE), None)
        self.zapisz_stan(gotowe=gotowe, diagnoza=d, lock_sha=self.lock_sha(), kurs_wersja=(meta_kursu(self.id).get("wersja") if meta_kursu(self.id) else self.wym.get("_wersja")),
                         python_venv=str(self.python_venv() or ""), python_bazowy=(py["szczegoly"] if py else ""),
                         tydzien=(tydzien if tydzien is not None else self.stan().get("tydzien", 0)),
                         wersje=self.wersje_pakietow() if self.python_venv() else {})
        return d

    def _zainstaluj_runtime(self, kolejka, anuluj, log):
        if not WINDOWS:
            raise RuntimeError("Automatyczne pobranie Pythona jest dostępne tylko w Windows. Zainstaluj Pythona 3.11–3.13 narzędziami systemu i kliknij „Sprawdź ponownie”.")
        cel_tar = KATALOG_POBRANE / RUNTIME["plik"]
        log(f"Pobieram {RUNTIME['plik']} ({RUNTIME['rozmiar'] / 1e6:.1f} MB) z {RUNTIME['url']}")

        def postep(p, calk):
            kolejka.put(("postep", "python", (p / calk) if calk else 0, f"pobrano {p / 1e6:.1f} / {(calk or RUNTIME['rozmiar']) / 1e6:.1f} MB"))
        pobierz(RUNTIME["url"], cel_tar, RUNTIME["sha256"], RUNTIME["rozmiar"], postep, anuluj)
        log("Suma SHA-256 zgodna z przypiętą w Mentorze. Rozpakowuję…")
        cel = KATALOG_RUNTIME / f"cpython-{RUNTIME['wersja']}"
        tmp = KATALOG_RUNTIME / f"_tmp-{RUNTIME['wersja']}"
        shutil.rmtree(tmp, ignore_errors=True)
        tmp.mkdir(parents=True)
        with tarfile.open(cel_tar) as t:
            czl = t.getmembers()
            baza = tmp.resolve()
            for i, m in enumerate(czl):
                if anuluj.is_set():
                    raise RuntimeError("Anulowano.")
                if m.issym() or m.islnk() or m.name.startswith("/") or ".." in Path(m.name).parts:
                    continue
                if not str((baza / m.name).resolve()).startswith(str(baza)):
                    continue
                try:
                    t.extract(m, tmp, filter="data")     # Python ≥3.12: bezpieczny filtr (bez uprawnień specjalnych, bez wyjścia poza katalog)
                except TypeError:
                    t.extract(m, tmp)
                if i % 400 == 0:
                    kolejka.put(("postep", "python", i / len(czl), f"rozpakowano {i}/{len(czl)} plików"))
        if cel.exists():
            shutil.rmtree(cel, ignore_errors=True)
        os.replace(tmp, cel)
        exe = cel / "python" / "python.exe"
        info = sprawdz_pythona(exe)
        if not info:
            raise RuntimeError("Pobrany Python nie uruchamia się — usuń katalog runtime i spróbuj ponownie.")
        log(f"Python {info['wersja']} działa: {exe}")
        return str(exe)

    def _utworz_venv(self, python_exe, log):
        if not python_exe:
            pyth = [p for p in znajdz_pythony(self.spec_pythona()) if p["pasuje"]]
            if not pyth:
                raise RuntimeError("Brak zgodnego Pythona do utworzenia środowiska — najpierw krok „Python”.")
            python_exe = pyth[0]["exe"]
        if self.python_venv() and sprawdz_pythona(self.python_venv()):
            log(f"Środowisko {self.venv} już istnieje — zostawiam.")
            return
        if self.venv.exists():
            log("Uszkodzone .venv — usuwam i tworzę od nowa.")
            shutil.rmtree(self.venv, ignore_errors=True)
        log(f"Tworzę środowisko: {python_exe} -m venv {self.venv}")
        kod, out, err = uruchom([python_exe, "-m", "venv", str(self.venv)], timeout=240)
        if kod != 0 or not self.python_venv():
            raise RuntimeError("Nie udało się utworzyć .venv: " + (err or out).strip()[-400:])
        pv = self.python_venv()
        kod, out, err = uruchom([pv, "-m", "pip", "--version"], timeout=60)
        if kod != 0:
            log("pip nie działa w nowym środowisku — próbuję ensurepip…")
            kod, out, err = uruchom([pv, "-m", "ensurepip", "--upgrade"], timeout=240)
            if kod != 0:
                raise RuntimeError("Brak pip w środowisku i ensurepip nie zadziałał: " + (err or out).strip()[-300:])
        log("Środowisko utworzone, pip: " + out.strip().splitlines()[-1][:80] if out.strip() else "Środowisko utworzone.")

    def _zainstaluj_pakiety(self, kolejka, anuluj, log):
        pv = self.python_venv()
        if not pv:
            raise RuntimeError("Brak środowiska .venv — najpierw krok „Środowisko”.")
        lock, zr = self.plik_lock()
        if not lock:
            raise RuntimeError("Brak pliku lock z sumami kontrolnymi dla tego kursu — Mentor nie instaluje pakietów bez niego.")
        pak, bledy = sprawdz_lock(lock.read_text(encoding="utf-8", errors="replace"))
        if bledy:
            raise RuntimeError("Lock odrzucony: " + "; ".join(bledy[:3]))
        log(f"pip install --require-hashes -r {lock} ({zr}, {len(pak)} pakietów)")
        args = [str(pv), "-m", "pip", "install", "--require-hashes", "--only-binary=:all:", "--no-input", "--disable-pip-version-check",
                "--progress-bar", "off", "--timeout", "30", "--retries", "3", "-r", str(lock)]
        try:
            p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding="utf-8", errors="replace", env=_env_czysty(), **_flagi())
        except OSError as e:
            raise RuntimeError(f"Nie udało się uruchomić pip: {e}")
        start = time.time()
        ostatnie = []
        linie = queue.Queue()

        def czytaj():      # osobny wątek czyta wyjście pip, żeby „Anuluj” i limit czasu działały także, gdy pip milczy (zawieszone pobieranie)
            for l in p.stdout:
                linie.put(l)
            linie.put(None)
        threading.Thread(target=czytaj, daemon=True).start()
        koniec_wyjscia = False
        while True:
            try:
                linia = linie.get(timeout=0.25)
            except queue.Empty:
                linia = ""
            if linia is None:
                koniec_wyjscia = True
                linia = ""
            if koniec_wyjscia and p.poll() is not None:
                break
            if linia:
                log("pip: " + linia.rstrip())
                ostatnie = (ostatnie + [linia.strip()])[-12:]
                m = re.search(r"Collecting (\S+)|Downloading (\S+)|Installing collected packages", linia)
                if m:
                    kolejka.put(("postep", "pakiety", None, linia.strip()[:90]))
            if anuluj.is_set():
                _zabij(p)
                raise RuntimeError("Anulowano instalację pakietów — środowisko zostaje w stanie częściowym; „Ponów” dokończy.")
            if time.time() - start > LIMIT_PIP_S:
                _zabij(p)
                raise RuntimeError("Instalacja pakietów trwała za długo (limit 20 min) — sprawdź połączenie i kliknij „Ponów”.")
        if p.returncode != 0:
            tekst = "\n".join(ostatnie)
            if "THESE PACKAGES DO NOT MATCH THE HASHES" in tekst or ("hash" in tekst.lower() and "mismatch" in tekst.lower()):
                m = re.search(r"\n\s*([A-Za-z0-9_.-]+==[0-9][^\s]*) from", tekst)
                raise RuntimeError(f"Pobrany plik pakietu {m.group(1) if m else ''} nie ma sumy SHA-256 z pliku lock — instalacja przerwana, nic nie zainstalowano z tego pakietu. "
                                   "Najczęstsza przyczyna: inna wersja Pythona lub systemu niż te, dla których przygotowano lock (3.11–3.13, Windows x64). "
                                   "Jeśli Python jest zgodny, a błąd się powtarza — nie używaj tego pakietu i zgłoś problem autorowi kursu.")
            if "No matching distribution" in tekst:
                raise RuntimeError("Brak gotowego pakietu (wheel) dla tej wersji Pythona — użyj Pythona 3.11–3.13 (Mentor może pobrać 3.12).\n" + tekst[-400:])
            if "Could not find a version" in tekst or "Connection" in tekst or "Temporary failure" in tekst or "timed out" in tekst.lower():
                raise RuntimeError("Problem z połączeniem podczas pobierania pakietów — kliknij „Ponów”.\n" + tekst[-400:])
            if "No space left" in tekst or "Errno 28" in tekst:
                raise RuntimeError("Brak miejsca na dysku podczas instalacji pakietów.")
            raise RuntimeError("pip zakończył się błędem:\n" + tekst[-600:])
        log("Pakiety zainstalowane.")

    # --- testy powdrożeniowe ---------------------------------------------------
    def testy(self, kolejka=None, anuluj=None, log=None, odswiez_stan=True):
        """Uruchamia wszystkie testy kursu; zapisuje wyniki (z datą i wersjami) i zwraca {id: wynik}."""
        log = log or self.loguj
        kt = katalog_testow()
        wyniki = {}
        pv = self.python_venv()
        for tid, nazwa in self.lista_testow():
            if _anulowano(anuluj):
                break
            if kolejka:
                kolejka.put(("postep", "testy", None, f"test: {nazwa}"))
            start = time.time()
            try:
                if not pv:
                    raise RuntimeError("brak środowiska .venv")
                if not kt:
                    raise RuntimeError("brak katalogu skryptów testowych Mentora (srodowisko_testy)")
                szcz = getattr(self, f"_test_{tid}")(pv, kt, log)
                status = GOTOWE
            except TestPominiety as e:
                szcz, status = str(e), POMINIETO
            except RuntimeError as e:
                szcz, status = str(e), BLAD
            except Exception as e:  # noqa: BLE001
                szcz, status = f"{type(e).__name__}: {e}", BLAD
            wyniki[tid] = {"id": tid, "nazwa": nazwa, "status": status, "szczegoly": szcz[:600], "czas_s": round(time.time() - start, 1),
                           "data": dt.datetime.now().isoformat(timespec="seconds")}
            log(f"TEST {nazwa}: {status} — {szcz[:200]}")
            if kolejka:
                kolejka.put(("test", tid, status, szcz[:200]))
        s = self.stan()
        s.setdefault("testy", {}).update(wyniki)
        self.zapisz_stan(testy=s["testy"], wersje=self.wersje_pakietow() if pv else {}, lock_sha=self.lock_sha(),
                         kurs_wersja=(meta_kursu(self.id).get("wersja") if meta_kursu(self.id) else self.wym.get("_wersja")))
        if odswiez_stan:
            self._odswiez_stan()     # „gotowe” wynika z diagnozy + wyników testów — nigdy z samego przebiegu instalacji
        return wyniki

    def _test_python(self, pv, kt, log):
        info = sprawdz_pythona(pv)
        if not info:
            raise RuntimeError("interpreter środowiska nie uruchamia się")
        if self.spec_pythona() and not wersja_spelnia(info["wersja"], self.spec_pythona()):
            raise RuntimeError(f"Python {info['wersja']} nie spełnia {self.spec_pythona()}")
        return f"Python {info['wersja']} ({pv})"

    def _test_importy(self, pv, kt, log):
        w = self.wersje_pakietow()
        brak = [p for p in self.pakiety_wymagane() if not w.get(self.modul(p))]
        if brak:
            raise RuntimeError("nie importują się: " + ", ".join(brak))
        return ", ".join(f"{p} {w[self.modul(p)]}" for p in self.pakiety_wymagane()) or "brak pakietów do sprawdzenia"

    def _test_pytest(self, pv, kt, log):
        with tempfile.TemporaryDirectory(prefix="mentor_pytest_") as td:
            shutil.copy(kt / "test_probka.py", Path(td) / "test_probka.py")
            kod, out, err = uruchom([pv, "-m", "pytest", "-q", "-p", "no:cacheprovider", "test_probka.py"], timeout=180, cwd=td)
        if kod != 0:
            raise RuntimeError("pytest zakończył się błędem:\n" + (out + err).strip()[-500:])
        m = re.search(r"(\d+) passed", out)
        return f"{m.group(0) if m else 'test przeszedł'} — pytest działa w środowisku kursu"

    def _test_api(self, pv, kt, log):
        port = _wolny_port()
        try:
            serwer = subprocess.Popen([str(pv), "-I", str(kt / "api_serwer.py"), str(port)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                      text=True, encoding="utf-8", errors="replace", env=_env_czysty(), **_flagi())
        except OSError as e:
            raise RuntimeError(f"nie udało się uruchomić serwera testowego: {e}")
        try:
            url = f"http://127.0.0.1:{port}/health"
            gotowy = False
            for _ in range(60):
                if serwer.poll() is not None:
                    raise RuntimeError("serwer testowy zakończył się przedwcześnie:\n" + (serwer.stdout.read() or "")[-400:])
                try:
                    with urllib.request.urlopen(url, timeout=2) as r:
                        if r.status == 200:
                            gotowy = True
                            break
                except (urllib.error.URLError, OSError):
                    time.sleep(0.5)
            if not gotowy:
                raise RuntimeError("serwer lokalny nie odpowiedział w 30 s (port zajęty? zapora?)")
            # prawdziwe żądanie HTTP z biblioteką kursu (requests), jeśli jest wymagana
            klient = "requests" if "requests" in self.pakiety_wymagane() else "urllib"
            kod, out, err = uruchom([pv, "-I", str(kt / "api_klient.py"), url, klient], timeout=60)
            if kod != 0:
                raise RuntimeError(f"żądanie HTTP ({klient}) nie powiodło się:\n" + (out + err).strip()[-400:])
            return f"serwer na porcie {port} odpowiedział 200, klient {klient}: {out.strip().splitlines()[-1][:120]}"
        finally:
            _zabij(serwer)

    def _test_selenium(self, pv, kt, log):
        b = znajdz_przegladarke(self.wym.get("przegladarka") or "edge")
        if not b:
            raise TestPominiety("nie znaleziono przeglądarki (Edge/Chrome) — test pominięty; zainstaluj przeglądarkę i uruchom „Sprawdź działanie”")
        html = None
        mat = katalog_materialow(self.id)
        for c in self.wym.get("sprawdzenia", []):
            if c.get("kind") == "file_exists" and str(c.get("path", "")).endswith(".html") and mat and (mat / c["path"]).exists():
                html = mat / c["path"]
                break
        html = html or (kt / "strona_testowa.html")
        log(f"Selenium: {b['nazwa']} {b['wersja']} ({b['exe']}), strona {html}")
        kod, out, err = uruchom([pv, "-I", str(kt / "selenium_test.py"), b["nazwa"], b["exe"], str(html)], timeout=180)
        if kod != 0:
            tekst = (out + err).strip()
            if "Unable to obtain" in tekst or "selenium-manager" in tekst.lower() or "SessionNotCreated" in tekst:
                raise RuntimeError("przeglądarka/sterownik: " + tekst[-500:] + "\n(Selenium Manager pobiera sterownik przy pierwszym uruchomieniu — potrzebny internet; sprawdź też zgodność wersji Edge i sterownika.)")
            raise RuntimeError(tekst[-600:])
        return out.strip().splitlines()[-1][:200]

    # --- naprawa / usuwanie -------------------------------------------------------
    def usun_srodowisko(self):
        if self.katalog.exists():
            shutil.rmtree(self.katalog, ignore_errors=True)
        return not self.katalog.exists()

    # --- uruchamianie programów ucznia ------------------------------------------
    def interpreter_ucznia(self):
        """(ścieżka, opis) interpretera do uruchamiania kodu ucznia: .venv kursu → Python systemowy/zarządzany pasujący do spec
        → (tylko poza EXE) Python Mentora. Nigdy Mentor.exe (sys.executable w PyInstallerze uruchamia GUI, nie skrypt)."""
        pv = self.python_venv()
        if pv:
            return pv, "środowisko kursu (.venv)"
        st = self.stan()
        for exe in [st.get("python_bazowy")] + [p["exe"] for p in znajdz_pythony(self.spec_pythona())]:
            if exe and Path(exe).exists() and not (ZAMROZONY and Path(exe).resolve() == Path(sys.executable).resolve()):
                return Path(exe), "Python systemowy (bez bibliotek kursu)"
        if not ZAMROZONY:
            return Path(sys.executable), "Python, w którym działa Mentor (tryb deweloperski)"
        return None, "brak interpretera"

    def uruchom_plik_ucznia(self, plik, wejscie="", limit=20, anuluj=None):
        """Uruchamia plik .py ucznia interpreterem kursu (nigdy Pythonem Mentora). Zwraca (kod, stdout, stderr)."""
        plik = Path(plik)
        return self.uruchom_w_srodowisku(["-X", "utf8", str(plik)], cwd=plik.parent, wejscie=wejscie, limit=limit, anuluj=anuluj)

    def uruchom_w_srodowisku(self, argumenty, cwd, wejscie="", limit=20, anuluj=None):
        """`python <argumenty>` interpreterem kursu w katalogu cwd, z limitem czasu i możliwością anulowania (Event).
        Proces potomny nie dziedziczy zmiennych Mentora/PyInstallera. Zwraca (kod, stdout, stderr); kod -1 = limit/anulowano, -2 = nie uruchomiono."""
        pv, _ = self.interpreter_ucznia()
        if not pv:
            return -2, "", "Brak Pythona do uruchomienia pliku — przygotuj środowisko w zakładce Środowisko."
        try:
            p = subprocess.Popen([str(pv)] + [str(a) for a in argumenty], cwd=str(cwd), stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE, env=_env_czysty(), **_flagi())
        except OSError as e:
            return -2, "", str(e)
        wynik = {}

        def czytaj():
            try:
                wynik["out"], wynik["err"] = p.communicate(input=(wejscie or "").encode("utf-8"))
            except (OSError, ValueError) as e:  # noqa: PERF203
                wynik["out"], wynik["err"] = b"", str(e).encode()
        w = threading.Thread(target=czytaj, daemon=True)
        w.start()
        start = time.monotonic()
        powod = ""
        while w.is_alive():
            w.join(0.1)
            if _anulowano(anuluj):
                powod = "[anulowano]"
                break
            if time.monotonic() - start > limit:
                powod = f"[przerwano po {limit} s — pętla nieskończona albo program czeka na input()]"
                break
        if powod:
            _zabij(p)
            w.join(5)
        out = wynik.get("out", b"").decode("utf-8", "replace")
        err = wynik.get("err", b"").decode("utf-8", "replace")
        if powod:
            return -1, out, (err + "\n" if err else "") + powod
        return p.returncode, out, err


class TestPominiety(RuntimeError):
    """Test nie mógł się odbyć z powodu brakującego składnika (np. przeglądarki) — raportowany osobno, nie jako GOTOWE."""


def _anulowano(anuluj):
    return anuluj is not None and anuluj.is_set()


def _wolny_port():
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def srodowisko_programu(P_, meta=None):
    """Srodowisko dla aktywnego programu: wymagania z meta.json paczki albo z pola „srodowisko” programu."""
    meta = meta if meta is not None else meta_kursu(P_.id)
    if meta and meta.get("wymagania"):
        wym = dict(meta["wymagania"])
    else:
        import paczki
        wym = paczki.wymagania_kursu(P_.d)
    wym.setdefault("_wersja", P_.d.get("wersja"))
    return Srodowisko(P_.id, wym)
