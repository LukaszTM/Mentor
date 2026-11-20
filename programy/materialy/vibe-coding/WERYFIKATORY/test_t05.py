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


# Weryfikator tygodnia 5 — AGENTS.md/CLAUDE.md i konwerter.py.

TAJEMNICE = [r"sk-[A-Za-z0-9_\-]{16,}", r"ghp_[A-Za-z0-9]{20,}", r"(?i)(api[_-]?key|token|hasło|haslo|password)\s*[:=]\s*\S{6,}"]


def test_instrukcje_agents():
    t = tekst("AGENTS.md")
    linie = t.splitlines()
    assert len(linie) <= 200, f"AGENTS.md ma {len(linie)} linii — skróć do najważniejszych (≤ 200)"
    for wz in TAJEMNICE:
        assert not re.search(wz, t), "AGENTS.md: coś wygląda na klucz, token albo hasło — usuń je z pliku (instrukcje trafiają do repozytorium)"
    s = sekcje_md(t)
    for k in ("projekt", "polecenia", "zasady", "nie ruszaj"):
        assert k in s and s[k], f"AGENTS.md: brak niepustej sekcji „## {k.capitalize()}”"
    assert any("pytest" in l for l in s["polecenia"]), "AGENTS.md: w sekcji Polecenia brak polecenia uruchamiania testów (python -m pytest -q)"
    assert sum(1 for l in s["zasady"] if l.startswith(("-", "*"))) >= 3, "AGENTS.md: potrzeba co najmniej 3 zasad (linie „- …”) w sekcji Zasady"
    assert sum(1 for l in s["nie ruszaj"] if l.startswith(("-", "*"))) >= 1, "AGENTS.md: sekcja Nie ruszaj potrzebuje co najmniej jednej pozycji"


def test_instrukcje_claude():
    t = tekst("CLAUDE.md")
    assert any(l.strip() == "@AGENTS.md" for l in t.splitlines()), "CLAUDE.md: brak osobnej linii @AGENTS.md (import wspólnych instrukcji)"
    for wz in TAJEMNICE:
        assert not re.search(wz, t), "CLAUDE.md: coś wygląda na klucz, token albo hasło — usuń"


def _k():
    m = modul("konwerter")
    return funkcja(m, "parsuj_kwote"), funkcja(m, "zl_na_eur"), funkcja(m, "formatuj_zl")


def test_konwerter_parsuj():
    p, _, _ = _k()
    for t, w in (("1 234,56 zł", 1234.56), ("1234.56", 1234.56), ("  99 zł", 99), ("1 234 zł", 1234), ("0,5", 0.5), ("12 000,00", 12000)):
        ok(p(t), w, f"parsuj_kwote({t!r})")


def test_konwerter_parsuj_zle():
    p, _, _ = _k()
    for t in ("abc", "", "12,3,4", "zł"):
        rzuca(p, t, opis=f"parsuj_kwote({t!r})")


def test_konwerter_eur():
    _, e, _ = _k()
    ok(e(430, 4.30), 100.0, "zl_na_eur(430, 4.30)")
    ok(e(100, 4.27), 23.42, "zl_na_eur(100, 4.27) — zaokrąglenie do centów")
    ok(e(0, 4.3), 0, "zl_na_eur(0, 4.3)")
    rzuca(e, -5, 4.3, opis="zl_na_eur(-5, 4.3)")
    rzuca(e, 100, 0, opis="zl_na_eur(100, 0)")
    rzuca(e, 100, -4.3, opis="zl_na_eur(100, -4.3)")


def test_konwerter_formatuj():
    _, _, f = _k()
    for k, w in ((1234.56, "1 234,56 zł"), (5, "5,00 zł"), (1000000, "1 000 000,00 zł"), (0.1, "0,10 zł"), (999.999, "1 000,00 zł")):
        wynik = f(k).replace(" ", " ")
        ok(wynik, w, f"formatuj_zl({k!r})")
