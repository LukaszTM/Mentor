# -*- coding: utf-8 -*-
"""
Paczki kursów (ZIP) — podgląd, bezpieczne rozpakowanie, import i aktualizacja. (W spec: course_package_manager.)

Układ po imporcie (katalog danych użytkownika, nigdy katalog EXE):
    kursy/<id>/kurs.json     — program w formacie mentor-program/1 (kopia pliku wejściowego paczki)
    kursy/<id>/meta.json     — id, wersja, nazwa, źródło (plik + SHA-256), data importu, manifest, wymagania środowiska
    kursy/<id>/paczka/       — cała zawartość ZIP bez zmian (materiały, przykłady, requirements, skrypty — NIGDY nie uruchamiane)
    kursy/_kopie/<id>_<wersja>_<data>/ — poprzednia wersja kursu po aktualizacji
Katalog roboczy ucznia (PRACA) jest poza tym drzewem: Dokumenty/Mentor/<id>/PRACA.

Bezpieczeństwo: odrzucamy wpisy z „..”, ścieżkami absolutnymi, literą dysku, dowiązaniami symbolicznymi; limity liczby i rozmiaru
plików oraz podejrzany stopień kompresji; rozpakowanie do katalogu tymczasowego i atomowe zatwierdzenie (os.replace).
Z paczki NIE wykonujemy żadnych poleceń: .bat/.ps1/.sh/.exe są tylko wypisywane w podglądzie jako „niewykonywane”.
"""

import datetime as dt
import hashlib
import json
import os
import re
import shutil
import stat
import zipfile
from pathlib import Path, PurePosixPath

import program as _program
from program import KATALOG_KURSOW, waliduj

SCHEMAT_MANIFESTU = "mentor-course/1"
LIMIT_LICZBY_PLIKOW = 20_000
LIMIT_ROZMIARU = 2 * 1024 ** 3          # 2 GiB po rozpakowaniu
LIMIT_PLIKU = 512 * 1024 ** 2           # jeden plik do 512 MiB
LIMIT_STOPNIA_KOMPRESJI = 400           # bomba zip: >400× przy pliku > 8 MiB
ROZSZERZENIA_SKRYPTOW = {".bat", ".cmd", ".ps1", ".sh", ".exe", ".msi", ".vbs", ".js", ".jar", ".com", ".scr"}
PAKIETY_ZAUFANE = {"pytest", "requests", "selenium", "flask"}      # instalowane z lockiem Mentora, gdy paczka nie ma własnego locka z hashami
ID_WZORZEC = re.compile(r"^[a-z0-9][a-z0-9._-]{1,63}$")


class BladPaczki(Exception):
    pass


# ============================================================ pomocnicze
def sha256_pliku(sciezka, blok=1 << 20):
    h = hashlib.sha256()
    with open(sciezka, "rb") as f:
        for b in iter(lambda: f.read(blok), b""):
            h.update(b)
    return h.hexdigest()


def _rozmiar_tekst(b):
    for jedn in ("B", "KB", "MB", "GB"):
        if b < 1024 or jedn == "GB":
            return f"{b:.0f} {jedn}" if jedn == "B" else f"{b:.1f} {jedn}"
        b /= 1024


def _jest_dowiazaniem(info):
    return stat.S_ISLNK(info.external_attr >> 16)


def _sprawdz_nazwe(nazwa):
    """Zwraca znormalizowaną ścieżkę względną (POSIX) albo rzuca BladPaczki."""
    if "\x00" in nazwa:
        raise BladPaczki(f"Niedozwolony znak w nazwie: {nazwa!r}")
    n = nazwa.replace("\\", "/")
    if n.startswith("/") or re.match(r"^[A-Za-z]:", n) or n.startswith("//"):
        raise BladPaczki(f"Ścieżka absolutna w archiwum: {nazwa}")
    czesci = [c for c in n.split("/") if c not in ("", ".")]
    if any(c == ".." for c in czesci):
        raise BladPaczki(f"Ścieżka wychodząca poza katalog („..”): {nazwa}")
    if any(c.strip() == "" for c in czesci):
        raise BladPaczki(f"Pusta część ścieżki: {nazwa}")
    return "/".join(czesci)


