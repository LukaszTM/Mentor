# -*- coding: utf-8 -*-
"""
Mentor — interaktywny nauczyciel do programu
Interaktywny nauczyciel do dowolnego programu nauczania wczytanego z pliku JSON (patrz programy/).

Uruchomienie:  python mentor.py
Wymaga tylko Pythona 3.10+ (tkinter jest w standardowej instalacji z python.org).
Dane zapisują się w pliku mentor_dane.json obok tego skryptu.
"""

import datetime as dt
import json
import os
import random
import re
import shutil
import subprocess
import sys
import threading
import webbrowser
from pathlib import Path

import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, ttk

import tkinter.font as tkfont

from asystent import EmulatorOffline, KlientAPI
from motywy import GRUPY, MOTYW_DOMYSLNY, MOTYWY, motyw
import warsztat
from program import (P, KATALOG_PROGRAMOW, domyslna_sciezka, importuj as importuj_program, lista_programow,
                     wczytaj as wczytaj_program, zapisz_szablon)

KATALOG = Path(sys.executable).resolve().parent if getattr(sys, "frozen", False) else Path(__file__).resolve().parent
PLIK_DANYCH = KATALOG / "mentor_dane.json"
WINDOWS = sys.platform.startswith("win")

# ---------------------------------------------------------------------------
# Wygląd — K (kolory) i czcionki wypełnia zastosuj_wyglad(); patrz motywy.py
# ---------------------------------------------------------------------------
K = {}
FONT = "Segoe UI"
MONO = "Consolas"
SKALA = 1.0          # mnożnik wielkości czcionek (Ustawienia → Wygląd)
JASNOSC_TERM = 0.7   # jasność motywów terminalowych 0.4–1.0

CZCIONKI_UI = ["Segoe UI", "Segoe UI Variable", "Calibri", "Arial", "Verdana", "Tahoma", "Trebuchet MS", "Georgia",
               "Cambria", "Bahnschrift", "Consolas", "Cascadia Mono", "Cascadia Code", "Courier New", "Lucida Console",
               "DejaVu Sans", "DejaVu Sans Mono", "Liberation Sans", "Noto Sans"]
ROZMIARY = [("Mała", 0.85), ("Normalna", 1.0), ("Większa", 1.15), ("Duża", 1.3), ("Bardzo duża", 1.5)]


def czc(rozmiar, styl="normal", mono=False):
    """Krotka czcionki (rodzina, rozmiar·SKALA, styl) — jedno miejsce, gdzie liczy się wielkość."""
    return (MONO if mono else FONT, max(6, round(rozmiar * SKALA)), styl)


def rodziny_czcionek():
    try:
        return set(tkfont.families())
    except tk.TclError:
        return set()


def _czcionka(preferowana, zapasowe):
    rodziny = rodziny_czcionek()
    if not rodziny:
        return preferowana
    for f in (preferowana, *zapasowe):
        if f in rodziny:
            return f
    return preferowana


def zastosuj_wyglad(dane):
    """Przepisuje globalne kolory i czcionki na wartości z motywu i ustawień. Widoki trzeba potem zbudować od nowa."""
    global FONT, MONO, SKALA, JASNOSC_TERM
    from motywy import mieszaj
    m = motyw(dane.get("motyw", MOTYW_DOMYSLNY))
    K.clear()
    K.update({k: v for k, v in m.items() if k not in ("id", "nazwa", "grupa", "ciemny", "font", "mono")})
    K["id"] = m["id"]
    K["grupa"] = m["grupa"]
    # jasność motywów terminalowych: ściemniamy tekst i akcenty w stronę tła
    JASNOSC_TERM = float(dane.get("jasnosc_term", 0.7))
    if m["grupa"] == "terminal" and JASNOSC_TERM < 1.0:
        for k in ("tekst", "szary", "bok_tekst", "bok_tytul", "akcent", "akcent_c", "pomar", "pomar_c", "czerw", "ziel", "nieb", "ramka"):
            K[k] = mieszaj(K[k], K["tlo"], 1.0 - JASNOSC_TERM)
        K["zolty"] = mieszaj(K["karta"], K["pomar"], 0.14)
        for k, kol in (("ziel_tlo", "ziel"), ("czerw_tlo", "czerw"), ("nieb_tlo", "nieb")):
            K[k] = mieszaj(K["karta"], K[kol], 0.18)
    MONO_ZAPAS = ("Consolas", "Cascadia Mono", "DejaVu Sans Mono", "Liberation Mono", "Courier New")
    SANS_ZAPAS = ("Segoe UI", "DejaVu Sans", "Liberation Sans", "Arial", "Helvetica")
    MONO = _czcionka(m["mono"], MONO_ZAPAS)
    wlasna = dane.get("czcionka", "")
    if wlasna and wlasna in rodziny_czcionek():
        FONT = wlasna
    else:
        FONT = _czcionka(m["font"], MONO_ZAPAS if m["font"] == m["mono"] else SANS_ZAPAS)
    SKALA = float(dane.get("skala_czcionki", 1.0))
DNI = ["Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela"]
MIESIACE = ["stycznia", "lutego", "marca", "kwietnia", "maja", "czerwca", "lipca",
            "sierpnia", "września", "października", "listopada", "grudnia"]
POMIJANE_KATALOGI = {".git", ".venv", "venv", "env", "__pycache__", "node_modules", ".idea", ".pytest_cache"}

XP_SESJA_DNIA = 5
XP_QUIZ_PYTANIE = 2
XP_QUIZ_BONUS_100 = 10
XP_DZIENNIK = 3


def dzis():
    return dt.date.today()


def data_pl(d):
    return f"{DNI[d.weekday()]}, {d.day} {MIESIACE[d.month - 1]} {d.year}"


def czas_hm(minuty):
    h, m = divmod(int(minuty), 60)
    return f"{h} h {m} min" if h else f"{m} min"


# ---------------------------------------------------------------------------
# Stan — wszystko, co zapisujemy między uruchomieniami
# ---------------------------------------------------------------------------
class Stan:
    DOMYSLNE = {
        "imie": "", "projekt": "", "start": None, "program": "",
        "zadania": {},      # id zadania -> data ukończenia
        "checklista": {},   # "grupa-indeks" -> True
        "sesje": {},        # "YYYY-MM-DD" -> {"minuty": int, "wpisy": [{"minuty", "temat", "zrodlo", "test"}], "xp": bool}
        "quizy": {},        # "tydzien" -> {"wynik":, "max":, "data":}
        "lekcje": {},       # id lekcji -> {"wynik":, "max":, "data":}  (mini-testy)
        "powtorki": [],     # id pytań do powtórki "tydzien-indeks"
        "dziennik": [],     # {"data", "tekst", "nastroj"}
        "xp": 0, "odznaki": [], "skala_sesji": 1.0,
        "przewodnik": {},   # id programu -> True, gdy uczeń zamknął „Jak zacząć”
        "warsztat": {},     # dane Warsztatu (symulatory, kartoteka) — per program
    }
    # postępy liczone per program: klucze zależne od programu trzymamy w "programy": {id: {...}}
    KLUCZE_PROGRAMU = ("zadania", "checklista", "quizy", "lekcje", "powtorki", "odznaki", "warsztat")

    def __init__(self):
        self.d = json.loads(json.dumps(self.DOMYSLNE))
        if PLIK_DANYCH.exists():
            try:
                self.d.update(json.loads(PLIK_DANYCH.read_text(encoding="utf-8")))
            except (json.JSONDecodeError, OSError):
                pass
        if not self.d["start"]:
            self.d["start"] = str(dzis())
        # migracja: sesje jako liczba -> słownik
        for k, v in list(self.d["sesje"].items()):
            if isinstance(v, (int, float)):
                self.d["sesje"][k] = {"minuty": int(v), "wpisy": [{"minuty": int(v), "temat": "", "zrodlo": "timer", "test": None}], "xp": True}

    # --- przełączanie programu: postępy każdego programu osobno ---------------
    def przelacz_program(self, nowy_id):
        stary = self.d.get("program_id")
        magazyn = self.d.setdefault("programy", {})
        if stary and stary != nowy_id:
            magazyn[stary] = {k: self.d[k] for k in self.KLUCZE_PROGRAMU}
        if nowy_id != stary:
            zapisane = magazyn.get(nowy_id, {})
            for k in self.KLUCZE_PROGRAMU:
                self.d[k] = json.loads(json.dumps(zapisane.get(k, self.DOMYSLNE[k])))
        self.d["program_id"] = nowy_id
        self.zapisz()

    def minuty_dnia(self, klucz):
        v = self.d["sesje"].get(klucz)
        return v["minuty"] if isinstance(v, dict) else int(v or 0)

    def zapisz(self):
        try:
            PLIK_DANYCH.write_text(json.dumps(self.d, ensure_ascii=False, indent=2), encoding="utf-8")
        except OSError as e:
            messagebox.showwarning("Zapis", f"Nie udało się zapisać danych:\n{e}")

    # --- zadania -----------------------------------------------------------
    def zrobione(self, zid):
        return zid in self.d["zadania"]

    def oznacz(self, zadanie, wartosc):
        if wartosc and not self.zrobione(zadanie["id"]):
            self.d["zadania"][zadanie["id"]] = str(dzis())
            self.d["xp"] += zadanie["xp"]
        elif not wartosc and self.zrobione(zadanie["id"]):
            del self.d["zadania"][zadanie["id"]]
            self.d["xp"] = max(0, self.d["xp"] - zadanie["xp"])
        self.zapisz()

    def tydzien_ukonczony(self, w):
        return all(self.zrobione(z["id"]) for z in w["zadania"])

    def postep_tygodnia(self, w):
        return sum(self.zrobione(z["id"]) for z in w["zadania"]), len(w["zadania"])

    def biezacy_tydzien(self):
        for w in P.tygodnie:
            if not self.tydzien_ukonczony(w):
                return w["tydzien"]
        return P.tygodnie[-1]["tydzien"]

    # --- sesje i serie -----------------------------------------------------
    def dodaj_minuty(self, minuty, temat="", zrodlo="timer", test=None):
        """Zapisuje wpis czasu. XP za dzień nauki przyznaje się RAZ NA DOBĘ, niezależnie od liczby wpisów."""
        klucz = str(dzis())
        dzien = self.d["sesje"].setdefault(klucz, {"minuty": 0, "wpisy": [], "xp": False})
        dzien["minuty"] += int(minuty)
        dzien["wpisy"].append({"minuty": int(minuty), "temat": temat, "zrodlo": zrodlo, "test": test,
                               "godzina": dt.datetime.now().strftime("%H:%M")})
        xp_przyznane = False
        if not dzien.get("xp"):
            dzien["xp"] = True
            self.d["xp"] += XP_SESJA_DNIA
            xp_przyznane = True
        self.zapisz()
        return xp_przyznane

    def tematy_ostatnie(self, n=8):
        """Ostatnio wpisywane tematy (do podpowiedzi w polu tematu)."""
        wynik = []
        for k in sorted(self.d["sesje"], reverse=True):
            v = self.d["sesje"][k]
            if isinstance(v, dict):
                for w in reversed(v.get("wpisy", [])):
                    t = w.get("temat")
                    if t and t not in wynik:
                        wynik.append(t)
            if len(wynik) >= n:
                break
        return wynik[:n]

    def seria_biezaca(self):
        sesje = self.d["sesje"]
        d = dzis()
        if str(d) not in sesje:
            d -= dt.timedelta(days=1)
        seria = 0
        while True:
            if d.weekday() == 6:          # niedziela: wolne, nie przerywa serii
                d -= dt.timedelta(days=1)
                continue
            if str(d) in sesje:
                seria += 1
                d -= dt.timedelta(days=1)
            else:
                return seria

    def najdluzsza_seria(self):
        sesje = self.d["sesje"]
        if not sesje:
            return 0
        d = dt.date.fromisoformat(min(sesje))
        koniec = dzis()
        najdl = seria = 0
        while d <= koniec:
            if d.weekday() != 6:
                if str(d) in sesje:
                    seria += 1
                    najdl = max(najdl, seria)
                else:
                    seria = 0
            d += dt.timedelta(days=1)
        return najdl

    def dni_od_ostatniej_sesji(self):
        if not self.d["sesje"]:
            return None
        ostatnia = dt.date.fromisoformat(max(self.d["sesje"]))
        return (dzis() - ostatnia).days

    # --- statystyki i odznaki ---------------------------------------------
    def statystyki(self):
        tyg = sum(self.tydzien_ukonczony(w) for w in P.tygodnie)
        etapy = 0
        for e in P.etapy:
            if all(self.tydzien_ukonczony(P.tydzien(t)) for t in e["tygodnie"]):
                etapy += 1
        quizy = self.d["quizy"].values()
        return {
            "dni_nauki": len(self.d["sesje"]),
            "minuty": sum(self.minuty_dnia(k) for k in self.d["sesje"]),
            "seria": self.seria_biezaca(),
            "najdluzsza_seria": self.najdluzsza_seria(),
            "tygodnie_ukonczone": tyg,
            "etapy_ukonczone": etapy,
            "zadania_ukonczone": len(self.d["zadania"]),
            "zadania_wszystkie": sum(len(w["zadania"]) for w in P.tygodnie),
            "quizy_100": sum(1 for q in quizy if q["wynik"] == q["max"]),
            "quizy_zaliczone": sum(1 for q in quizy if q["max"] and q["wynik"] / q["max"] >= 0.6),
            "wpisy_dziennika": len(self.d["dziennik"]),
            "lekcje_zaliczone": sum(1 for l in self.d.get("lekcje", {}).values() if l["max"] and l["wynik"] / l["max"] >= 0.67),
            "xp": self.d["xp"],
        }

    def nowe_odznaki(self):
        s = self.statystyki()
        nowe = []
        for o in odznaki():
            if o["id"] not in self.d["odznaki"] and o["warunek"](s):
                self.d["odznaki"].append(o["id"])
                nowe.append(o)
        if nowe:
            self.zapisz()
        return nowe


# ---------------------------------------------------------------------------
# Odznaki — generyczne, etapy brane z aktywnego programu
# ---------------------------------------------------------------------------
def odznaki():
    lista = [
        {"id": "start", "ikona": "🚀", "nazwa": "Start", "opis": "Pierwsza zapisana sesja nauki", "warunek": lambda s: s["dni_nauki"] >= 1},
        {"id": "tydzien1", "ikona": "👋", "nazwa": "Pierwszy tydzień", "opis": "Ukończony pierwszy tydzień programu", "warunek": lambda s: s["tygodnie_ukonczone"] >= 1},
        {"id": "seria5", "ikona": "🔥", "nazwa": "Rozgrzewka", "opis": "Seria 5 dni nauki", "warunek": lambda s: s["najdluzsza_seria"] >= 5},
        {"id": "seria15", "ikona": "🔥🔥", "nazwa": "Nawyk", "opis": "Seria 15 dni nauki", "warunek": lambda s: s["najdluzsza_seria"] >= 15},
        {"id": "seria30", "ikona": "🏆", "nazwa": "Żelazna dyscyplina", "opis": "Seria 30 dni nauki", "warunek": lambda s: s["najdluzsza_seria"] >= 30},
    ]
    for i, e in enumerate(P.etapy, 1):
        lista.append({"id": f"etap{e['nr']}", "ikona": "🎓" if i == len(P.etapy) else "🏅", "nazwa": f"Etap {e['nr']}: {e['nazwa']}",
                      "opis": f"Ukończony etap {e['nr']} (tygodnie {e['tygodnie'][0]}–{e['tygodnie'][-1]})" if e["tygodnie"] else "Ukończony etap",
                      "warunek": (lambda n: lambda s: s["etapy_ukonczone"] >= n)(i)})
    lista += [
        {"id": "quiz100", "ikona": "💯", "nazwa": "Bezbłędnie", "opis": "Quiz tygodnia na 100%", "warunek": lambda s: s["quizy_100"] >= 1},
        {"id": "quiz5", "ikona": "🧠", "nazwa": "Powtarzacz", "opis": "5 zaliczonych quizów", "warunek": lambda s: s["quizy_zaliczone"] >= 5},
        {"id": "lekcje10", "ikona": "📖", "nazwa": "Pilny uczeń", "opis": "10 zaliczonych testów z lekcji", "warunek": lambda s: s.get("lekcje_zaliczone", 0) >= 10},
        {"id": "xp100", "ikona": "⭐", "nazwa": "100 XP", "opis": "Zdobyte 100 punktów doświadczenia", "warunek": lambda s: s["xp"] >= 100},
        {"id": "xp500", "ikona": "🌟", "nazwa": "500 XP", "opis": "Zdobyte 500 punktów doświadczenia", "warunek": lambda s: s["xp"] >= 500},
        {"id": "dziennik10", "ikona": "📓", "nazwa": "Kronikarz", "opis": "10 wpisów w dzienniku nauki", "warunek": lambda s: s["wpisy_dziennika"] >= 10},
        {"id": "sesje20", "ikona": "⏱", "nazwa": "20 sesji", "opis": "20 dni z zapisaną sesją nauki", "warunek": lambda s: s["dni_nauki"] >= 20},
        {"id": "godziny50", "ikona": "⏳", "nazwa": "50 godzin", "opis": "50 godzin nauki łącznie", "warunek": lambda s: s["minuty"] >= 50 * 60},
    ]
    return lista


# ---------------------------------------------------------------------------
# Pomocnicze widżety
# ---------------------------------------------------------------------------
class Przewijane(tk.Frame):
    """Ramka z pionowym paskiem przewijania. Zawartość wkładaj do .wnetrze."""

    def __init__(self, parent, bg):
        super().__init__(parent, bg=bg)
        self.canvas = tk.Canvas(self, bg=bg, highlightthickness=0, bd=0)
        pasek = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.wnetrze = tk.Frame(self.canvas, bg=bg)
        self._okno = self.canvas.create_window((0, 0), window=self.wnetrze, anchor="nw")
        self.canvas.configure(yscrollcommand=pasek.set)
        pasek.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.wnetrze.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.bind("<Configure>", lambda e: self.canvas.itemconfig(self._okno, width=e.width))
        self.canvas.bind("<Enter>", self._podlacz)
        self.canvas.bind("<Leave>", self._odlacz)

    def _kolko(self, e):
        if e.num == 4 or e.delta > 0:
            self.canvas.yview_scroll(-1, "units")
        elif e.num == 5 or e.delta < 0:
            self.canvas.yview_scroll(1, "units")

    def _podlacz(self, _):
        self.canvas.bind_all("<MouseWheel>", self._kolko)
        self.canvas.bind_all("<Button-4>", self._kolko)
        self.canvas.bind_all("<Button-5>", self._kolko)

    def _odlacz(self, _):
        self.canvas.unbind_all("<MouseWheel>")
        self.canvas.unbind_all("<Button-4>")
        self.canvas.unbind_all("<Button-5>")


def karta(parent, tytul=None, bg=None, padx=18, pady=14):
    bg = bg or K["karta"]
    zew = tk.Frame(parent, bg=bg, highlightbackground=K["ramka"], highlightthickness=1)
    wew = tk.Frame(zew, bg=bg)
    wew.pack(fill="both", expand=True, padx=padx, pady=pady)
    if tytul:
        tk.Label(wew, text=tytul, font=czc(12, "bold"), bg=bg, fg=K["tekst"], anchor="w").pack(fill="x", pady=(0, 6))
    return zew, wew


def etykieta(parent, tekst, rozmiar=10, bold=False, kolor=None, bg=None, wrap=0, anchor="w", mono=False):
    styl = czc(rozmiar, "bold" if bold else "normal", mono=mono)
    lbl = tk.Label(parent, text=tekst, font=styl, bg=bg or parent.cget("bg"), fg=kolor or K["tekst"],
                   wraplength=wrap, justify="left", anchor=anchor)
    if wrap:
        # zawijanie dopasowuje się do faktycznej szerokości etykiety (zmiana rozmiaru okna, czcionki, paska bocznego)
        lbl.bind("<Configure>", lambda e, w=lbl: w.configure(wraplength=max(120, e.width - 4)))
    return lbl


def przycisk(parent, tekst, cmd, styl="glowny", szer=None):
    kolory = {
        "glowny": (K["akcent"], K["btn_tekst"], K["akcent_c"]),
        "drugi": (K["jasny"], K["tekst"], K["ramka"]),
        "ostrz": (K["pomar"], K["btn_tekst"], K["pomar_c"]),
        "ciemny": (K["bok"], K["bok_tytul"], K["bok_akt"]),
    }[styl]
    b = tk.Button(parent, text=tekst, command=cmd, bg=kolory[0], fg=kolory[1], activebackground=kolory[2],
                  activeforeground=kolory[1], relief="flat", bd=0, padx=14, pady=6, cursor="hand2",
                  font=czc(10, "bold" if styl == "glowny" else "normal"))
    if szer:
        b.configure(width=szer)
    return b


def plakietka(parent, tekst, kolor_tla, kolor_tekstu):
    return tk.Label(parent, text=tekst, bg=kolor_tla, fg=kolor_tekstu, font=czc(9, "bold"), padx=8, pady=2)


