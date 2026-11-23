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


# Weryfikator tygodnia 1 — kalkulator.py, wiek.py, rabat.py, bmi.py (program uruchamiany z danymi dla input()).
import datetime as _dt


def test_kalkulator():
    for dane, ocz in (("8\n+\n2\n", "10"), ("7\n/\n2\n", "3.5"), ("6\n*\n2.5\n", "15"), ("3\n-\n10\n", "-7")):
        kod, out = uruchom("kalkulator.py", dane)
        bez_bledu(kod, out, dane)
        zawiera(out, ocz, dane=dane)
    kod, out = uruchom("kalkulator.py", "5\n/\n0\n")
    bez_bledu(kod, out, "5 / 0")
    zawiera(out, "zero", dane="5 / 0 (komunikat o dzieleniu przez zero)")
    kod, out = uruchom("kalkulator.py", "5\n%\n2\n")
    bez_bledu(kod, out, "5 % 2")
    zawiera(out, "nieznane", dane="5 % 2 (komunikat „Nieznane działanie”)")


def test_wiek():
    rok = _dt.date.today().year
    for ur, wiek, kat in ((rok - 30, 30, "pełnoletni"), (rok - 18, 18, "pełnoletni"), (rok - 17, 17, "niepełnoletni"), (rok - 5, 5, "niepełnoletni")):
        kod, out = uruchom("wiek.py", f"{ur}\n")
        bez_bledu(kod, out, ur)
        zawiera(out, str(wiek), kat, dane=ur)
        if kat == "pełnoletni":
            assert "niepelnoletn" not in norm(out), f"dla roku {ur} (wiek {wiek}) program wypisał „niepełnoletni” — sprawdź warunek >= 18"
    kod, out = uruchom("wiek.py", f"{rok + 1}\n")
    bez_bledu(kod, out, rok + 1)
    zawiera(out, "przyszłości", dane=f"{rok + 1} (rok z przyszłości)")


def test_rabat():
    for kwota, proc, zaplata in (("99.99", "0%", "99.99"), ("100", "5%", "95.00"), ("299.99", "5%", "284.99"), ("300", "10%", "270.00"), ("1000", "10%", "900.00")):
        kod, out = uruchom("rabat.py", kwota + "\n")
        bez_bledu(kod, out, kwota)
        zawiera(out, proc, zaplata, dane=kwota)
    kod, out = uruchom("rabat.py", "-5\n")
    bez_bledu(kod, out, "-5")
    zawiera(out, "ujemna", dane="-5 (komunikat: kwota nie może być ujemna)")


def test_bmi():
    for dane, bmi, kat in (("1.80\n81\n", "25.0", "nadwaga"), ("1.70\n50\n", "17.3", "niedowaga"), ("1.75\n70\n", "22.9", "norma"), ("1.60\n80\n", "31.2", "otyłość"),
                           ("2.00\n74\n", "18.5", "norma")):
        kod, out = uruchom("bmi.py", dane)
        bez_bledu(kod, out, dane)
        zawiera(out, bmi, kat, dane=dane)
    kod, out = uruchom("bmi.py", "0\n70\n")
    bez_bledu(kod, out, "0 i 70")
    zawiera(out, "większe od zera", dane="wzrost 0")
    kod, out = uruchom("bmi.py", "180\n80\n")
    bez_bledu(kod, out, "180 i 80")
    zawiera(out, "metrach", dane="wzrost 180 (w centymetrach)")