def _wpisy(z):
    """Lista (nazwa_znormalizowana, ZipInfo) plików (bez katalogów) po walidacji bezpieczeństwa i limitów."""
    wpisy, razem = [], 0
    infos = z.infolist()
    if len(infos) > LIMIT_LICZBY_PLIKOW:
        raise BladPaczki(f"Za dużo plików w archiwum: {len(infos)} (limit {LIMIT_LICZBY_PLIKOW}).")
    for info in infos:
        if _jest_dowiazaniem(info):
            raise BladPaczki(f"Dowiązanie symboliczne w archiwum: {info.filename}")
        nazwa = _sprawdz_nazwe(info.filename)
        if info.is_dir() or info.filename.endswith("/") or not nazwa:
            continue
        if info.file_size > LIMIT_PLIKU:
            raise BladPaczki(f"Plik {info.filename} jest za duży ({_rozmiar_tekst(info.file_size)}; limit {_rozmiar_tekst(LIMIT_PLIKU)}).")
        if info.compress_size and info.file_size > 8 * 1024 ** 2 and info.file_size / info.compress_size > LIMIT_STOPNIA_KOMPRESJI:
            raise BladPaczki(f"Podejrzany stopień kompresji pliku {info.filename} — archiwum odrzucone.")
        razem += info.file_size
        if razem > LIMIT_ROZMIARU:
            raise BladPaczki(f"Archiwum po rozpakowaniu przekracza {_rozmiar_tekst(LIMIT_ROZMIARU)}.")
        wpisy.append((nazwa, info))
    if not wpisy:
        raise BladPaczki("Archiwum jest puste.")
    return wpisy, razem


def _wspolny_korzen(nazwy):
    """Jeśli wszystkie pliki leżą w jednym katalogu najwyższego poziomu (np. „Kadry-i-place/…”), zwraca jego nazwę."""
    pierwsze = {n.split("/", 1)[0] for n in nazwy}
    if len(pierwsze) == 1 and all("/" in n for n in nazwy):
        return pierwsze.pop()
    return ""


def _json_z_zip(z, info):
    try:
        return json.loads(z.read(info).decode("utf-8-sig"))
    except (UnicodeDecodeError, json.JSONDecodeError) as e:
        raise BladPaczki(f"Plik {info.filename} nie jest poprawnym JSON: {e}")


# ============================================================ wymagania (zaufana synteza)
def _parsuj_requirements(tekst):
    """Nazwy pakietów i wersje z requirements.txt/.lock (tylko proste linie PyPI; opcje typu -e/--index-url są odrzucane)."""
    pakiety, hashe, bledy = [], False, []
    for linia in tekst.splitlines():
        s = linia.strip()
        if not s or s.startswith("#"):
            continue
        s = s.rstrip("\\").strip()
        if s.startswith("--hash="):
            hashe = True
            continue
        if s.startswith("-") or "://" in s or s.startswith("git+") or s.startswith("file:"):
            bledy.append(f"Niedozwolona linia w pliku zależności: {s[:60]}")
            continue
        m = re.match(r"^([A-Za-z0-9][A-Za-z0-9._-]*)(\[[^\]]*\])?\s*(==|>=|<=|~=|!=|>|<)?\s*([A-Za-z0-9.*+!-]*)", s)
        if not m:
            bledy.append(f"Nierozpoznana linia: {s[:60]}")
            continue
        pakiety.append({"nazwa": m.group(1).lower().replace("_", "-"), "wersja": m.group(4) if m.group(3) == "==" else None})
        if "--hash=" in s:
            hashe = True
    return pakiety, hashe, bledy


