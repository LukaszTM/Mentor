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


# Weryfikator tygodnia 11 — aplikacja Flask projektu Magazyn (test_client na bazie tymczasowej), testy E2E w POM, uruchomienie jedną komendą i CI.


@pytest.fixture
def apka(tmp_path):
    a = modul("app")
    b = modul("baza")
    db = tmp_path / "web.db"
    app = funkcja(a, "create_app")(db)
    app.config["TESTING"] = True
    con = b.utworz_baze(db)
    return app.test_client(), b, con, db


def _html(o):
    return o.get_data(as_text=True)


def test_lista(apka):
    k, b, con, _ = apka
    b.dodaj_produkt(con, "Zeszyt A5", "zeszyty", 4.5, 120)
    b.dodaj_produkt(con, "Segregator A4", "biuro", 11.9, 45)
    o = k.get("/")
    assert o.status_code == 200, f"GET / → {o.status_code}"
    h = _html(o)
    for f in ("Zeszyt A5", "Segregator A4", "120", "4,50"):
        assert f in h, f"strona główna: brak „{f}” (nazwa, ilość, cena z przecinkiem i 2 miejscami)"
    assert h.index("Segregator A4") < h.index("Zeszyt A5"), "strona główna: produkty alfabetycznie"


def test_formularz(apka):
    k, b, con, _ = apka
    assert k.get("/dodaj").status_code == 200, "GET /dodaj → formularz"
    o = k.post("/dodaj", data={"nazwa": "Klej w sztyfcie", "kategoria": "akcesoria", "cena": "3,40", "ilosc": "10"})
    assert o.status_code == 302, f"poprawny formularz → przekierowanie (302), jest {o.status_code}"
    assert "Klej w sztyfcie" in _html(k.get("/")), "po dodaniu produkt jest na liście"
    zle = [({"nazwa": "", "kategoria": "biuro", "cena": "2", "ilosc": "1"}, "nazw"),
           ({"nazwa": "X1", "kategoria": "biuro", "cena": "abc", "ilosc": "1"}, "cen"),
           ({"nazwa": "X2", "kategoria": "biuro", "cena": "-1", "ilosc": "1"}, "cen"),
           ({"nazwa": "X3", "kategoria": "biuro", "cena": "2", "ilosc": "1.5"}, "ilo"),
           ({"nazwa": "X4", "kategoria": "", "cena": "2", "ilosc": "1"}, "kategori"),
           ({"nazwa": "klej w sztyfcie", "kategoria": "akcesoria", "cena": "2", "ilosc": "1"}, "istnieje")]
    for dane, slowo in zle:
        o = k.post("/dodaj", data=dane)
        assert o.status_code == 400, f"POST /dodaj {dane} → oczekiwano 400, jest {o.status_code}"
        assert slowo in norm(_html(o)), f"POST /dodaj {dane}: komunikat dla użytkownika ze słowem „{slowo}…”"
    assert len(b.pobierz_produkty(con)) == 1, "błędne formularze nie mogą dodać produktu do bazy"
    o = k.post("/dodaj", data={"nazwa": "<script>alert(1)</script>", "kategoria": "", "cena": "1", "ilosc": "1"})
    assert "<script>alert(1)</script>" not in _html(o), "wpisany tekst wraca na stronę zabezpieczony (Jinja {{ }}) — bez wstrzykniętego <script>"


def test_historia(apka):
    k, b, con, _ = apka
    m = modul("magazyn")
    pid = b.dodaj_produkt(con, "Zszywacz", "biuro", 19.9, 0)
    m.przyjecie(con, pid, 15, "2026-11-20")
    m.wydanie(con, pid, 5, "2026-11-22")
    o = k.get(f"/produkt/{pid}")
    assert o.status_code == 200, f"GET /produkt/{pid} → {o.status_code}"
    h = _html(o)
    for f in ("Zszywacz", "2026-11-20", "2026-11-22", "15", "5"):
        assert f in h, f"strona produktu: brak „{f}” (nazwa i historia operacji)"
    assert h.index("2026-11-20") < h.index("2026-11-22"), "historia rosnąco po dacie"
    assert k.get("/produkt/9999").status_code == 404, "nieistniejący produkt → 404"


def test_e2e_pom():
    nazwa = "test_e2e.py" if (WS / "test_e2e.py").exists() else "tests/test_e2e.py"
    t = tekst(nazwa)
    assert len(re.findall(r"^def test_\w+", t, re.M)) >= 3, f"{nazwa}: co najmniej 3 testy E2E (lista, dodanie formularzem, historia)"
    assert re.search(r"from pages[\w.]* import|import pages", t), f"{nazwa}: testy używają Page Objectów z pages/"
    assert "sleep" not in t, f"{nazwa}: bez time.sleep"
    cf = "".join(p.read_text(encoding="utf-8") for p in (WS / "conftest.py", WS / "tests" / "conftest.py") if p.exists())
    assert "make_server" in cf or "serwer" in cf, "conftest.py: fixtura uruchamiająca aplikację na serwerze testowym (werkzeug make_server w wątku)"
    assert "create_app" in cf, "conftest.py: serwer testowy z create_app(ścieżka bazy tymczasowej)"


def test_jedna_komenda_i_ci():
    t = tekst("app.py")
    assert re.search(r"if __name__ == ['\"]__main__['\"]:", t) and ".run(" in t, "app.py: uruchomienie jedną komendą — app.run(…) w bloku __main__"
    assert "debug=True" not in t.split("__main__")[-1] or "environ" in t, "app.py: debug=True tylko lokalnie (np. zależnie od zmiennej środowiskowej)"
    r = tekst("README.md")
    assert "python app.py" in r, "README.md: polecenie uruchomienia `python app.py`"
    wf = sorted((WS / ".github" / "workflows").glob("*.y*ml"))
    assert wf and "pytest" in wf[0].read_text(encoding="utf-8"), "workflow CI uruchamia pytest"
