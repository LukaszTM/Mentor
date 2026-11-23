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


WZORZEC = {'baza.py': '"""Warstwa danych projektu Magazyn — SQLite, zapytania wyłącznie z parametrami ?."""\nimport sqlite3\n\n\ndef utworz_baze(sciezka="magazyn.db"):\n    """Połączenie z bazą (wiersze jak słowniki) i tabele, jeśli ich nie ma."""\n    con = sqlite3.connect(sciezka)\n    con.row_factory = sqlite3.Row\n    with con:\n        con.execute("""CREATE TABLE IF NOT EXISTS produkty (\n            id INTEGER PRIMARY KEY, nazwa TEXT NOT NULL UNIQUE, kategoria TEXT NOT NULL,\n            cena REAL NOT NULL CHECK (cena >= 0), ilosc INTEGER NOT NULL DEFAULT 0 CHECK (ilosc >= 0))""")\n        con.execute("""CREATE TABLE IF NOT EXISTS operacje (\n            id INTEGER PRIMARY KEY, produkt_id INTEGER NOT NULL REFERENCES produkty(id),\n            typ TEXT NOT NULL CHECK (typ IN (\'przyjecie\', \'wydanie\')), ilosc INTEGER NOT NULL, data TEXT NOT NULL)""")\n    return con\n\n\ndef dodaj_produkt(con, nazwa, kategoria, cena, ilosc=0):\n    """Dodaje produkt i zwraca jego id; duplikat nazwy → sqlite3.IntegrityError."""\n    with con:\n        cur = con.execute("INSERT INTO produkty (nazwa, kategoria, cena, ilosc) VALUES (?, ?, ?, ?)", (nazwa.strip(), kategoria.strip(), cena, ilosc))\n    return cur.lastrowid\n\n\ndef pobierz_produkty(con, kategoria=None):\n    """Lista produktów (słowniki) alfabetycznie; opcjonalnie z jednej kategorii."""\n    if kategoria is None:\n        wiersze = con.execute("SELECT * FROM produkty ORDER BY nazwa").fetchall()\n    else:\n        wiersze = con.execute("SELECT * FROM produkty WHERE kategoria = ? ORDER BY nazwa", (kategoria,)).fetchall()\n    return [dict(w) for w in wiersze]\n\n\ndef pobierz_produkt(con, pid):\n    w = con.execute("SELECT * FROM produkty WHERE id = ?", (pid,)).fetchone()\n    return dict(w) if w else None\n\n\ndef zmien_ilosc(con, pid, delta):\n    """Zmienia stan o delta i zwraca nowy stan; brak produktu albo stan < 0 → ValueError."""\n    p = pobierz_produkt(con, pid)\n    if p is None:\n        raise ValueError(f"nie ma produktu o id {pid}")\n    nowa = p["ilosc"] + delta\n    if nowa < 0:\n        raise ValueError(f"stan nie może być ujemny (jest {p[\'ilosc\']})")\n    with con:\n        con.execute("UPDATE produkty SET ilosc = ? WHERE id = ?", (nowa, pid))\n    return nowa\n\n\ndef usun_produkt(con, pid):\n    with con:\n        if con.execute("DELETE FROM produkty WHERE id = ?", (pid,)).rowcount == 0:\n            raise ValueError(f"nie ma produktu o id {pid}")\n\n\ndef dodaj_operacje(con, pid, typ, ilosc, data):\n    with con:\n        con.execute("INSERT INTO operacje (produkt_id, typ, ilosc, data) VALUES (?, ?, ?, ?)", (pid, typ, ilosc, data))\n', 'magazyn.py': '"""Logika magazynu: przyjęcia i wydania z kontrolą stanu oraz historia operacji."""\nimport baza\n\n\ndef _ilosc_poprawna(ilosc):\n    if not isinstance(ilosc, int) or ilosc <= 0:\n        raise ValueError("ilość musi być dodatnią liczbą całkowitą")\n\n\ndef przyjecie(con, pid, ilosc, data):\n    """Przyjmuje towar; zwraca nowy stan."""\n    _ilosc_poprawna(ilosc)\n    nowy = baza.zmien_ilosc(con, pid, ilosc)\n    baza.dodaj_operacje(con, pid, "przyjecie", ilosc, data)\n    return nowy\n\n\ndef wydanie(con, pid, ilosc, data):\n    """Wydaje towar (najwyżej cały stan); zwraca nowy stan."""\n    p = baza.pobierz_produkt(con, pid)\n    if p is None:\n        raise ValueError(f"nie ma produktu o id {pid}")\n    stan = p["ilosc"]\n    if ilosc <= 0 or ilosc > stan or not isinstance(ilosc, int):\n        raise ValueError(f"nie można wydać {ilosc} szt. (stan: {stan})")\n    nowy = baza.zmien_ilosc(con, pid, -ilosc)\n    baza.dodaj_operacje(con, pid, "wydanie", ilosc, data)\n    return nowy\n\n\ndef historia(con, pid):\n    """Lista (data, typ, ilość) operacji produktu rosnąco po dacie."""\n    w = con.execute("SELECT data, typ, ilosc FROM operacje WHERE produkt_id = ? ORDER BY data, id", (pid,)).fetchall()\n    return [(r["data"], r["typ"], r["ilosc"]) for r in w]\n\n\ndef wartosc_magazynu(con):\n    return round(sum(p["cena"] * p["ilosc"] for p in baza.pobierz_produkty(con)), 2)\n'}

