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


# Weryfikator tygodnia 14 — wymagania.md.


def test_wymagania():
    t = tekst("wymagania.md")
    linie = t.splitlines()
    idx = [i for i, l in enumerate(linie) if re.search(r"\bjako\b.+\bchc[eę]\b.+\baby\b", norm(l))]
    assert len(idx) >= 5, f"wymagania.md: {len(idx)} historyjek w formacie „Jako … chcę …, aby …” (potrzeba ≥ 5)"
    granice = idx[1:] + [len(linie)]
    for a, b in zip(idx, granice):
        kryteria = [l for l in linie[a + 1:b] if l.strip().startswith(("-", "*")) and len(l.strip("-* ").strip()) >= 5 and not l.strip().startswith("##")]
        stop = next((j for j, l in enumerate(linie[a + 1:b]) if l.strip().startswith("## ")), None)
        if stop is not None:
            kryteria = [l for l in linie[a + 1:a + 1 + stop] if l.strip().startswith(("-", "*")) and len(l.strip("-* ").strip()) >= 5]
        assert len(kryteria) >= 2, f"wymagania.md: historyjka „{linie[a].strip()[:60]}…” ma mniej niż 2 kryteria akceptacji (linie „- …” pod nią)"
    s = sekcje_md(t)
    pz = next((v for k, v in s.items() if k.startswith("poza zakresem")), None)
    assert pz is not None and sum(1 for l in pz if l.startswith(("-", "*"))) >= 2, "wymagania.md: sekcja „## Poza zakresem” z ≥ 2 pozycjami"
    pyt = next((v for k, v in s.items() if k.startswith("pytania")), None)
    assert pyt is not None and sum(1 for l in pyt if l.startswith(("-", "*", "1", "2", "3", "4", "5"))) >= 3, "wymagania.md: sekcja „## Pytania do klienta” z ≥ 3 pytaniami"
