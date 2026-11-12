# -*- coding: utf-8 -*-
"""
Asystent — dwa silniki dla osób bez subskrypcji Claude Code:

  EmulatorOffline  — bez konta i internetu. Nie jest modelem językowym: rozpoznaje prompty z planu nauki
                     (uczę się…, utknąłem…, przejrzyj @plik…, quiz…, commit…), tłumaczy tematy z wiedza.py,
                     recenzuje kod analizą statyczną (ast), uruchamia pliki i tłumaczy tracebacki, prowadzi quiz,
                     pomaga z commitem. Zanim coś wykona lub zapisze, pyta o zgodę — jak Claude Code w trybie „pytaj”.

  KlientAPI        — prawdziwy Claude przez Anthropic API (klucz z console.anthropic.com, płatność za użycie).
                     Dostaje zasady z CLAUDE.md i kontekst tygodnia; pliki wskazane przez @nazwa.py czyta z projektu.
"""

import ast
import datetime as dt
import json
import os
import random
import re
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

from program import P
from wiedza_ogolna import BLEDY_OGOLNE

def _bledy():
    return P.bledy or BLEDY_OGOLNE


POMIJANE = {".git", ".venv", "venv", "env", "__pycache__", "node_modules", ".idea", ".pytest_cache"}
WINDOWS = sys.platform.startswith("win")


def _flagi():
    return {"creationflags": subprocess.CREATE_NO_WINDOW} if WINDOWS else {}


def znajdz_plik(projekt, nazwa):
    """Szuka pliku po nazwie w katalogu projektu (bez .venv/.git)."""
    if not projekt:
        return None
    p = Path(projekt)
    if (p / nazwa).is_file():
        return p / nazwa
    for root, dirs, files in os.walk(projekt):
        dirs[:] = [d for d in dirs if d not in POMIJANE]
        if nazwa in files:
            return Path(root) / nazwa
    return None


def pliki_z_tekstu(tekst):
    """Nazwy plików z tekstu: @bmi.py, bmi.py, test_x.py, README.md…"""
    znalezione = re.findall(r"@?([\w\-./\\]+\.(?:py|md|csv|txt|yml|yaml|json|html))\b", tekst)
    wynik = []
    for z in znalezione:
        if z not in wynik:
            wynik.append(z)
    return wynik


