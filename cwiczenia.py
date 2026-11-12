# -*- coding: utf-8 -*-
"""
Ćwiczenia wewnątrz Mentora (etap 3 specyfikacji): przy zadaniu kursu, który wymaga środowiska, pojawia się pasek
„Ćwiczenie w Mentorze” z przyciskami: Otwórz przykład · Utwórz plik ćwiczenia · Otwórz w edytorze · Uruchom · Sprawdź wynik · Pokaż podpowiedź.

Zasady:
- pliki ucznia powstają w katalogu PRACA („Mój projekt”); Mentor nigdy nie nadpisuje istniejącego pliku bez pytania,
- kod uruchamia się tylko po kliknięciu, interpreterem KURSU (.venv kursu — nigdy Mentor.exe), z limitem czasu i przyciskiem Anuluj,
- stdout/stderr pokazujemy w oknie, a traceback tłumaczymy po polsku (asystent.wyjasnij_traceback),
- „Sprawdź wynik” zalicza zadanie tylko, gdy jest zdefiniowane sprawdzenie (uruchomienie bez błędu / oczekiwane wyjście / pytest).
  Gdy sprawdzenia nie ma, status to „Plik istnieje — wymaga sprawdzenia” — NIE „Zaliczone”.
- plik .py nigdy nie jest otwierany przez os.startfile (to by go uruchomiło) — tylko znanym edytorem.

Pole zadania (opcjonalne) — patrz programy/FORMAT.md:
  "cwiczenie": {"plik": "hello.py", "szablon": "...", "przyklad": "...kod...", "przyklad_plik": "przyklady/hello.py",
                "podpowiedz": "...", "stdin": "6\\n3\\n",
                "sprawdzenie": {"rodzaj": "uruchom_bez_bledu" | "wyjscie_zawiera" | "pytest" | "plik_istnieje",
                                "stdin": "...", "tekst": ["..."], "nie_zawiera": ["..."], "min_linii": 5, "plik_testu": "test_x.py", "limit_s": 20}}
Zadanie bez pola „cwiczenie”, ale z plikiem .py w „pliki”, dostaje pasek z domyślnym szablonem i sprawdzeniem „plik_istnieje”.
"""

import datetime as dt
import os
import queue
import shutil
import subprocess
import sys
import threading
import tkinter as tk
from pathlib import Path
from tkinter import messagebox, scrolledtext

import asystent
import paczki
import srodowisko as S
from program import P, katalog_materialow

WINDOWS = sys.platform.startswith("win")
RODZAJE = ("uruchom_bez_bledu", "wyjscie_zawiera", "pytest", "plik_istnieje")
STATUS_ZALICZONE = "zaliczone"
STATUS_WYMAGA = "wymaga_sprawdzenia"
STATUS_BLAD = "blad"


def _M():
    import mentor
    return mentor


# ============================================================ definicja ćwiczenia
def definicja(zad):
    """Znormalizowane dane ćwiczenia dla zadania albo None (zadanie bez pliku .py i bez pola „cwiczenie”)."""
    c = zad.get("cwiczenie")
    if c is not None and not isinstance(c, dict):
        c = None
    pliki_py = [p for p in zad.get("pliki", []) if isinstance(p, str) and p.endswith(".py")]
    plik = (c or {}).get("plik") or (pliki_py[0] if pliki_py else None)
    if not plik or not isinstance(plik, str) or "/" in plik or "\\" in plik or plik.startswith("."):
        return None
    spr = (c or {}).get("sprawdzenie") or {"rodzaj": "plik_istnieje"}
    if not isinstance(spr, dict) or spr.get("rodzaj") not in RODZAJE:
        spr = {"rodzaj": "plik_istnieje"}
    return {
        "plik": plik,
        "alternatywy": [p for p in pliki_py if p != plik],
        "szablon": (c or {}).get("szablon") or _szablon_domyslny(zad, plik),
        "przyklad": (c or {}).get("przyklad"),
        "przyklad_plik": (c or {}).get("przyklad_plik"),
        "podpowiedz": (c or {}).get("podpowiedz"),
        "stdin": (c or {}).get("stdin") or spr.get("stdin") or "",
        "sprawdzenie": spr,
    }