# ---------------------------------------------------------------------------
# Aplikacja
# ---------------------------------------------------------------------------
class Mentor(tk.Tk):
    WIDOKI = [
        ("panel", "🏠", "Panel"), ("plan", "📅", "Plan nauki"), ("sesja", "⏱", "Sesja nauki"),
        ("lekcje", "📖", "Lekcje"), ("warsztat", "🧰", "Warsztat"), ("projekt", "📂", "Mój projekt"), ("prompty", "💬", "Prompty"), ("asystent", "🤖", "Asystent"), ("quiz", "🧠", "Quiz"),
        ("dziennik", "📓", "Dziennik"), ("checklista", "✅", "Checklista"), ("sciaga", "📎", "Ściąga"),
        ("ustawienia", "⚙", "Ustawienia"),
    ]
    BOK_MIN, BOK_MAX, BOK_ZWINIETY, BOK_PROG = 170, 420, 76, 130

    def __init__(self):
        super().__init__()
        self.stan = Stan()
        self._zaladuj_program_startowy()
        self.title("Mentor — interaktywny nauczyciel")
        try:
            ikona = Path(getattr(sys, "_MEIPASS", KATALOG)) / "mentor.ico"
            if ikona.exists() and WINDOWS:
                self.iconbitmap(str(ikona))
        except tk.TclError:
            pass
        self.geometry("1200x780")
        self.minsize(980, 640)
        zastosuj_wyglad(self.stan.d)
        self.configure(bg=K["tlo"])
        self._styl()

        # stan timera sesji (żyje niezależnie od widoku)
        self.t_faza = 0
        self.t_dziala = False
        self.t_pozostalo = self._sek_fazy(0)
        self.t_etykieta = None
        self.t_faza_etykiety = []
        self.walka_koniec = None
        self.walka_etykieta = None
        self.t_temat = ""

        self._pliki_cache = {}
        self._dymek = None
        self.emulator = EmulatorOffline(self._kontekst_asystenta)
        self.klient_api = None
        self.asyst_hist = {"offline": [], "api": []}
        self.asyst_wstaw = ""
        self.asyst_zajety = False
        self.asyst_txt = None
        self.asyst_tryb = None
        self.aktywny = None
        self.przyciski_boku = {}
        self._zbuduj_szkielet()
        self.after(1000, self._petla)
        self.pokaz("start" if self._pokazac_przewodnik() else "panel")

    # --------------------------------------------------------------- program
    def _zaladuj_program_startowy(self):
        sciezka = self.stan.d.get("program") or ""
        if not sciezka or not Path(sciezka).exists():
            sciezka = domyslna_sciezka()
        if sciezka and not wczytaj_program(sciezka):
            self.stan.d["program"] = str(sciezka)
            self.stan.przelacz_program(P.id)
        else:
            self.stan.przelacz_program(P.id)

    def ustaw_program(self, sciezka):
        """Przełącza aktywny program. Postępy poprzedniego zostają zapisane pod jego id."""
        bledy = wczytaj_program(sciezka)
        if bledy:
            messagebox.showerror("Program", "Nie można wczytać programu:\n\n" + "\n".join(bledy[:8]), parent=self)
            return False
        self.stan.d["program"] = str(sciezka)
        self.stan.przelacz_program(P.id)
        self._pliki_cache.clear()
        self.asyst_hist = {"offline": [], "api": []}
        self.emulator = EmulatorOffline(self._kontekst_asystenta)
        self.klient_api = None
        self._timer_reset()
        self.przebuduj()
        if self._pokazac_przewodnik():
            self.pokaz("start")
        return True

    # ------------------------------------------------------------------ styl
    def _styl(self):
        s = ttk.Style(self)
        try:
            s.theme_use("clam")
        except tk.TclError:
            pass
        s.configure("TProgressbar", troughcolor=K["jasny"], background=K["akcent"], bordercolor=K["jasny"],
                    lightcolor=K["akcent"], darkcolor=K["akcent"], thickness=10)
        s.configure("Pomar.Horizontal.TProgressbar", troughcolor=K["jasny"], background=K["pomar"],
                    bordercolor=K["jasny"], lightcolor=K["pomar"], darkcolor=K["pomar"], thickness=10)
        s.configure("TCombobox", fieldbackground=K["karta"], background=K["jasny"], foreground=K["tekst"],
                    arrowcolor=K["tekst"], bordercolor=K["ramka"], font=czc(10))
        s.map("TCombobox", fieldbackground=[("readonly", K["karta"])], foreground=[("readonly", K["tekst"])],
              selectbackground=[("readonly", K["karta"])], selectforeground=[("readonly", K["tekst"])])
        s.configure("Vertical.TScrollbar", troughcolor=K["tlo"], background=K["ramka"], arrowcolor=K["szary"],
                    bordercolor=K["tlo"])
        s.configure("Horizontal.TScale", troughcolor=K["jasny"], background=K["akcent"], bordercolor=K["jasny"],
                    lightcolor=K["akcent"], darkcolor=K["akcent"])
        self.option_add("*TCombobox*Listbox.font", czc(10))
        self.option_add("*TCombobox*Listbox.background", K["karta"])
        self.option_add("*TCombobox*Listbox.foreground", K["tekst"])
        self.option_add("*TCombobox*Listbox.selectBackground", K["akcent"])
        self.option_add("*TCombobox*Listbox.selectForeground", K["btn_tekst"])

    def przebuduj(self):
        """Stosuje bieżące ustawienia wyglądu: nowe kolory/czcionki, nowy szkielet, ten sam widok. Timer sesji nie ginie."""
        self.stan.zapisz()
        zastosuj_wyglad(self.stan.d)
        self.configure(bg=K["tlo"])
        self._styl()
        self.bok.destroy()
        self.tresc.destroy()
        self.przyciski_boku = {}
        self._zbuduj_szkielet()
        self.pokaz(self.aktywny or "panel")

    def zmien_motyw(self, id_):
        self.stan.d["motyw"] = id_
        self.przebuduj()

    # ------------------------------------------------------------ pasek boczny
    def _bok_zwiniety(self):
        return bool(self.stan.d.get("bok_zwiniety", False))

    def _bok_szerokosc(self):
        return self.BOK_ZWINIETY if self._bok_zwiniety() else int(self.stan.d.get("bok_szer", 250))

    def _zbuduj_szkielet(self):
        zw = self._bok_zwiniety()
        self.bok = tk.Frame(self, bg=K["bok"], width=self._bok_szerokosc())
        self.bok.pack(side="left", fill="y")
        self.bok.pack_propagate(False)

        # nagłówek: tytuł + przycisk zwijania
        naglowek = tk.Frame(self.bok, bg=K["bok"])
        naglowek.pack(fill="x", pady=(18, 0), padx=(14 if zw else 20, 8))
        tk.Label(naglowek, text="M" if zw else "Mentor", font=czc(20, "bold"), bg=K["bok"], fg=K["bok_tytul"]).pack(side="left")
        zwijacz = tk.Label(naglowek, text="▶" if zw else "◀", font=czc(10), bg=K["bok"], fg=K["bok_tekst"], cursor="hand2", padx=6, pady=4)
        zwijacz.pack(side="right")
        zwijacz.bind("<Button-1>", lambda e: self._bok_przelacz())
        self._dymek_dla(zwijacz, "Rozwiń pasek" if zw else "Zwiń do ikon")
        if not zw:
            tk.Label(self.bok, text=P.nazwa, font=czc(9), bg=K["bok"], fg=K["bok_tekst"],
                     justify="left", anchor="w", wraplength=self._bok_szerokosc() - 44).pack(padx=20, fill="x", pady=(0, 16))
        else:
            tk.Frame(self.bok, bg=K["bok"], height=12).pack()

        # zakładki: większe, rozsunięte, pogrubione (przy dużej czcionce ciaśniej, żeby zmieściło się 10 pozycji)
        widoki = self._widoki()
        pad_y = (11 if len(widoki) <= 12 else 9) if SKALA <= 1.15 else (8 if SKALA <= 1.3 else 5)
        for klucz, ikona, tekst in widoki:
            r = tk.Frame(self.bok, bg=K["bok"], cursor="hand2")
            r.pack(fill="x", pady=2, padx=6)
            etyk = [r]
            if zw:
                li = tk.Label(r, text=ikona, font=czc(15), bg=K["bok"], fg=K["bok_tekst"], pady=pad_y)
                li.pack(fill="x")
                etyk.append(li)
                self._dymek_dla(r, tekst)
                self._dymek_dla(li, tekst)
            else:
                li = tk.Label(r, text=ikona, font=czc(14), bg=K["bok"], fg=K["bok_tekst"], width=2, pady=pad_y, padx=4)
                li.pack(side="left", padx=(8, 4))
                lt = tk.Label(r, text=tekst, font=czc(12, "bold"), bg=K["bok"], fg=K["bok_tekst"], anchor="w", pady=pad_y)
                lt.pack(side="left", fill="x", expand=True)
                etyk += [li, lt]
            for w in etyk:
                w.bind("<Button-1>", lambda e, k=klucz: self.pokaz(k))
                w.bind("<Enter>", lambda e, k=klucz: self._bok_koloruj(k, K["bok_akt"], K["bok_tytul"]) if k != self.aktywny else None)
                w.bind("<Leave>", lambda e, k=klucz: self._bok_koloruj(k, K["bok"], K["bok_tekst"]) if k != self.aktywny else None)
            self.przyciski_boku[klucz] = etyk

        self.bok_stopka = tk.Label(self.bok, text="", font=czc(9), bg=K["bok"], fg=K["bok_tekst"],
                                   justify="center" if zw else "left", anchor="center" if zw else "w")
        self.bok_stopka.pack(side="bottom", fill="x", padx=4 if zw else 20, pady=16)

        # uchwyt do zmiany szerokości (prawa krawędź paska)
        uchwyt = tk.Frame(self.bok, bg=K["bok"], width=6, cursor="sb_h_double_arrow")
        uchwyt.place(relx=1.0, rely=0, relheight=1.0, anchor="ne")
        uchwyt.bind("<B1-Motion>", self._bok_przeciagnij)
        uchwyt.bind("<ButtonRelease-1>", lambda e: self._bok_zakoncz_przeciaganie())
        uchwyt.bind("<Enter>", lambda e: uchwyt.configure(bg=K["bok_akt"]))
        uchwyt.bind("<Leave>", lambda e: uchwyt.configure(bg=K["bok"]))
        uchwyt.lift()
        self._dymek_dla(uchwyt, "Przeciągnij, żeby zmienić szerokość")

        self.tresc = tk.Frame(self, bg=K["tlo"])
        self.tresc.pack(side="right", fill="both", expand=True)

    def _widoki(self):
        """Zakładki paska bocznego: Warsztat tylko wtedy, gdy program ma narzędzia."""
        return [w for w in self.WIDOKI if w[0] != "warsztat" or P.narzedzia]

    def _bok_koloruj(self, klucz, bg, fg):
        for w in self.przyciski_boku.get(klucz, []):
            try:
                w.configure(bg=bg)
                if isinstance(w, tk.Label):
                    w.configure(fg=fg)
            except tk.TclError:
                pass

    def _bok_przelacz(self):
        self.stan.d["bok_zwiniety"] = not self._bok_zwiniety()
        self.przebuduj()

    def _bok_przeciagnij(self, e):
        szer = e.x_root - self.bok.winfo_rootx()
        szer = max(self.BOK_ZWINIETY, min(self.BOK_MAX, szer))
        self._bok_nowa_szer = szer
        self.bok.configure(width=szer if szer >= self.BOK_PROG else self.BOK_ZWINIETY)

    def _bok_zakoncz_przeciaganie(self):
        szer = getattr(self, "_bok_nowa_szer", None)
        if szer is None:
            return
        self._bok_nowa_szer = None
        if szer < self.BOK_PROG:
            self.stan.d["bok_zwiniety"] = True
        else:
            self.stan.d["bok_zwiniety"] = False
            self.stan.d["bok_szer"] = max(self.BOK_MIN, szer)
        self.przebuduj()

    # dymki (tooltipy) — proste okienko bez ramki
    def _dymek_dla(self, wid, tekst):
        wid.bind("<Enter>", lambda e: self._dymek_pokaz(wid, tekst), add="+")
        wid.bind("<Leave>", lambda e: self._dymek_schowaj(), add="+")
        wid.bind("<Button-1>", lambda e: self._dymek_schowaj(), add="+")

    def _dymek_pokaz(self, wid, tekst):
        self._dymek_schowaj()
        try:
            x = wid.winfo_rootx() + wid.winfo_width() + 6
            y = wid.winfo_rooty() + wid.winfo_height() // 2 - 12
        except tk.TclError:
            return
        d = tk.Toplevel(self)
        d.wm_overrideredirect(True)
        d.wm_geometry(f"+{x}+{y}")
        tk.Label(d, text=tekst, font=czc(9), bg=K["karta"], fg=K["tekst"], padx=8, pady=4,
                 highlightbackground=K["ramka"], highlightthickness=1).pack()
        self._dymek = d

    def _dymek_schowaj(self):
        if self._dymek is not None:
            try:
                self._dymek.destroy()
            except tk.TclError:
                pass
            self._dymek = None

    def _odswiez_stopke(self):
        s = self.stan.statystyki()
        if self._bok_zwiniety():
            self.bok_stopka.configure(text=f"🔥{s['seria']}\n⭐{s['xp']}")
        else:
            self.bok_stopka.configure(text=f"🔥 seria: {s['seria']} dni\n⭐ {s['xp']} XP\n⏳ {czas_hm(s['minuty'])} nauki")

    def pokaz(self, nazwa):
        podsw = {"wpis": "sesja", "czcionki": "ustawienia", "start": "panel"}.get(nazwa, nazwa)
        for k in self.przyciski_boku:
            self._bok_koloruj(k, K["bok_akt"] if k == podsw else K["bok"], K["bok_tytul"] if k == podsw else K["bok_tekst"])
        self.aktywny = nazwa
        for w in self.tresc.winfo_children():
            w.destroy()
        self.t_etykieta = None
        self.t_faza_etykiety = []
        self.walka_etykieta = None
        self._odswiez_stopke()
        getattr(self, "widok_" + nazwa)()

    def _naglowek(self, parent, tytul, podtytul=None):
        tk.Label(parent, text=tytul, font=czc(20, "bold"), bg=K["tlo"], fg=K["tekst"], anchor="w").pack(fill="x", padx=28, pady=(24, 0))
        if podtytul:
            tk.Label(parent, text=podtytul, font=czc(10), bg=K["tlo"], fg=K["szary"], anchor="w",
                     wraplength=900, justify="left").pack(fill="x", padx=28, pady=(2, 10))
        else:
            tk.Frame(parent, bg=K["tlo"], height=10).pack()

    def _strona(self, tytul, podtytul=None):
        """Zwraca przewijane wnętrze strony z nagłówkiem."""
        p = Przewijane(self.tresc, K["tlo"])
        p.pack(fill="both", expand=True)
        self._naglowek(p.wnetrze, tytul, podtytul)
        return p.wnetrze

    def _pokazac_przewodnik(self):
        """Przewodnik „Jak zacząć” otwiera się sam: przy pierwszym uruchomieniu (brak imienia) i przy pierwszym wejściu w nowy program."""
        return not self.stan.d["imie"] or not self.stan.d.get("przewodnik", {}).get(P.id)

    def schowek(self, tekst, komunikat="Skopiowano do schowka."):
        self.clipboard_clear()
        self.clipboard_append(tekst)
        if komunikat:
            messagebox.showinfo("Schowek", komunikat, parent=self)

    def _odznaki_popup(self):
        for o in self.stan.nowe_odznaki():
            messagebox.showinfo("Nowa odznaka!", f"{o['ikona']}  {o['nazwa']}\n\n{o['opis']}", parent=self)
        self._odswiez_stopke()

    # ================================================================== PANEL
    # ================================================================ JAK ZACZĄĆ
    def widok_start(self):
        w = self._strona("Jak zacząć — przewodnik po Mentorze", f"Program: {P.nazwa}. Dziesięć minut, które oszczędzą tygodnie błądzenia. "
                         "Wrócisz tu zawsze przyciskiem „Jak zacząć” na Panelu.")
        W = 860

        # krok 1 — imię i katalog
        z, k = karta(w, tytul="Krok 1 · Imię i katalog projektu")
        z.pack(fill="x", padx=28)
        r = tk.Frame(k, bg=K["karta"])
        r.pack(fill="x")
        etykieta(r, "Jak masz na imię? ", 10).pack(side="left")
        imie = tk.StringVar(value=self.stan.d["imie"])
        tk.Entry(r, textvariable=imie, font=czc(10), relief="flat", bg=K["jasny"], fg=K["tekst"], insertbackground=K["tekst"], width=22).pack(side="left", ipady=4)

        def zapisz_imie():
            self.stan.d["imie"] = imie.get().strip()
            self.stan.zapisz()
            self._odswiez_stopke()
            zap.configure(text="✔ zapisano")

        zap = przycisk(r, "Zapisz", zapisz_imie, "drugi")
        zap.pack(side="left", padx=8)
        r = tk.Frame(k, bg=K["karta"])
        r.pack(fill="x", pady=(8, 0))
        proj = self.stan.d["projekt"]
        etykieta(r, "Katalog projektu: " + (proj if proj else "jeszcze nie wybrany"), 10, bold=bool(proj), kolor=K["tekst"] if proj else K["czerw"]).pack(side="left")
        przycisk(r, "Wybierz katalog…", self._wybierz_projekt, "drugi").pack(side="left", padx=8)
        etykieta(k, f"To zwykły folder na dysku (proponowana nazwa: {P.katalog_projektu}). Trafiają do niego wszystkie pliki z zadań — Mentor sprawdza, "
                 "czy powstały (zakładka Mój projekt), a Asystent może je czytać. Jeśli folderu nie ma, utwórz go w Eksploratorze i wskaż tutaj.", 9, kolor=K["szary"], wrap=W).pack(fill="x", pady=(6, 0))

        # krok 2 — dzień nauki
        z, k = karta(w, tytul=f"Krok 2 · Jak wygląda dzień nauki ({sum(f['minuty'] for f in P.rytm_dnia)} min, 4 fazy)")
        z.pack(fill="x", padx=28, pady=(12, 0))
        for i, f in enumerate(P.rytm_dnia, 1):
            r = tk.Frame(k, bg=K["karta"])
            r.pack(fill="x", pady=2)
            tk.Label(r, text=f"{f['ikona']} {i}. {f['nazwa']} · {f['minuty']} min", font=czc(10, "bold"), bg=K["jasny"], fg=K["tekst"], width=30, anchor="w", padx=8, pady=3).pack(side="left", anchor="n")
            etykieta(r, "  " + f["opis"], 10, wrap=560).pack(side="left", fill="x", expand=True)
        etykieta(k, "Timer w zakładce Sesja nauki prowadzi Cię przez fazy i sam zapisuje czas. Masz mniej czasu? Ustawienia → skala sesji (np. 50%) "
                 "albo wpisz czas ręcznie po nauce (Sesja → „Dodaj czas ręcznie” — z tematem i 3-pytaniowym testem; XP raz dziennie).", 9, kolor=K["szary"], wrap=W).pack(fill="x", pady=(6, 0))
        przycisk(k, "▶ Otwórz Sesję nauki", lambda: self.pokaz("sesja"), "drugi").pack(anchor="w", pady=(8, 0))

        # krok 3 — lekcja, zadanie, odhaczenie
        z, k = karta(w, tytul="Krok 3 · Lekcja → zadanie → odhaczenie (codzienna pętla)")
        z.pack(fill="x", padx=28, pady=(12, 0))
        for t in ("1. Panel → „Dzisiaj”: Mentor wybiera zadanie dnia (pon–czw zadania 1–4, piątek zadanie tygodnia, sobota quiz, niedziela wolne).",
                  "2. Lekcje → przeczytaj lekcję dnia: cel, wyjaśnienie, przykład (przelicz sam!), pułapki, 3 zadania, pytania, test 3 pytania.",
                  "3. Plan → zadanie → rozwiń „Jak to zrobić” — kroki są kompletne, od „otwórz…” do „zapisz jako…”. Wykonujesz w katalogu projektu.",
                  "4. Plan → zaznacz ✔ przy zadaniu → +10 XP (zadanie tygodnia +25). Odznaki i seria dni rosną same.",
                  "5. Dziennik → jedno zdanie „czego się dziś nauczyłem” (+3 XP). Po każdym etapie — Checklista (co masz umieć), w sobotę — Quiz."):
            etykieta(k, t, 10, wrap=W).pack(fill="x", pady=(0, 3))
        r = tk.Frame(k, bg=K["karta"])
        r.pack(fill="x", pady=(8, 0))
        if P.lekcje:
            przycisk(r, "📖 Lekcja wprowadzająca", lambda: self.pokaz_lekcje(P.lekcje[0]["id"]), "drugi").pack(side="left")
        przycisk(r, f"📅 Plan — tydzień {P.tygodnie[0]['tydzien']}", lambda: self.pokaz_tydzien(P.tygodnie[0]["tydzien"]), "drugi").pack(side="left", padx=8)

        # krok 3b — warsztat (programy z narzędziami)
        if P.narzedzia:
            z, k = karta(w, tytul="Warsztat · wszystko w jednym miejscu — bez kont, instalacji i arkuszy")
            z.pack(fill="x", padx=28, pady=(12, 0))
            nazwy = [n[2] for n in warsztat.NARZEDZIA if n[0] in P.narzedzia]
            etykieta(k, "Zadania, które w prawdziwej pracy robi się w zewnętrznych systemach (eZUS, Płatnik, e-Urząd) albo w arkuszu, tu wykonujesz w zakładce Warsztat: "
                     + ", ".join(nazwy) + ". Każde narzędzie pokazuje obliczenie krok po kroku i ma przycisk „Zapisz do projektu”. Zasada kursu: najpierw liczysz sam, potem sprawdzasz w Warsztacie.", 10, wrap=W).pack(fill="x")
            przycisk(k, "🧰 Otwórz Warsztat", lambda: self.pokaz("warsztat"), "drugi").pack(anchor="w", pady=(8, 0))

        # krok 4 — asystent
        z, k = karta(w, tytul="Krok 4 · Asystent — nauczyciel, nie wykonawca")
        z.pack(fill="x", padx=28, pady=(12, 0))
        etykieta(k, "Trzy karty w zakładce Asystent: Subskrypcja (Claude Code w terminalu — pełny model), API (własny klucz, rozmowa w Mentorze), "
                 "Offline (wbudowany, bez internetu: „uczę się [temat]”, „co to jest [pojęcie]”, „zadaj mi 3 pytania”, „quiz z tygodnia 2”, „odpytaj mnie jak rekruter”). "
                 "Zasada we wszystkich: najpierw 15 minut własnej walki, potem pytanie o podpowiedź — nie o wynik. Gotowe prompty: zakładka Prompty.", 10, wrap=W).pack(fill="x")
        przycisk(k, "🤖 Otwórz Asystenta", lambda: self.pokaz("asystent"), "drugi").pack(anchor="w", pady=(8, 0))

        # zakładki
        z, k = karta(w, tytul="Co jest w pasku bocznym")
        z.pack(fill="x", padx=28, pady=(12, 0))
        opisy = {"panel": "start dnia: zadanie na dziś, seria, XP, etapy, wskazówka", "plan": "wszystkie tygodnie i zadania z instrukcją „Jak to zrobić”; tu odhaczasz",
                 "sesja": "timer 4 faz z promptami do każdej fazy; ręczny wpis czasu z testem", "lekcje": "krótka lekcja do każdego zagadnienia + test",
                 "projekt": "Twój katalog: wykryte pliki, Git, CLAUDE.md", "prompty": "gotowe prompty i szablony dokumentów do skopiowania",
                 "asystent": "Subskrypcja / API / Offline — pomoc w nauce", "quiz": "quiz tygodnia (sobota) i powtórki błędnych pytań",
                 "dziennik": "notatki z nauki, nastrój, pytania na później", "checklista": "co masz umieć po każdym etapie — odhaczasz sam",
                 "sciaga": "najważniejsze liczby, komendy, terminy i linki", "ustawienia": "imię, program nauczania, motyw, czcionki, eksport postępów",
                 "warsztat": "narzędzia wewnętrzne: kalkulatory, symulator eZUS/Płatnika i e-Urzędu, przepisy — bez kont i instalacji"}
        for klucz, ikona, tekst in self._widoki():
            r = tk.Frame(k, bg=K["karta"])
            r.pack(fill="x", pady=1)
            tk.Label(r, text=f"{ikona} {tekst}", font=czc(10, "bold"), bg=K["jasny"], fg=K["tekst"], width=18, anchor="w", padx=8, pady=2).pack(side="left")
            etykieta(r, "  " + opisy.get(klucz, ""), 10).pack(side="left")

        # FAQ
        z, k = karta(w, tytul="Co, jeśli…")
        z.pack(fill="x", padx=28, pady=(12, 0))
        for p, o in (("…nie wiem, co dziś robić?", "Panel → karta „Dzisiaj”. Zawsze jest jedno zadanie i jedna lekcja na dziś."),
                     ("…nie rozumiem lekcji?", "Przelicz przykład sam, zadaj pytanie Asystentowi („wytłumacz [temat] inaczej”), zapisz pytanie w Dzienniku i wróć jutro — zadanie i tak możesz robić."),
                     ("…miałem przerwę?", "Nic nie przepada. Panel pokaże, ile dni minęło i od czego zacząć. Seria liczy się od nowa, XP i odznaki zostają."),
                     ("…chcę się uczyć czegoś innego?", "Ustawienia → Program nauczania: przełączasz między programami, postępy każdego są osobno."),
                     ("…nie mam 90 minut?", "Ustawienia → skala sesji 50% (45 min) albo wpis ręczny. Lepiej 30 minut codziennie niż 3 godziny raz w tygodniu.")):
            etykieta(k, p, 10, bold=True).pack(fill="x", pady=(4, 0))
            etykieta(k, o, 10, wrap=W).pack(fill="x")

        r = tk.Frame(w, bg=K["tlo"])
        r.pack(fill="x", padx=28, pady=(16, 24))

        def gotowe():
            self.stan.d.setdefault("przewodnik", {})[P.id] = True
            if imie.get().strip():
                self.stan.d["imie"] = imie.get().strip()
            self.stan.zapisz()
            self.pokaz("panel")

        przycisk(r, "✔ Rozumiem — pokaż Panel", gotowe).pack(side="left")
        etykieta(r, "  Przewodnik nie otworzy się już sam; zawsze jest pod „Jak zacząć” na Panelu.", 9, kolor=K["szary"]).pack(side="left")

    def widok_panel(self):
        w = self._strona("")
        for ch in w.winfo_children():
            ch.destroy()
        imie = self.stan.d["imie"] or "programisto"
        s = self.stan.statystyki()
        d = dzis()
        godz = dt.datetime.now().hour
        powitanie = "Dzień dobry" if godz < 12 else ("Dobry wieczór" if godz >= 18 else "Cześć")
        gora = tk.Frame(w, bg=K["tlo"])
        gora.pack(fill="x", padx=28, pady=(24, 0))
        tk.Label(gora, text=f"{powitanie}, {imie}!", font=czc(22, "bold"), bg=K["tlo"], fg=K["tekst"], anchor="w").pack(side="left")
        przycisk(gora, "❓ Jak zacząć", lambda: self.pokaz("start"), "drugi").pack(side="right")
        tk.Label(w, text=data_pl(d), font=czc(11), bg=K["tlo"], fg=K["szary"], anchor="w").pack(fill="x", padx=28)

        # pierwsze kroki — dopóki nie ma ani jednego zadania i sesji w tym programie
        if s["zadania_ukonczone"] == 0 and s["dni_nauki"] == 0:
            z, k = karta(w, bg=K["nieb_tlo"])
            z.pack(fill="x", padx=28, pady=(14, 0))
            etykieta(k, "Pierwsze kroki w tym programie", 12, bold=True, bg=K["nieb_tlo"], kolor=K["nieb"]).pack(fill="x")
            lekcja0 = P.lekcje[0] if P.lekcje else None
            kroki = [("1", "Przeczytaj lekcję wprowadzającą (10 min)", "📖 Otwórz lekcję", (lambda: self.pokaz_lekcje(lekcja0["id"])) if lekcja0 else None),
                     ("2", f"Wskaż katalog projektu (proponowana nazwa: {P.katalog_projektu})", "📂 Mój projekt", lambda: self.pokaz("projekt")),
                     ("3", "Zobacz zadanie na dziś i rozwiń „Jak to zrobić”", "📅 Plan — tydzień 0", lambda: self.pokaz_tydzien(P.tygodnie[0]["tydzien"])),
                     ("4", "Uruchom sesję nauki — 4 fazy, timer prowadzi", "▶ Sesja nauki", lambda: self.pokaz("sesja"))]
            for nr, opis, tekst, cmd in kroki:
                r = tk.Frame(k, bg=K["nieb_tlo"])
                r.pack(fill="x", pady=2)
                tk.Label(r, text=nr, font=czc(11, "bold"), bg=K["nieb"], fg=K["btn_tekst"], width=3).pack(side="left", padx=(0, 8))
                etykieta(r, opis, 10, bg=K["nieb_tlo"]).pack(side="left")
                if cmd:
                    przycisk(r, tekst, cmd, "drugi").pack(side="right")
            etykieta(k, "Pełny przewodnik po aplikacji: przycisk „Jak zacząć” u góry. Ta karta zniknie po pierwszym zadaniu lub sesji.", 9, kolor=K["szary"], bg=K["nieb_tlo"], wrap=860).pack(fill="x", pady=(6, 0))

        # powrót po przerwie
        dni = self.stan.dni_od_ostatniej_sesji()
        if dni is not None and dni >= 2:
            z, k = karta(w, bg=K["zolty"])
            z.pack(fill="x", padx=28, pady=(14, 0))
            etykieta(k, f"Minęło {dni} dni od ostatniej sesji.", 11, bold=True, bg=K["zolty"]).pack(fill="x")
            etykieta(k, random.choice(P.motywacja_powrot) if P.motywacja_powrot else "Zacznij od jednego małego zadania.", 10, bg=K["zolty"], wrap=860).pack(fill="x", pady=(2, 0))

        # statystyki
        rzad = tk.Frame(w, bg=K["tlo"])
        rzad.pack(fill="x", padx=28, pady=(16, 0))
        tydz = self.stan.biezacy_tydzien()
        proc = int(100 * s["zadania_ukonczone"] / s["zadania_wszystkie"])
        kafle = [
            ("🔥", f"{s['seria']}", "dni serii", f"rekord: {s['najdluzsza_seria']}"),
            ("⭐", f"{s['xp']}", "XP", f"{len(self.stan.d['odznaki'])}/{len(odznaki())} odznak"),
            ("📅", f"{tydz}/{P.tygodnie[-1]['tydzien']}", "tydzień", P.tydzien(tydz)["tytul"]),
            ("📈", f"{proc}%", "programu", f"{s['zadania_ukonczone']}/{s['zadania_wszystkie']} zadań"),
            ("⏳", czas_hm(s["minuty"]), "nauki", f"{s['dni_nauki']} dni z sesją"),
        ]
        for i, (ik, duze, male, pod) in enumerate(kafle):
            z, k = karta(rzad, padx=14, pady=10)
            z.grid(row=0, column=i, sticky="nsew", padx=(0, 10))
            rzad.columnconfigure(i, weight=1)
            tk.Label(k, text=f"{ik} {duze}", font=czc(16, "bold"), bg=K["karta"], fg=K["tekst"], anchor="w").pack(fill="x")
            etykieta(k, male, 9, kolor=K["szary"]).pack(fill="x")
            etykieta(k, pod, 8, kolor=K["szary"]).pack(fill="x")

        # dzisiaj
        tytul, opis, zadanie, tydz_z = self._zadanie_dnia()
        z, k = karta(w, tytul="Dzisiaj")
        z.pack(fill="x", padx=28, pady=(16, 0))
        etykieta(k, tytul, 13, bold=True, kolor=K["akcent"], wrap=860).pack(fill="x")
        etykieta(k, opis, 10, wrap=860).pack(fill="x", pady=(4, 8))
        bt = tk.Frame(k, bg=K["karta"])
        bt.pack(fill="x")
        przycisk(bt, "▶ Zacznij sesję (90 min)", lambda: self.pokaz("sesja")).pack(side="left")
        if zadanie:
            przycisk(bt, "✔ Oznacz jako zrobione", lambda: (self.stan.oznacz(zadanie, True), self._odznaki_popup(), self.pokaz("panel")),
                     "drugi").pack(side="left", padx=8)
            przycisk(bt, "Jak to zrobić (Plan)", lambda: self.pokaz_tydzien(tydz_z), "drugi").pack(side="left")
            lekcje_dnia = P.lekcje_tygodnia(tydz_z)
            if lekcje_dnia:
                przycisk(bt, "📖 Lekcja", lambda: self.pokaz_lekcje(lekcje_dnia[0]["id"]), "drugi").pack(side="left", padx=8)
        elif d.weekday() == 5:
            przycisk(bt, "Zrób quiz tygodnia", lambda: self.pokaz("quiz"), "drugi").pack(side="left", padx=8)

        # dwie kolumny: etapy + wskazówka/odznaki
        kol = tk.Frame(w, bg=K["tlo"])
        kol.pack(fill="x", padx=28, pady=(16, 24))
        kol.columnconfigure(0, weight=3)
        kol.columnconfigure(1, weight=2)
        z, k = karta(kol, tytul="Postęp etapów")
        z.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
        for e in P.etapy:
            zrob = sum(self.stan.postep_tygodnia(P.tydzien(t))[0] for t in e["tygodnie"])
            wsz = sum(self.stan.postep_tygodnia(P.tydzien(t))[1] for t in e["tygodnie"])
            r = tk.Frame(k, bg=K["karta"])
            r.pack(fill="x", pady=3)
            etykieta(r, f"Etap {e['nr']}: {e['nazwa']}", 10, bold=(zrob < wsz and zrob > 0)).pack(fill="x")
            pb = ttk.Progressbar(r, maximum=wsz, value=zrob)
            pb.pack(fill="x", pady=(2, 0))
            etykieta(r, f"{zrob}/{wsz} zadań · tygodnie {e['tygodnie'][0]}–{e['tygodnie'][-1]}", 8, kolor=K["szary"]).pack(fill="x")

        prawa = tk.Frame(kol, bg=K["tlo"])
        prawa.grid(row=0, column=1, sticky="nsew")
        z, k = karta(prawa, tytul="💡 Wskazówka dnia")
        z.pack(fill="x")
        etykieta(k, P.wskazowki[d.timetuple().tm_yday % len(P.wskazowki)] if P.wskazowki else "Dziś bez wskazówki — ten program ich nie ma.", 10, wrap=360).pack(fill="x")
        z, k = karta(prawa, tytul="🏅 Odznaki")
        z.pack(fill="x", pady=(10, 0))
        zdob = [o for o in odznaki() if o["id"] in self.stan.d["odznaki"]]
        if zdob:
            etykieta(k, "  ".join(o["ikona"] for o in zdob), 16).pack(fill="x")
            etykieta(k, ", ".join(o["nazwa"] for o in zdob[-4:]), 9, kolor=K["szary"], wrap=360).pack(fill="x")
        else:
            etykieta(k, "Jeszcze żadnej. Pierwsza za pierwszą zapisaną sesję.", 9, kolor=K["szary"], wrap=360).pack(fill="x")
        nast = next((o for o in odznaki() if o["id"] not in self.stan.d["odznaki"]), None)
        if nast:
            etykieta(k, f"Następna: {nast['ikona']} {nast['nazwa']} — {nast['opis']}", 9, kolor=K["akcent"], wrap=360).pack(fill="x", pady=(6, 0))

    def _zadanie_dnia(self):
        d = dzis().weekday()
        tydz = self.stan.biezacy_tydzien()
        w = P.tydzien(tydz)
        nie = [z for z in w["zadania"] if not self.stan.zrobione(z["id"])]
        if d == 6:
            return ("Niedziela — wolne", "Mózg utrwala w przerwie. Seria nie przerywa się w niedzielę. "
                    "Jeśli naprawdę chcesz — przejrzyj dziennik albo zrób quiz powtórkowy.", None, tydz)
        if d == 5:
            return (f"Sobota — quiz z tygodnia {tydz} + poprawki + README (45 min)",
                    "Bez nowej teorii. Quiz w zakładce Quiz (albo z Asystentem: „quiz z tygodnia N”), poprawki po recenzji, "
                    "porządek w katalogu projektu i wpis w Dzienniku. " + (f"Zostało Ci jeszcze {len(nie)} zadań z tego tygodnia." if nie else "Tydzień masz zaliczony — brawo."),
                    None, tydz)
        if not nie:
            if all(self.stan.tydzien_ukonczony(x) for x in P.tygodnie):
                return ("Program ukończony 🎓", f"„{P.nazwa}” — wszystkie zadania odhaczone. Utrzymuj serię: powtórka z najsłabszego quizu, "
                        "wpis w Dzienniku, albo wgraj następny program w Ustawieniach.", None, tydz)
            return (f"Tydzień {tydz} ukończony", "Wszystkie zadania odhaczone. Zrób quiz i checklistę etapu, a potem rusz dalej.", None, tydz)
        ostatnie = w["zadania"][-1]
        if d == 4 and len(w["zadania"]) > 1 and not self.stan.zrobione(ostatnie["id"]):
            z = ostatnie
        else:
            z = nie[0]
        if z is ostatnie and len(w["zadania"]) > 1:
            etykieta_dnia = "Piątek — zadanie tygodnia (bez nowej teorii)" if d == 4 else f"{DNI[d]} — zostało zadanie tygodnia (piątkowe)"
        else:
            etykieta_dnia = f"{DNI[d]} — tydzień {tydz}: {w['tytul']}"
        tytul = z["tytul"].replace("Piątek: ", "", 1)
        opis = z.get("opis", "")
        if z.get("kroki"):
            opis += f"\n\nPierwszy krok: {z['kroki'][0][:220]}{'…' if len(z['kroki'][0]) > 220 else ''}\n(Pełna instrukcja — {len(z['kroki'])} kroków — w Planie.)"
        return (f"{etykieta_dnia}\n{tytul}", opis + f"\n\nTematy tygodnia: {w.get('tematy', '')}", z, tydz)

    # =================================================================== PLAN
    def widok_plan(self, tydzien=None):
        if tydzien is None:
            tydzien = self.stan.biezacy_tydzien()
        self._naglowek(self.tresc, f"Plan — {P.liczba_tygodni()} tygodni", "Odhaczaj, gdy efekt zadania jest w katalogu projektu (i w commicie, jeśli używasz Gita). "
                       "Zadania 1–4 to pon–czw, zadanie 5 to piątek.")
        cialo = tk.Frame(self.tresc, bg=K["tlo"])
        cialo.pack(fill="both", expand=True, padx=28, pady=(0, 20))
        lewa = tk.Frame(cialo, bg=K["tlo"], width=270)
        lewa.pack(side="left", fill="y")
        lewa.pack_propagate(False)
        for w in P.tygodnie:
            z, c = self.stan.postep_tygodnia(w)
            akt = w["tydzien"] == tydzien
            ok = z == c
            bg = K["akcent"] if akt else (K["ziel_tlo"] if ok else K["karta"])
            fg = K["btn_tekst"] if akt else K["tekst"]
            r = tk.Frame(lewa, bg=bg, highlightbackground=K["ramka"], highlightthickness=1, cursor="hand2")
            r.pack(fill="x", pady=1)
            p = tk.Label(r, text=f"{z}/{c}", font=czc(8, "bold"), bg=bg, fg=fg if akt else (K["ziel"] if ok else K["szary"]), padx=8)
            p.pack(side="right")
            tytul = w["tytul"] if len(w["tytul"]) <= 22 else w["tytul"][:21] + "…"
            t = tk.Label(r, text=f"{'✔ ' if ok else ''}T{w['tydzien']}: {tytul}", font=czc(10, "bold" if akt else "normal"),
                         bg=bg, fg=fg, anchor="w", padx=10, pady=5)
            t.pack(side="left", fill="x", expand=True)
            for wid in (r, t, p):
                wid.bind("<Button-1>", lambda e, n=w["tydzien"]: self.pokaz_tydzien(n))

        prawa = Przewijane(cialo, K["tlo"])
        prawa.pack(side="left", fill="both", expand=True, padx=(16, 0))
        w = P.tydzien(tydzien)
        e = P.etap_tygodnia(w["tydzien"])
        z, k = karta(prawa.wnetrze)
        z.pack(fill="x")
        plakietka(k, f"ETAP {e['nr']} · {e['nazwa'].upper()}", K["nieb_tlo"], K["nieb"]).pack(anchor="w")
        WRAP = 560
        etykieta(k, f"Tydzień {w['tydzien']}: {w['tytul']}", 15, bold=True, wrap=WRAP).pack(fill="x", pady=(6, 0))
        etykieta(k, "Tematy: " + w["tematy"], 10, wrap=WRAP).pack(fill="x", pady=(4, 0))
        etykieta(k, "Rola asystenta: " + w.get("rola_asystenta", ""), 10, kolor=K["szary"], wrap=WRAP).pack(fill="x", pady=(4, 0))
        etykieta(k, "Cel etapu: " + e.get("cel", ""), 9, kolor=K["szary"], wrap=WRAP).pack(fill="x", pady=(4, 0))
        lekcje = P.lekcje_tygodnia(w["tydzien"])
        if lekcje:
            etykieta(k, "Lekcje tygodnia (przeczytaj przed zadaniem):", 10, bold=True).pack(fill="x", pady=(8, 2))
            for l in lekcje:
                zal = self.stan.d.get("lekcje", {}).get(l["id"])
                ok = bool(zal and zal["max"] and zal["wynik"] / zal["max"] >= 0.67)
                lr = tk.Frame(k, bg=K["karta"])
                lr.pack(fill="x", pady=1)
                przycisk(lr, ("✔ " if ok else "📖 ") + l["nazwa"], lambda lid=l["id"]: self.pokaz_lekcje(lid), "drugi").pack(side="left")
                if zal:
                    etykieta(lr, f"  test {zal['wynik']}/{zal['max']}", 9, kolor=K["ziel"] if ok else K["pomar"]).pack(side="left")

        wykryte = self._wykryj_pliki(w)
        n_zad = len(w["zadania"])
        for i, zad in enumerate(w["zadania"]):
            piatek = (i == n_zad - 1) and n_zad > 1
            z, k = karta(prawa.wnetrze, bg=K["zolty"] if piatek else K["karta"])
            z.pack(fill="x", pady=(8, 0))
            bg = z.cget("bg")
            # górny rząd: plakietki (status, XP, wykrycie)
            g0 = tk.Frame(k, bg=bg)
            g0.pack(fill="x")
            dzien_nazwa = (DNI[i].upper() if i < 7 else f"ZADANIE {i + 1}")
            plakietka(g0, "ZADANIE TYGODNIA" if piatek else dzien_nazwa, K["jasny"] if not piatek else K["zolty"],
                      K["szary"] if not piatek else K["pomar"]).pack(side="left")
            plakietka(g0, f"+{zad['xp']} XP", K["jasny"], K["szary"]).pack(side="left", padx=6)
            plakietka(g0, f"~{zad.get('czas_min', 60)} min", K["jasny"], K["szary"]).pack(side="left", padx=(0, 6))
            if zad["pliki"]:
                if wykryte.get(zad["id"]):
                    plakietka(g0, f"✔ wykryto {wykryte[zad['id']]}", K["ziel_tlo"], K["ziel"]).pack(side="left")
                elif self.stan.d["projekt"]:
                    plakietka(g0, "plik nie wykryty", K["jasny"], K["szary"]).pack(side="left")
            if self.stan.zrobione(zad["id"]):
                plakietka(g0, f"✔ zrobione {self.stan.d['zadania'][zad['id']]}", K["ziel_tlo"], K["ziel"]).pack(side="right")
            # dolny rząd: checkbox + tytuł
            g = tk.Frame(k, bg=bg)
            g.pack(fill="x", pady=(6, 0))
            var = tk.BooleanVar(value=self.stan.zrobione(zad["id"]))
            cb = tk.Checkbutton(g, variable=var, bg=bg, activebackground=bg, fg=K["tekst"], selectcolor=K["jasny"], cursor="hand2",
                                command=lambda v=var, zz=zad: self._przelacz_zadanie(zz, v.get()))
            cb.pack(side="left", anchor="n")
            tytul = zad["tytul"].replace("Piątek: ", "", 1)
            etykieta(g, tytul, 11, bold=True, bg=bg, wrap=WRAP - 30).pack(side="left", fill="x", expand=True)
            if zad.get("opis"):
                etykieta(k, zad["opis"], 10, bg=bg, wrap=WRAP - 30).pack(fill="x", padx=(26, 0), pady=(2, 0))
            self._kroki_zadania(k, zad, bg, WRAP - 30)

        z, k = karta(prawa.wnetrze)
        z.pack(fill="x", pady=(8, 0))
        r = tk.Frame(k, bg=K["karta"])
        r.pack(fill="x")
        if P.quiz_tygodnia(tydzien):
            przycisk(r, f"Quiz z tygodnia {tydzien}", lambda: self.pokaz_quiz(tydzien)).pack(side="left")
        if P.prompty:
            przycisk(r, "Prompt „Nowy temat” do Asystenta", lambda: self.pokaz_asystenta(None,
                P.prompty[0]["tresc"].replace("[temat]", w.get("tematy", ""))), "drugi").pack(side="left", padx=8)
        if self.stan.d["projekt"]:
            przycisk(r, "Otwórz Claude Code w projekcie", self.otworz_claude, "ciemny").pack(side="left")

    def pokaz_tydzien(self, n):
        self.pokaz("plan")
        for ch in self.tresc.winfo_children():
            ch.destroy()
        self.widok_plan(n)

    def _kroki_zadania(self, k, zad, bg, wrap):
        """Rozwijana sekcja „Jak to zrobić”: kroki, sprawdzenie, typowe problemy."""
        kroki = zad.get("kroki") or []
        if not kroki and not zad.get("sprawdz"):
            return
        klucz = "rozwin-" + zad["id"]
        otwarte = self.stan.d.setdefault("rozwiniete", {}).get(klucz, not self.stan.zrobione(zad["id"]))
        box = tk.Frame(k, bg=bg)
        box.pack(fill="x", padx=(26, 0), pady=(6, 0))
        naglowek = tk.Label(box, text=("▾ " if otwarte else "▸ ") + f"Jak to zrobić — {len(kroki)} krok{'ów' if len(kroki) != 1 else ''}",
                            font=czc(10, "bold"), bg=bg, fg=K["akcent"], cursor="hand2", anchor="w")
        naglowek.pack(fill="x")
        tresc = tk.Frame(box, bg=bg)

        def przelacz(_=None):
            stan = not self.stan.d["rozwiniete"].get(klucz, otwarte)
            self.stan.d["rozwiniete"][klucz] = stan
            self.stan.zapisz()
            naglowek.configure(text=("▾ " if stan else "▸ ") + naglowek.cget("text")[2:])
            if stan:
                tresc.pack(fill="x", pady=(4, 0))
            else:
                tresc.pack_forget()

        naglowek.bind("<Button-1>", przelacz)
        for i, krok in enumerate(kroki, 1):
            r = tk.Frame(tresc, bg=bg)
            r.pack(fill="x", pady=2)
            tk.Label(r, text=f"{i}.", font=czc(10, "bold"), bg=bg, fg=K["akcent"], width=3, anchor="ne").pack(side="left", anchor="n")
            self._tekst_z_kodem(r, krok, bg, wrap - 30)
        if zad.get("sprawdz"):
            r = tk.Frame(tresc, bg=K["ziel_tlo"])
            r.pack(fill="x", pady=(8, 0))
            etykieta(r, "✔ Gotowe, gdy: " + zad["sprawdz"], 10, bg=K["ziel_tlo"], kolor=K["ziel"], wrap=wrap - 20).pack(fill="x", padx=8, pady=6)
        if zad.get("problemy"):
            r = tk.Frame(tresc, bg=K["jasny"])
            r.pack(fill="x", pady=(6, 0))
            etykieta(r, "Gdy coś nie działa:", 9, bold=True, bg=K["jasny"], kolor=K["szary"]).pack(fill="x", padx=8, pady=(6, 0))
            for pr in zad["problemy"]:
                etykieta(r, "• " + pr, 9, bg=K["jasny"], kolor=K["szary"], wrap=wrap - 20).pack(fill="x", padx=8, pady=(2, 0))
            tk.Frame(r, bg=K["jasny"], height=6).pack()
        if otwarte:
            tresc.pack(fill="x", pady=(4, 0))

    def _tekst_z_kodem(self, parent, tekst, bg, wrap):
        """Akapit, w którym linie po \n wyglądające na komendy/kod pokazujemy czcionką mono."""
        czesci = tekst.split("\n")
        kol = tk.Frame(parent, bg=bg)
        kol.pack(side="left", fill="x", expand=True)
        for cz in czesci:
            if not cz.strip():
                continue
            kodowe = cz.strip().startswith(("git ", "python", "pip ", "cd ", "irm ", "curl ", "print(", "import ", "from ", "def ", "@", "pytest", ".venv", "claude", "PS", "mkdir", "echo "))
            if kodowe:
                tk.Label(kol, text=cz.strip(), font=czc(9, mono=True), bg=K["jasny"], fg=K["tekst"], anchor="w", justify="left",
                         padx=8, pady=3, wraplength=wrap).pack(fill="x", pady=1)
            else:
                etykieta(kol, cz, 10, bg=bg, wrap=wrap).pack(fill="x")

    def _przelacz_zadanie(self, zad, wartosc):
        self.stan.oznacz(zad, wartosc)
        if wartosc:
            w = next(w for w in P.tygodnie if zad in w["zadania"])
            if self.stan.tydzien_ukonczony(w):
                messagebox.showinfo("Tydzień zaliczony!", f"Tydzień {w['tydzien']} ({w['tytul']}) ukończony.\n\n"
                                    "Zanim ruszysz dalej: quiz z tego tygodnia i checklista etapu. "
                                    "Jeśli coś w checkliście zostaje puste — dodaj tydzień, nie skracaj.", parent=self)
        self._odznaki_popup()
        self.pokaz_tydzien(next(w["tydzien"] for w in P.tygodnie if zad in w["zadania"]))

    # ---------------------------------------------------------- wykrywanie plików
    def _lista_plikow_projektu(self):
        sciezka = self.stan.d["projekt"]
        if not sciezka or not Path(sciezka).is_dir():
            return set()
        if sciezka in self._pliki_cache:
            return self._pliki_cache[sciezka]
        nazwy = set()
        licznik = 0
        for root, dirs, files in os.walk(sciezka):
            dirs[:] = [d for d in dirs if d not in POMIJANE_KATALOGI]
            nazwy.update(files)
            nazwy.update(dirs)
            licznik += len(files)
            if licznik > 20000:
                break
        if (Path(sciezka) / ".git").exists():
            nazwy.add(".git")
        self._pliki_cache[sciezka] = nazwy
        return nazwy

    def _wykryj_pliki(self, tydzien):
        nazwy = self._lista_plikow_projektu()
        wynik = {}
        for z in tydzien["zadania"]:
            for p in z["pliki"]:
                if p in nazwy:
                    wynik[z["id"]] = p
                    break
        return wynik

    # ================================================================== SESJA
    def _sek_fazy(self, i):
        return int(P.rytm_dnia[i]["minuty"] * self.stan.d.get("skala_sesji", 1.0) * 60)

    def widok_sesja(self):
        w = self._strona("Sesja nauki", "Rytm dnia 20 / 50 / 15 / 5 minut. Dzwonek na końcu każdej fazy. "
                         "Minuty zapisują się automatycznie — to z nich liczy się seria.")
        kol = tk.Frame(w, bg=K["tlo"])
        kol.pack(fill="x", padx=28)
        kol.columnconfigure(0, weight=3)
        kol.columnconfigure(1, weight=2)

        # lewa: zegar
        z, k = karta(kol)
        z.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
        tr = tk.Frame(k, bg=K["karta"])
        tr.pack(fill="x", pady=(0, 6))
        etykieta(tr, "Temat sesji: ", 10).pack(side="left")
        self.t_temat_var = tk.StringVar(value=self.t_temat or (P.lekcje_tygodnia(self.stan.biezacy_tydzien())[0]["nazwa"] if P.lekcje_tygodnia(self.stan.biezacy_tydzien()) else P.tydzien(self.stan.biezacy_tydzien()).get("tematy", "")))
        cb = ttk.Combobox(tr, textvariable=self.t_temat_var, values=self._lista_tematow(), width=42, font=czc(10))
        cb.pack(side="left")
        cb.bind("<<ComboboxSelected>>", lambda e: setattr(self, "t_temat", self.t_temat_var.get()))
        cb.bind("<FocusOut>", lambda e: setattr(self, "t_temat", self.t_temat_var.get()))
        f = P.rytm_dnia[min(self.t_faza, len(P.rytm_dnia) - 1)]
        self.t_faza_naglowek = etykieta(k, f"{f['ikona']}  Faza {self.t_faza + 1}/{len(P.rytm_dnia)}: {f['nazwa']}", 13, bold=True, kolor=K["akcent"])
        self.t_faza_naglowek.pack(fill="x")
        self.t_etykieta = tk.Label(k, text=self._fmt(self.t_pozostalo), font=czc(56, "bold", mono=True), bg=K["karta"], fg=K["tekst"])
        self.t_etykieta.pack(pady=(6, 2))
        self.t_opis = etykieta(k, f["opis"], 10, kolor=K["szary"], wrap=400, anchor="center")
        self.t_opis.pack(fill="x")
        bt = tk.Frame(k, bg=K["karta"])
        bt.pack(pady=12)
        self.t_przycisk = przycisk(bt, "⏸ Pauza" if self.t_dziala else "▶ Start", self._timer_start_pauza, szer=12)
        self.t_przycisk.pack(side="left", padx=4)
        przycisk(bt, "⏭ Pomiń fazę", self._timer_pomin, "drugi").pack(side="left", padx=4)
        przycisk(bt, "↺ Od nowa", self._timer_reset, "drugi").pack(side="left", padx=4)
        sk = tk.Frame(k, bg=K["karta"])
        sk.pack()
        etykieta(sk, "Długość sesji:", 9, kolor=K["szary"]).pack(side="left")
        for nazwa, skala in (("pełna 90 min", 1.0), ("skrócona 45 min", 0.5), ("mini 30 min", 0.34)):
            akt = abs(self.stan.d.get("skala_sesji", 1.0) - skala) < 0.01
            tk.Button(sk, text=nazwa, relief="flat", bd=0, cursor="hand2", font=czc(9, "bold" if akt else "normal"),
                      bg=K["ziel_tlo"] if akt else K["jasny"], fg=K["ziel"] if akt else K["tekst"], padx=8, pady=3,
                      command=lambda s=skala: self._ustaw_skale(s)).pack(side="left", padx=3)

        # prompt do bieżącej fazy
        z2, k2 = karta(w, tytul="Prompt do tej fazy (wklej w Claude Code)")
        z2.pack(fill="x", padx=28, pady=(10, 0))
        self.t_prompt = tk.Text(k2, height=4, font=czc(10), wrap="word", bg=K["jasny"], fg=K["tekst"], insertbackground=K["tekst"], relief="flat", padx=10, pady=8)
        self.t_prompt.pack(fill="x")
        self.t_prompt.insert("1.0", f["prompt"])
        self.t_prompt.configure(state="disabled")
        r = tk.Frame(k2, bg=K["karta"])
        r.pack(fill="x", pady=(8, 0))
        przycisk(r, "Wypełnij [nawiasy] i skopiuj", lambda: self._wypelnij_i_skopiuj(P.rytm_dnia[min(self.t_faza, 3)]["prompt"]), "drugi").pack(side="left")
        przycisk(r, "Wyślij do Asystenta", lambda: self.pokaz_asystenta(None, P.rytm_dnia[min(self.t_faza, 3)]["prompt"]), "drugi").pack(side="left", padx=8)
        przycisk(r, "Otwórz Claude Code", self.otworz_claude, "ciemny").pack(side="left")

        # prawa: fazy + walka + ręczny zapis
        prawa = tk.Frame(kol, bg=K["tlo"])
        prawa.grid(row=0, column=1, sticky="nsew")
        z, k = karta(prawa, tytul="Plan sesji")
        z.pack(fill="x")
        self.t_faza_etykiety = []
        for i, fz in enumerate(P.rytm_dnia):
            minuty = round(fz["minuty"] * self.stan.d.get("skala_sesji", 1.0))
            stan = "✔" if i < self.t_faza else ("▶" if i == self.t_faza else "·")
            lab = etykieta(k, f"{stan}  {fz['ikona']} {fz['nazwa']} — {minuty} min", 10, bold=(i == self.t_faza),
                           kolor=K["akcent"] if i == self.t_faza else (K["szary"] if i < self.t_faza else K["tekst"]))
            lab.pack(fill="x", pady=2)
            self.t_faza_etykiety.append(lab)

        z, k = karta(prawa, tytul="🥊 Utknąłem — 15 min walki", bg=K["zolty"])
        z.pack(fill="x", pady=(10, 0))
        etykieta(k, "Zasada nr 1: zanim zapytasz Claude, próbuj sam. Włącz licznik; gdy dojdzie do zera, "
                 "masz prawo użyć promptu „Utknąłem”.", 9, bg=K["zolty"], wrap=340).pack(fill="x")
        self.walka_etykieta = tk.Label(k, text=self._walka_tekst(), font=czc(20, "bold", mono=True), bg=K["zolty"], fg=K["pomar"])
        self.walka_etykieta.pack(pady=4)
        przycisk(k, "Start 15 min", self._walka_start, "ostrz").pack()

        z, k = karta(prawa, tytul="Sesja bez timera?")
        z.pack(fill="x", pady=(10, 0))
        etykieta(k, "Uczyłeś się poza aplikacją — dopisz czas ręcznie: podasz temat i odpowiesz na 3–4 pytania z tego tematu. "
                 "XP za dzień nauki przyznaje się raz na dobę.", 9, kolor=K["szary"], wrap=340).pack(fill="x")
        przycisk(k, "➕ Dopisz czas nauki…", self._zapisz_recznie, "drugi").pack(anchor="w", pady=(6, 0))
        dzien = self.stan.d["sesje"].get(str(dzis()))
        dzisiejsze = self.stan.minuty_dnia(str(dzis()))
        etykieta(k, f"Dziś zapisane: {czas_hm(dzisiejsze)}", 9, kolor=K["ziel"]).pack(fill="x", pady=(6, 0))
        if isinstance(dzien, dict):
            for wp in dzien.get("wpisy", [])[-4:]:
                t = wp.get("test")
                etykieta(k, f"  {wp.get('godzina', '')} · {wp['minuty']} min · {wp.get('temat') or '(bez tematu)'}"
                         + (f" · test {t['wynik']}/{t['max']}" if t else "") + (" · timer" if wp.get("zrodlo") == "timer" else ""),
                         8, kolor=K["szary"], wrap=330).pack(fill="x")
        tk.Frame(w, bg=K["tlo"], height=20).pack()

    def _lista_tematow(self):
        """Tematy do wyboru przy wpisie czasu: lekcje bieżącego tygodnia najpierw, potem reszta, potem ostatnio wpisane."""
        tydz = self.stan.biezacy_tydzien()
        biez = [l["nazwa"] for l in P.lekcje_tygodnia(tydz)]
        reszta = [l["nazwa"] for l in P.lekcje if l["nazwa"] not in biez]
        ost = [t for t in self.stan.tematy_ostatnie() if t not in biez and t not in reszta]
        return biez + reszta + ost

    @staticmethod
    def _fmt(sek):
        m, s = divmod(max(0, int(sek)), 60)
        return f"{m:02d}:{s:02d}"

    def _ustaw_skale(self, s):
        self.stan.d["skala_sesji"] = s
        self.stan.zapisz()
        self._timer_reset()

    def _timer_start_pauza(self):
        if self.t_faza >= len(P.rytm_dnia):
            self._timer_reset()
        self.t_dziala = not self.t_dziala
        if self.t_przycisk and self.t_przycisk.winfo_exists():
            self.t_przycisk.configure(text="⏸ Pauza" if self.t_dziala else "▶ Start")

    def _timer_pomin(self):
        if self.t_faza < len(P.rytm_dnia):
            przepracowane = (self._sek_fazy(self.t_faza) - self.t_pozostalo) / 60
            if przepracowane >= 1:
                self.stan.dodaj_minuty(round(przepracowane), temat=self.t_temat, zrodlo="timer")
            self._nastepna_faza(cicho=True)

    def _timer_reset(self):
        self.t_faza = 0
        self.t_dziala = False
        self.t_pozostalo = self._sek_fazy(0)
        if self.aktywny == "sesja":
            self.pokaz("sesja")

    def _nastepna_faza(self, cicho=False):
        self.t_dziala = False
        self.t_faza += 1
        if self.t_faza < len(P.rytm_dnia):
            self.t_pozostalo = self._sek_fazy(self.t_faza)
            if not cicho:
                f = P.rytm_dnia[self.t_faza]
                messagebox.showinfo("Koniec fazy", f"Faza zakończona.\n\nNastępna: {f['ikona']} {f['nazwa']} ({round(f['minuty'] * self.stan.d.get('skala_sesji', 1.0))} min)\n\n{f['opis']}", parent=self)
        else:
            self.t_pozostalo = 0
            if not cicho:
                messagebox.showinfo("Sesja zakończona 🎉", "Cała sesja za Tobą. Zrób commit, odhacz zadanie w Planie "
                                    "i wpisz 2 zdania do Dziennika — to utrwala najmocniej.", parent=self)
        self._odznaki_popup()
        if self.aktywny == "sesja":
            self.pokaz("sesja")

    def _petla(self):
        if self.t_dziala and self.t_faza < len(P.rytm_dnia):
            self.t_pozostalo -= 1
            if self.t_etykieta and self.t_etykieta.winfo_exists():
                self.t_etykieta.configure(text=self._fmt(self.t_pozostalo))
            if self.t_pozostalo <= 0:
                self.bell()
                self.stan.dodaj_minuty(round(P.rytm_dnia[self.t_faza]["minuty"] * self.stan.d.get("skala_sesji", 1.0)), temat=self.t_temat, zrodlo="timer")
                self._nastepna_faza()
        if self.walka_koniec and self.walka_etykieta and self.walka_etykieta.winfo_exists():
            self.walka_etykieta.configure(text=self._walka_tekst())
            if dt.datetime.now() >= self.walka_koniec:
                self.walka_koniec = None
                self.bell()
                messagebox.showinfo("15 minut minęło", "Walczyłeś uczciwie. Teraz możesz użyć promptu „Utknąłem” — "
                                    "ale nadal proś o pytanie naprowadzające, nie o rozwiązanie.", parent=self)
        self.after(1000, self._petla)

    def _walka_tekst(self):
        if not self.walka_koniec:
            return "15:00"
        return self._fmt((self.walka_koniec - dt.datetime.now()).total_seconds())

    def _walka_start(self):
        self.walka_koniec = dt.datetime.now() + dt.timedelta(minutes=15)

    def _zapisz_recznie(self):
        self.pokaz("wpis")

    def widok_wpis(self):
        """Pełnoekranowy wpis czasu nauki (bez osobnego okna): minuty + temat → mini-test z tematu (3–4 pytania) → zapis."""
        strona = self._strona("Dopisz czas nauki", "Czas spoza aplikacji liczy się do serii i statystyk. Podaj temat i odpowiedz na kilka pytań z tego tematu — "
                              "bez testu wpis nie powstaje. XP za dzień nauki przyznaje się raz na dobę.")
        ramka = tk.Frame(strona, bg=K["karta"], highlightbackground=K["ramka"], highlightthickness=1)
        ramka.pack(fill="x", padx=28, pady=(0, 24))
        wew = tk.Frame(ramka, bg=K["karta"])
        wew.pack(fill="both", expand=True, padx=18, pady=14)
        okno = None  # zgodność z dawnym kodem dialogu
        etykieta(wew, "Krok 1 z 2 — co i jak długo", 12, bold=True).pack(fill="x")
        r = tk.Frame(wew, bg=K["karta"])
        r.pack(fill="x", pady=(10, 0))
        etykieta(r, "Minuty: ", 10).pack(side="left")
        min_var = tk.StringVar(value="60")
        pole_min = tk.Entry(r, textvariable=min_var, width=6, font=czc(10), relief="flat", bg=K["jasny"], fg=K["tekst"], insertbackground=K["tekst"])
        pole_min.pack(side="left", ipady=4)
        for m in (30, 45, 60, 90):
            tk.Button(r, text=str(m), relief="flat", bd=0, cursor="hand2", font=czc(9), bg=K["jasny"], fg=K["tekst"], padx=8, pady=3,
                      command=lambda m_=m: min_var.set(str(m_))).pack(side="left", padx=2)
        r_temat = tk.Frame(wew, bg=K["karta"])
        r_temat.pack(fill="x", pady=(10, 0))
        etykieta(r_temat, "Temat: ", 10).pack(side="left")
        temat_var = tk.StringVar(value=self.t_temat or "")
        cb = ttk.Combobox(r_temat, textvariable=temat_var, values=self._lista_tematow(), width=44, font=czc(10))
        cb.pack(side="left")
        etykieta(wew, "Wybierz lekcję z listy (wtedy dostaniesz test z jej pytań) albo wpisz własny temat — wtedy pytania będą z bieżącego tygodnia.",
                 9, kolor=K["szary"], wrap=820).pack(fill="x", pady=(6, 0))
        info = etykieta(wew, "", 9, kolor=K["czerw"], wrap=820)
        info.pack(fill="x", pady=(6, 0))
        test_ramka = tk.Frame(wew, bg=K["karta"])
        test_ramka.pack(fill="both", expand=True, pady=(10, 0))
        dol = tk.Frame(wew, bg=K["karta"])
        dol.pack(fill="x", pady=(8, 0))
        stan = {"pytania": [], "i": 0, "wynik": 0, "minuty": 0, "temat": ""}

        def pytania_dla(temat):
            l = P.lekcja_po_nazwie(temat)
            pula = list(l.get("test", [])) if l else []
            if len(pula) < 3:
                pula += [q for q in P.quiz_tygodnia(self.stan.biezacy_tydzien()) if q not in pula]
            if len(pula) < 3:
                pula += [q for lek in P.lekcje for q in lek.get("test", []) if q not in pula]
            random.shuffle(pula)
            return pula[:4] if len(pula) >= 4 else pula[:3], l

        def start_testu():
            try:
                m = int(min_var.get())
                if not 1 <= m <= 600:
                    raise ValueError
            except ValueError:
                info.configure(text="Podaj liczbę minut od 1 do 600.")
                return
            temat = temat_var.get().strip()
            if len(temat) < 3:
                info.configure(text="Wpisz temat (co najmniej 3 znaki) — bez tematu czas się nie liczy.")
                return
            pyt, lekcja = pytania_dla(temat)
            if not pyt:
                info.configure(text="Ten program nie ma żadnych pytań testowych — zapisuję bez testu.")
                zakoncz(m, temat, None, None)
                return
            stan.update({"pytania": pyt, "i": 0, "wynik": 0, "minuty": m, "temat": temat, "lekcja": lekcja})
            for ch in dol.winfo_children():
                ch.destroy()
            pole_min.configure(state="disabled", disabledbackground=K["jasny"], disabledforeground=K["szary"])
            cb.pack_forget()
            etykieta(r_temat, temat, 10, bold=True).pack(side="left")
            info.configure(text=f"{m} min · {temat}" + (" · pytania z tej lekcji" if lekcja else " · pytania z bieżącego tygodnia"), fg=K["szary"])
            pokaz_pytanie()

        def pokaz_pytanie():
            for ch in test_ramka.winfo_children():
                ch.destroy()
            q = stan["pytania"][stan["i"]]
            etykieta(test_ramka, f"Krok 2 z 2 — test z tematu „{stan['temat']}”  ·  pytanie {stan['i'] + 1}/{len(stan['pytania'])}", 11, bold=True, wrap=820).pack(fill="x")
            etykieta(test_ramka, q["p"], 11, wrap=820).pack(fill="x", pady=(8, 6))
            var = tk.IntVar(value=-1)
            radia = []
            for i, o in enumerate(q["o"]):
                rb = tk.Radiobutton(test_ramka, text=o, variable=var, value=i, font=czc(10), bg=K["karta"], activebackground=K["karta"],
                                    fg=K["tekst"], activeforeground=K["tekst"], selectcolor=K["jasny"], anchor="w", justify="left", wraplength=780, cursor="hand2", padx=6, pady=3)
                rb.pack(fill="x")
                radia.append(rb)
            wyn = etykieta(test_ramka, "", 10, wrap=820)
            wyn.pack(fill="x", pady=(6, 0))
            przyciski = tk.Frame(test_ramka, bg=K["karta"])
            przyciski.pack(fill="x", pady=(8, 0))

            def sprawdz():
                if var.get() < 0:
                    return
                dobrze = var.get() == q["odp"]
                for i, rb in enumerate(radia):
                    rb.configure(state="disabled", disabledforeground=K["ziel"] if i == q["odp"] else (K["czerw"] if i == var.get() else K["szary"]))
                if dobrze:
                    stan["wynik"] += 1
                    wyn.configure(text="✔ Dobrze. " + q.get("w", ""), fg=K["ziel"])
                else:
                    wyn.configure(text=f"✘ Poprawna: {q['o'][q['odp']]}. {q.get('w', '')}", fg=K["czerw"])
                b_spr.configure(state="disabled")
                b_dalej.configure(state="normal")

            def dalej():
                stan["i"] += 1
                if stan["i"] < len(stan["pytania"]):
                    pokaz_pytanie()
                else:
                    zakoncz(stan["minuty"], stan["temat"], {"wynik": stan["wynik"], "max": len(stan["pytania"])}, stan.get("lekcja"))

            b_spr = przycisk(przyciski, "Sprawdź", sprawdz)
            b_spr.pack(side="left")
            b_dalej = przycisk(przyciski, "Dalej →", dalej, "drugi")
            b_dalej.pack(side="left", padx=8)
            b_dalej.configure(state="disabled")

        def zakoncz(m, temat, test, lekcja):
            xp = self.stan.dodaj_minuty(m, temat=temat, zrodlo="recznie", test=test)
            if test and lekcja:
                self.stan.d.setdefault("lekcje", {})[lekcja["id"]] = {"wynik": test["wynik"], "max": test["max"], "data": str(dzis())}
                self.stan.zapisz()
            self._odznaki_popup()
            kom = f"Dodano {m} min · temat: {temat}."
            if test:
                kom += f"\nTest: {test['wynik']}/{test['max']}" + (" — bezbłędnie." if test["wynik"] == test["max"] else " — błędne pytania wrócą w Lekcjach.")
            kom += f"\n\n+{XP_SESJA_DNIA} XP za dzisiejszy dzień nauki." if xp else "\n\nXP za dzień nauki już dziś przyznane (raz na dobę)."
            messagebox.showinfo("Zapisano", kom, parent=self)
            self.pokaz("sesja")

        przycisk(dol, "Dalej → test z tematu", start_testu).pack(side="left")
        przycisk(dol, "Anuluj", lambda: self.pokaz("sesja"), "drugi").pack(side="left", padx=8)
        cb.focus_set()


    # ================================================================= LEKCJE
    def pokaz_lekcje(self, lid=None):
        self.lekcja_wybrana = lid
        self.pokaz("lekcje")

    def widok_lekcje(self):
        self._naglowek(self.tresc, "Lekcje", "Jedna lekcja dziennie, przed zadaniem: cel → wyjaśnienie → przykład → pułapki → zadania → pytania → test. "
                       "Pierwszy raz tutaj? Zacznij od pierwszej lekcji na liście — to wprowadzenie do programu. ✔ oznacza zaliczony test.")
        cialo = tk.Frame(self.tresc, bg=K["tlo"])
        cialo.pack(fill="both", expand=True, padx=28, pady=(0, 20))
        lewa = Przewijane(cialo, K["tlo"])
        lewa.pack(side="left", fill="y")
        lewa.canvas.configure(width=300)
        lid = getattr(self, "lekcja_wybrana", None)
        if lid is None:
            biez = P.lekcje_tygodnia(self.stan.biezacy_tydzien())
            lid = biez[0]["id"] if biez else (P.lekcje[0]["id"] if P.lekcje else None)
            self.lekcja_wybrana = lid
        ost_tydz = None
        for l in P.lekcje:
            if l["tydzien"] != ost_tydz:
                ost_tydz = l["tydzien"]
                tk.Label(lewa.wnetrze, text=f"Tydzień {l['tydzien']} — {P.tydzien(l['tydzien'])['tytul']}", font=czc(9, "bold"), bg=K["tlo"],
                         fg=K["szary"], anchor="w").pack(fill="x", pady=(8, 2))
            zal = self.stan.d.get("lekcje", {}).get(l["id"])
            ok = bool(zal and zal["max"] and zal["wynik"] / zal["max"] >= 0.67)
            akt = l["id"] == lid
            bg = K["akcent"] if akt else (K["ziel_tlo"] if ok else K["karta"])
            fg = K["btn_tekst"] if akt else K["tekst"]
            r = tk.Frame(lewa.wnetrze, bg=bg, highlightbackground=K["ramka"], highlightthickness=1, cursor="hand2")
            r.pack(fill="x", pady=1)
            t = tk.Label(r, text=("✔ " if ok else "") + l["nazwa"], font=czc(10, "bold" if akt else "normal"), bg=bg, fg=fg, anchor="w",
                         padx=10, pady=5, wraplength=270, justify="left")
            t.pack(fill="x")
            for wid in (r, t):
                wid.bind("<Button-1>", lambda e, i=l["id"]: self.pokaz_lekcje(i))

        prawa = Przewijane(cialo, K["tlo"])
        prawa.pack(side="left", fill="both", expand=True, padx=(16, 0))
        l = P.lekcja(lid) if lid else None
        if not l:
            etykieta(prawa.wnetrze, "Ten program nie ma lekcji.", 11, kolor=K["szary"]).pack(fill="x")
            return
        W = 600
        idx = [x["id"] for x in P.lekcje]
        poz = idx.index(l["id"]) if l["id"] in idx else 0
        z, k = karta(prawa.wnetrze)
        z.pack(fill="x")
        r0 = tk.Frame(k, bg=K["karta"])
        r0.pack(fill="x")
        plakietka(r0, f"TYDZIEŃ {l['tydzien']}", K["nieb_tlo"], K["nieb"]).pack(side="left")
        plakietka(r0, f"lekcja {poz + 1} z {len(idx)}", K["jasny"], K["szary"]).pack(side="left", padx=6)
        if l.get("czas_min"):
            plakietka(r0, f"≈ {l['czas_min']} min", K["jasny"], K["szary"]).pack(side="left")
        etykieta(k, l["nazwa"], 15, bold=True, wrap=W).pack(fill="x", pady=(6, 4))
        if l.get("cel"):
            etykieta(k, "🎯 Po tej lekcji: " + l["cel"], 10, bold=True, kolor=K["ziel"], wrap=W).pack(fill="x", pady=(0, 6))
        etykieta(k, "Jak pracować z lekcją:  1 przeczytaj wyjaśnienie  →  2 przelicz przykład sam  →  3 zrób zadania  →  4 odpowiedz na pytania na głos  →  5 test (2/3 zalicza)",
                 9, kolor=K["szary"], wrap=W).pack(fill="x", pady=(0, 8))
        etykieta(k, "1 · Wyjaśnienie", 11, bold=True).pack(fill="x", pady=(4, 4))
        for akapit in l["wyjasnienie"].split("\n"):
            a = akapit.strip()
            if not a:
                continue
            if a.startswith("## "):
                etykieta(k, a[3:], 10, bold=True, kolor=K["akcent"], wrap=W).pack(fill="x", pady=(6, 2))
            elif a.startswith(("- ", "• ")):
                etykieta(k, "• " + a[2:], 10, wrap=W).pack(fill="x", padx=(12, 0), pady=(0, 2))
            else:
                etykieta(k, a, 10, wrap=W).pack(fill="x", pady=(0, 6))
        if l.get("przyklad"):
            etykieta(k, "2 · Przykład — przelicz lub prześledź sam, zanim spojrzysz na wynik", 11, bold=True).pack(fill="x", pady=(8, 4))
            tk.Label(k, text=l["przyklad"], font=czc(10, mono=True), bg=K["jasny"], fg=K["tekst"], anchor="w", justify="left",
                     padx=12, pady=8, wraplength=W).pack(fill="x")
        if l.get("w_praktyce"):
            z2, k2 = karta(prawa.wnetrze, tytul="W praktyce — jak to robisz w firmie, krok po kroku")
            z2.pack(fill="x", pady=(8, 0))
            for i, kr in enumerate(l["w_praktyce"], 1):
                etykieta(k2, f"{i}. {kr}", 10, wrap=W).pack(fill="x", pady=(0, 3))
        if l.get("pulapki"):
            z2, k2 = karta(prawa.wnetrze, bg=K["zolty"])
            z2.pack(fill="x", pady=(8, 0))
            etykieta(k2, "3 · ⚠ Pułapki — zapisz do dziennika", 10, bold=True, bg=K["zolty"], kolor=K["pomar"]).pack(fill="x")
            for pu in l["pulapki"]:
                etykieta(k2, "• " + pu, 10, bg=K["zolty"], wrap=W).pack(fill="x", pady=(2, 0))
        if l.get("zadania"):
            z2, k2 = karta(prawa.wnetrze, tytul=f"4 · {len(l['zadania'])} zadania — zrób w katalogu projektu, bez rozwiązań")
            z2.pack(fill="x", pady=(8, 0))
            for i, zd in enumerate(l["zadania"], 1):
                etykieta(k2, f"{i}. {zd}", 10, wrap=W).pack(fill="x", pady=(0, 4))
        if l.get("pytania"):
            z2, k2 = karta(prawa.wnetrze, tytul="5 · Pytania sprawdzające — odpowiedz na głos, potem kliknij, by rozwinąć")
            z2.pack(fill="x", pady=(8, 0))
            for pq, odp in l["pytania"]:
                r = tk.Frame(k2, bg=K["karta"])
                r.pack(fill="x", pady=2)
                lab = etykieta(r, "▸ " + pq, 10, wrap=W)
                lab.pack(fill="x")
                lab.configure(cursor="hand2")
                lab.bind("<Button-1>", lambda e, w_=lab, o=odp, q_=pq: w_.configure(text=f"▾ {q_}\n   → {o}", fg=K["ziel"]))
        z2, k2 = karta(prawa.wnetrze)
        z2.pack(fill="x", pady=(8, 16))
        zal = self.stan.d.get("lekcje", {}).get(l["id"])
        r = tk.Frame(k2, bg=K["karta"])
        r.pack(fill="x")
        if l.get("test"):
            przycisk(r, f"6 · Sprawdź się — test ({len(l['test'])} pytania)", lambda: self._test_lekcji(l)).pack(side="left")
        if zal:
            plakietka(r, f"ostatni wynik {zal['wynik']}/{zal['max']} · {zal['data']}", K["ziel_tlo"] if zal["wynik"] / max(zal["max"], 1) >= 0.67 else K["czerw_tlo"],
                      K["ziel"] if zal["wynik"] / max(zal["max"], 1) >= 0.67 else K["czerw"]).pack(side="left", padx=10)
        przycisk(r, "Zapytaj Asystenta o ten temat", lambda: self.pokaz_asystenta(None, f"Uczę się: {l['nazwa']}. Wytłumacz na 2 przykładach z życia i daj 3 zadania. Nie podawaj rozwiązań."), "drugi").pack(side="left", padx=(0, 8))
        tydz_zad = [z for z in P.tydzien(l["tydzien"])["zadania"]]
        if tydz_zad:
            przycisk(r, f"Zadania tygodnia {l['tydzien']}", lambda: self.pokaz_tydzien(l["tydzien"]), "drugi").pack(side="left")
        nav = tk.Frame(k2, bg=K["karta"])
        nav.pack(fill="x", pady=(10, 0))
        if poz > 0:
            przycisk(nav, "← " + P.lekcje[poz - 1]["nazwa"][:38], lambda: self.pokaz_lekcje(P.lekcje[poz - 1]["id"]), "drugi").pack(side="left")
        if poz + 1 < len(idx):
            przycisk(nav, P.lekcje[poz + 1]["nazwa"][:38] + " →", lambda: self.pokaz_lekcje(P.lekcje[poz + 1]["id"]), "drugi").pack(side="right")

    def _test_lekcji(self, l):
        pytania = [(f"L{l['id']}-{i}", q) for i, q in enumerate(l["test"])]
        random.shuffle(pytania)
        self._uruchom_quiz(pytania, None, f"Test z lekcji: {l['nazwa']}", lekcja_id=l["id"])
    # ================================================================ PROJEKT
    # ================================================================ WARSZTAT
    def widok_warsztat(self):
        self._naglowek(self.tresc, "Warsztat", "Narzędzia wewnętrzne programu: liczysz, wypełniasz i „wysyłasz” tutaj — żadnych kont zewnętrznych ani instalacji. "
                       "Wyniki zapisujesz do katalogu projektu jednym przyciskiem.")
        cialo = tk.Frame(self.tresc, bg=K["tlo"])
        cialo.pack(fill="both", expand=True, padx=28, pady=(0, 20))
        lewa = tk.Frame(cialo, bg=K["tlo"], width=190)
        lewa.pack(side="left", fill="y")
        lewa.pack_propagate(False)
        dostepne = [n for n in warsztat.NARZEDZIA if n[0] in P.narzedzia]
        if not dostepne:
            etykieta(cialo, "Ten program nie ma narzędzi Warsztatu.", 11, kolor=K["szary"]).pack(fill="x", padx=16)
            return
        wyb = getattr(self, "narzedzie_wybrane", None)
        if wyb not in [n[0] for n in dostepne]:
            wyb = dostepne[0][0]
            self.narzedzie_wybrane = wyb
        for klucz, ikona, nazwa in dostepne:
            akt = klucz == wyb
            r = tk.Frame(lewa, bg=K["akcent"] if akt else K["karta"], highlightbackground=K["ramka"], highlightthickness=1, cursor="hand2")
            r.pack(fill="x", pady=2)
            l = tk.Label(r, text=f"{ikona}  {nazwa}", font=czc(10, "bold" if akt else "normal"), bg=r.cget("bg"), fg=K["btn_tekst"] if akt else K["tekst"], anchor="w", padx=10, pady=7)
            l.pack(fill="x")
            for wdg in (r, l):
                wdg.bind("<Button-1>", lambda e, kk=klucz: (setattr(self, "narzedzie_wybrane", kk), self.pokaz("warsztat")))
        prawa = Przewijane(cialo, K["tlo"])
        prawa.pack(side="left", fill="both", expand=True, padx=(16, 0))
        try:
            warsztat.zbuduj(self, prawa.wnetrze, wyb)
        except Exception as e:  # narzędzie nie może blokować całej aplikacji
            etykieta(prawa.wnetrze, f"Nie udało się zbudować narzędzia: {e}", 10, kolor=K["czerw"], wrap=700).pack(fill="x")

    def widok_projekt(self):
        w = self._strona("Mój projekt", "Mentor zagląda do katalogu projektu: sprawdza, czy pliki z zadań istnieją, "
                         "czy jest CLAUDE.md i co mówi Git. Nic nie zmienia bez Twojej zgody.")
        sciezka = self.stan.d["projekt"]
        z, k = karta(w, tytul="Katalog projektu")
        z.pack(fill="x", padx=28)
        etykieta(k, sciezka or "Nie wybrano. Wskaż katalog nauka-python.", 10, mono=bool(sciezka), kolor=K["tekst"] if sciezka else K["czerw"]).pack(fill="x")
        r = tk.Frame(k, bg=K["karta"])
        r.pack(fill="x", pady=(8, 0))
        przycisk(r, "Wybierz katalog…", self._wybierz_projekt, "drugi").pack(side="left")
        if sciezka:
            przycisk(r, "Odśwież", lambda: (self._pliki_cache.clear(), self.pokaz("projekt")), "drugi").pack(side="left", padx=8)
            przycisk(r, "Otwórz Claude Code tutaj", self.otworz_claude, "ciemny").pack(side="left")
            przycisk(r, "Otwórz folder", lambda: self._otworz_folder(sciezka), "drugi").pack(side="left", padx=8)
        if not sciezka or not Path(sciezka).is_dir():
            return

        p = Path(sciezka)
        # narzędzia
        z, k = karta(w, tytul="Narzędzia")
        z.pack(fill="x", padx=28, pady=(12, 0))
        for nazwa, cmd in (("Python", "python"), ("Git", "git"), ("Claude Code", "claude")):
            ok = shutil.which(cmd) is not None
            r = tk.Frame(k, bg=K["karta"])
            r.pack(fill="x")
            plakietka(r, "OK" if ok else "BRAK", K["ziel_tlo"] if ok else K["czerw_tlo"], K["ziel"] if ok else K["czerw"]).pack(side="left")
            etykieta(r, f"  {nazwa}" + ("" if ok else f" — nie znaleziono komendy „{cmd}” w PATH (tydzień 0, zadanie 1)"), 10).pack(side="left")
        r = tk.Frame(k, bg=K["karta"])
        r.pack(fill="x", pady=(4, 0))
        ma_claude_md = (p / "CLAUDE.md").exists()
        plakietka(r, "OK" if ma_claude_md else "BRAK", K["ziel_tlo"] if ma_claude_md else K["czerw_tlo"], K["ziel"] if ma_claude_md else K["czerw"]).pack(side="left")
        etykieta(r, "  CLAUDE.md z zasadami nauki", 10).pack(side="left")
        if not ma_claude_md:
            przycisk(r, "Utwórz CLAUDE.md z zasadami", self._utworz_claude_md, "drugi").pack(side="left", padx=10)

        # git
        z, k = karta(w, tytul="Git")
        z.pack(fill="x", padx=28, pady=(12, 0))
        if not (p / ".git").exists():
            etykieta(k, "To nie jest jeszcze repozytorium Git. Zadanie 4 z tygodnia 0: poproś Claude „poprowadź mnie przez git init…”.", 10, kolor=K["czerw"], wrap=800).pack(fill="x")
        elif shutil.which("git") is None:
            etykieta(k, "Git nie jest zainstalowany lub nie ma go w PATH.", 10, kolor=K["czerw"]).pack(fill="x")
        else:
            ost = self._git(p, "log", "-1", "--format=%cd|%s", "--date=format:%Y-%m-%d %H:%M")
            liczba = self._git(p, "rev-list", "--count", "HEAD") or "0"
            dzisiaj = self._git(p, "log", "--since=midnight", "--oneline")
            status = self._git(p, "status", "--porcelain")
            galaz = self._git(p, "branch", "--show-current") or "?"
            zdalne = self._git(p, "remote", "-v")
            if ost:
                data, _, msg = ost.partition("|")
                etykieta(k, f"Ostatni commit: {data} — „{msg}”", 10, wrap=800).pack(fill="x")
            else:
                etykieta(k, "Brak commitów. Pierwszy commit to zadanie 4 z tygodnia 0.", 10, kolor=K["pomar"]).pack(fill="x")
            etykieta(k, f"Commity łącznie: {liczba} · gałąź: {galaz} · zdalne repo: {'tak (GitHub)' if zdalne else 'nie — git remote add origin …'}", 10, kolor=K["szary"]).pack(fill="x")
            r = tk.Frame(k, bg=K["karta"])
            r.pack(fill="x", pady=(6, 0))
            if dzisiaj:
                plakietka(r, f"✔ dziś {len(dzisiaj.splitlines())} commit(y)", K["ziel_tlo"], K["ziel"]).pack(side="left")
            else:
                plakietka(r, "dziś jeszcze bez commita", K["zolty"], K["pomar"]).pack(side="left")
            n = len(status.splitlines()) if status else 0
            if n:
                plakietka(r, f"{n} plik(ów) ze zmianami bez commita", K["czerw_tlo"], K["czerw"]).pack(side="left", padx=8)
                etykieta(k, "Pamiętaj: git add . && git commit -m \"dzień N: temat\" && git push", 9, kolor=K["szary"], mono=True).pack(fill="x", pady=(6, 0))
            else:
                plakietka(r, "drzewo robocze czyste", K["ziel_tlo"], K["ziel"]).pack(side="left", padx=8)

        # pliki z zadań
        tydz = self.stan.biezacy_tydzien()
        z, k = karta(w, tytul=f"Pliki z zadań — tydzień {tydz} ({P.tydzien(tydz)['tytul']})")
        z.pack(fill="x", padx=28, pady=(12, 0))
        nazwy = self._lista_plikow_projektu()
        for i, zad in enumerate(P.tydzien(tydz)["zadania"]):
            r = tk.Frame(k, bg=K["karta"])
            r.pack(fill="x", pady=1)
            if not zad["pliki"]:
                plakietka(r, "— ", K["jasny"], K["szary"]).pack(side="left")
                etykieta(r, f"  {zad['tytul']}  (bez pliku do wykrycia — odhacz w Planie)", 10, kolor=K["szary"]).pack(side="left")
                continue
            znal = next((f for f in zad["pliki"] if f in nazwy), None)
            if znal:
                plakietka(r, f"✔ {znal}", K["ziel_tlo"], K["ziel"]).pack(side="left")
            else:
                plakietka(r, f"brak {zad['pliki'][0]}", K["jasny"], K["szary"]).pack(side="left")
            etykieta(r, f"  {zad['tytul']}" + ("  ✔ odhaczone" if self.stan.zrobione(zad["id"]) else ""), 10).pack(side="left")
        etykieta(k, "Wykrycie pliku to podpowiedź, nie zaliczenie — zaliczasz w Planie, gdy zadanie naprawdę działa (i jest w commicie, jeśli używasz Gita).", 9, kolor=K["szary"], wrap=800).pack(fill="x", pady=(8, 0))

        # pliki .py w projekcie
        pyki = sorted(n for n in nazwy if n.endswith(".py"))
        z, k = karta(w, tytul=f"Pliki .py w projekcie ({len(pyki)})")
        z.pack(fill="x", padx=28, pady=(12, 24))
        etykieta(k, ", ".join(pyki[:60]) + (" …" if len(pyki) > 60 else "") if pyki else "Jeszcze żadnego. hello.py czeka.", 9, mono=True, kolor=K["szary"], wrap=820).pack(fill="x")

    def _git(self, p, *args):
        try:
            flagi = {"creationflags": subprocess.CREATE_NO_WINDOW} if WINDOWS else {}
            out = subprocess.run(["git", *args], cwd=str(p), capture_output=True, text=True, timeout=10, **flagi)
            return out.stdout.strip() if out.returncode == 0 else ""
        except (OSError, subprocess.SubprocessError):
            return ""

    def _wybierz_projekt(self):
        s = filedialog.askdirectory(title="Wybierz katalog projektu (np. nauka-python)", parent=self)
        if s:
            self.stan.d["projekt"] = s
            self.stan.zapisz()
            self._pliki_cache.clear()
            self.pokaz("projekt")

    def _utworz_claude_md(self):
        p = Path(self.stan.d["projekt"]) / "CLAUDE.md"
        if messagebox.askyesno("CLAUDE.md", f"Utworzyć plik:\n{p}\n\nz zasadami nauki (bez rozwiązań za Ciebie, po polsku, wskazówki)?", parent=self):
            try:
                p.write_text(P.claude_md, encoding="utf-8")
                self._pliki_cache.clear()
                self.pokaz("projekt")
            except OSError as e:
                messagebox.showerror("Błąd", str(e), parent=self)

    def _otworz_folder(self, s):
        try:
            if WINDOWS:
                os.startfile(s)  # noqa
            elif sys.platform == "darwin":
                subprocess.Popen(["open", s])
            else:
                subprocess.Popen(["xdg-open", s])
        except OSError as e:
            messagebox.showerror("Błąd", str(e), parent=self)

    @staticmethod
    def znajdz_claude():
        """Ścieżka do komendy claude: PATH, a gdy jej tam nie ma — typowe katalogi instalatora (Windows: %USERPROFILE%\\.local\\bin, npm)."""
        w = shutil.which("claude")
        if w:
            return w
        dom = Path.home()
        kandydaci = [dom / ".local" / "bin" / "claude.exe", dom / ".local" / "bin" / "claude",
                     dom / "AppData" / "Roaming" / "npm" / "claude.cmd", dom / "AppData" / "Local" / "Programs" / "claude" / "claude.exe",
                     Path("/usr/local/bin/claude"), Path("/opt/homebrew/bin/claude")]
        for k in kandydaci:
            if k.exists():
                return str(k)
        return None

    def otworz_claude(self):
        sciezka = self.stan.d["projekt"] or str(KATALOG)
        claude = self.znajdz_claude()
        if claude is None:
            if messagebox.askyesno("Claude Code", "Nie znaleziono komendy „claude” w PATH (Claude Code nie jest zainstalowany "
                                   "albo nie masz subskrypcji).\n\nOtworzyć wbudowanego Asystenta (tryb offline lub API)?", parent=self):
                self.pokaz_asystenta("offline")
            return
        try:
            if WINDOWS:
                subprocess.Popen(["cmd", "/k", claude], cwd=sciezka, creationflags=subprocess.CREATE_NEW_CONSOLE)
            elif sys.platform == "darwin":
                subprocess.Popen(["osascript", "-e", f'tell app "Terminal" to do script "cd \\"{sciezka}\\" && \\"{claude}\\""'])
            else:
                for term in (["x-terminal-emulator", "-e"], ["gnome-terminal", "--"], ["konsole", "-e"], ["xterm", "-e"]):
                    if shutil.which(term[0]):
                        subprocess.Popen([*term, "bash", "-c", f'cd "{sciezka}" && "{claude}"; exec bash'])
                        break
                else:
                    raise OSError("brak terminala")
        except OSError as e:
            messagebox.showwarning("Claude Code", f"Nie udało się otworzyć terminala ({e}).\nOtwórz go sam, wejdź do katalogu projektu i wpisz: claude", parent=self)

    # ================================================================ P.prompty
    def widok_prompty(self):
        self._naglowek(self.tresc, "Szablony promptów", "Prompt to umowa z Claude: ma Cię uczyć, nie wyręczać. "
                       "Zamień [nawiasy] na swoje dane, skopiuj, wklej w Claude Code.")
        cialo = tk.Frame(self.tresc, bg=K["tlo"])
        cialo.pack(fill="both", expand=True, padx=28, pady=(0, 20))
        lewa = tk.Frame(cialo, bg=K["tlo"], width=300)
        lewa.pack(side="left", fill="y")
        lewa.pack_propagate(False)
        lb = tk.Listbox(lewa, font=czc(10), bg=K["karta"], fg=K["tekst"], relief="flat", selectbackground=K["akcent"],
                        selectforeground=K["btn_tekst"], activestyle="none", highlightthickness=1, highlightbackground=K["ramka"])
        lb.pack(fill="both", expand=True)
        pozycje = [(p["nazwa"], p["kiedy"], p["tresc"]) for p in P.prompty]
        if P.claude_md:
            pozycje.append(("Treść pliku CLAUDE.md", "Tydzień 0 — do każdego projektu nauki", P.claude_md))
        for klucz, sz in P.szablony.items():
            if isinstance(sz, dict):
                pozycje.append((sz.get("nazwa") or klucz, sz.get("kiedy", "Szablon dokumentu"), sz.get("tresc", "")))
            else:
                nazwa = {"bug_raport": "Szablon bug raportu"}.get(klucz, "Szablon: " + klucz.replace("_", " "))
                pozycje.append((nazwa, "Szablon dokumentu — uzupełnij [nawiasy]", sz))
        for n, _, _ in pozycje:
            lb.insert("end", "  " + n)

        prawa = tk.Frame(cialo, bg=K["tlo"])
        prawa.pack(side="left", fill="both", expand=True, padx=(16, 0))
        z, k = karta(prawa)
        z.pack(fill="both", expand=True)
        tyt = etykieta(k, "", 13, bold=True)
        tyt.pack(fill="x")
        kiedy = etykieta(k, "", 9, kolor=K["szary"])
        kiedy.pack(fill="x", pady=(0, 8))
        txt = tk.Text(k, font=czc(11), wrap="word", bg=K["jasny"], fg=K["tekst"], insertbackground=K["tekst"], relief="flat", padx=12, pady=10, height=14)
        txt.pack(fill="both", expand=True)
        r = tk.Frame(k, bg=K["karta"])
        r.pack(fill="x", pady=(10, 0))

        def wybrany():
            i = lb.curselection()
            return pozycje[i[0]] if i else pozycje[0]

        def pokaz_prompt(_=None):
            n, kd, t = wybrany()
            tyt.configure(text=n)
            kiedy.configure(text="Kiedy: " + kd)
            txt.configure(state="normal")
            txt.delete("1.0", "end")
            txt.insert("1.0", t)

        przycisk(r, "Wypełnij [nawiasy] i skopiuj", lambda: self._wypelnij_i_skopiuj(txt.get("1.0", "end").strip())).pack(side="left")
        przycisk(r, "Kopiuj bez zmian", lambda: self.schowek(txt.get("1.0", "end").strip()), "drugi").pack(side="left", padx=8)
        przycisk(r, "Wyślij do Asystenta", lambda: self.pokaz_asystenta(None, txt.get("1.0", "end").strip()), "drugi").pack(side="left")
        przycisk(r, "Claude Code ▸", self.otworz_claude, "ciemny").pack(side="left", padx=8)
        etykieta(k, "Tekst możesz edytować przed skopiowaniem.", 8, kolor=K["szary"]).pack(fill="x", pady=(6, 0))
        lb.bind("<<ListboxSelect>>", pokaz_prompt)
        lb.selection_set(0)
        pokaz_prompt()

    def _wypelnij_i_skopiuj(self, tekst):
        luki = []
        for m in re.findall(r"\[([^\]\n]+)\]", tekst):
            if m not in luki:
                luki.append(m)
        for l in luki:
            odp = simpledialog.askstring("Uzupełnij prompt", f"{l}:", parent=self)
            if odp is None:
                return
            tekst = tekst.replace(f"[{l}]", odp)
        self.schowek(tekst, "Prompt gotowy — skopiowany do schowka. Wklej go w Claude Code (prawy przycisk myszy lub Ctrl+V).")


    # =============================================================== ASYSTENT
    KARTY_ASYSTENTA = [
        ("subskrypcja", "🟣 Subskrypcja", "Claude Code"),
        ("api", "🔑 API", "Claude przez klucz"),
        ("offline", "💾 Offline", "wbudowany emulator"),
    ]

    def _kontekst_asystenta(self):
        return {"projekt": self.stan.d.get("projekt", ""), "tydzien": self.stan.biezacy_tydzien(),
                "imie": self.stan.d.get("imie", ""), "tryb_zgody": self.stan.d.get("asystent_zgoda", True),
                "dni": len(self.stan.d["sesje"]), "przelacz_tryb": self._asystent_przelacz_tryb,
                "zapisz_quiz": self._asystent_zapisz_quiz}

    def _asystent_przelacz_tryb(self):
        self.stan.d["asystent_zgoda"] = not self.stan.d.get("asystent_zgoda", True)
        self.stan.zapisz()

    def _asystent_zapisz_quiz(self, tydzien, wynik, maks):
        self.stan.d["quizy"][str(tydzien)] = {"wynik": wynik, "max": maks, "data": str(dzis())}
        self.stan.d["xp"] += wynik * XP_QUIZ_PYTANIE + (XP_QUIZ_BONUS_100 if wynik == maks else 0)
        self.stan.zapisz()
        self._odznaki_popup()

    def pokaz_asystenta(self, karta=None, tekst=None):
        """Otwiera zakładkę Asystent na danej karcie; opcjonalnie wkleja tekst do pola wpisywania."""
        if karta:
            self.stan.d["asystent_karta"] = karta
        elif self.stan.d.get("asystent_karta", "offline") == "subskrypcja":
            self.stan.d["asystent_karta"] = "offline"
        self.asyst_wstaw = tekst or ""
        self.pokaz("asystent")

    def widok_asystent(self):
        self._naglowek(self.tresc, "Asystent", "Trzy sposoby pracy z „nauczycielem”: subskrypcja Claude Code, własny klucz API "
                       "albo wbudowany tryb offline. Wybierz kartę.")
        karta_akt = self.stan.d.get("asystent_karta", "offline")
        pasek = tk.Frame(self.tresc, bg=K["tlo"])
        pasek.pack(fill="x", padx=28)
        for kid, tytul, pod in self.KARTY_ASYSTENTA:
            akt = kid == karta_akt
            r = tk.Frame(pasek, bg=K["akcent"] if akt else K["karta"], highlightbackground=K["akcent"] if akt else K["ramka"],
                         highlightthickness=1, cursor="hand2")
            r.pack(side="left", padx=(0, 8), ipadx=14, ipady=6)
            t1 = tk.Label(r, text=tytul, font=czc(11, "bold"), bg=r.cget("bg"), fg=K["btn_tekst"] if akt else K["tekst"])
            t1.pack(anchor="w", padx=8)
            t2 = tk.Label(r, text=pod, font=czc(8), bg=r.cget("bg"), fg=K["btn_tekst"] if akt else K["szary"])
            t2.pack(anchor="w", padx=8)
            for w in (r, t1, t2):
                w.bind("<Button-1>", lambda e, k=kid: self.pokaz_asystenta(k))
        cialo = tk.Frame(self.tresc, bg=K["tlo"])
        cialo.pack(fill="both", expand=True, padx=28, pady=(12, 20))
        getattr(self, "_asystent_" + karta_akt)(cialo)

    # ---- karta 1: subskrypcja
    def _asystent_subskrypcja(self, cialo):
        p = Przewijane(cialo, K["tlo"])
        p.pack(fill="both", expand=True)
        w = p.wnetrze
        z, k = karta(w, tytul="Subskrypcja — Claude Code w terminalu")
        z.pack(fill="x")
        etykieta(k, "Dla kogo: masz plan Pro, Max, Team lub Enterprise na claude.ai. Darmowy plan nie wystarczy.\n"
                 "Co dostajesz: pełnego Claude w terminalu PyCharm — czyta Twoje pliki (@plik.py), uruchamia komendy za zgodą, "
                 "pamięta zasady z CLAUDE.md, ma tryb planowania (Shift+Tab). To wariant, dla którego napisano ten program nauki.\n"
                 "Koszt: stała opłata miesięczna za plan; Claude Code wliczony w limity planu.", 10, wrap=820).pack(fill="x")
        gdzie = self.znajdz_claude()
        ma = gdzie is not None
        w_path = shutil.which("claude") is not None
        r = tk.Frame(k, bg=K["karta"])
        r.pack(fill="x", pady=(10, 0))
        plakietka(r, "ZAINSTALOWANY" if ma else "NIE ZNALEZIONO", K["ziel_tlo"] if ma else K["czerw_tlo"], K["ziel"] if ma else K["czerw"]).pack(side="left")
        etykieta(r, "  komenda claude" + (" w PATH" if w_path else (f" (poza PATH): {gdzie}" if ma else " — ani w PATH, ani w typowych katalogach instalatora")), 10).pack(side="left")
        if ma:
            przycisk(r, "Otwórz Claude Code w projekcie", self.otworz_claude, "ciemny").pack(side="left", padx=12)
        if ma and not w_path and WINDOWS:
            z2, k2 = karta(w, tytul="Claude jest zainstalowany, ale terminal go nie widzi")
            z2.pack(fill="x", pady=(10, 0))
            etykieta(k2, "Instalator wgrał claude.exe do katalogu, którego nie ma w PATH. Dodaj go raz w PowerShellu (potem otwórz NOWE okno terminala):", 9, kolor=K["szary"], wrap=820).pack(fill="x")
            cmd = '[Environment]::SetEnvironmentVariable("Path", [Environment]::GetEnvironmentVariable("Path", "User") + ";$env:USERPROFILE\\.local\\bin", "User")'
            r2 = tk.Frame(k2, bg=K["karta"])
            r2.pack(fill="x", pady=4)
            tk.Label(r2, text=cmd, font=czc(9, mono=True), bg=K["jasny"], fg=K["tekst"], padx=8, pady=3, wraplength=700, justify="left").pack(side="left")
            przycisk(r2, "Kopiuj", lambda c=cmd: self.schowek(c, None), "drugi").pack(side="left", padx=8)

        z, k = karta(w, tytul="Instalacja (tydzień 0)")
        z.pack(fill="x", pady=(10, 0))
        for opis, cmd in (("Windows — PowerShell:", "irm https://claude.ai/install.ps1 | iex"),
                          ("macOS / Linux / WSL:", "curl -fsSL https://claude.ai/install.sh | bash"),
                          ("Sprawdzenie w NOWYM oknie terminala:", "claude --version"),
                          ("Diagnostyka:", "claude doctor")):
            r = tk.Frame(k, bg=K["karta"])
            r.pack(fill="x", pady=2)
            etykieta(r, opis, 9, kolor=K["szary"]).pack(side="left")
            tk.Label(r, text=cmd, font=czc(10, mono=True), bg=K["jasny"], fg=K["tekst"], padx=8, pady=3).pack(side="left", padx=8)
            przycisk(r, "Kopiuj", lambda c=cmd: self.schowek(c, None), "drugi").pack(side="left")
        etykieta(k, "Potem: uruchom claude w pustym katalogu i zaloguj się w przeglądarce. W PyCharm zainstaluj wtyczkę Claude Code "
                 "(Settings → Plugins) i uruchamiaj claude w terminalu wbudowanym.", 9, kolor=K["szary"], wrap=820).pack(fill="x", pady=(8, 0))
        l = tk.Label(k, text="🔗 Dokumentacja: code.claude.com/docs", font=czc(10, "underline"), bg=K["karta"], fg=K["nieb"], cursor="hand2", anchor="w")
        l.pack(fill="x", pady=(6, 0))
        l.bind("<Button-1>", lambda e: webbrowser.open("https://code.claude.com/docs"))

        z, k = karta(w, tytul="Nie masz subskrypcji?")
        z.pack(fill="x", pady=(10, 0))
        etykieta(k, "Karta API — płacisz tylko za użycie, bez abonamentu; ten sam model, rozmowa w tym oknie.\n"
                 "Karta Offline — zero kosztów i internetu; nie jest modelem językowym, ale zna cały plan nauki: tłumaczy tematy, "
                 "recenzuje pliki, tłumaczy błędy, robi quizy. Na tygodnie 0–3 wystarcza w zupełności.", 10, wrap=820).pack(fill="x")

    # ---- karta 2: API
    def _asystent_api(self, cialo):
        gora = tk.Frame(cialo, bg=K["tlo"])
        gora.pack(fill="x")
        z, k = karta(gora, tytul="API — prawdziwy Claude bez abonamentu")
        z.pack(fill="x")
        etykieta(k, "Dla kogo: nie chcesz płacić miesięcznie; masz konto na console.anthropic.com z doładowanym saldem (przedpłata). "
                 "Co dostajesz: tego samego Claude co w Claude Code, w tym oknie — z zasadami z CLAUDE.md i kontekstem Twojego tygodnia; "
                 "pliki wskazujesz przez @nazwa.py (czytam je z katalogu projektu). Nie uruchamia komend i nie edytuje plików — to robisz Ty. "
                 "Koszt: za tokeny; krótka rozmowa o jednym pliku to zwykle ułamek grosza do kilku groszy. Klucz zapisuje się w mentor_dane.json "
                 "na Twoim dysku — nie commituj tego pliku.", 10, wrap=820).pack(fill="x")
        r = tk.Frame(k, bg=K["karta"])
        r.pack(fill="x", pady=(10, 0))
        etykieta(r, "Klucz API: ", 10).pack(side="left")
        klucz_var = tk.StringVar(value=self.stan.d.get("api_klucz", ""))
        e = tk.Entry(r, textvariable=klucz_var, show="•", width=30, font=czc(10, mono=True), relief="flat", bg=K["jasny"], fg=K["tekst"], insertbackground=K["tekst"])
        e.pack(side="left", ipady=4)
        etykieta(r, "  Model: ", 10).pack(side="left")
        model_var = tk.StringVar(value=self.stan.d.get("api_model", KlientAPI.MODEL_DOMYSLNY))
        tk.Entry(r, textvariable=model_var, width=22, font=czc(10, mono=True), relief="flat", bg=K["jasny"], fg=K["tekst"], insertbackground=K["tekst"]).pack(side="left", ipady=4)

        def zapisz():
            self.stan.d["api_klucz"] = klucz_var.get().strip()
            self.stan.d["api_model"] = model_var.get().strip() or KlientAPI.MODEL_DOMYSLNY
            self.stan.zapisz()
            self.klient_api = None
            self._dopisz_asyst("api", [("ok", "Zapisano klucz i model. Napisz coś — albo „Sprawdź połączenie”.")])

        przycisk(r, "Zapisz", zapisz, "drugi").pack(side="left", padx=8)
        przycisk(r, "Test", lambda: (zapisz(), self._asystent_wyslij_api("Odpowiedz jednym zdaniem: kim jesteś i jak będziesz mi pomagał?")), "drugi").pack(side="left")
        etykieta(k, "Klucz: console.anthropic.com → API Keys → Create Key. Saldo: Billing. Nazwę modelu zmień, jeśli API odpowie 404 "
                 "(lista aktualnych modeli jest w dokumentacji docs.claude.com).", 9, kolor=K["szary"], wrap=820).pack(fill="x", pady=(6, 0))
        self._konsola(cialo, "api")

    # ---- karta 3: offline
    def _asystent_offline(self, cialo):
        gora = tk.Frame(cialo, bg=K["tlo"])
        gora.pack(fill="x")
        z, k = karta(gora, tytul="Offline — wbudowany emulator Claude Code")
        z.pack(fill="x")
        przyklad_lekcji = P.lekcje[0]["nazwa"].split(":")[0].split("—")[0].strip().lower() if P.lekcje else "temat"
        etykieta(k, "Dla kogo: bez konta, bez karty, bez internetu. Co dostajesz: nie model językowy, tylko podręcznik z komendami — "
                 f"rozumie prompty z planu („uczę się {przyklad_lekcji}”, „przejrzyj @plik.py”, „utknąłem… błąd: …”, „zadaj mi 3 pytania”, „quiz z tygodnia 2”, „commit”), "
                 f"tłumaczy {len(P.lekcje)} lekcji tego programu z przykładami, zna {len(P.pojecia)} pojęć („co to jest…”), recenzuje kod Pythona analizą statyczną, uruchamia pliki i tłumaczy błędy, "
                 "odpytuje jak rekruter z pytań programu. Zanim coś wykona lub zapisze — pyta o zgodę. "
                 "Nie odpowie na dowolne pytanie „dlaczego” — wtedy zapisz je w Dzienniku na tryb API/Claude Code.", 10, wrap=820).pack(fill="x")
        r = tk.Frame(k, bg=K["karta"])
        r.pack(fill="x", pady=(8, 0))
        zgoda = self.stan.d.get("asystent_zgoda", True)
        plakietka(r, "TRYB: PYTAJ O ZGODĘ" if zgoda else "TRYB: AUTO", K["ziel_tlo"] if zgoda else K["zolty"], K["ziel"] if zgoda else K["pomar"]).pack(side="left")
        przycisk(r, "Przełącz tryb (jak Shift+Tab)", lambda: (self._asystent_przelacz_tryb(), self.pokaz("asystent")), "drugi").pack(side="left", padx=8)
        przycisk(r, "/help", lambda: self._asystent_wyslij_offline("/help"), "drugi").pack(side="left")
        przycisk(r, "/tematy", lambda: self._asystent_wyslij_offline("/tematy"), "drugi").pack(side="left", padx=8)
        self._konsola(cialo, "offline")

    # ---- wspólna konsola
    def _konsola(self, cialo, tryb):
        z, k = karta(cialo, padx=10, pady=8)
        z.pack(fill="both", expand=True, pady=(10, 0))
        # pole wpisywania pakujemy od dołu, żeby nigdy nie wypadło poza okno
        etykieta(k, "Enter wysyła, Shift+Enter nowa linia. Pliki wskazuj przez @nazwa.py.", 8, kolor=K["szary"]).pack(side="bottom", fill="x", pady=(4, 0))
        dol = tk.Frame(k, bg=K["karta"])
        dol.pack(side="bottom", fill="x", pady=(6, 0))
        ramka = tk.Frame(k, bg=K["karta"])
        ramka.pack(side="top", fill="both", expand=True)
        txt = tk.Text(ramka, font=czc(10), wrap="word", bg=K["karta"], fg=K["tekst"], relief="flat", padx=10, pady=8,
                      state="disabled", cursor="arrow", insertbackground=K["tekst"], selectbackground=K["akcent"], selectforeground=K["btn_tekst"])
        sb = ttk.Scrollbar(ramka, orient="vertical", command=txt.yview)
        txt.configure(yscrollcommand=sb.set)
        sb.pack(side="right", fill="y")
        txt.pack(side="left", fill="both", expand=True)
        txt.tag_configure("ty", foreground=K["akcent"], font=czc(10, "bold"), spacing1=8)
        txt.tag_configure("naglowek", foreground=K["tekst"], font=czc(11, "bold"), spacing1=6)
        txt.tag_configure("tekst", foreground=K["tekst"])
        txt.tag_configure("kod", foreground=K["tekst"], font=czc(10, mono=True), background=K["jasny"], lmargin1=12, lmargin2=12, spacing1=3, spacing3=3)
        txt.tag_configure("ostrz", foreground=K["pomar"])
        txt.tag_configure("ok", foreground=K["ziel"])
        txt.tag_configure("pytanie", foreground=K["nieb"], font=czc(10, "italic"))
        txt.tag_configure("blad", foreground=K["czerw"])
        txt.tag_configure("szary", foreground=K["szary"], font=czc(9))
        self.asyst_txt = txt
        self.asyst_tryb = tryb
        if not self.asyst_hist[tryb]:
            if tryb == "offline":
                self.asyst_hist[tryb] = [("szary", f"Asystent offline · katalog: {self.stan.d.get('projekt') or '(nie wybrano — Mój projekt)'} · "
                                                   f"tydzień {self.stan.biezacy_tydzien()} · wpisz /help")]
            else:
                self.asyst_hist[tryb] = [("szary", "Asystent API · rozmowa zaczyna się od zera przy każdym uruchomieniu programu · /clear czyści")]
        for styl, t in self.asyst_hist[tryb]:
            self._konsola_wypisz(styl, t)
        tk.Label(dol, text=">", font=czc(12, "bold", mono=True), bg=K["karta"], fg=K["akcent"]).pack(side="left", padx=(4, 6))
        wej = tk.Text(dol, height=2, font=czc(10), wrap="word", bg=K["jasny"], fg=K["tekst"], relief="flat", padx=8, pady=6, insertbackground=K["tekst"])
        wej.pack(side="left", fill="x", expand=True)
        self.asyst_wej = wej
        if self.asyst_wstaw:
            wej.insert("1.0", self.asyst_wstaw)
            self.asyst_wstaw = ""

        def wyslij(_=None):
            t = wej.get("1.0", "end").strip()
            if not t:
                return "break"
            wej.delete("1.0", "end")
            if t.lower() == "/clear":
                self.asyst_hist[tryb] = []
                if tryb == "api" and self.klient_api:
                    self.klient_api.wyczysc()
                self.pokaz("asystent")
                return "break"
            if tryb == "offline":
                self._asystent_wyslij_offline(t)
            else:
                self._asystent_wyslij_api(t)
            return "break"

        wej.bind("<Return>", wyslij)
        wej.bind("<Shift-Return>", lambda e: None)
        przycisk(dol, "Wyślij ⏎", wyslij).pack(side="left", padx=(8, 0))
        wej.focus_set()

    def _konsola_wypisz(self, styl, tekst):
        txt = self.asyst_txt
        if not txt or not txt.winfo_exists():
            return
        txt.configure(state="normal")
        prefix = "Ty: " if styl == "ty" else ""
        txt.insert("end", prefix + tekst + "\n", styl)
        txt.configure(state="disabled")
        txt.see("end")

    def _dopisz_asyst(self, tryb, wpisy):
        self.asyst_hist[tryb].extend(wpisy)
        self.asyst_hist[tryb] = self.asyst_hist[tryb][-400:]
        if self.aktywny == "asystent" and getattr(self, "asyst_tryb", None) == tryb:
            for styl, t in wpisy:
                self._konsola_wypisz(styl, t)

    def _asystent_wyslij_offline(self, tekst):
        self._dopisz_asyst("offline", [("ty", tekst)])
        try:
            odp = self.emulator.odpowiedz(tekst)
        except Exception as e:  # emulator nie może położyć aplikacji
            odp = [("blad", f"Emulator się wywalił ({type(e).__name__}: {e}). To jest bug — zgłoś go, a tymczasem użyj innej komendy.")]
        self._dopisz_asyst("offline", odp)
        self._pliki_cache.clear()

    def _asystent_wyslij_api(self, tekst):
        if self.asyst_zajety:
            self._dopisz_asyst("api", [("ostrz", "Czekam jeszcze na poprzednią odpowiedź.")])
            return
        if self.klient_api is None:
            self.klient_api = KlientAPI(self.stan.d.get("api_klucz", ""), self.stan.d.get("api_model"), self._kontekst_asystenta)
        self._dopisz_asyst("api", [("ty", tekst), ("szary", "… myślę")])
        self.asyst_zajety = True

        def praca():
            try:
                odp = self.klient_api.wyslij(tekst)
                uz = getattr(self.klient_api, "ostatnie_uzycie", (0, 0))
                wynik = self._api_na_wpisy(odp) + [("szary", f"tokeny: {uz[0]} wejście / {uz[1]} wyjście")]
            except RuntimeError as e:
                wynik = [("blad", str(e))]
            except Exception as e:
                wynik = [("blad", f"Nieoczekiwany błąd: {type(e).__name__}: {e}")]
            self.after(0, lambda: self._api_gotowe(wynik))

        threading.Thread(target=praca, daemon=True).start()

    def _api_gotowe(self, wynik):
        self.asyst_zajety = False
        if self.asyst_hist["api"] and self.asyst_hist["api"][-1] == ("szary", "… myślę"):
            self.asyst_hist["api"].pop()
            if self.aktywny == "asystent" and getattr(self, "asyst_tryb", None) == "api" and self.asyst_txt.winfo_exists():
                self.asyst_txt.configure(state="normal")
                self.asyst_txt.delete("end-2l", "end-1l")
                self.asyst_txt.configure(state="disabled")
        self._dopisz_asyst("api", wynik)

    @staticmethod
    def _api_na_wpisy(odp):
        """Dzieli odpowiedź modelu na tekst i bloki kodu (```...```)."""
        wpisy = []
        czesci = re.split(r"```[\w+-]*\n?", odp)
        for i, cz in enumerate(czesci):
            cz = cz.strip("\n")
            if not cz.strip():
                continue
            wpisy.append(("kod" if i % 2 == 1 else "tekst", cz))
        return wpisy or [("tekst", odp)]

    # =================================================================== QUIZ
    def widok_quiz(self):
        w = self._strona("Quiz", "Sobota to dzień quizu, ale możesz sprawdzać się codziennie. Błędne odpowiedzi wracają w powtórkach — "
                         "to najlepszy sposób, żeby wiedza została.")
        z, k = karta(w, tytul="Wybierz quiz")
        z.pack(fill="x", padx=28)
        r = tk.Frame(k, bg=K["karta"])
        r.pack(fill="x")
        etykieta(r, "Tydzień: ", 10).pack(side="left")
        opcje = [f"{t} — {P.tydzien(t)['tytul']}" for t in sorted(int(k) for k in P.quizy)]
        self.q_wybor = ttk.Combobox(r, values=opcje, state="readonly", width=40, font=czc(10))
        self.q_wybor.current(min(self.stan.biezacy_tydzien(), len(opcje) - 1))
        self.q_wybor.pack(side="left")
        przycisk(r, "Start", lambda: self.pokaz_quiz(int(self.q_wybor.get().split(" ")[0]))).pack(side="left", padx=8)
        n_pow = len(self.stan.d["powtorki"])
        przycisk(r, f"Powtórka ({n_pow} pytań do poprawy)" if n_pow else "Powtórka losowa (5 pytań)", self._quiz_powtorka, "ostrz").pack(side="left")

        z, k = karta(w, tytul="Twoje wyniki")
        z.pack(fill="x", padx=28, pady=(12, 24))
        if not self.stan.d["quizy"]:
            etykieta(k, "Jeszcze żadnego quizu. Pierwszy quiz z tygodnia 0 to dobre rozgrzanie.", 10, kolor=K["szary"]).pack(fill="x")
        for t in sorted(self.stan.d["quizy"], key=int):
            q = self.stan.d["quizy"][t]
            proc = int(100 * q["wynik"] / q["max"]) if q["max"] else 0
            rr = tk.Frame(k, bg=K["karta"])
            rr.pack(fill="x", pady=2)
            etykieta(rr, f"Tydzień {t}: {P.tydzien(int(t))['tytul']}", 10, anchor="w").pack(side="left", fill="x", expand=True)
            kol = K["ziel"] if proc >= 80 else (K["pomar"] if proc >= 60 else K["czerw"])
            plakietka(rr, f"{q['wynik']}/{q['max']} ({proc}%) · {q['data']}", K["jasny"], kol).pack(side="right")

    def _quiz_powtorka(self):
        pytania = []
        for pid in self.stan.d["powtorki"]:
            t, i = pid.split("-")
            t, i = int(t), int(i)
            if str(t) in P.quizy and i < len(P.quizy[str(t)]):
                pytania.append((pid, P.quizy[str(t)][i]))
        if not pytania:
            pula = [(f"{t}-{i}", q) for t in (int(k) for k in P.quizy) for i, q in enumerate(P.quizy[str(t)]) if t <= self.stan.biezacy_tydzien()]
            pytania = random.sample(pula, min(5, len(pula)))
        self._uruchom_quiz(pytania, tydzien=None, tytul="Powtórka")

    def pokaz_quiz(self, tydzien):
        pytania = [(f"{tydzien}-{i}", q) for i, q in enumerate(P.quiz_tygodnia(tydzien))]
        self._uruchom_quiz(pytania, tydzien, f"Quiz: tydzień {tydzien} — {P.tydzien(tydzien)['tytul']}")

    def _uruchom_quiz(self, pytania, tydzien, tytul, lekcja_id=None):
        self.pokaz("quiz")
        for ch in self.tresc.winfo_children():
            ch.destroy()
        q = {"pytania": pytania, "i": 0, "wynik": 0, "tydzien": tydzien, "tytul": tytul, "sprawdzone": False, "lekcja_id": lekcja_id}
        self._q = q
        self._quiz_pytanie()

    def _quiz_pytanie(self):
        q = self._q
        for ch in self.tresc.winfo_children():
            ch.destroy()
        w = self._strona(q["tytul"], f"Pytanie {q['i'] + 1} z {len(q['pytania'])} · wynik: {q['wynik']}")
        pid, p = q["pytania"][q["i"]]
        z, k = karta(w)
        z.pack(fill="x", padx=28)
        etykieta(k, p["p"], 13, bold=True, wrap=820).pack(fill="x", pady=(0, 10))
        var = tk.IntVar(value=-1)
        radia = []
        for i, o in enumerate(p["o"]):
            rb = tk.Radiobutton(k, text=o, variable=var, value=i, font=czc(11), bg=K["karta"], activebackground=K["karta"], fg=K["tekst"], activeforeground=K["tekst"],
                                selectcolor=K["jasny"], anchor="w", justify="left", wraplength=780, cursor="hand2", padx=6, pady=4)
            rb.pack(fill="x")
            radia.append(rb)
        wynik_lab = etykieta(k, "", 10, wrap=820)
        wynik_lab.pack(fill="x", pady=(8, 0))
        r = tk.Frame(k, bg=K["karta"])
        r.pack(fill="x", pady=(10, 0))

        def sprawdz():
            if var.get() < 0:
                messagebox.showinfo("Quiz", "Zaznacz odpowiedź.", parent=self)
                return
            dobrze = var.get() == p["odp"]
            for i, rb in enumerate(radia):
                rb.configure(state="disabled", disabledforeground=K["ziel"] if i == p["odp"] else (K["czerw"] if i == var.get() else K["szary"]))
            if dobrze:
                q["wynik"] += 1
                self.stan.d["xp"] += XP_QUIZ_PYTANIE
                if pid in self.stan.d["powtorki"]:
                    self.stan.d["powtorki"].remove(pid)
                wynik_lab.configure(text="✔ Dobrze!  " + p["w"], fg=K["ziel"])
            else:
                if pid not in self.stan.d["powtorki"]:
                    self.stan.d["powtorki"].append(pid)
                wynik_lab.configure(text=f"✘ Nie. Poprawna odpowiedź: {p['o'][p['odp']]}\n{p['w']}", fg=K["czerw"])
            self.stan.zapisz()
            b_spr.configure(state="disabled")
            b_dalej.configure(state="normal")

        def dalej():
            q["i"] += 1
            if q["i"] < len(q["pytania"]):
                self._quiz_pytanie()
            else:
                self._quiz_koniec()

        b_spr = przycisk(r, "Sprawdź", sprawdz)
        b_spr.pack(side="left")
        b_dalej = przycisk(r, "Dalej →", dalej, "drugi")
        b_dalej.pack(side="left", padx=8)
        b_dalej.configure(state="disabled")
        przycisk(r, "Przerwij", lambda: self.pokaz_lekcje(q["lekcja_id"]) if q.get("lekcja_id") else self.pokaz("quiz"), "drugi").pack(side="right")

    def _quiz_koniec(self):
        q = self._q
        n = len(q["pytania"])
        proc = int(100 * q["wynik"] / n)
        if q["tydzien"] is not None:
            self.stan.d["quizy"][str(q["tydzien"])] = {"wynik": q["wynik"], "max": n, "data": str(dzis())}
            if q["wynik"] == n:
                self.stan.d["xp"] += XP_QUIZ_BONUS_100
        if q.get("lekcja_id"):
            self.stan.d.setdefault("lekcje", {})[q["lekcja_id"]] = {"wynik": q["wynik"], "max": n, "data": str(dzis())}
        self.stan.zapisz()
        komentarz = ("Bezbłędnie. To już Twoje." if proc == 100 else "Solidnie. Błędne pytania wrócą w powtórce." if proc >= 60
                     else "Za nisko, żeby iść dalej spokojnie. Wróć do tematu z Claude: „Wytłumacz mi [temat] jeszcze raz, inaczej niż poprzednio.”")
        self._odznaki_popup()
        messagebox.showinfo("Wynik", f"{q['wynik']}/{n} ({proc}%)\n\n{komentarz}", parent=self)
        if q.get("lekcja_id"):
            self.pokaz_lekcje(q["lekcja_id"])
        else:
            self.pokaz("quiz")

    # =============================================================== DZIENNIK
    def widok_dziennik(self):
        w = self._strona("Dziennik nauki", "Dwa zdania dziennie: co zrozumiałem, co jeszcze nie. Pisanie o tym, czego się nauczyłeś, "
                         "utrwala mocniej niż ponowne czytanie.")
        pytania = ["Co dziś było najtrudniejsze i jak to rozgryzłeś?", "Jaki błąd Pythona dziś zobaczyłeś i co oznaczał?",
                   "Co byś wytłumaczył koledze bez IT z dzisiejszego tematu?", "Gdzie Claude zrobił za dużo, a gdzie pomógł w sam raz?",
                   "Jaką jedną rzecz zrobisz jutro jako pierwszą?", "Co w Twoim kodzie jest dziś czytelniejsze niż wczoraj?",
                   "Jak dzisiejszy temat przyda się w testowaniu?"]
        z, k = karta(w, tytul="Nowy wpis — " + data_pl(dzis()))
        z.pack(fill="x", padx=28)
        etykieta(k, "Pytanie mentora: " + random.choice(pytania), 10, kolor=K["akcent"], wrap=820).pack(fill="x", pady=(0, 6))
        txt = tk.Text(k, height=6, font=czc(11), wrap="word", bg=K["jasny"], fg=K["tekst"], insertbackground=K["tekst"], relief="flat", padx=12, pady=10)
        txt.pack(fill="x")
        r = tk.Frame(k, bg=K["karta"])
        r.pack(fill="x", pady=(8, 0))
        etykieta(r, "Jak poszło: ", 10).pack(side="left")
        nastroj = tk.StringVar(value="🙂")
        for e in ("😫", "😐", "🙂", "🤩"):
            tk.Radiobutton(r, text=e, variable=nastroj, value=e, font=czc(13), bg=K["karta"], activebackground=K["karta"], fg=K["tekst"], activeforeground=K["tekst"],
                           selectcolor=K["ziel_tlo"], indicatoron=False, relief="flat", bd=0, padx=8, cursor="hand2").pack(side="left", padx=2)

        def zapisz():
            t = txt.get("1.0", "end").strip()
            if len(t) < 10:
                messagebox.showinfo("Dziennik", "Napisz chociaż jedno pełne zdanie.", parent=self)
                return
            self.stan.d["dziennik"].insert(0, {"data": str(dzis()), "tekst": t, "nastroj": nastroj.get()})
            self.stan.d["xp"] += XP_DZIENNIK
            self.stan.zapisz()
            self._odznaki_popup()
            self.pokaz("dziennik")

        przycisk(r, f"Zapisz wpis (+{XP_DZIENNIK} XP)", zapisz).pack(side="right")

        z, k = karta(w, tytul=f"Wcześniejsze wpisy ({len(self.stan.d['dziennik'])})")
        z.pack(fill="x", padx=28, pady=(12, 24))
        if not self.stan.d["dziennik"]:
            etykieta(k, "Pusto. Pierwszy wpis po pierwszej sesji.", 10, kolor=K["szary"]).pack(fill="x")
        for i, wpis in enumerate(self.stan.d["dziennik"][:40]):
            rr = tk.Frame(k, bg=K["karta"])
            rr.pack(fill="x", pady=(0, 8))
            g = tk.Frame(rr, bg=K["karta"])
            g.pack(fill="x")
            etykieta(g, f"{wpis['nastroj']}  {data_pl(dt.date.fromisoformat(wpis['data']))}", 9, bold=True, kolor=K["szary"]).pack(side="left")
            tk.Button(g, text="usuń", relief="flat", bd=0, fg=K["szary"], bg=K["karta"], cursor="hand2", font=czc(8),
                      command=lambda j=i: self._usun_wpis(j)).pack(side="right")
            etykieta(rr, wpis["tekst"], 10, wrap=820).pack(fill="x")

    def _usun_wpis(self, j):
        if messagebox.askyesno("Dziennik", "Usunąć ten wpis?", parent=self):
            del self.stan.d["dziennik"][j]
            self.stan.zapisz()
            self.pokaz("dziennik")

    # ============================================================= P.checklista
    def widok_checklista(self):
        w = self._strona("Checklista postępów", "Odhaczaj tylko to, co potrafisz zrobić BEZ pomocy Claude. "
                         "Jeśli po etapie zostają puste pola — dodaj tydzień, zanim ruszysz dalej.")
        razem = sum(len(g["punkty"]) for g in P.checklista)
        zrob = sum(1 for v in self.stan.d["checklista"].values() if v)
        z, k = karta(w)
        z.pack(fill="x", padx=28)
        etykieta(k, f"Umiejętności potwierdzone: {zrob}/{razem}", 11, bold=True).pack(fill="x")
        ttk.Progressbar(k, maximum=razem, value=zrob, style="Pomar.Horizontal.TProgressbar").pack(fill="x", pady=(4, 0))
        for gi, g in enumerate(P.checklista):
            z, k = karta(w, tytul=g["po"])
            z.pack(fill="x", padx=28, pady=(10, 0))
            for pi, p in enumerate(g["punkty"]):
                klucz = f"{gi}-{pi}"
                var = tk.BooleanVar(value=self.stan.d["checklista"].get(klucz, False))

                def zmien(k_=klucz, v=var):
                    self.stan.d["checklista"][k_] = v.get()
                    self.stan.zapisz()
                    self._odswiez_stopke()

                tk.Checkbutton(k, text=p, variable=var, command=zmien, font=czc(10), bg=K["karta"], activebackground=K["karta"], fg=K["tekst"], activeforeground=K["tekst"], selectcolor=K["jasny"],
                               anchor="w", justify="left", wraplength=800, cursor="hand2").pack(fill="x")
        tk.Frame(w, bg=K["tlo"], height=24).pack()

    # ================================================================= ŚCIĄGA
    def widok_sciaga(self):
        w = self._strona("Ściąga", "Najważniejsze liczby, komendy i skróty z programu nauki. Reszta czeka pod /help w Asystencie.")
        for sekcja in P.sciaga:
            tytul, dane = sekcja["tytul"], sekcja["pozycje"]
            z, k = karta(w, tytul=tytul)
            z.pack(fill="x", padx=28, pady=(0, 12))
            for cmd, opis in dane:
                r = tk.Frame(k, bg=K["karta"])
                r.pack(fill="x", pady=1)
                tk.Label(r, text=cmd, font=czc(10, "bold", mono=True), bg=K["jasny"], fg=K["tekst"], width=26, anchor="w", padx=8, pady=3).pack(side="left", anchor="n")
                etykieta(r, "  " + opis, 10, wrap=600).pack(side="left", fill="x", expand=True, pady=2)
        z, k = karta(w, tytul="Linki")
        z.pack(fill="x", padx=28, pady=(0, 24))
        for n, u in P.linki:
            l = tk.Label(k, text="🔗 " + n, font=czc(10, "underline"), bg=K["karta"], fg=K["nieb"], cursor="hand2", anchor="w")
            l.pack(fill="x", pady=1)
            l.bind("<Button-1>", lambda e, url=u: webbrowser.open(url))

    # ============================================================= USTAWIENIA
    def widok_ustawienia(self):
        w = self._strona("Ustawienia")
        z, k = karta(w, tytul="Profil")
        z.pack(fill="x", padx=28)
        r = tk.Frame(k, bg=K["karta"])
        r.pack(fill="x")
        etykieta(r, "Imię: ", 10).pack(side="left")
        imie = tk.StringVar(value=self.stan.d["imie"])
        tk.Entry(r, textvariable=imie, font=czc(10), relief="flat", bg=K["jasny"], fg=K["tekst"], insertbackground=K["tekst"], width=24).pack(side="left", ipady=4)

        def zapisz_imie():
            self.stan.d["imie"] = imie.get().strip()
            self.stan.zapisz()
            messagebox.showinfo("Zapisano", "Imię zapisane.", parent=self)

        przycisk(r, "Zapisz", zapisz_imie, "drugi").pack(side="left", padx=8)
        etykieta(k, f"Start programu: {self.stan.d['start']} · plik danych: {PLIK_DANYCH}", 9, kolor=K["szary"], wrap=820).pack(fill="x", pady=(8, 0))

        # --- program nauczania
        z, k = karta(w, tytul="Program nauczania")
        z.pack(fill="x", padx=28, pady=(12, 0))
        etykieta(k, f"Aktywny: {P.nazwa}" + (f" — {P.podtytul}" if P.podtytul else ""), 11, bold=True, wrap=820).pack(fill="x")
        if P.opis:
            etykieta(k, P.opis, 9, kolor=K["szary"], wrap=820).pack(fill="x", pady=(2, 0))
        etykieta(k, f"{P.liczba_tygodni()} tygodni · {len(P.wszystkie_zadania())} zadań · {len(P.lekcje)} lekcji · "
                 f"plik: {Path(P.sciezka).name if P.sciezka else '—'}", 9, kolor=K["szary"], wrap=820).pack(fill="x")
        etykieta(k, "Postępy każdego programu są zapisywane osobno — możesz przełączać bez straty.", 9, kolor=K["szary"], wrap=820).pack(fill="x", pady=(2, 8))
        for sc, nazwa, pod, n_tyg in lista_programow():
            r = tk.Frame(k, bg=K["karta"])
            r.pack(fill="x", pady=2)
            akt = P.sciezka and Path(P.sciezka).resolve() == sc.resolve()
            plakietka(r, "AKTYWNY" if akt else f"{n_tyg} tyg.", K["ziel_tlo"] if akt else K["jasny"], K["ziel"] if akt else K["szary"]).pack(side="left")
            etykieta(r, f"  {nazwa}" + (f" — {pod}" if pod else ""), 10, wrap=560).pack(side="left", fill="x", expand=True)
            if not akt and n_tyg:
                przycisk(r, "Przełącz", lambda s_=sc: self.ustaw_program(s_), "drugi").pack(side="right")
        r = tk.Frame(k, bg=K["karta"])
        r.pack(fill="x", pady=(8, 0))
        przycisk(r, "Wgraj program z pliku…", self._wgraj_program, "drugi").pack(side="left")
        przycisk(r, "Otwórz folder programów", lambda: self._otworz_folder(str(KATALOG_PROGRAMOW)), "drugi").pack(side="left", padx=8)
        przycisk(r, "Zapisz pusty szablon programu", self._szablon_programu, "drugi").pack(side="left")
        etykieta(k, "Program to plik JSON: nazwa, etapy, tygodnie z zadaniami (każde z krokami „jak to zrobić”), lekcje z testami, quizy, checklista, prompty. "
                 "Opis formatu: programy/FORMAT.md. Źródła przykładowego programu (w Pythonie, z generatorem): programy/zrodla/.", 9, kolor=K["szary"], wrap=820).pack(fill="x", pady=(6, 0))

        z, k = karta(w, tytul="Wygląd")
        z.pack(fill="x", padx=28, pady=(12, 0))
        etykieta(k, "Motyw zmienia się od razu i zostaje zapamiętany. Schematy PyCharm to te wbudowane oraz najczęściej "
                 "pobierane z JetBrains Marketplace.", 9, kolor=K["szary"], wrap=820).pack(fill="x", pady=(0, 6))
        # --- czcionka: rodzina i wielkość
        etykieta(k, "Czcionka", 10, bold=True).pack(fill="x", pady=(8, 4))
        r = tk.Frame(k, bg=K["karta"])
        r.pack(fill="x")
        etykieta(r, "Krój: ", 10).pack(side="left")
        dostepne = rodziny_czcionek()
        lista = ["(domyślna motywu)"] + [f for f in CZCIONKI_UI if f in dostepne]
        wybor = ttk.Combobox(r, values=lista, state="readonly", width=24, font=czc(10))
        biez = self.stan.d.get("czcionka", "")
        wybor.set(biez if biez in lista else "(domyślna motywu)")
        wybor.pack(side="left")

        def zmien_krój(_=None):
            w_ = wybor.get()
            self.stan.d["czcionka"] = "" if w_.startswith("(") else w_
            self.przebuduj()

        wybor.bind("<<ComboboxSelected>>", zmien_krój)
        przycisk(r, "Wszystkie czcionki…", self._wybierz_czcionke_z_listy, "drugi").pack(side="left", padx=8)
        etykieta(r, f"teraz: {FONT}", 9, kolor=K["szary"]).pack(side="left")

        r = tk.Frame(k, bg=K["karta"])
        r.pack(fill="x", pady=(6, 0))
        etykieta(r, "Wielkość: ", 10).pack(side="left")
        for nazwa, sk in ROZMIARY:
            akt = abs(SKALA - sk) < 0.01
            tk.Button(r, text=nazwa, relief="flat", bd=0, cursor="hand2", font=czc(9, "bold" if akt else "normal"),
                      bg=K["ziel_tlo"] if akt else K["jasny"], fg=K["ziel"] if akt else K["tekst"], padx=8, pady=3,
                      command=lambda s_=sk: self._ustaw_skale_czcionki(s_)).pack(side="left", padx=3)
        etykieta(r, f"{int(SKALA * 100)}%", 9, kolor=K["szary"]).pack(side="left", padx=6)

        # --- jasność motywów terminalowych
        etykieta(k, "Jasność terminala", 10, bold=True).pack(fill="x", pady=(10, 4))
        r = tk.Frame(k, bg=K["karta"])
        r.pack(fill="x")
        czy_term = K.get("grupa") == "terminal"
        etykieta(r, "Przygaszony ", 9, kolor=K["szary"]).pack(side="left")
        self.jasnosc_var = tk.DoubleVar(value=JASNOSC_TERM)
        suwak = ttk.Scale(r, from_=0.4, to=1.0, orient="horizontal", variable=self.jasnosc_var, length=220)
        suwak.pack(side="left")
        etykieta(r, " Pełny", 9, kolor=K["szary"]).pack(side="left")
        wart = etykieta(r, f"{int(JASNOSC_TERM * 100)}%", 9, kolor=K["szary"])
        wart.pack(side="left", padx=8)
        suwak.bind("<Motion>", lambda e: wart.configure(text=f"{int(self.jasnosc_var.get() * 100)}%"))
        suwak.bind("<ButtonRelease-1>", lambda e: self._ustaw_jasnosc(self.jasnosc_var.get()))
        etykieta(k, "Działa w motywach terminalowych (zielonym i bursztynowym): przyciemnia tekst i akcenty, tło zostaje czarne."
                 + ("" if czy_term else " Włącz motyw terminalowy, żeby zobaczyć efekt."), 9, kolor=K["szary"], wrap=820).pack(fill="x", pady=(2, 0))

        # --- pasek boczny
        etykieta(k, "Pasek boczny", 10, bold=True).pack(fill="x", pady=(10, 4))
        r = tk.Frame(k, bg=K["karta"])
        r.pack(fill="x")
        etykieta(r, "Szerokość: ", 10).pack(side="left")
        self.bok_var = tk.IntVar(value=int(self.stan.d.get("bok_szer", 250)))
        suw_b = ttk.Scale(r, from_=self.BOK_MIN, to=self.BOK_MAX, orient="horizontal", variable=self.bok_var, length=220)
        suw_b.pack(side="left")
        wart_b = etykieta(r, f"{self.bok_var.get()} px", 9, kolor=K["szary"])
        wart_b.pack(side="left", padx=8)
        suw_b.bind("<Motion>", lambda e: wart_b.configure(text=f"{self.bok_var.get()} px"))
        suw_b.bind("<ButtonRelease-1>", lambda e: self._ustaw_bok(self.bok_var.get()))
        przycisk(r, "Rozwiń pasek" if self._bok_zwiniety() else "Zwiń do ikon", self._bok_przelacz, "drugi").pack(side="left", padx=8)
        etykieta(k, "Szerokość zmienisz też przeciągając prawą krawędź paska; przeciągnięcie bardzo wąsko zwija go do ikon.",
                 9, kolor=K["szary"], wrap=820).pack(fill="x", pady=(2, 0))

        etykieta(k, "Motyw", 10, bold=True).pack(fill="x", pady=(12, 0))
        biezacy = K.get("id", MOTYW_DOMYSLNY)
        for gid, gnazwa in GRUPY:
            etykieta(k, gnazwa, 10, bold=True).pack(fill="x", pady=(8, 4))
            siatka = tk.Frame(k, bg=K["karta"])
            siatka.pack(fill="x")
            motywy_grupy = [m for m in MOTYWY if m["grupa"] == gid]
            for i, m in enumerate(motywy_grupy):
                self._kafelek_motywu(siatka, m, m["id"] == biezacy).grid(row=i // 4, column=i % 4, padx=(0, 8), pady=(0, 8), sticky="w")

        z, k = karta(w, tytul="Projekt")
        z.pack(fill="x", padx=28, pady=(12, 0))
        etykieta(k, self.stan.d["projekt"] or "nie wybrano", 10, mono=True).pack(fill="x")
        przycisk(k, "Zmień katalog projektu…", self._wybierz_projekt, "drugi").pack(anchor="w", pady=(6, 0))

        z, k = karta(w, tytul="Eksport")
        z.pack(fill="x", padx=28, pady=(12, 0))
        etykieta(k, "Raport postępów w Markdown — wrzuć go do repo jako POSTEPY.md albo pokaż komuś, kto Cię wspiera.", 10, kolor=K["szary"], wrap=820).pack(fill="x")
        przycisk(k, "Eksportuj POSTEPY.md", self._eksport, "drugi").pack(anchor="w", pady=(6, 0))

        z, k = karta(w, tytul="Strefa ostrożności", bg=K["czerw_tlo"])
        z.pack(fill="x", padx=28, pady=(12, 24))
        etykieta(k, "Wyzeruj wszystkie postępy (zadania, sesje, quizy, dziennik, XP). Nie da się cofnąć.", 10, bg=K["czerw_tlo"], wrap=820).pack(fill="x")
        przycisk(k, "Wyzeruj dane", self._reset, "ostrz").pack(anchor="w", pady=(6, 0))

    def _wgraj_program(self):
        sc = filedialog.askopenfilename(title="Wybierz plik programu (JSON)", filetypes=[("Program Mentora", "*.json")], parent=self)
        if not sc:
            return
        cel, bledy = importuj_program(sc)
        if bledy:
            messagebox.showerror("Program", "Plik nie jest poprawnym programem:\n\n" + "\n".join(bledy[:10]), parent=self)
            return
        if messagebox.askyesno("Program", f"Program skopiowany do programy/{cel.name}.\n\nPrzełączyć na niego teraz?", parent=self):
            self.ustaw_program(cel)
        else:
            self.pokaz("ustawienia")

    def _szablon_programu(self):
        sc = filedialog.asksaveasfilename(parent=self, initialdir=str(KATALOG_PROGRAMOW), initialfile="moj-program.json",
                                          defaultextension=".json", filetypes=[("Program Mentora", "*.json")])
        if sc:
            zapisz_szablon(sc)
            messagebox.showinfo("Szablon", f"Zapisano {sc}.\nWypełnij go w edytorze tekstu (np. PyCharm) i wgraj przez „Wgraj program z pliku…”.", parent=self)

    def _ustaw_skale_czcionki(self, s):
        self.stan.d["skala_czcionki"] = s
        self.przebuduj()

    def _ustaw_jasnosc(self, j):
        self.stan.d["jasnosc_term"] = round(max(0.4, min(1.0, float(j))), 2)
        if K.get("grupa") == "terminal":
            self.przebuduj()
        else:
            self.stan.zapisz()

    def _ustaw_bok(self, szer):
        self.stan.d["bok_szer"] = int(max(self.BOK_MIN, min(self.BOK_MAX, szer)))
        self.stan.d["bok_zwiniety"] = False
        self.przebuduj()

    def _wybierz_czcionke_z_listy(self):
        self.pokaz("czcionki")

    def widok_czcionki(self):
        """Pełna lista czcionek systemu z podglądem — jako strona w aplikacji, nie osobne okno."""
        self._naglowek(self.tresc, "Wybierz czcionkę", "Kliknij czcionkę, żeby zobaczyć podgląd; „Użyj” zastosuje ją w całym programie.")
        cialo = tk.Frame(self.tresc, bg=K["tlo"])
        cialo.pack(fill="both", expand=True, padx=28, pady=(0, 20))
        rodziny = sorted(f for f in rodziny_czcionek() if not f.startswith("@"))
        lewa = tk.Frame(cialo, bg=K["tlo"], width=360)
        lewa.pack(side="left", fill="y")
        lewa.pack_propagate(False)
        szukaj = tk.StringVar()
        e = tk.Entry(lewa, textvariable=szukaj, font=czc(10), relief="flat", bg=K["karta"], fg=K["tekst"], insertbackground=K["tekst"])
        e.pack(fill="x", ipady=5)
        ramka = tk.Frame(lewa, bg=K["tlo"])
        ramka.pack(fill="both", expand=True, pady=(8, 0))
        lb = tk.Listbox(ramka, font=czc(10), bg=K["karta"], fg=K["tekst"], relief="flat", selectbackground=K["akcent"],
                        selectforeground=K["btn_tekst"], activestyle="none", highlightthickness=1, highlightbackground=K["ramka"])
        sb = ttk.Scrollbar(ramka, orient="vertical", command=lb.yview)
        lb.configure(yscrollcommand=sb.set)
        sb.pack(side="right", fill="y")
        lb.pack(side="left", fill="both", expand=True)
        prawa = tk.Frame(cialo, bg=K["tlo"])
        prawa.pack(side="left", fill="both", expand=True, padx=(16, 0))
        z, k = karta(prawa, tytul="Podgląd")
        z.pack(fill="x")
        podglad = tk.Label(k, text="Zażółć gęślą jaźń — def test_bmi(): assert 1 + 1 == 2", font=czc(13), bg=K["jasny"],
                           fg=K["tekst"], anchor="w", padx=12, pady=14, wraplength=560, justify="left")
        podglad.pack(fill="x")
        nazwa_lab = etykieta(k, f"Obecnie: {FONT}", 9, kolor=K["szary"])
        nazwa_lab.pack(fill="x", pady=(8, 0))

        def wypelnij(*_):
            f = szukaj.get().lower()
            lb.delete(0, "end")
            for r_ in rodziny:
                if f in r_.lower():
                    lb.insert("end", r_)

        def wybrana():
            i = lb.curselection()
            return lb.get(i[0]) if i else None

        def podejrzyj(_=None):
            w_ = wybrana()
            if w_:
                podglad.configure(font=(w_, czc(13)[1]), text=f"{w_}: Zażółć gęślą jaźń — def test_bmi(): assert 1 + 1 == 2")
                nazwa_lab.configure(text=f"Wybrana: {w_}")

        def uzyj():
            w_ = wybrana()
            if w_:
                self.stan.d["czcionka"] = w_
                self.aktywny = "ustawienia"
                self.przebuduj()

        szukaj.trace_add("write", wypelnij)
        lb.bind("<<ListboxSelect>>", podejrzyj)
        lb.bind("<Double-Button-1>", lambda e_: uzyj())
        wypelnij()
        bt = tk.Frame(k, bg=K["karta"])
        bt.pack(fill="x", pady=(12, 0))
        przycisk(bt, "Użyj tej czcionki", uzyj).pack(side="left")
        przycisk(bt, "Wróć do ustawień", lambda: self.pokaz("ustawienia"), "drugi").pack(side="left", padx=8)
        e.focus_set()

    def _kafelek_motywu(self, parent, m, wybrany):
        """Mały podgląd motywu: pasek boczny | tło z kartą i akcentem, pod spodem nazwa."""
        ramka = tk.Frame(parent, bg=K["akcent"] if wybrany else K["ramka"], padx=2, pady=2, cursor="hand2")
        wew = tk.Frame(ramka, bg=m["karta"], width=196, height=78)
        wew.pack()
        wew.pack_propagate(False)
        pod = tk.Frame(wew, bg=m["tlo"], height=46)
        pod.pack(fill="x")
        pod.pack_propagate(False)
        tk.Frame(pod, bg=m["bok"], width=34).pack(side="left", fill="y")
        srodek = tk.Frame(pod, bg=m["tlo"])
        srodek.pack(side="left", fill="both", expand=True, padx=6, pady=6)
        k1 = tk.Frame(srodek, bg=m["karta"], highlightbackground=m["ramka"], highlightthickness=1, height=14)
        k1.pack(fill="x")
        tk.Frame(srodek, bg=m["akcent"], height=8, width=60).pack(anchor="w", pady=(5, 0))
        tk.Label(wew, text=("✔ " if wybrany else "") + m["nazwa"], font=czc(8, "bold" if wybrany else "normal", mono=(m["font"] == m["mono"])),
                 bg=m["karta"], fg=m["tekst"], anchor="w", padx=6).pack(fill="x", pady=(3, 0))
        for wid in ramka.winfo_children() + [ramka]:
            self._zbinduj_rekurencyjnie(wid, lambda e, mid=m["id"]: self.zmien_motyw(mid))
        return ramka

    def _zbinduj_rekurencyjnie(self, wid, fn):
        wid.bind("<Button-1>", fn)
        for ch in wid.winfo_children():
            self._zbinduj_rekurencyjnie(ch, fn)

    def _eksport(self):
        s = self.stan.statystyki()
        linie = [f"# Postępy — {P.nazwa} (stan na {dzis()})", "",
                 f"- Seria: {s['seria']} dni (rekord {s['najdluzsza_seria']}) · XP: {s['xp']} · nauka łącznie: {czas_hm(s['minuty'])}",
                 f"- Zadania: {s['zadania_ukonczone']}/{s['zadania_wszystkie']} · ukończone tygodnie: {s['tygodnie_ukonczone']}/{P.liczba_tygodni()}", ""]
        for w in P.tygodnie:
            z, c = self.stan.postep_tygodnia(w)
            linie.append(f"## Tydzień {w['tydzien']}: {w['tytul']} ({z}/{c})")
            for zad in w["zadania"]:
                ok = self.stan.zrobione(zad["id"])
                linie.append(f"- [{'x' if ok else ' '}] {zad['tytul']}" + (f" — {self.stan.d['zadania'][zad['id']]}" if ok else ""))
            linie.append("")
        linie.append("## Checklista umiejętności")
        for gi, g in enumerate(P.checklista):
            for pi, p in enumerate(g["punkty"]):
                linie.append(f"- [{'x' if self.stan.d['checklista'].get(f'{gi}-{pi}') else ' '}] {p}")
        cel = Path(self.stan.d["projekt"]) if self.stan.d["projekt"] and Path(self.stan.d["projekt"]).is_dir() else KATALOG
        sciezka = filedialog.asksaveasfilename(parent=self, initialdir=str(cel), initialfile="POSTEPY.md", defaultextension=".md",
                                               filetypes=[("Markdown", "*.md")])
        if sciezka:
            Path(sciezka).write_text("\n".join(linie), encoding="utf-8")
            messagebox.showinfo("Eksport", f"Zapisano: {sciezka}", parent=self)

    def _reset(self):
        if messagebox.askyesno("Wyzeruj", "Na pewno wyzerować wszystkie postępy?", parent=self) and \
                messagebox.askyesno("Wyzeruj", "Naprawdę? Tego nie da się cofnąć.", parent=self):
            zachowaj = {k: self.stan.d[k] for k in ("imie", "projekt", "motyw", "czcionka", "skala_czcionki", "jasnosc_term",
                                                   "bok_szer", "bok_zwiniety") if k in self.stan.d}
            self.stan.d = json.loads(json.dumps(Stan.DOMYSLNE))
            self.stan.d.update(zachowaj)
            self.stan.d["start"] = str(dzis())
            self.stan.zapisz()
            self._timer_reset()
            self.pokaz("panel")


if __name__ == "__main__":
    app = Mentor()
    app.mainloop()
