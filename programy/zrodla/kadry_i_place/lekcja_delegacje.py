# -*- coding: utf-8 -*-
"""Lekcja „Podróże służbowe: diety, ryczałty, kilometrówka” + bloki standardu. Stan prawny: XI 2026
(dieta krajowa 45 zł — t.j. Dz.U. 2023 poz. 2190; projekt 60 zł od 1.01.2027 nieogłoszony)."""

LEKCJA_DELEGACJE = {
    "id": "delegacje", "tydzien": 7, "nazwa": "Podróże służbowe: diety, ryczałty, kilometrówka — krajowe i zagraniczne",
    "slowa": ["delegacja", "podróż służbowa", "podroz sluzbowa", "dieta", "diety", "kilometrówka", "kilometrowka", "ryczałt za nocleg", "polecenie wyjazdu", "dieta zagraniczna", "kierowca"],
    "cel": "rozliczasz krajową i zagraniczną podróż służbową (diety, pomniejszenia, noclegi, dojazdy, kilometrówka), rozliczasz zaliczkę i wiesz, która część jest przychodem na liście płac.",
    "czas_min": 60,
    "wyjasnienie": """## Co to jest podróż służbowa (art. 77⁵ KP)
Podróż służbowa ma trzy cechy naraz. Pracodawca wydaje polecenie. Pracownik wykonuje zadanie służbowe. Robi to poza miejscowością siedziby firmy albo poza stałym miejscem pracy z umowy.
Brakuje jednej cechy — to nie jest delegacja. Wtedy nie ma diet.
Pracodawca prywatny (AGRO-MLEKO) ustala należności w regulaminie wynagradzania. Może dać więcej niż rozporządzenie. Nie może dać diety niższej niż 45 zł. Bez własnych zapisów stosuje rozporządzenie w całości.

| Sytuacja | Czy to delegacja? | Co przysługuje |
|---|---|---|
| Handlowiec z Krakowa jedzie na 2 dni do Gdańska | tak | diety, nocleg, przejazd, dojazdy |
| Operator z Krakowa pracuje 3 miesiące w zakładzie w Tarnowie (aneks: miejsce pracy Tarnów) | nie — oddelegowanie (zmiana miejsca pracy) | wynagrodzenie; diet nie ma |
| Serwisant ma w umowie miejsce pracy „województwo małopolskie” | nie — porusza się w swoim miejscu pracy | zwrot kosztów wg regulaminu (jazdy lokalne), bez diet |
| Kierowca w przewozie krajowym poza Kraków | tak (art. 2 pkt 7 ustawy o czasie pracy kierowców) | jak pracownik sfery budżetowej (art. 21a) |
| Kierowca w przewozie międzynarodowym | nie (art. 21b, od 2.02.2022) | zamiast diet: wyłączenia z ZUS i PIT (art. 26f) |

## Pięć składników należności (§ 2 rozporządzenia)
- Diety — na wyżywienie.
- Zwrot kosztów przejazdu — bilety albo kilometrówka.
- Zwrot kosztów dojazdów komunikacją miejscową — ryczałt.
- Zwrot kosztów noclegu — rachunek albo ryczałt.
- Inne niezbędne, udokumentowane wydatki — parking, autostrada, bagaż.
Pracodawca wskazuje środek transportu w poleceniu wyjazdu. Samochód prywatny — tylko na wniosek pracownika i za zgodą.

## Dieta krajowa: 45 zł za dobę (§ 7)
Dieta należy się za dobę podróży, nie za dzień kalendarzowy. Doba to 24 godziny od wyjazdu. Liczysz od godziny wyjazdu do godziny powrotu.

| Podróż trwa | Dieta |
|---|---|
| do 24 h: mniej niż 8 h | nie przysługuje |
| do 24 h: od 8 do 12 h | 50% (22,50 zł) |
| do 24 h: ponad 12 h | 100% (45 zł) |
| ponad 24 h: każda pełna doba | 100% |
| ponad 24 h: rozpoczęta doba do 8 h | 50% |
| ponad 24 h: rozpoczęta doba ponad 8 h | 100% |

Zapewniony posiłek pomniejsza dietę. Pomniejszenie liczysz od pełnej diety (45 zł), także wtedy, gdy za daną dobę należy się tylko połowa. Dieta nie może spaść poniżej zera.

| Posiłek zapewniony bezpłatnie | Pomniejszenie krajowe (§ 7 ust. 4) | Pomniejszenie zagraniczne (§ 14 ust. 2) |
|---|---|---|
| śniadanie | 25% (11,25 zł) | 15% |
| obiad | 50% (22,50 zł) | 30% |
| kolacja | 25% (11,25 zł) | 30% |
| całodzienne wyżywienie | dieta nie przysługuje | przysługuje 25% diety |

Dieta nie przysługuje też za delegację do miejscowości, w której pracownik mieszka.

## Nocleg i dojazdy w kraju (§ 8–9)
Nocleg z rachunku zwracasz do 900 zł za dobę hotelową (20 diet). Wyższy rachunek — tylko w uzasadnionym przypadku, za zgodą pracodawcy.
Nocleg bez rachunku to ryczałt 67,50 zł (150% diety). Warunek: nocleg trwał co najmniej 6 godzin między 21:00 a 7:00. Ryczałt nie należy się za nocleg w czasie przejazdu ani gdy pracownik mógł wrócić na noc.
Dojazdy komunikacją miejscową: ryczałt 9 zł (20% diety) za każdą rozpoczętą dobę. Ryczałt nie należy się, gdy pracownik nie ponosi kosztów — jedzie samochodem służbowym albo prywatnym.

## Kilometrówka (rozp. MI z 25.03.2002, Dz.U. 2023 poz. 5)
Stawki maksymalne obowiązują od 17.01.2023.

| Pojazd prywatny | Stawka za 1 km |
|---|---|
| samochód osobowy do 900 cm³ | 0,89 zł |
| samochód osobowy powyżej 900 cm³ | 1,15 zł |
| motocykl | 0,69 zł |
| motorower | 0,42 zł |

Podstawą wypłaty jest ewidencja przebiegu: data, cel, trasa, kilometry, stawka. Pracodawca może ustalić stawkę niższą. Wyższa stawka to przychód pracownika.

## Podróż zagraniczna (§ 12–21)
Czas za granicą liczysz od przekroczenia granicy. Lądowo — w drodze za granicę. Lotniczo — od startu samolotu z ostatniego lotniska w kraju do lądowania na pierwszym lotnisku w kraju. Część krajową (dojazd na lotnisko) rozliczasz jak podróż krajową (§ 21).
Dieta i limit noclegu zależą od państwa (załącznik). Przykłady: Niemcy 49 EUR / 170 EUR, Czechy 41 EUR / 120 EUR, Francja 55 EUR / 200 EUR, Wielka Brytania 45 GBP / 220 GBP.

| Element podróży zagranicznej | Zasada |
|---|---|
| niepełna doba do 8 h | 1/3 diety |
| niepełna doba ponad 8 do 12 h | 1/2 diety |
| niepełna doba ponad 12 h | pełna dieta |
| nocleg bez rachunku | ryczałt 25% limitu |
| dojazd z/do dworca, lotniska, portu | 1 dieta (50%, gdy tylko w jedną stronę) |
| komunikacja miejscowa | 10% diety za każdą rozpoczętą dobę |
| zaliczka | obowiązkowa, w walucie (w PLN — za zgodą pracownika) |
| kurs do rozliczenia | średni NBP z dnia wypłaty zaliczki |

## Rozliczenie, dokumenty, terminy (§ 5, § 11, § 20)
Pracownik rozlicza podróż w 14 dni od powrotu. Dołącza bilety, faktury, rachunki. Gdy dokumentu nie ma, pisze oświadczenie o wydatku i o przyczynie braku dokumentu.
Zaliczka krajowa — na wniosek pracownika. Zaliczka zagraniczna — obowiązkowa.
Polecenie wyjazdu nie ma urzędowego wzoru. Zapisz w nim: kto, dokąd, od kiedy do kiedy, cel, środek transportu, zaliczkę.

## Podatek i składki (art. 21 ust. 1 pkt 16 PIT; § 2 ust. 1 pkt 15 rozp. składkowego)
Diety i należności do limitów z rozporządzenia są wolne od PIT i wyłączone z podstawy składek.
Nadwyżka ponad limit to przychód ze stosunku pracy. Trafia na listę płac jak premia: składki i PIT. Przykład: regulamin daje dietę 70 zł; 25 zł z każdej diety to przychód.
Zwrot noclegu ponad 900 zł za zgodą pracodawcy mieści się w rozporządzeniu (§ 8 ust. 2) — nadal jest zwolniony.
Zleceniobiorca w podróży: zwolnienie z art. 21 ust. 1 pkt 16 lit. b PIT, do tych samych limitów.

## Kierowcy — dwa różne światy
Kierowca w przewozie krajowym jest w podróży służbowej przy każdym przewozie poza miejscowość siedziby. Rozliczasz go jak w tej lekcji.
Kierowca w przewozie międzynarodowym nie jest w podróży służbowej. Nie dostaje diet. Od 19.08.2023 podstawę składek pomniejszasz o równowartość 60 EUR za każdy dzień pobytu za granicą (gdy przychód przekracza prognozowane przeciętne wynagrodzenie), a z PIT zwalniasz równowartość 20 EUR za dzień (art. 26f ustawy o czasie pracy kierowców; art. 21 ust. 1 pkt 23d PIT). Te przepisy zmieniały się kilka razy — przed zastosowaniem sprawdź brzmienie w ISAP.

## Co jest projektem, a co obowiązuje (stan XI 2026)
Obowiązuje: dieta 45 zł, ryczałt za nocleg 67,50 zł, ryczałt na dojazdy 9 zł, limit noclegu 900 zł.
Projekt z 21.05.2026: dieta 60 zł, ryczałt za nocleg 90 zł, dojazdy 12 zł, limit 1 200 zł, nowe diety zagraniczne — planowo od 1.01.2027. Do ogłoszenia w Dzienniku Ustaw nie liczysz nim niczego.""",
    "przyklad": """Handlowiec AGRO-MLEKO, Kraków → Gdańsk (targi), pociągiem.
Wyjazd 16.11.2026 06:00, powrót 17.11.2026 18:30 = 36,5 h → 1 pełna doba + 12,5 h (ponad 8 h) = 2 diety = 90,00.
Śniadanie w hotelu wliczone: − 25% × 45 = − 11,25 → diety 78,75.
Hotel z faktury 380,00 (limit 900 ✔). Dojazdy komunikacją miejscową: 2 rozpoczęte doby × 9,00 = 18,00. Bilety PKP 298,00.
Razem 774,75 − zaliczka 500,00 = do wypłaty 274,75 zł. Całość wolna od PIT i ZUS.""",
    "zadania": [
        "Napisz dla AGRO-MLEKO wzór polecenia wyjazdu i rozliczenia delegacji (jedna strona: kto, dokąd, cel, środek transportu, zaliczka, tabela wydatków, oświadczenie o braku dokumentu).",
        "Policz w Warsztacie trzy warianty jednej podróży (18 h, 36 h, 60 h) z tym samym zestawem posiłków — zapisz, jak zmienia się liczba diet.",
        "Sprawdź w regulaminie wynagradzania AGRO-MLEKO zapis o dietach: jeśli daje 60 zł, policz nadwyżkę dla 12 delegacji handlowca w roku i wskaż jej miejsce na liście płac.",
    ],
    "pytania": [
        ["Podróż trwała dokładnie 12 godzin. Ile diety?", "50% (22,50 zł) — „od 8 do 12 godzin” obejmuje równe 12 h; pełna dieta jest dopiero za ponad 12 h."],
        ["Pracownik jechał własnym autem. Czy dostaje ryczałt 9 zł na dojazdy?", "Nie — ryczałt na dojazdy komunikacją miejscową nie przysługuje, gdy pracownik nie ponosi tych kosztów (§ 9 ust. 2)."],
        ["Regulamin daje dietę 70 zł. Co z 25 zł?", "To przychód ze stosunku pracy: składki ZUS i PIT w liście płac; 45 zł pozostaje wolne."],
    ],
    "pulapki": [
        "Dieta „za dzień kalendarzowy” — rozporządzenie liczy doby od godziny wyjazdu; 2 dni kalendarzowe mogą dać tylko pół diety (np. 20:00 → 7:00 = 11 h = 50%).",
        "Kierowca międzynarodowy z „dietami” jak w delegacji — od 2.02.2022 to nie podróż służbowa; rozliczasz wyłączenia z art. 26f, nie diety.",
        "Rachunek za hotel na 1 100 zł bez zgody pracodawcy — ponad limit 900 zł zwrot wymaga zgody w uzasadnionym przypadku; bez zgody 200 zł nie ma podstawy.",
    ],
    "test": [
        {"p": "Delegacja krajowa od 9:00 do 19:30 tego samego dnia (10,5 h). Dieta?", "o": ["Nie przysługuje", "22,50 zł", "45,00 zł", "67,50 zł"], "odp": 1, "w": "Od 8 do 12 h — 50% diety = 22,50 zł."},
        {"p": "Pracodawca zapewnił obiad w podróży krajowej. Dietę pomniejszasz o:", "o": ["15% diety", "25% diety", "50% pełnej diety", "100% diety"], "odp": 2, "w": "§ 7 ust. 4: obiad = 50% pełnej diety (22,50 zł) — także gdy za dobę należy się tylko połowa."},
        {"p": "Regulamin AGRO-MLEKO: dieta 60 zł. Pracownik był 3 doby w delegacji. Na listę płac trafia:", "o": ["0 zł — diety są zawsze zwolnione", "45 zł przychodu", "180 zł przychodu", "60 zł przychodu"], "odp": 1, "w": "Nadwyżka (60 − 45) × 3 = 45 zł to przychód ze stosunku pracy — składki i PIT."},
        {"p": "Stawka za 1 km samochodem prywatnym powyżej 900 cm³ (od 17.01.2023):", "o": ["0,8358 zł", "0,89 zł", "1,15 zł", "1,30 zł"], "odp": 2, "w": "1,15 zł (Dz.U. 2023 poz. 5); 0,89 zł dotyczy aut do 900 cm³."},
    ],
    "w_praktyce": [
        "Polecenie wyjazdu przed podróżą: cel, miejsce, daty i godziny, środek transportu, zaliczka — podpis pracodawcy.",
        "Po powrocie: rozliczenie w 14 dni z rachunkami; brak rachunku → oświadczenie pracownika; sprawdź limity (900 zł nocleg, stawki km).",
        "Policz w Warsztacie → Delegacje i diety; zapisz rozliczenie do 04-place; kwotę do wypłaty przelej poza listą płac (bez ZUS/PIT).",
        "Nadwyżkę ponad limity (dieta regulaminowa wyższa niż 45 zł, stawka km wyższa niż rozporządzenie) dolicz do listy płac miesiąca jako przychód.",
        "Kierowców rozliczaj osobno: krajowi — delegacja; międzynarodowi — art. 26f (60 EUR składki / 20 EUR PIT), nie diety.",
    ],
}