def _szablon_domyslny(zad, plik):
    linie = [f"# {plik} — {zad.get('tytul', '')}".rstrip()]
    if zad.get("opis"):
        linie.append("# Zadanie: " + zad["opis"].replace("\n", " ")[:300])
    if zad.get("sprawdz"):
        linie.append("# Gotowe, gdy: " + zad["sprawdz"].replace("\n", " ")[:300])
    linie += ["", "# Pisz samodzielnie — Mentor uruchomi ten plik przyciskiem „Uruchom”.", ""]
    return "\n".join(linie)


def _podpowiedz(zad, d):
    if d.get("podpowiedz"):
        return d["podpowiedz"]
    kroki = zad.get("kroki") or []
    czesci = []
    if kroki:
        czesci.append("Pierwszy krok:\n" + kroki[0])
    if len(kroki) > 1:
        czesci.append("Potem:\n" + kroki[1])
    if zad.get("problemy"):
        czesci.append("Gdy coś nie działa:\n• " + "\n• ".join(zad["problemy"][:3]))
    return "\n\n".join(czesci) or "Rozwiń „Jak to zrobić” pod zadaniem — tam są kroki."


def _rok(tekst):
    return tekst.replace("{rok}", str(dt.date.today().year)) if isinstance(tekst, str) else tekst


# ============================================================ katalog PRACA
def katalog_pracy(app):
    sc = app.stan.d.get("projekt")
    if sc and Path(sc).is_dir():
        return Path(sc)
    return None


def zapewnij_prace(app):
    """Zwraca katalog roboczy; gdy nie ma — proponuje utworzenie Dokumenty/Mentor/<kurs>/PRACA i podpina go jako „Mój projekt”."""
    k = katalog_pracy(app)
    if k:
        return k
    prop = paczki.katalog_pracy(P.id)
    if not messagebox.askyesno("Katalog roboczy", f"Nie masz jeszcze katalogu roboczego kursu („Mój projekt”).\n\nUtworzyć go tutaj?\n{prop}\n\n"
                               "W nim będą powstawać Twoje pliki ćwiczeń. Możesz też wskazać własny katalog w zakładce Mój projekt.", parent=app):
        return None
    try:
        prop.mkdir(parents=True, exist_ok=True)
    except OSError as e:
        messagebox.showerror("Katalog roboczy", f"Nie udało się utworzyć katalogu:\n{e}", parent=app)
        return None
    app.stan.d["projekt"] = str(prop)
    app.stan.zapisz()
    app._pliki_cache.clear()
    return prop


# ============================================================ edytor
def _kandydaci_edytora():
    """Edytory w kolejności: VS Code, PyCharm, (Windows) Notatnik, (POSIX) gedit/kate/xdg-open. Nigdy os.startfile dla .py."""
    kand = []
    for n in ("code", "code.cmd", "codium", "pycharm", "pycharm64.exe", "charm", "subl", "notepad++"):
        w = shutil.which(n)
        if w:
            kand.append([w])
    if WINDOWS:
        import glob
        for wz in (os.path.expandvars(r"%LOCALAPPDATA%\Programs\JetBrains\*\bin\pycharm64.exe"),
                   r"C:\Program Files\JetBrains\*\bin\pycharm64.exe",
                   os.path.expandvars(r"%LOCALAPPDATA%\Programs\Microsoft VS Code\Code.exe"),
                   r"C:\Program Files\Microsoft VS Code\Code.exe",
                   r"C:\Program Files\Notepad++\notepad++.exe"):
            for f in sorted(glob.glob(wz), reverse=True):
                kand.append([f])
        kand.append(["notepad.exe"])
    else:
        for n in ("gedit", "kate", "mousepad", "xed", "pluma"):
            w = shutil.which(n)
            if w:
                kand.append([w])
        if shutil.which("xdg-open"):
            kand.append(["xdg-open"])
    return kand


def otworz_w_edytorze(plik):
    """Otwiera plik w edytorze tekstu. Zwraca nazwę użytego programu albo None."""
    plik = str(plik)
    for cmd in _kandydaci_edytora():
        try:
            kw = {}
            if WINDOWS:
                kw["creationflags"] = 0x00000008  # DETACHED_PROCESS
            else:
                kw["start_new_session"] = True
            subprocess.Popen(cmd + [plik], stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, **kw)
            return Path(cmd[0]).name
        except OSError:
            continue
    return None


