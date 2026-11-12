# -*- coding: utf-8 -*-
"""Kurs Python → Junior QA: każde automatyczne sprawdzenie zalicza wzorcowe rozwiązanie napisane wg kroków zadania i NIE zalicza samego szablonu."""

import pytest

import cwiczenia as C

ROZW = {
"t0z3": 'import datetime\nprint("Cześć, tu Ola")\nprint("Dziś jest", datetime.date.today())\n',
"t1z1": 'imie = "Krasula"\nwaga_kg = 612.5\nwiek_lat = 4\nrasa = "HF"\nczy_zdrowe = True\nprint(imie, type(imie))\nprint(waga_kg, type(waga_kg))\nprint(wiek_lat, type(wiek_lat))\nprint(rasa, type(rasa))\nprint(czy_zdrowe, type(czy_zdrowe))\n',
"t1z2": 'a = float(input("Pierwsza liczba: "))\ndzialanie = input("Działanie (+ - * /): ")\nb = float(input("Druga liczba: "))\nif dzialanie == "+":\n    print("Wynik:", a + b)\nelif dzialanie == "-":\n    print("Wynik:", a - b)\nelif dzialanie == "*":\n    print("Wynik:", a * b)\nelif dzialanie == "/":\n    if b == 0:\n        print("Nie można dzielić przez zero")\n    else:\n        print("Wynik:", a / b)\nelse:\n    print("Nieznane działanie")\n',
"t1z3": 'import datetime\nrok_urodzenia = int(input("Rok urodzenia: "))\nrok = datetime.date.today().year\nwiek = rok - rok_urodzenia\nprint(f"Masz {wiek} lat")\nif wiek < 0:\n    print("to jeszcze nie ten rok")\nelif wiek >= 18:\n    print("pełnoletni")\nelse:\n    print("niepełnoletni")\n',
"t1z4": 'litry = float(input("Litry mleka: "))\ntluszcz = float(input("Tłuszcz w %: "))\nkg = litry * 1.03\nif tluszcz > 4.0:\n    cena = 2.10\nelif tluszcz > 3.5:\n    cena = 1.90\nelse:\n    cena = 1.70\nwartosc = litry * cena\nprint("Kilogramy:", round(kg, 1))\nprint("Cena za litr:", cena)\nprint(f"Wartość dostawy: {wartosc:.2f} zł")\n',
"t1z5": 'wzrost = float(input("Wzrost w m: "))\nwaga = float(input("Waga w kg: "))\nif wzrost <= 0 or waga <= 0:\n    print("Podaj wartości większe od zera")\nelse:\n    if wzrost > 3:\n        print("Uwaga: wzrost podaj w metrach, nie centymetrach")\n    bmi = waga / (wzrost * wzrost)\n    if bmi < 18.5:\n        kat = "niedowaga"\n    elif bmi < 25:\n        kat = "norma"\n    elif bmi < 30:\n        kat = "nadwaga"\n    else:\n        kat = "otyłość"\n    print(f"BMI: {bmi:.1f}, {kat}")\n',
"t2z1": 'for a in range(1, 11):\n    for b in range(1, 11):\n        print(f"{a} x {b} = {a * b}")\n    print()\n',
"t2z3": 'liczby = []\nwhile True:\n    x = float(input("Liczba (0 = koniec): "))\n    if x == 0:\n        break\n    liczby.append(x)\nif len(liczby) == 0:\n    print("nic nie podano")\nelse:\n    print("suma:", sum(liczby))\n    print("średnia:", sum(liczby) / len(liczby))\n    print("max:", max(liczby))\n',
"t2z4": 'tekst = input("Wpisz zdanie: ").strip()\nprint(tekst.upper())\nprint(tekst[::-1])\nprint(len(tekst))\nlicznik = 0\nfor litera in tekst.lower():\n    if litera in "aeiouyąęó":\n        licznik += 1\nprint(licznik)\nslowa = tekst.split()\nprint(len(slowa))\nnajdluzsze = ""\nfor s in slowa:\n    if len(s) > len(najdluzsze):\n        najdluzsze = s\nprint(najdluzsze)\n',
"t3z1": 'def pole_prostokata(a, b):\n    """Pole."""\n    return a * b\n\n\ndef czy_parzysta(n):\n    """Parzysta?"""\n    return n % 2 == 0\n\n\ndef maksimum(lista):\n    """Max bez max()."""\n    najwieksza = lista[0]\n    for x in lista:\n        if x > najwieksza:\n            najwieksza = x\n    return najwieksza\n\n\ndef odwroc(napis):\n    """Od tyłu."""\n    return napis[::-1]\n\n\ndef silnia(n):\n    """n!"""\n    wynik = 1\n    for i in range(1, n + 1):\n        wynik *= i\n    return wynik\n\n\nprint(pole_prostokata(3, 4))\nprint(czy_parzysta(7))\nprint(maksimum([3, 9, 2]))\nprint(odwroc("kot"))\nprint(silnia(5))\nprint(silnia(0))\n',
"t3z2": 'wagi = {"Krasula": 612, "Mućka": 580}\n\n\ndef dodaj(wagi, imie, waga):\n    wagi[imie] = waga\n\n\ndef usun(wagi, imie):\n    if imie in wagi:\n        del wagi[imie]\n    else:\n        print("nie ma takiego zwierzęcia")\n\n\ndef wypisz_posortowane(wagi):\n    for imie, waga in sorted(wagi.items(), key=lambda p: p[1]):\n        print(imie, waga)\n\n\nwhile True:\n    wybor = input("1 dodaj, 2 usuń, 3 wypisz, 0 koniec: ")\n    if wybor == "1":\n        dodaj(wagi, input("imię: "), float(input("waga: ")))\n    elif wybor == "2":\n        usun(wagi, input("imię: "))\n    elif wybor == "3":\n        wypisz_posortowane(wagi)\n    elif wybor == "0":\n        break\n    else:\n        print("nieznana opcja")\n',
"t3z3": 'def wczytaj_liczbe(komunikat):\n    while True:\n        try:\n            return float(input(komunikat))\n        except ValueError:\n            print("To nie liczba")\n\n\na = wczytaj_liczbe("Pierwsza: ")\nb = wczytaj_liczbe("Druga: ")\ntry:\n    print("a / b =", a / b)\nexcept ZeroDivisionError:\n    print("Nie dzielimy przez zero")\n',
"t3z4": 'import random\nimport datetime\nstado = ["Krasula", "Mućka", "Łaciata", "Jagoda", "Malina", "Bura", "Siwa", "Zorza"]\ndo_kontroli = random.sample(stado, 3)\nprint("Do kontroli:", do_kontroli)\ndzis = datetime.date.today()\ntermin = dzis + datetime.timedelta(days=7)\nprint(termin.strftime("%d.%m.%Y"), termin.strftime("%A"))\nprint("Dni do Nowego Roku:", (datetime.date(dzis.year + 1, 1, 1) - dzis).days)\n',
"t4z2": 'imiona = ["Krasula", "Mućka", "Łaciata", "Jagoda", "Malina"]\nwith open("stado.txt", "w", encoding="utf-8") as f:\n    for imie in imiona:\n        f.write(imie + "\\n")\nwith open("stado.txt", encoding="utf-8") as f:\n    for linia in f:\n        print(linia.strip())\n',
"t5z1": 'class Zwierze:\n    def __init__(self, imie, rasa, waga):\n        self.imie = imie\n        self.rasa = rasa\n        self.waga = waga\n\n    def opis(self):\n        return f"{self.imie} ({self.rasa}), {self.waga} kg"\n\n    def przybierz(self, kg):\n        self.waga += kg\n\n    def __str__(self):\n        return self.opis()\n\n\nkrasula = Zwierze("Krasula", "HF", 612)\nmucka = Zwierze("Mućka", "Simental", 580)\nkrasula.przybierz(8)\nfor z in [krasula, mucka]:\n    print(z)\n',
"t5z4": 'import requests\nurl = "https://api.open-meteo.com/v1/forecast?latitude=51.78&longitude=22.62&daily=temperature_2m_min,temperature_2m_max&timezone=Europe/Warsaw"\ntry:\n    odp = requests.get(url, timeout=10)\n    if odp.status_code != 200:\n        print("Serwer odpowiedział kodem", odp.status_code)\n    else:\n        dane = odp.json()\n        print(dane["daily"]["time"][0], dane["daily"]["temperature_2m_min"][0], dane["daily"]["temperature_2m_max"][0])\nexcept requests.exceptions.RequestException as e:\n    print("Brak połączenia z internetem:", type(e).__name__)\n',
}