# ===========================================================================
# Analiza statyczna kodu — recenzja „jak cierpliwy mentor”
# ===========================================================================
def analizuj_kod(zrodlo, nazwa="plik.py"):
    """Zwraca słownik: dobrze / bledy / czytelniej / pytanie. Nie poprawia kodu."""
    wynik = {"dobrze": [], "bledy": [], "czytelniej": [], "pytanie": ""}
    try:
        drzewo = ast.parse(zrodlo, filename=nazwa)
    except SyntaxError as e:
        wynik["bledy"].append(f"Błąd składni w linii {e.lineno}: {e.msg}. Zajrzyj też do linii {max(1, (e.lineno or 1) - 1)} — "
                              "brakujący dwukropek lub nawias objawia się zwykle linię niżej.")
        wynik["pytanie"] = "Czy każdy if/for/while/def w tym pliku kończy się dwukropkiem i czy nawiasy są domknięte?"
        return wynik

    linie = zrodlo.splitlines()
    funkcje = [n for n in ast.walk(drzewo) if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]
    klasy = [n for n in ast.walk(drzewo) if isinstance(n, ast.ClassDef)]
    petle = [n for n in ast.walk(drzewo) if isinstance(n, (ast.For, ast.While))]
    try_bloki = [n for n in ast.walk(drzewo) if isinstance(n, ast.Try)]
    importy = [n for n in ast.walk(drzewo) if isinstance(n, (ast.Import, ast.ImportFrom))]

    # --- co jest dobrze
    if funkcje:
        z_doc = [f for f in funkcje if ast.get_docstring(f)]
        wynik["dobrze"].append(f"Kod podzielony na {len(funkcje)} funkcj{'ę' if len(funkcje) == 1 else 'e/i'}"
                               + (f", {len(z_doc)} z docstringiem." if z_doc else "."))
    if klasy:
        wynik["dobrze"].append(f"Używasz klas ({', '.join(k.name for k in klasy)}) — dane i czynności razem.")
    if try_bloki:
        wynik["dobrze"].append("Jest obsługa błędów try/except — program nie wywala się na złym wpisie.")
    dlugie_nazwy = [n.id for n in ast.walk(drzewo) if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Store) and len(n.id) > 3]
    if dlugie_nazwy:
        wynik["dobrze"].append(f"Opisowe nazwy zmiennych (np. {', '.join(sorted(set(dlugie_nazwy))[:3])}).")
    if any(isinstance(n, ast.If) and isinstance(n.test, ast.Compare) and getattr(n.test.left, "id", "") == "__name__" for n in drzewo.body):
        wynik["dobrze"].append("Jest blok if __name__ == \"__main__\": — plik da się bezpiecznie importować.")
    if not wynik["dobrze"]:
        wynik["dobrze"].append("Plik się parsuje — składnia w porządku. Na tym etapie to już coś.")

    # --- błędy i ryzyka
    for n in ast.walk(drzewo):
        if isinstance(n, ast.ExceptHandler) and n.type is None:
            wynik["bledy"].append(f"Linia {n.lineno}: gołe except: łapie WSZYSTKO, także literówki w Twoim kodzie, i je ukrywa. "
                                  "Jaki konkretnie błąd chcesz tu złapać?")
        if isinstance(n, ast.While) and isinstance(n.test, ast.Constant) and n.test.value is True:
            ma_break = any(isinstance(m, ast.Break) for m in ast.walk(n))
            if not ma_break:
                wynik["bledy"].append(f"Linia {n.lineno}: while True bez break — pętla nie ma wyjścia.")
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
            for d in n.args.defaults:
                if isinstance(d, (ast.List, ast.Dict, ast.Set)):
                    wynik["bledy"].append(f"Linia {n.lineno}: zmienna wartość domyślna ({ast.unparse(d)}) w def {n.name} — "
                                          "jest współdzielona między wywołaniami. Klasyczna pułapka.")
        if isinstance(n, ast.Compare) and any(isinstance(c, (ast.Eq, ast.NotEq)) for c in n.ops):
            for c in n.comparators:
                if isinstance(c, ast.Constant) and c.value is None:
                    wynik["czytelniej"].append(f"Linia {n.lineno}: porównanie z None pisz przez „is None” / „is not None”.")
                elif isinstance(c, ast.Constant) and isinstance(c.value, bool):
                    wynik["czytelniej"].append(f"Linia {n.lineno}: „== {c.value}” jest zbędne — if warunek: / if not warunek:.")

    # input() użyty w arytmetyce bez zamiany typu
    zmienne_z_input = set()
    for n in ast.walk(drzewo):
        if isinstance(n, ast.Assign) and isinstance(n.value, ast.Call) and getattr(n.value.func, "id", "") == "input":
            for t in n.targets:
                if isinstance(t, ast.Name):
                    zmienne_z_input.add(t.id)
    if zmienne_z_input:
        ARYTM = (ast.Sub, ast.Div, ast.FloorDiv, ast.Mod, ast.Pow, ast.Mult)
        for n in ast.walk(drzewo):
            if isinstance(n, (ast.BinOp, ast.Compare)):
                strony = [n.left] + (n.comparators if isinstance(n, ast.Compare) else [n.right])
                nazwy = {s.id for s in strony if isinstance(s, ast.Name)}
                liczby = any(isinstance(s, ast.Constant) and isinstance(s.value, (int, float)) and not isinstance(s.value, bool) for s in strony)
                arytmetyka = isinstance(n, ast.BinOp) and isinstance(n.op, ARYTM)
                trafione = nazwy & zmienne_z_input
                if trafione and (liczby or arytmetyka):
                    wynik["bledy"].append(f"Linia {n.lineno}: {', '.join(sorted(trafione))} pochodzi z input() — to NAPIS, a tu liczysz lub porównujesz "
                                          "jak z liczbą. Jakiego typu jest ta zmienna w tym miejscu i gdzie powinna zmienić typ?")
                    break

    # zmienne przypisane, nigdy nieczytane (poza _ i wielkimi stałymi)
    przypisane, czytane = {}, set()
    for n in ast.walk(drzewo):
        if isinstance(n, ast.Name):
            if isinstance(n.ctx, ast.Store):
                przypisane.setdefault(n.id, n.lineno)
            else:
                czytane.add(n.id)
    nieuzyte = [(v, l) for v, l in przypisane.items() if v not in czytane and not v.startswith("_") and not v.isupper()]
    for v, l in nieuzyte[:3]:
        wynik["czytelniej"].append(f"Linia {l}: zmienna {v} jest ustawiana, ale nigdzie potem używana — potrzebna?")

    # --- czytelność
    for f in funkcje:
        dl = (getattr(f, "end_lineno", f.lineno) or f.lineno) - f.lineno + 1
        if dl > 30:
            wynik["czytelniej"].append(f"Funkcja {f.name} ma {dl} linii. Którą część dałoby się wydzielić jako osobną funkcję z własną nazwą?")
        if not ast.get_docstring(f) and not f.name.startswith("test_"):
            wynik["czytelniej"].append(f"def {f.name} (linia {f.lineno}) bez docstringa — jedno zdanie: co zwraca i po co.")
    krotkie = sorted({n.id for n in ast.walk(drzewo) if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Store)
                      and len(n.id) == 1 and n.id not in "ijknxyfe_"})
    if krotkie:
        wynik["czytelniej"].append(f"Jednoliterowe nazwy: {', '.join(krotkie)}. Co trzymają? Nazwa powinna to mówić (waga_kg, nie w).")
    for n in ast.walk(drzewo):
        if isinstance(n, ast.For) and isinstance(n.iter, ast.Call) and getattr(n.iter.func, "id", "") == "range":
            arg = n.iter.args[0] if n.iter.args else None
            if isinstance(arg, ast.Call) and getattr(arg.func, "id", "") == "len" and len(n.iter.args) == 1:
                wynik["czytelniej"].append(f"Linia {n.lineno}: for i in range(len(lista)) — jeśli nie potrzebujesz indeksu, "
                                           "czytelniej: for element in lista (albo enumerate, gdy potrzebujesz obu).")
        if isinstance(n, ast.Call) and getattr(n.func, "id", "") == "len" and isinstance(getattr(n, "parent", None), ast.Compare):
            pass
    if len(linie) > 120 and len(funkcje) < 3:
        wynik["czytelniej"].append(f"{len(linie)} linii i tylko {len(funkcje)} funkcje — plik rośnie. Co da się podzielić na funkcje lub moduły?")
    if "print(" in zrodlo and funkcje and any("return" not in ast.unparse(f) for f in funkcje if f.name not in ("main",)):
        bez_return = [f.name for f in funkcje if f.name != "main" and not any(isinstance(m, ast.Return) for m in ast.walk(f))]
        if bez_return:
            wynik["czytelniej"].append(f"Funkcje bez return ({', '.join(bez_return[:3])}) — wypisują wynik zamiast go zwracać. "
                                       "Taką funkcję trudno przetestować pytestem. Czy mogłaby zwracać wartość, a print zostawić na zewnątrz?")

    # --- pytanie naprowadzające
    if wynik["bledy"]:
        wynik["pytanie"] = "Weź pierwszy punkt z listy błędów: w której linii zmienna dostaje wartość, która potem psuje wynik? Wypisz ją print()-em tuż przed tą linią."
    elif wynik["czytelniej"]:
        wynik["pytanie"] = "Gdybyś miał wytłumaczyć ten plik koledze bez IT w 3 zdaniach — które miejsce byłoby najtrudniejsze do opowiedzenia? To miejsce prosi o refaktor."
    else:
        wynik["pytanie"] = "Co się stanie, gdy użytkownik wpisze pustą linię, zero albo literę tam, gdzie oczekujesz liczby? Sprawdź ręcznie, zanim napiszesz test."
    # odfiltruj duplikaty, zachowując kolejność
    for k in ("dobrze", "bledy", "czytelniej"):
        widziane, nowe = set(), []
        for x in wynik[k]:
            if x not in widziane:
                widziane.add(x)
                nowe.append(x)
        wynik[k] = nowe[:6]
    return wynik


def uruchom_plik(sciezka, dane_wejsciowe="", limit=10):
    """Uruchamia plik .py w osobnym procesie; zwraca (kod, stdout, stderr)."""
    try:
        r = subprocess.run([sys.executable, str(sciezka)], cwd=str(Path(sciezka).parent), input=dane_wejsciowe,
                           capture_output=True, text=True, timeout=limit, **_flagi())
        return r.returncode, r.stdout, r.stderr
    except subprocess.TimeoutExpired as e:
        return -1, (e.stdout or ""), f"Program nie skończył się w {limit} s — pętla nieskończona albo czeka na input()."
    except OSError as e:
        return -2, "", str(e)


def wyjasnij_traceback(stderr):
    """Z tracebacku wyciąga typ błędu, komunikat, linię; dokłada wyjaśnienie ze słownika błędów programu."""
    if not stderr.strip():
        return None
    linie = stderr.strip().splitlines()
    ostatnia = linie[-1]
    typ, _, komunikat = ostatnia.partition(":")
    typ = typ.strip().split(".")[-1]
    nr = None
    for l in reversed(linie):
        m = re.search(r'File "([^"]+)", line (\d+)', l)
        if m:
            nr = int(m.group(2))
            break
    if typ == "EOFError":
        return {"typ": typ, "komunikat": komunikat.strip(), "linia": nr,
                "co": "Program wywołał input(), a Asystent nie podał danych.",
                "pytanie": "Uruchom go w terminalu (python plik.py) albo podaj dane po <<, np.: /uruchom plik.py << 12; 34"}
    opis = _bledy().get(typ)
    return {"typ": typ, "komunikat": komunikat.strip(), "linia": nr,
            "co": opis["co"] if opis else "Tego typu nie mam w słowniku — przeczytaj komunikat od końca: ostatnia linia mówi CO, wyżej GDZIE.",
            "pytanie": opis["pytanie"] if opis else "Która wartość w tej linii nie jest tym, czym myślałeś, że jest? Wypisz ją print()-em."}