# ============================================================ okno wyjścia programu
class OknoWyjscia(tk.Toplevel):
    """Okno z wynikiem uruchomienia: stdout/stderr, wyjaśnienie błędu po polsku, pole danych wejściowych, Anuluj / Uruchom ponownie."""

    def __init__(self, app, tytul, uruchom, stdin_domyslny=""):
        super().__init__(app)
        M = _M()
        K = M.K
        self.app = app
        self.uruchom_fn = uruchom          # callable(stdin, anuluj) -> (kod, out, err)
        self.title(tytul)
        self.configure(bg=K["tlo"])
        self.geometry("820x560")
        self.transient(app)
        self.anuluj = None
        self.kolejka = queue.Queue()
        g = tk.Frame(self, bg=K["tlo"])
        g.pack(fill="x", padx=12, pady=(10, 4))
        self.lbl = tk.Label(g, text="Uruchamiam…", font=M.czc(10, "bold"), bg=K["tlo"], fg=K["tekst"], anchor="w")
        self.lbl.pack(side="left", fill="x", expand=True)
        self.btn_anuluj = M.przycisk(g, "■ Anuluj", self._anuluj, "ostrz")
        self.btn_anuluj.pack(side="right")
        self.btn_ponow = M.przycisk(g, "▶ Uruchom ponownie", self.start, "glowny")
        self.btn_ponow.pack(side="right", padx=8)
        r = tk.Frame(self, bg=K["tlo"])
        r.pack(fill="x", padx=12)
        tk.Label(r, text="Dane dla input() (każda linia = jedna odpowiedź):", font=M.czc(9), bg=K["tlo"], fg=K["szary"], anchor="w").pack(fill="x")
        self.stdin = tk.Text(r, height=3, font=M.czc(9, mono=True), bg=K["karta"], fg=K["tekst"], relief="flat", highlightthickness=1, highlightbackground=K["ramka"])
        self.stdin.pack(fill="x")
        self.stdin.insert("1.0", stdin_domyslny or "")
        self.txt = scrolledtext.ScrolledText(self, font=M.czc(10, mono=True), bg=K["karta"], fg=K["tekst"], relief="flat", wrap="word",
                                             highlightthickness=1, highlightbackground=K["ramka"])
        self.txt.pack(fill="both", expand=True, padx=12, pady=(8, 12))
        self.txt.tag_configure("err", foreground=K["czerw"])
        self.txt.tag_configure("ok", foreground=K["ziel"])
        self.txt.tag_configure("info", foreground=K["szary"])
        self.txt.tag_configure("wyj", foreground=K["nieb"], font=M.czc(10, "bold"))
        self.protocol("WM_DELETE_WINDOW", self._zamknij)
        self.wynik = None
        self.start()

    def _pisz(self, tekst, tag=None):
        self.txt.configure(state="normal")
        self.txt.insert("end", tekst, tag) if tag else self.txt.insert("end", tekst)
        self.txt.see("end")
        self.txt.configure(state="disabled")

    def start(self):
        if self.anuluj is not None and not self.anuluj.is_set() and getattr(self, "watek", None) and self.watek.is_alive():
            return
        self.txt.configure(state="normal")
        self.txt.delete("1.0", "end")
        self.txt.configure(state="disabled")
        self.lbl.configure(text="Uruchamiam… (limit czasu chroni przed pętlą nieskończoną)")
        self.btn_anuluj.configure(state="normal")
        self.anuluj = threading.Event()
        wejscie = self.stdin.get("1.0", "end-1c")
        if wejscie and not wejscie.endswith("\n"):
            wejscie += "\n"

        def praca():
            try:
                self.kolejka.put(("koniec", self.uruchom_fn(wejscie, self.anuluj)))
            except Exception as e:  # noqa: BLE001
                self.kolejka.put(("koniec", (-2, "", f"Mentor nie uruchomił programu: {e}")))
        self.watek = threading.Thread(target=praca, daemon=True)
        self.watek.start()
        self.after(100, self._poll)

    def _poll(self):
        if not self.winfo_exists():
            return
        try:
            rodzaj, dane = self.kolejka.get_nowait()
        except queue.Empty:
            self.after(100, self._poll)
            return
        kod, out, err = dane
        self.wynik = dane
        self.btn_anuluj.configure(state="disabled")
        if out:
            self._pisz("── wyjście programu ──\n", "wyj")
            self._pisz(out if out.endswith("\n") else out + "\n")
        if err:
            self._pisz("── błędy / komunikaty ──\n", "wyj")
            self._pisz(err if err.endswith("\n") else err + "\n", "err")
            w = asystent.wyjasnij_traceback(err)
            if w and w.get("typ") and "Traceback" in err:
                self._pisz("\n── po polsku ──\n", "wyj")
                self._pisz(f"{w['typ']}" + (f" w linii {w['linia']}" if w.get("linia") else "") + f": {w['co']}\n", "info")
                if w.get("pytanie"):
                    self._pisz("Pytanie do Ciebie: " + w["pytanie"] + "\n", "info")
        if kod == 0:
            self.lbl.configure(text="Program zakończył się poprawnie (kod 0)." + ("" if out else " Nic nie wypisał — brak print()?"))
            self._pisz("\n✔ kod wyjścia 0\n", "ok")
        elif kod == -1:
            self.lbl.configure(text="Przerwano (limit czasu lub Anuluj).")
        elif kod == -2:
            self.lbl.configure(text="Nie udało się uruchomić — zobacz komunikat.")
        else:
            self.lbl.configure(text=f"Program zakończył się błędem (kod {kod}). Przeczytaj ostatnią linię błędu — mówi CO, wyżej GDZIE.")

    def _anuluj(self):
        if self.anuluj is not None:
            self.anuluj.set()

    def _zamknij(self):
        self._anuluj()
        self.destroy()