def _api_lokalne(d):
    """Deklaracja lokalnego serwera API kursu: {skrypt, port, health, sha256} albo None. Mentor uruchamia go TYLKO na żądanie ucznia,
    interpreterem kursu, po weryfikacji sumy skryptu (manifest lub INTEGRITY.json) — nigdy przy imporcie."""
    if not isinstance(d, dict) or not d:
        return None
    skrypt = d.get("skrypt") or d.get("script")
    if not skrypt or not isinstance(skrypt, str):
        return None
    try:
        skrypt = _sprawdz_nazwe(skrypt)
    except BladPaczki:
        return None
    try:
        port = int(d.get("port") or 8765)
    except (TypeError, ValueError):
        port = 8765
    return {"skrypt": skrypt, "port": port, "health": str(d.get("health") or d.get("health_path") or "/health"), "sha256": d.get("sha256"),
            "opis": str(d.get("opis") or d.get("description") or "")}


def _wymagania_z_manifestu(man):
    r = man.get("requirements") or {}
    narz_opc = r.get("optional_tools") or []
    pak = []
    for x in r.get("python_packages") or []:
        if isinstance(x, str):
            pak.append({"nazwa": x.lower(), "wersja": None})
        elif isinstance(x, dict) and x.get("name"):
            pak.append({"nazwa": str(x["name"]).lower(), "wersja": x.get("version")})
    wym = {
        "zrodlo": "manifest",
        "python": r.get("python") or None,
        "lock": r.get("python_packages_lock") or None,
        "pakiety": pak,
        "api_lokalne": _api_lokalne(man.get("local_api") or r.get("local_api")),
        "sandbox_html": (str(man.get("sandbox_html")) if man.get("sandbox_html") else None),
        "narzedzia_wymagane": [str(x).lower() for x in (r.get("required_tools") or [])],
        "narzedzia_opcjonalne": [{"nazwa": str(x).lower(), "od_tygodnia": None} if isinstance(x, str) else {"nazwa": str(x.get("name", "")).lower(), "od_tygodnia": x.get("from_week")} for x in narz_opc],
        "przegladarka": (r.get("browser") or None),
        "przegladarka_od_tygodnia": r.get("browser_from_week"),
        "sprawdzenia": [c for c in (man.get("checks") or []) if isinstance(c, dict)],
        "uwagi": [],
    }
    return wym


def _wymagania_z_programu(dane):
    s = dane.get("srodowisko") or {}
    if not isinstance(s, dict) or not s:
        return None
    opc = s.get("narzedzia_opcjonalne") or {}
    if isinstance(opc, dict):
        opc = [{"nazwa": k, "od_tygodnia": v} for k, v in opc.items()]
    return {
        "zrodlo": "program",
        "python": s.get("python"),
        "lock": s.get("lock"),
        "pakiety": [{"nazwa": p, "wersja": None} if isinstance(p, str) else p for p in (s.get("pakiety") or [])],
        "narzedzia_wymagane": list(s.get("narzedzia_wymagane") or []),
        "narzedzia_opcjonalne": opc,
        "api_lokalne": _api_lokalne(s.get("api_lokalne")),
        "sandbox_html": s.get("sandbox_html"),
        "przegladarka": s.get("przegladarka"),
        "przegladarka_od_tygodnia": s.get("przegladarka_od_tygodnia"),
        "sprawdzenia": list(s.get("sprawdzenia") or []),
        "uwagi": list(s.get("uwagi") or []),
    }


