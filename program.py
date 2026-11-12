# -*- coding: utf-8 -*-
"""
Programy nauczania — wczytywanie, walidacja, program aktywny.

Program to plik JSON (format "mentor-program/1") w katalogu programy/. Minimalny program:
  nazwa, etapy, tygodnie (z zadaniami), lekcje. Reszta ma wartości domyślne.
Zobacz programy/szablon-programu.json — pusty szkielet do wypełnienia.

Użycie w aplikacji:
    from program import P, wczytaj, lista_programow
    wczytaj("programy/python-junior-qa.json")
    P.tygodnie, P.lekcje, P.quizy ...        # atrybuty = klucze JSON
Funkcje emulatora i widoków czytają P w chwili wywołania, więc zmiana programu działa od razu.
"""

import datetime as dt
import json
import os
import shutil
import sys
from pathlib import Path

# W wersji .exe (PyInstaller) zasoby wbudowane leżą w paczce (sys._MEIPASS — TYLKO DO ODCZYTU), a dane użytkownika
# (postępy, kursy, środowiska, logi) w katalogu danych użytkownika: %LOCALAPPDATA%\Mentor. Katalog EXE traktujemy jako
# potencjalnie tylko do odczytu (Program Files, pendrive z blokadą). Tryb przenośny: plik portable.txt obok EXE → dane obok EXE.
# Uruchomienie ze źródeł (python mentor.py): dane w katalogu repozytorium, jak dotąd. Zmienna MENTOR_DANE nadpisuje wszystko (testy).
ZAMROZONY = getattr(sys, "frozen", False)
WINDOWS = sys.platform.startswith("win")
KATALOG = Path(sys.executable).resolve().parent if ZAMROZONY else Path(__file__).resolve().parent
KATALOG_ZASOBOW = Path(getattr(sys, "_MEIPASS", KATALOG))          # tylko do odczytu w EXE
FORMAT = "mentor-program/1"


def _katalog_danych():
    env = os.environ.get("MENTOR_DANE")
    if env:
        return Path(env).expanduser().resolve()
    if not ZAMROZONY or (KATALOG / "portable.txt").exists():
        return KATALOG
    if WINDOWS:
        baza = os.environ.get("LOCALAPPDATA") or str(Path.home() / "AppData" / "Local")
        return Path(baza) / "Mentor"
    if sys.platform == "darwin":
        return Path.home() / "Library" / "Application Support" / "Mentor"
    return Path(os.environ.get("XDG_DATA_HOME") or Path.home() / ".local" / "share") / "mentor"


KATALOG_DANYCH = _katalog_danych()
KATALOG_PROGRAMOW = KATALOG_DANYCH / "programy"        # programy JSON + materialy/ (wbudowane i wgrane z pliku)
KATALOG_KURSOW = KATALOG_DANYCH / "kursy"              # kursy zaimportowane z paczek ZIP: kursy/<id>/{kurs.json, meta.json, paczka/}
KATALOG_SRODOWISK = KATALOG_DANYCH / "srodowiska"      # .venv i stan środowiska per kurs
KATALOG_LOGOW = KATALOG_DANYCH / "logi"
KATALOG_POBRANE = KATALOG_DANYCH / "pobrane"           # pobrane instalatory/runtime (z weryfikacją SHA-256)
KATALOG_RUNTIME = KATALOG_DANYCH / "python"            # Python zarządzany przez Mentora (gdy w systemie go nie ma)
PLIK_DANYCH = KATALOG_DANYCH / "mentor_dane.json"
MIGRACJA = {"wykonana": False, "kroki": [], "bledy": []}


def _utworz_katalogi():
    for k in (KATALOG_DANYCH, KATALOG_PROGRAMOW, KATALOG_KURSOW, KATALOG_SRODOWISK, KATALOG_LOGOW, KATALOG_POBRANE):
        try:
            k.mkdir(parents=True, exist_ok=True)
        except OSError as e:
            MIGRACJA["bledy"].append(f"Nie można utworzyć {k}: {e}")


