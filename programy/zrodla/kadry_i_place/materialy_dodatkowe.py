# -*- coding: utf-8 -*-
"""Dodatkowe pliki paczki materiałów przywoływane w lekcjach (przykłady, dane do ćwiczeń, szablony startowe).
Klucz = ścieżka względem katalogu materiałów. Dane są fikcyjne (AGRO-MLEKO)."""

PRZYKLADY = {
    "przyklady/tydzien_01/ogloszenia_do_oceny.md": """# Trzy ogłoszenia do oceny (fikcyjne) — lekcja „Rekrutacja”

Oceń każde pod kątem: widełki (art. 22¹ᵇ KP), neutralność (art. 18³ᵃ), zakazane pytania/dane (art. 22¹), klauzula RODO.

## Ogłoszenie A
**Młody, dynamiczny operator wózka widłowego** do magazynu w Lublinie. Wynagrodzenie: atrakcyjne, do uzgodnienia. Wymagamy: uprawnień UDT, dyspozycyjności, niekaralności (zaświadczenie). W CV prosimy podać oczekiwania i dotychczasowe zarobki. Prosimy o dołączenie zdjęcia.

## Ogłoszenie B
**Osoba na stanowisko specjalisty ds. jakości** (laboratorium, system podstawowy 7–15). Wynagrodzenie zasadnicze 6 000–7 200 zł brutto zależnie od doświadczenia + premia regulaminowa do 10%. Wymagania: wykształcenie kierunkowe (technologia żywności lub pokrewne), znajomość HACCP. Klauzula: Administratorem danych jest AGRO-MLEKO sp. z o.o.; dane przetwarzamy na podstawie art. 22¹ KP i art. 6 ust. 1 lit. b, c RODO do zakończenia rekrutacji; za osobną zgodą — 12 miesięcy; prawa: dostęp, sprostowanie, usunięcie, skarga do PUODO.

## Ogłoszenie C
**Pakowaczka** — praca na 2 zmiany. Wynagrodzenie od 4 806 zł. Mile widziane panie bez małych dzieci (praca zmianowa). Zgłoszenia z CV na adres … Klauzula: „Wyrażam zgodę na przetwarzanie danych w celach rekrutacyjnych”.

## Klucz odpowiedzi (sprawdź po własnej ocenie)
- A: brak widełek (✘), „młody, dynamiczny” — kryterium wieku (✘), żądanie dotychczasowych zarobków (✘ art. 22¹ §1 pkt 6), niekaralność tylko gdy ustawa wymaga (operator wózka — nie) (✘), zdjęcie — dana nadmiarowa (✘), brak klauzuli RODO (✘).
- B: poprawne.
- C: nazwa stanowiska w rodzaju żeńskim (✘ neutralność), „od 4 806” bez górnej kwoty (✘), „panie bez małych dzieci” — dyskryminacja ze względu na płeć i rodzicielstwo (✘), klauzula zgody zamiast informacyjnej — zgoda nie jest podstawą dla danych z art. 22¹ (✘).
""",
    "przyklady/tydzien_02/grafik_grudzien_2026.md": """# Grafik — operator linii (system równoważny do 12 h, 3-miesięczny okres), grudzień 2026 (1–15.12)

Zmiany: D = 06:00–18:00, N = 18:00–06:00, W5 = wolne z 5-dniowego tygodnia, WN = wolna niedziela. Pora nocna 22:00–06:00.
Zdarzenia (dopisz do ewidencji): 05.12 urlop wypoczynkowy (UW), 08–09.12 choroba (e-ZLA), 12.12 praca przedłużona do 20:00 (polecenie nadgodzin nr 7/12).

| Data | Dzień | Zmiana |
|---|---|---|
| 01.12 | wt | D |
| 02.12 | śr | W5 |
| 03.12 | czw | N |
| 04.12 | pt | W5 (po nocy) |
| 05.12 | sb | D (zaplanowane 12 h) |
| 06.12 | nd | WN |
| 07.12 | pn | D |
| 08.12 | wt | N (zaplanowane) |
| 09.12 | śr | W5 |
| 10.12 | czw | N |
| 11.12 | pt | W5 |
| 12.12 | sb | D |
| 13.12 | nd | WN |
| 14.12 | pn | D |
| 15.12 | wt | W5 |

Wymiar grudnia 2026: 160 h (Warsztat → Czas pracy). Dni 16–31.12 ułóż sam w rotacji D, D, N, N, W, W (z zachowaniem 11 h i 35 h odpoczynku) tak, by miesiąc zbilansować do 160 h łącznie z nieobecnościami.
""",
    "przyklady/tydzien_03/zaswiadczenie_zus_wzor.md": """# Zaświadczenie o okresach ubezpieczenia (wzór fikcyjny — tak wygląda informacja z eZUS)

ZUS — Zakład Ubezpieczeń Społecznych, Oddział w Lublinie
Zaświadczenie o okresach podlegania ubezpieczeniom społecznym — wydane na wniosek ubezpieczonego (eZUS, data: 1.11.2026)

Ubezpieczona: Ewa Sobczak, PESEL 83092510121

| Od | Do | Tytuł (kod) | Płatnik | Składki emerytalno-rentowe |
|---|---|---|---|---|
| 2012-09-01 | 2016-08-31 | pracownik (01 10) | Zakłady Mięsne X sp. z o.o. | opłacone |
| 2016-09-01 | 2018-08-31 | zleceniobiorca (04 11) | Agencja Y | opłacone |
| 2017-03-01 | 2018-02-28 | zleceniobiorca (04 11) | Firma Z | opłacone (okres równoległy) |
| 2018-09-01 | 2019-02-28 | działalność — ulga na start (05 40) | — | tylko zdrowotne |
| 2019-03-01 | 2021-02-28 | działalność — preferencyjne (05 70) | — | opłacone |
| 2021-03-01 | nadal | pracownik (01 10) | AGRO-MLEKO sp. z o.o. | opłacone |

Okresy wliczane do stażu (art. 302¹ KP): te z opłaconymi składkami emerytalno-rentowymi; okresy równoległe — raz; ulga na start — nie.
""",
    "przyklady/tydzien_06/kartoteka_zielinski.md": """# Kartoteka wypłat — Marek Zieliński (5 400 zł) — 12 miesięcy przed niezdolnością od 16.11.2026

Składniki: stałe 5 400 (zasadnicze); premia regulaminowa do 10% — POMNIEJSZANA proporcjonalnie za dni choroby (wliczasz); dodatek stażowy 108 zł — wypłacany w pełnej wysokości także za chorobę (NIE wliczasz).

| Miesiąc | Stałe | Premia (zmienne) | Dodatek stażowy | Dni obowiązujące | Dni przepracowane | Uwagi |
|---|---|---|---|---|---|---|
| XI 2025 | 5 400 | 400 | 108 | 19 | 19 | |
| XII 2025 | 5 400 | 400 | 108 | 20 | 20 | |
| I 2026 | 5 400 | 400 | 108 | 20 | 20 | |
| II 2026 | 5 400 | 400 | 108 | 20 | 20 | |
| III 2026 | 5 400 (pensja wypłacona 2 700 + chorobowe) | 200 | 108 | 22 | 11 | choroba 12 dni (9–20.03) |
| IV 2026 | 5 400 | 400 | 108 | 21 | 21 | |
| V 2026 | 5 400 | 400 | 108 | 20 | 20 | |
| VI 2026 | 5 400 | 400 | 108 | 21 | 21 | |
| VII 2026 | 5 400 (wypłacona 3 240 + chorobowe) | 87 | 108 | 23 | 5 | choroba 20–31.07 + urlop (urlop = przepracowane: 5 dni pracy) |
| VIII 2026 | 5 400 | 400 | 108 | 21 | 21 | |
| IX 2026 | 5 400 | 400 | 108 | 22 | 22 | |
| X 2026 | 5 400 | 400 | 108 | 22 | 22 | |

Do Warsztat → Zasiłki → karta A wpisujesz: Stałe = 5 400 (kwota umowna), Zmienne = premia faktycznie wypłacona, dni obow. i przepr. jak wyżej.
""",
    "przyklady/tydzien_06/kontrola_sytuacje.md": """# Sześć dodatkowych sytuacji do oceny — kontrola zwolnień 2026

Oceń: praca zarobkowa / aktywność niezgodna z celem / czynność życia codziennego / wymaga wyjaśnień; podaj podstawę (art. 17 ustawy zasiłkowej).

1. Pracownica na L4 (złamana ręka) prowadzi webinar dla swojej fundacji — nieodpłatnie, 1 godzina.
2. Pracownik na L4 (zapalenie płuc) wyjeżdża do sanatorium na własny koszt, zgłasza adres w 3 dni.
3. Pracownik na L4 (depresja) pracuje w weekend w drugiej firmie na zleceniu (ma tam dobrowolne chorobowe).
4. Pracownica na L4 (ciąża — zagrożona) odbiera dziecko ze szkoły i robi zakupy.
5. Pracownik na L4 (uraz kolana) gra w meczu amatorskiej ligi piłkarskiej.
6. Pracownika nie zastano pod adresem; po wezwaniu wyjaśnia, że był u lekarza (ma zaświadczenie).

Klucz (sprawdź po własnej ocenie): 1 — nieodpłatna aktywność nie jest pracą zarobkową; oceniasz zgodność z celem (webinar przy złamanej ręce — zwykle dopuszczalny) → brak sankcji; 2 — dozwolone (zgłoszony adres, leczenie); 3 — praca zarobkowa → utrata świadczenia (także w drugim tytule — ZUS); 4 — czynności życia codziennego → brak; 5 — aktywność niezgodna z celem → utrata; 6 — wyjaśnienie wiarygodne → brak sankcji.
""",
    "przyklady/tydzien_07/umowy_do_oceny.md": """# Sześć umów „o dzieło” do oceny — lekcja „Umowa zlecenia i o dzieło”

Dla każdej: dzieło czy zlecenie/świadczenie usług (dlaczego), ryzyko przekwalifikowania (ZUS), co z RUD.

1. „Wykonanie 40 zdjęć produktów do katalogu, z przeniesieniem praw autorskich, odbiór protokołem” — 3 000 zł.
2. „Prowadzenie comiesięcznych szkoleń BHP dla nowych pracowników przez 12 miesięcy” — 500 zł/mies.
3. „Przygotowanie i wygłoszenie jednorazowego wykładu autorskiego o HACCP (2 h) z materiałami” — 1 200 zł.
4. „Sprzątanie biura 3 razy w tygodniu” — 1 800 zł/mies.
5. „Opracowanie regulaminu ZFŚS wraz z tabelą progów” — 2 500 zł.
6. „Obsługa stoiska targowego 20–22.11” — 900 zł.

Klucz: 1 dzieło ✔ (utwór, odbiór); 2 zlecenie (czynności cykliczne, staranne działanie); 3 dzieło ✔ (jednorazowy utwór — wykład autorski); 4 zlecenie (czynności ciągłe; test art. 22); 5 dzieło ✔ (rezultat — dokument; opisz rezultat, nie „doradztwo”); 6 zlecenie (wykonywanie czynności w czasie). RUD w 7 dni dla 1, 3, 5 (gdy wykonawca nie jest pracownikiem zamawiającego).
""",
    "przyklady/tydzien_11/dane_luka_placowa.md": """# Dane do policzenia luki płacowej — kategoria „pakowacz” (18 osób) — fikcyjne

Wynagrodzenie całkowite = zasadnicze + dodatek stażowy + średnia dodatku nocnego (zł/mies.) + średnia premii z 12 mies.

| Nr | Płeć | Zasadnicze | Staż w firmie (lata) | Dodatek stażowy (2%/rok) | Nocne (śr. zł/mies.) | Premia (śr.) | Całkowite |
|---|---|---|---|---|---|---|---|
| 1 | M | 4 900 | 6 | 588 | 160 | — | 5 400 (zaokr.) |
| 2 | M | 4 900 | 5 | 490 | 150 | — | 5 300 |
| 3 | M | 4 900 | 4 | 392 | 120 | — | 5 250 (zaokr.) |
| 4 | M | 4 900 | 4 | 392 | 100 | — | 5 200 |
| 5 | M | 4 900 | 4 | 392 | 100 | — | 5 200 |
| 6 | M | 4 900 | 3 | 294 | 100 | — | 5 150 (zaokr.) |
| 7 | M | 4 900 | 4 | 392 | 100 | — | 5 200 |
| 8 | M | 4 900 | 3 | 294 | 50 | — | 5 140 (zaokr.) |
| 9 | K | 4 900 | 4 | 392 | 50 | — | 5 150 (zaokr.) |
| 10 | K | 4 900 | 3 | 294 | 50 | — | 5 100 (zaokr.) |
| 11 | K | 4 900 | 3 | 294 | 0 | — | 5 050 (zaokr.) |
| 12 | K | 4 900 | 3 | 294 | 0 | — | 5 000 (zaokr.) |
| 13 | K | 4 900 | 3 | 294 | 0 | — | 5 000 (zaokr.) |
| 14 | K | 4 900 | 3 | 294 | 0 | — | 5 000 (zaokr.) |
| 15 | K | 4 806 | 3 | 288 | 0 | — | 4 950 (zaokr.) |
| 16 | K | 4 806 | 3 | 288 | 0 | — | 4 950 (zaokr.) |
| 17 | K | 4 806 | 3 | 288 | 0 | — | 4 950 (zaokr.) |
| 18 | K | 4 806 | 3 | 288 | 0 | — | 4 950 (zaokr.) |

Uwaga: w kolumnie „Całkowite” kwoty są zaokrąglone do użycia w ćwiczeniu; licz na nich. Średni staż: M 4,1 roku, K 3,1; średnie nocne: M 110, K 12,5 — w ćwiczeniu przyjmij uproszczone wartości z treści lekcji (M +1,5 roku stażu, nocne M 110 / K 50) i zobacz, jak zmienia to wniosek.
""",
}