def _wymagania_heurystyczne(dane):
    """Stara paczka bez manifestu i requirements: rozpoznajemy tylko znane, zaufane pakiety po treści kursu (sygnał do diagnozy)."""
    txt = json.dumps(dane, ensure_ascii=False).lower()
    pak = [p for p in sorted(PAKIETY_ZAUFANE) if re.search(r"\b" + p + r"\b", txt)]
    narz = []
    if re.search(r"\bgit\b", txt):
        narz.append({"nazwa": "git", "od_tygodnia": None})
    if "claude" in txt:
        narz.append({"nazwa": "claude", "od_tygodnia": None})
    if not pak and not narz:
        return {"zrodlo": "brak", "python": None, "lock": None, "pakiety": [], "narzedzia_wymagane": [], "narzedzia_opcjonalne": [],
                "przegladarka": None, "sprawdzenia": [], "uwagi": ["Kurs nie deklaruje żadnych narzędzi — wystarczy Mentor."]}
    return {"zrodlo": "heurystyka", "python": ">=3.11,<3.14" if pak else None, "lock": None, "pakiety": [{"nazwa": p, "wersja": None} for p in pak],
            "narzedzia_wymagane": [], "narzedzia_opcjonalne": narz, "przegladarka": "edge" if "selenium" in pak else None,
            "sprawdzenia": [{"kind": "python_import", "module": p} for p in pak],
            "uwagi": ["Paczka bez manifestu — wymagania rozpoznane po treści kursu" + (" (zaufane pakiety: " + ", ".join(pak) + ")" if pak else " (narzędzia: " + ", ".join(n["nazwa"] for n in narz) + ")") + ". "
                      "Nowe paczki powinny mieć mentor-manifest.json."]}


def wymagania_kursu(dane, manifest=None, requirements_txt=None, requirements_lock=None):
    """Zaufana synteza wymagań: manifest → pole „srodowisko” programu → requirements(.lock/.txt) → heurystyka."""
    if manifest:
        wym = _wymagania_z_manifestu(manifest)
        if not wym["pakiety"] and wym.get("lock") and requirements_lock:
            pak, hashe, bledy = _parsuj_requirements(requirements_lock)
            if hashe and pak:
                wym["pakiety"] = pak        # manifest wskazuje lock paczki — lista pakietów z niego
        z_programu = _wymagania_z_programu(dane) or {}
        # manifest ma pierwszeństwo, ale pole „srodowisko” programu uzupełnia to, czego manifest nie podaje
        for k in ("pakiety", "api_lokalne", "sandbox_html", "przegladarka", "przegladarka_od_tygodnia", "python", "sprawdzenia", "narzedzia_opcjonalne"):
            if not wym.get(k) and z_programu.get(k):
                wym[k] = z_programu[k]
        if z_programu.get("uwagi"):
            wym["uwagi"] = list(wym.get("uwagi") or []) + [u for u in z_programu["uwagi"] if u not in (wym.get("uwagi") or [])]
    else:
        wym = _wymagania_z_programu(dane)
    if wym is None:
        if requirements_lock or requirements_txt:
            pak, hashe, bledy = _parsuj_requirements(requirements_lock or requirements_txt)
            wym = {"zrodlo": "requirements", "python": ">=3.11,<3.14", "lock": "requirements.lock" if (requirements_lock and hashe) else None,
                   "pakiety": pak, "narzedzia_wymagane": [], "narzedzia_opcjonalne": [], "przegladarka": None,
                   "sprawdzenia": [{"kind": "python_import", "module": p["nazwa"].replace("-", "_")} for p in pak if p["nazwa"] in PAKIETY_ZAUFANE],
                   "uwagi": bledy}
            if requirements_lock and not hashe:
                wym["uwagi"].append("requirements.lock bez sum kontrolnych — Mentor użyje własnego locka z hashami dla zaufanych pakietów.")
            txt = json.dumps(dane, ensure_ascii=False).lower()
            if "selenium" in [p["nazwa"] for p in pak] or "selenium" in txt:
                wym["przegladarka"] = "edge"
            if re.search(r"\bgit\b", txt):
                wym["narzedzia_opcjonalne"].append({"nazwa": "git", "od_tygodnia": None})
        else:
            wym = _wymagania_heurystyczne(dane)
    elif not wym["pakiety"] and (requirements_lock or requirements_txt):
        pak, hashe, bledy = _parsuj_requirements(requirements_lock or requirements_txt)
        wym["pakiety"] = pak
        wym["uwagi"] += bledy
        if requirements_lock and hashe and not wym.get("lock"):
            wym["lock"] = "requirements.lock"
        if wym.get("lock") and not (requirements_lock and hashe):
            wym["uwagi"].append("Manifest wskazuje lock, ale w archiwum nie ma requirements.lock z sumami kontrolnymi — Mentor użyje własnego locka dla zaufanych pakietów.")
            wym["lock"] = None
    # pakiety spoza zaufanej listy bez locka z hashami — nie instalujemy automatycznie
    nieobslugiwane = [p["nazwa"] for p in wym["pakiety"] if p["nazwa"] not in PAKIETY_ZAUFANE and not wym.get("lock")]
    if nieobslugiwane:
        wym["uwagi"].append("Pakiety spoza zaufanej listy bez locka z hashami (nie będą instalowane automatycznie): " + ", ".join(nieobslugiwane))
    wym["nieobslugiwane"] = nieobslugiwane
    return wym


