# -*- coding: utf-8 -*-
# Wspólny początek plików WERYFIKATORY/test_tNN.py (zbuduj.py wkleja go na górę każdego testu — test musi działać jako jeden plik).
import importlib.util
import os
import re
import sys
import unicodedata
from pathlib import Path

import pytest

WS = Path(os.environ.get("MENTOR_WORKSPACE") or ".").resolve()


def plik(nazwa):
    p = WS / nazwa
    assert p.exists(), f"Brak pliku {nazwa} w katalogu roboczym {WS}"
    return p


def tekst(nazwa):
    return plik(nazwa).read_text(encoding="utf-8", errors="replace")


def modul(nazwa):
    """Importuje plik ucznia <nazwa>.py z katalogu roboczego (świeżo, bez pamięci podręcznej)."""
    p = WS / f"{nazwa}.py"
    assert p.exists(), f"Brak pliku {nazwa}.py w katalogu roboczym {WS}"
    if str(WS) not in sys.path:
        sys.path.insert(0, str(WS))
    spec = importlib.util.spec_from_file_location(f"uczen_{nazwa}", p)
    m = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = m          # Flask i inne biblioteki szukają katalogu modułu po nazwie (szablony templates/)
    try:
        spec.loader.exec_module(m)
    except (OSError, EOFError) as e:
        if "stdin" in str(e) or isinstance(e, EOFError):
            pytest.fail(f"{nazwa}.py wywołuje input() przy imporcie — przenieś input() do bloku if __name__ == \"__main__\":")
        raise
    return m


def funkcja(m, nazwa):
    assert hasattr(m, nazwa) and callable(getattr(m, nazwa)), f"Brak funkcji {nazwa}"
    return getattr(m, nazwa)


def norm(s):
    s = unicodedata.normalize("NFKD", str(s)).casefold().replace("ł", "l")
    return "".join(c for c in s if not unicodedata.combining(c))


def sekcje_md(t):
    """{nagłówek_znormalizowany: [linie treści]} dla nagłówków ## w Markdown."""
    wynik, biez = {}, None
    for linia in t.splitlines():
        m = re.match(r"^\s*##\s+(.+?)\s*$", linia)
        if m:
            biez = norm(m.group(1)).strip(" :")
            wynik[biez] = []
        elif biez is not None and linia.strip():
            wynik[biez].append(linia.strip())
    return wynik


def ok(wynik, oczekiwany, opis):
    liczba = lambda x: isinstance(x, (int, float)) and not isinstance(x, bool)
    if liczba(oczekiwany):
        assert liczba(wynik) and abs(float(wynik) - float(oczekiwany)) < 0.005, f"{opis}: oczekiwano {oczekiwany}, otrzymano {wynik!r}"
    else:
        assert wynik == oczekiwany, f"{opis}: oczekiwano {oczekiwany!r}, otrzymano {wynik!r}"


def rzuca(f, *a, wyjatek=ValueError, opis="", **k):
    try:
        w = f(*a, **k)
    except wyjatek:
        return
    except Exception as e:  # noqa: BLE001
        pytest.fail(f"{opis}: oczekiwano {_nazwa_wyjatku(wyjatek)}, a funkcja rzuciła {type(e).__name__}: {e}")
    pytest.fail(f"{opis}: oczekiwano {_nazwa_wyjatku(wyjatek)}, a funkcja zwróciła {w!r}")


def _nazwa_wyjatku(w):
    return " albo ".join(x.__name__ for x in w) if isinstance(w, tuple) else w.__name__


def git(*args):
    """Uruchamia git w katalogu roboczym; zwraca (kod, wyjście). Brak gita → czytelny błąd testu."""
    import shutil
    import subprocess
    if not shutil.which("git"):
        pytest.fail("Nie znaleziono programu git — zainstaluj Git for Windows (lekcja „Narzędzia”) i uruchom Mentora ponownie")
    p = subprocess.run(["git", "-C", str(WS), *args], capture_output=True, text=True, encoding="utf-8", errors="replace")
    return p.returncode, (p.stdout + p.stderr).strip()


def repo():
    assert (WS / ".git").exists(), f"W katalogu roboczym {WS} nie ma repozytorium Git — wpisz git init (lekcja „Git i GitHub — pierwszy commit”)"