# ============================================================ sprawdzenie
def wykonaj_sprawdzenie(sr, d, plik, anuluj=None):
    """Zwraca {status, opis, szczegoly, data}. Nigdy nie zwraca „zaliczone” bez realnego potwierdzenia."""
    spr = d["sprawdzenie"]
    rodzaj = spr.get("rodzaj", "plik_istnieje")
    teraz = dt.datetime.now().isoformat(timespec="minutes")
    if not plik.exists():
        return {"status": STATUS_BLAD, "opis": f"Brak pliku {plik.name}", "szczegoly": f"Oczekiwany: {plik}", "data": teraz}
    if plik.stat().st_size == 0:
        return {"status": STATUS_BLAD, "opis": f"Plik {plik.name} jest pusty", "szczegoly": "", "data": teraz}
    if rodzaj == "plik_istnieje":
        return {"status": STATUS_WYMAGA, "opis": "Plik istnieje — wymaga sprawdzenia", "szczegoly": "To zadanie nie ma automatycznego testu: porównaj wynik z „Gotowe, gdy” i odhacz samodzielnie.", "data": teraz}
    limit = int(spr.get("limit_s") or 20)
    if rodzaj == "pytest":
        cel = plik.parent / (spr.get("plik_testu") or plik.name)
        if "/" in str(spr.get("plik_testu") or "") or ".." in str(spr.get("plik_testu") or ""):
            return {"status": STATUS_BLAD, "opis": "Nieprawidłowa nazwa pliku testu w definicji zadania", "szczegoly": "", "data": teraz}
        kod, out, err = sr.uruchom_w_srodowisku(["-X", "utf8", "-m", "pytest", "-q", "-p", "no:cacheprovider", cel.name], cwd=plik.parent, limit=max(limit, 60), anuluj=anuluj)
        tekst = (out + "\n" + err).strip()
        if kod == 0 and "passed" in out:
            return {"status": STATUS_ZALICZONE, "opis": "Zaliczone — pytest: " + out.strip().splitlines()[-1][:80], "szczegoly": tekst[-2000:], "data": teraz}
        if kod == -2 or "No module named pytest" in err:
            return {"status": STATUS_BLAD, "opis": "pytest nie jest dostępny w środowisku kursu — zakładka Środowisko → Zainstaluj brakujące", "szczegoly": tekst[-2000:], "data": teraz}
        return {"status": STATUS_BLAD, "opis": "Testy nie przechodzą" if kod > 0 else "Testy przerwane (limit czasu)", "szczegoly": tekst[-3000:], "data": teraz}
    # uruchom_bez_bledu / wyjscie_zawiera
    wejscie = _rok(spr.get("stdin") or d.get("stdin") or "")
    if wejscie and not wejscie.endswith("\n"):
        wejscie += "\n"
    kod, out, err = sr.uruchom_plik_ucznia(plik, wejscie=wejscie, limit=limit, anuluj=anuluj)
    szcz = ("WYJŚCIE:\n" + out[-2000:] + ("\nBŁĘDY:\n" + err[-2000:] if err.strip() else "")).strip()
    if kod == -2:
        return {"status": STATUS_BLAD, "opis": "Nie udało się uruchomić programu", "szczegoly": err, "data": teraz}
    if kod == -1:
        return {"status": STATUS_BLAD, "opis": f"Program nie skończył się w {limit} s (pętla? input() bez danych?)", "szczegoly": szcz, "data": teraz}
    if kod != 0:
        w = asystent.wyjasnij_traceback(err)
        opis = "Program kończy się błędem" + (f": {w['typ']}" + (f" (linia {w['linia']})" if w.get("linia") else "") if w else "")
        return {"status": STATUS_BLAD, "opis": opis, "szczegoly": szcz, "data": teraz}
    min_linii = int(spr.get("min_linii") or 0)
    linie = [l for l in out.splitlines() if l.strip()]
    if min_linii and len(linie) < min_linii:
        return {"status": STATUS_BLAD, "opis": f"Program wypisał {len(linie)} linii, oczekiwano co najmniej {min_linii}", "szczegoly": szcz, "data": teraz}
    if rodzaj == "wyjscie_zawiera":
        szukane = [_rok(t) for t in (spr.get("tekst") or []) if isinstance(t, str)]
        brak = [t for t in szukane if t.lower() not in out.lower()]
        if brak:
            return {"status": STATUS_BLAD, "opis": "W wyjściu brakuje: " + ", ".join(f"„{t}”" for t in brak[:3]), "szczegoly": szcz, "data": teraz}
        zle = [t for t in (spr.get("nie_zawiera") or []) if isinstance(t, str) and _rok(t).lower() in out.lower()]
        if zle:
            return {"status": STATUS_BLAD, "opis": "Wyjście zawiera niepożądane: " + ", ".join(f"„{t}”" for t in zle[:3]), "szczegoly": szcz, "data": teraz}
        return {"status": STATUS_ZALICZONE, "opis": "Zaliczone — program działa i wypisuje oczekiwane wartości" + (f" (dane: {wejscie.strip().replace(chr(10), ', ')})" if wejscie.strip() else ""), "szczegoly": szcz, "data": teraz}
    return {"status": STATUS_ZALICZONE, "opis": "Zaliczone — program działa bez błędu" + (f" (dane: {wejscie.strip().replace(chr(10), ', ')})" if wejscie.strip() else ""), "szczegoly": szcz, "data": teraz}


