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


# Weryfikator tygodnia 7 — zepsute_raporty.py, stan.md, kalendarz.py.

R = [{"pokoj": "Lipowy", "noce": 3, "kwota": 720}, {"pokoj": "Dębowy", "noce": 2, "kwota": 440}, {"pokoj": "Lipowy", "noce": 2, "kwota": 480},
     {"pokoj": "Klonowy", "noce": 5, "kwota": 1100}, {"pokoj": "Dębowy", "noce": 5, "kwota": 1000}]


def test_raporty_suma():
    f = funkcja(modul("zepsute_raporty"), "suma_przychodu")
    ok(f(R), 3740, "suma_przychodu(5 rezerwacji)")
    ok(f([]), 0, "suma_przychodu([])")


def test_raporty_srednia():
    f = funkcja(modul("zepsute_raporty"), "srednia_dlugosc")
    ok(f(R), 3.4, "srednia_dlugosc(5 rezerwacji) — (3+2+2+5+5)/5")
    ok(f(R[:2]), 2.5, "srednia_dlugosc(2 rezerwacje)")
    ok(f([]), 0, "srednia_dlugosc([])")


def test_raporty_top():
    f = funkcja(modul("zepsute_raporty"), "top_pokoje")
    ok([tuple(x) for x in f(R)], [("Dębowy", 7), ("Klonowy", 5), ("Lipowy", 5)], "top_pokoje(R)")
    ok([tuple(x) for x in f(R, 1)], [("Dębowy", 7)], "top_pokoje(R, 1)")
    ok([tuple(x) for x in f(R[:1], 5)], [("Lipowy", 3)], "top_pokoje(1 rezerwacja, n=5)")


def test_stan():
    t = tekst("stan.md")
    niepuste = [l for l in t.splitlines() if l.strip()]
    assert len(niepuste) <= 20, f"stan.md ma {len(niepuste)} niepustych linii — notatka przekazania ma być krótka (≤ 20)"
    s = sekcje_md(t)
    for k in ("zrobione", "decyzje", "nastepny krok"):
        assert k in s, f"stan.md: brak sekcji „## {k.capitalize()}”"
        assert any(len(l.strip("-* ").strip()) >= 3 for l in s[k]), f"stan.md: sekcja „{k}” jest pusta"


def _kal():
    m = modul("kalendarz")
    return [funkcja(m, n) for n in ("noce", "koliduje", "czy_wolny", "wolne_pokoje")]


def r(p, od, do):
    return {"pokoj": p, "od": od, "do": do}


def test_kalendarz_noce():
    noce, *_ = _kal()
    ok(noce("2026-12-20", "2026-12-23"), 3, "noce(20.12, 23.12)")
    ok(noce("2026-12-28", "2027-01-02"), 5, "noce(28.12.2026, 2.01.2027)")
    ok(noce("2028-02-28", "2028-03-01"), 2, "noce(28.02.2028, 1.03.2028) — rok przestępny")
    rzuca(noce, "2026-12-23", "2026-12-20", opis="noce(do przed od)")
    rzuca(noce, "2026-12-20", "2026-12-20", opis="noce(od == do)")


def test_kalendarz_koliduje():
    _, kol, _, _ = _kal()
    a = r("Lipowy", "2026-12-20", "2026-12-23")
    assert kol(a, r("Lipowy", "2026-12-23", "2026-12-25")) is False, "wyjazd w dniu przyjazdu nie jest kolizją (Lipowy 20–23 i 23–25)"
    assert kol(r("Lipowy", "2026-12-23", "2026-12-25"), a) is False, "kolejność argumentów nie może zmieniać wyniku (23–25 i 20–23)"
    assert kol(a, r("Lipowy", "2026-12-22", "2026-12-24")) is True, "Lipowy 20–23 i 22–24 kolidują"
    assert kol(a, r("Dębowy", "2026-12-20", "2026-12-23")) is False, "różne pokoje nie kolidują"
    assert kol(a, r("Lipowy", "2026-12-18", "2026-12-26")) is True, "przedział obejmujący (18–26) koliduje z 20–23"
    assert kol(a, r("Lipowy", "2026-12-21", "2026-12-22")) is True, "przedział wewnątrz (21–22) koliduje z 20–23"


def test_kalendarz_wolne():
    _, _, wolny, wolne = _kal()
    rez = [r("Lipowy", "2026-12-20", "2026-12-23"), r("Klonowy", "2026-12-22", "2026-12-27")]
    assert wolny(rez, "Lipowy", "2026-12-23", "2026-12-25") is True, "Lipowy wolny od 23.12 (dzień wyjazdu poprzedniego gościa)"
    assert wolny(rez, "Lipowy", "2026-12-19", "2026-12-21") is False, "Lipowy zajęty 20–23"
    ok(list(wolne(rez, "2026-12-21", "2026-12-22")), ["Dębowy", "Klonowy"], "wolne_pokoje 21–22.12")
    ok(list(wolne(rez, "2026-12-22", "2026-12-24")), ["Dębowy"], "wolne_pokoje 22–24.12")
    ok(list(wolne([], "2026-12-01", "2026-12-02")), ["Lipowy", "Dębowy", "Klonowy"], "wolne_pokoje bez rezerwacji — kolejność Lipowy, Dębowy, Klonowy")


def test_kalendarz_proces():
    repo()
    kod, log = git("log", "--format=%h", "--", "kalendarz.py")
    n = len([l for l in log.splitlines() if l.strip()]) if kod == 0 else 0
    assert n >= 4, f"W historii Gita jest {n} commitów zmieniających kalendarz.py — proces wymaga commita po każdym z 4 kroków"
