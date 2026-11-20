# Weryfikator tygodnia 8 — testy ucznia (mutanty), debug_rezerwacje.py, refaktoryzacja raport_obroty.py.
import ast
import datetime as _dt
import subprocess
import tempfile

CENNIK = '''
CENY = {"Lipowy": (180, 140), "Dębowy": (160, 120), "Klonowy": (200, 150)}
SEZON_WYSOKI = (6, 7, 8, 12)


def cena_pokoju(pokoj, miesiac):
    if pokoj not in CENY:
        raise ValueError("nieznany pokój")
    if miesiac not in range(1, 13):
        raise ValueError("miesiąc 1–12")
    wysoka, niska = CENY[pokoj]
    return wysoka if miesiac in SEZON_WYSOKI else niska


def oplata_klimatyczna(dorosli, noce, dzieci=0):
    if dorosli < 1 or noce < 1 or dzieci < 0:
        raise ValueError("złe dane")
    return round(dorosli * noce * 2.5, 2)
'''
MUTANTY = {
    "sezon (grudzień jako sezon niski)": CENNIK.replace("SEZON_WYSOKI = (6, 7, 8, 12)", "SEZON_WYSOKI = (6, 7, 8)"),
    "dzieci (dzieci płacą opłatę)": CENNIK.replace("dorosli * noce * 2.5", "(dorosli + dzieci) * noce * 2.5"),
    "pokój (nieznany pokój bez błędu)": CENNIK.replace('    if pokoj not in CENY:\n        raise ValueError("nieznany pokój")\n', '    if pokoj not in CENY:\n        return 0\n'),
}


def _uruchom_testy_ucznia(kod_cennika):
    testy = tekst("test_cennik.py")
    with tempfile.TemporaryDirectory() as td:
        Path(td, "cennik.py").write_text(kod_cennika, encoding="utf-8")
        Path(td, "test_cennik.py").write_text(testy, encoding="utf-8")
        p = subprocess.run([sys.executable, "-X", "utf8", "-m", "pytest", "-q", "-p", "no:cacheprovider", "-o", "addopts=", "test_cennik.py"],
                           cwd=td, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=120)
        return p.returncode, p.stdout + p.stderr


def test_cennik_testy_przechodza_na_dobrym_kodzie():
    kod, out = _uruchom_testy_ucznia(CENNIK)
    assert kod == 0, "Twoje testy NIE przechodzą na poprawnym cenniku (specyfikacja z docstringu) — sprawdź oczekiwane wartości:\n" + out[-1500:]
    m = re.search(r"(\d+) passed", out)
    assert m and int(m.group(1)) >= 6, f"Za mało testów: {m.group(1) if m else 0} (potrzeba ≥ 6)"


def test_cennik_testy_lapia_mutanty():
    przezyly = [n for n, kod in MUTANTY.items() if _uruchom_testy_ucznia(kod)[0] == 0]
    assert not przezyly, "Te mutanty (celowo zepsute cenniki) przeszły Twoje testy — dopisz przypadki, które je wykryją: " + "; ".join(przezyly)


def _dbg():
    m = modul("debug_rezerwacje")
    return funkcja(m, "parsuj_linie"), funkcja(m, "wczytaj_rezerwacje"), funkcja(m, "noce_razem")


def test_debug_daty():
    parsuj, _, _ = _dbg()
    r = parsuj("Anna;Lipowy;05.07.2026;08.07.2026")
    ok(r["od"], _dt.date(2026, 7, 5), "parsuj_linie: 05.07.2026 to 5 lipca (dzień.miesiąc.rok)")
    r = parsuj("  Piotr ; Dębowy ; 20.12.2026 ; 23.12.2026 ")
    ok((r["gosc"], r["pokoj"], r["do"]), ("Piotr", "Dębowy", _dt.date(2026, 12, 23)), "parsuj_linie z dniem > 12 i spacjami")
    rzuca(parsuj, "Anna;Lipowy;05.07.2026", opis="parsuj_linie z 3 polami")


def test_debug_lista_nie_jest_wspolna():
    _, wczytaj, _ = _dbg()
    a = wczytaj(["Anna;Lipowy;05.07.2026;08.07.2026"])
    b = wczytaj(["Ewa;Klonowy;01.08.2026;03.08.2026", "", "   "])
    ok(len(a), 1, "pierwsze wczytanie: liczba rezerwacji")
    ok(len(b), 1, "drugie wczytanie: liczba rezerwacji (lista nie może zawierać danych z pierwszego — wartość domyślna wynik=[])")


def test_debug_noce():
    _, wczytaj, noce = _dbg()
    rez = wczytaj(["Anna;Lipowy;05.07.2026;08.07.2026", "Ewa;Klonowy;30.12.2026;02.01.2027"])
    ok(noce(rez), 6, "noce_razem: 3 + 3 noce")
    ok(noce([]), 0, "noce_razem([])")


R8 = [{"miesiac": 7, "noce": 3, "osoby": 2}, {"miesiac": 7, "noce": 7, "osoby": 1}, {"miesiac": 3, "noce": 2, "osoby": 2},
      {"miesiac": 12, "noce": 10, "osoby": 4}, {"miesiac": 3, "noce": 8, "osoby": 1}]


def test_refaktor_zachowanie():
    m = modul("raport_obroty")
    ok(funkcja(m, "przychod")(R8), 8477.0, "przychod(R)")
    ok(funkcja(m, "przychod")([]), 0, "przychod([])")
    ok(funkcja(m, "raport_tekstowy")(R8), "Marzec: 1 232,00 zł\nLipiec: 1 845,00 zł\nGrudzień: 5 400,00 zł\nRazem: 8 477,00 zł", "raport_tekstowy(R)")
    ok(funkcja(m, "raport_tekstowy")([{"miesiac": 1, "noce": 1, "osoby": 1}]), "Styczeń: 110,00 zł\nRazem: 110,00 zł", "raport_tekstowy(1 rezerwacja)")


def test_refaktor_struktura():
    drzewo = ast.parse(tekst("raport_obroty.py"))
    funkcje = [n for n in ast.walk(drzewo) if isinstance(n, ast.FunctionDef)]
    assert len(funkcje) >= 4, f"raport_obroty.py ma {len(funkcje)} funkcje — wydziel kroki (np. cena_nocy, koszt, formatowanie kwoty): potrzeba ≥ 4"
    for f in funkcje:
        dl = f.end_lineno - f.lineno + 1
        assert dl <= 20, f"funkcja {f.name} ma {dl} linii — podziel ją (≤ 20)"
        assert ast.get_docstring(f), f"funkcja {f.name} nie ma docstringu (jednozdaniowy opis w \"\"\"…\"\"\")"
    for liczba in (150, 110, 0.9):
        n = sum(1 for x in ast.walk(drzewo) if isinstance(x, ast.Constant) and type(x.value) in (int, float) and x.value == liczba and not isinstance(x.value, bool))
        assert n <= 1, f"liczba {liczba} występuje w kodzie {n} razy — zamień ją na stałą z nazwą"