# ============================================================ pasek przy zadaniu
def zbuduj_pasek(app, parent, zad, bg, wrap):
    """Dodaje do karty zadania pasek „Ćwiczenie w Mentorze”. Zwraca True, gdy zadanie ma ćwiczenie."""
    M = _M()
    K = M.K
    d = definicja(zad)
    if not d:
        return False
    sr = S.srodowisko_programu(P)
    if not sr.wymaga_srodowiska():
        return False
    box = tk.Frame(parent, bg=bg)
    box.pack(fill="x", padx=(26, 0), pady=(8, 0))
    praca = katalog_pracy(app)
    plik = (praca / d["plik"]) if praca else None
    istnieje = bool(plik and plik.exists())
    if not istnieje and praca:
        for alt in d["alternatywy"]:
            if (praca / alt).exists():
                plik, istnieje = praca / alt, True
                break
    g = tk.Frame(box, bg=bg)
    g.pack(fill="x")
    tk.Label(g, text="🧪 Ćwiczenie w Mentorze · " + d["plik"], font=M.czc(9, "bold"), bg=bg, fg=K["akcent"], anchor="w").pack(side="left")
    wynik = (app.stan.d.get("sprawdzenia") or {}).get(zad["id"])
    if wynik:
        kol = {STATUS_ZALICZONE: ("ziel_tlo", "ziel"), STATUS_WYMAGA: ("zolty", "pomar"), STATUS_BLAD: ("czerw_tlo", "czerw")}.get(wynik["status"], ("jasny", "szary"))
        pl = M.plakietka(g, {STATUS_ZALICZONE: "✔ ZALICZONE AUTOMATYCZNIE", STATUS_WYMAGA: "PLIK ISTNIEJE — WYMAGA SPRAWDZENIA", STATUS_BLAD: "✖ SPRAWDZENIE NIE PRZESZŁO"}.get(wynik["status"], wynik["status"]) + f" · {wynik['data'][:16].replace('T', ' ')}", K[kol[0]], K[kol[1]])
        pl.pack(side="left", padx=8)
        pl.bind("<Button-1>", lambda e, w=wynik: _pokaz_szczegoly(app, zad, w))
        pl.configure(cursor="hand2")
    elif istnieje:
        M.plakietka(g, "plik jest w PRACA", K["jasny"], K["szary"]).pack(side="left", padx=8)
    ma_przyklad = bool(d["przyklad"]) or bool(d["przyklad_plik"] and katalog_materialow(P.id) and (katalog_materialow(P.id) / d["przyklad_plik"]).exists())
    r = tk.Frame(box, bg=bg)      # rząd 1: pliki i pomoc
    r.pack(fill="x", pady=(4, 0))
    if ma_przyklad:
        M.przycisk(r, "📄 Otwórz przykład", lambda: otworz_przyklad(app, zad, d), "drugi").pack(side="left", padx=(0, 6), pady=2)
    M.przycisk(r, ("📝 Otwórz w edytorze" if istnieje else "📝 Utwórz plik ćwiczenia"), lambda: otworz_edytor(app, zad, d), "drugi").pack(side="left", padx=(0, 6), pady=2)
    M.przycisk(r, "💡 Pokaż podpowiedź", lambda: messagebox.showinfo("Podpowiedź — " + zad["tytul"][:60], _podpowiedz(zad, d), parent=app), "drugi").pack(side="left", pady=2)
    r = tk.Frame(box, bg=bg)      # rząd 2: uruchomienie i sprawdzenie
    r.pack(fill="x")
    M.przycisk(r, "▶ Uruchom", lambda: uruchom(app, zad, d), "glowny").pack(side="left", padx=(0, 6), pady=2)
    M.przycisk(r, "✔ Sprawdź wynik", lambda: sprawdz(app, zad, d), "drugi").pack(side="left", padx=(0, 6), pady=2)
    opis_spr = {"plik_istnieje": "bez automatycznego testu — „Sprawdź wynik” potwierdzi tylko, że plik istnieje",
                "uruchom_bez_bledu": "test: program musi zakończyć się bez błędu",
                "wyjscie_zawiera": "test: program musi wypisać oczekiwane wartości" + (" dla danych: " + _rok(d["sprawdzenie"].get("stdin") or d["stdin"]).strip().replace("\n", ", ") if (d["sprawdzenie"].get("stdin") or d["stdin"]) else ""),
                "pytest": "test: pytest w środowisku kursu musi być zielony"}[d["sprawdzenie"]["rodzaj"]]
    tk.Label(box, text=opis_spr + " · uruchamianie: interpreter kursu, limit czasu, bez terminala", font=M.czc(8), bg=bg, fg=K["szary"], anchor="w", wraplength=max(200, wrap - 40), justify="left").pack(fill="x", pady=(2, 0))
    return True


