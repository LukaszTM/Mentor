# -*- coding: utf-8 -*-
"""Firma ćwiczeniowa dla Warsztatu: osoby (fikcyjne, PESEL-e poprawne formalnie), regulaminy, parametry roku, narzędzia."""
import datetime as dt
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
import kadry  # noqa: E402

_OSOBY = [
    # imie, nazwisko, plec, ur, stanowisko, rodzaj, umowa, od, do, etat, zasadnicze, ppk, kup, pit2, kod, flagi, uwagi
    ("Anna", "Kowalczyk", "K", "1991-05-14", "specjalistka ds. jakości", "pracownik", "próbna 3 mies.", "2026-10-01", "2026-12-31", 1, 6000, True, 250, 300, "011000", {}, "okres próbny; planowana umowa na czas określony"),
    ("Marek", "Zieliński", "M", "1988-02-20", "operator linii (3 zmiany)", "pracownik", "czas określony", "2025-03-01", "2027-02-28", 1, 5400, True, 250, 300, "011000", {}, "praca nocna, system równoważny 12 h"),
    ("Halina", "Mazur", "K", "1972-08-03", "główna księgowa", "pracownik", "nieokreślony", "2009-04-01", "", 1, 7800, False, 300, 300, "011000", {}, "54 lata — chorobowe 14 dni; dojeżdża (KUP 300)"),
    ("Piotr", "Nowak", "M", "1985-11-30", "magazynier", "pracownik", "nieokreślony", "2019-09-01", "", 0.5, 2500, False, 250, 0, "011000", {}, "1/2 etatu; PIT-2 złożony u drugiego pracodawcy"),
    ("Katarzyna", "Wójcik", "K", "1995-06-18", "pracownik produkcji", "pracownik", "nieokreślony", "2023-01-16", "", 1, 4806, True, 250, 300, "011000", {}, "pensja minimalna; dziecko 5 lat"),
    ("Tomasz", "Lis", "M", "1979-01-09", "dyrektor produkcji", "pracownik", "nieokreślony", "2015-05-01", "", 1, 14000, True, 250, 300, "011000", {}, "przekracza próg 120 000 zł w listopadzie"),
    ("Ewa", "Sobczak", "K", "1983-09-25", "specjalistka ds. administracji", "pracownik", "nieokreślony", "2021-03-01", "", 1, 5200, True, 250, 300, "011002", {}, "orzeczenie — stopień umiarkowany (7 h / 35 h, 10 dni dodatkowego urlopu)"),
    ("Jakub", "Krawczyk", "M", "2002-03-03", "pakowacz", "pracownik", "nieokreślony", "2026-07-01", "", 1, 4900, True, 250, 300, "011000", {"mlody": True}, "24 lata — ulga dla młodych"),
    ("Michał", "Dąbrowski", "M", "2004-04-12", "zlecenie: pomoc w magazynie", "zlecenie", "zlecenie", "2026-09-01", "", 0, 2000, False, 0, 0, "", {"student": True, "mlody": True}, "student 22 l. — bez ZUS, ulga dla młodych; 31,40 zł/h × ok. 64 h"),
    ("Agnieszka", "Pawlak", "K", "1990-12-02", "zlecenie: obsługa sklepu firmowego", "zlecenie", "zlecenie", "2026-02-01", "", 0, 3000, False, 0, 0, "041100", {}, "etat 5 000 zł u innego pracodawcy → ze zlecenia tylko zdrowotna"),
    ("Robert", "Król", "M", "1976-07-07", "zlecenie: kierowca dostaw", "zlecenie", "zlecenie", "2024-06-01", "", 0, 3500, True, 0, 300, "041100", {}, "bez innego tytułu — pełne składki, dobrowolne chorobowe; PPK tak"),
    ("Joanna", "Michalska", "K", "1987-10-21", "dzieło: projekt etykiet", "dzieło", "umowa o dzieło", "2026-11-02", "2026-11-30", 0, 2500, False, 0, 0, "", {}, "RUD w 7 dni od zawarcia; KUP 50% (prawa autorskie)"),
]

FIRMA_OSOBY = []
for i, (im, nz, pl, ur, st, rodz, um, od, do, et, zas, ppk, kup, pit2, kod, flagi, uw) in enumerate(_OSOBY):
    FIRMA_OSOBY.append({"id": f"o{i + 1}", "imie": im, "nazwisko": nz, "plec": pl, "ur": ur, "pesel": kadry.pesel_z_daty(dt.date.fromisoformat(ur), pl, seria=i),
                        "stanowisko": st, "rodzaj": rodz, "umowa": um, "od": od, "do": do, "etat": et, "zasadnicze": zas, "ppk": ppk, "kup": kup, "pit2": pit2,
                        "kod": kod, "uwagi": uw, "dokumenty": [], **flagi})

FIRMA_REGULAMINY = [
    "Wypłata wynagrodzenia do 10. dnia następnego miesiąca przelewem; gdy 10. jest dniem wolnym — dzień roboczy wcześniej.",
    "Biuro: podstawowy system czasu pracy, 1-miesięczny okres rozliczeniowy, 8:00–16:00. Produkcja i logistyka: równoważny do 12 h, 3-miesięczny okres rozliczeniowy, 3 zmiany (6–18, 18–6), pora nocna 22:00–6:00.",
    "Dodatek nocny ustawowy (20% stawki godzinowej z minimalnego wynagrodzenia). Nadgodziny: dodatki ustawowe 50/100% lub czas wolny.",
    "Premia regulaminowa do 10% wynagrodzenia zasadniczego za wynik miesiąca — POMNIEJSZANA proporcjonalnie za dni choroby (wlicza się do podstawy zasiłku).",
    "Dodatek stażowy 2% zasadniczego za każdy rok pracy w firmie (max 20%) — wypłacany w pełnej wysokości także za czas choroby (NIE wlicza się do podstawy zasiłku).",
    "Składka wypadkowa firmy: 1,20% (stopa ustalona przez ZUS na podstawie IWA, obowiązuje od 1.04.2026 do 31.03.2027).",
    "Firma jest płatnikiem zasiłków (na 30.11.2025 zgłaszała 66 osób do ubezpieczenia chorobowego).",
    "ZFŚS prowadzony (62 pracowników = 58,5 etatu); regulamin ZFŚS z kryterium dochodu na osobę w rodzinie; komisja socjalna 3-osobowa.",
    "PPK w instytucji „PFR TFI” (ćwiczeniowo): wpłaty podstawowe 2% / 1,5%; brak wpłat dodatkowych.",
    "Regulamin pracy i wynagradzania z 1.03.2025; brak związków zawodowych — przedstawiciel załogi wybrany 10.02.2025; benefity (karta sportowa, pakiet medyczny) współfinansowane przez pracownika (1 zł) wg regulaminu wynagradzania.",
    "Kategorie zaszeregowania: I pracownicy produkcji i magazynu, II operatorzy i kierowcy, III specjaliści, IV kierownicy, V dyrektorzy — widełki w siatce płac (tydzień 11).",
]

PARAMETRY = dict(kadry.DOMYSLNE, rok=2026, wypadkowa=1.20)
NARZEDZIA = ["firma", "place", "zasilki", "urlopy", "czas", "potracenia", "delegacje", "zus", "pit", "przepisy"]
