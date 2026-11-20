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


# Weryfikator tygodnia 1 — terminal i kalkulator_pobytu.py.


def test_terminal():
    for f in ("raporty", "dane", "notatki"):
        assert (WS / f).is_dir(), f"Brak folderu {f} w katalogu roboczym — utwórz go komendą mkdir {f}"
    p = plik("terminal.txt")
    surowe = p.read_bytes()
    t = surowe.decode("utf-8", errors="replace") + "\n" + surowe.decode("cp852", errors="replace")
    assert "<DIR>" in t, "terminal.txt nie zawiera „<DIR>” — zapisz wynik komendy: dir > terminal.txt (nie wpisuj listy ręcznie)"
    for f in ("raporty", "dane", "notatki"):
        assert f in t, f"terminal.txt: na liście z komendy dir brakuje folderu {f} — utwórz folder i zapisz listę ponownie"


def _k():
    return funkcja(modul("kalkulator_pobytu"), "koszt_pobytu")


def test_kalkulator_przyklady():
    f = _k()
    ok(f(2, 2), 480, "koszt_pobytu(2, 2)")
    ok(f(1, 1), 120, "koszt_pobytu(1, 1)")
    ok(f(6, 1), 720, "koszt_pobytu(6, 1) — 6 nocy, jeszcze bez rabatu")


def test_kalkulator_rabat_od_7_nocy():
    f = _k()
    ok(f(7, 1), 756.0, "koszt_pobytu(7, 1) — granica: od 7 nocy rabat 10%")
    ok(f(7, 2), 1512.0, "koszt_pobytu(7, 2)")
    ok(f(10, 3), 3240.0, "koszt_pobytu(10, 3)")


def test_kalkulator_inna_cena_i_grosze():
    f = _k()
    ok(f(2, 2, cena_za_osobe_noc=150), 600, "koszt_pobytu(2, 2, cena_za_osobe_noc=150)")
    ok(f(7, 1, cena_za_osobe_noc=99.99), 629.94, "koszt_pobytu(7, 1, cena_za_osobe_noc=99.99) — zaokrąglenie do groszy")
    w = f(7, 1, cena_za_osobe_noc=99.99)
    assert round(w, 2) == w, f"wynik {w!r} nie jest zaokrąglony do groszy — użyj round(koszt, 2)"


def test_kalkulator_zle_dane():
    f = _k()
    rzuca(f, 0, 2, opis="koszt_pobytu(0, 2) — zero nocy")
    rzuca(f, 2, 0, opis="koszt_pobytu(2, 0) — zero osób")
    rzuca(f, -3, 1, opis="koszt_pobytu(-3, 1) — ujemna liczba nocy")