def _plik(app, d, zad):
    praca = zapewnij_prace(app)
    if not praca:
        return None, None
    plik = praca / d["plik"]
    if not plik.exists():
        for alt in d["alternatywy"]:
            if (praca / alt).exists():
                return praca, praca / alt
    return praca, plik


def otworz_przyklad(app, zad, d):
    M = _M()
    K = M.K
    kod = d["przyklad"]
    if not kod and d["przyklad_plik"]:
        try:
            kod = (katalog_materialow(P.id) / d["przyklad_plik"]).read_text(encoding="utf-8", errors="replace")
        except OSError as e:
            messagebox.showerror("Przykład", f"Nie udało się odczytać przykładu:\n{e}", parent=app)
            return
    okno = tk.Toplevel(app)
    okno.title("Przykład — " + zad["tytul"][:70])
    okno.configure(bg=K["tlo"])
    okno.geometry("760x520")
    okno.transient(app)
    tk.Label(okno, text="Przykład pokazuje konstrukcję w INNYM kontekście — przepisz ideę, nie tekst. Rozwiązanie zadania piszesz sam.",
             font=M.czc(9), bg=K["tlo"], fg=K["szary"], anchor="w", wraplength=720, justify="left").pack(fill="x", padx=12, pady=(10, 4))
    t = scrolledtext.ScrolledText(okno, font=M.czc(10, mono=True), bg=K["karta"], fg=K["tekst"], relief="flat", highlightthickness=1, highlightbackground=K["ramka"])
    t.pack(fill="both", expand=True, padx=12, pady=(0, 8))
    t.insert("1.0", kod or "")
    t.configure(state="disabled")
    r = tk.Frame(okno, bg=K["tlo"])
    r.pack(fill="x", padx=12, pady=(0, 12))
    M.przycisk(r, "Kopiuj do schowka", lambda: (app.clipboard_clear(), app.clipboard_append(kod or "")), "drugi").pack(side="left")
    M.przycisk(r, "Zamknij", okno.destroy, "drugi").pack(side="right")


