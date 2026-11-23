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


# Weryfikator tygodnia 3 — funkcje.py, stany.py, bledy.py, losowanie.py, menedzer.py.
import ast as _ast
import datetime as _dt


def test_funkcje():
    m = modul("funkcje")
    pole, parz, maks, odw, sil = (funkcja(m, n) for n in ("pole_prostokata", "czy_parzysta", "maksimum", "odwroc", "silnia"))
    ok(pole(3, 4), 12, "pole_prostokata(3, 4)")
    ok(pole(2.5, 2), 5.0, "pole_prostokata(2.5, 2)")
    ok(parz(4), True, "czy_parzysta(4)")
    ok(parz(7), False, "czy_parzysta(7)")
    ok(parz(0), True, "czy_parzysta(0)")
    ok(maks([3, 9, 2]), 9, "maksimum([3, 9, 2])")
    ok(maks([-5, -2, -9]), -2, "maksimum([-5, -2, -9])")
    ok(maks([7]), 7, "maksimum([7])")
    rzuca(maks, [], opis="maksimum([])")
    ok(odw("kot"), "tok", "odwroc(\"kot\")")
    ok(odw(""), "", "odwroc(\"\")")
    ok(sil(0), 1, "silnia(0)")
    ok(sil(5), 120, "silnia(5)")
    rzuca(sil, -1, opis="silnia(-1)")
    for n in ("pole_prostokata", "czy_parzysta", "maksimum", "odwroc", "silnia"):
        assert (getattr(m, n).__doc__ or "").strip(), f"funkcja {n} nie ma docstringu"
    for w in _ast.walk(drzewo("funkcje.py")):
        if isinstance(w, _ast.FunctionDef) and w.name == "maksimum":
            uzyte = {getattr(c.func, "id", "") for c in _ast.walk(w) if isinstance(c, _ast.Call)}
            assert not uzyte & {"max", "sorted"}, "maksimum: napisz pętlę — bez wbudowanych max() i sorted()"


def test_stany():
    m = modul("stany")
    dodaj, usun, pos, razem = (funkcja(m, n) for n in ("dodaj", "usun", "posortowane", "razem"))
    s = {}
    dodaj(s, "zeszyt", 120)
    dodaj(s, "klej", 30)
    dodaj(s, "zeszyt", 10)
    ok(s, {"zeszyt": 130, "klej": 30}, "stany po dodaj(zeszyt 120), dodaj(klej 30), dodaj(zeszyt 10)")
    rzuca(dodaj, s, "gumka", 0, opis="dodaj(…, 0)")
    rzuca(dodaj, s, "gumka", -5, opis="dodaj(…, -5)")
    dodaj(s, "gumka", 30)
    ok(pos(s), [("gumka", 30), ("klej", 30), ("zeszyt", 130)], "posortowane — rosnąco po ilości, przy remisie po nazwie")
    ok(razem(s), 190, "razem")
    usun(s, "klej")
    assert "klej" not in s, "usun(s, \"klej\") — klej nadal jest w słowniku"
    rzuca(usun, s, "farby", opis="usun(s, \"farby\") — brak produktu")
    ok(razem({}), 0, "razem({})")


def test_bledy():
    m = modul("bledy")
    f = funkcja(m, "na_liczbe")
    ok(f("4.5"), 4.5, "na_liczbe(\"4.5\")")
    ok(f("4,5"), 4.5, "na_liczbe(\"4,5\")")
    ok(f("  3 "), 3.0, "na_liczbe(\"  3 \")")
    for zle in ("abc", "", "4,5,6"):
        rzuca(f, zle, opis=f"na_liczbe({zle!r})")
    kod, out = uruchom("bledy.py", "abc\n9\n2\n")
    bez_bledu(kod, out, "abc, 9, 2")
    zawiera(out, "nie liczba", "4.5", dane="abc → ponowne pytanie, potem 9 i 2")
    kod, out = uruchom("bledy.py", "8\n0\n")
    bez_bledu(kod, out, "8 i 0")
    zawiera(out, "zero", dane="8 / 0")


def test_losowanie():
    m = modul("losowanie")
    los, termin = funkcja(m, "do_inwentaryzacji"), funkcja(m, "termin")
    prod = ["zeszyt", "długopis", "klej", "gumka", "blok", "kredki"]
    w = los(prod)
    assert isinstance(w, list) and len(w) == 3, f"do_inwentaryzacji(produkty) ma zwrócić listę 3 produktów, zwróciła {w!r}"
    assert len(set(w)) == 3 and set(w) <= set(prod), f"wylosowane produkty mają być różne i z listy: {w!r}"
    ok(len(los(prod, 5)), 5, "len(do_inwentaryzacji(produkty, 5))")
    assert los(prod, 3, seed=7) == los(prod, 3, seed=7), "ten sam seed ma dawać ten sam wynik"
    rzuca(los, prod, 10, opis="do_inwentaryzacji(6 produktów, 10)")
    ok(prod, ["zeszyt", "długopis", "klej", "gumka", "blok", "kredki"], "lista wejściowa po losowaniu (nie zmieniaj jej)")
    ok(termin(_dt.date(2026, 1, 28)), _dt.date(2026, 2, 4), "termin(28.01.2026)")
    ok(termin(_dt.date(2026, 12, 28), 7), _dt.date(2027, 1, 4), "termin(28.12.2026, 7)")
    ok(termin(_dt.date(2026, 1, 28), 30), _dt.date(2026, 2, 27), "termin(28.01.2026, 30)")


def test_menedzer():
    m = modul("menedzer")
    dodaj, oznacz, usun, otwarte = (funkcja(m, n) for n in ("dodaj", "oznacz", "usun", "otwarte"))
    z = []
    dodaj(z, "Zamówić papier")
    dodaj(z, "  Policzyć zeszyty ")
    dodaj(z, "Wysłać paczkę")
    ok(otwarte(z), ["Zamówić papier", "Policzyć zeszyty", "Wysłać paczkę"], "otwarte po 3 × dodaj (spacje usunięte)")
    rzuca(dodaj, z, "   ", opis="dodaj(z, \"   \")")
    oznacz(z, 2)
    ok(otwarte(z), ["Zamówić papier", "Wysłać paczkę"], "otwarte po oznacz(z, 2)")
    for zly in (0, 4, -1):
        rzuca(oznacz, z, zly, opis=f"oznacz(z, {zly})")
    ok(usun(z, 1), "Zamówić papier", "usun(z, 1) zwraca tytuł")
    ok(len(z), 2, "liczba zadań po usunięciu")
    ok(otwarte(z), ["Wysłać paczkę"], "otwarte po usunięciu")
    rzuca(usun, z, 3, opis="usun(z, 3) przy 2 zadaniach")
    kod, out = uruchom("menedzer.py", "1\nZamówić papier\n3\n0\n")
    bez_bledu(kod, out, "menu: dodaj, lista, koniec")
    zawiera(out, "Zamówić papier", dane="menu: 1 dodaj → 3 lista → 0")
