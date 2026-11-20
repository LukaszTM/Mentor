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


# Weryfikator tygodnia 13 — README.md i CI (GitHub Actions).

SEKCJE = ["opis", "wymagania", "instalacja", "uruchomienie", "testy", "konfiguracja", "ograniczenia", "jak powstal", "licencja"]
TAJ = [r"sk-[A-Za-z0-9_\-]{16,}", r"ghp_[A-Za-z0-9]{20,}"]
ZAMIENNIKI = ("wygeneruj", "twoj", "przyklad", "losow", "xxx", "wartosc", "klucz", "...", "<", "$", "{")


def _sekrety(t):
    """Wzorce kluczy i przypisania NAZWA=wartość, które nie wyglądają na zamiennik (np. „twoj_klucz”)."""
    if any(re.search(wz, t) for wz in TAJ):
        return True
    for m in re.finditer(r"(?i)(api[_-]?key|secret[_-]?key|token|haslo|hasło|password)\s*[:=]\s*[\"']?([^\s\"'`]{8,})", t):
        w = norm(m.group(2))
        if not any(z in w for z in ZAMIENNIKI) and re.search(r"\d", w) and re.search(r"[a-z]", w):
            return True
    return False


def test_readme():
    t = tekst("README.md")
    s = sekcje_md(t)
    for k in SEKCJE:
        assert any(n == k or n.startswith(k) for n in s), f"README.md: brak sekcji „## {k.capitalize()}”"
    assert "pytest" in t, "README.md: brak polecenia uruchomienia testów (python -m pytest -q)"
    assert "bin/activate" not in t, "README.md: polecenie z Linuksa (…/bin/activate) — podaj wersję dla Windows (.venv\\Scripts\\activate)"
    assert not _sekrety(t), "README.md: coś wygląda na wartość klucza/hasła — w README tylko nazwy zmiennych (albo zamiennik typu twoj_klucz)"
    n = len([l for l in t.splitlines() if l.strip()])
    assert n >= 25, f"README.md ma {n} niepustych linii — za mało na pełną dokumentację (≥ 25)"


def test_ci():
    req = [l.strip().lower() for l in tekst("requirements.txt").splitlines() if l.strip() and not l.strip().startswith("#")]
    for p in ("flask", "pytest"):
        assert any(re.match(rf"{p}\b", l) for l in req), f"requirements.txt: brak {p}"
    wf = list((WS / ".github" / "workflows").glob("*.y*ml")) if (WS / ".github" / "workflows").is_dir() else []
    assert wf, "Brak pliku workflow w .github/workflows/ (np. testy.yml)"
    t = "\n".join(p.read_text(encoding="utf-8") for p in wf)
    for fraza, opis in (("actions/checkout", "kroku actions/checkout"), ("actions/setup-python", "kroku actions/setup-python"),
                        ("requirements.txt", "instalacji zależności pip install -r requirements.txt"), ("pytest", "uruchomienia pytest"),
                        ("pull_request", "zdarzenia pull_request"), ("push", "zdarzenia push")):
        assert fraza in t, f"workflow: brak {opis}"
    assert not _sekrety(t), "workflow: coś wygląda na sekret wpisany w plik — użyj ${{ secrets.NAZWA }}"