def utworz_plik(app, zad, d):
    praca, plik = _plik(app, d, zad)
    if not plik:
        return
    if plik.exists():
        if not messagebox.askyesno("Plik już istnieje", f"{plik.name} już jest w katalogu roboczym.\n\nZASTĄPIĆ go szablonem? Twoja dotychczasowa treść zostanie utracona.\n\n(Nie — otwieram istniejący plik w edytorze.)", parent=app, default="no"):
            otworz_edytor(app, zad, d)
            return
        try:
            kopia = plik.with_name(plik.name + f".kopia-{dt.datetime.now():%Y%m%d-%H%M%S}")
            shutil.copy2(plik, kopia)
        except OSError:
            kopia = None
    else:
        kopia = None
    try:
        plik.write_text(d["szablon"], encoding="utf-8")
    except OSError as e:
        messagebox.showerror("Utwórz plik", f"Nie udało się zapisać pliku:\n{e}", parent=app)
        return
    app._pliki_cache.clear()
    ed = otworz_w_edytorze(plik)
    messagebox.showinfo("Plik ćwiczenia", f"Utworzono {plik}" + (f"\n(poprzednia wersja: {kopia.name})" if kopia else "") + ("\n\nOtwarty w edytorze: " + ed if ed else "\n\nNie znalazłem edytora — otwórz plik w PyCharm/VS Code/Notatniku ręcznie."), parent=app)
    app.pokaz_tydzien(next(w["tydzien"] for w in P.tygodnie if zad in w["zadania"]))


def otworz_edytor(app, zad, d):
    praca, plik = _plik(app, d, zad)
    if not plik:
        return
    if not plik.exists():
        utworz_plik(app, zad, d)
        return
    ed = otworz_w_edytorze(plik)
    if not ed:
        messagebox.showwarning("Edytor", f"Nie znalazłem edytora tekstu. Otwórz plik ręcznie:\n{plik}", parent=app)


def uruchom(app, zad, d):
    praca, plik = _plik(app, d, zad)
    if not plik:
        return
    if not plik.exists():
        if messagebox.askyesno("Uruchom", f"Pliku {plik.name} jeszcze nie ma w katalogu roboczym.\n\nUtworzyć go z szablonu?", parent=app):
            utworz_plik(app, zad, d)
        return
    sr = S.srodowisko_programu(P)
    inter, opis = sr.interpreter_ucznia()
    if not inter:
        messagebox.showwarning("Uruchom", "Brak interpretera Pythona dla kursu — przygotuj środowisko w zakładce Środowisko.", parent=app)
        app.pokaz("srodowisko")
        return
    if not sr.python_venv() and sr.pakiety_wymagane():
        messagebox.showinfo("Uruchom", f"Środowisko kursu nie jest jeszcze gotowe — uruchamiam {opis}. Biblioteki kursu (pytest, requests…) mogą nie działać, dopóki nie zainstalujesz środowiska.", parent=app)
    limit = int(d["sprawdzenie"].get("limit_s") or 20)
    OknoWyjscia(app, f"Uruchom: {plik.name} ({opis})", lambda wejscie, anuluj: sr.uruchom_plik_ucznia(plik, wejscie=wejscie, limit=limit, anuluj=anuluj), stdin_domyslny=_rok(d["stdin"]))


