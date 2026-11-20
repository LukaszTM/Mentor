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


# Weryfikator tygodnia 0 — struktura katalogu roboczego i słowniczek.


def test_struktura_foldery():
    for f in ("notatki", "dane"):
        assert (WS / f).is_dir(), f"Brak folderu {f} bezpośrednio w katalogu roboczym {WS} (nazwa małymi literami, bez spacji)"


def test_struktura_o_mnie():
    p = WS / "notatki" / "o_mnie.md"
    if not p.exists() and (WS / "notatki" / "o_mnie.md.txt").exists():
        pytest.fail("Jest notatki/o_mnie.md.txt — rozszerzenia były ukryte; zmień nazwę na o_mnie.md")
    assert p.exists(), "Brak pliku notatki/o_mnie.md"
    linie = [l.strip() for l in p.read_text(encoding="utf-8", errors="replace").splitlines() if l.strip()]
    assert any(l.startswith("#") for l in linie), "notatki/o_mnie.md: brak nagłówka zaczynającego się od #"
    assert sum(1 for l in linie if l.startswith(("- ", "* "))) >= 2, "notatki/o_mnie.md: potrzebne co najmniej 2 punkty listy (linie zaczynające się od „- ”)"


def test_struktura_dziennik():
    t = tekst("dziennik.md")
    assert re.search(r"\b20\d\d-\d\d-\d\d\b|\b\d{1,2}\.\d{1,2}\.20\d\d\b", t), "dziennik.md: brak wpisu z datą (RRRR-MM-DD albo DD.MM.RRRR) — zamień RRRR-MM-DD z szablonu na dzisiejszą datę"
    tresc = [l for l in t.splitlines() if l.strip().startswith("-") and len(l.split(":", 1)[-1].strip()) >= 3]
    assert tresc, "dziennik.md: wpisz treść przynajmniej przy jednym punkcie (co zrobiłem / co sprawdziłem / czego nie rozumiem)"


POJECIA = ["model", "token", "kontekst", "halucynacja", "agent", "prompt", "specyfikacja", "test"]


def test_slowniczek():
    t = tekst("slowniczek.md")
    znalezione = {}
    for linia in t.splitlines():
        m = re.match(r"^\s*[-*]\s*\**([^:*]+?)\**\s*:\s*(.*)$", linia)
        if m:
            znalezione[norm(m.group(1)).strip()] = m.group(2).strip()
    for p in POJECIA:
        assert p in znalezione, f"slowniczek.md: brak pojęcia „{p}” w formacie „- {p}: wyjaśnienie”"
        assert len(znalezione[p].split()) >= 6, f"slowniczek.md: wyjaśnienie pojęcia „{p}” ma mniej niż 6 słów — napisz je pełnym zdaniem"
