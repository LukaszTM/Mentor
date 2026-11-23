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


# Weryfikator tygodnia 6 — do_poprawy.py (debugowanie), notatki_projekt.md, bmi.py po refaktoryzacji, README.md, porządek w repozytorium.
import ast as _ast


def test_debugowanie():
    m = modul("do_poprawy")
    sr, razem, kat = funkcja(m, "srednia_ceny"), funkcja(m, "razem_koszyka"), funkcja(m, "kategoria_ceny")
    ok(sr([4.0, 2.0, 6.0]), 4.0, "srednia_ceny([4.0, 2.0, 6.0]) — błąd 1: pierwszy element pomijany")
    ok(sr([10.0]), 10.0, "srednia_ceny([10.0])")
    ok(sr([]), 0, "srednia_ceny([]) — pusta lista")
    ok(razem([(2.0, 3), (5.0, 2)]), 16.0, "razem_koszyka — błąd 2: suma nadpisywana zamiast dodawana")
    ok(razem([]), 0, "razem_koszyka([])")
    for cena, w in ((5, "tani"), (9.99, "tani"), (10, "średni"), (49.99, "średni"), (50, "drogi"), (500, "drogi")):
        ok(kat(cena), w, f"kategoria_ceny({cena}) — błąd 3: kolejność progów")


def test_notatki_projekt():
    s = sekcje_md(tekst("notatki_projekt.md"))
    for f in ("readme.md", "app.py", "baza.py", "raport.py"):
        klucz = next((k for k in s if f.replace(".", "") in k.replace(".", "")), None)
        assert klucz, f"notatki_projekt.md: brak sekcji dla pliku {f} (np. „## {f}”)"
        assert len(" ".join(s[klucz]).split()) >= 10, f"notatki_projekt.md: sekcja {f} — co najmniej 10 słów: odpowiedzialność pliku i najważniejsze funkcje"
    pyt = next((k for k in s if "pytania" in k), None)
    assert pyt and any(l.startswith(("-", "*")) for l in s[pyt]), "notatki_projekt.md: sekcja „## Pytania” z co najmniej jednym pytaniem w formie listy"


def test_bmi_refaktoryzacja():
    m = modul("bmi")
    obl, kat = funkcja(m, "oblicz_bmi"), funkcja(m, "kategoria")
    ok(obl(81, 1.80), 25.0, "oblicz_bmi(81, 1.80)")
    ok(obl(50, 1.70), 17.3, "oblicz_bmi(50, 1.70)")
    for zle in ((0, 1.7), (70, 0), (-5, 1.7), (80, 180)):
        rzuca(obl, *zle, opis=f"oblicz_bmi{zle}")
    for bmi, w in ((18.4, "niedowaga"), (18.5, "norma"), (24.9, "norma"), (25, "nadwaga"), (29.9, "nadwaga"), (30, "otyłość")):
        ok(kat(bmi), w, f"kategoria({bmi})")
    for n in ("oblicz_bmi", "kategoria"):
        assert (getattr(m, n).__doc__ or "").strip(), f"bmi.py: funkcja {n} bez docstringu"
    stale = [w.targets[0].id for w in drzewo("bmi.py").body if isinstance(w, _ast.Assign) and isinstance(w.targets[0], _ast.Name) and w.targets[0].id.isupper()]
    assert stale, "bmi.py: progi jako stałe na górze pliku (np. PROG_NADWAGI = 25) zamiast liczb w warunkach"


def test_readme():
    t = tekst("README.md")
    assert t.lstrip().startswith("# "), "README.md: pierwsza linia to tytuł „# …”"
    s = sekcje_md(t)
    proj = next((k for k in s if "projekty" in k), None)
    assert proj, "README.md: brak sekcji „## Projekty”"
    wiersze = [l for l in s[proj] if l.startswith("|") and not set(l) <= set("|-: ")]
    assert len(wiersze) >= 5, f"README.md: tabela projektów — nagłówek + co najmniej 4 projekty (jest {max(len(wiersze) - 1, 0)})"
    uru = next((k for k in s if "jak uruchomic" in k), None)
    assert uru, "README.md: brak sekcji „## Jak uruchomić”"
    assert "```" in t.split("##", 1)[-1], "README.md: polecenia uruchomienia w bloku kodu (```)"


ZLE_OPISY = {"zmiany", "asdf", "final", "final2", "x", "update", "commit", "fix", "poprawki", "test"}


def test_porzadek_repo():
    gi = tekst(".gitignore")
    for w in (".venv", "__pycache__", ".env"):
        assert w in gi, f".gitignore: brak wpisu {w}"
    repo()
    kod, pliki = git("ls-files")
    sledzone = pliki.split()
    zle = [p for p in sledzone if p.startswith(".venv/") or "__pycache__/" in p or p.endswith(".pyc") or p.split("/")[-1] == ".env"]
    assert not zle, f"W repozytorium są pliki, które powinny być ignorowane: {zle[:5]} — git rm -r --cached …"
    wzor = re.compile(r"(api_key|apikey|token|haslo|password|secret)\s*=\s*['\"][^'\"]{6,}['\"]", re.I)
    for p in sledzone:
        if p.endswith((".py", ".md", ".txt", ".json", ".yml", ".yaml", ".cfg", ".ini")) and (WS / p).is_file():
            assert not wzor.search((WS / p).read_text(encoding="utf-8", errors="ignore")), f"{p}: wygląda na sekret (hasło/klucz) zapisany w kodzie — usuń, unieważnij, przenieś do .env"
    kod, log = git("log", "--format=%s")
    opisy = [l.strip() for l in log.splitlines() if l.strip()]
    assert len(opisy) >= 5, f"Historia ma {len(opisy)} commitów — porządkuj małymi krokami (co najmniej 5 commitów)"
    slabe = [o for o in opisy if o.lower() in ZLE_OPISY]
    assert len(slabe) <= len(opisy) // 5, f"Za dużo commitów z opisem bez treści ({len(slabe)}): {slabe[:5]} — opisuj, co zmieniasz („Dodaj…”, „Popraw…”)"