TEST_FUNKCJE = (
    "from funkcje import pole_prostokata, czy_parzysta, maksimum, odwroc, silnia\n\n\n"
    "def test_pole():\n    assert pole_prostokata(3, 4) == 12\n\n\n"
    "def test_parzysta():\n    assert czy_parzysta(7) is False\n\n\n"
    "def test_maksimum():\n    assert maksimum([3, 9, 2]) == 9\n\n\n"
    "def test_odwroc():\n    assert odwroc(\"kot\") == \"tok\"\n\n\n"
    "def test_silnia():\n    assert silnia(5) == 120 and silnia(0) == 1\n"
)


def _zad(kurs_json, zid):
    return next(z for t in kurs_json["tygodnie"] for z in t["zadania"] if z["id"] == zid)


@pytest.mark.parametrize("zid", sorted(ROZW))
def test_wzorcowe_rozwiazanie_zalicza_a_szablon_nie(srodowisko_kursu, kurs_json, tmp_path, zid):
    d = C.definicja(_zad(kurs_json, zid))
    assert d and d["sprawdzenie"]["rodzaj"] != "plik_istnieje"
    plik = tmp_path / d["plik"]
    plik.write_text(d["szablon"], encoding="utf-8")
    assert C.wykonaj_sprawdzenie(srodowisko_kursu, d, plik)["status"] != C.STATUS_ZALICZONE, "sam szablon nie może zaliczać"
    plik.write_text(ROZW[zid], encoding="utf-8")
    w = C.wykonaj_sprawdzenie(srodowisko_kursu, d, plik)
    if zid == "t5z4" and w["status"] != C.STATUS_ZALICZONE:
        pytest.skip("t5z4 wymaga internetu albo poprawnej obsługi braku sieci: " + w["opis"])
    assert w["status"] == C.STATUS_ZALICZONE, (w["opis"], w["szczegoly"][:500])