def czy_wymaga_srodowiska(wym):
    return bool(wym and (wym.get("python") or wym.get("pakiety") or wym.get("narzedzia_wymagane") or wym.get("przegladarka")))


# ============================================================ podgląd ZIP
def przejrzyj_zip(sciezka):
    """Analizuje archiwum bez rozpakowywania. Zwraca słownik podglądu albo rzuca BladPaczki."""
    sciezka = Path(sciezka)
    if not sciezka.is_file():
        raise BladPaczki(f"Nie ma pliku: {sciezka}")
    if not zipfile.is_zipfile(sciezka):
        raise BladPaczki("To nie jest archiwum ZIP.")
    with zipfile.ZipFile(sciezka) as z:
        wpisy, razem = _wpisy(z)
        nazwy = [n for n, _ in wpisy]
        korzen = _wspolny_korzen(nazwy)
        rel = {n[len(korzen) + 1:] if korzen else n: info for n, info in wpisy}
        manifest = None
        if "mentor-manifest.json" in rel:
            manifest = _json_z_zip(z, rel["mentor-manifest.json"])
            if not isinstance(manifest, dict) or manifest.get("schema") != SCHEMAT_MANIFESTU:
                raise BladPaczki(f"mentor-manifest.json: nieobsługiwany schemat (oczekiwano „{SCHEMAT_MANIFESTU}”).")
        # plik programu
        if manifest and manifest.get("entrypoint"):
            ep = _sprawdz_nazwe(str(manifest["entrypoint"]))
            if ep not in rel:
                raise BladPaczki(f"Manifest wskazuje plik „{ep}”, którego nie ma w archiwum.")
            kandydaci = [ep]
        else:
            kandydaci = [n for n in rel if "/" not in n and n.lower().endswith(".json") and n != "mentor-manifest.json" and n != "manifest.json"]
            kandydaci.sort(key=lambda n: (n != "kurs_mentor.json", n != "kurs.json", n))
        programy = []
        for n in kandydaci:
            if rel[n].file_size > 64 * 1024 ** 2:
                continue
            d = _json_z_zip(z, rel[n])
            if isinstance(d, dict) and d.get("format") == _program.FORMAT and "tygodnie" in d:
                programy.append((n, d))
        if not programy:
            raise BladPaczki("W archiwum nie ma pliku kursu (JSON w formacie mentor-program/1 w katalogu głównym).")
        if len(programy) > 1 and not manifest:
            raise BladPaczki("W archiwum jest kilka plików kursu: " + ", ".join(n for n, _ in programy) + " — dodaj mentor-manifest.json z polem „entrypoint”.")
        entrypoint, dane = programy[0]
        bledy = waliduj(dane)
        if bledy:
            raise BladPaczki("Plik kursu ma błędy:\n" + "\n".join(bledy[:8]))
        kurs_id = str(dane.get("id") or "").strip()
        if manifest:
            mid = str(manifest.get("course_id") or "").strip()
            if kurs_id and mid and mid != kurs_id:
                raise BladPaczki(f"Sprzeczne metadane: manifest course_id=„{mid}”, a plik kursu id=„{kurs_id}”.")
            kurs_id = kurs_id or mid
            wersja = str(manifest.get("version") or dane.get("wersja") or "1.0")
            if dane.get("wersja") and manifest.get("version") and str(dane["wersja"]) != str(manifest["version"]):
                raise BladPaczki(f"Sprzeczne metadane: manifest version=„{manifest['version']}”, a plik kursu wersja=„{dane['wersja']}”.")
        else:
            wersja = str(dane.get("wersja") or "1.0")
        if not kurs_id:
            kurs_id = re.sub(r"[^a-z0-9._-]+", "-", Path(entrypoint).stem.lower()).strip("-")
        if not ID_WZORZEC.match(kurs_id):
            raise BladPaczki(f"Identyfikator kursu „{kurs_id}” jest niedozwolony (małe litery, cyfry, . _ -, 2–64 znaki).")
        req_txt = z.read(rel["requirements.txt"]).decode("utf-8", "replace") if "requirements.txt" in rel else None
        req_lock = z.read(rel["requirements.lock"]).decode("utf-8", "replace") if "requirements.lock" in rel else None
        wym = wymagania_kursu(dane, manifest, req_txt, req_lock)
        skrypty = sorted(n for n in rel if PurePosixPath(n).suffix.lower() in ROZSZERZENIA_SKRYPTOW)
        assets = sorted({n.split("/", 1)[0] for n in rel if "/" in n})
        istniejacy = _program.meta_kursu(kurs_id)
        internet = bool(wym.get("pakiety") or wym.get("python") or wym.get("przegladarka"))
        return {
            "plik": str(sciezka), "rozmiar_zip": sciezka.stat().st_size, "rozmiar_po_rozpakowaniu": razem, "liczba_plikow": len(wpisy),
            "korzen": korzen, "entrypoint": entrypoint, "manifest": manifest, "id": kurs_id, "wersja": wersja,
            "nazwa": dane.get("nazwa", ""), "autor": dane.get("autor", ""), "podtytul": dane.get("podtytul", ""),
            "lekcje": len(dane.get("lekcje", [])), "tygodnie": len(dane.get("tygodnie", [])),
            "zadania": sum(len(w.get("zadania", [])) for w in dane.get("tygodnie", [])),
            "wymagania": wym, "skrypty": skrypty, "katalogi": assets, "requirements_txt": req_txt is not None, "requirements_lock": req_lock is not None,
            "internet": internet, "uprawnienia": "brak — instalacja wyłącznie w katalogu użytkownika (bez uprawnień administratora)",
            "istniejacy": istniejacy or None, "sha256": sha256_pliku(sciezka),
            "ostrzezenia": ([f"Archiwum zawiera skrypty ({len(skrypty)}): " + ", ".join(skrypty[:6]) + (" …" if len(skrypty) > 6 else "") + " — Mentor ich NIE uruchamia."] if skrypty else [])
                           + list(wym.get("uwagi", [])),
        }