# ===========================================================================
# Ukryte błędy i programy ćwiczeniowe
# ===========================================================================
MUTACJE = [
    (r"\+=", "=", "przypisanie zamiast dodawania"),
    (r"(?<![<>=!])<(?!=)", "<=", "nierówność nieostra zamiast ostrej"),
    (r"(?<![<>=!])>(?!=)", ">=", "nierówność nieostra zamiast ostrej"),
    (r"range\((\w+)\)", r"range(1, \1)", "pętla pomija pierwszy element"),
    (r"== 0\b", "== 1", "zły warunek graniczny"),
    (r"\breturn (\w+)\b", r"return \1 * 1 + 0\n    return None", "kod po return — nieosiągalny"),
    (r"\.append\(", ".insert(0, ", "dodawanie na początek zamiast na koniec"),
    (r"\.lower\(\)", ".upper()", "wielkość liter odwrócona"),
    (r"/ len\(", "/ 1 * len(", "zła kolejność działań"),
    (r"\bmax\(", "min(", "min zamiast max"),
]


def wprowadz_ukryty_blad(zrodlo):
    """Jedna losowa mutacja w kodzie. Zwraca (nowy_kod, opis) lub (None, powód)."""
    kandydaci = [(wz, zam, opis) for wz, zam, opis in MUTACJE if re.search(wz, zrodlo)]
    random.shuffle(kandydaci)
    for wz, zam, opis in kandydaci:
        trafienia = list(re.finditer(wz, zrodlo))
        if not trafienia:
            continue
        t = random.choice(trafienia)
        nowy = zrodlo[:t.start()] + re.sub(wz, zam, t.group(0), count=1) + zrodlo[t.end():]
        try:
            ast.parse(nowy)
        except SyntaxError:
            continue
        if nowy != zrodlo:
            nr = zrodlo[:t.start()].count("\n") + 1
            return nowy, f"linia {nr}: {opis}"
    return None, "W tym pliku nie znalazłem miejsca na bezpieczną mutację (za mało pętli, porównań lub operacji)."


PROGRAM_DEBUG = '''"""Dziennik stada — wersja ćwiczeniowa do debugowania. Zawiera 3 ukryte błędy."""
import csv


def wczytaj(sciezka):
    """Wczytuje zwierzęta z CSV do listy słowników."""
    zwierzeta = []
    with open(sciezka, encoding="utf-8", newline="") as f:
        for wiersz in csv.DictReader(f):
            wiersz["waga"] = float(wiersz["waga"])
            zwierzeta.append(wiersz)
    return zwierzeta


def srednia_waga(zwierzeta):
    """Średnia waga stada."""
    suma = 0
    for z in zwierzeta:
        suma = z["waga"]
    return suma / len(zwierzeta)


def najciezsze(zwierzeta):
    """Zwraca zwierzę o największej wadze."""
    naj = zwierzeta[0]
    for z in zwierzeta:
        if z["waga"] < naj["waga"]:
            naj = z
    return naj


def po_rasie(zwierzeta, rasa):
    """Lista zwierząt danej rasy (bez względu na wielkość liter)."""
    wynik = []
    for z in zwierzeta:
        if z["rasa"].lower() == rasa:
            wynik.append(z)
    return wynik


def dodaj(zwierzeta, imie, rasa, waga):
    """Dodaje zwierzę do listy i zwraca listę."""
    zwierzeta.append({"imie": imie, "rasa": rasa, "waga": waga})
    return zwierzeta


def statystyki(zwierzeta):
    """Wypisuje podsumowanie."""
    print("Liczba zwierząt:", len(zwierzeta))
    print("Średnia waga:", round(srednia_waga(zwierzeta), 1))
    print("Najcięższe:", najciezsze(zwierzeta)["imie"])


if __name__ == "__main__":
    stado = [
        {"imie": "Krasula", "rasa": "HF", "waga": 612.0},
        {"imie": "Mućka", "rasa": "Simental", "waga": 580.0},
        {"imie": "Łaciata", "rasa": "HF", "waga": 640.0},
    ]
    dodaj(stado, "Bystra", "Jersey", 450.0)
    statystyki(stado)
    print("HF:", [z["imie"] for z in po_rasie(stado, "HF")])
'''
BLEDY_DEBUG = ["srednia_waga: suma = z[\"waga\"] zamiast suma += — średnia to waga ostatniego zwierzęcia",
               "najciezsze: porównanie < zamiast > — zwraca najlżejsze",
               "po_rasie: argument rasa nie jest zamieniony na małe litery — po_rasie(stado, \"HF\") zwraca pustą listę"]


