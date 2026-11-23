# wzorce: funkcje.py, bmi.py, zadania.py, magazyn_csv.py, magazyn_ukryty.py
# Weryfikator tygodnia 7 — testy ucznia uruchamiane na kodzie wzorcowym (muszą przejść) i na mutantach (muszą paść).


def _test_funkcji(plik_testu, nazwa):
    t = tekst(plik_testu)
    return len(re.findall(r"^\s*def test_\w+", t, re.M)), t


def test_testy_funkcji():
    mutanty("test_funkcje.py", "funkcje", WZORZEC["funkcje.py"], [
        ("pole liczone jako a + b", "return a * b", "return a + b"),
        ("czy_parzysta odwrócona", "return n % 2 == 0", "return n % 2 == 1"),
        ("maksimum zwraca pierwszy element", "        if x > najwieksza:\n            najwieksza = x\n", "        pass\n"),
        ("odwroc zwraca napis bez zmian", "return napis[::-1]", "return napis"),
        ("silnia(0) = 0", "    wynik = 1\n", "    wynik = 1 if n else 0\n"),
    ], min_testow=5)


def test_parametrize_bmi():
    n, t = _test_funkcji("test_bmi.py", "bmi")
    assert "@pytest.mark.parametrize" in t, "test_bmi.py: użyj @pytest.mark.parametrize (jeden test, wiele przypadków)"
    mutanty("test_bmi.py", "bmi", WZORZEC["bmi.py"], [
        ("granica niedowagi: 18.5 zaliczane do niedowagi", "if bmi < PROG_NIEDOWAGI:", "if bmi <= PROG_NIEDOWAGI:"),
        ("granica nadwagi: 25 zaliczane do normy", "if bmi < PROG_NADWAGI:", "if bmi <= PROG_NADWAGI:"),
        ("granica otyłości: 30 zaliczane do nadwagi", "if bmi < PROG_OTYLOSCI:", "if bmi <= PROG_OTYLOSCI:"),
    ], min_testow=6)


def test_fixture_menedzer():
    n, t = _test_funkcji("test_menedzer.py", "zadania")
    assert "@pytest.fixture" in t, "test_menedzer.py: przygotuj dane fixturą (@pytest.fixture)"
    fx = re.search(r"@pytest\.fixture[^\n]*\ndef (\w+)", t)
    assert fx, "test_menedzer.py: nie znaleziono definicji fixtury pod @pytest.fixture"
    uzycia = len(re.findall(rf"def test_\w+\([^)]*\b{fx.group(1)}\b", t))
    assert uzycia >= 4, f"test_menedzer.py: fixtura {fx.group(1)} użyta w {uzycia} testach — potrzeba co najmniej 4"
    mutanty("test_menedzer.py", "zadania", WZORZEC["zadania.py"], [
        ("dodaj nie usuwa spacji z tytułu", "    tytul = tytul.strip()\n", ""),
        ("oznacz oznacza złe zadanie (pomyłka o jeden)", 'zadania[nr - 1]["zrobione"] = True', 'zadania[nr % len(zadania)]["zrobione"] = True'),
        ("otwarte zwraca też zrobione", 'if not z["zrobione"]]', "]"),
        ("numer 0 akceptowany", "if not 1 <= nr <= len(zadania):", "if not 0 <= nr <= len(zadania):"),
    ], min_testow=4)


def test_ukryty_blad():
    m = modul("magazyn_ukryty")
    wyd = funkcja(m, "wydaj")
    ok(wyd(10, 10), 0, "Twoja poprawiona wersja: wydaj(10, 10) — wydanie całego stanu")
    ok(wyd(10, 3), 7, "wydaj(10, 3)")
    rzuca(wyd, 10, 11, opis="wydaj(10, 11)")
    rzuca(wyd, 10, 0, opis="wydaj(10, 0)")
    mutanty("test_ukryty.py", "magazyn_ukryty", WZORZEC["magazyn_ukryty.py"], [
        ("ukryty błąd z paczki: wydanie całego stanu blokowane", "if n <= 0 or n > stan:", "if n <= 0 or n >= stan:"),
    ], min_testow=1)


def test_testy_magazynu():
    n, t = _test_funkcji("test_magazyn.py", "magazyn_csv")
    assert n >= 15, f"test_magazyn.py: {n} testów — potrzeba co najmniej 15 (z przypadkami brzegowymi i negatywnymi)"
    assert "pytest.raises" in t, "test_magazyn.py: sprawdź też złe dane (pytest.raises)"
    mutanty("test_magazyn.py", "magazyn_csv", WZORZEC["magazyn_csv.py"], [
        ("duplikat nazwy z inną wielkością liter przechodzi", 'if any(p["nazwa"].lower() == nazwa.lower() for p in produkty):', 'if any(p["nazwa"] == nazwa for p in produkty):'),
        ("cena 0 odrzucana", "if cena < 0:", "if cena <= 0:"),
        ("id nowego produktu = liczba produktów + 1", 'max((p["id"] for p in produkty), default=0) + 1', "len(produkty) + 1"),
        ("statystyki dla pustej listy rzucają wyjątek", "    if not produkty:\n        return {", "    if False:\n        return {"),
        ("szukaj rozróżnia wielkość liter", 'f = fraza.strip().lower()', 'f = fraza.strip()'),
        ("wartość magazynu liczona bez ilości", 'round(sum(p["cena"] * p["ilosc"] for p in produkty), 2)}', 'round(sum(p["cena"] for p in produkty), 2)}'),
        ("pusta nazwa akceptowana", '    if not nazwa:\n        raise ValueError("nazwa nie może być pusta")\n', ""),
    ], min_testow=15)
