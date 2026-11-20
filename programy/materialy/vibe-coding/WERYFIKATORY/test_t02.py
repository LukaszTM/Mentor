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
        pytest.fail(f"{opis}: oczekiwano {wyjatek.__name__}, a funkcja rzuciła {type(e).__name__}: {e}")
    pytest.fail(f"{opis}: oczekiwano {wyjatek.__name__}, a funkcja zwróciła {w!r}")


def git(*args):
    """Uruchamia git w katalogu roboczym; zwraca (kod, wyjście). Brak gita → czytelny błąd testu."""
    import shutil
    import subprocess
    if not shutil.which("git"):
        pytest.fail("Nie znaleziono programu git — zainstaluj Git for Windows (lekcja „Git”) i uruchom Mentora ponownie")
    p = subprocess.run(["git", "-C", str(WS), *args], capture_output=True, text=True, encoding="utf-8", errors="replace")
    return p.returncode, (p.stdout + p.stderr).strip()


def repo():
    assert (WS / ".git").exists(), f"W katalogu roboczym {WS} nie ma repozytorium Git — wpisz git init (lekcja „Git”)"


# Weryfikator tygodnia 2 — napraw_mnie.py i lista_gosci.py.


def test_napraw_srednia():
    f = funkcja(modul("napraw_mnie"), "srednia_ocen")
    ok(f([5, 4, 5]), 4.67, "srednia_ocen([5, 4, 5])")
    ok(f([3]), 3, "srednia_ocen([3])")
    ok(f([]), 0, "srednia_ocen([]) — pusta lista (bez dzielenia przez zero)")


def test_napraw_najlepsza():
    f = funkcja(modul("napraw_mnie"), "najlepsza")
    ok(f([3, 5, 4]), 5, "najlepsza([3, 5, 4])")
    ok(f([2]), 2, "najlepsza([2])")
    assert f([]) is None, "najlepsza([]) powinna zwrócić None"


def test_napraw_noclegi():
    f = funkcja(modul("napraw_mnie"), "liczba_noclegow")
    ok(f([{"noce": 2}, {"noce": 3}]), 5, "liczba_noclegow([{'noce': 2}, {'noce': 3}])")
    ok(f([{"noce": 1}, {"noce": 1}, {"noce": 4}]), 6, "liczba_noclegow — trzy rezerwacje")
    ok(f([]), 0, "liczba_noclegow([])")


def _lg():
    m = modul("lista_gosci")
    return funkcja(m, "dodaj_goscia"), funkcja(m, "liczba_gosci"), funkcja(m, "raport")


def test_lista_dodawanie():
    dodaj, liczba, _ = _lg()
    l = []
    w = dodaj(l, "Anna", 2)
    assert w is l, "dodaj_goscia powinna zwrócić tę samą listę (return lista)"
    assert l == [{"imie": "Anna", "noce": 2}], f"po dodaj_goscia([], 'Anna', 2) lista to {l!r}, oczekiwano [{{'imie': 'Anna', 'noce': 2}}]"
    dodaj(l, "  Piotr ", 3)
    assert l[1] == {"imie": "Piotr", "noce": 3}, f"imię powinno być bez spacji na brzegach: otrzymano {l[1]!r}"
    ok(liczba(l), 2, "liczba_gosci po dodaniu 2 gości")
    ok(liczba([]), 0, "liczba_gosci([])")


def test_lista_walidacja():
    dodaj, _, _ = _lg()
    rzuca(dodaj, [], "", 2, opis="dodaj_goscia z pustym imieniem")
    rzuca(dodaj, [], "   ", 2, opis="dodaj_goscia z imieniem z samych spacji")
    rzuca(dodaj, [], "Ewa", 0, opis="dodaj_goscia z 0 nocy")


def test_lista_raport_odmiana():
    _, _, raport = _lg()
    l = [{"imie": i, "noce": n} for i, n in (("Anna", 1), ("Piotr", 3), ("Ola", 5), ("Ewa", 12), ("Jan", 22), ("Iza", 25), ("Tomek", 4))]
    linie = [x.strip() for x in raport(l).strip().splitlines()]
    oczek = ["Anna: 1 noc", "Piotr: 3 noce", "Ola: 5 nocy", "Ewa: 12 nocy", "Jan: 22 noce", "Iza: 25 nocy", "Tomek: 4 noce"]
    assert linie == oczek, f"raport: oczekiwano linii {oczek}, otrzymano {linie}"


def test_lista_raport_pusty():
    _, _, raport = _lg()
    ok(raport([]).strip(), "Brak gości", "raport([])")
