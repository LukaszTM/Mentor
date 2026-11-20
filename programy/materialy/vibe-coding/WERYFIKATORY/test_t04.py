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


# Weryfikator tygodnia 4 — instalacja agenta i powitanie.py.


def test_instalacja():
    p = plik("instalacja.txt")
    surowe = p.read_bytes()
    for kod in ("utf-8", "utf-16", "cp1250"):
        try:
            t = surowe.decode(kod)
            if re.search(r"\d+\.\d+", t):
                break
        except UnicodeDecodeError:
            continue
    else:
        t = surowe.decode("utf-8", errors="replace")
    t = t.replace("\x00", "")
    assert re.search(r"\b\d+\.\d+\.\d+\s*\(Claude Code\)", t) or re.search(r"codex(-cli)?\s+v?\d+\.\d+\.\d+", t, re.I), \
        "instalacja.txt nie zawiera wyniku claude --version („X.Y.Z (Claude Code)”) ani codex --version („codex-cli X.Y.Z”) — zapisz go komendą: claude --version > instalacja.txt"


def _p():
    return funkcja(modul("powitanie"), "powitanie")


def test_powitanie_godziny():
    f = _p()
    for g, w in ((9, "Dzień dobry, Anna!"), (5, "Dzień dobry, Anna!"), (17, "Dzień dobry, Anna!"), (18, "Dobry wieczór, Anna!"),
                 (23, "Dobry wieczór, Anna!"), (0, "Dobry wieczór, Anna!"), (4, "Dobry wieczór, Anna!")):
        ok(f("Anna", g), w, f"powitanie('Anna', {g})")


def test_powitanie_imie():
    f = _p()
    ok(f("anna", 9), "Dzień dobry, Anna!", "powitanie('anna', 9) — wielka pierwsza litera")
    ok(f("  Ewa ", 20), "Dobry wieczór, Ewa!", "powitanie('  Ewa ', 20) — bez spacji na brzegach")
    ok(f("maria-józefa", 10), "Dzień dobry, Maria-józefa!", "powitanie('maria-józefa', 10) — reszta imienia bez zmian")
    ok(f("ANNA", 10), "Dzień dobry, ANNA!", "powitanie('ANNA', 10) — reszta imienia bez zmian (nie capitalize)")


def test_powitanie_zle_dane():
    f = _p()
    rzuca(f, "", 9, opis="powitanie('', 9)")
    rzuca(f, "   ", 9, opis="powitanie('   ', 9)")
    rzuca(f, "Anna", 24, opis="powitanie('Anna', 24)")
    rzuca(f, "Anna", -1, opis="powitanie('Anna', -1)")