# ===========================================================================
# Emulator offline
# ===========================================================================
class EmulatorOffline:
    """Rozmowa w stylu Claude Code bez modelu językowego. odpowiedz() zwraca listę (styl, tekst)."""

    def __init__(self, kontekst):
        """kontekst() -> dict: projekt, tydzien, tematy, imie, tryb_zgody"""
        self.kontekst = kontekst
        self.oczekuje = None      # (opis, funkcja) — czeka na „t”
        self.quiz = None
        self.rekrutacja = None
        self.ostatni_temat = None
        self._ostatnie_pytania = []
        self.ukryte = {}          # plik -> opis błędu

    # ---------------------------------------------------------------- pomocnicze
    def _k(self):
        return self.kontekst()

    def _projekt(self):
        return self._k().get("projekt") or ""

    def _tydzien(self):
        return P.tydzien(self._k().get("tydzien", 0))

    def _temat(self, tekst):
        t = tekst.lower()
        najlepszy, punkty = None, 0
        for temat in P.lekcje:
            p = sum(1 for s in temat["slowa"] if s.lower() in t)
            if temat["nazwa"].lower() in t:
                p += 3
            if p > punkty:
                najlepszy, punkty = temat, p
        return najlepszy

    def _pojecie(self, tekst):
        t = tekst.lower()
        for nazwa, opis in P.pojecia.items():
            if nazwa in t:
                return nazwa, opis
        return None, None

    def _potwierdzenie(self, opis, funkcja):
        if self._k().get("tryb_zgody", True):
            self.oczekuje = (opis, funkcja)
            return [("ostrz", f"Zamierzam: {opis}"), ("pytanie", "Wykonać? Wpisz  t  (tak) albo  n  (nie). "
                                                       "W trybie „pytaj” nic nie robię bez Twojej zgody — jak Claude Code po Shift+Tab.")]
        return funkcja()

    # ---------------------------------------------------------------- główne wejście
    def odpowiedz(self, tekst):
        tekst = tekst.strip()
        if not tekst:
            return []
        t = tekst.lower()

        # 1) oczekujące potwierdzenie
        if self.oczekuje:
            opis, fn = self.oczekuje
            self.oczekuje = None
            if t in ("t", "tak", "y", "yes", "ok"):
                return fn()
            return [("tekst", "Dobrze, nie robię tego. Twój kod, Twoja decyzja.")]

        # 2) trwający quiz / rekrutacja
        if self.quiz:
            return self._quiz_odpowiedz(t)
        if self.rekrutacja is not None:
            return self._rekrutacja_odpowiedz(tekst)

        # 3) komendy
        if t.startswith("/"):
            return self._komenda(tekst)

        # 4) prompty z planu
        pliki = pliki_z_tekstu(tekst)
        if any(s in t for s in ("ukryty błąd", "ukryty blad", "wprowadź do", "wprowadz do")) and pliki:
            return self._ukryty_blad(pliki[0])
        if "program z 3 błęd" in t or "program z 3 bled" in t or "z ukrytymi błędami" in t or "do debugowania" in t:
            return self._program_debug()
        if any(s in t for s in ("przejrzyj", "recenz", "sprawdź @", "sprawdz @", "oceń @", "ocen @")) and pliki:
            return self._recenzja(pliki[0])
        if any(s in t for s in ("utknął", "utknal", "nie działa", "nie dziala", "błąd:", "blad:", "error", "traceback", "wywala")):
            return self._utknalem(tekst, pliki)
        if pliki and any(s in t for s in ("uruchom", "odpal", "wykonaj")):
            return self._uruchom(pliki[0], self._dane_wejsciowe(tekst))
        if t.startswith(("myślę, że", "mysle, ze", "myślę że", "mysle ze")) or "czy dobrze rozumiem" in t:
            return self._sprawdz_rozumienie(tekst, pliki)
        if "quiz" in t:
            return self._quiz_start(tekst)
        if any(s in t for s in ("pytania sprawdzając", "pytania sprawdzajac", "3 pytania", "trzy pytania", "odpytaj")) and "rekrut" not in t:
            return self._pytania_sprawdzajace(tekst)
        if any(s in t for s in ("rekruter", "rekrutac", "rozmow")):
            return self._rekrutacja_start()
        if "commit" in t:
            return self._commit()
        if any(s in t for s in ("zatrzymaj", "zrobiłeś to za mnie", "zrobiles to za mnie", "cofnij")):
            return [("tekst", "Zatrzymuję się. W trybie offline i tak nie zmieniam Twoich plików bez zgody — ale masz rację co do zasady."),
                    ("pytanie", "Pierwszy krok, i tylko pierwszy: napisz samą nazwę funkcji i jej docstring. Co ma przyjmować, co zwracać? Wróć, gdy to będzie w pliku.")]
        if any(s in t for s in ("chcę zbudować", "chce zbudowac", "plan projektu", "zaproponuj strukturę", "zaproponuj strukture", "plan.md")):
            return self._plan(tekst)
        if t.startswith(("co to jest", "co to", "czym jest", "wytłumacz mi, czym", "wytlumacz mi, czym")):
            nazwa, opis = self._pojecie(tekst)
            if opis:
                return [("naglowek", nazwa.capitalize()), ("tekst", opis),
                        ("pytanie", "Powiedz to teraz własnymi słowami, na przykładzie z Twojego gospodarstwa. Jeśli się nie da — zapytaj „dlaczego”.")]
        if any(s in t for s in ("uczę się", "ucze sie", "wytłumacz", "wytlumacz", "wyjaśnij", "wyjasnij", "naucz", "temat", "jak działa", "jak dziala")):
            temat = self._temat(tekst)
            if temat:
                return self._wyjasnij_temat(temat)
            nazwa, opis = self._pojecie(tekst)
            if opis:
                return [("naglowek", nazwa.capitalize()), ("tekst", opis)]
        if any(s in t for s in ("zadani", "ćwicz", "cwicz")) and self.ostatni_temat:
            return self._zadania(self.ostatni_temat)
        if t in ("cześć", "czesc", "hej", "hello", "dzień dobry", "dzien dobry", "siema", "witaj"):
            k = self._k()
            return [("tekst", f"Cześć{', ' + k['imie'] if k.get('imie') else ''}. Tryb offline: umiem to, co jest w planie nauki — "
                              "tematy, recenzje plików, uruchamianie, quizy, commit. Wpisz /help albo po prostu: „uczę się pętli”."),
                    ("tekst", f"Twój tydzień: {k.get('tydzien', 0)} — {self._tydzien()['tytul']}.")]
        if t.startswith("dlaczego"):
            return self._dlaczego(tekst)

        # 5) ostatnia deska: dopasuj temat po słowach, inaczej powiedz uczciwie
        temat = self._temat(tekst)
        if temat:
            return [("tekst", f"Brzmi jak temat „{temat['nazwa']}”. Wyjaśniam:")] + self._wyjasnij_temat(temat)
        return [("ostrz", "Tryb offline nie rozumie dowolnych pytań — to podręcznik z komendami, nie model językowy."),
                ("tekst", "Umiem: „uczę się [temat]”, „przejrzyj @plik.py”, „utknąłem … błąd: …”, „uruchom @plik.py”, „quiz z tygodnia N”, "
                          "„zadaj mi 3 pytania”, „co to jest [pojęcie]”, „commit”, „odpytaj mnie jak rekruter”, „chcę zbudować [projekt]”. "
                          "Pełna lista: /help. Tematy: /tematy."),
                ("tekst", "Jeśli potrzebujesz prawdziwej rozmowy o kodzie — karta API (klucz, płatność za użycie) albo Subskrypcja (Claude Code).")]

    # ---------------------------------------------------------------- komendy
    def _komenda(self, tekst):
        czesci = tekst[1:].split(maxsplit=1)
        cmd = czesci[0].lower()
        arg = czesci[1].strip() if len(czesci) > 1 else ""
        if cmd == "help":
            return [("naglowek", "Komendy trybu offline"),
                    ("kod", "/temat <nazwa>        wyjaśnienie z przykładami i 3 zadaniami\n"
                            "/tematy               lista tematów z bazy wiedzy\n"
                            "/zadania              3 zadania do ostatniego tematu\n"
                            "/pytania              3 pytania sprawdzające z bieżącego tygodnia\n"
                            "/quiz [tydzień]       quiz w rozmowie (A/B/C/D)\n"
                            "/rekrutacja           15 pytań jak na rozmowie na Junior QA\n"
                            "/sprawdz <plik.py>    recenzja: co dobrze, co błędem, co czytelniej\n"
                            "/uruchom <plik.py> [<< dane; po; średniku]   uruchom i wytłumacz błąd\n"
                            "/blad <NazwaBłędu>    co znaczy np. TypeError i jak go szukać\n"
                            "/coto <pojęcie>       definicja jak dziesięciolatkowi\n"
                            "/debug                program z 3 ukrytymi błędami do ćwiczeń\n"
                            "/rozwiazanie          zdradza ukryte błędy (dopiero gdy się poddasz)\n"
                            "/git                  status repozytorium\n"
                            "/commit [opis]        proponuje i (za zgodą) wykonuje commit\n"
                            "/init                 tworzy CLAUDE.md z zasadami\n"
                            "/plan <projekt>       szkielet PLAN.md\n"
                            "/bugraport            szablon bug raportu\n"
                            "/tryb                 przełącza „pytaj o zgodę” / „auto”\n"
                            "/clear                czyści rozmowę"),
                    ("tekst", "Albo po ludzku: „uczę się pętli”, „przejrzyj @bmi.py”, „utknąłem na zadaniu…”, „zadaj mi 3 pytania”, „co to jest fixture”.")]
        if cmd == "tematy":
            return [("naglowek", "Tematy w bazie wiedzy")] + [("tekst", f"tydz. {t['tydzien']:>2} · {t['nazwa']}   (/temat {t['id']})") for t in P.lekcje]
        if cmd == "temat":
            temat = next((x for x in P.lekcje if x["id"] == arg.lower()), None) or self._temat(arg)
            return self._wyjasnij_temat(temat) if temat else [("ostrz", f"Nie znam tematu „{arg}”. Lista: /tematy")]
        if cmd == "zadania":
            temat = self.ostatni_temat or self._temat(self._tydzien().get("tematy", "")) or (P.lekcje[0] if P.lekcje else None)
            if not temat:
                return [("ostrz", "Ten program nie ma lekcji.")]
            return self._zadania(temat)
        if cmd == "pytania":
            return self._pytania_sprawdzajace(arg)
        if cmd == "odpowiedzi":
            if not self._ostatnie_pytania:
                return [("tekst", "Najpierw poproś o pytania: /pytania albo „zadaj mi 3 pytania”.")]
            return [("naglowek", "Wzorcowe odpowiedzi")] + [("tekst", f"{i}. {p}\n   → {o}") for i, (p, o) in enumerate(self._ostatnie_pytania, 1)]
        if cmd == "quiz":
            return self._quiz_start(arg)
        if cmd == "rekrutacja":
            return self._rekrutacja_start()
        if cmd in ("sprawdz", "sprawdź", "recenzja"):
            return self._recenzja(arg.lstrip("@")) if arg else [("ostrz", "Podaj plik: /sprawdz bmi.py")]
        if cmd == "uruchom":
            if not arg:
                return [("ostrz", "Podaj plik: /uruchom bmi.py  (dane do input() po <<, np. << 1.8; 75)")]
            return self._uruchom(arg.split("<<")[0].strip().lstrip("@"), self._dane_wejsciowe(arg))
        if cmd in ("blad", "błąd"):
            return self._blad(arg)
        if cmd == "coto":
            nazwa, opis = self._pojecie(arg)
            return [("naglowek", nazwa.capitalize()), ("tekst", opis)] if opis else [("ostrz", f"Nie mam „{arg}”. Znam: {', '.join(P.pojecia) or 'nic — ten program nie ma słowniczka'}")]
        if cmd == "debug":
            return self._program_debug()
        if cmd == "rozwiazanie":
            if not self.ukryte:
                return [("tekst", "Nie ma czego zdradzać — najpierw /debug albo „wprowadź do @plik.py ukryty błąd”.")]
            return [("naglowek", "Ukryte błędy")] + [("tekst", f"{p}: {o}") for p, o in self.ukryte.items()]
        if cmd == "git":
            return self._git_status()
        if cmd == "commit":
            return self._commit(arg)
        if cmd == "init":
            return self._init()
        if cmd == "plan":
            return self._plan(arg or "projekt")
        if cmd == "bugraport":
            return [("naglowek", "Szablon bug raportu"), ("kod", P.szablony.get("bug_raport", "(ten program nie ma szablonu bug raportu)"))]
        if cmd == "tryb":
            k = self._k()
            k["przelacz_tryb"]()
            return [("tekst", f"Tryb: {'pytam o zgodę przed każdą akcją' if self._k().get('tryb_zgody') else 'auto — wykonuję bez pytania (na czas nauki lepiej „pytaj”)'}.")]
        return [("ostrz", f"Nieznana komenda /{cmd}. Lista: /help")]

    # ---------------------------------------------------------------- tematy
    def _wyjasnij_temat(self, temat):
        self.ostatni_temat = temat
        out = [("naglowek", f"{temat['nazwa']}  (tydzień {temat['tydzien']})"), ("tekst", temat["wyjasnienie"]),
               ("tekst", "Przykład:"), ("kod", temat["przyklad"])]
        if temat.get("pulapki"):
            out.append(("ostrz", "Pułapki: " + " ".join(temat["pulapki"])))
        out += self._zadania(temat)
        return out

    def _zadania(self, temat):
        self.ostatni_temat = temat
        out = [("naglowek", "3 zadania — bez rozwiązań, 15 minut własnej walki przed pytaniem")]
        for i, z in enumerate(temat["zadania"], 1):
            out.append(("tekst", f"{i}. {z}"))
        out.append(("pytanie", "Gdy skończysz: „przejrzyj @nazwa_pliku.py” — zrobię recenzję. Gdy utkniesz: „utknąłem … błąd: …”."))
        return out

    def _pytania_sprawdzajace(self, tekst):
        temat = self._temat(tekst) if tekst else None
        if not temat:
            temat = self.ostatni_temat
        pula = [temat] if temat else P.lekcje_tygodnia(self._tydzien()["tydzien"]) or P.lekcje[:1]
        if not pula:
            return [("ostrz", "Ten program nie ma lekcji z pytaniami.")]
        pytania = []
        for x in pula:
            pytania += x["pytania"]
        wybrane = random.sample(pytania, min(3, len(pytania)))
        out = [("naglowek", f"3 pytania sprawdzające — {', '.join(x['nazwa'] for x in pula)}")]
        for i, (p, _) in enumerate(wybrane, 1):
            out.append(("tekst", f"{i}. {p}"))
        out.append(("pytanie", "Odpowiedz na głos albo w notatkach, potem wpisz /odpowiedzi — pokażę wzorcowe."))
        self._ostatnie_pytania = wybrane
        return out

    def _dlaczego(self, tekst):
        temat = self._temat(tekst) or self.ostatni_temat
        if temat:
            return [("tekst", f"„Dlaczego” to dobre pytanie — ale offline nie mam odpowiedzi na dowolne „dlaczego”. Mam wyjaśnienie tematu "
                              f"„{temat['nazwa']}” i jego pułapki:"), ("tekst", temat["wyjasnienie"]),
                    ("ostrz", "Pułapki: " + " ".join(temat.get("pulapki", []))),
                    ("pytanie", "Jeśli po tym nadal nie jest oczywiste — zapisz pytanie w Dzienniku; w trybie API lub Claude Code zadasz je modelowi.")]
        return [("tekst", "Nie wiem, o który temat chodzi. Napisz np. „dlaczego input zwraca napis” — dopasuję temat.")]

    # ---------------------------------------------------------------- pliki
    def _znajdz(self, nazwa):
        p = znajdz_plik(self._projekt(), Path(nazwa).name)
        if not p:
            if not self._projekt():
                return None, [("ostrz", "Nie wskazano katalogu projektu — zakładka Mój projekt → Wybierz katalog.")]
            return None, [("ostrz", f"Nie znalazłem pliku {nazwa} w {self._projekt()}.")]
        return p, []

    def _recenzja(self, nazwa):
        p, blad = self._znajdz(nazwa)
        if not p:
            return blad
        try:
            zrodlo = p.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as e:
            return [("ostrz", f"Nie mogę przeczytać {p.name}: {e}")]
        if not p.suffix == ".py":
            return [("tekst", f"{p.name} ma {len(zrodlo.splitlines())} linii. Recenzję kodu robię tylko dla .py; dla Markdown sprawdź: "
                              "czy jest tytuł, „co robi”, „jak uruchomić”, przykład wyniku.")]
        w = analizuj_kod(zrodlo, p.name)
        out = [("naglowek", f"Recenzja {p.name} ({len(zrodlo.splitlines())} linii) — bez przepisywania")]
        out.append(("ok", "Co jest dobrze:"))
        out += [("tekst", "  • " + x) for x in w["dobrze"]]
        out.append(("ostrz", "Co jest błędem lub ryzykiem:" if w["bledy"] else "Błędów statycznych nie widzę (to nie znaczy, że ich nie ma — uruchom i przetestuj)."))
        out += [("tekst", "  • " + x) for x in w["bledy"]]
        if w["czytelniej"]:
            out.append(("tekst", "Co można napisać czytelniej:"))
            out += [("tekst", "  • " + x) for x in w["czytelniej"]]
        out.append(("pytanie", w["pytanie"]))
        return out

    def _dane_wejsciowe(self, tekst):
        if "<<" in tekst:
            return "\n".join(x.strip() for x in tekst.split("<<", 1)[1].split(";")) + "\n"
        return ""

    def _uruchom(self, nazwa, dane=""):
        p, blad = self._znajdz(nazwa)
        if not p:
            return blad

        def wykonaj():
            kod, out, err = uruchom_plik(p, dane)
            wynik = [("naglowek", f"python {p.name}" + (" (z danymi do input)" if dane else ""))]
            if out.strip():
                wynik.append(("kod", out.rstrip()[-3000:]))
            if kod == 0:
                wynik.append(("ok", "Zakończono bez błędu (kod 0)."))
                wynik.append(("pytanie", "Czy wynik jest taki, jak przewidywałeś PRZED uruchomieniem? Jeśli nie — która linia zmieniła dane inaczej, niż myślałeś?"))
                return wynik
            tb = wyjasnij_traceback(err)
            wynik.append(("kod", err.rstrip()[-2500:]))
            if tb:
                wynik.append(("ostrz", f"{tb['typ']}" + (f" w linii {tb['linia']}" if tb["linia"] else "") + f": {tb['co']}"))
                wynik.append(("pytanie", tb["pytanie"]))
            return wynik

        return self._potwierdzenie(f"uruchomić  python {p.name}  w {p.parent}" + (" z danymi do input()" if dane else ""), wykonaj)

    def _utknalem(self, tekst, pliki):
        out = []
        typ = None
        for nazwa in _bledy():
            if nazwa.lower() in tekst.lower():
                typ = nazwa
                break
        if typ:
            out += [("ostrz", f"{typ}: {_bledy()[typ]['co']}"), ("pytanie", _bledy()[typ]["pytanie"])]
        if pliki:
            p, blad = self._znajdz(pliki[0])
            if p and p.suffix == ".py":
                w = analizuj_kod(p.read_text(encoding="utf-8"), p.name)
                if w["bledy"]:
                    out.append(("tekst", f"W {p.name} widzę statycznie:"))
                    out += [("tekst", "  • " + x) for x in w["bledy"][:3]]
                out.append(("tekst", f"Mogę też uruchomić plik i przeczytać prawdziwy traceback: „uruchom @{p.name}”."))
            else:
                out += blad
        if not out:
            out = [("tekst", "Nie widzę nazwy błędu ani pliku. Wklej ostatnią linię tracebacku (np. „TypeError: …”) i podaj plik przez @nazwa.py."),
                   ("pytanie", "Zanim to zrobisz: która linia wykonała się jako ostatnia przed błędem i jakie wartości miały tam zmienne?")]
        out.append(("tekst", "Nie poprawiam kodu — odpowiedz sobie na pytanie wyżej, popraw, uruchom ponownie."))
        return out

    def _blad(self, nazwa):
        n = nazwa.strip()
        B = _bledy()
        klucz = next((k for k in B if k.lower() == n.lower() or k.lower().startswith(n.lower())), None) if n else None
        if not klucz:
            return [("ostrz", f"Nie mam „{n}”. Znam: {', '.join(B)}")]
        return [("naglowek", klucz), ("tekst", B[klucz]["co"]), ("pytanie", B[klucz]["pytanie"])]

    def _sprawdz_rozumienie(self, tekst, pliki):
        out = [("tekst", "Offline nie potrafię ocenić, czy Twój opis jest poprawny — mogę za to pokazać, z czego plik naprawdę się składa, "
                         "żebyś sam porównał z tym, co powiedziałeś.")]
        if pliki:
            p, blad = self._znajdz(pliki[0])
            if p and p.suffix == ".py":
                try:
                    drzewo = ast.parse(p.read_text(encoding="utf-8"))
                except SyntaxError as e:
                    return out + [("ostrz", f"Plik ma błąd składni w linii {e.lineno} — najpierw to.")]
                el = []
                for n in drzewo.body:
                    if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        el.append(f"funkcja {n.name}({', '.join(a.arg for a in n.args.args)}) — {ast.get_docstring(n) or 'BEZ docstringa'}")
                    elif isinstance(n, ast.ClassDef):
                        el.append(f"klasa {n.name}")
                    elif isinstance(n, (ast.For, ast.While)):
                        el.append(f"pętla {'for' if isinstance(n, ast.For) else 'while'} w linii {n.lineno}")
                    elif isinstance(n, ast.If):
                        el.append(f"warunek if w linii {n.lineno}")
                    elif isinstance(n, (ast.Import, ast.ImportFrom)):
                        el.append("import " + ", ".join(a.name for a in n.names))
                out.append(("naglowek", f"Z czego składa się {p.name}"))
                out += [("tekst", "  • " + x) for x in el] or [("tekst", "  • same instrukcje na najwyższym poziomie, bez funkcji")]
            else:
                out += blad
        out.append(("pytanie", "Dla każdego elementu z listy powiedz jednym zdaniem: co wchodzi, co wychodzi, kiedy się wykona. "
                               "Element, przy którym się zawahasz, to ten, którego jeszcze nie rozumiesz — zapytaj o niego „dlaczego”."))
        return out

    # ---------------------------------------------------------------- ukryte błędy
    def _ukryty_blad(self, nazwa):
        p, blad = self._znajdz(nazwa)
        if not p:
            return blad
        if p.suffix != ".py":
            return [("ostrz", "Ukryty błąd wprowadzam tylko do plików .py.")]
        cel = p.with_name(p.stem + "_z_bledem.py")

        def wykonaj():
            nowy, opis = wprowadz_ukryty_blad(p.read_text(encoding="utf-8"))
            if not nowy:
                return [("ostrz", opis)]
            cel.write_text(nowy, encoding="utf-8")
            self.ukryte[cel.name] = opis
            return [("ok", f"Zapisałem {cel.name} z jednym ukrytym błędem. Oryginał nietknięty."),
                    ("pytanie", f"Napisz testy do {cel.name} tak, żeby jeden z nich był czerwony. Gdy się poddasz: /rozwiazanie.")]

        return self._potwierdzenie(f"zapisać kopię {p.name} jako {cel.name} z jednym ukrytym błędem (oryginału nie ruszam)", wykonaj)

    def _program_debug(self):
        projekt = self._projekt()
        if not projekt:
            return [("ostrz", "Najpierw wskaż katalog projektu (Mój projekt)."), ("kod", PROGRAM_DEBUG)]
        cel = Path(projekt) / "cwiczenie_debug.py"

        def wykonaj():
            cel.write_text(PROGRAM_DEBUG, encoding="utf-8")
            self.ukryte[cel.name] = " | ".join(BLEDY_DEBUG)
            return [("ok", f"Zapisałem {cel.name} ({len(PROGRAM_DEBUG.splitlines())} linii, 3 ukryte błędy logiczne — program się uruchamia, ale liczy źle)."),
                    ("pytanie", "Uruchom go, przewiduj wynik PRZED uruchomieniem, postaw breakpoint w PyCharm w każdej funkcji. Gdy znajdziesz wszystkie: /rozwiazanie.")]

        return self._potwierdzenie(f"zapisać {cel.name} w katalogu projektu", wykonaj)

    # ---------------------------------------------------------------- quiz
    def _quiz_start(self, tekst):
        m = re.search(r"\d+", tekst or "")
        tydz = int(m.group(0)) if m else None
        if tydz is None:
            temat = self._temat(tekst or "")
            tydz = temat["tydzien"] if temat else self._tydzien()["tydzien"]
        pyt = P.quiz_tygodnia(tydz)[:]
        if not pyt:
            return [("ostrz", f"Nie mam quizu dla tygodnia {tydz}. Dostępne: {', '.join(P.quizy) or 'brak'}")]
        random.shuffle(pyt)
        self.quiz = {"tydzien": tydz, "pytania": pyt, "i": 0, "wynik": 0}
        return [("naglowek", f"Quiz z tygodnia {tydz} — {len(pyt)} pytań, odpowiadaj literą A–D")] + self._quiz_pytanie()

    def _quiz_pytanie(self):
        q = self.quiz
        p = q["pytania"][q["i"]]
        out = [("tekst", f"{q['i'] + 1}/{len(q['pytania'])}  {p['p']}")]
        for lit, o in zip("ABCD", p["o"]):
            out.append(("tekst", f"   {lit}) {o}"))
        return out

    def _quiz_odpowiedz(self, t):
        q = self.quiz
        if t in ("/stop", "stop", "koniec", "przerwij"):
            self.quiz = None
            return [("tekst", "Quiz przerwany.")]
        if t not in ("a", "b", "c", "d"):
            return [("ostrz", "Odpowiedz literą A, B, C lub D (albo „stop”).")]
        p = q["pytania"][q["i"]]
        idx = "abcd".index(t)
        if idx == p["odp"]:
            q["wynik"] += 1
            out = [("ok", "Dobrze. " + p["w"])]
        else:
            out = [("ostrz", f"Nie. Poprawna: {'ABCD'[p['odp']]}) {p['o'][p['odp']]}. {p['w']}")]
        q["i"] += 1
        if q["i"] < len(q["pytania"]):
            return out + self._quiz_pytanie()
        n = len(q["pytania"])
        proc = int(100 * q["wynik"] / n)
        self.quiz = None
        kom = "Bezbłędnie." if proc == 100 else ("Solidnie — wróć do pytań, które poszły źle." if proc >= 60 else "Za nisko, żeby iść dalej spokojnie — /temat i jeszcze raz.")
        k = self._k()
        if k.get("zapisz_quiz"):
            k["zapisz_quiz"](q["tydzien"], q["wynik"], n)
        return out + [("naglowek", f"Wynik: {q['wynik']}/{n} ({proc}%). {kom}")]

    # ---------------------------------------------------------------- rekrutacja
    def _rekrutacja_start(self):
        pyt = [tuple(x) for x in P.pytania_rekrutacyjne]
        if not pyt:
            return [("ostrz", "Ten program nie ma pytań rekrutacyjnych.")]
        random.shuffle(pyt)
        self.rekrutacja = {"pytania": pyt, "i": 0}
        return [("naglowek", "Próbna rozmowa rekrutacyjna — Junior QA"),
                ("tekst", "Odpowiadaj pełnym zdaniem, jak na rozmowie. Po każdej odpowiedzi pokażę wzorzec — porównaj sam, czego zabrakło. "
                          "„stop” kończy."),
                ("pytanie", f"[{pyt[0][0]}] {pyt[0][1]}")]

    def _rekrutacja_odpowiedz(self, tekst):
        r = self.rekrutacja
        if tekst.lower() in ("stop", "/stop", "koniec"):
            self.rekrutacja = None
            return [("tekst", f"Koniec rozmowy po {r['i']} pytaniach. Zapisz w Dzienniku, które poszły najgorzej.")]
        kat, p, wzor = r["pytania"][r["i"]]
        out = [("ok", "Wzorcowa odpowiedź: " + wzor)]
        if len(tekst.split()) < 8:
            out.append(("ostrz", "Twoja odpowiedź ma mniej niż 8 słów — na rozmowie rozwiń: przykład z projektu + dlaczego."))
        r["i"] += 1
        if r["i"] >= len(r["pytania"]):
            self.rekrutacja = None
            return out + [("naglowek", "To było ostatnie pytanie. Które 3 odpowiedzi wymagają pracy? Wpisz je do Dziennika.")]
        kat, p, _ = r["pytania"][r["i"]]
        return out + [("pytanie", f"[{kat}] {p}")]

    # ---------------------------------------------------------------- git
    def _git(self, *args):
        projekt = self._projekt()
        if not projekt:
            return None
        try:
            r = subprocess.run(["git", *args], cwd=projekt, capture_output=True, text=True, timeout=20, **_flagi())
            return r
        except (OSError, subprocess.SubprocessError):
            return None

    def _git_status(self):
        if not self._projekt():
            return [("ostrz", "Najpierw wskaż katalog projektu.")]
        r = self._git("status", "--short", "--branch")
        if r is None or r.returncode != 0:
            return [("ostrz", "To nie jest repozytorium Git albo git nie jest w PATH. Zadanie 4 z tygodnia 0: „git init”. Jak to zrobić: /temat git")]
        log = self._git("log", "--oneline", "-5")
        return [("naglowek", "git status"), ("kod", r.stdout.strip() or "(czysto)"),
                ("tekst", "Ostatnie commity:"), ("kod", log.stdout.strip() if log and log.stdout.strip() else "(brak commitów)")]

    def _commit(self, opis=""):
        if not self._projekt():
            return [("ostrz", "Najpierw wskaż katalog projektu.")]
        r = self._git("status", "--porcelain")
        if r is None or r.returncode != 0:
            return [("ostrz", "To nie jest repozytorium Git. /temat git")]
        zmiany = [l for l in r.stdout.splitlines() if l.strip()]
        if not zmiany:
            return [("tekst", "Nie ma zmian do zacommitowania — drzewo czyste. Zrób coś, potem wróć.")]
        pliki = [l[3:].strip() for l in zmiany]
        k = self._k()
        if not opis:
            opis = f"dzień {k.get('dni', 0) + 1}: {self._tydzien()['tytul'].lower()} — {', '.join(Path(p).name for p in pliki[:3])}"
        out = [("naglowek", f"Zmiany ({len(zmiany)}):"), ("kod", "\n".join(zmiany[:20]))]
        out.append(("tekst", f"Proponowana treść commita: „{opis}”. Lepsza jest Twoja — z nazwą tematu, nie plików: /commit \"dzień 7: słowniki\"."))

        def wykonaj():
            a = self._git("add", ".")
            c = self._git("commit", "-m", opis)
            if c is None or c.returncode != 0:
                return [("ostrz", "Commit się nie udał:"), ("kod", (c.stderr if c else "") or (a.stderr if a else "brak gita"))]
            return [("ok", "Commit zapisany:"), ("kod", c.stdout.strip()),
                    ("tekst", "Teraz git push — w terminalu albo /commit nie robi pusha celowo: zobacz sam, co się wysyła.")]

        return out + self._potwierdzenie(f"wykonać  git add .  oraz  git commit -m \"{opis}\"", wykonaj)

    def _init(self):
        projekt = self._projekt()
        if not projekt:
            return [("ostrz", "Najpierw wskaż katalog projektu.")]
        cel = Path(projekt) / "CLAUDE.md"
        if cel.exists():
            return [("tekst", "CLAUDE.md już istnieje:"), ("kod", cel.read_text(encoding="utf-8")[:1500])]

        def wykonaj():
            cel.write_text(P.claude_md, encoding="utf-8")
            return [("ok", f"Utworzyłem {cel}"), ("kod", P.claude_md)]

        return self._potwierdzenie(f"utworzyć {cel} z zasadami nauki", wykonaj)

    def _plan(self, tekst):
        nazwa = re.sub(r"^(chcę zbudować|chce zbudowac|/plan)\s*", "", tekst, flags=re.I).strip(" .") or "projekt"
        szablon = (f"# PLAN: {nazwa}\n\n## Cel (jedno zdanie)\n[co użytkownik może zrobić, gdy skończysz]\n\n"
                   "## Zakres\n- wchodzi: ...\n- NIE wchodzi (świadomie): ...\n\n## Struktura plików\n"
                   "- main.py — uruchomienie i menu\n- [logika].py — funkcje/klasy bez input/print\n- [dane].py — zapis/odczyt (CSV/SQLite)\n"
                   "- test_[logika].py — testy pytest\n- README.md\n\n## Kolejność kroków\n1. dane: struktura + zapis/odczyt + test\n"
                   "2. logika: jedna funkcja naraz + test\n3. interfejs (menu/Flask)\n4. README, CI\n\n## Ryzyka\n- ...\n")
        return [("tekst", f"Tryb planowania (offline): nie znam Twojego projektu, więc daję szkielet. Wypełnij nawiasy, zanim napiszesz linię kodu."),
                ("kod", szablon),
                ("pytanie", "Który krok z „Kolejności” zrobisz pierwszy i jak sprawdzisz, że działa, ZANIM przejdziesz do drugiego? Ty decydujesz.")]


