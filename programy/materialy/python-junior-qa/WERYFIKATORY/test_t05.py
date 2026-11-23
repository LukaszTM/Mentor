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


# Weryfikator tygodnia 5 — produkt.py (klasa), menedżer w 3 plikach (main.py, zadania.py, plik.py), requirements.txt i .gitignore, api.py, raport_cen.py.
import ast as _ast
import csv as _csv
import json as _json
import threading as _threading
from http.server import BaseHTTPRequestHandler as _Handler, HTTPServer as _Server

PRODUKTY_API = [{"id": 1, "nazwa": "Zeszyt A5", "kategoria": "zeszyty", "cena": 4.5, "ilosc": 120},
                {"id": 9, "nazwa": "Papier ksero A4", "kategoria": "papier", "cena": 24.99, "ilosc": 35},
                {"id": 17, "nazwa": "Zszywki", "kategoria": "biuro", "cena": 3.9, "ilosc": 0},
                {"id": 16, "nazwa": "Zszywacz", "kategoria": "biuro", "cena": 19.9, "ilosc": 8}]


@pytest.fixture
def api():
    class H(_Handler):
        def do_GET(self):
            if self.path.startswith("/api/produkty"):
                kod, tresc = 200, _json.dumps(PRODUKTY_API).encode()
            elif self.path.startswith("/api/awaria"):
                kod, tresc = 500, b'{"blad": "awaria"}'
            else:
                kod, tresc = 404, b'{"blad": "nie ma"}'
            self.send_response(kod)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(tresc)

        def log_message(self, *a):
            pass
    srv = _Server(("127.0.0.1", 0), H)
    _threading.Thread(target=srv.serve_forever, daemon=True).start()
    yield f"http://127.0.0.1:{srv.server_port}"
    srv.shutdown()
    srv.server_close()


def test_produkt():
    m = modul("produkt")
    P = funkcja(m, "Produkt")
    p = P("Kredki", 12.9, 40)
    p.wydaj(15)
    p.przyjmij(5)
    ok(p.ilosc, 30, "ilosc po wydaj(15) i przyjmij(5)")
    ok(p.wartosc(), 387.0, "wartosc()")
    ok(str(p), "Kredki — 12.90 zł, 30 szt.", "str(produkt)")
    ok(P("Klej", 3.4).ilosc, 0, "domyślna ilość")
    for metoda, n in (("wydaj", 31), ("wydaj", 0), ("przyjmij", 0), ("przyjmij", -2)):
        rzuca(getattr(p, metoda), n, opis=f"{metoda}({n})")
    ok(p.ilosc, 30, "ilosc po nieudanych operacjach (bez zmian)")
    p.wydaj(30)
    ok(p.ilosc, 0, "wydanie całego stanu (wartość brzegowa)")
    rzuca(P, "Zły", -1, 5, opis="Produkt z ceną ujemną")
    a, b = P("A", 1.0, 1), P("B", 2.0, 2)
    a.przyjmij(1)
    ok(b.ilosc, 2, "dwa obiekty mają osobne ilości")


def test_menedzer_moduly(tmp_path):
    z = modul("zadania")
    pl = modul("plik")
    dodaj, oznacz, usun, otwarte = (funkcja(z, n) for n in ("dodaj", "oznacz", "usun", "otwarte"))
    lista = []
    dodaj(lista, " Zamówić papier ")
    dodaj(lista, "Policzyć zeszyty")
    oznacz(lista, 2)
    ok(otwarte(lista), ["Zamówić papier"], "otwarte")
    rzuca(dodaj, lista, "", opis="dodaj pusty tytuł")
    rzuca(oznacz, lista, 3, opis="oznacz(…, 3) przy 2 zadaniach")
    ok(usun(lista, 1), "Zamówić papier", "usun zwraca tytuł")
    sc = tmp_path / "zadania.json"
    funkcja(pl, "zapisz")(lista, sc)
    ok(funkcja(pl, "wczytaj")(sc), lista, "plik.zapisz → plik.wczytaj")
    ok(funkcja(pl, "wczytaj")(tmp_path / "brak.json"), [], "wczytaj nieistniejący plik")
    assert "ą" in sc.read_text(encoding="utf-8") or "ę" in sc.read_text(encoding="utf-8") or "Policzyć" in sc.read_text(encoding="utf-8"), \
        "plik.zapisz: polskie litery czytelne w pliku (json.dump(…, ensure_ascii=False))"
    main = tekst("main.py")
    assert ("import zadania" in main or "from zadania import" in main) and ("import plik" in main or "from plik import" in main), \
        "main.py ma importować moduły zadania i plik"
    assert "def dodaj" not in main and "def wczytaj" not in main, "main.py nie powinien powtarzać funkcji z zadania.py/plik.py — tylko menu"
    modul("main")  # import nie może uruchamiać menu (input) — blok if __name__ == "__main__":
    kod, out = uruchom("main.py", "1\nZamówić papier\n3\n0\n")
    bez_bledu(kod, out, "menu: dodaj, lista, koniec")
    zawiera(out, "Zamówić papier", dane="menu main.py: 1 → tytuł → 3 → 0")


