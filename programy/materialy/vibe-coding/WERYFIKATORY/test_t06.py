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


# Weryfikator tygodnia 6 — repozytorium Git i GitHub.

ZLE_OPISY = {"zmiany", "fix", "update", "asdf", "commit", "poprawki", "wip", "test"}


def test_git_repo():
    repo()
    kod, log = git("log", "--format=%s")
    assert kod == 0 and log, "Repozytorium nie ma jeszcze commitów — git add <pliki> i git commit -m \"opis\""
    opisy = [l.strip() for l in log.splitlines() if l.strip()]
    assert len(opisy) >= 3, f"W historii jest {len(opisy)} commitów — potrzeba co najmniej 3"
    dobre = [o for o in opisy if len(o) >= 10 and o.lower() not in ZLE_OPISY]
    assert len(dobre) >= 3, "Co najmniej 3 commity muszą mieć opis ≥ 10 znaków mówiący, co zmieniono (nie „fix”, „zmiany”)"


def test_git_ignore():
    repo()
    t = tekst(".gitignore")
    linie = {l.strip().rstrip("/") for l in t.splitlines() if l.strip() and not l.strip().startswith("#")}
    for w in (".env", ".venv", "__pycache__"):
        assert w in linie, f".gitignore: brak wpisu {w}"
    kod, pliki = git("ls-files")
    sledzone = pliki.splitlines()
    assert ".env" not in sledzone, "Plik .env jest w repozytorium — git rm --cached .env, commit, a klucze z niego unieważnij"
    assert not any(p.startswith(".venv/") for p in sledzone), "Folder .venv jest w repozytorium — git rm -r --cached .venv i commit"


def test_github():
    repo()
    t = tekst("adres_repo.txt")
    m = re.search(r"https://github\.com/([\w.-]+)/([\w.-]+?)(?:\.git)?/?(?:\s|$)", t)
    assert m, "adres_repo.txt: brak adresu w formacie https://github.com/NAZWA/REPO"
    kod, url = git("remote", "get-url", "origin")
    assert kod == 0, "Repozytorium nie ma zdalnego origin — git remote add origin https://github.com/NAZWA/pod-lipa.git"
    assert "github.com" in url, f"origin wskazuje {url} — oczekiwano adresu github.com"
    nazwa = lambda s: s.lower().rstrip("/").removesuffix(".git").split("github.com")[-1].strip(":/")
    assert nazwa(url) == nazwa(m.group(0).strip()), f"Adres w adres_repo.txt ({m.group(0).strip()}) nie pasuje do origin ({url})"
    kod, _ = git("rev-parse", "--verify", "--quiet", "refs/remotes/origin/main")
    assert kod == 0, "Brak gałęzi origin/main — wyślij historię: git push -u origin main"
    assert (WS / "README.md").exists(), "Brak README.md w repozytorium"