def opis_podgladu(pg):
    """Tekst podglądu do okna potwierdzenia importu."""
    w = pg["wymagania"]
    linie = [f"Kurs: {pg['nazwa']}", f"Identyfikator: {pg['id']} · wersja {pg['wersja']}" + (f" · autor: {pg['autor']}" if pg["autor"] else ""),
             f"Treść: {pg['tygodnie']} tygodni, {pg['lekcje']} lekcji, {pg['zadania']} zadań",
             f"Archiwum: {pg['liczba_plikow']} plików, {_rozmiar_tekst(pg['rozmiar_zip'])} (po rozpakowaniu {_rozmiar_tekst(pg['rozmiar_po_rozpakowaniu'])})",
             f"Źródło: {pg['plik']}", f"SHA-256 archiwum: {pg['sha256'][:16]}…",
             "Manifest: " + ("mentor-manifest.json (" + SCHEMAT_MANIFESTU + ")" if pg["manifest"] else "brak — starsza paczka (wymagania rozpoznane: " + w["zrodlo"] + ")")]
    if czy_wymaga_srodowiska(w):
        czesci = []
        if w.get("python"):
            czesci.append(f"Python {w['python']}")
        if w.get("pakiety"):
            czesci.append("pakiety: " + ", ".join(p["nazwa"] + (f"=={p['wersja']}" if p.get("wersja") else "") for p in w["pakiety"][:8]) + (" …" if len(w["pakiety"]) > 8 else ""))
        if w.get("narzedzia_wymagane"):
            czesci.append("narzędzia: " + ", ".join(w["narzedzia_wymagane"]))
        if w.get("narzedzia_opcjonalne"):
            czesci.append("opcjonalnie: " + ", ".join(x["nazwa"] for x in w["narzedzia_opcjonalne"]))
        if w.get("przegladarka"):
            czesci.append("przeglądarka: " + w["przegladarka"])
        linie.append("Wymagania środowiska: " + "; ".join(czesci))
        linie.append("Internet: potrzebny przy pierwszej instalacji zależności (po imporcie — osobny krok, za Twoją zgodą)")
    else:
        linie.append("Wymagania środowiska: brak — kurs działa w samym Mentorze")
        linie.append("Internet: niepotrzebny")
    linie.append("Uprawnienia: " + pg["uprawnienia"])
    if pg["istniejacy"]:
        linie.append(f"UWAGA: kurs „{pg['id']}” jest już zaimportowany w wersji {pg['istniejacy'].get('wersja')} — import zastąpi go (poprzednia wersja trafi do kopii, postępy zostaną).")
    for o in pg["ostrzezenia"]:
        linie.append("! " + o)
    return "\n".join(linie)


