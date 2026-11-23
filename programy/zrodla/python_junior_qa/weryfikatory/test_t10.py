# wzorce: baza.py, magazyn.py
# Weryfikator tygodnia 10 — projekt Magazyn: PLAN.md, baza.py (SQLite), magazyn.py (logika), testy z bazą tymczasową, rdzeń z menu.
import ast as _ast
import sqlite3 as _sqlite3


def test_plan():
    s = sekcje_md(tekst("PLAN.md"))
    for k in ("cel", "zakres", "poza zakresem", "struktura", "kolejnosc", "ryzyka"):
        klucz = next((x for x in s if x.startswith(k) or (k == "zakres" and x == "zakres")), None)
        assert klucz, f"PLAN.md: brak sekcji „## {k.capitalize()}”"
        assert s[klucz], f"PLAN.md: sekcja „{k}” jest pusta"
    assert sum(1 for l in s[next(x for x in s if x.startswith('kolejnosc'))] if re.match(r"^(\d+\.|-)", l)) >= 4, "PLAN.md: kolejność — co najmniej 4 kroki"


def _baza(tmp_path):
    b = modul("baza")
    con = funkcja(b, "utworz_baze")(tmp_path / "test.db")
    return b, con


def test_baza(tmp_path):
    b, con = _baza(tmp_path)
    dodaj, pobierz, zmien, usun = (funkcja(b, n) for n in ("dodaj_produkt", "pobierz_produkty", "zmien_ilosc", "usun_produkt"))
    a = dodaj(con, "Zeszyt A5", "zeszyty", 4.5, 120)
    s = dodaj(con, "Segregator A4", "biuro", 11.9)
    assert isinstance(a, int) and a != s, "dodaj_produkt zwraca id nowego produktu (int)"
    p = pobierz(con)
    ok([x["nazwa"] for x in p], ["Segregator A4", "Zeszyt A5"], "pobierz_produkty — alfabetycznie po nazwie")
    ok(p[0]["ilosc"], 0, "domyślna ilość 0")
    ok([x["nazwa"] for x in pobierz(con, "biuro")], ["Segregator A4"], "pobierz_produkty(con, \"biuro\")")
    ok(pobierz(con, "x' OR '1'='1"), [], "pobierz_produkty z próbą SQL injection — parametry ?")
    ok(zmien(con, a, -20), 100, "zmien_ilosc(con, id, -20) zwraca nowy stan")
    rzuca(zmien, con, a, -101, opis="zmien_ilosc poniżej zera")
    rzuca(zmien, con, 999, 5, opis="zmien_ilosc nieistniejącego produktu")
    rzuca(dodaj, con, "Zeszyt A5", "zeszyty", 1.0, wyjatek=(ValueError, _sqlite3.IntegrityError), opis="duplikat nazwy")
    usun(con, s)
    ok([x["nazwa"] for x in pobierz(con)], ["Zeszyt A5"], "po usun_produkt")
    rzuca(usun, con, s, opis="usun_produkt nieistniejącego")
    con2 = funkcja(b, "utworz_baze")(tmp_path / "test.db")
    ok([x["ilosc"] for x in funkcja(b, "pobierz_produkty")(con2)], [100], "dane zapisane w pliku bazy (commit) — widoczne po ponownym połączeniu")
    for w in _ast.walk(drzewo("baza.py")):
        if isinstance(w, _ast.Call) and getattr(w.func, "attr", "") in ("execute", "executemany") and w.args and isinstance(w.args[0], _ast.JoinedStr):
            pytest.fail("baza.py: f-string w execute() — zapytania tylko z parametrami ? (SQL injection)")