def sprawdz(app, zad, d):
    praca, plik = _plik(app, d, zad)
    if not plik:
        return
    sr = S.srodowisko_programu(P)
    M = _M()
    K = M.K
    okno = tk.Toplevel(app)
    okno.title("Sprawdzam… " + plik.name)
    okno.configure(bg=K["tlo"])
    okno.geometry("520x120")
    okno.transient(app)
    tk.Label(okno, text=f"Sprawdzam {plik.name} w środowisku kursu…", font=M.czc(10, "bold"), bg=K["tlo"], fg=K["tekst"]).pack(padx=16, pady=(18, 6))
    anuluj = threading.Event()
    M.przycisk(okno, "Anuluj", anuluj.set, "ostrz").pack(pady=4)
    q = queue.Queue()

    def praca_w():
        try:
            q.put(wykonaj_sprawdzenie(sr, d, plik, anuluj))
        except Exception as e:  # noqa: BLE001
            q.put({"status": STATUS_BLAD, "opis": f"Sprawdzenie nie powiodło się: {e}", "szczegoly": "", "data": dt.datetime.now().isoformat(timespec="minutes")})
    threading.Thread(target=praca_w, daemon=True).start()

    def poll():
        if not okno.winfo_exists():
            return
        try:
            w = q.get_nowait()
        except queue.Empty:
            okno.after(100, poll)
            return
        okno.destroy()
        app.stan.d.setdefault("sprawdzenia", {})[zad["id"]] = w
        if w["status"] == STATUS_ZALICZONE and not app.stan.zrobione(zad["id"]):
            app.stan.oznacz(zad, True)
            app._odznaki_popup() if hasattr(app, "_odznaki_popup") else None
        app.stan.zapisz()
        app._pliki_cache.clear()
        _pokaz_szczegoly(app, zad, w)
        try:
            app.pokaz_tydzien(next(t["tydzien"] for t in P.tygodnie if zad in t["zadania"]))
        except StopIteration:
            pass
    okno.after(100, poll)


def _pokaz_szczegoly(app, zad, w):
    M = _M()
    K = M.K
    okno = tk.Toplevel(app)
    okno.title("Sprawdzenie — " + zad["tytul"][:60])
    okno.configure(bg=K["tlo"])
    okno.geometry("760x480")
    okno.transient(app)
    kol = {STATUS_ZALICZONE: K["ziel"], STATUS_WYMAGA: K["pomar"], STATUS_BLAD: K["czerw"]}.get(w["status"], K["tekst"])
    tk.Label(okno, text=w["opis"], font=M.czc(11, "bold"), bg=K["tlo"], fg=kol, anchor="w", wraplength=720, justify="left").pack(fill="x", padx=12, pady=(12, 2))
    tk.Label(okno, text=f"{w['data'].replace('T', ' ')} · " + {STATUS_ZALICZONE: "zadanie odhaczone automatycznie", STATUS_WYMAGA: "odhacz samodzielnie, gdy wynik zgadza się z „Gotowe, gdy”",
                                                           STATUS_BLAD: "popraw i kliknij „Sprawdź wynik” ponownie"}.get(w["status"], ""), font=M.czc(9), bg=K["tlo"], fg=K["szary"], anchor="w").pack(fill="x", padx=12)
    t = scrolledtext.ScrolledText(okno, font=M.czc(9, mono=True), bg=K["karta"], fg=K["tekst"], relief="flat", highlightthickness=1, highlightbackground=K["ramka"])
    t.pack(fill="both", expand=True, padx=12, pady=8)
    t.insert("1.0", w.get("szczegoly") or "(brak dodatkowych informacji)")
    if w["status"] == STATUS_BLAD and "Traceback" in (w.get("szczegoly") or ""):
        wy = asystent.wyjasnij_traceback(w["szczegoly"].split("BŁĘDY:", 1)[-1])
        if wy:
            t.insert("end", f"\n\n── po polsku ──\n{wy['typ']}: {wy['co']}\nPytanie do Ciebie: {wy.get('pytanie', '')}")
    t.configure(state="disabled")
    M.przycisk(okno, "Zamknij", okno.destroy, "drugi").pack(pady=(0, 12))