# ============================================================ import
def katalog_pracy(kurs_id):
    """Domyślny katalog roboczy ucznia: Dokumenty/Mentor/<id>/PRACA (poza katalogiem kursu i środowiska).
    Zmienna MENTOR_PRACA (testy, nietypowe instalacje) wskazuje inny katalog bazowy."""
    if os.environ.get("MENTOR_PRACA"):
        return Path(os.environ["MENTOR_PRACA"]) / kurs_id / "PRACA"
    dom = Path.home()
    dok = dom / "Documents"
    if not dok.is_dir():
        dok = dom / "Dokumenty" if (dom / "Dokumenty").is_dir() else dom
    return dok / "Mentor" / kurs_id / "PRACA"


def importuj_zip(sciezka, nadpisz=False, utworz_prace=True, postep=None):
    """Importuje paczkę. Zwraca słownik {id, wersja, katalog, kurs_json, praca, kopia, podglad}.
    Gdy kurs o tym id już jest i nadpisz=False → BladPaczki z atrybutem .konflikt = podgląd."""
    pg = przejrzyj_zip(sciezka)
    kurs_id = pg["id"]
    cel = KATALOG_KURSOW / kurs_id
    if cel.exists() and not nadpisz:
        e = BladPaczki(f"Kurs „{kurs_id}” jest już zaimportowany (wersja {pg['istniejacy'].get('wersja') if pg['istniejacy'] else '?'}).")
        e.konflikt = pg
        raise e
    KATALOG_KURSOW.mkdir(parents=True, exist_ok=True)
    tmp = KATALOG_KURSOW / f"_tmp-{kurs_id}-{os.getpid()}"
    if tmp.exists():
        shutil.rmtree(tmp, ignore_errors=True)
    (tmp / "paczka").mkdir(parents=True)
    try:
        with zipfile.ZipFile(sciezka) as z:
            wpisy, _ = _wpisy(z)
            korzen = pg["korzen"]
            baza = (tmp / "paczka").resolve()
            for i, (nazwa, info) in enumerate(wpisy):
                rel = nazwa[len(korzen) + 1:] if korzen else nazwa
                if not rel:
                    continue
                out = (baza / rel)
                if baza not in out.resolve().parents and out.resolve() != baza:
                    raise BladPaczki(f"Ścieżka poza katalogiem docelowym: {nazwa}")
                out.parent.mkdir(parents=True, exist_ok=True)
                with z.open(info) as src, open(out, "wb") as dst:
                    shutil.copyfileobj(src, dst, 1 << 20)
                if postep and i % 50 == 0:
                    postep(i + 1, len(wpisy))
        shutil.copy2(tmp / "paczka" / pg["entrypoint"], tmp / "kurs.json")
        dane = json.loads((tmp / "kurs.json").read_text(encoding="utf-8-sig"))
        if dane.get("id") != kurs_id:
            dane["id"] = kurs_id
            (tmp / "kurs.json").write_text(json.dumps(dane, ensure_ascii=False, indent=1), encoding="utf-8")
        meta = {"id": kurs_id, "wersja": pg["wersja"], "nazwa": pg["nazwa"], "autor": pg["autor"], "entrypoint": pg["entrypoint"],
                "zrodlo": {"plik": pg["plik"], "sha256": pg["sha256"], "rozmiar": pg["rozmiar_zip"]},
                "data_importu": dt.datetime.now().isoformat(timespec="seconds"), "manifest": pg["manifest"], "wymagania": pg["wymagania"],
                "skrypty_niewykonywane": pg["skrypty"], "liczba_plikow": pg["liczba_plikow"]}
        (tmp / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=1), encoding="utf-8")
        kopia = None
        if cel.exists():
            stare_meta = _program.meta_kursu(kurs_id)
            kop = KATALOG_KURSOW / "_kopie"
            kop.mkdir(exist_ok=True)
            kopia = kop / f"{kurs_id}_{stare_meta.get('wersja', '0')}_{dt.datetime.now():%Y%m%d-%H%M%S}"
            os.replace(cel, kopia)
        os.replace(tmp, cel)
    except Exception:
        shutil.rmtree(tmp, ignore_errors=True)
        raise
    praca = None
    if utworz_prace:
        praca = katalog_pracy(kurs_id)
        try:
            praca.mkdir(parents=True, exist_ok=True)
        except OSError:
            praca = None
    return {"id": kurs_id, "wersja": pg["wersja"], "katalog": cel, "kurs_json": cel / "kurs.json", "praca": praca, "kopia": kopia, "podglad": pg}