def uruchom(nazwa, stdin="", limit=15, env=None):
    """Uruchamia program ucznia <nazwa> (plik w katalogu roboczym) z danymi dla input(); zwraca (kod_wyjścia, wyjście+błędy)."""
    import subprocess
    p = plik(nazwa)
    e = dict(os.environ, PYTHONIOENCODING="utf-8", **(env or {}))
    try:
        w = subprocess.run([sys.executable, "-X", "utf8", str(p)], input=stdin, capture_output=True, text=True, encoding="utf-8",
                           errors="replace", cwd=str(WS), timeout=limit, env=e)
    except subprocess.TimeoutExpired:
        pytest.fail(f"{nazwa} nie zakończył się w {limit} s dla danych {stdin!r} — pętla nieskończona albo program czeka na więcej danych")
    return w.returncode, w.stdout + w.stderr


def zawiera(wyjscie, *fragmenty, dane=""):
    """Każdy fragment (bez wielkości liter i ogonków) musi wystąpić w wyjściu programu."""
    n = norm(wyjscie)
    for f in fragmenty:
        assert norm(f) in n, f"dla danych {dane!r} w wyjściu brakuje „{f}”. Wyjście programu:\n{wyjscie[-800:]}"


def bez_bledu(kod, wyjscie, dane=""):
    assert kod == 0 and "Traceback" not in wyjscie, f"program zakończył się błędem dla danych {dane!r}:\n{wyjscie[-800:]}"


def drzewo(nazwa):
    """Drzewo składni (ast) pliku ucznia — do sprawdzania budowy kodu bez uruchamiania (np. skrypty Selenium)."""
    import ast
    return ast.parse(tekst(nazwa))


def wywolania(nazwa):
    """Lista nazw wywoływanych funkcji/metod w pliku ucznia (np. ['get', 'find_element', 'quit'])."""
    import ast
    out = []
    for w in ast.walk(drzewo(nazwa)):
        if isinstance(w, ast.Call):
            f = w.func
            out.append(f.attr if isinstance(f, ast.Attribute) else getattr(f, "id", ""))
    return out


