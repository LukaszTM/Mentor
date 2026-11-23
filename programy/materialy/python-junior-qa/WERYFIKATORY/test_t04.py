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


# Weryfikator tygodnia 4 — gałąź i pull request (TYDZIEN4.md), zapis.py, csv_odczyt.py, odzyskiwanie.md, magazyn_csv.py.
import csv as _csv

CSV_TEST = ("id,nazwa,kategoria,cena,ilosc\n"
            "1,Zeszyt A5 w kratkę,zeszyty,4.50,120\n"
            "3,Długopis niebieski,pisaki,2.30,300\n"
            "9,\"Papier ksero A4, 500 ark.\",papier,24.99,35\n"
            "17,Zszywki 1000 szt.,biuro,3.90,0\n"
            "14,Segregator A4,biuro,11.90,45\n")


def _csv_plik(tmp_path, tresc=CSV_TEST):
    p = tmp_path / "produkty.csv"
    p.write_text(tresc, encoding="utf-8")
    return p


def test_galaz_pr():
    repo()
    kod, galezie = git("branch", "-a", "--format=%(refname:short)")
    nazwy = [g.strip() for g in galezie.splitlines()]
    kandydaci = [g for g in nazwy if g.endswith("feature/tydzien4")]
    assert kandydaci, "Brak gałęzi feature/tydzien4 (lokalnie albo na GitHubie: git branch -a) — git switch -c feature/tydzien4"
    assert any(git("merge-base", "--is-ancestor", g, "HEAD")[0] == 0 for g in kandydaci), \
        "Gałąź feature/tydzien4 nie jest scalona z bieżącą gałęzią — Merge pull request na GitHubie, potem git switch main i git pull"
    kod, pliki = git("ls-files")
    assert "TYDZIEN4.md" in pliki.split(), "TYDZIEN4.md nie jest w repozytorium na gałęzi main"
    assert len([l for l in tekst("TYDZIEN4.md").splitlines() if l.strip()]) >= 3, "TYDZIEN4.md: co najmniej 3 niepuste linie (co zrobiłem w tygodniu 4)"


def test_zapis(tmp_path):
    m = modul("zapis")
    zap, wcz, dop = funkcja(m, "zapisz_liste"), funkcja(m, "wczytaj_liste"), funkcja(m, "dopisz")
    p = tmp_path / "produkty.txt"
    zap(["Zeszyt A5", "Długopis niebieski", "Gumka"], p)
    assert p.read_bytes().decode("utf-8").splitlines() == ["Zeszyt A5", "Długopis niebieski", "Gumka"], "zapisz_liste: każdy element w osobnej linii, kodowanie utf-8"
    dop(p, "Klej w sztyfcie")
    ok(wcz(p), ["Zeszyt A5", "Długopis niebieski", "Gumka", "Klej w sztyfcie"], "wczytaj_liste po dopisz")
    p.write_text("  Zeszyt  \n\nKlej\n\n", encoding="utf-8")
    ok(wcz(p), ["Zeszyt", "Klej"], "wczytaj_liste — bez spacji na brzegach i bez pustych linii")
    zap([], p)
    ok(wcz(p), [], "zapisz_liste([]) i wczytaj")
    ok(wcz(tmp_path / "nie_ma.txt"), [], "wczytaj_liste dla nieistniejącego pliku zwraca []")


def test_csv_odczyt(tmp_path):
    m = modul("csv_odczyt")
    wcz, sr, brak, wart = (funkcja(m, n) for n in ("wczytaj", "srednia_cena", "brak_na_stanie", "wartosc_magazynu"))
    p = wcz(_csv_plik(tmp_path))
    ok(len(p), 5, "liczba wczytanych produktów")
    ok(p[2]["nazwa"], "Papier ksero A4, 500 ark.", "nazwa z przecinkiem w cudzysłowie")
    assert isinstance(p[0]["cena"], float) and isinstance(p[0]["ilosc"], int), "wczytaj: cena jako float, ilosc jako int"
    ok(sr(p), 9.52, "srednia_cena (zaokrąglona do 2 miejsc)")
    ok(brak(p), ["Zszywki 1000 szt."], "brak_na_stanie")
    ok(wart(p), 2640.15, "wartosc_magazynu (suma cena × ilość, 2 miejsca)")
    ok(sr([]), 0, "srednia_cena([])")
    ok(wart([]), 0, "wartosc_magazynu([])")


def test_odzyskiwanie():
    s = sekcje_md(tekst("odzyskiwanie.md"))
    for slowo in ("restore", "stash", "revert"):
        klucz = next((k for k in s if slowo in k), None)
        assert klucz, f"odzyskiwanie.md: brak sekcji z „{slowo}” w nagłówku (np. „## git {slowo}”)"
        tresc = " ".join(s[klucz])
        assert len(tresc.split()) >= 15, f"odzyskiwanie.md: sekcja „{slowo}” — co najmniej 15 słów: kiedy używasz, co robi, czego nie cofniesz"
        assert f"git {slowo}" in tresc, f"odzyskiwanie.md: w sekcji „{slowo}” wpisz polecenie, którego użyłeś(-aś) (git {slowo} …)"


def test_magazyn_csv(tmp_path):
    m = modul("magazyn_csv")
    wcz, zap, dodaj, stat, szukaj = (funkcja(m, n) for n in ("wczytaj", "zapisz", "dodaj", "statystyki", "szukaj"))
    p = wcz(_csv_plik(tmp_path))
    st = stat(p)
    ok(st["liczba"], 5, "statystyki: liczba")
    ok(st["srednia_cena"], 9.52, "statystyki: srednia_cena")
    ok(st["najdrozszy"], "Papier ksero A4, 500 ark.", "statystyki: najdrozszy")
    ok(st["wartosc"], 2640.15, "statystyki: wartosc")
    ok(stat([]), {"liczba": 0, "srednia_cena": 0, "najdrozszy": None, "wartosc": 0}, "statystyki([])")
    dodaj(p, "Klej w sztyfcie", "akcesoria", 3.4, 110)
    ok(p[-1]["id"], 18, "id nowego produktu = największe id + 1")
    for zle, opis in ((("zeszyt a5 w kratkę", "zeszyty", 1.0, 1), "duplikat nazwy (bez względu na wielkość liter)"),
                      (("Nowy", "biuro", -1, 5), "cena ujemna"), (("Nowy", "biuro", 2.0, -1), "ilość ujemna"), (("", "biuro", 2.0, 1), "pusta nazwa")):
        rzuca(dodaj, p, *zle, opis=f"dodaj — {opis}")
    ok(len(p), 6, "liczba produktów po błędnych próbach dodania (bez zmian)")
    ok([x["nazwa"] for x in szukaj(p, "BIURO")], ["Zszywki 1000 szt.", "Segregator A4"], "szukaj(\"BIURO\") — po kategorii, bez wielkości liter")
    ok([x["nazwa"] for x in szukaj(p, "zeszyt")], ["Zeszyt A5 w kratkę"], "szukaj(\"zeszyt\") — po nazwie")
    ok(szukaj(p, "farby"), [], "szukaj(\"farby\")")
    cel = tmp_path / "zapis.csv"
    zap(p, cel)
    ok(wcz(cel), p, "zapisz → wczytaj daje te same dane")
    with open(cel, encoding="utf-8", newline="") as f:
        assert next(_csv.reader(f)) == ["id", "nazwa", "kategoria", "cena", "ilosc"], "zapisz: nagłówek id,nazwa,kategoria,cena,ilosc"