def lista_kursow():
    """[(id, meta)] zaimportowanych paczek."""
    out = []
    if KATALOG_KURSOW.is_dir():
        for k in sorted(KATALOG_KURSOW.iterdir()):
            if k.is_dir() and not k.name.startswith("_") and (k / "kurs.json").exists():
                out.append((k.name, _program.meta_kursu(k.name)))
    return out


def usun_kurs(kurs_id, usun_prace=False, usun_srodowisko=False):
    """Usuwa kurs z paczki (kursy/<id>). Domyślnie NIE usuwa katalogu PRACA ani postępów (te są w mentor_dane.json)."""
    cel = KATALOG_KURSOW / kurs_id
    if cel.is_dir():
        shutil.rmtree(cel)
    if usun_srodowisko:
        s = _program.KATALOG_SRODOWISK / kurs_id
        if s.is_dir():
            shutil.rmtree(s, ignore_errors=True)
    if usun_prace:
        p = katalog_pracy(kurs_id)
        if p.is_dir():
            shutil.rmtree(p)
    return True


def zbuduj_paczke(katalog_kursu, cel_zip, manifest=None):
    """Pomocnik dla autorów kursów: pakuje katalog (z kurs_mentor.json/kurs.json) do ZIP z opcjonalnym mentor-manifest.json."""
    katalog_kursu = Path(katalog_kursu)
    with zipfile.ZipFile(cel_zip, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(katalog_kursu.rglob("*")):
            if f.is_file() and "__pycache__" not in f.parts:
                z.write(f, f.relative_to(katalog_kursu).as_posix())
        if manifest:
            z.writestr("mentor-manifest.json", json.dumps(manifest, ensure_ascii=False, indent=1))
    return Path(cel_zip)