def pytest_ucznia(katalog, *args, limit=120):
    """Uruchamia pytest w podanym katalogu (np. testy ucznia z modułem wzorcowym albo mutantem); zwraca (kod, wyjście)."""
    import subprocess
    w = subprocess.run([sys.executable, "-X", "utf8", "-m", "pytest", "-q", "-p", "no:cacheprovider", "-o", "addopts=", *args], cwd=str(katalog),
                       capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=limit,
                       env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1"))
    return w.returncode, w.stdout + w.stderr


def mutanty(test_plik, modul, wzorzec, zmiany, min_testow=1):
    """Testy ucznia (test_plik) muszą przejść na poprawnym module (wzorzec — tekst kodu) i paść na KAŻDYM mutancie
    (zmiany: [(opis, stary_fragment, nowy_fragment)]). Testy uruchamiane w osobnym katalogu tymczasowym."""
    import re as _re
    import shutil
    import tempfile
    zrodlo = tekst(test_plik)
    with tempfile.TemporaryDirectory(prefix="mut_") as td:
        td = Path(td)
        (td / test_plik).write_text(zrodlo, encoding="utf-8")
        (td / f"{modul}.py").write_text(wzorzec, encoding="utf-8")
        kod, out = pytest_ucznia(td, test_plik)
        assert kod == 0, f"{test_plik}: testy nie przechodzą na POPRAWNYM module {modul}.py (wzorcowym) — sprawdź oczekiwane wartości:\n{out[-1500:]}"
        m = _re.search(r"(\d+) passed", out)
        n = int(m.group(1)) if m else 0
        assert n >= min_testow, f"{test_plik}: {n} testów — potrzeba co najmniej {min_testow}"
        for opis, stary, nowy in zmiany:
            assert stary in wzorzec, f"(błąd weryfikatora) brak fragmentu {stary!r}"
            (td / f"{modul}.py").write_text(wzorzec.replace(stary, nowy, 1), encoding="utf-8")
            shutil.rmtree(td / "__pycache__", ignore_errors=True)
            kod, out = pytest_ucznia(td, test_plik)
            assert kod != 0, f"{test_plik}: testy NIE wykryły błędu: {opis}. Dopisz przypadek, który go łapie (wartości brzegowe, przypadki negatywne)."


WZORZEC = {'funkcje.py': 'def pole_prostokata(a, b):\n    """Zwraca pole prostokąta o bokach a i b."""\n    return a * b\n\n\ndef czy_parzysta(n):\n    """True, gdy liczba całkowita n jest parzysta."""\n    return n % 2 == 0\n\n\ndef maksimum(lista):\n    """Największy element listy (bez max()); pusta lista → ValueError."""\n    if not lista:\n        raise ValueError("lista jest pusta")\n    najwieksza = lista[0]\n    for x in lista:\n        if x > najwieksza:\n            najwieksza = x\n    return najwieksza\n\n\ndef odwroc(napis):\n    """Zwraca napis od tyłu."""\n    return napis[::-1]\n\n\ndef silnia(n):\n    """n! dla n ≥ 0; liczba ujemna → ValueError."""\n    if n < 0:\n        raise ValueError("silnia liczby ujemnej nie istnieje")\n    wynik = 1\n    for i in range(2, n + 1):\n        wynik *= i\n    return wynik\n\n\nif __name__ == "__main__":\n    print(pole_prostokata(3, 4), czy_parzysta(7), maksimum([3, 9, 2]), odwroc("kot"), silnia(5))\n', 'bmi.py': '"""Kalkulator BMI: wskaźnik masy ciała i kategoria (progi WHO: 18.5, 25, 30)."""\n\nPROG_NIEDOWAGI = 18.5\nPROG_NADWAGI = 25\nPROG_OTYLOSCI = 30\n\n\ndef oblicz_bmi(waga, wzrost):\n    """Zwraca BMI zaokrąglone do 1 miejsca; waga w kg, wzrost w metrach.\n\n    Wartości ≤ 0 albo wzrost > 3 (podany w centymetrach) → ValueError.\n    """\n    if waga <= 0 or wzrost <= 0:\n        raise ValueError("waga i wzrost muszą być większe od zera")\n    if wzrost > 3:\n        raise ValueError("podaj wzrost w metrach, np. 1.75")\n    return round(waga / wzrost ** 2, 1)\n\n\ndef kategoria(bmi):\n    """Zwraca kategorię BMI: niedowaga, norma, nadwaga albo otyłość."""\n    if bmi < PROG_NIEDOWAGI:\n        return "niedowaga"\n    if bmi < PROG_NADWAGI:\n        return "norma"\n    if bmi < PROG_OTYLOSCI:\n        return "nadwaga"\n    return "otyłość"\n\n\nif __name__ == "__main__":\n    wzrost = float(input("Wzrost w metrach: ").replace(",", "."))\n    waga = float(input("Waga w kg: ").replace(",", "."))\n    try:\n        bmi = oblicz_bmi(waga, wzrost)\n    except ValueError as e:\n        if wzrost > 3:\n            print("Uwaga: wzrost podaj w metrach, nie w centymetrach")\n        else:\n            print("Podaj wartości większe od zera")\n    else:\n        print(f"BMI: {bmi:.1f} — {kategoria(bmi)}")\n', 'zadania.py': '"""Logika menedżera zadań — bez input() i print()."""\n\n\ndef dodaj(zadania, tytul):\n    tytul = tytul.strip()\n    if not tytul:\n        raise ValueError("tytuł nie może być pusty")\n    zadania.append({"tytul": tytul, "zrobione": False})\n\n\ndef _sprawdz(zadania, nr):\n    if not 1 <= nr <= len(zadania):\n        raise ValueError(f"nie ma zadania nr {nr}")\n\n\ndef oznacz(zadania, nr):\n    _sprawdz(zadania, nr)\n    zadania[nr - 1]["zrobione"] = True\n\n\ndef usun(zadania, nr):\n    _sprawdz(zadania, nr)\n    return zadania.pop(nr - 1)["tytul"]\n\n\ndef otwarte(zadania):\n    return [z["tytul"] for z in zadania if not z["zrobione"]]\n', 'magazyn_csv.py': 'import csv\n\nPOLA = ["id", "nazwa", "kategoria", "cena", "ilosc"]\n\n\ndef wczytaj(sciezka):\n    """Produkty z CSV (id, ilosc → int; cena → float)."""\n    with open(sciezka, encoding="utf-8", newline="") as f:\n        wiersze = list(csv.DictReader(f))\n    return [{"id": int(w["id"]), "nazwa": w["nazwa"], "kategoria": w["kategoria"], "cena": float(w["cena"]), "ilosc": int(w["ilosc"])} for w in wiersze]\n\n\ndef zapisz(produkty, sciezka):\n    with open(sciezka, "w", encoding="utf-8", newline="") as f:\n        w = csv.DictWriter(f, fieldnames=POLA)\n        w.writeheader()\n        w.writerows(produkty)\n\n\ndef dodaj(produkty, nazwa, kategoria, cena, ilosc):\n    """Dodaje produkt z walidacją: niepusta, unikalna nazwa (bez wielkości liter), cena ≥ 0, ilość całkowita ≥ 0."""\n    nazwa = nazwa.strip()\n    if not nazwa:\n        raise ValueError("nazwa nie może być pusta")\n    if any(p["nazwa"].lower() == nazwa.lower() for p in produkty):\n        raise ValueError(f"produkt {nazwa} już istnieje")\n    if cena < 0:\n        raise ValueError("cena nie może być ujemna")\n    if not isinstance(ilosc, int) or ilosc < 0:\n        raise ValueError("ilość musi być liczbą całkowitą ≥ 0")\n    nowy = {"id": max((p["id"] for p in produkty), default=0) + 1, "nazwa": nazwa, "kategoria": kategoria, "cena": float(cena), "ilosc": ilosc}\n    produkty.append(nowy)\n    return nowy\n\n\ndef statystyki(produkty):\n    if not produkty:\n        return {"liczba": 0, "srednia_cena": 0, "najdrozszy": None, "wartosc": 0}\n    return {"liczba": len(produkty),\n            "srednia_cena": round(sum(p["cena"] for p in produkty) / len(produkty), 2),\n            "najdrozszy": max(produkty, key=lambda p: p["cena"])["nazwa"],\n            "wartosc": round(sum(p["cena"] * p["ilosc"] for p in produkty), 2)}\n\n\ndef szukaj(produkty, fraza):\n    """Produkty, których nazwa albo kategoria zawiera frazę (bez wielkości liter)."""\n    f = fraza.strip().lower()\n    return [p for p in produkty if f in p["nazwa"].lower() or f in p["kategoria"].lower()]\n\n\nif __name__ == "__main__":\n    p = wczytaj("dane/produkty.csv")\n    print(statystyki(p))\n    for x in szukaj(p, input("Szukaj: ")):\n        print(x["id"], x["nazwa"], x["cena"])\n', 'magazyn_ukryty.py': '"""Moduł magazynu z paczki kursu (tydzień 7) — wersja poprawiona po znalezieniu błędu testem."""\n\n\ndef przyjmij(stan, n):\n    """Nowy stan po przyjęciu n sztuk; n ≤ 0 → ValueError."""\n    if n <= 0:\n        raise ValueError("ilość musi być dodatnia")\n    return stan + n\n\n\ndef wydaj(stan, n):\n    """Nowy stan po wydaniu n sztuk; n ≤ 0 albo więcej niż stan → ValueError."""\n    if n <= 0 or n > stan:\n        raise ValueError(f"nie można wydać {n} szt. (stan: {stan})")\n    return stan - n\n\n\ndef wartosc(stan, cena):\n    """Wartość towaru na stanie."""\n    return round(stan * cena, 2)\n'}

# wzorce: funkcje.py, bmi.py, zadania.py, magazyn_csv.py, magazyn_ukryty.py
# Weryfikator tygodnia 7 — testy ucznia uruchamiane na kodzie wzorcowym (muszą przejść) i na mutantach (muszą paść).


def _test_funkcji(plik_testu, nazwa):
    t = tekst(plik_testu)
    return len(re.findall(r"^\s*def test_\w+", t, re.M)), t


def test_testy_funkcji():
    mutanty("test_funkcje.py", "funkcje", WZORZEC["funkcje.py"], [
        ("pole liczone jako a + b", "return a * b", "return a + b"),
        ("czy_parzysta odwrócona", "return n % 2 == 0", "return n % 2 == 1"),
        ("maksimum zwraca pierwszy element", "        if x > najwieksza:\n            najwieksza = x\n", "        pass\n"),
        ("odwroc zwraca napis bez zmian", "return napis[::-1]", "return napis"),
        ("silnia(0) = 0", "    wynik = 1\n", "    wynik = 1 if n else 0\n"),
    ], min_testow=5)


def test_parametrize_bmi():
    n, t = _test_funkcji("test_bmi.py", "bmi")
    assert "@pytest.mark.parametrize" in t, "test_bmi.py: użyj @pytest.mark.parametrize (jeden test, wiele przypadków)"
    mutanty("test_bmi.py", "bmi", WZORZEC["bmi.py"], [
        ("granica niedowagi: 18.5 zaliczane do niedowagi", "if bmi < PROG_NIEDOWAGI:", "if bmi <= PROG_NIEDOWAGI:"),
        ("granica nadwagi: 25 zaliczane do normy", "if bmi < PROG_NADWAGI:", "if bmi <= PROG_NADWAGI:"),
        ("granica otyłości: 30 zaliczane do nadwagi", "if bmi < PROG_OTYLOSCI:", "if bmi <= PROG_OTYLOSCI:"),
    ], min_testow=6)


def test_fixture_menedzer():
    n, t = _test_funkcji("test_menedzer.py", "zadania")
    assert "@pytest.fixture" in t, "test_menedzer.py: przygotuj dane fixturą (@pytest.fixture)"
    fx = re.search(r"@pytest\.fixture[^\n]*\ndef (\w+)", t)
    assert fx, "test_menedzer.py: nie znaleziono definicji fixtury pod @pytest.fixture"
    uzycia = len(re.findall(rf"def test_\w+\([^)]*\b{fx.group(1)}\b", t))
    assert uzycia >= 4, f"test_menedzer.py: fixtura {fx.group(1)} użyta w {uzycia} testach — potrzeba co najmniej 4"
    mutanty("test_menedzer.py", "zadania", WZORZEC["zadania.py"], [
        ("dodaj nie usuwa spacji z tytułu", "    tytul = tytul.strip()\n", ""),
        ("oznacz oznacza złe zadanie (pomyłka o jeden)", 'zadania[nr - 1]["zrobione"] = True', 'zadania[nr % len(zadania)]["zrobione"] = True'),
        ("otwarte zwraca też zrobione", 'if not z["zrobione"]]', "]"),
        ("numer 0 akceptowany", "if not 1 <= nr <= len(zadania):", "if not 0 <= nr <= len(zadania):"),
    ], min_testow=4)


def test_ukryty_blad():
    m = modul("magazyn_ukryty")
    wyd = funkcja(m, "wydaj")
    ok(wyd(10, 10), 0, "Twoja poprawiona wersja: wydaj(10, 10) — wydanie całego stanu")
    ok(wyd(10, 3), 7, "wydaj(10, 3)")
    rzuca(wyd, 10, 11, opis="wydaj(10, 11)")
    rzuca(wyd, 10, 0, opis="wydaj(10, 0)")
    mutanty("test_ukryty.py", "magazyn_ukryty", WZORZEC["magazyn_ukryty.py"], [
        ("ukryty błąd z paczki: wydanie całego stanu blokowane", "if n <= 0 or n > stan:", "if n <= 0 or n >= stan:"),
    ], min_testow=1)


def test_testy_magazynu():
    n, t = _test_funkcji("test_magazyn.py", "magazyn_csv")
    assert n >= 15, f"test_magazyn.py: {n} testów — potrzeba co najmniej 15 (z przypadkami brzegowymi i negatywnymi)"
    assert "pytest.raises" in t, "test_magazyn.py: sprawdź też złe dane (pytest.raises)"
    mutanty("test_magazyn.py", "magazyn_csv", WZORZEC["magazyn_csv.py"], [
        ("duplikat nazwy z inną wielkością liter przechodzi", 'if any(p["nazwa"].lower() == nazwa.lower() for p in produkty):', 'if any(p["nazwa"] == nazwa for p in produkty):'),
        ("cena 0 odrzucana", "if cena < 0:", "if cena <= 0:"),
        ("id nowego produktu = liczba produktów + 1", 'max((p["id"] for p in produkty), default=0) + 1', "len(produkty) + 1"),
        ("statystyki dla pustej listy rzucają wyjątek", "    if not produkty:\n        return {", "    if False:\n        return {"),
        ("szukaj rozróżnia wielkość liter", 'f = fraza.strip().lower()', 'f = fraza.strip()'),
        ("wartość magazynu liczona bez ilości", 'round(sum(p["cena"] * p["ilosc"] for p in produkty), 2)}', 'round(sum(p["cena"] for p in produkty), 2)}'),
        ("pusta nazwa akceptowana", '    if not nazwa:\n        raise ValueError("nazwa nie może być pusta")\n', ""),
    ], min_testow=15)
