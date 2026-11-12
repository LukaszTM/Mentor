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

import json
import shutil
import sys
from pathlib import Path

# W wersji .exe (PyInstaller) dane użytkownika leżą obok pliku exe, a wbudowane programy w paczce (sys._MEIPASS);
# przy pierwszym uruchomieniu kopiujemy je do katalogu programy/ obok exe, żeby dało się je edytować i dokładać własne.
ZAMROZONY = getattr(sys, "frozen", False)
KATALOG = Path(sys.executable).resolve().parent if ZAMROZONY else Path(__file__).resolve().parent
KATALOG_PROGRAMOW = KATALOG / "programy"
FORMAT = "mentor-program/1"


def _rozpakuj_wbudowane():
    if not ZAMROZONY:
        return
    zrodlo = Path(getattr(sys, "_MEIPASS", KATALOG)) / "programy"
    if not zrodlo.is_dir():
        return
    try:
        KATALOG_PROGRAMOW.mkdir(exist_ok=True)
        for f in zrodlo.iterdir():
            cel = KATALOG_PROGRAMOW / f.name
            if f.is_file() and not cel.exists():
                shutil.copy(f, cel)
    except OSError:
        pass


_rozpakuj_wbudowane()

DOMYSLNE = {
    "podtytul": "", "opis": "", "autor": "", "wersja": "1.0", "jezyk": "pl",
    "katalog_projektu": "projekt",
    "czas_dziennie_min": 90, "dni_w_tygodniu": [0, 1, 2, 3, 4], "dzien_quizu": 5, "dzien_wolny": 6,
    "zasady": [], "quizy": {}, "prompty": [], "claude_md": "", "szablony": {}, "checklista": [],
    "sciaga": [], "linki": [], "wskazowki": [], "motywacja_powrot": [], "pojecia": {}, "bledy": {},
    "pytania_rekrutacyjne": [], "tematy_wpisu": [], "stanowisko": "", "stan_prawny": "",
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
    for nr, qs in dane.get("quizy", {}).items():
        for q in qs:
            if not (isinstance(q.get("odp"), int) and 0 <= q["odp"] < len(q.get("o", []))):
                bledy.append(f"Quiz tygodnia {nr}: pytanie z błędnym „odp”: {q.get('p', '')[:40]}")
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
    """[(sciezka, nazwa, podtytul, liczba_tygodni)] z katalogu programy/."""
    wynik = []
    KATALOG_PROGRAMOW.mkdir(exist_ok=True)
    for p in sorted(KATALOG_PROGRAMOW.glob("*.json")):
        if p.name.startswith("szablon"):
            continue
        try:
            d = json.loads(p.read_text(encoding="utf-8"))
            wynik.append((p, d.get("nazwa", p.stem), d.get("podtytul", ""), len(d.get("tygodnie", []))))
        except (OSError, json.JSONDecodeError):
            wynik.append((p, p.stem + " (uszkodzony plik)", "", 0))
    return wynik


def importuj(zrodlo):
    """Kopiuje plik programu do programy/ po walidacji. Zwraca (sciezka_docelowa, błędy)."""
    dane, bledy = wczytaj_plik(zrodlo)
    if bledy:
        return None, bledy
    KATALOG_PROGRAMOW.mkdir(exist_ok=True)
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