# wzorce: baza.py, magazyn.py
# Weryfikator tygodnia 10 — projekt Magazyn: PLAN.md, baza.py (SQLite), magazyn.py (logika), testy z bazą tymczasową, rdzeń z menu.
import ast as _ast
import sqlite3 as _sqlite3


def test_plan():
    s = sekcje_md(tekst("PLAN.md"))
    for k in ("cel", "zakres", "poza zakresem", "struktura", "kolejnosc", "ryzyka"):
        klucz = next((x for x in s if x.startswith(k) or (k == "zakres" and x == "zakres")), None)
        assert klucz, f"PLAN.md: brak sekcji „## {k.capitalize()}”"
        assert s[klucz], f"PLAN.md: sekcja „{k}” jest pusta"
    assert sum(1 for l in s[next(x for x in s if x.startswith('kolejnosc'))] if re.match(r"^(\d+\.|-)", l)) >= 4, "PLAN.md: kolejność — co najmniej 4 kroki"


def _baza(tmp_path):
    b = modul("baza")
    con = funkcja(b, "utworz_baze")(tmp_path / "test.db")
    return b, con


def test_baza(tmp_path):
    b, con = _baza(tmp_path)
    dodaj, pobierz, zmien, usun = (funkcja(b, n) for n in ("dodaj_produkt", "pobierz_produkty", "zmien_ilosc", "usun_produkt"))
    a = dodaj(con, "Zeszyt A5", "zeszyty", 4.5, 120)
    s = dodaj(con, "Segregator A4", "biuro", 11.9)
    assert isinstance(a, int) and a != s, "dodaj_produkt zwraca id nowego produktu (int)"
    p = pobierz(con)
    ok([x["nazwa"] for x in p], ["Segregator A4", "Zeszyt A5"], "pobierz_produkty — alfabetycznie po nazwie")
    ok(p[0]["ilosc"], 0, "domyślna ilość 0")
    ok([x["nazwa"] for x in pobierz(con, "biuro")], ["Segregator A4"], "pobierz_produkty(con, \"biuro\")")
    ok(pobierz(con, "x' OR '1'='1"), [], "pobierz_produkty z próbą SQL injection — parametry ?")
    ok(zmien(con, a, -20), 100, "zmien_ilosc(con, id, -20) zwraca nowy stan")
    rzuca(zmien, con, a, -101, opis="zmien_ilosc poniżej zera")
    rzuca(zmien, con, 999, 5, opis="zmien_ilosc nieistniejącego produktu")
    rzuca(dodaj, con, "Zeszyt A5", "zeszyty", 1.0, wyjatek=(ValueError, _sqlite3.IntegrityError), opis="duplikat nazwy")
    usun(con, s)
    ok([x["nazwa"] for x in pobierz(con)], ["Zeszyt A5"], "po usun_produkt")
    rzuca(usun, con, s, opis="usun_produkt nieistniejącego")
    con2 = funkcja(b, "utworz_baze")(tmp_path / "test.db")
    ok([x["ilosc"] for x in funkcja(b, "pobierz_produkty")(con2)], [100], "dane zapisane w pliku bazy (commit) — widoczne po ponownym połączeniu")
    for w in _ast.walk(drzewo("baza.py")):
        if isinstance(w, _ast.Call) and getattr(w.func, "attr", "") in ("execute", "executemany") and w.args and isinstance(w.args[0], _ast.JoinedStr):
            pytest.fail("baza.py: f-string w execute() — zapytania tylko z parametrami ? (SQL injection)")