def migruj_dane():
    """Przenosi dane z katalogu EXE (stary układ: mentor_dane.json i programy/ obok Mentor.exe) do katalogu danych użytkownika.
    Nic nie usuwa: oryginały zostają, a przed migracją powstaje kopia mentor_dane.json.kopia-<data>. Wynik w MIGRACJA."""
    if KATALOG_DANYCH == KATALOG:
        return
    stare = KATALOG / "mentor_dane.json"
    if stare.exists() and not PLIK_DANYCH.exists():
        try:
            kopia = KATALOG / f"mentor_dane.json.kopia-{dt.datetime.now():%Y%m%d-%H%M%S}"
            shutil.copy2(stare, kopia)
            shutil.copy2(stare, PLIK_DANYCH)
            MIGRACJA["kroki"].append(f"Postępy przeniesione do {PLIK_DANYCH} (kopia: {kopia.name}, oryginał obok EXE bez zmian).")
            MIGRACJA["wykonana"] = True
        except OSError as e:
            MIGRACJA["bledy"].append(f"Postępy: {e}")
    stare_prog = KATALOG / "programy"
    if stare_prog.is_dir() and stare_prog.resolve() != KATALOG_PROGRAMOW.resolve():
        n = 0
        try:
            for f in stare_prog.rglob("*"):
                if not f.is_file() or "__pycache__" in f.parts:
                    continue
                cel = KATALOG_PROGRAMOW / f.relative_to(stare_prog)
                if not cel.exists():
                    cel.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(f, cel)
                    n += 1
        except OSError as e:
            MIGRACJA["bledy"].append(f"Programy: {e}")
        if n:
            MIGRACJA["kroki"].append(f"Skopiowano {n} plików programów z katalogu EXE do {KATALOG_PROGRAMOW} (oryginały zostały).")
            MIGRACJA["wykonana"] = True


def _rozpakuj_wbudowane():
    """Wbudowane programy i materiały (z paczki EXE) trafiają do katalogu danych — tylko brakujące pliki, nic nie nadpisujemy."""
    if not ZAMROZONY:
        return
    zrodlo = KATALOG_ZASOBOW / "programy"
    if not zrodlo.is_dir():
        return
    try:
        KATALOG_PROGRAMOW.mkdir(parents=True, exist_ok=True)
        for f in zrodlo.rglob("*"):
            cel = KATALOG_PROGRAMOW / f.relative_to(zrodlo)
            if f.is_file() and not cel.exists():
                cel.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy(f, cel)
    except OSError as e:
        MIGRACJA["bledy"].append(f"Wbudowane programy: {e}")


_utworz_katalogi()
migruj_dane()
_rozpakuj_wbudowane()


def katalog_kursu(program_id):
    """Katalog kursu zaimportowanego z paczki ZIP (kursy/<id>/) albo None."""
    if not program_id:
        return None
    k = KATALOG_KURSOW / program_id
    return k if (k / "kurs.json").exists() else None


