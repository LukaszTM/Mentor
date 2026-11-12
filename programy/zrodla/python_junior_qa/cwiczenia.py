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
        "podpowiedz": "Napis w cudzysłowie, float z kropką (612.5), int bez kropki, bool to True/False (wielka litera). print(zmienna, type(zmienna)) wypisze wartość i <class '…'>. „Sprawdź wynik” oczekuje co najmniej 5 linii i czterech typów: str, float, int, bool.",
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
        "podpowiedz": "Bieżący rok: datetime.date.today().year (po import datetime). Trzy gałęzie: wiek < 0 → „to jeszcze nie ten rok”; wiek >= 18 → „pełnoletni”; else → „niepełnoletni”. „Sprawdź wynik” podaje rok 2000 i oczekuje słowa „pełnoletni” (a nie „niepełnoletni”).",
        "stdin": "2000\n",
        "sprawdzenie": {"rodzaj": "wyjscie_zawiera", "stdin": "2000\n", "tekst": ["pełnoletni"], "nie_zawiera": ["niepełnoletni"]},
    },
    "t1z4": {
        "plik": "litry.py",
        "szablon": "# litry.py — litry mleka i % tłuszczu → kilogramy, cena za litr, wartość dostawy\n# kg = litry * 1.03; progi: > 4.0 → 2.10, > 3.5 → 1.90, inaczej 1.70\n\n",
        "przyklad": 'kg_ziarna = float(input("Ile kg ziarna? "))\nwilgotnosc = float(input("Wilgotność w %: "))\nif wilgotnosc > 20:\n    cena = 0.70\nelif wilgotnosc > 15:\n    cena = 0.85\nelse:\n    cena = 0.95\nprint(f"Cena za kg: {cena:.2f} zł")\nprint(f"Wartość: {kg_ziarna * cena:.2f} zł")\n',
        "podpowiedz": "Progi sprawdzaj od NAJWYŻSZEGO (if tłuszcz > 4.0 … elif > 3.5 … else). Zaokrąglenie: round(kg, 1); dwa miejsca po przecinku w f-stringu: f\"{wartosc:.2f}\". „Sprawdź wynik” podaje 500 i 4.2 i szuka 515, 2.1 i 1050.",
        "stdin": "500\n4.2\n",
        "sprawdzenie": {"rodzaj": "wyjscie_zawiera", "stdin": "500\n4.2\n", "tekst": ["515", "2.1", "1050"]},
    },
    "t1z5": {
        "plik": "bmi.py",
        "szablon": "# bmi.py — wzrost (m) i waga (kg) → BMI i kategoria\n# walidacja: wzrost > 0 i waga > 0, inaczej komunikat i brak obliczeń\n\n",
        "przyklad": 'dlugosc = float(input("Długość pola w m: "))\nszerokosc = float(input("Szerokość pola w m: "))\nif dlugosc <= 0 or szerokosc <= 0:\n    print("Podaj wartości większe od zera")\nelse:\n    ary = dlugosc * szerokosc / 100\n    print(f"Powierzchnia: {ary:.1f} a")\n    if ary < 10:\n        print("małe pole")\n    elif ary < 100:\n        print("średnie pole")\n    else:\n        print("duże pole")\n',
        "podpowiedz": "Najpierw walidacja (wzrost > 0 i waga > 0), potem obliczenie — w else. BMI z jednym miejscem po przecinku: f\"{bmi:.1f}\". „Sprawdź wynik” podaje 1.80 i 75 i szuka 23.1 oraz słowa „norma”.",
        "stdin": "1.80\n75\n",
        "sprawdzenie": {"rodzaj": "wyjscie_zawiera", "stdin": "1.80\n75\n", "tekst": ["23.1", "norma"]},
    },
    "t2z1": {
        "plik": "tabliczka.py",
        "szablon": "# tabliczka.py — tabliczka mnożenia 1–10 pętlą for (potem pętla w pętli)\n\n",
        "przyklad": 'for dzien in range(1, 8):\n    print(f"Dzień {dzien}: {dzien * 20} minut nauki")\nprint()\nfor rzad in range(1, 4):\n    for kol in range(1, 4):\n        print(f"{rzad * kol:3}", end="")\n    print()\n',
        "podpowiedz": "range(1, 11) daje 1…10 (koniec jest wyłączony). Pętla w pętli: zewnętrzna po a, wewnętrzna po b, w środku print(f\"{a} x {b} = {a*b}\"). „Sprawdź wynik” oczekuje co najmniej 10 linii i liczby 100 w wyjściu.",
        "sprawdzenie": {"rodzaj": "wyjscie_zawiera", "tekst": ["100"], "min_linii": 10},
    },
    "t2z2": {"plik": "lista_zakupow.py", "sprawdzenie": {"rodzaj": "plik_istnieje"}},
    "t2z3": {
        "plik": "suma.py",
        "szablon": "# suma.py — pętla while: liczby do wpisania 0 → suma, średnia, maksimum\n# len(liczby) == 0 → komunikat, nie ZeroDivisionError\n\n",
        "przyklad": 'udoje = []\nwhile True:\n    litry = float(input("Udój w litrach (0 = koniec): "))\n    if litry == 0:\n        break\n    udoje.append(litry)\nif len(udoje) == 0:\n    print("nic nie podano")\nelse:\n    najmniejszy = udoje[0]\n    for u in udoje:\n        if u < najmniejszy:\n            najmniejszy = u\n    print("udojów:", len(udoje), "najmniejszy:", najmniejszy)\n',
        "podpowiedz": "Pętla while True z break przy 0; po pętli NAJPIERW sprawdź, czy lista nie jest pusta (inaczej dzielenie przez zero przy średniej). „Sprawdź wynik” podaje 5, 10, 15, 0 i szuka 30, 10 i 15.",
        "stdin": "5\n10\n15\n0\n",
        "sprawdzenie": {"rodzaj": "wyjscie_zawiera", "stdin": "5\n10\n15\n0\n", "tekst": ["30", "10", "15"]},
    },
    "t2z4": {
        "plik": "napisy.py",
        "szablon": "# napisy.py — tekst = input(...).strip(); upper(), [::-1], len(), samogłoski, słowa, najdłuższe słowo\n\n",
        "stdin": "Krowa je trawę\n",
        "przyklad": 'zdanie = input("Zdanie: ").strip()\nprint(zdanie.lower())          # małymi literami\nprint(zdanie.replace(" ", "_"))  # spacje na podkreślenia\nspolgloski = 0\nfor litera in zdanie.lower():\n    if litera in "bcdfghjklmnprstwz":\n        spolgloski += 1\nprint("spółgłosek:", spolgloski)\nprint("słów:", len(zdanie.split()))\n',
        "podpowiedz": "Metody napisu nie zmieniają zmiennej — zwracają NOWY napis (tekst.upper() trzeba wypisać albo przypisać). Od tyłu: tekst[::-1]. „Sprawdź wynik” podaje „Krowa je trawę” i oczekuje: KROWA JE TRAWĘ, 14 (znaków ze spacjami), 5 (samogłosek), 3 (słowa).",
        "sprawdzenie": {"rodzaj": "wyjscie_zawiera", "stdin": "Krowa je trawę\n", "tekst": ["KROWA JE TRAWĘ", "14", "5", "3"]},
    },
    "t2z5": {"plik": "zgadnij.py", "sprawdzenie": {"rodzaj": "plik_istnieje"}},
    "t3z1": {
        "plik": "funkcje.py",
        "szablon": '# funkcje.py — 5 funkcji z docstringami, bez input()/print() w środku\n\n\ndef pole_prostokata(a, b):\n    """Zwraca pole prostokąta o bokach a i b."""\n    ...\n\n\n# czy_parzysta(n), maksimum(lista), odwroc(napis), silnia(n)\n\n\nif __name__ == "__main__":\n    print(pole_prostokata(3, 4))\n',
        "przyklad": 'def srednia(lista):\n    """Zwraca średnią arytmetyczną listy liczb (0 dla pustej listy)."""\n    if not lista:\n        return 0\n    suma = 0\n    for x in lista:\n        suma += x\n    return suma / len(lista)\n\n\nif __name__ == "__main__":\n    print(srednia([2, 4, 6]))\n    help(srednia)\n',
        "podpowiedz": "Funkcja ZWRACA (return), program główny WYPISUJE (print na dole pliku). silnia: wynik = 1; for i in range(1, n + 1): wynik *= i. „Sprawdź wynik” oczekuje w wyjściu 12 (pole 3×4), 120 (silnia 5) i tok (odwroc kot) — wypisz te wywołania na dole pliku.",
        "sprawdzenie": {"rodzaj": "wyjscie_zawiera", "tekst": ["12", "120", "tok"]},
    },
    "t3z2": {
        "plik": "slownik.py",
        "przyklad": 'ceny = {"pasza": 120, "siano": 80}\n\n\ndef dodaj_cene(ceny, produkt, cena):\n    """Dodaje lub nadpisuje cenę produktu."""\n    ceny[produkt] = cena\n\n\ndef usun_cene(ceny, produkt):\n    """Usuwa produkt, jeśli jest w słowniku."""\n    if produkt in ceny:\n        del ceny[produkt]\n    else:\n        print("nie ma takiego produktu")\n\n\ndodaj_cene(ceny, "otręby", 95)\nusun_cene(ceny, "sól")\nfor produkt, cena in sorted(ceny.items(), key=lambda para: para[1]):\n    print(produkt, cena)\n',
        "podpowiedz": "Przed del i przed odczytem sprawdź: if imie in wagi. Sortowanie po wartości: sorted(wagi.items(), key=lambda p: p[1]). Menu jak w liście zakupów: 1 dodaj, 2 usuń, 3 wypisz, 0 koniec. „Sprawdź wynik” podaje: 2, Niema (usunięcie nieistniejącego — bez KeyError), 3 (wypisanie), 0 i szuka w wyjściu Krasula i Mućka.",
        "stdin": "2\nNiema\n3\n0\n",
        "sprawdzenie": {"rodzaj": "wyjscie_zawiera", "stdin": "2\nNiema\n3\n0\n", "tekst": ["Krasula", "Mućka"]},
    },
    "t3z3": {
        "plik": "bledy.py",
        "przyklad": 'def wczytaj_calkowita(komunikat):\n    """Pyta tak długo, aż użytkownik poda liczbę całkowitą."""\n    while True:\n        try:\n            return int(input(komunikat))\n        except ValueError:\n            print("To nie jest liczba całkowita, spróbuj jeszcze raz")\n\n\nsztuk = wczytaj_calkowita("Ile sztuk bydła? ")\nprint("Zapisano:", sztuk)\n',
        "podpowiedz": "Funkcja wczytaj_liczbe: while True → try: return float(input(komunikat)) → except ValueError: komunikat. Dzielenie a / b w try z except ZeroDivisionError. „Sprawdź wynik” podaje: abc, 5, 0 — program musi przeżyć literę i zero (bez tracebacku) i wypisać komunikaty (np. „To nie liczba”, „Nie dzielimy przez zero”).",
        "stdin": "abc\n5\n0\n",
        "sprawdzenie": {"rodzaj": "wyjscie_zawiera", "stdin": "abc\n5\n0\n", "tekst": ["nie"], "min_linii": 1},
    },
    "t3z4": {
        "plik": "losowanie.py",
        "przyklad": 'import datetime\nimport random\n\npola = ["Łąka", "Pod lasem", "Za stodołą", "Przy drodze", "Górka"]\ndo_koszenia = random.sample(pola, 2)      # dwa RÓŻNE pola\nprint("Do koszenia:", do_koszenia)\ndzis = datetime.date.today()\nza_miesiac = dzis + datetime.timedelta(days=30)\nprint("Następny przegląd:", za_miesiac.strftime("%d.%m.%Y"))\n',
        "podpowiedz": "random.sample(lista, 3) daje 3 różne elementy; random.choice daje jeden (może się powtórzyć). Data za tydzień: dzis + datetime.timedelta(days=7); format: .strftime(\"%d.%m.%Y\"). „Sprawdź wynik” wymaga uruchomienia bez błędu i co najmniej 2 linii.",
        "sprawdzenie": {"rodzaj": "uruchom_bez_bledu", "min_linii": 2},
    },
    "t3z5": {"plik": "menedzer.py", "sprawdzenie": {"rodzaj": "plik_istnieje"}},
    "t4z2": {
        "plik": "zapis.py",
        "przyklad": 'zadania = ["nakarmić", "zważyć", "wyczyścić boks"]\nwith open("zadania.txt", "w", encoding="utf-8") as f:\n    for z in zadania:\n        f.write(z + "\\n")\n\nwith open("zadania.txt", encoding="utf-8") as f:\n    for nr, linia in enumerate(f, start=1):\n        print(nr, linia.strip())\n',
        "podpowiedz": "Zapis: open(\"stado.txt\", \"w\", encoding=\"utf-8\") i f.write(imie + \"\\n\"); odczyt: for linia in f: print(linia.strip()). Z with nie potrzebujesz close(). „Sprawdź wynik” wymaga uruchomienia bez błędu i co najmniej 5 linii (odczyt).",
        "sprawdzenie": {"rodzaj": "uruchom_bez_bledu", "min_linii": 5},
    },
    "t4z3": {"plik": "csv_odczyt.py", "sprawdzenie": {"rodzaj": "plik_istnieje"}},
    "t4z5": {"plik": "dziennik_stada.py", "sprawdzenie": {"rodzaj": "plik_istnieje"}},
    "t5z1": {
        "plik": "zwierze.py",
        "przyklad": 'class Maszyna:\n    def __init__(self, nazwa, rok, motogodziny):\n        self.nazwa = nazwa\n        self.rok = rok\n        self.motogodziny = motogodziny\n\n    def pracuj(self, godziny):\n        self.motogodziny += godziny\n\n    def __str__(self):\n        return f"{self.nazwa} ({self.rok}), {self.motogodziny} mth"\n\n\nciagnik = Maszyna("Ursus", 1998, 4200)\nciagnik.pracuj(6)\nprint(ciagnik)\n',
        "podpowiedz": "Każda metoda ma self jako pierwszy parametr; __init__ ustawia self.imie, self.rasa, self.waga; __str__ zwraca napis, który print pokaże zamiast <object at 0x…>. „Sprawdź wynik” wymaga uruchomienia bez błędu — wypisz opisy obiektów na dole pliku.",
        "sprawdzenie": {"rodzaj": "uruchom_bez_bledu", "min_linii": 1},
    },
    "t5z2": {"plik": "main.py", "sprawdzenie": {"rodzaj": "plik_istnieje"}},
    "t5z4": {"plik": "api.py", "sprawdzenie": {"rodzaj": "uruchom_bez_bledu", "limit_s": 40}},
    "t5z5": {"plik": "pogoda.py", "sprawdzenie": {"rodzaj": "uruchom_bez_bledu", "limit_s": 40}},
    "t7z1": {
        "plik": "test_funkcje.py",
        "szablon": '# test_funkcje.py — 5 testów funkcji z funkcje.py (ten sam katalog)\nfrom funkcje import pole_prostokata\n\n\ndef test_pole_prostokata():\n    assert pole_prostokata(3, 4) == 12\n',
        "podpowiedz": "Plik test_*.py, funkcje def test_*, jeden assert z konkretną wartością. funkcje.py musi leżeć w tym samym katalogu i nie może wywoływać input() przy imporcie (kod startowy pod if __name__ == \"__main__\":). „Sprawdź wynik” uruchamia pytest w środowisku kursu — zielone = zaliczone.",
        "sprawdzenie": {"rodzaj": "pytest"},
    },
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
