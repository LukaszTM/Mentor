# -*- coding: utf-8 -*-
"""
Środowisko kursu i ćwiczenia „w Mentorze” dla programu Python → Junior QA.

SRODOWISKO — co Mentor ma sprawdzić i (za zgodą ucznia) zainstalować w osobnym środowisku kursu.
CWICZENIA  — dla zadań z plikiem .py: szablon, przykład (inny kontekst niż zadanie!), podpowiedź, dane dla input()
             i SPRAWDZENIE. Zadanie bez sprawdzenia dostaje status „Plik istnieje — wymaga sprawdzenia”, nie „Zaliczone”.
Rodzaje sprawdzeń: uruchom_bez_bledu · wyjscie_zawiera (tekst, nie_zawiera, min_linii, stdin) · pytest (plik_testu) · plik_istnieje.
„{rok}” w tekście/stdin = bieżący rok.
"""

SRODOWISKO = {
    "python": ">=3.11,<3.14",
    "pakiety": ["pytest", "requests", "selenium", "flask"],
    "lock": "programy/zaleznosci/requirements.lock",
    "narzedzia_wymagane": [],
    "narzedzia_opcjonalne": {"git": 0, "claude": 0},
    "przegladarka": "edge",
    "przegladarka_od_tygodnia": 8,
    "sprawdzenia": [
        {"kind": "python_import", "module": "pytest"},
        {"kind": "python_import", "module": "requests"},
        {"kind": "python_import", "module": "selenium"},
        {"kind": "python_import", "module": "flask"},
        {"kind": "pytest_sample"},
        {"kind": "local_api"},
        {"kind": "selenium_browser", "optional": True},
    ],
    "uwagi": ["Git i Claude Code są opcjonalne: Mentor ich nie instaluje, pokazuje tylko, czy działają (zadanie 1 tygodnia 0 prowadzi przez instalację).",
              "Przeglądarka (Edge) potrzebna od tygodnia 8 (Selenium) — Windows 10/11 ma ją wbudowaną."],
}