# treść dopisywana do pliku startowego ćwiczenia (po treści zadania) — tam, gdzie ćwiczenie wymaga tabeli/listy/szablonu
EXTRA_START = {
    "start_jak_sie_uczyc_2": "## Szablon FIRMA.md (gdy wolisz napisać ręcznie)\n\n# AGRO-MLEKO sp. z o.o.\n## Zatrudnienie\n- liczba osób / etatów: \n- umowy cywilne: \n## Czas pracy\n- biuro: \n- produkcja: \n## Wynagrodzenia\n- termin wypłaty: \n- składniki (stażowy, premia, nocne): \n## ZUS i zasiłki\n- płatnik zasiłków (tak/nie, dlaczego): \n- stopa wypadkowa: \n## Regulaminy\n- pracy, wynagradzania, ZFŚS, PPK: \n",
    "narzedzia_kadrowca_1": "## Tabela do uzupełnienia\n\n| System | Do czego | Kto w firmie | Pełnomocnictwo | Podpisuje |\n|---|---|---|---|---|\n| eZUS | podgląd ubezpieczonych, e-ZLA, saldo, wysyłka ePłatnikiem | specjalista ds. kadr i płac | PEL (ZUS-PEL) | prezes zarządu |\n| Płatnik | | | | |\n| e-Urząd Skarbowy | | | | |\n| PPK (PFR TFI) | | | | |\n| praca.gov.pl | | | | |\n| program kadrowy | | | | |\n",
    "rekrutacja_jawnosc_1": "## Szablon ogłoszenia\n\n# Ogłoszenie: osoba na stanowisko …\n**Dział i organizacja pracy:** \n**Wynagrodzenie:** … – … zł brutto (zasadnicze) + składniki zmienne: \n**Zadania:** \n**Wymagania:** \n**Oferujemy:** \n**Klauzula informacyjna (RODO):** Administratorem danych jest … Dane przetwarzamy w celu … na podstawie … Przechowujemy … Masz prawo … \n☐ Zgoda na przyszłe rekrutacje (12 miesięcy)\n",
    "umowa_o_prace_1": "## Tabela limitu 33/3\n\n| Osoba | Umowa z kolei (z limitu) | Miesiące wykorzystane | Miesiące do limitu | Data, po której tylko nieokreślona |\n|---|---|---|---|---|\n| Anna Kowalczyk | | | | |\n| Marek Zieliński | | | | |\n| Jakub Krawczyk | | | | |\n",
    "onboarding_akta_1": "## Harmonogram onboardingu\n\n| Termin | Dokument / czynność | Akta (A–E) | Podstawa |\n|---|---|---|---|\n| | | | |\n(10 wierszy)\n",
    "onboarding_akta_2": "## 20 dokumentów do posortowania (A / B / C / D / E / poza aktami / usunąć)\n\n1. Kwestionariusz osobowy kandydata\n2. Orzeczenie lekarskie z badań wstępnych\n3. Umowa o pracę\n4. Informacja o warunkach zatrudnienia (art. 29 §3)\n5. Karta szkolenia wstępnego BHP\n6. Oświadczenie o zapoznaniu z regulaminem pracy\n7. PIT-2\n8. Umowa o prowadzenie PPK\n9. Orzeczenie z badań okresowych\n10. Wniosek urlopowy z 2025 r.\n11. Ewidencja czasu pracy za 2025 r.\n12. Kara nagany z 2024 r. (pracownik od tego czasu bez uwag)\n13. Protokół kontroli trzeźwości sprzed 14 miesięcy (wynik negatywny)\n14. Wypowiedzenie umowy (kopia) z 2026 r.\n15. Świadectwo pracy (kopia)\n16. CV kandydata, którego nie zatrudniono (rekrutacja zakończona 2025, brak zgody)\n17. Zaświadczenie ZUS o okresach ubezpieczenia (staż)\n18. Upoważnienie do przetwarzania danych osobowych\n19. Karta ewidencji przydziału odzieży roboczej\n20. Umowa o zakazie konkurencji\n",
    "czas_pracy_systemy_1": "## Wymiar 2027 — tabela\n\n| Miesiąc | Pełne tygodnie × 40 | Dni wystające × 8 | Święta × 8 (które?) | Wymiar | Warsztat |\n|---|---|---|---|---|---|\n| I | | | | | |\n| IV | | | | | |\n| V | | | | | |\n(pozostałe miesiące — zadanie dodatkowe)\n",
    "ewidencja_czasu_1": "## Karta ewidencji czasu pracy — grudzień 2026 — operator linii (równoważny 12 h)\n\n| Data | Dzień | Od–do | Godziny pracy | Nocne (22–6) | Nadgodziny (nr polecenia) | Kod nieobecności / dnia wolnego | Uwagi |\n|---|---|---|---|---|---|---|---|\n| 01.12 | wt | | | | | | |\n| 02.12 | śr | | | | | | |\n| 03.12 | czw | | | | | | |\n| 04.12 | pt | | | | | | |\n| 05.12 | sb | | | | | | |\n| 06.12 | nd | | | | | | |\n| 07.12 | pn | | | | | | |\n| 08.12 | wt | | | | | | |\n| 09.12 | śr | | | | | | |\n| 10.12 | czw | | | | | | |\n| 11.12 | pt | | | | | | |\n| 12.12 | sb | | | | | | |\n| 13.12 | nd | | | | | | |\n| 14.12 | pn | | | | | | |\n| 15.12 | wt | | | | | | |\n\nSuma 1–15.12: praca … h, nocne … h, nadgodziny … h, UW … h, CH … dni. Kody: D/N zmiana, W5, WN, WŚ, UW, UŻ, CH, SW, UO, UB.\n",
    "urlop_wypoczynkowy_1": "## Tabela\n\n| Osoba | Staż urlopowy | Wymiar roczny | Etat | Proporcja (miesiące/12) | Dni / godziny u Ciebie | Na żądanie |\n|---|---|---|---|---|---|---|\n| Piotr Nowak | | | | | | |\n| Anna Kowalczyk | | | | | | |\n| Jakub Krawczyk | | | | | | |\n",
    "staz_pracy_2026_1": "## Okresy do oceny\n\n| Okres | Tytuł | Wliczam? | Dlaczego |\n|---|---|---|---|\n| szkoła średnia | nauka | | |\n| 2012–2016 | etat | | |\n| 2016–2018 | zlecenie z ubezpieczeniem | | |\n| 2017–2018 | drugie zlecenie (równoległe) | | |\n| 2018–2019 (6 mies.) | działalność — ulga na start | | |\n| 2019–2021 | działalność — składki preferencyjne | | |\n| 2021–nadal | AGRO-MLEKO | | |\nStaż ogólny przed: … / po: …; wymiar urlopu: …\n",
    "urlopy_rodzicielskie_1": "## Kalendarz\n\n| Część | Kto | Od | Do | Tygodni | % zasiłku | Kod RSA |\n|---|---|---|---|---|---|---|\n| macierzyński | matka | 3.12.2026 | | 20 | | 327 |\n| rodzicielski | matka | | | | | 319 |\n| ojcowski | ojciec | | | 2 | | 325 |\n| rodzicielski (9 tyg.) | ojciec | | | 9 | | 319 |\n",
    "nieobecnosci_inne_1": "## Tabela 12 nieobecności (uzupełnij przy okazji — zadanie tygodnia)\n\n| Nieobecność | Podstawa | Limit roczny | % wynagrodzenia | Dzielnik | Kod RSA |\n|---|---|---|---|---|---|\n| siła wyższa | art. 148¹ | 2 dni / 16 h | 50% | wymiar godzin | — |\n| urlop opiekuńczy | art. 173¹ | 5 dni | 0% | wymiar godzin | 151 |\n| art. 188 | | | | | |\n| okolicznościowy (ślub, pogrzeb) | | | | | |\n| urlop bezpłatny | | | | | |\n| choroba | | | | | |\n| opieka (zasiłek) | | | | | |\n| krwiodawstwo | | | | | |\n| wezwanie do sądu | | | | | |\n| badania okresowe | | | | | |\n| szkolenie BHP | | | | | |\n| poszukiwanie pracy (art. 37) | | | | | |\n\n## Rozliczenie listopada — Ewa Sobczak\n| Zdarzenie | Godziny | % | Potrącenie | Kod |\n|---|---|---|---|---|\n",
    "lista_plac_krok_1": "## Osiem kroków (wpisz kwoty)\n\n1. Przychód oskładkowany: \n2. Składki: emerytalna … rentowa … chorobowa … = \n3. Podstawa zdrowotnej … → zdrowotna \n4. PPK pracodawcy (przychód): \n5. Podstawa PIT (zaokr.): \n6. Zaliczka (zaokr.): \n7. PPK pracownika: \n8. Netto: \nBilans: netto + obciążenia = brutto? \nKoszt pracodawcy: \n",
    "zaliczka_pit_1": "## Oświadczenia\n\n| Osoba | PIT-2: kwota zmniejszająca (1/12, 1/24, 1/36, brak) | KUP (250/300) | Inne pola PIT-2 | Zaliczka z oświadczeniem | Zaliczka bez |\n|---|---|---|---|---|---|\n| Halina Mazur | | | | | |\n| Piotr Nowak | | | | | |\n| Agnieszka Pawlak | | | | | |\n",
    "koszt_pracodawcy_1": "## Tabela kosztu\n\n| Osoba | Brutto | Emer. 9,76 | Rent. 6,5 | Wyp. 1,2 | FP 2,45 | FGŚP 0,1 | PPK 1,5 | Koszt mies. | × 12 | ZFŚS | Koszt roczny |\n|---|---|---|---|---|---|---|---|---|---|---|---|\n| Halina Mazur | 7 800 | | | | | | 0 | | | 2 943,23 | |\n| Tomasz Lis | 14 000 | | | | | | | | | 2 943,23 | |\n| Piotr Nowak | 2 500 | | | | | | 0 | | | 1 471,62 | |\n",
    "potracenia_1": "## Rachunek\n\nNetto: \nGranica (1/2 lub 3/5): \nKwota wolna (parametry pracownika): \nPotrącenie = min(granica, netto − wolna, zajęcie): \nZostaje pracownikowi: \n\n## Odpowiedź komornikowi (3 zdania)\n",
    "swiadczenia_pozaplacowe_1": "## Tabela 10 świadczeń\n\n| Świadczenie | ZUS (tak/nie) | PIT (tak/nie/limit) | Warunek / podstawa |\n|---|---|---|---|\n| auto prywatnie, ryczałt 400 | | | |\n| karta sportowa 150, pracownik płaci 1 zł | | | |\n| pakiet medyczny za 1 zł | | | |\n| paczka świąteczna z ZFŚS 400 wg dochodu | | | |\n| wczasy pod gruszą ZFŚS 1 500 | | | |\n| nagroda jubileuszowa za 20 lat | | | |\n| posiłki w stołówce 300/mies. | | | |\n| telefon służbowy prywatnie | | | |\n| szkolenie z Excela | | | |\n| ekwiwalent za pranie 40 zł | | | |\n",
    "chorobowe_podstawy_1": "## Tabela zwolnień\n\n| Zwolnienie | Dni | Chorobowe (pracodawca) | Zasiłek | Kwoty | Okres zasiłkowy | RSA |\n|---|---|---|---|---|---|---|\n| 9–20.03 | | | | | | |\n| 20–31.07 | | | | | | |\n| 16–30.11 | | | | | | |\n",
    "podstawa_zasilku_1": "## 12 miesięcy (przepisz z przyklady/tydzien_06/kartoteka_zielinski.md)\n\n| Miesiąc | Stałe | Zmienne (wliczane) | Dni obow. | Dni przepr. | Status (pełny / uzupełniony / wyłączony) | Kwota do średniej |\n|---|---|---|---|---|---|---|\n(12 wierszy)\nSuma … / liczba miesięcy … = … ; − 13,71% → … ; minimum 4 147,10? ; stawka dzienna … ; 80% = …\n",
    "zasilki_inne_1": "## Z-15A — kluczowe pola\n\n- Dane ubezpieczonej: \n- Dane dziecka (PESEL/data ur.): \n- Okres opieki: \n- Oświadczenie o braku innego opiekuna: \n- Dni opieki wykorzystane w roku: ja … / drugi rodzic … \n- Numer e-ZLA: \n\n## Rachunek\nStawka dzienna … × 80% = … × dni … = … ; pomniejszenie pensji … ; RSA: kod … od … do … dni … kwota … ; limit rodziny: 60 − … − … = …\n",
    "kontrola_l4_2026_1": "## Ocena 6 sytuacji\n\n| Nr | Sytuacja | Kwalifikacja | Podstawa | Skutek |\n|---|---|---|---|---|\n| 1 | sklep internetowy | | | |\n| 2 | narty po operacji kolana | | | |\n| 3 | wyjazd do rodziny (depresja) | | | |\n| 4 | apteka i zakupy (grypa) | | | |\n| 5 | odpłatna joga (ciąża) | | | |\n| 6 | nie zastano pod adresem | | | |\n",
    "zlecenie_dzielo_1": "## Tabela\n\n| Osoba | Tytuły | Schemat składek | Stawka/h (≥ 31,40?) | Składki | Zdrowotna | KUP | Zaliczka | Netto | Dokument ZUS |\n|---|---|---|---|---|---|---|---|---|---|\n| Agnieszka Pawlak | | | | | | | | | |\n| Robert Król | | | | | | | | | |\n| Michał Dąbrowski | | | | | | | | | |\n",
    "ppk_1": "## Tabela\n\n| Osoba | Podstawa wpłat | Pracownik % / zł | Pracodawca % / zł | Zmiana netto | Umowa o prowadzenie — termin | Przekazanie do instytucji |\n|---|---|---|---|---|---|---|\n| Anna Kowalczyk | | | | | | |\n| Piotr Nowak | | | | | | |\n| Robert Król | | | | | | |\n",
    "cudzoziemcy_b2b_1": "## Checklista — operator z Gruzji od 4.01.2027\n\n| Kiedy | Co | Kto | Gdzie w aktach |\n|---|---|---|---|\n(12 wierszy)\n",
    "cudzoziemcy_b2b_2": "## Test 8 cech — 3 umowy\n\n| Cecha | A informatyk | B doradca | C kierowca |\n|---|---|---|---|\n| podporządkowanie | | | |\n| miejsce | | | |\n| czas | | | |\n| osobiste świadczenie | | | |\n| ryzyko | | | |\n| sprzęt | | | |\n| wyłączność | | | |\n| kary/urlopy | | | |\n| **Suma / werdykt** | | | |\nRyzyko składkowe (A, 3 lata): \n",
    "zus_zgloszenia_1": "## Tabela zgłoszeń\n\n| Osoba | Dokument | Kod tytułu | Data powstania | Termin | UPP (z symulatora) |\n|---|---|---|---|---|---|\n| Anna Kowalczyk | | | | | |\n| Ewa Sobczak | | | | | |\n| Agnieszka Pawlak | | | | | |\n| Robert Król | | | | | |\n| Joanna Michalska | | | | | |\n",
    "zus_rozliczenia_1": "## Komplet 12/2026 (wypłata 10.12)\n\nRCA (osoby, kody, podstawy): \nRSA (kod, okres, dni, kwota, czy odliczana): \nDRA: liczba ubezpieczonych …, składki …, zasiłki do odliczenia …, do zapłaty …, identyfikator …, termin …\n",
    "zus_korekty_1": "## Korekta — student po utracie statusu\n\n1. Dokumenty zgłoszeniowe (typ, kod, data, termin): \n2. Komplety korygujące (identyfikator, zawartość): \n3. Składki do dopłaty (część zleceniobiorcy / zleceniodawcy / zdrowotna): \n4. Odsetki (od kiedy, stopa): \n5. PIT: \n6. PPK: \n7. Do akt / procedura: \n",
    "pit_roczny_1": "## PIT-11 za 2026 — Anna Kowalczyk\n\n- Przychód ze stosunku pracy: \n- KUP: \n- Dochód: \n- Zaliczka pobrana: \n- Składki społeczne: \n- Składka zdrowotna (informacyjnie): \n- Co trafia do PIT-11 za 2027: \n\n## Uzgodnienie PIT-4R\n| Miesiąc | Zaliczka należna | Wpłata | Różnica | Wyjaśnienie |\n|---|---|---|---|---|\n",
    "zfss_pfron_1": "## Kalkulator\n\nZFŚS 2027: etaty … × odpis … = … ; zwiększenia … × 6,25% × … = … ; razem … ; 75% do 31.05: … ; reszta do 30.09: … ; korekta 31.12 wg …\nPFRON: 6% × etaty … = … ; zatrudnionych z orzeczeniem … ; brakuje … × 40,65% × przeciętne … = … /mies. (DEK-I-0 do 20.)\nSOD: … (Wn-D do 25.); warunki: \n",
    "kalendarz_roczny_1": "## Kalendarz — szablon\n\n### Terminy miesięczne (powtarzalne)\n| Dzień | Zdarzenie | Podstawa | Właściciel | Zastępca | Alert | Przesunięcie, gdy dzień wolny |\n|---|---|---|---|---|---|---|\n| 5 | zamknięcie ewidencji | | | | | |\n| 8 | lista płac | | | | | |\n| 10 | wypłata | art. 85 | | | | poprzedni roboczy |\n| 15 | ZUS + PPK | | | | | następny roboczy |\n| 20 | PIT + DEK-I-0 | | | | | następny roboczy |\n| 25 | Wn-D | | | | | |\n\n### Terminy roczne\n| Data | Zdarzenie | Podstawa | Właściciel |\n|---|---|---|---|\n| 31.01 | PIT-4R, PIT-8AR, PIT-11 do US; IWA | | |\n| 28.02 | PIT-11 pracownikom; informacja o autozapisie PPK (2027) | | |\n| 31.05 | 75% odpisu ZFŚS | | |\n| 30.09 | reszta odpisu; urlopy zaległe | | |\n| 30.11 | stan ubezpieczonych do chorobowego (płatnik zasiłków) | | |\n| 31.12 | korekta ZFŚS; przegląd retencji | | |\n\n### Cykliczne (per pracownik) / zdarzeniowe / zmiany prawa\n| Zdarzenie | Termin | Podstawa | Właściciel |\n|---|---|---|---|\n\n### Alert tygodnia 11–15.01.2027\n| Termin | Zdarzenie | Podstawa | Właściciel | Co robisz |\n|---|---|---|---|---|\n",
    "rozwiazanie_umowy_1": "## Tabela\n\n| Osoba | Staż zakładowy | Okres | Koniec | Przyczyna wymagana? | Konsultacja | Ochrona |\n|---|---|---|---|---|---|---|\n| Halina Mazur | | | | | | |\n| Marek Zieliński | | | | | | |\n| Anna Kowalczyk | | | | | | |\n| Jakub Krawczyk | | | | | | |\n",
    "odprawy_grupowe_1": "## Lista 12 osób działu pakowania (do redukcji „na papierze”)\n\n| Nr | Osoba | Staż zakładowy | Pensja | Wiek | Sytuacja | Odprawa | Ochrona |\n|---|---|---|---|---|---|---|---|\n| 1 | Halina Mazur | 17 lat | 7 800 | 54 | | | |\n| 2 | Tomasz Lis | 11 lat | 14 000 | 47 | | | |\n| 3 | Piotr Nowak | 7 lat | 2 500 (1/2) | 41 | | | |\n| 4 | Marek Zieliński | 1 r. 11 m. | 5 400 | 38 | | | |\n| 5 | P5 | 9 lat | 5 300 | 35 | w ciąży | | |\n| 6 | P6 | 12 lat | 5 400 | 63 | | | |\n| 7 | P7 | 3 lata | 5 000 | 29 | | | |\n| 8 | P8 | 1 rok | 4 950 | 24 | | | |\n| 9 | P9 | 6 lat | 5 200 | 44 | | | |\n| 10 | P10 | 2 lata | 5 000 | 31 | na urlopie rodzicielskim | | |\n| 11 | P11 | 15 lat | 5 600 | 52 | społeczny inspektor pracy | | |\n| 12 | P12 | 4 lata | 5 100 | 39 | | | |\n",
    "swiadectwo_rozliczenie_1": "## Świadectwo (ust. 1–8)\n\n1. \n2. \n3. (tryb i podstawa — bez przyczyny) \n4. urlop: \n5. bezpłatny: \n6. chorobowe (art. 92): \n7. nieskładkowe: \n8. zajęcie: \n\n## ZWUA: data …, kod …, tryb …, termin …\n\n## Lista końcowa (10.12)\n| Pozycja | Kwota | ZUS | PIT |\n|---|---|---|---|\n",
    "mobbing_dyskryminacja_2026_1": "## Kwalifikacja 5 kazusów\n\n| Nr | Kazus | Kwalifikacja | Podstawa | Roszczenia / reakcja pracodawcy |\n|---|---|---|---|---|\n| 1 | wyśmiewanie za jąkanie | | | |\n| 2 | awans a ciąża | | | |\n| 3 | różne premie | | | |\n| 4 | „leń” jednorazowo | | | |\n| 5 | 58-latek bez szkoleń | | | |\n",
    "jawnosc_wynagrodzen_1": "## Luka — kategoria „pakowacz”\n\n| | n | Średnia | Mediana |\n|---|---|---|---|\n| M | 8 | | |\n| K | 10 | | |\nLuka (średnia): (śr M − śr K)/śr M = … % ; (mediana): … %\nRozkład: staż … zł; nocne … zł; po korekcie: M … / K … → … %\nWniosek i działanie: \n",
    "sygnalisci_zdalna_rodo_1": "## Praca zdalna — Ewa Sobczak\n\n1. Odpowiedź (termin, treść): \n2. Porozumienie (10 elementów): \n3. Kalkulacja ryczałtu: energia … kWh × … = … ; internet … ; razem … → ryczałt … zł\n4. Dokumenty BHP/RODO: \n",
    "sygnalisci_zdalna_rodo_2": "## Mini-audyt RODO i compliance w kadrach\n\n| # | Pytanie | Stan (TAK/NIE/CZĘŚCIOWO) | Podstawa | Ryzyko | Działanie | Termin | Właściciel |\n|---|---|---|---|---|---|---|---|\n| 1 | Czy każda osoba z dostępem do danych kadrowych ma upoważnienie? | | | | | | |\n| 2 | Czy jest rejestr czynności przetwarzania (RCPD)? | | | | | | |\n| 3 | Czy są umowy powierzenia (program w chmurze, biuro rachunkowe)? | | | | | | |\n| 4 | Czy jest tabela retencji i harmonogram usuwania? | | | | | | |\n| 5 | Czy kontrola trzeźwości ma podstawę w regulaminie i informację 2 tyg.? | | | | | | |\n| 6 | Czy monitoring (wizyjny, poczta) jest opisany w regulaminie z informacją dla pracowników? | | | | | | |\n| 7 | Czy jest procedura naruszeń (72 h) i rejestr naruszeń? | | | | | | |\n| 8 | Czy jest procedura zgłoszeń wewnętrznych (sygnaliści ≥ 50)? | | | | | | |\n| 9 | Czy klauzule informacyjne są aktualne (kandydaci, pracownicy, rodziny)? | | | | | | |\n| 10 | Czy praca zdalna ma procedurę ochrony danych? | | | | | | |\n",
    "kontrola_pip_zus_1": "## Teczka kontrolna — 40 dokumentów\n\n| # | Dokument | Gdzie (folder/system) | Ostatnia aktualizacja | Właściciel | Status |\n|---|---|---|---|---|---|\n| 1 | regulamin pracy (z obwieszczeniem o systemach czasu pracy) | | | | |\n| 2 | regulamin wynagradzania | | | | |\n| 3 | regulamin ZFŚS + tabela progów | | | | |\n| 4 | procedura antymobbingowa | | | | |\n| 5 | procedura zgłoszeń wewnętrznych | | | | |\n| 6 | regulamin pracy zdalnej / porozumienia | | | | |\n| 7 | zasady kontroli trzeźwości i monitoringu + informacje dla pracowników | | | | |\n| 8 | ewidencja czasu pracy (36 mies.) | | | | |\n| 9 | harmonogramy / grafiki | | | | |\n| 10 | polecenia nadgodzin, wnioski o czas wolny | | | | |\n| 11 | listy płac i kartoteki (36 mies.) | | | | |\n| 12 | umowy o pracę, aneksy, informacje 29 §3 | | | | |\n| 13 | akta osobowe A–E + wykaz | | | | |\n| 14 | orzeczenia lekarskie, karty BHP, ocena ryzyka | | | | |\n| 15 | umowy zlecenia + ewidencje godzin + oświadczenia | | | | |\n| 16 | umowy o dzieło + protokoły odbioru + RUD | | | | |\n| 17 | ZUA/ZZA/ZWUA + UPP (rejestr) | | | | |\n| 18 | DRA/RCA/RSA/RPA + UPP + przelewy NRS | | | | |\n| 19 | IWA, zawiadomienie o stopie wypadkowej | | | | |\n| 20 | dokumentacja zasiłkowa (Z-15, protokoły powypadkowe, kontrole L4) | | | | |\n| 21 | PIT-4R, PIT-8AR, PIT-11 + UPO, potwierdzenia doręczeń | | | | |\n| 22 | PPK: umowa o zarządzanie, rejestr uczestników, rezygnacje, pliki wpłat | | | | |\n| 23 | PFRON: DEK-I-0, Wn-D, orzeczenia | | | | |\n| 24 | ZFŚS: plan odpisu, przelewy, protokoły komisji, oświadczenia | | | | |\n| 25 | cudzoziemcy: tytuły pobytu, powiadomienia, oświadczenia | | | | |\n| 26 | plan urlopów, karty urlopowe | | | | |\n| 27 | świadectwa pracy (kopie), wypowiedzenia | | | | |\n| 28 | rejestr kar porządkowych | | | | |\n| 29 | rejestr wypadków, Z-KW | | | | |\n| 30 | upoważnienia RODO, RCPD, umowy powierzenia, tabela retencji | | | | |\n| 31 | procedura naruszeń RODO | | | | |\n| 32 | rejestr zgłoszeń (sygnaliści, mobbing) | | | | |\n| 33 | pełnomocnictwa PEL, UPL-1 | | | | |\n| 34 | książka kontroli | | | | |\n| 35 | protokoły poprzednich kontroli i odpowiedzi | | | | |\n| 36 | kalendarz kadrowo-płacowy | | | | |\n| 37 | siatka płac, wartościowanie stanowisk, analiza luki | | | | |\n| 38 | szkolenia kadry (listy obecności) | | | | |\n| 39 | ogłoszenia rekrutacyjne (wzory) i klauzule | | | | |\n| 40 | instrukcja „wizyta inspektora” | | | | |\n\n## Kontrola ZUS 1.12.2026 — przygotowanie, przebieg, ustalenia, środki\n",
    "kontrola_pip_zus_2": "## Audyt skrócony — 20 pytań\n\n| # | Obszar | Pytanie | Podstawa | Dowód | Stan | Ryzyko | Działanie | Termin | Właściciel |\n|---|---|---|---|---|---|---|---|---|---|\n| 1 | umowy | limit 33/3, próbne wg planu | | | | | | | |\n| 2 | umowy | przyczyna przy wypowiedzeniu określonej | | | | | | | |\n| 3 | czas pracy | ewidencja od–do, polecenia | | | | | | | |\n| 4 | czas pracy | odpoczynki 11/35, grafiki miesiąc + tydzień | | | | | | | |\n| 5 | płace | dodatki 50/100%, nocne z wymiaru | | | | | | | |\n| 6 | płace | składki osobno, zaokrąglenia, bilans | | | | | | | |\n| 7 | płace | kwoty wolne per pracownik | | | | | | | |\n| 8 | zasiłki | pula 33/14, podstawy wg regulaminu | | | | | | | |\n| 9 | zlecenia | stawka ≥ 31,40, ewidencja, oświadczenia, student | | | | | | | |\n| 10 | ZUS | zgłoszenia 7 dni, kody, ZWUA z trybem | | | | | | | |\n| 11 | ZUS | komplety = listy, RSA właściwy miesiąc | | | | | | | |\n| 12 | PIT | PIT-4R = przelewy, PIT-11 doręczone | | | | | | | |\n| 13 | ZFŚS | kryterium, terminy 31.05/30.09 | | | | | | | |\n| 14 | PFRON | wskaźnik, DEK, SOD z efektem zachęty | | | | | | | |\n| 15 | akta | A–E, 10 lat, czyszczenie D/E | | | | | | | |\n| 16 | BHP | badania, szkolenia w terminach | | | | | | | |\n| 17 | compliance | mobbing (5.05.2027), sygnaliści | | | | | | | |\n| 18 | compliance | zdalna, monitoring, trzeźwość | | | | | | | |\n| 19 | RODO | upoważnienia, retencja, powierzenia, 72 h | | | | | | | |\n| 20 | organizacja | teczka kontrolna, kalendarz, książka kontroli | | | | | | | |\n\n## Plan działań po protokole PIP (8 punktów, daty od 24.11.2026)\n",
    "powtorka_etap_4_1": "## Audyt — 10 wierszy\n\n| Obszar | Pytanie | Podstawa | Dowód | Stan | Ryzyko (zł, sankcja) | Działanie | Termin | Właściciel |\n|---|---|---|---|---|---|---|---|---|\n| Umowy | | | | | | | | |\n| Ewidencja | | | | | | | | |\n| Nadgodziny | | | | | | | | |\n| Zasiłki | | | | | | | | |\n| Zlecenia | | | | | | | | |\n| ZUS | | | | | | | | |\n| PIT | | | | | | | | |\n| ZFŚS/PFRON | | | | | | | | |\n| Procedury | | | | | | | | |\n| Teczka/kalendarz | | | | | | | | |\nPriorytety 1–3: \nHarmonogram 30/60/90 dni: \n",
}
