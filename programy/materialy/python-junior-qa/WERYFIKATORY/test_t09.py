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


# Weryfikator tygodnia 9 — przypadki testowe, raporty błędów sklepu testowego, GitHub Actions z pytest-html, repozytorium testów (struktura POM, CI w README).


def test_przypadki_testowe():
    t = tekst("przypadki_testowe.md")
    naglowek = next((l for l in t.splitlines() if l.strip().startswith("|") and "oczekiwany" in norm(l)), None)
    assert naglowek, "przypadki_testowe.md: tabela z nagłówkiem zawierającym kolumnę „Oczekiwany wynik”"
    kol = [norm(c.strip()) for c in naglowek.strip().strip("|").split("|")]
    for k in ("id", "kroki", "oczekiwany"):
        assert any(k in c for c in kol), f"przypadki_testowe.md: brak kolumny „{k}” w nagłówku tabeli"
    io = next(i for i, c in enumerate(kol) if "oczekiwany" in c)
    wiersze = [[c.strip() for c in l.strip().strip("|").split("|")] for l in t.splitlines() if re.match(r"^\s*\|\s*TC-\d+", l)]
    assert len(wiersze) >= 10, f"przypadki_testowe.md: {len(wiersze)} przypadków (wiersze „| TC-01 | …”) — potrzeba 10"
    for w in wiersze:
        assert len(w) > io and len(w[io].split()) >= 2, f"{w[0]}: wpisz oczekiwany wynik (co najmniej 2 słowa)"
    ids = [w[0] for w in wiersze]
    assert len(set(ids)) == len(ids), "przypadki_testowe.md: identyfikatory TC-… muszą być unikalne"
    negatywne = sum(1 for w in wiersze if any(s in norm(" ".join(w)) for s in ("blad", "bledn", "odrzuc", "komunikat", "pust", "nie ")))
    assert negatywne >= 3, "przypadki_testowe.md: co najmniej 3 przypadki negatywne (złe dane → komunikat / odrzucenie)"


DEFEKTY = [("10", "kosz"), ("00000",), ("wielk", "szuk"), ("wielk", "login"), ("stan", "kosz"), ("kot10",), ("zszywk",)]


def test_bug_raporty():
    t = tekst("bug_raporty.md")
    czesci = re.split(r"^##\s+", t, flags=re.M)[1:]
    raporty = [c for c in czesci if norm(c.split("\n", 1)[0]).startswith("bug")]
    assert len(raporty) >= 3, f"bug_raporty.md: {len(raporty)} raportów — potrzeba 3 sekcji „## BUG-01: …”"
    for r in raporty:
        tyt = r.split("\n", 1)[0].strip()
        n = norm(r)
        for pole in ("srodowisko", "kroki", "oczekiwany", "rzeczywisty", "waznosc"):
            assert pole in n, f"raport „{tyt}”: brak pola „{pole}”"
        assert re.search(r"^\s*1\.", r, re.M) and re.search(r"^\s*2\.", r, re.M), f"raport „{tyt}”: kroki ponumerowane (1., 2., …)"
        assert len(tyt.split()) >= 4, f"raport „{tyt}”: tytuł mówi gdzie + co + w jakich warunkach (co najmniej 4 słowa)"
    trafione = sum(1 for r in raporty if any(all(k in norm(r) for k in d) for d in DEFEKTY))
    assert trafione >= 2, "bug_raporty.md: co najmniej 2 raporty dotyczą prawdziwych defektów sklepu testowego (porównaj działanie sklepu z wymaganiami w jego README)"


def _workflow():
    pliki = sorted((WS / ".github" / "workflows").glob("*.y*ml")) if (WS / ".github" / "workflows").exists() else []
    assert pliki, "Brak pliku workflow w .github/workflows/ (np. .github/workflows/tests.yml — folder .github z kropką)"
    return pliki[0], pliki[0].read_text(encoding="utf-8")


def test_github_actions():
    p, t = _workflow()
    assert "\t" not in t, f"{p.name}: tabulator w YAML — wcięcia tylko spacjami"
    for f in ("actions/checkout", "actions/setup-python", "pip install -r requirements.txt", "pytest"):
        assert f in t, f"{p.name}: brak „{f}”"
    assert re.search(r"\bpush\b", t), f"{p.name}: uruchamiaj przy push (on: [push, pull_request])"
    assert not re.search(r"(password|token|api_key)\s*:\s*['\"]?\w{6,}", t, re.I), f"{p.name}: sekret w workflow — użyj ${{ secrets.NAZWA }}"


def test_pytest_html():
    p, t = _workflow()
    assert "--html" in t, f"{p.name}: pytest z opcją --html=raport.html (pytest-html)"
    assert "upload-artifact" in t and re.search(r"if:\s*always\(\)", t), f"{p.name}: raport jako artefakt (actions/upload-artifact) z if: always()"
    assert re.search(r"^pytest-html", tekst("requirements.txt"), re.M | re.I), "requirements.txt: dopisz pytest-html (CI instaluje tylko to, co jest na liście)"


def test_repo_testow():
    for f in ("pages/__init__.py", "conftest.py"):
        assert (WS / f).exists(), f"Brak {f} — struktura projektu testów: pages/ (Page Objecty), tests/ (testy), conftest.py (fixtury)"
    strony = [p for p in (WS / "pages").glob("*.py") if p.name != "__init__.py"]
    assert len(strony) >= 2, "pages/: co najmniej 2 Page Objecty (np. login_page.py, cart_page.py)"
    testy = list((WS / "tests").glob("test_*.py")) if (WS / "tests").exists() else []
    assert testy, "tests/: pliki test_*.py z testami E2E"
    liczba = sum(len(re.findall(r"^def test_\w+", p.read_text(encoding="utf-8"), re.M)) for p in testy)
    assert liczba >= 8, f"tests/: {liczba} testów — potrzeba co najmniej 8 (5 z tygodnia 8 + nowe: koszyk, zamówienie, przypadki negatywne)"
    r = tekst("README.md")
    assert "badge.svg" in r, "README.md: odznaka CI ![Testy](https://github.com/…/actions/workflows/tests.yml/badge.svg)"
    s = sekcje_md(r)
    jt = next((k for k in s if "jak testuj" in k), None)
    assert jt and len(" ".join(s[jt]).split()) >= 15, "README.md: sekcja „## Jak testuję” (co najmniej 15 słów: poziomy, narzędzia, jak uruchomić)"