CWICZENIA = {
    "t0z3": {
        "plik": "hello.py",
        "szablon": "# hello.py — pierwszy program\n# 1) wypisz powitanie ze swoim imieniem\n# 2) na górze: import datetime, na dole wypisz dzisiejszą datę\n\n",
        "przyklad": 'import datetime\n\nprint("Dzień dobry z Mentora")\nprint("Dziś jest dzień tygodnia numer", datetime.date.today().weekday() + 1)\n',
        "podpowiedz": "print(\"tekst w cudzysłowie\") wypisuje tekst. datetime.date.today() zwraca dzisiejszą datę — ale najpierw import datetime na górze pliku. Jeśli widzisz SyntaxError: sprawdź cudzysłowy i nawiasy.",
        "sprawdzenie": {"rodzaj": "wyjscie_zawiera", "tekst": ["{rok}"], "min_linii": 2},
    },
    "t1z1": {
        "plik": "zmienne.py",
        "szablon": "# zmienne.py — 5 zmiennych różnych typów opisujących jedno zwierzę\n# imie (str), waga_kg (float), wiek_lat (int), rasa (str), czy_zdrowe (bool)\n# dla każdej: print(zmienna, type(zmienna))\n\n",
        "przyklad": 'tytul = "Mentor"          # str\nwersja = 2.7             # float\nlekcji = 60              # int\ndarmowy = True           # bool\n\nprint(tytul, type(tytul))\nprint(wersja, type(wersja))\nprint(lekcji, type(lekcji))\nprint(darmowy, type(darmowy))\n',
        "sprawdzenie": {"rodzaj": "wyjscie_zawiera", "tekst": ["<class 'str'>", "<class 'float'>", "<class 'int'>", "<class 'bool'>"], "min_linii": 5},
    },
    "t1z2": {
        "plik": "kalkulator.py",
        "szablon": "# kalkulator.py — trzy input(): pierwsza liczba, działanie (+ - * /), druga liczba\n# if/elif/elif/elif/else; przed dzieleniem sprawdź b == 0\n\n",
        "przyklad": 'temperatura = float(input("Temperatura w °C: "))\njednostka = input("Na co przeliczyć (F/K)? ")\n\nif jednostka == "F":\n    print("Wynik:", temperatura * 9 / 5 + 32)\nelif jednostka == "K":\n    print("Wynik:", temperatura + 273.15)\nelse:\n    print("Nieznana jednostka")\n',
        "stdin": "6\n*\n3\n",
        "podpowiedz": "input() zawsze zwraca napis — liczby zamień przez float(). Porównanie działania to podwójny znak: if dzialanie == \"+\":. Test „Sprawdź wynik” podaje: 6, potem *, potem 3 — w tej kolejności (liczba, działanie, liczba) — i szuka w wyjściu 18.",
        "sprawdzenie": {"rodzaj": "wyjscie_zawiera", "stdin": "6\n*\n3\n", "tekst": ["18"]},
    },
    "t1z3": {
        "plik": "wiek.py",
        "szablon": "# wiek.py — rok urodzenia → wiek i pełnoletniość\n# int(input(...)); import datetime; rok = datetime.date.today().year\n\n",
        "przyklad": 'import datetime\n\nrok_zakupu = int(input("Rok zakupu ciągnika: "))\nlata = datetime.date.today().year - rok_zakupu\nif lata < 0:\n    print("to jeszcze nie ten rok")\nelif lata >= 10:\n    print(f"Ciągnik ma {lata} lat — czas na przegląd")\nelse:\n    print(f"Ciągnik ma {lata} lat")\n',
        "stdin": "2000\n",
        "sprawdzenie": {"rodzaj": "wyjscie_zawiera", "stdin": "2000\n", "tekst": ["pełnoletni"], "nie_zawiera": ["niepełnoletni"]},
    },
    "t1z4": {
        "plik": "litry.py",
        "szablon": "# litry.py — litry mleka i % tłuszczu → kilogramy, cena za litr, wartość dostawy\n# kg = litry * 1.03; progi: > 4.0 → 2.10, > 3.5 → 1.90, inaczej 1.70\n\n",
        "stdin": "500\n4.2\n",
        "sprawdzenie": {"rodzaj": "wyjscie_zawiera", "stdin": "500\n4.2\n", "tekst": ["515", "2.1", "1050"]},
    },
    "t1z5": {
        "plik": "bmi.py",
        "szablon": "# bmi.py — wzrost (m) i waga (kg) → BMI i kategoria\n# walidacja: wzrost > 0 i waga > 0, inaczej komunikat i brak obliczeń\n\n",
        "stdin": "1.80\n75\n",
        "sprawdzenie": {"rodzaj": "wyjscie_zawiera", "stdin": "1.80\n75\n", "tekst": ["23.1", "norma"]},
    },
    "t2z1": {
        "plik": "tabliczka.py",
        "szablon": "# tabliczka.py — tabliczka mnożenia 1–10 pętlą for (potem pętla w pętli)\n\n",
        "przyklad": 'for dzien in range(1, 8):\n    print(f"Dzień {dzien}: {dzien * 20} minut nauki")\nprint()\nfor rzad in range(1, 4):\n    for kol in range(1, 4):\n        print(f"{rzad * kol:3}", end="")\n    print()\n',
        "sprawdzenie": {"rodzaj": "wyjscie_zawiera", "tekst": ["100"], "min_linii": 10},
    },
    "t2z2": {"plik": "lista_zakupow.py", "sprawdzenie": {"rodzaj": "plik_istnieje"}},
    "t2z3": {
        "plik": "suma.py",
        "szablon": "# suma.py — pętla while: liczby do wpisania 0 → suma, średnia, maksimum\n# len(liczby) == 0 → komunikat, nie ZeroDivisionError\n\n",
        "stdin": "5\n10\n15\n0\n",
        "sprawdzenie": {"rodzaj": "wyjscie_zawiera", "stdin": "5\n10\n15\n0\n", "tekst": ["30", "10", "15"]},
    },
    "t2z4": {
        "plik": "napisy.py",
        "szablon": "# napisy.py — tekst = input(...).strip(); upper(), [::-1], len(), samogłoski, słowa, najdłuższe słowo\n\n",
        "stdin": "Krowa je trawę\n",
        "sprawdzenie": {"rodzaj": "wyjscie_zawiera", "stdin": "Krowa je trawę\n", "tekst": ["KROWA JE TRAWĘ", "15", "6", "3"]},
    },
    "t2z5": {"plik": "zgadnij.py", "sprawdzenie": {"rodzaj": "plik_istnieje"}},
    "t3z1": {
        "plik": "funkcje.py",
        "szablon": '# funkcje.py — 5 funkcji z docstringami, bez input()/print() w środku\n\n\ndef pole_prostokata(a, b):\n    """Zwraca pole prostokąta o bokach a i b."""\n    ...\n\n\n# czy_parzysta(n), maksimum(lista), odwroc(napis), silnia(n)\n\n\nif __name__ == "__main__":\n    print(pole_prostokata(3, 4))\n',
        "przyklad": 'def srednia(lista):\n    """Zwraca średnią arytmetyczną listy liczb (0 dla pustej listy)."""\n    if not lista:\n        return 0\n    suma = 0\n    for x in lista:\n        suma += x\n    return suma / len(lista)\n\n\nif __name__ == "__main__":\n    print(srednia([2, 4, 6]))\n    help(srednia)\n',
        "sprawdzenie": {"rodzaj": "wyjscie_zawiera", "tekst": ["12", "120", "tok"]},
    },
    "t3z2": {"plik": "slownik.py", "sprawdzenie": {"rodzaj": "uruchom_bez_bledu", "stdin": "Krasula\nNiema\n"}},
    "t3z3": {"plik": "bledy.py", "stdin": "abc\n5\n0\n", "sprawdzenie": {"rodzaj": "uruchom_bez_bledu", "stdin": "abc\n5\n0\n7\n"}},
    "t3z4": {"plik": "losowanie.py", "sprawdzenie": {"rodzaj": "uruchom_bez_bledu", "min_linii": 2}},
    "t3z5": {"plik": "menedzer.py", "sprawdzenie": {"rodzaj": "plik_istnieje"}},
    "t4z2": {"plik": "zapis.py", "sprawdzenie": {"rodzaj": "uruchom_bez_bledu", "min_linii": 5}},
    "t4z3": {"plik": "csv_odczyt.py", "sprawdzenie": {"rodzaj": "plik_istnieje"}},
    "t4z5": {"plik": "dziennik_stada.py", "sprawdzenie": {"rodzaj": "plik_istnieje"}},
    "t5z1": {"plik": "zwierze.py", "sprawdzenie": {"rodzaj": "uruchom_bez_bledu"}},
    "t5z2": {"plik": "main.py", "sprawdzenie": {"rodzaj": "plik_istnieje"}},
    "t5z4": {"plik": "api.py", "sprawdzenie": {"rodzaj": "uruchom_bez_bledu", "limit_s": 40}},
    "t5z5": {"plik": "pogoda.py", "sprawdzenie": {"rodzaj": "uruchom_bez_bledu", "limit_s": 40}},
    "t7z1": {"plik": "test_funkcje.py", "szablon": '# test_funkcje.py — 5 testów funkcji z funkcje.py\nfrom funkcje import pole_prostokata\n\n\ndef test_pole_prostokata():\n    assert pole_prostokata(3, 4) == 12\n', "sprawdzenie": {"rodzaj": "pytest"}},
    "t7z2": {"plik": "test_bmi.py", "sprawdzenie": {"rodzaj": "pytest"}},
    "t7z3": {"plik": "test_menedzer.py", "sprawdzenie": {"rodzaj": "pytest"}},
    "t7z5": {"plik": "test_dziennik.py", "sprawdzenie": {"rodzaj": "pytest"}},
    "t8z1": {"plik": "saucedemo.py", "sprawdzenie": {"rodzaj": "plik_istnieje"}},
    "t8z2": {"plik": "lokatory.py", "sprawdzenie": {"rodzaj": "plik_istnieje"}},
    "t8z3": {"plik": "formularz.py", "sprawdzenie": {"rodzaj": "plik_istnieje"}},
    "t8z4": {"plik": "login_page.py", "sprawdzenie": {"rodzaj": "plik_istnieje"}},
    "t8z5": {"plik": "test_meridianbank.py", "sprawdzenie": {"rodzaj": "pytest", "limit_s": 180}},
    "t10z2": {"plik": "baza.py", "sprawdzenie": {"rodzaj": "plik_istnieje"}},
    "t10z3": {"plik": "stado.py", "sprawdzenie": {"rodzaj": "plik_istnieje"}},
    "t10z4": {"plik": "test_baza.py", "sprawdzenie": {"rodzaj": "pytest"}},
    "t11z1": {"plik": "app.py", "sprawdzenie": {"rodzaj": "plik_istnieje"}},
    "t11z4": {"plik": "test_web.py", "sprawdzenie": {"rodzaj": "pytest", "limit_s": 180}},
}