def test_magazyn(tmp_path):
    b, con = _baza(tmp_path)
    m = modul("magazyn")
    prz, wyd, hist, wart = (funkcja(m, n) for n in ("przyjecie", "wydanie", "historia", "wartosc_magazynu"))
    pid = funkcja(b, "dodaj_produkt")(con, "Klej w sztyfcie", "akcesoria", 3.4, 0)
    ok(prz(con, pid, 50, "2026-11-20"), 50, "przyjecie zwraca nowy stan")
    ok(wyd(con, pid, 20, "2026-11-22"), 30, "wydanie zwraca nowy stan")
    ok(wyd(con, pid, 30, "2026-11-23"), 0, "wydanie całego stanu (wartość brzegowa)")
    rzuca(wyd, con, pid, 1, "2026-11-23", opis="wydanie ponad stan")
    rzuca(prz, con, pid, 0, "2026-11-23", opis="przyjęcie 0 sztuk")
    rzuca(wyd, con, pid, -5, "2026-11-23", opis="wydanie ujemne")
    prz(con, pid, 5, "2026-11-21")
    ok(hist(con, pid), [("2026-11-20", "przyjecie", 50), ("2026-11-21", "przyjecie", 5), ("2026-11-22", "wydanie", 20), ("2026-11-23", "wydanie", 30)],
       "historia — (data, typ, ilość) rosnąco po dacie, bez nieudanych operacji")
    ok(wart(con), 17.0, "wartosc_magazynu (5 szt. × 3.40)")


def test_testy_bazy():
    t = tekst("test_baza.py")
    assert "tmp_path" in t or ":memory:" in t, "test_baza.py: baza tymczasowa (fixtura z tmp_path albo \":memory:\") — testy nie dotykają magazyn.db"
    assert "@pytest.fixture" in t, "test_baza.py: fixtura tworząca świeżą bazę dla każdego testu"
    import shutil as _sh
    import tempfile as _tf
    with _tf.TemporaryDirectory(prefix="mut10_") as td:
        td = Path(td)
        (td / "test_baza.py").write_text(t, encoding="utf-8")
        zmiany = [("magazyn.py", "wydanie całego stanu blokowane", "if ilosc <= 0 or ilosc > stan ", "if ilosc <= 0 or ilosc >= stan "),
                  ("magazyn.py", "historia bez sortowania po dacie", "ORDER BY data, id", "ORDER BY id"),
                  ("baza.py", "zmiana ilości bez kontroli zera", "    if nowa < 0:\n        raise ValueError", "    if False:\n        raise ValueError"),
                  ("baza.py", "filtr kategorii ignorowany", "WHERE kategoria = ? ORDER BY nazwa", "WHERE ? IS NOT NULL ORDER BY nazwa")]
        for plik_, kod in WZORZEC.items():
            (td / plik_).write_text(kod, encoding="utf-8")
        kod, out = pytest_ucznia(td, "test_baza.py")
        assert kod == 0, f"test_baza.py nie przechodzi na wzorcowych baza.py i magazyn.py:\n{out[-1500:]}"
        m = re.search(r"(\d+) passed", out)
        assert m and int(m.group(1)) >= 8, "test_baza.py: co najmniej 8 testów"
        for plik_, opis, stary, nowy in zmiany:
            assert stary in WZORZEC[plik_], f"(błąd weryfikatora) {stary!r}"
            (td / plik_).write_text(WZORZEC[plik_].replace(stary, nowy, 1), encoding="utf-8")
            _sh.rmtree(td / "__pycache__", ignore_errors=True)
            kod, out = pytest_ucznia(td, "test_baza.py")
            assert kod != 0, f"test_baza.py nie wykrył błędu: {opis}"
            (td / plik_).write_text(WZORZEC[plik_], encoding="utf-8")


def test_rdzen(tmp_path):
    import shutil as _sh
    kod, out = uruchom("menu_magazyn.py", "1\nZeszyt A5\nzeszyty\n4.50\n2\n1\n30\n4\n0\n", env={"MAGAZYN_DB": str(tmp_path / "menu.db")})
    bez_bledu(kod, out, "menu: dodaj produkt, przyjęcie, lista, koniec")
    zawiera(out, "Zeszyt A5", "30", dane="1 dodaj → 2 przyjęcie 30 szt. → 4 lista → 0")
    kod, out = uruchom("menu_magazyn.py", "3\n1\n500\n0\n", env={"MAGAZYN_DB": str(tmp_path / "menu.db")})
    bez_bledu(kod, out, "wydanie ponad stan")
    zawiera(out, "Błąd", dane="3 wydanie 500 szt. (więcej niż stan) → komunikat, program działa dalej")
    liczba = 0
    for p in list(WS.glob("test_*.py")) + list((WS / "tests").glob("test_*.py")):
        liczba += len(re.findall(r"^def test_\w+", p.read_text(encoding="utf-8", errors="ignore"), re.M))
    assert liczba >= 20, f"W projekcie jest {liczba} testów — rdzeń projektu ma mieć co najmniej 20"