def test_srodowisko_projektu():
    req = [l.strip() for l in tekst("requirements.txt").splitlines() if l.strip() and not l.startswith("#")]
    assert any(re.match(r"requests==\d", l, re.I) for l in req), "requirements.txt: brak linii requests==wersja (python -m pip freeze > requirements.txt)"
    gi = tekst(".gitignore")
    for wzor in (".venv", "__pycache__", ".env"):
        assert wzor in gi, f".gitignore: brak wpisu {wzor}"
    if (WS / ".git").exists():
        kod, pliki = git("ls-files")
        assert not any(x.startswith(".venv/") for x in pliki.split()), ".venv jest w repozytorium — git rm -r --cached .venv i commit"


def test_api(api):
    m = modul("api")
    pob, tanie = funkcja(m, "pobierz_produkty"), funkcja(m, "tanie")
    p = pob(api + "/api/produkty")
    ok(len(p), 4, "pobierz_produkty — liczba produktów")
    ok(p[0]["nazwa"], "Zeszyt A5", "pobierz_produkty — pierwszy produkt")
    for zly in ("/api/awaria", "/api/nie-ma"):
        try:
            pob(api + zly)
        except RuntimeError as e:
            assert ("500" if "awaria" in zly else "404") in str(e), f"RuntimeError dla {zly} ma zawierać kod odpowiedzi; jest: {e}"
        except Exception as e:  # noqa: BLE001
            pytest.fail(f"pobierz_produkty({zly}) rzuciła {type(e).__name__} — oczekiwano RuntimeError z kodem odpowiedzi")
        else:
            pytest.fail(f"pobierz_produkty({zly}) nie zgłosiła błędu dla kodu innego niż 200")
    rzuca(pob, "http://127.0.0.1:9/api/produkty", wyjatek=RuntimeError, opis="pobierz_produkty — serwer niedostępny (RuntimeError zamiast ConnectionError)")
    ok(tanie(p, 20), ["Zszywki", "Zeszyt A5", "Zszywacz"], "tanie(produkty, 20) — nazwy z ceną < 20, rosnąco po cenie")
    ok(tanie(p, 1), [], "tanie(produkty, 1)")
    get = [w for w in _ast.walk(drzewo("api.py")) if isinstance(w, _ast.Call) and getattr(w.func, "attr", "") == "get" and getattr(w.func.value, "id", "") == "requests"]
    assert get and all(any(k.arg == "timeout" for k in w.keywords) for w in get), "api.py: requests.get(…) zawsze z timeout=…"


def test_raport_cen(tmp_path):
    m = modul("raport_cen")
    zap, ostrz = funkcja(m, "zapisz_raport"), funkcja(m, "ostrzezenia")
    cel = tmp_path / "raport.csv"
    ok(zap(PRODUKTY_API, cel, "2026-11-23"), 4, "zapisz_raport zwraca liczbę zapisanych wierszy")
    with open(cel, encoding="utf-8", newline="") as f:
        w = list(_csv.reader(f))
    ok(w[0], ["data", "nazwa", "kategoria", "cena"], "nagłówek raportu")
    ok([x[1] for x in w[1:]], ["Papier ksero A4", "Zszywacz", "Zeszyt A5", "Zszywki"], "kolejność: malejąco po cenie")
    ok(w[1][0], "2026-11-23", "data w każdym wierszu")
    ok(float(w[1][3]), 24.99, "cena w raporcie")
    ok(ostrz(PRODUKTY_API), ["Zszywacz", "Zszywki"], "ostrzezenia — ilość < 10, alfabetycznie")
    ok(ostrz(PRODUKTY_API, 1), ["Zszywki"], "ostrzezenia(…, prog=1)")
    ok(zap([], tmp_path / "pusty.csv", "2026-11-23"), 0, "raport z pustej listy")