# ===========================================================================
# Klient Anthropic API
# ===========================================================================
class KlientAPI:
    URL = "https://api.anthropic.com/v1/messages"
    MODEL_DOMYSLNY = "claude-sonnet-5-5"

    def __init__(self, klucz, model=None, kontekst=None):
        self.klucz = klucz.strip()
        self.model = (model or self.MODEL_DOMYSLNY).strip()
        self.kontekst = kontekst or (lambda: {})
        self.historia = []

    def wyczysc(self):
        self.historia = []

    def _system(self):
        k = self.kontekst()
        tydz = P.tydzien(k.get("tydzien", 0))
        return (P.claude_md + "\n\n# Kontekst ucznia\n"
                f"- Imię: {k.get('imie') or 'uczeń'}.\n"
                f"- Program: {P.nazwa} ({P.liczba_tygodni()} tygodni). Bieżący tydzień {tydz['tydzien']}: {tydz['tytul']}. Tematy: {tydz.get('tematy', '')}.\n"
                f"- Rola asystenta w tym etapie: {tydz.get('rola_asystenta', '')}\n"
                "- Odpowiadaj po polsku, zwięźle. Kod pokazuj tylko, gdy uczeń o to poprosi lub gdy etap na to pozwala. "
                "Zamiast rozwiązania zadawaj pytanie naprowadzające. Jeśli uczeń napisze „zatrzymaj się” — cofnij się do pierwszego kroku.\n"
                "- Gdy w wiadomości jest treść pliku, odnoś się do konkretnych linii.")

    def _dolacz_pliki(self, tekst):
        k = self.kontekst()
        projekt = k.get("projekt") or ""
        dodatki = []
        for nazwa in pliki_z_tekstu(tekst):
            p = znajdz_plik(projekt, Path(nazwa).name)
            if p and p.is_file():
                try:
                    tresc = p.read_text(encoding="utf-8")[:20000]
                    dodatki.append(f"\n\n--- Zawartość pliku {p.name} ---\n```\n{tresc}\n```")
                except (OSError, UnicodeDecodeError):
                    dodatki.append(f"\n\n(nie udało się odczytać {nazwa})")
            else:
                dodatki.append(f"\n\n(pliku {nazwa} nie ma w katalogu projektu)")
        return tekst + "".join(dodatki)

    def wyslij(self, tekst):
        """Blokująco: wysyła wiadomość, zwraca tekst odpowiedzi lub rzuca RuntimeError z czytelnym opisem."""
        if not self.klucz:
            raise RuntimeError("Brak klucza API. Wpisz go w karcie API (Ustawienia → Asystent).")
        tresc = self._dolacz_pliki(tekst)
        wiadomosci = self.historia + [{"role": "user", "content": tresc}]
        dane = {"model": self.model, "max_tokens": 1500, "system": self._system(), "messages": wiadomosci[-20:]}
        req = urllib.request.Request(self.URL, data=json.dumps(dane).encode("utf-8"), method="POST",
                                     headers={"content-type": "application/json", "x-api-key": self.klucz,
                                              "anthropic-version": "2023-06-01"})
        try:
            with urllib.request.urlopen(req, timeout=120) as odp:
                body = json.loads(odp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            try:
                szczegoly = json.loads(e.read().decode("utf-8")).get("error", {}).get("message", "")
            except Exception:
                szczegoly = ""
            opisy = {401: "zły lub nieaktywny klucz API", 403: "klucz nie ma uprawnień", 404: f"model „{self.model}” nie istnieje — zmień nazwę modelu",
                     429: "limit zapytań lub brak środków na koncie", 529: "API przeciążone — spróbuj za chwilę"}
            raise RuntimeError(f"API odpowiedziało {e.code}: {opisy.get(e.code, 'błąd')}. {szczegoly}".strip())
        except urllib.error.URLError as e:
            raise RuntimeError(f"Brak połączenia z API ({e.reason}). Sprawdź internet.")
        except (TimeoutError, OSError) as e:
            raise RuntimeError(f"Błąd połączenia: {e}")
        czesci = [c.get("text", "") for c in body.get("content", []) if c.get("type") == "text"]
        odpowiedz = "\n".join(czesci).strip() or "(pusta odpowiedź)"
        self.historia = wiadomosci + [{"role": "assistant", "content": odpowiedz}]
        uz = body.get("usage", {})
        self.ostatnie_uzycie = (uz.get("input_tokens", 0), uz.get("output_tokens", 0))
        return odpowiedz