def test_magazyn(tmp_path):
    b, con = _baza(tmp_path)
    m = modul("magazyn")
    prz, wyd, hist, wart = (funkcja(m, n) for n in ("przyjecie", "wydanie", "historia", "wartosc_magazynu"))
    pid = funkcja(b, "dodaj_produkt")(con, "Klej w sztyfcie", "akcesoria", 3.4, 0)
    ok(prz(con, pid, 50, "2026-11-20"), 50, "przyjecie zwraca nowy stan")
    ok(wyd(con, pid, 20, "2026-11-22"), 30, "wydanie zwraca nowy stan")
    ok(wyd(con, pid, 30, "2026-11-23"), 0, "wydanie całego stanu (wartość brzegowa)")
    rzuca(wyd, con, pid, 1, "2026-11-23", opis="wydanie ponad stan")
    rzuca(prz, con, pid, 0, "2026-11-23", opis="przyjęcie 0 sztuk")
    rzuca(wyd, con, pid, -5, "2026-11-23", opis="wydanie ujemne")
    prz(con, pid, 5, "2026-11-21")
    ok(hist(con, pid), [("2026-11-20", "przyjecie", 50), ("2026-11-21", "przyjecie", 5), ("2026-11-22", "wydanie", 20), ("2026-11-23", "wydanie", 30)],
       "historia — (data, typ, ilość) rosnąco po dacie, bez nieudanych operacji")
    ok(wart(con), 17.0, "wartosc_magazynu (5 szt. × 3.40)")


def test_testy_bazy():
    t = tekst("test_baza.py")
    assert "tmp_path" in t or ":memory:" in t, "test_baza.py: baza tymczasowa (fixtura z tmp_path albo \":memory:\") — testy nie dotykają magazyn.db"
    assert "@pytest.fixture" in t, "test_baza.py: fixtura tworząca świeżą bazę dla każdego testu"
    import shutil as _sh
    import tempfile as _tf
    with _tf.TemporaryDirectory(prefix="mut10_") as td:
        td = Path(td)
        (td / "test_baza.py").write_text(t, encoding="utf-8")
        zmiany = [("magazyn.py", "wydanie całego stanu blokowane", "if ilosc <= 0 or ilosc > stan ", "if ilosc <= 0 or ilosc >= stan "),
                  ("magazyn.py", "historia bez sortowania po dacie", "ORDER BY data, id", "ORDER BY id"),
                  ("baza.py", "zmiana ilości bez kontroli zera", "    if nowa < 0:\n        raise ValueError", "    if False:\n        raise ValueError"),
                  ("baza.py", "filtr kategorii ignorowany", "WHERE kategoria = ? ORDER BY nazwa", "WHERE ? IS NOT NULL ORDER BY nazwa")]
        for plik_, kod in WZORZEC.items():
            (td / plik_).write_text(kod, encoding="utf-8")
        kod, out = pytest_ucznia(td, "test_baza.py")
        assert kod == 0, f"test_baza.py nie przechodzi na wzorcowych baza.py i magazyn.py:\n{out[-1500:]}"
        m = re.search(r"(\d+) passed", out)
        assert m and int(m.group(1)) >= 8, "test_baza.py: co najmniej 8 testów"
        for plik_, opis, stary, nowy in zmiany:
            assert stary in WZORZEC[plik_], f"(błąd weryfikatora) {stary!r}"
            (td / plik_).write_text(WZORZEC[plik_].replace(stary, nowy, 1), encoding="utf-8")
            _sh.rmtree(td / "__pycache__", ignore_errors=True)
            kod, out = pytest_ucznia(td, "test_baza.py")
            assert kod != 0, f"test_baza.py nie wykrył błędu: {opis}"
            (td / plik_).write_text(WZORZEC[plik_], encoding="utf-8")


def test_rdzen(tmp_path):
    import shutil as _sh
    kod, out = uruchom("menu_magazyn.py", "1\nZeszyt A5\nzeszyty\n4.50\n2\n1\n30\n4\n0\n", env={"MAGAZYN_DB": str(tmp_path / "menu.db")})
    bez_bledu(kod, out, "menu: dodaj produkt, przyjęcie, lista, koniec")
    zawiera(out, "Zeszyt A5", "30", dane="1 dodaj → 2 przyjęcie 30 szt. → 4 lista → 0")
    kod, out = uruchom("menu_magazyn.py", "3\n1\n500\n0\n", env={"MAGAZYN_DB": str(tmp_path / "menu.db")})
    bez_bledu(kod, out, "wydanie ponad stan")
    zawiera(out, "Błąd", dane="3 wydanie 500 szt. (więcej niż stan) → komunikat, program działa dalej")
    liczba = 0
    for p in list(WS.glob("test_*.py")) + list((WS / "tests").glob("test_*.py")):
        liczba += len(re.findall(r"^def test_\w+", p.read_text(encoding="utf-8", errors="ignore"), re.M))
    assert liczba >= 20, f"W projekcie jest {liczba} testów — rdzeń projektu ma mieć co najmniej 20"