STANDARD_DELEGACJE = {
    "delegacje": {
        "po_co": "AGRO-MLEKO ma handlowców, serwisantów i kierowców — co miesiąc kilkanaście rozliczeń podróży. Jedna źle policzona doba albo dieta regulaminowa „w całości bez PIT” to zaległe składki i podatek przy kontroli ZUS i US.",
        "wymagania": [
            "Warsztat → Delegacje i diety: kalkulator krajowy i zagraniczny (doby, pomniejszenia, noclegi, dojazdy, kilometrówka, zaliczka) + tabela stawek.",
            "Warsztat → Przepisy: hasła „podróż służbowa”, „dieta 45 zł”, „kilometrówka”, „kierowca”.",
            "Lekcje wcześniejsze: „Lista płac krok po kroku” (gdzie trafia nadwyżka) i „Świadczenia pozapłacowe” (co jest przychodem).",
            "Pojęcia: doba podróży (24 h od wyjazdu, nie dzień kalendarzowy), dieta (45 zł), ryczałt (kwota bez rachunku), limit noclegu (20 diet = 900 zł), kilometrówka (stawka za km × ewidencja przebiegu), nadwyżka ponad limit (przychód na liście płac).",
        ],
        "demonstracja": {
            "tytul": "Handlowiec: Kraków → Gdańsk pociągiem, 16.11 06:00 → 17.11 18:30, śniadanie w hotelu, faktura 380 zł, bilety 298 zł, zaliczka 500 zł",
            "kroki": [
                "„36,5 h → 2 diety”: 16.11 06:00 → 17.11 06:00 to pełna doba (1 dieta); 06:00 → 18:30 to rozpoczęta doba 12,5 h — ponad 8 h, więc pełna dieta. Razem 2 × 45 = 90,00. Dni kalendarzowych też jest 2, ale to zbieg okoliczności — liczysz godziny.",
                "„− 11,25”: śniadanie w cenie hotelu to zapewniony posiłek. Pomniejszenie 25% pełnej diety = 11,25. Diety po pomniejszeniu: 78,75.",
                "„nocleg 380,00”: faktura hotelowa; limit 20 diet = 900 zł — mieści się. Gdyby faktura była na 1 100 zł, 200 zł wymagałoby zgody pracodawcy (§ 8 ust. 2).",
                "„dojazdy 2 × 9 = 18,00”: ryczałt na komunikację miejscową za każdą rozpoczętą dobę (2). Przysługuje, bo pracownik jechał pociągiem i po Gdańsku poruszał się tramwajem na własny koszt.",
                "„bilety 298,00”: przejazd wg biletów — środek transportu z polecenia wyjazdu (pociąg). Bez biletu — oświadczenie pracownika (§ 5 ust. 2).",
                "„razem 774,75 − 500 = 274,75”: pracownik dostaje 274,75 zł przelewem poza listą płac. Całość mieści się w limitach: bez PIT (art. 21 ust. 1 pkt 16 lit. a) i bez składek (§ 2 ust. 1 pkt 15).",
                "Kontrola: gdyby regulamin AGRO-MLEKO dawał dietę 70 zł, kalkulator pokazałby nadwyżkę (70 − 45) × 2 = 50 zł — i to trafia na listę płac listopada jako przychód.",
            ],
            "wynik": "diety 78,75 + nocleg 380,00 + dojazdy 18,00 + bilety 298,00 = 774,75 zł; do wypłaty po zaliczce 274,75 zł; nadwyżka 0 (regulamin = rozporządzenie).",
        },
        "jak_uruchomic": [
            "Warsztat → Delegacje i diety → karta „Podróż krajowa”: Wyjazd 2026-11-16 06:00, Powrót 2026-11-17 18:30, Śniadania 1, Noclegi z rachunku 380 / liczba 1, Bilety 298, Zaliczka 500 → „Policz”.",
            "Porównaj każdy wiersz z demonstracją: 2,00 diety; 90,00; −11,25; 78,75; 380,00; 18,00; 298,00; 774,75; −500,00; 274,75.",
            "Wpisz „Dieta wg regulaminu firmy” 70 → „Policz” → ostatni wiersz pokazuje nadwyżkę 50,00 zł (przychód).",
            "„Zapisz do projektu” → 04-place/delegacja_krajowa.md. Oczekiwany wynik: plik z pełnym rozliczeniem i podstawą prawną w każdym wierszu.",
        ],
        "cwiczenia": [
            {"rodzaj": "prowadzone",
             "tresc": "Technik utrzymania ruchu jedzie na szkolenie do Poznania własnym autem (1,6 l): wyjazd 23.11.2026 07:00, powrót 24.11.2026 16:00; organizator zapewnia obiad w oba dni; hotel z faktury 420 zł; trasa 2 × 310 km; zaliczka 400 zł. Policz na kartce jak w demonstracji, potem sprawdź w Warsztacie. Plik: cwiczenia/tydzien_07/delegacje_1.md. Czas: 20 minut.",
             "wynik": "33 h → 2 diety = 90,00; − 2 obiady × 22,50 = − 45,00 → diety 45,00; nocleg 420,00; ryczałt na dojazdy 0 (auto prywatne); kilometrówka 620 × 1,15 = 713,00; razem 1 178,00; − zaliczka 400 = do wypłaty 778,00 zł.",
             "wskazowki": [
                 "Ile godzin trwała podróż i ile z tego to pełna doba? Co z resztą (9 h — więcej czy mniej niż 8)?",
                 "Lekcja: tabela diety krajowej (rozpoczęta doba ponad 8 h) i tabela posiłków (obiad = 50% pełnej diety); § 9 ust. 2 — ryczałt na dojazdy przy własnym aucie.",
                 "Szkic: 07:00 → 07:00 następnego dnia = 1 doba, 07:00 → 16:00 = 9 h → pełna dieta; 2 × 45 − 2 × 22,50 = 45; km: 620 × 1,15 = 713,00; dojazdy: 0, bo pracownik nie ponosi kosztów komunikacji miejscowej…",
             ],
             "rozwiazanie": "1. Czas: 23.11 07:00 → 24.11 16:00 = 33 h = 1 pełna doba + 9 h (ponad 8 h) → 2 diety × 45 = 90,00.\n2. Obiady 2 × 50% × 45 = 45,00 → diety 45,00 (pomniejszasz od pełnej diety).\n3. Nocleg z faktury 420,00 (limit 900 ✔).\n4. Dojazdy komunikacją miejscową: 0,00 — pracownik jechał własnym autem (§ 9 ust. 2).\n5. Kilometrówka: 620 km × 1,15 zł (pow. 900 cm³) = 713,00 — na podstawie ewidencji przebiegu.\n6. Razem 45,00 + 420,00 + 713,00 = 1 178,00; − zaliczka 400,00 = 778,00 zł do wypłaty.\n7. Wszystko w limitach: bez PIT i bez składek. Warsztat: te same kwoty (Doby z ryczałtem na dojazdy = 0, Km = 620, Pojazd powyżej 900 cm³)."},
            {"rodzaj": "samodzielne",
             "tresc": "Kierownik sprzedaży leci na targi do Kolonii. Pociąg Kraków → lotnisko Warszawa 2.12.2026 03:30–07:00; start samolotu 08:10; lądowanie w Warszawie 4.12.2026 21:40; pociąg do Krakowa 22:00 → 5.12 01:30. Hotel 2 noce po 150 EUR (faktura), śniadania wliczone; taksówki lotnisko–hotel–lotnisko bez paragonów; po mieście metrem na własny koszt; zaliczka 200 EUR wypłacona 27.11 (kurs średni NBP z tego dnia: 4,2850). Zdecyduj: od kiedy liczysz czas za granicą, czy za część krajową należy się dieta, jak rozliczasz taksówki — i policz kwotę do wypłaty w EUR i w PLN. Plik: cwiczenia/tydzien_07/delegacje_2.md. Czas: 25 minut.",
             "wynik": "czas za granicą 2.12 08:10 → 4.12 21:40 = 61,5 h → 3 diety × 49 = 147,00 EUR; − 2 śniadania × 15% × 49 = − 14,70 → 132,30; hotel 300,00 (limit 170/dobę ✔); dojazd lotnisko ryczałt 1 dieta 49,00; komunikacja miejscowa 3 × 4,90 = 14,70; razem 496,00 EUR − 200 = 296,00 EUR × 4,2850 = 1 268,36 zł; część krajowa 3,5 + 3,5 = 7 h → dieta krajowa nie przysługuje.",
             "wskazowki": [
                 "Gdzie przebiega granica dla podróży lotniczej — na lotnisku, przy odprawie czy w chwili startu? I co z 7 godzinami pociągiem po Polsce?",
                 "Lekcja: tabela podróży zagranicznej (niepełna doba ponad 12 h, ryczałt na dojazd z/do lotniska = 1 dieta, komunikacja 10%/doba) i § 21 (część krajowa jak krajowa).",
                 "Szkic: 61,5 h = 2 doby + 13,5 h → 3 diety; śniadania zagraniczne −15% każda; taksówki bez paragonu = ryczałt 1 dieta (obie strony); 3 rozpoczęte doby × 10% × 49…",
             ],
             "rozwiazanie": "1. Czas za granicą (§ 12 pkt 2): od startu 2.12 08:10 do lądowania 4.12 21:40 = 61,5 h = 2 pełne doby + 13,5 h (ponad 12 h) → 3 diety × 49 EUR = 147,00.\n2. Śniadania wliczone: 2 × 15% × 49 = 14,70 → diety 132,30 EUR.\n3. Hotel: 2 × 150 = 300,00 EUR (limit 170 EUR/dobę ✔).\n4. Taksówki lotnisko–hotel–lotnisko bez dokumentów: ryczałt 1 dieta = 49,00 EUR (§ 17 ust. 1).\n5. Komunikacja miejscowa: 3 rozpoczęte doby × 10% × 49 = 14,70 EUR.\n6. Razem 496,00 EUR; − zaliczka 200,00 = 296,00 EUR; × 4,2850 (kurs z dnia wypłaty zaliczki, § 20 ust. 3) = 1 268,36 zł.\n7. Część krajowa (§ 21): 3,5 h + 3,5 h = 7 h < 8 h → dieta krajowa nie przysługuje; bilety PKP zwracasz z biletów.\nWarsztat → Podróż zagraniczna: Niemcy, 61,5 h, śniadania 2, noclegi z rachunku 300 / 2, dojazd 2, kurs 4,2850, zaliczka 200, część krajowa 7 h."},
        ],
        "typowe_bledy": [
            {"komunikat": "Rozliczenie: 2 dni kalendarzowe = 2 diety, choć podróż trwała 11 h (20:00 → 7:00).",
             "przyczyna": "Dieta zależy od godzin podróży, nie od liczby dni w kalendarzu.",
             "diagnoza": "Policz godziny od wyjazdu do powrotu: 11 h → od 8 do 12 h → 50%.",
             "poprawka": "Warsztat → Delegacje: wpisz godziny wyjazdu i powrotu; kalkulator pokazuje doby i procent."},
            {"komunikat": "Obiad pomniejszony o 11,25 zł, bo „za tę dobę była połowa diety”.",
             "przyczyna": "Pomniejszenie liczy się od pełnej diety (45 zł), niezależnie od tego, ile diety przysługuje za dobę.",
             "diagnoza": "Sprawdź § 7 ust. 4: „obiad — 50% diety”, bez „diety należnej za dobę”. Wynik nie może być ujemny.",
             "poprawka": "Obiad = 22,50 zł; jeśli dieta za dobę to 22,50 → po pomniejszeniu 0,00."},
            {"komunikat": "Ryczałt 9 zł na dojazdy doliczony pracownikowi, który jechał własnym autem.",
             "przyczyna": "Ryczałt na komunikację miejscową przysługuje tylko wtedy, gdy pracownik ponosi koszty dojazdów.",
             "diagnoza": "Czy pracownik płacił za tramwaj/autobus w miejscu delegacji? Nie — miał auto.",
             "poprawka": "Pole „Doby z ryczałtem na dojazdy” = 0."},
            {"komunikat": "Dieta regulaminowa 70 zł wypłacona w całości poza listą płac, bez PIT i ZUS.",
             "przyczyna": "Zwolnienie z PIT i wyłączenie ze składek sięgają tylko do 45 zł; nadwyżka to przychód ze stosunku pracy.",
             "diagnoza": "Porównaj dietę z regulaminu z dietą z rozporządzenia; różnica × liczba diet.",
             "poprawka": "Nadwyżkę dolicz do listy płac miesiąca (składki + PIT); kalkulator: pole „Dieta wg regulaminu firmy”."},
            {"komunikat": "Kierowca w transporcie międzynarodowym rozliczony dietami jak handlowiec.",
             "przyczyna": "Od 2.02.2022 kierowca w przewozie międzynarodowym nie jest w podróży służbowej (art. 21b).",
             "diagnoza": "Sprawdź rodzaj przewozu i datę; dla międzynarodowego szukaj art. 26f (60 EUR składki / 20 EUR PIT).",
             "poprawka": "Kierowcy krajowi — delegacja; międzynarodowi — wyłączenia z art. 26f w liście płac."},
        ],
        "podsumowanie": "Policzyć liczbę diet z godzin podróży, pomniejszyć je za posiłki od pełnej diety, rozliczyć nocleg (rachunek do limitu albo ryczałt), dojazdy, kilometrówkę i zaliczkę; dla podróży zagranicznej — liczyć czas od granicy, w walucie, po kursie z dnia zaliczki; wskazać nadwyżkę ponad limity, która idzie na listę płac.",
    },
}