def test_pytest_t7z1(srodowisko_kursu, kurs_json, tmp_path):
    d = C.definicja(_zad(kurs_json, "t7z1"))
    (tmp_path / "funkcje.py").write_text(ROZW["t3z1"].split("\n\n\nprint")[0] + "\n", encoding="utf-8")
    plik = tmp_path / "test_funkcje.py"
    plik.write_text(TEST_FUNKCJE, encoding="utf-8")
    w = C.wykonaj_sprawdzenie(srodowisko_kursu, d, plik)
    assert w["status"] == C.STATUS_ZALICZONE and "5 passed" in w["opis"], w


def test_program_czekajacy_na_dane_nie_jest_bledem(srodowisko_kursu, kurs_json, tmp_path):
    d = C.definicja(_zad(kurs_json, "t3z2"))
    plik = tmp_path / "slownik.py"
    plik.write_text('while True:\n    if input("q = koniec: ") == "q":\n        break\n', encoding="utf-8")
    w = C.wykonaj_sprawdzenie(srodowisko_kursu, d, plik)
    assert w["status"] == C.STATUS_WYMAGA and "więcej danych" in w["opis"]


def test_kazde_cwiczenie_ma_spojne_dane(kurs_json):
    """stdin sprawdzenia i stdin przycisku Uruchom nie mogą się różnić; podpowiedź/przykład w zadaniach z testem tygodni 0–3."""
    for t in kurs_json["tygodnie"]:
        for z in t["zadania"]:
            c = z.get("cwiczenie")
            if not c:
                continue
            spr = c.get("sprawdzenie") or {}
            if c.get("stdin") and spr.get("stdin"):
                assert c["stdin"] == spr["stdin"], z["id"]
            assert z["kroki"][-1].startswith("W Mentorze") or z["id"] == "t0z3", z["id"]
            if t["tydzien"] <= 3 and spr.get("rodzaj") in ("wyjscie_zawiera", "uruchom_bez_bledu"):
                assert c.get("podpowiedz"), z["id"]