def meta_kursu(program_id):
    """meta.json kursu z paczki (id, wersja, źródło, data importu, wymagania, manifest) albo {}."""
    k = katalog_kursu(program_id)
    if not k:
        return {}
    try:
        return json.loads((k / "meta.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def katalog_materialow(program_id):
    """Katalog z materiałami kursu (START_TUTAJ.md, cwiczenia/, przyklady/, rozwiazania/, pomoc/) albo None.
    Kolejność: kursy/<id>/paczka (zaimportowany ZIP — jawna decyzja ucznia) → programy/materialy/<id> (wbudowane)."""
    if not program_id:
        return None
    kk = KATALOG_KURSOW / program_id / "paczka"
    if kk.is_dir():
        return kk
    k = KATALOG_PROGRAMOW / "materialy" / program_id
    return k if k.is_dir() else None


def skopiuj_materialy(program_id, cel):
    """Kopiuje materiały kursu do katalogu projektu bez nadpisywania istniejących plików.
    Zwraca (skopiowane, pominięte) — liczby plików."""
    zrodlo = katalog_materialow(program_id)
    if not zrodlo:
        return 0, 0
    cel = Path(cel)
    skopiowane = pominiete = 0
    for f in sorted(zrodlo.rglob("*")):
        if not f.is_file():
            continue
        c = cel / f.relative_to(zrodlo)
        if c.exists():
            pominiete += 1
            continue
        c.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(f, c)
        skopiowane += 1
    return skopiowane, pominiete

DOMYSLNE = {
    "podtytul": "", "opis": "", "autor": "", "wersja": "1.0", "jezyk": "pl",
    "katalog_projektu": "projekt",
    "czas_dziennie_min": 90, "dni_w_tygodniu": [0, 1, 2, 3, 4], "dzien_quizu": 5, "dzien_wolny": 6,
    "zasady": [], "quizy": {}, "prompty": [], "claude_md": "", "szablony": {}, "checklista": [],
    "sciaga": [], "linki": [], "wskazowki": [], "motywacja_powrot": [], "pojecia": {}, "bledy": {},
    "pytania_rekrutacyjne": [], "tematy_wpisu": [], "stanowisko": "", "stan_prawny": "",
    "narzedzia": [], "parametry": {}, "firma": "", "firma_osoby": [], "firma_regulaminy": [], "przepisy": [],
    "diagnoza": [], "pytania_dziennika": [], "materialy": "",
    "rytm_dnia": [
        {"nazwa": "Nowy temat", "minuty": 20, "ikona": "📖", "opis": "Lekcja i przykłady.", "prompt": "Uczę się [temat]. Wytłumacz na 2 przykładach i daj 3 zadania bez rozwiązań."},
        {"nazwa": "Ćwiczenie", "minuty": 50, "ikona": "⌨", "opis": "Samodzielna praca nad zadaniem.", "prompt": "Utknąłem na zadaniu [opis]. Nie podawaj rozwiązania — zadaj pytanie naprowadzające."},
        {"nazwa": "Recenzja", "minuty": 15, "ikona": "🔍", "opis": "Przegląd tego, co powstało.", "prompt": "Przejrzyj @[plik] jak cierpliwy mentor: co dobrze, co błędem, co czytelniej."},
        {"nazwa": "Podsumowanie", "minuty": 5, "ikona": "✅", "opis": "Zapis i 3 pytania sprawdzające.", "prompt": "Zadaj mi 3 pytania sprawdzające z tego, co dziś robiłem."},
    ],
}


class Program:
    """Opakowanie słownika z dostępem przez atrybuty. P.tygodnie[0]['zadania'] itd."""

    def __init__(self, dane=None, sciezka=None):
        self.d = {}
        self.sciezka = sciezka
        self.ustaw(dane or pusty())

    def ustaw(self, dane):
        d = dict(DOMYSLNE)
        d.update(dane)
        self.d = d
        self._lekcje_po_id = {l["id"]: l for l in d.get("lekcje", [])}
        self._tyg_po_nr = {w["tydzien"]: w for w in d.get("tygodnie", [])}

    def __getattr__(self, nazwa):
        if nazwa.startswith("_") or nazwa in ("d", "sciezka"):
            raise AttributeError(nazwa)
        try:
            return self.d[nazwa]
        except KeyError:
            raise AttributeError(nazwa)

    # --- wygodne dostępy
    def tydzien(self, nr):
        return self._tyg_po_nr.get(nr) or self.tygodnie[min(max(nr, 0), len(self.tygodnie) - 1)]

    def lekcja(self, lid):
        return self._lekcje_po_id.get(lid)

    def lekcje_tygodnia(self, nr):
        w = self.tydzien(nr)
        return [self._lekcje_po_id[l] for l in w.get("lekcje", []) if l in self._lekcje_po_id]

    def lekcja_po_nazwie(self, nazwa):
        n = (nazwa or "").strip().lower()
        for l in self.lekcje:
            if l["nazwa"].lower() == n:
                return l
        for l in self.lekcje:
            if n and (n in l["nazwa"].lower() or any(s.lower() in n for s in l.get("slowa", []))):
                return l
        return None

    def quiz_tygodnia(self, nr):
        return self.quizy.get(str(nr), [])

    def liczba_tygodni(self):
        return len(self.tygodnie)

    def wszystkie_zadania(self):
        return [z for w in self.tygodnie for z in w["zadania"]]

    def etap_tygodnia(self, nr):
        w = self.tydzien(nr)
        for e in self.etapy:
            if e["nr"] == w.get("etap"):
                return e
        return self.etapy[0] if self.etapy else {"nr": 0, "nazwa": "", "tygodnie": [], "cel": ""}


def pusty():
    return {
        "format": FORMAT, "id": "pusty", "nazwa": "Brak programu",
        "etapy": [{"nr": 0, "nazwa": "Start", "tygodnie": [0], "cel": ""}],
        "tygodnie": [{"tydzien": 0, "etap": 0, "tytul": "Brak programu", "tematy": "", "rola_asystenta": "", "lekcje": [], "zadania": []}],
        "lekcje": [],
    }


def waliduj(dane):
    """Zwraca listę błędów (pusta = OK). Sprawdza to, bez czego aplikacja by się wywaliła."""
    bledy = []
    if not isinstance(dane, dict):
        return ["Plik nie zawiera obiektu JSON."]
    for k in ("nazwa", "etapy", "tygodnie", "lekcje"):
        if k not in dane:
            bledy.append(f"Brak pola „{k}”.")
    if bledy:
        return bledy
    if not dane["tygodnie"]:
        bledy.append("Program nie ma żadnego tygodnia.")
    ids = set()
    lekcje_ids = {l.get("id") for l in dane["lekcje"]}
    for i, w in enumerate(dane["tygodnie"]):
        for k in ("tydzien", "tytul", "zadania"):
            if k not in w:
                bledy.append(f"Tydzień nr {i}: brak pola „{k}”.")
        for lid in w.get("lekcje", []):
            if lid not in lekcje_ids:
                bledy.append(f"Tydzień {w.get('tydzien')}: lekcja „{lid}” nie istnieje.")
        for z in w.get("zadania", []):
            if "id" not in z or "tytul" not in z:
                bledy.append(f"Tydzień {w.get('tydzien')}: zadanie bez id lub tytułu.")
                continue
            if z["id"] in ids:
                bledy.append(f"Powtórzone id zadania: {z['id']}.")
            ids.add(z["id"])
            z.setdefault("opis", "")
            z.setdefault("kroki", [])
            z.setdefault("sprawdz", "")
            z.setdefault("problemy", [])
            z.setdefault("pliki", [])
            z.setdefault("xp", 10)
            z.setdefault("czas_min", 60)
    for l in dane["lekcje"]:
        for k in ("id", "nazwa", "wyjasnienie"):
            if k not in l:
                bledy.append(f"Lekcja bez pola „{k}”: {l.get('id') or l.get('nazwa') or '?'}")
        l.setdefault("tydzien", 0)
        l.setdefault("slowa", [])
        l.setdefault("przyklad", "")
        l.setdefault("zadania", [])
        l.setdefault("pytania", [])
        l.setdefault("pulapki", [])
        l.setdefault("test", [])
        for q in l.get("test", []):
            if not (isinstance(q.get("odp"), int) and 0 <= q["odp"] < len(q.get("o", []))):
                bledy.append(f"Lekcja {l.get('id')}: pytanie testowe z błędnym „odp”: {q.get('p', '')[:40]}")
        # bloki standardu (opcjonalne) — jeśli są, muszą mieć właściwy kształt
        dem = l.get("demonstracja")
        if dem is not None and not (isinstance(dem, dict) and isinstance(dem.get("kroki", []), list)):
            bledy.append(f"Lekcja {l.get('id')}: „demonstracja” musi być obiektem z listą „kroki”.")
        for i, cw in enumerate(l.get("cwiczenia", []) or []):
            if not isinstance(cw, dict) or not cw.get("tresc"):
                bledy.append(f"Lekcja {l.get('id')}: ćwiczenie nr {i + 1} bez treści.")
                continue
            cw.setdefault("rodzaj", "samodzielne")
            cw.setdefault("wskazowki", [])
            cw.setdefault("rozwiazanie", "")
            cw.setdefault("wynik", "")
        for i, b in enumerate(l.get("typowe_bledy", []) or []):
            if not isinstance(b, dict) or not b.get("komunikat"):
                bledy.append(f"Lekcja {l.get('id')}: typowy błąd nr {i + 1} bez „komunikat”.")
    for nr, qs in dane.get("quizy", {}).items():
        for q in qs:
            if not (isinstance(q.get("odp"), int) and 0 <= q["odp"] < len(q.get("o", []))):
                bledy.append(f"Quiz tygodnia {nr}: pytanie z błędnym „odp”: {q.get('p', '')[:40]}")
            if q.get("lekcja") and q["lekcja"] not in lekcje_ids:
                bledy.append(f"Quiz tygodnia {nr}: pytanie wskazuje nieistniejącą lekcję „{q['lekcja']}”.")
    for i, q in enumerate(dane.get("diagnoza", []) or []):
        if not (isinstance(q, dict) and isinstance(q.get("odp"), int) and 0 <= q["odp"] < len(q.get("o", []))):
            bledy.append(f"Diagnoza: pytanie nr {i + 1} z błędnym „odp”.")
        elif q.get("lekcja") and q["lekcja"] not in lekcje_ids:
            bledy.append(f"Diagnoza: pytanie nr {i + 1} wskazuje nieistniejącą lekcję „{q['lekcja']}”.")
    for e in dane["etapy"]:
        for k in ("nr", "nazwa", "tygodnie"):
            if k not in e:
                bledy.append(f"Etap bez pola „{k}”.")
    return bledy


def wczytaj_plik(sciezka):
    """Czyta i waliduje JSON. Zwraca (dane, błędy)."""
    try:
        dane = json.loads(Path(sciezka).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        return None, [f"Nie można odczytać pliku: {e}"]
    bledy = waliduj(dane)
    return (dane if not bledy else None), bledy


def lista_programow():
    """[(sciezka, nazwa, podtytul, liczba_tygodni)] z katalogu programy/ oraz kursów z paczek (kursy/<id>/kurs.json)."""
    wynik, widziane = [], set()
    KATALOG_PROGRAMOW.mkdir(parents=True, exist_ok=True)
    sciezki = []
    if KATALOG_KURSOW.is_dir():   # kursy z paczek mają pierwszeństwo przed wbudowanym plikiem o tym samym id
        sciezki += sorted(p for p in KATALOG_KURSOW.glob("*/kurs.json") if not p.parent.name.startswith("_"))
    sciezki += [p for p in sorted(KATALOG_PROGRAMOW.glob("*.json")) if not p.name.startswith("szablon")]
    for p in sciezki:
        try:
            d = json.loads(p.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            wynik.append((p, p.stem + " (uszkodzony plik)", "", 0))
            continue
        pid = d.get("id") or p.stem
        if pid in widziane:
            continue
        widziane.add(pid)
        wynik.append((p, d.get("nazwa", p.stem), d.get("podtytul", ""), len(d.get("tygodnie", []))))
    return wynik


def importuj(zrodlo):
    """Kopiuje plik programu do programy/ po walidacji. Zwraca (sciezka_docelowa, błędy)."""
    dane, bledy = wczytaj_plik(zrodlo)
    if bledy:
        return None, bledy
    KATALOG_PROGRAMOW.mkdir(parents=True, exist_ok=True)
    cel = KATALOG_PROGRAMOW / Path(zrodlo).name
    if cel.exists() and cel.resolve() != Path(zrodlo).resolve():
        i = 2
        while (KATALOG_PROGRAMOW / f"{Path(zrodlo).stem}-{i}.json").exists():
            i += 1
        cel = KATALOG_PROGRAMOW / f"{Path(zrodlo).stem}-{i}.json"
    if cel.resolve() != Path(zrodlo).resolve():
        shutil.copy(zrodlo, cel)
    return cel, []


P = Program()


def wczytaj(sciezka):
    """Ustawia program aktywny. Zwraca listę błędów (pusta = OK); przy błędach P zostaje bez zmian."""
    dane, bledy = wczytaj_plik(sciezka)
    if bledy:
        return bledy
    P.ustaw(dane)
    P.sciezka = str(sciezka)
    return []


def domyslna_sciezka():
    lista = lista_programow()
    for p, *_ in lista:
        if p.stem == "python-junior-qa":
            return p
    return lista[0][0] if lista else None


SZABLON = {
    "format": FORMAT,
    "id": "moj-program",
    "nazwa": "Mój program nauki",
    "podtytul": "np. 4 tygodnie · czego i po co",
    "opis": "Jedno–dwa zdania: co uczeń potrafi po ukończeniu.",
    "autor": "",
    "wersja": "1.0",
    "katalog_projektu": "moj-projekt",
    "czas_dziennie_min": 60,
    "zasady": ["Najpierw próbujesz sam, potem pytasz.", "Przepisuj, nie kopiuj."],
    "etapy": [{"nr": 0, "nazwa": "Podstawy", "tygodnie": [0, 1], "cel": "Co uczeń umie po etapie."}],
    "tygodnie": [
        {"tydzien": 0, "etap": 0, "tytul": "Tytuł tygodnia", "tematy": "temat A, temat B",
         "rola_asystenta": "Co asystent może, a czego nie może robić w tym tygodniu.",
         "lekcje": ["lekcja-1"],
         "zadania": [
             {"id": "t0z1", "tytul": "Nazwa zadania", "opis": "Jedno zdanie, co ma powstać.",
              "kroki": ["Krok 1 — konkretnie, z komendami/kliknięciami.", "Krok 2.", "Krok 3."],
              "sprawdz": "Jak samemu sprawdzić, że gotowe.", "problemy": ["Typowy problem → co zrobić."],
              "pliki": ["plik_do_wykrycia.py"], "xp": 10, "czas_min": 45},
             {"id": "t0z2", "tytul": "Zadanie tygodnia (większe)", "opis": "", "kroki": ["…"], "sprawdz": "", "pliki": [], "xp": 25, "czas_min": 90}
         ]},
    ],
    "lekcje": [
        {"id": "lekcja-1", "tydzien": 0, "nazwa": "Nazwa lekcji",
         "cel": "po tej lekcji uczeń potrafi… (jedno zdanie)", "czas_min": 20,
         "slowa": ["słowa", "kluczowe", "do rozpoznania w promptach"],
         "wyjasnienie": "## Nagłówek sekcji\nKrótka lekcja: 2–4 akapity z przykładami z życia ucznia.\n- punkt listy\n- drugi punkt",
         "w_praktyce": ["Krok 1 — jak to robisz naprawdę.", "Krok 2."],
         "przyklad": "kod lub przykład krok po kroku",
         "zadania": ["Zadanie łatwe.", "Średnie.", "Trudniejsze."],
         "pytania": [["Pytanie otwarte?", "Wzorcowa odpowiedź."]],
         "pulapki": ["Na co uważać."],
         "test": [{"p": "Pytanie zamknięte?", "o": ["A", "B", "C", "D"], "odp": 1, "w": "Wyjaśnienie poprawnej odpowiedzi."}]}
    ],
    "quizy": {"0": [{"p": "Pytanie z tygodnia 0?", "o": ["A", "B", "C", "D"], "odp": 0, "w": "Dlaczego A."}]},
    "checklista": [{"po": "Po tygodniu 0", "punkty": ["Umiem X bez pomocy."]}],
    "prompty": [{"nazwa": "Nowy temat", "kiedy": "Początek dnia", "tresc": "Uczę się [temat]. Wytłumacz i daj 3 zadania bez rozwiązań."}],
    "sciaga": [{"tytul": "Skróty", "pozycje": [["komenda", "co robi"]]}],
    "linki": [["Dokumentacja", "https://example.org"]],
    "wskazowki": ["Jedna zasada nauki dziennie."],
    "motywacja_powrot": ["Dobrze, że jesteś."],
}


def zapisz_szablon(cel=None):
    cel = Path(cel) if cel else KATALOG_PROGRAMOW / "szablon-programu.json"
    cel.write_text(json.dumps(SZABLON, ensure_ascii=False, indent=1), encoding="utf-8")
    return cel


if __name__ == "__main__":
    print(zapisz_szablon())
    for p, n, pod, t in lista_programow():
        d, b = wczytaj_plik(p)
        print(p.name, "—", n, f"({t} tyg.)", "OK" if not b else b)
