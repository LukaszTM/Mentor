# -*- coding: utf-8 -*-
"""Diagnoza na start (STANDARD §2 pkt 3 — nie blokuje nauki; wynik wskazuje lekcje do powtórki),
pytania dziennika i ręczne przypisanie pytań quizowych do lekcji (gdzie dopasowanie po słowach kluczowych zawodzi)."""

DIAGNOZA = [
    {"p": "Pracownik ma 4 806 zł brutto, KUP 250, PIT-2, bez PPK. Ile dostaje „na rękę” w 2026 r.?",
     "o": ["3 305,85", "3 605,85", "3 905,85", "4 147,10"], "odp": 1,
     "w": "Składki 658,91, zdrowotna 373,24, zaliczka 168 → 3 605,85. Jeśli to nowość — lekcja „Wskaźniki 2026”.", "lekcja": "wskazniki_2026"},
    {"p": "Umowa na czas określony: 24 miesiące + aneks wydłużający o 12 miesięcy. Co się dzieje?",
     "o": ["Nic — aneks nie liczy się do limitu", "Aneks = nowa umowa; po 33. miesiącu umowa staje się bezterminowa", "Umowa wygasa po 24 miesiącach", "Potrzebna zgoda PIP"], "odp": 1,
     "w": "Art. 25¹ §2–3 KP — limit 33 miesięcy / 3 umów. Lekcja „Umowa o pracę”.", "lekcja": "umowa_o_prace"},
    {"p": "Wymiar czasu pracy w grudniu 2026 (święta 24, 25, 26.12 w czw, pt, sb) wynosi:",
     "o": ["184 h", "176 h", "168 h", "160 h"], "odp": 3,
     "w": "23 dni pon–pt × 8 = 184 − 3 święta × 8 = 160 h (sobotnie święto też obniża). Lekcja „Czas pracy”.", "lekcja": "czas_pracy_systemy"},
    {"p": "Pracownik na pełny etat chorował 10 dni w listopadzie (wymiar 160 h), pensja 6 000. Pensja za przepracowaną część:",
     "o": ["6 000 − 6 000/160 × 80 = 3 000", "6 000 − 6 000/30 × 10 = 4 000", "6 000 − 6 000/20 × 10 = 3 000", "6 000 — choroba nie pomniejsza pensji"], "odp": 1,
     "w": "Chorobę pomniejszasz zawsze przez 30 (§11 rozp. urlopowego). Lekcja „Wynagrodzenie za urlop i ekwiwalent”.", "lekcja": "wynagrodzenie_urlopowe"},
    {"p": "Pracownik (42 lata) chorował w roku łącznie 40 dni. Kto płaci za dni 34–40?",
     "o": ["Pracodawca — wynagrodzenie chorobowe", "ZUS — zasiłek chorobowy (wypłaca płatnik zasiłków lub ZUS)", "Nikt — po 33 dniach brak świadczenia", "Pracodawca 50%, ZUS 50%"], "odp": 1,
     "w": "Art. 92 KP: 33 dni (14 po 50. roku życia) pracodawca; potem zasiłek. Lekcja „Wynagrodzenie chorobowe i zasiłek”.", "lekcja": "chorobowe_podstawy"},
    {"p": "Zleceniobiorca-student (23 lata) zarabia 2 000 zł miesięcznie. Składki ZUS:",
     "o": ["Pełne — jak pracownik", "Tylko zdrowotna", "Żadne — nie zgłaszasz go do ZUS", "Tylko emerytalna i rentowa"], "odp": 2,
     "w": "Art. 6 ust. 4 ustawy systemowej — uczeń/student do 26 lat na zleceniu nie podlega ubezpieczeniom. Lekcja „Umowa zlecenia i o dzieło”.", "lekcja": "zlecenie_dzielo"},
    {"p": "Nowy pracownik zaczął pracę 16.11.2026 (umowę podpisał 10.11). ZUA składasz:",
     "o": ["Do 17.11 z datą 10.11", "Do 23.11 z datą 16.11", "Do 30.11 z datą 1.12", "Razem z pierwszą listą płac"], "odp": 1,
     "w": "7 dni od powstania obowiązku = rozpoczęcia pracy. Lekcja „Dokumenty zgłoszeniowe ZUS”.", "lekcja": "zus_zgloszenia"},
    {"p": "Pracownik ze stażem 6 lat w firmie dostaje wypowiedzenie we wtorek 17.11.2026. Umowa rozwiąże się:",
     "o": ["5.12.2026 (2 tygodnie)", "31.12.2026 (1 miesiąc)", "28.02.2027 (3 miesiące)", "17.02.2027 (3 miesiące od doręczenia)"], "odp": 2,
     "w": "Staż ≥ 3 lata → 3 miesiące, koniec ostatniego dnia miesiąca (art. 36 §1 pkt 3, art. 30 §2¹). Lekcja „Rozwiązanie umowy o pracę”.", "lekcja": "rozwiazanie_umowy"},
    {"p": "Od 5.11.2026 nowa definicja mobbingu NIE wymaga już wykazania:",
     "o": ["Uporczywości zachowań", "Długotrwałości i skutku w postaci rozstroju zdrowia / zaniżonej oceny przydatności", "Naruszenia godności", "Winy pracodawcy"], "odp": 1,
     "w": "Ustawa z 19.06.2026 (Dz.U. 2026 poz. 1046). Lekcja „Mobbing po nowelizacji”.", "lekcja": "mobbing_dyskryminacja_2026"},
    {"p": "Komplet DRA/RCA/RSA za wynagrodzenia za listopad wypłacone 10 grudnia spółka z o.o. składa:",
     "o": ["Do 15 grudnia jako 11/2026", "Do 15 stycznia jako 12/2026", "Do 20 grudnia jako 11/2026", "Do 31 grudnia jako 12/2026"], "odp": 1,
     "w": "Zasada kasowa: miesiąc kompletu = miesiąc wypłaty; osoby prawne do 15. Lekcja „Rozliczenia miesięczne”.", "lekcja": "zus_rozliczenia"},
]

PYTANIA_DZIENNIKA = [
    "Jaką liczbę lub termin z dzisiejszej lekcji policzyłem sam, zanim sprawdziłem w Warsztacie — i czy się zgadzało?",
    "Który przepis (artykuł, Dz.U.) był dziś podstawą rozstrzygnięcia? Zapisz go z datą sprawdzenia.",
    "Co w dzisiejszym kazusie zrobiłbym inaczej, gdyby zmienił się jeden fakt (etat, staż, wiek, data)?",
    "Jaki błąd z sekcji „Typowe błędy” mógłbym popełnić w prawdziwej firmie i jak go wykryję?",
    "Czego nie rozumiem po dzisiejszej lekcji — jedno pytanie do Asystenta na jutro.",
    "Który plik w katalogu projektu dziś powstał lub się zmienił i do którego zadania należy?",
]

# (tydzień, indeks pytania w quizie) → id lekcji — tam, gdzie dopasowanie po słowach kluczowych w zbuduj.py zawodzi
QUIZ_LEKCJE = {
    (0, 3): "wskazniki_2026",
    (1, 2): "onboarding_akta",
    (1, 4): "onboarding_akta",
    (2, 2): "nadgodziny_noc",
    (5, 3): "wynagrodzenie_urlopowe",
    (9, 4): "urlop_wypoczynkowy",
}
