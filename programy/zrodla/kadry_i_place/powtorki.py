# -*- coding: utf-8 -*-
"""Powtórki — jedna rozbudowana na etap (STANDARD_KURSOW.md §8): przypomnienie pojęć, przykład, typowe błędy,
ćwiczenie prowadzone i samodzielne, pytania i test. Dołączane do ostatniego tygodnia etapu."""

POWTORKI = [
    {
        "id": "powtorka_etap_0", "tydzien": 0, "czas_min": 30, "etap": 0,
        "nazwa": "Powtórka etapu 0: warsztat kadrowca — źródła, narzędzia, wskaźniki",
        "cel": "bez zaglądania do notatek rozkładasz pytanie kadrowe na przepis → kwotę → dzielnik → rachunek, wiesz, które narzędzie w Warsztacie do czego służy, i liczysz minimalne brutto → netto → koszt.",
        "po_co": "etap 0 to fundament — w kolejnych 11 tygodniach każda lekcja zakłada, że umiesz znaleźć przepis, odczytać wskaźnik i sprawdzić wynik w Warsztacie.",
        "slowa": ["powtórka", "powtorka", "etap 0", "podsumowanie etapu"],
        "wymagania": ["Zaliczone testy 4 lekcji tygodnia 0 (Lekcje → ✔).", "Plik wskazniki_2026.md i FIRMA.md w katalogu projektu.", "Warsztat → Lista płac, Czas pracy, Przepisy."],
        "wyjasnienie":
            "## Pojęcia, które muszą zostać\n"
            "- Hierarchia źródeł: Konstytucja → ustawa (KP, ustawa systemowa, zasiłkowa, o PIT) → rozporządzenie (wydane na podstawie ustawy: składkowe, urlopowe, o dokumentacji) → obwieszczenie (ogłasza kwotę: 30-krotność, odpis ZFŚS) → układ/regulamin → umowa. Niższe źródło nie może być mniej korzystne dla pracownika (art. 9, 18 KP).\n"
            "- Stan prawny: OBOWIĄZUJE / PROJEKT / NIE WIEM — zapisujesz przy każdej notatce; kwota bez Dz.U. i daty sprawdzenia nie jest źródłem.\n"
            "- Obieg miesiąca: 5. ewidencja → 8. lista → 10. wypłata → 15. ZUS (osoby prawne) i PPK → 20. PIT i DEK-I-0 → 25. Wn-D; terminy w dzień wolny: ZUS/PIT → następny roboczy, wypłata → poprzedni roboczy.\n"
            "- Pełnomocnictwa: PEL (ZUS), UPL-1 (US) — podpisuje zarząd; dokumenty mają stany: przygotowany → zweryfikowany → wysłany (UPP/UPO).\n"
            "- Wskaźniki 2026: minimalne 4 806 (stawka 31,40), składki pracownika 9,76 / 1,5 / 2,45 (osobno zaokrąglane), zdrowotna 9% (ograniczenie do hipotetycznej zaliczki 2021), KUP 250/300, PIT 12% do 120 000 / 32%, kwota zmniejszająca 300, ulga dla młodych 85 528, 30-krotność 282 600, współczynnik ekwiwalentu 20,92, odpis ZFŚS 2 943,23, wypadkowa firmy 1,20% (mały płatnik 1,67%), PPK 2% / 1,5%.\n"
            "## Co umiesz zrobić w Warsztacie\n"
            "- Lista płac (Tryb ćwiczenia: najpierw swoje netto, potem Sprawdź), Czas pracy (wymiar, nocne), Przepisy (48 streszczeń), Firma ćwiczeniowa (12 osób, parametry, regulaminy), eZUS/Płatnik i e-Urząd (symulatory z weryfikacją i UPP/UPO).",
        "przyklad":
            "Pytanie z etapu: „Ile kosztuje firmę pracownik z minimalnym wynagrodzeniem i ile dostaje na rękę w listopadzie 2026, jeśli pracuje 40 h w nocy?”\n"
            "1. Nocne: art. 151⁸ KP → 20% × (4 806 / 160 h) = 6,01 zł × 40 h = 240,40.\n"
            "2. Brutto 4 806 + 240,40 = 5 046,40 (nocne są oskładkowane i opodatkowane).\n"
            "3. Składki: 492,53 + 75,70 + 123,64 = 691,87 → zdrowotna 9% × 4 354,53 = 391,91 → podstawa PIT 5 046,40 − 691,87 − 250 = 4 104,53 → 4 105 → 492,60 − 300 = 192,60 → 193 → netto 3 769,62.\n"
            "4. Koszt (wypadkowa 1,2%): 5 046,40 + 492,53 + 328,02 + 60,56 + 123,64 + 5,05 = 6 056,20 zł.",
        "demonstracja": {
            "tytul": "Jedno pytanie, cztery lekcje etapu 0 — prześledź, skąd bierze się każda liczba",
            "kroki": ["Krok 1 (lekcja „Źródła prawa”): reguła z ustawy (20% stawki z minimalnego), kwota z rozporządzenia (4 806), dzielnik z art. 130 (160 h w listopadzie) — stawka 30,04, dodatek 6,01 zł/h.",
                      "Krok 2 (lekcja „Narzędzia”): sprawdzasz w Warsztat → Czas pracy (nocne 40 h → 240,40) — kalkulator potwierdza, nie zastępuje rachunku.",
                      "Krok 3 (lekcja „Wskaźniki”): trzy składki osobno od 5 046,40; zdrowotna od różnicy; KUP i zaokrąglenia; zaliczka 193 — gdyby pracownik nie złożył PIT-2, zaliczka 493 i netto o 300 niższe.",
                      "Krok 4 (lekcja „Wskaźniki”, koszt): składki pracodawcy 9,76 + 6,5 + 1,2 + 2,45 + 0,1 = 20,01% × 5 046,40 = 1 009,80 → koszt 6 056,20; z PPK byłoby + 75,70.",
                      "Zapis odpowiedzi: wynik + źródła + data sprawdzenia; w dzienniku jedno zdanie: „nocne liczę z wymiaru miesiąca, nie ze 168”."],
            "wynik": "netto 3 769,62 zł; koszt pracodawcy 6 056,20 zł; wszystkie liczby z podstawą prawną."},
        "jak_uruchomic": ["Warsztat → Czas pracy: 2026, 11, nocne 40 → 240,40.", "Warsztat → Lista płac: Zasadnicze 4806, Nadgodziny/premie/nocne 240.40, PPK 0/0 → Tryb ćwiczenia: wpisz 3 769,62 → Sprawdź.", "Oczekiwany wynik: ✔ i kroki; koszt 6 056,20."],
        "cwiczenia": [
            {"rodzaj": "prowadzone",
             "tresc": "Powtórz ścieżkę z demonstracji dla Katarzyny Wójcik (4 806, PPK 2%/1,5%) z 24 h nocnymi w grudniu 2026 (wymiar 160 h): nocne, brutto, netto, koszt. Plik: cwiczenia/tydzien_00/powtorka_etap_0_1.md. Czas: 15 minut.",
             "wynik": "nocne 24 × 6,01 = 144,24; brutto 4 950,24; społeczne 483,14 + 74,25 + 121,28 = 678,67; zdrowotna 384,44; PPK pracodawcy 74,25; podstawa 4 950,24 + 74,25 − 678,67 − 250 = 4 095,82 → 4 096 → 491,52 − 300 → 192; PPK pracownika 99,00; netto 4 950,24 − 678,67 − 384,44 − 192 − 99 = 3 596,13; koszt = 4 950,24 + 990,54 + 74,25 = 6 015,03.",
             "wskazowki": ["Czy dodatek nocny w grudniu jest taki sam jak w listopadzie? (Wymiar obu miesięcy = 160 h.)",
                           "Demonstracja, kroki 1–4 — zmień tylko godziny nocne i dodaj PPK (lekcja „Wskaźniki”, ćwiczenie prowadzone).",
                           "Szkic: 24 × 6,01 = 144,24; 4 950,24 × 9,76% = 483,14; … ; PPK 1,5% = 74,25 do PIT, 2% = 99,00 z netto…"],
             "rozwiazanie": "Nocne: 4 806/160 = 30,04 × 20% = 6,01 × 24 h = 144,24\nBrutto: 4 806 + 144,24 = 4 950,24\nSkładki: 483,14 + 74,25 + 121,28 = 678,67; zdrowotna 9% × 4 271,57 = 384,44\nPPK pracodawcy 74,25 (przychód); podstawa PIT 4 950,24 + 74,25 − 678,67 − 250 = 4 095,82 → 4 096 × 12% = 491,52 − 300 = 191,52 → 192\nPPK pracownika 2% = 99,00\nNetto = 4 950,24 − 678,67 − 384,44 − 192 − 99 = 3 596,13 zł\nKoszt = 4 950,24 + (483,14 + 321,77 + 59,40 + 121,28 + 4,95 = 990,54) + 74,25 = 6 015,03 zł"},
            {"rodzaj": "samodzielne",
             "tresc": "Zarząd pyta: „Czy od stycznia 2027 możemy zostawić pensje 4 806 zł i dopłacać różnicę premią?”. Zdecyduj na podstawie przepisów o minimalnym wynagrodzeniu (które składniki wliczasz do minimalnego, a których nie), policz, ile osób w FIRMA.md wymaga aneksu, i napisz 3-zdaniową odpowiedź ze źródłami. Plik: cwiczenia/tydzien_00/powtorka_etap_0_2.md. Czas: 15 minut.",
             "wynik": "do minimalnego wlicza się składniki wynagrodzenia z wyjątkiem nadgodzin, nocnego, nagrody jubileuszowej, odprawy emerytalnej i — od 2024 — dodatku za szczególne warunki (art. 6 ust. 5 ustawy o minimalnym wynagrodzeniu); premia regulaminowa (uznaniowa „do 10%”) nie gwarantuje minimum — w miesiącu bez premii pensja 4 806 < 4 950 → wyrównanie; aneks potrzebny dla Wójcik (4 806) i Krawczyka (4 900) oraz proporcjonalnie Nowaka (2 500 → 2 475 min. na 1/2 etatu — OK, 2 500 ≥ 2 475).",
             "wskazowki": ["Jaka jest różnica między składnikiem stałym a premią „do 10%” z punktu widzenia gwarancji minimalnego?",
                           "Warsztat → Przepisy → „Minimalne wynagrodzenie 2026” (art. 6 ustawy z 10.10.2002) — lista wyłączeń; Firma ćwiczeniowa → Osoby.",
                           "Szkic: 2027 minimalne 4 950; osoby < 4 950 na pełny etat: Wójcik 4 806, Krawczyk 4 900 → aneksy; Nowak 1/2 etatu: min. 2 475 ≤ 2 500 ✔; premia uznaniowa nie wlicza się „na zapas”…"],
             "rozwiazanie": "Art. 6 ust. 4–5 ustawy o minimalnym wynagrodzeniu: do minimalnego wlicza się składniki zaliczane do wynagrodzeń osobowych (GUS), ale NIE: nagrody jubileuszowej, odprawy emerytalnej/rentowej, wynagrodzenia za nadgodziny, dodatku za pracę w nocy, dodatku za staż pracy (od 2020) i dodatku za szczególne warunki pracy (od 2024). Premia regulaminowa „do 10% za wynik” formalnie się wlicza, ale tylko w miesiącu, w którym jest wypłacona i w wysokości faktycznej — w miesiącu bez premii pracownik musi dostać wyrównanie do 4 950 (art. 7). Rozwiązanie: aneksy podnoszące zasadnicze do 4 950 dla Katarzyny Wójcik (4 806) i Jakuba Krawczyka (4 900); Piotr Nowak (1/2 etatu, 2 500): minimum proporcjonalne 2 475 — bez aneksu; pozostali powyżej. Odpowiedź: „Od 1.01.2027 minimalne wynagrodzenie wynosi 4 950 zł (rozporządzenie RM na 2027). Premia regulaminowa nie gwarantuje minimum, bo w miesiącach bez premii musielibyśmy wypłacać wyrównanie, a dodatek nocny i nadgodziny w ogóle nie wchodzą do minimum (art. 6 ust. 5 ustawy z 10.10.2002). Proponuję aneksy do 4 950 zł dla dwóch osób od 1.01.2027 — koszt ok. 2 × 150 zł × 1,2 miesięcznie.”"},
        ],
        "typowe_bledy": [
            {"komunikat": "Dodatek nocny policzony ze 168 h w listopadzie.", "przyczyna": "Dzielnik „na stałe”.", "diagnoza": "Warsztat → Czas pracy → wymiar 11/2026 = 160.", "poprawka": "Stawka = minimalne / wymiar danego miesiąca."},
            {"komunikat": "Netto różni się o kilka złotych od Warsztatu.", "przyczyna": "Brak zaokrągleń podstawy i zaliczki do złotego albo KUP odjęty przed składkami.", "diagnoza": "Tryb ćwiczenia → „Sprawdź” wskaże krok.", "poprawka": "Kolejność: składki osobno → zdrowotna → podstawa (zaokr.) → zaliczka (zaokr.)."},
            {"komunikat": "Kwota w notatce bez Dz.U. i daty.", "przyczyna": "Źródło = portal.", "diagnoza": "Czy przy liczbie jest akt i data sprawdzenia?", "poprawka": "Warsztat → Przepisy → przepisz akt; dopisz datę."},
        ],
        "pulapki": ["Powtórka to nie ponowne czytanie lekcji — to policzenie przykładu bez patrzenia i porównanie z Warsztatem.", "Jeśli którakolwiek z 4 lekcji ma test poniżej 2/3 — wróć do niej przed zadaniem tygodnia."],
        "zadania": ["Zrób test każdej z 4 lekcji etapu jeszcze raz — bez notatek; zapisz, które pytanie sprawiło trudność.",
                    "Policz z pamięci wskaźniki: składki, KUP, próg, kwota zmniejszająca, 30-krotność, współczynnik — potem sprawdź w Firma ćwiczeniowa → Parametry.",
                    "Zapisz w dzienniku 3 rzeczy, które z etapu 0 wykorzystasz w pracy już pierwszego dnia."],
        "pytania": [["Jak rozkładasz pytanie kadrowe na elementy?", "Reguła z ustawy → kwota z rozporządzenia/obwieszczenia → dzielnik z Kodeksu → rachunek; wynik ze źródłem i datą."],
                    ["Co się dzieje z terminem wypłaty, a co z terminem ZUS, gdy wypadają w niedzielę?", "Wypłata — poprzedni dzień roboczy (art. 85 §3); ZUS/PIT — następny dzień roboczy."],
                    ["Dlaczego składki liczysz osobno, a nie 13,71% razem?", "Zaokrąglenie każdej do grosza — jedna kwota daje różnicę o grosz, którą Płatnik odrzuci."]],
        "podsumowanie": "Policzyć listę od nocnych do kosztu pracodawcy, wskazać źródło każdej liczby, obsłużyć przesunięcia terminów i ocenić, czy pensja spełnia minimum.",
        "test": [
            {"p": "Który akt ustala kwotę minimalnego wynagrodzenia na dany rok?", "o": ["Kodeks pracy", "Rozporządzenie Rady Ministrów (lub obwieszczenie Prezesa RM)", "Regulamin wynagradzania", "Ustawa budżetowa"], "odp": 1, "w": "Ustawa daje regułę, rozporządzenie RM — kwotę (4 806 na 2026, Dz.U. 2025 poz. 1242)."},
            {"p": "Termin ZUS 15.11.2026 wypada w niedzielę. Do kiedy płaci spółka z o.o.?", "o": ["13.11 (piątek)", "16.11 (poniedziałek)", "15.11 — przelew działa w niedzielę", "20.11"], "odp": 1, "w": "Termin w dzień wolny przesuwa się na następny dzień roboczy."},
            {"p": "Pracownik na pełny etat ma 4 806 zł zasadniczego i co miesiąc premię 300 zł. Czy od 1.01.2027 trzeba podpisać aneks?", "o": ["Nie — z premią przekracza 4 950", "Tak — premia nie gwarantuje minimum w każdym miesiącu", "Nie — minimalne dotyczy tylko nowych umów", "Tak — ale dopiero od marca"], "odp": 1, "w": "W miesiącu bez premii należy się wyrównanie; bezpieczniej podnieść zasadnicze."},
        ],
    },
    {
        "id": "powtorka_etap_1", "tydzien": 3, "czas_min": 40, "etap": 1,
        "nazwa": "Powtórka etapu 1: od ogłoszenia do urlopu — prawo pracy w praktyce",
        "cel": "prowadzisz pracownika od ogłoszenia przez umowę, onboarding, czas pracy i ewidencję do urlopu i nieobecności — bez zaglądania do lekcji liczysz wymiar, nadgodziny, limit 33/3 i urlop.",
        "po_co": "etap 1 to codzienność kadr; wszystko, co w etapie 2 trafi na listę płac (nadgodziny, nocne, nieobecności, urlop), tu powstaje — błąd w ewidencji czy wymiarze przenosi się na pieniądze.",
        "slowa": ["powtórka", "etap 1", "prawo pracy powtórka"],
        "wymagania": ["Zaliczone testy lekcji tygodni 1–3.", "Pliki z zadań: umowa, onboarding, karta ewidencji, wymiar 2027, urlopy 8 osób.", "Warsztat → Czas pracy, Urlopy i ekwiwalent."],
        "wyjasnienie":
            "## Pojęcia etapu\n"
            "- Rekrutacja: widełki obowiązkowe (art. 22¹ᵇ), katalog danych kandydata (art. 22¹), zakaz pytania o dotychczasowe zarobki, RODO: retencja do końca rekrutacji (+12 mies. za zgodą).\n"
            "- Umowa: próbna 1/2/3 mies. zależnie od planu; limit 33 mies. / 3 umowy (próbna nie liczy się; aneks = nowa umowa); treść art. 29 §1; informacja 29 §3 w 7 dni.\n"
            "- Onboarding: badania PRZED (A), umowa przed pracą (B), BHP dzień 1, ZUA 7 dni, PPK po 3 mies. (do 10. dnia nast. mies.), akta A–E, 10 lat; D i E — rok.\n"
            "- Czas pracy: wymiar = pełne tygodnie × 40 + dni wystające × 8 − święta × 8; 11/35 h odpoczynku; równoważny do 12 h; grafik miesiąc naprzód; nadgodziny: normalne + 50%/100%, czas wolny 1:1 (wniosek) / 1:1,5; nocne 20% stawki z minimalnego / wymiar.\n"
            "- Ewidencja §6: od–do, nocne, nadgodziny z poleceniem, kody; urlop w godzinach z planu; brak ewidencji = przegrany spór.\n"
            "- Urlop: 20/26 (staż: nauka + zatrudnienie + od 2026 zlecenia/działalność), proporcja (w górę), pierwsza praca 1/12 (bez zaokrąglania), 4 dni na żądanie w puli, zaległy do 30.09; rodzicielskie: 20 + 41 (9 ojca), 81,5% przy wniosku w 21 dni; ochrona ciąży (przedłużenie do porodu, zakaz nocy); krótkie nieobecności: 100/50/0, dzielnik — wymiar godzin (choroba — 30).",
        "przyklad":
            "Kazus etapu: operator (równoważny 12 h) zatrudniony 1.09.2026, staż 12 lat, w grudniu 2026: 2 zmiany po 14 h (po 2 h nadgodzin dobowych w nocy), 48 h nocnych, 1 dzień urlopu (12 h), 1 dzień siły wyższej (12 h).\n"
            "1. Wymiar grudnia 160 h; urlop 2026: 26 × 4/12 = 8,67 → 9 dni = 72 h (zostaje 60 h po 12 h urlopu).\n"
            "2. Nadgodziny: 4 h × stawka (5 400/160 = 33,75) normalne 135 + dodatek 100% (noc) 135 = 270; czas wolny bez wniosku 6 h w okresie rozliczeniowym zamiast dodatku.\n"
            "3. Nocne 48 × 6,01 = 288,48 (także za nadgodziny nocne).\n"
            "4. Siła wyższa 12 h: potrącenie 50% × 12 × 33,75 = 202,50 (tryb „dni” wybrany przy pierwszym wniosku — 1 z 2 dni).\n"
            "5. Ewidencja: 2 wiersze 06:00–20:00 z poleceniem nadgodzin; UW 12 h; SW 12 h; suma = 160 h.",
        "demonstracja": {
            "tytul": "Jeden grudzień operatora — sześć lekcji etapu w jednym rozliczeniu",
            "kroki": ["Wymiar (lekcja „Czas pracy”): 184 − 24 = 160 h; w równoważnym 13 zmian × 12 + 4 h.",
                      "Urlop (lekcja „Urlop”): staż 12 lat → 26; u Ciebie od 1.09 → 4/12 × 26 = 8,67 → 9 dni (w górę); urlop udzielany w godzinach z planu — 12 h za dzień.",
                      "Nadgodziny (lekcja „Nadgodziny”): ponad 12 h z grafiku → dobowe; w nocy → 100%; stawka z wymiaru grudnia; alternatywa: czas wolny 1,5 × 4 = 6 h do końca okresu rozliczeniowego (kwartał).",
                      "Nocne: 48 h × 6,01 (grudzień 160 h) = 288,48 — niezależnie od dodatku za nadgodziny.",
                      "Siła wyższa (lekcja „Inne nieobecności”): 50% wynagrodzenia, dzielnik — wymiar godzin, dzień = 12 h z grafiku; pierwszy wniosek ustala tryb na rok.",
                      "Ewidencja (lekcja „Ewidencja”): każda godzina ma wiersz; suma pracy + urlop + nieobecności = wymiar; polecenia nadgodzin dołączone."],
            "wynik": "do listy płac trafia: zasadnicze 5 400 − 202,50 (SW) + 270 (nadgodziny) + 288,48 (nocne); urlop: zostaje 60 h; ewidencja zbilansowana do 160 h."},
        "jak_uruchomic": ["Warsztat → Czas pracy: wymiar 12/2026, nocne 48; Nadgodziny: 5400 / 160 / h100 = 4.", "Warsztat → Urlopy: staż 12, etat 1, miesięcy 4 → 9 dni.", "Warsztat → Urlopy → trzecia karta: pensja 5400, godz. innych nieobecności 12 → 405 (pełne); 50% = 202,50 licz ręcznie.", "Oczekiwany wynik: liczby z demonstracji."],
        "cwiczenia": [
            {"rodzaj": "prowadzone",
             "tresc": "Zrób to samo dla pracownicy biura (podstawowy system, 8 h), zatrudnionej 15.03.2026, staż 6 lat (szkoła wyższa 8 lat → 26 dni!), 5 200 zł, listopad 2026: 6 h nadgodzin dobowych w dni robocze, 1 dzień urlopu, 8 h art. 188, 16 h urlopu opiekuńczego. Policz urlop na 2026, nadgodziny, potrącenia i zbilansuj ewidencję. Plik: cwiczenia/tydzien_03/powtorka_etap_1_1.md. Czas: 20 minut.",
             "wynik": "staż urlopowy 8 (studia) + 6 = 14 lat → 26 dni; u Ciebie od 15.03 → marzec liczy się cały (jeśli poprzedni pracodawca rozliczył do lutego) → 10/12 × 26 = 21,67 → 22 dni = 176 h; nadgodziny: stawka 5 200/160 = 32,50; normalne 6 × 32,50 = 195 + 50% = 97,50 → 292,50; art. 188 — 100%, bez potrącenia; opiekuńczy 16 h: 16 × 32,50 = 520 potrącenia; ewidencja: 20 dni × 8 = 160 = praca 128 + UW 8 + art. 188 8 + UO 16 (+ nadgodziny 6 osobno).",
             "wskazowki": ["Studia wyższe dają 8 lat stażu urlopowego — czy sumujesz je z pracą, czy wybierasz korzystniejsze? (Nie sumujesz okresów nauki — bierzesz najwyższy, ale nauka + praca — tak, jeśli praca była po nauce.)",
                           "Lekcje „Urlop” (art. 155 §1 — okresy nauki nie sumują się między sobą, ale sumują z pracą po nauce) i „Inne nieobecności”.",
                           "Szkic: 26 × 10/12 = 21,67 → 22; nadgodziny 6 × 32,50 × 1,5 = 292,50; UO 16 × 32,50 = 520; art. 188 → 0…"],
             "rozwiazanie": "Staż urlopowy: szkoła wyższa 8 lat (art. 155 §1 pkt 6) + 6 lat pracy po studiach = 14 lat ≥ 10 → 26 dni. Proporcja u nowego pracodawcy: zatrudnienie 15.03 → miesiące III–XII = 10 (niepełny miesiąc liczy się jako pełny, gdy poprzedni pracodawca rozliczył do lutego — art. 155²ᵃ §2) → 26 × 10/12 = 21,67 → 22 dni (176 h), w tym 4 dni na żądanie.\nNadgodziny: stawka 5 200/160 = 32,50; normalne 6 × 32,50 = 195,00 + dodatek 50% 97,50 = 292,50 (albo 6 h wolnego na wniosek / 9 h bez wniosku).\nArt. 188 (8 h): 100% — bez potrącenia; limit 2 dni/16 h w roku (wybór trybu przy pierwszym wniosku).\nUrlop opiekuńczy 16 h: bezpłatny → 16 × 32,50 = 520,00 potrącenia; RSA 151.\nWynagrodzenie: 5 200 − 520 + 292,50 = 4 972,50 (składki i PIT od tej kwoty).\nEwidencja listopad (160 h): praca 128 h (16 dni) + UW 8 + art. 188 8 + UO 16 = 160 ✔; nadgodziny 6 h w osobnej kolumnie z numerami poleceń; 11.11 — święto (WŚ nie dotyczy, bo środa — obniża wymiar)."},
            {"rodzaj": "samodzielne",
             "tresc": "Kierownik produkcji chce „uprościć”: (1) nowym dać próbną 3 miesiące, a potem określoną na 4 miesiące „na sprawdzenie”, (2) grafik publikować w czwartek na następny tydzień, (3) nocki rozliczać ryczałtem 150 zł/mies. dla wszystkich operatorów, (4) urlop w równoważnym liczyć zawsze po 8 h. Zdecyduj, co jest legalne, podaj podstawę i poprawną wersję każdej propozycji. Plik: cwiczenia/tydzien_03/powtorka_etap_1_2.md. Czas: 15 minut.",
             "wynik": "(1) nie — przy planowanej określonej < 6 mies. próbna max 1 mies. (art. 25 §2²); poprawnie: próbna 1 mies. + określona 4 mies. albo próbna 3 mies. + określona ≥ 12 mies.; (2) nie — rozkład na min. 1 miesiąc, przekazany min. 1 tydzień przed (art. 129 §3); (3) ryczałt dopuszczalny tylko dla stale pracujących w nocy i nie niższy niż ustawowy (art. 151⁸ §3): operator 3-zmianowy ma ok. 56–64 h nocnych → 336–385 zł → 150 to niedopłata; (4) nie — urlop w godzinach z planu (art. 154² §1): dzień 12-godzinny = 12 h z puli.",
             "wskazowki": ["Dla każdej propozycji zapytaj: który przepis to reguluje i czy jest „nie mniej korzystny” niż Kodeks?",
                           "Lekcje „Umowa o pracę” (art. 25 §2²), „Czas pracy” (art. 129 §3), „Nadgodziny” (art. 151⁸ §3), „Ewidencja” (art. 154²).",
                           "Szkic: (1) 1 mies.; (2) miesiąc + tydzień; (3) ryczałt ≥ faktyczne; (4) 12 h…"],
             "rozwiazanie": "(1) Art. 25 §2² KP: jeśli po próbnej planujesz umowę określoną krótszą niż 6 miesięcy — próbna max 1 miesiąc; 6–12 mies. — max 2 miesiące; 3 miesiące — tylko przy planie ≥ 12 miesięcy lub nieokreślonej. Poprawnie: próbna 1 mies. + określona 4 mies. (w próbnej wpisujesz planowany okres kolejnej umowy — art. 29 §1¹); albo próbna 3 mies. + określona ≥ 12 mies.\n(2) Art. 129 §3: rozkład czasu pracy sporządzasz na okres co najmniej 1 miesiąca i przekazujesz co najmniej 1 tydzień przed rozpoczęciem pracy w okresie, na który jest sporządzony. „Czwartek na następny tydzień” narusza oba warunki → wykroczenie (art. 281 §1 pkt 5).\n(3) Art. 151⁸ §3: ryczałt za pracę w nocy dopuszczalny wobec pracowników wykonujących pracę w nocy STALE poza zakładem; w zakładzie — dodatek za faktyczne godziny; ryczałt nie może być niższy od należnego dodatku: operator 3-zmianowy ma ok. 56–64 h nocnych miesięcznie × 6,01 = 336–385 zł → ryczałt 150 zł to niedopłata (nakaz płacowy PIP + wyrównanie 3 lata wstecz).\n(4) Art. 154² §1–2: urlopu udziela się w dni pracy w wymiarze godzinowym odpowiadającym dobowemu wymiarowi z rozkładu — dzień 12-godzinny pomniejsza pulę o 12 h; liczenie „po 8” skraca urlop pracownikom równoważnym (208 h = 17 dni 12-godzinnych, nie 26 dni)."},
        ],
        "typowe_bledy": [
            {"komunikat": "Urlop proporcjonalny 21,67 zaokrąglony do 21.", "przyczyna": "Niepełny dzień zaokrągla się w górę (art. 155³).", "diagnoza": "Warsztat → Urlopy.", "poprawka": "22 dni."},
            {"komunikat": "Nadgodzina nocna z dodatkiem 50%.", "przyczyna": "Art. 151¹ §1 pkt 1 lit. a — w nocy 100%.", "diagnoza": "Czy godzina przypadła 22–6?", "poprawka": "100% + dodatek nocny."},
            {"komunikat": "Aneks wydłużający umowę określoną „nie liczy się do limitu”.", "przyczyna": "Art. 25¹ §2 — aneks to nowa umowa.", "diagnoza": "Policz miesiące i umowy po aneksie.", "poprawka": "Nowa umowa w limicie albo nieokreślona."},
        ],
        "pulapki": ["Powtórkę rób na własnych plikach z zadań — porównaj, czy dziś policzyłbyś tak samo.", "Jedna lekcja etapu z testem < 2/3 → wróć do niej przed quizem tygodnia 3."],
        "zadania": ["Powtórz testy 10 lekcji etapu 1 bez notatek; wynotuj tematy do powtórki.", "Zbilansuj ponownie kartę ewidencji z zadania tygodnia 3 — czy suma = wymiar?", "Przelicz urlopy 8 osób z zadania tygodnia 3 w Warsztacie i znajdź różnice."],
        "pytania": [["Od czego zależy maksymalna długość umowy próbnej?", "Od planowanej długości kolejnej umowy określonej: < 6 mies. → 1 mies.; 6–12 → 2; inaczej 3."],
                    ["Jaki dzielnik stosujesz do pensji przy chorobie, a jaki przy urlopie bezpłatnym?", "Choroba — 30; inne nieobecności — wymiar godzin miesiąca."],
                    ["Ile tygodni rodzicielskiego może wziąć matka, jeśli ojciec jest ubezpieczony?", "32 (41 − 9 nieprzenoszalnych tygodni ojca)."]],
        "podsumowanie": "Rozliczyć miesiąc pracownika od grafiku do nieobecności, policzyć urlop z proporcją i stażem, ocenić propozycje „uproszczeń” pod kątem Kodeksu.",
        "test": [
            {"p": "Pracownik w systemie równoważnym bierze urlop w dniu, w którym miał pracować 12 h. O ile zmniejsza się jego pula?", "o": ["8 h", "12 h", "1 dzień = 8 h, reszta przepada", "Zależy od regulaminu"], "odp": 1, "w": "Art. 154² §1 — godziny z rozkładu."},
            {"p": "Umowa określona 24 mies. + aneks o 12 mies. Co się dzieje?", "o": ["Nic — aneks nie liczy się do limitu", "Aneks = nowa umowa; po 33. miesiącu umowa staje się bezterminowa", "Umowa wygasa", "Trzeba zapłacić odprawę"], "odp": 1, "w": "Art. 25¹ §2–3."},
            {"p": "Pierwszy wniosek o siłę wyższą w roku złożono „na 4 godziny”. Drugi wniosek pracownik chce „na dzień”.", "o": ["Można — każdy wniosek osobno", "Nie — pierwszy wniosek ustala tryb (godziny) na cały rok", "Można, jeśli zgodzi się pracodawca", "Nie — siła wyższa przysługuje raz w roku"], "odp": 1, "w": "Art. 148¹ §2."},
        ],
    },
    {
        "id": "powtorka_etap_2", "tydzien": 7, "czas_min": 45, "etap": 2,
        "nazwa": "Powtórka etapu 2: płace od brutto do netto — lista, PIT, zasiłki, umowy cywilne, PPK",
        "cel": "liczysz pełną listę płac z nadgodzinami, chorobą, zasiłkiem, potrąceniem, benefitem i PPK, ustalasz podstawę zasiłku i rozliczasz zleceniobiorcę — i wiesz, który wynik sprawdzić w którym narzędziu.",
        "po_co": "etap 2 to serce kursu: każda liczba z lekcji 4–7 wraca w ZUS (etap 3) i w rozliczeniu końcowym (etap 4); kto tu jest pewny, tam tylko wysyła dokumenty.",
        "slowa": ["powtórka", "etap 2", "płace powtórka"],
        "wymagania": ["Zaliczone testy lekcji tygodni 4–7.", "Lista płac 2026-11 zapisana z Warsztatu (04-place/).", "Warsztat → Lista płac, Zasiłki, Potrącenia, Urlopy."],
        "wyjasnienie":
            "## Kolejność, która nigdy się nie zmienia\n"
            "- przychód oskładkowany (zasadnicze + zmienne + natura) → 3 składki osobno (limit 30-krotności dla E/R) → zdrowotna 9% od (przychód − składki + chorobowe), ograniczona hipotetyczną zaliczką 2021 → podstawa PIT = przychód ze stosunku pracy (+ PPK pracodawcy, + chorobowe, + benefity tylko-PIT) − składki − KUP (zaokr.) + zasiłki → zaliczka 12/32% − kwota zmniejszająca (zaokr.) → PPK pracownika → potrącenia (granice, kwoty wolne) → netto; bilans.\n"
            "- Chorobowe: bez społecznych, ze zdrowotną i PIT; zasiłek: tylko PIT bez KUP; benefit współfinansowany: bez ZUS, z PIT; ZFŚS z kryterium: bez ZUS, PIT do 1 000; odprawa: bez ZUS, z PIT; zwrot składek: przychód.\n"
            "- Dzielniki: choroba /30; inne nieobecności /wymiar; urlopowe ze zmiennych / godziny przepracowane; ekwiwalent /20,92 (× etat) /8.\n"
            "- Zasiłki: pula 33/14 (rok), okres 182/270 (przerwa > 60 dni), podstawa z 12 mies. (wyłącz < 50%, uzupełnij, −13,71%, minimum 4 147,10, nowa po przerwie ≥ 1 mies.), stawka dzienna × % (zaokr.) × dni; kody RSA 331/313/312/314/327/319/325/321.\n"
            "- Zlecenie: jedyny tytuł → pełne składki (chorobowa dobrowolna); etat ≥ min. gdzie indziej → tylko zdrowotna (ZZA); student < 26 → nic; stawka ≥ 31,40; KUP 20%/50%; PIT-2 możliwe; dzieło → RUD, ryzyko przekwalifikowania. PPK: po 3 mies., 2%/1,5% (0,5% przy ≤ 1,2 × min.), autozapis 1.04.2027.\n"
            "- Koszt: brutto × 1,2001 (wypadkowa 1,2%) + PPK 1,5% + ZFŚS/12; zwolnienia z FP/FGŚP (55+/60+, 36 mies. po rodzicielskim, podstawa < min. w przeliczeniu na miesiąc).",
        "przyklad":
            "Lista listopad 2026, Marek Zieliński (5 400, PPK, PIT-2, KUP 250): choroba 16–30.11 (9 dni chorobowego 1 201,14 + 6 dni zasiłku 800,76 ze stawki 133,46), nadgodziny z 1–15.11: 573,75, karta sportowa 1 zł (149 do PIT), zajęcie komornicze 1 200/mies.\n"
            "pensja 5 400 − 5 400/30 × 15 = 2 700; oskładkowane 2 700 + 573,75 = 3 273,75; składki 319,52 + 49,11 + 80,21 = 448,84; zdrowotna 9% × (3 273,75 − 448,84 + 1 201,14) = 362,34; PPK pracod. 49,11; podstawa PIT = 3 273,75 + 1 201,14 + 49,11 + 149 − 448,84 − 250 + 800,76 (zasiłek) = 4 774,92 → 4 775 → 573,00 − 300 = 273; PPK prac. 65,48; netto przed potrąceniem = (3 273,75 + 1 201,14 + 800,76) − 448,84 − 362,34 − 273 − 65,48 = 4 125,99; kwota wolna 3 501,73 → potrącenie 624,26; do wypłaty 3 501,73.",
        "demonstracja": {
            "tytul": "Jedna lista, osiem lekcji — prześledź każdą pozycję",
            "kroki": ["Pensja za część miesiąca (lekcja „Wynagrodzenie urlopowe”): choroba — dzielnik 30, 15 dni kalendarzowych → 2 700.",
                      "Chorobowe i zasiłek (lekcje „Chorobowe”, „Podstawa”): stawka 166,83 × 80% = 133,46 (zaokr.) × 9 i × 6; chorobowe wchodzi do zdrowotnej i PIT, zasiłek tylko do PIT.",
                      "Nadgodziny (etap 1) są oskładkowane → przychód oskładkowany 3 273,75; składki osobno; FP/FGŚP należne (pensja umowna 5 400 ≥ min.).",
                      "Benefit (lekcja „Świadczenia”): karta za 1 zł — bez ZUS, 149 do PIT; PPK pracodawcy 1,5% od 3 273,75 = 49,11 — do PIT.",
                      "Zaliczka (lekcja „Zaliczka PIT”): jedna podstawa łączna (praca + chorobowe + benefit + PPK − składki − KUP) + zasiłek bez KUP → 12% − 300.",
                      "Potrącenie (lekcja „Potrącenia”): netto 4 125,99; granica 1/2 = 2 063; kwota wolna z PPK 3 501,73 → potrącasz 624,26, nie 1 200.",
                      "ZUS (etap 3, zapowiedź): RCA od 3 273,75 (zdrowotna od 4 026,05); RSA 331 (9 dni, 1 201,14) i 313 (6 dni, 800,76 — do odliczenia w DRA)."],
            "wynik": "do wypłaty 3 501,73 zł; komornik 624,26; zaliczka 273; zasiłek 800,76 do odliczenia w DRA."},
        "jak_uruchomic": ["Warsztat → Lista płac: Osoba Zieliński, Zasadnicze 2700, Nadgodziny 573.75, Wynagrodzenie chorobowe 1201.14, Zasiłek 800.76, Pensja wg umowy 5400 → Policz (bez karty: netto 4 143,99; kartę 149 dolicz ręcznie → zaliczka +18 → 4 125,99).", "Warsztat → Potrącenia: netto 4125.99, inne, zajęcie 1200, PPK 2 → 624,26.", "Oczekiwany wynik: zgodny z przykładem co do grosza."],
        "cwiczenia": [
            {"rodzaj": "prowadzone",
             "tresc": "Policz listę za grudzień 2026 dla Ewy Sobczak (5 200, PPK, KUP 250, PIT-2, kod 01 10 0 2): opieka nad dzieckiem 16–20.11 była w listopadzie — w grudniu pełny miesiąc; premia 400; auto służbowe prywatnie (ryczałt 400 — natura); urlop opiekuńczy 8 h (wymiar 160). Potem oblicz zaliczkę i netto; wskaż pozycje do RCA/RSA. Plik: cwiczenia/tydzien_07/powtorka_etap_2_1.md. Czas: 20 minut.",
             "wynik": "pensja 5 200 − 5 200/160 × 8 = 4 940; oskładkowane 4 940 + 400 + 400 (auto) = 5 740; składki 560,22 + 86,10 + 140,63 = 786,95; zdrowotna 9% × 4 953,05 = 445,77; PPK pracod. 86,10; podstawa 5 740 + 86,10 − 786,95 − 250 = 4 789,15 → 4 789 × 12% = 574,68 − 300 → 275; PPK prac. 114,80; netto = (4 940 + 400) − 786,95 − 445,77 − 275 − 114,80 = 3 717,48 (auto nie jest wypłacane); RCA: podstawa 5 740; RSA 151 za 8 h opiekuńczego (dzień).",
             "wskazowki": ["Które z pozycji są „wypłacane”, a które tylko „doliczane do podstaw”? (Auto — doliczane.)",
                           "Lekcje „Świadczenia pozapłacowe” (natura w ZUS i PIT) i „Inne nieobecności” (dzielnik wymiar).",
                           "Szkic: 5 200/160 × 8 = 260 → 4 940; oskładkowane 5 740; składki 13,71% osobno; netto od gotówki 5 340…"],
             "rozwiazanie": "Pensja: 5 200 − 5 200/160 × 8 h (urlop opiekuńczy — bezpłatny, dzielnik wymiar 160) = 4 940,00.\nPrzychód oskładkowany: 4 940 + premia 400 + auto 400 (natura — ZUS i PIT) = 5 740,00.\nSkładki: emerytalna 560,22; rentowa 86,10; chorobowa 140,63 → 786,95. Zdrowotna 9% × (5 740 − 786,95) = 445,77.\nPPK: pracodawcy 1,5% × 5 740 = 86,10 (przychód); pracownika 2% = 114,80.\nPodstawa PIT: 5 740 + 86,10 − 786,95 − 250 = 4 789,15 → 4 789; 12% = 574,68 − 300 = 274,68 → 275.\nNetto = wypłaty pieniężne (4 940 + 400 = 5 340) − 786,95 − 445,77 − 275 − 114,80 = 3 717,48 zł (auto 400 nie jest wypłacane — pracownica „płaci” od niego składki i podatek).\nKoszt: 5 740 + 20,01% × 5 740 (1 148,57) + 86,10 = 6 974,67 (FP należne: pensja umowna 5 200 ≥ min.).\nZUS 12/2026 (wypłata 10.01.2027 → komplet 01 2027!): RCA 01 10 0 2 podstawa 5 740; RSA 151 (urlop opiekuńczy, dzień w grudniu) — bez kwoty."},
            {"rodzaj": "samodzielne",
             "tresc": "Dyrektor Tomasz Lis (14 000, PPK) w grudniu 2026: dochód narastająco po listopadzie 132 451 (próg przekroczony w październiku), premia roczna 30 000 oskładkowana, 5 dni choroby (podstawa zasiłku 12 080,60 → stawka?), zajęcie alimentacyjne 3 000. Zdecyduj i policz: składki E/R (30-krotność: podstawa narastająco 154 000 + grudzień?), zaliczkę 32%, zasiłek czy chorobowe (wykorzystał już 33 dni), potrącenie, netto. Plik: cwiczenia/tydzien_07/powtorka_etap_2_2.md. Czas: 25 minut.",
             "wynik": "30-krotność: 154 000 + (14 000 − 2 333,33 + 30 000) = 195 666,67 < 282 600 → bez ograniczenia; pensja 14 000 − 14 000/30 × 5 = 11 666,67; oskładkowane 41 666,67; składki 4 066,67 + 625,00 + 1 020,83 = 5 712,50; zasiłek (pula 33 wyczerpana → zasiłek od 1. dnia): 12 080,60/30 = 402,69 × 80% = 322,15 × 5 = 1 610,75 (tylko PIT); zdrowotna 9% × (41 666,67 − 5 712,50) = 3 235,88; PPK pracod. 625,00; podstawa = 41 666,67 + 625 − 5 712,50 − 250 + 1 610,75 (zasiłek) = 37 939,92 → 37 940 × 32% = 12 140,80 − 300 = 11 840,80 → 11 841; PPK prac. 833,33; netto = (41 666,67 + 1 610,75) − 5 712,50 − 3 235,88 − 11 841 − 833,33 = 21 654,71; alimenty: 3/5 × 21 654,71 = 12 992,83 ≥ 3 000, bez kwoty wolnej → potrącenie 3 000 → do wypłaty 18 654,71.",
             "wskazowki": ["Czy 30-krotność liczysz od przychodu, czy od podstawy E/R narastająco — i czy premia roczna się wlicza? (Tak, w miesiącu wypłaty.)",
                           "Lekcje „Zaliczka PIT” (32% od całości po progu), „Chorobowe” (pula wyczerpana → zasiłek od 1. dnia), „Potrącenia” (alimenty 3/5 bez kwoty wolnej).",
                           "Szkic: podstawa E/R narastająco po listopadzie 154 000; grudzień 41 666,67 → 195 666,67 < 282 600; zasiłek 402,69 × 0,8 = 322,15 × 5; 32% od (… ) − 300…"],
             "rozwiazanie": "30-krotność: podstawa E/R narastająco po listopadzie 11 × 14 000 = 154 000; grudzień: pensja 11 666,67 + premia 30 000 = 41 666,67 → 195 666,67 < 282 600 → składki E/R od całości.\nPensja: 14 000 − 14 000/30 × 5 = 11 666,67 (choroba — /30). Przychód oskładkowany 41 666,67.\nSkładki: 4 066,67 + 625,00 + 1 020,83 = 5 712,50. Zdrowotna 9% × 35 954,17 = 3 235,88 (zasiłek nie wchodzi).\nŚwiadczenie: pula 33 dni wyczerpana → zasiłek chorobowy od 1. dnia: 12 080,60/30 = 402,69; × 80% = 322,15; × 5 dni = 1 610,75 (płatnik wypłaca, odlicza w DRA; RSA 313); tylko PIT bez KUP.\nPPK: pracodawcy 625,00 (przychód), pracownika 833,33.\nPodstawa PIT: 41 666,67 + 625,00 − 5 712,50 − 250 + 1 610,75 = 37 939,92 → 37 940; po progu całość 32%: 12 140,80 − 300 = 11 840,80 → 11 841.\nNetto: (41 666,67 + 1 610,75) − 5 712,50 − 3 235,88 − 11 841 − 833,33 = 21 654,71.\nAlimenty: granica 3/5 netto = 12 992,83; bez kwoty wolnej → 3 000 w całości → do wypłaty 18 654,71 zł.\nDochód narastająco po grudniu: 132 451 + 37 940 = 170 391 → PIT-11."},
        ],
        "typowe_bledy": [
            {"komunikat": "KUP odjęte od zasiłku.", "przyczyna": "Zasiłek — przychód z innych źródeł.", "diagnoza": "Warsztat → pole „Zasiłek” — kroki pokazują „+ zasiłki” po KUP.", "poprawka": "KUP tylko od przychodu ze stosunku pracy (w tym chorobowego)."},
            {"komunikat": "Stawka zasiłku liczona jako podstawa × 80% / 30 bez zaokrąglenia dziennej.", "przyczyna": "Kolejność ZUS: dzienna → × % → zaokr. → × dni.", "diagnoza": "Porównaj z Warsztat → Zasiłki (stawka dzienna × % zaokrąglona).", "poprawka": "Zaokrąglaj stawkę dzienną po procencie."},
            {"komunikat": "Kwota wolna 3 605,85 u pracownika z PPK.", "przyczyna": "Minimalne netto z PPK = 3 501,73.", "diagnoza": "Warsztat → Potrącenia z PPK 2.", "poprawka": "Kwota wolna z parametrami pracownika."},
        ],
        "pulapki": ["Lista bez bilansu (brutto = netto + obciążenia) to lista niesprawdzona.", "Każdy wiersz listy najpierw na kartce, potem Tryb ćwiczenia — dopiero wtedy „Dodaj do listy miesiąca”."],
        "zadania": ["Powtórz testy 13 lekcji etapu 2; dla każdego błędnego pytania policz przykład z lekcji jeszcze raz.", "Zbuduj w Warsztacie listę grudnia 2026 dla 8 osób (z chorobą, nadgodzinami, benefitem) i zapisz MD + CSV.", "Wypisz w dzienniku 5 reguł etapu, które najczęściej mylisz — z poprawną wersją."],
        "pytania": [["Jakie obciążenia ma wynagrodzenie chorobowe, a jakie zasiłek?", "Chorobowe: zdrowotna + PIT (z KUP); zasiłek: tylko PIT bez KUP."],
                    ["Kiedy pracownik może obniżyć wpłatę PPK do 0,5%?", "Gdy jego wynagrodzenie nie przekracza 1,2 × minimalnego (5 767,20 w 2026)."],
                    ["Jaki schemat składek ma zleceniobiorca z etatem 5 000 u innej firmy?", "Tylko zdrowotna (ZZA, 04 11); społeczne dobrowolne."]],
        "podsumowanie": "Policzyć kompletną listę z chorobą, zasiłkiem, benefitem, PPK, progiem i potrąceniem, ustalić stawkę zasiłku i wskazać pozycje do RCA/RSA.",
        "test": [
            {"p": "Pracownik w PPK (2%) ma zajęcie niealimentacyjne. Kwota wolna od potrąceń to:", "o": ["3 605,85 — jak dla wszystkich", "3 501,73 — minimalne netto z uwzględnieniem PPK", "4 806", "1/2 netto"], "odp": 1, "w": "Art. 87¹ — minimalne netto dla parametrów pracownika, w tym PPK."},
            {"p": "Wpłata pracodawcy na PPK (1,5%) jest:", "o": ["Podstawą składek ZUS", "Przychodem do PIT, bez ZUS, niewypłacanym", "Potrącana z netto", "Zwolniona z PIT"], "odp": 1, "w": "Art. 12 PIT; §2 ust. 1 pkt 33 rozp. składkowego."},
            {"p": "Miesiąc, w którym pracownik przepracował 9 z 22 dni, w podstawie zasiłku:", "o": ["Uzupełniasz", "Wyłączasz (< 50%)", "Bierzesz faktyczne wynagrodzenie", "Liczysz podwójnie"], "odp": 1, "w": "Art. 38 ust. 2 — mniej niż połowa dni → wyłączenie."},
        ],
    },
    {
        "id": "powtorka_etap_3", "tydzien": 9, "czas_min": 40, "etap": 3,
        "nazwa": "Powtórka etapu 3: ZUS, US, ZFŚS, PFRON i kalendarz — zamknięcie miesiąca i roku",
        "cel": "zamykasz miesiąc (zgłoszenia, komplet, przelewy) i rok (PIT-4R/PIT-11, ZFŚS, PFRON, IWA) w terminach, robisz korekty i wiesz, jak wygląda kalendarz firmy — bez zaglądania do lekcji.",
        "po_co": "w etapie 3 liczby z listy płac stają się dokumentami do urzędów — tu błąd kosztuje odsetki i korekty, a terminy nie negocjują.",
        "slowa": ["powtórka", "etap 3", "ZUS powtórka"],
        "wymagania": ["Zaliczone testy lekcji tygodni 8–9.", "Komplet 01 12 2026 i korekta 02 w symulatorze (Rejestr).", "Warsztat → eZUS/Płatnik, e-Urząd: PIT."],
        "wyjasnienie":
            "## Miesiąc\n"
            "- Zgłoszenia: ZUA (wszystkie), ZZA (zdrowotne), ZWUA (dzień po, kod 100, tryb dla pracownika), ZCNA, ZIUA — 7 dni; kod 6-znakowy; student — brak; dzieło — RUD.\n"
            "- Komplet za miesiąc WYPŁATY: DRA + RCA (każdy z podstawą; 30 00 po ustaniu; 12 11 wychowawczy) + RSA (świadczenia za miesiąc wypłaty z faktycznym okresem; przerwy za miesiąc wystąpienia) + RPA (przychód za inny rok); do 15./20.; NRS; do zapłaty = składki − zasiłki (nie chorobowe); odsetki > 48,06 zł.\n"
            "- Korekty: identyfikator 02+, DRA zawsze, tylko zmienione RCA/RSA; nadpłata pracownika → zwrot (przychód: zdrowotna + PIT), pracodawcy → zaliczenie/RZS-P; niedopłata → dopłata z odsetkami (część ubezpieczonego za zgodą); 5 lat.\n"
            "## Rok\n"
            "- PIT-4R, PIT-8AR, PIT-11 do 31.01 (US), PIT-11 pracownikom do końca lutego (14 dni na wniosek po ustaniu); zasada kasowa; po ustaniu bez kwoty zmniejszającej; ryczałt do 200 zł → PIT-8AR; nierezydent → IFT-1R.\n"
            "- ZFŚS: ≥ 50 etatów; odpis 2 943,23/etat (+ 490,54 na osobę z orzeczeniem); 75% do 31.05, reszta 30.09, korekta 31.12; kryterium socjalne; PIT do 1 000.\n"
            "- PFRON: ≥ 25 etatów, wskaźnik 6%; wpłata = brakujące etaty × 40,65% × przeciętne; DEK-I-0 do 20.; SOD (2 760 / 1 550 / 575) Wn-D do 25. z efektem zachęty.\n"
            "- Kalendarz: miesięczny 5/8/10/15/20/25, roczny (31.01 PIT i IWA, 31.05/30.09 ZFŚS, 30.09 urlopy, 30.11 płatnik zasiłków, 31.12 korekta), cykliczny (badania, BHP, umowy, cudzoziemcy, kary 1 rok, PPK 4 lata), zdarzeniowy (7 dni ZUS, 14 dni protokół, 21 dni odwołanie); przesunięcia: ZUS/PIT → następny roboczy; wypłata → poprzedni.",
        "przyklad":
            "Styczeń 2027 w AGRO-MLEKO (wypłata za grudzień 8.01, bo 10.01 to niedziela; trzynastka 15.01):\n"
            "8.01 wypłata → komplet 01 01 2027 (do 15.02): RCA 62 + 2 (zleceniobiorcy), RSA (świadczenia wypłacone w styczniu za grudniowe L4 + przerwy styczniowe), RPA dla 62 osób (trzynastka za 2026); do zapłaty = składki − zasiłki.\n"
            "do 20.01: zaliczki PIT za wypłaty grudniowe (10.12) → mikrorachunek; DEK-I-0 za grudzień.\n"
            "do 31.01 (nd → 1.02): PIT-4R 2026 (12 miesięcy = 12 przelewów), PIT-8AR, PIT-11 ×70 do US; IWA; informacja o rezygnacji z ZFŚS — nie dotyczy (≥ 50).\n"
            "styczeń: nowe wskaźniki (4 950; 30-krotność; odpis), aneksy < 4 950, plan ZFŚS 2027, przegląd kalendarza.",
        "demonstracja": {
            "tytul": "Zamknięcie grudnia i roku — kolejność czynności kadr w styczniu",
            "kroki": ["Wypłata 8.01 (art. 85 §3 — dzień przed niedzielą) → lista + paski + przelewy komornicze; z niej RCA 01 2027.",
                      "RSA 01 2027: świadczenia wypłacone 8.01 (chorobowe/zasiłki za grudzień, z okresami grudniowymi — kasowo) + przerwy styczniowe (111, 151); RPA: trzynastka za 2026.",
                      "15.01 — ZUS za grudzień? NIE: komplet 12 2026 obejmował wypłatę 10.12 i został wysłany do 15.01; komplet 01 2027 (wypłata 8.01) — do 15.02. Pilnuj: miesiąc kompletu = miesiąc wypłaty.",
                      "20.01 — zaliczki PIT od wypłat GRUDNIOWYCH (10.12) + DEK-I-0; 25.01 — Wn-D.",
                      "31.01 → 1.02 — PIT-4R (uzgodniony z 12 przelewami), PIT-8AR (umowy do 200 zł), PIT-11 (zasada kasowa: wypłata 8.01 → rok 2027!), IWA.",
                      "Styczeń — parametry 2027 w programie i w Warsztacie (Firma ćwiczeniowa → Parametry), aneksy, kwoty wolne, plan odpisu ZFŚS, nowy kalendarz."],
            "wynik": "komplet 01 2027 do 15.02, PIT za grudzień do 20.01, deklaracje roczne do 1.02, parametry 2027 wdrożone — bez pomylenia miesiąca pracy z miesiącem wypłaty."},
        "jak_uruchomic": ["Warsztat → eZUS/Płatnik → Rozliczenie: miesiąc 2027-01 (wypłata 8.01) → Pokaż komplet → Weryfikuj.", "Warsztat → e-Urząd: PIT → Rok 2026 → PIT-4R (12 miesięcy) → porównaj z sumą zaliczek z list.", "Oczekiwany wynik: komplet 01 01 2027 z RSA za świadczenia styczniowe; PIT-4R = suma list 2026."],
        "cwiczenia": [
            {"rodzaj": "prowadzone",
             "tresc": "Zamknij luty 2027 jak w demonstracji: wypłata za styczeń 10.02 (środa), Kowalczyk odchodzi 28.02 (porozumienie), nowy zleceniobiorca od 15.02 (jedyny tytuł), Sobczak zasiłek opiekuńczy 3–5.02 wypłacony 10.03. Wypisz: dokumenty zgłoszeniowe z datami i terminami, komplet (który miesiąc, co w RSA), terminy PIT, ZFŚS i PFRON w lutym–marcu, przesunięcia. Plik: cwiczenia/tydzien_09/powtorka_etap_3_1.md. Czas: 20 minut.",
             "wynik": "ZUA 04 11 nowy zleceniobiorca: data 15.02, termin 22.02; ZWUA Kowalczyk: data 1.03, termin 8.03, kod 100, tryb 1; komplet 01 02 2027 (wypłata 10.02) do 15.03: RCA ze stycznia wypłaconego w lutym; RSA: przerwy lutowe (opieka 3–5.02 — zasiłek wypłacony 10.03 → RSA 312 w komplecie 03 2027, nie 02!), RPA — nie; PIT za wypłaty lutowe do 20.03 (sobota → 22.03); DEK-I-0 do 20.03 → 22.03; ZFŚS: plan odpisu (nie przelew); PFRON Wn-D 25.03; 28.02 — ostatni dzień na PIT-11 pracownikom za 2026 (niedziela → 1.03); Kowalczyk: świadectwo 28.02, ekwiwalent 10.03 (termin wypłaty po ustaniu), PIT-11 za 2027 na wniosek w 14 dni.",
             "wskazowki": ["Do którego kompletu trafia zasiłek za luty wypłacony w marcu? A przerwa 111 z lutego?",
                           "Lekcje „Rozliczenia miesięczne” (kasowo), „Zgłoszenia” (7 dni, dzień po), „Kalendarz” (przesunięcia); kalendarz 2027: 20.03 sobota, 28.02 niedziela.",
                           "Szkic: ZUA 22.02; ZWUA 8.03; komplet 02 do 15.03; RSA 312 → marzec; PIT 20.03 → 22.03; PIT-11 pracownikom 28.02 → 1.03…"],
             "rozwiazanie": "Zgłoszenia: nowy zleceniobiorca (jedyny tytuł) — ZUA 04 11 00, data powstania 15.02.2027, termin 22.02 (poniedziałek); dobrowolne chorobowe od dnia wniosku. Anna Kowalczyk — ZWUA data 1.03.2027, kod 100, tryb 1 (porozumienie), termin 8.03; ZCNA (jeśli zgłaszała rodzinę) wygasa automatycznie.\nKomplet 01 02 2027 (wypłata 10.02 za styczeń): DRA + RCA wszystkich (Kowalczyk jeszcze 01 10) + RSA: przerwy LUTOWE bez świadczeń (np. 111) — za luty; zasiłek opiekuńczy Sobczak 3–5.02 wypłacony 10.03 → RSA 312 w komplecie 01 03 2027 (miesiąc wypłaty), z okresem 3–5.02; RPA — brak (styczeń za styczeń). Termin: 15.03.2027 (poniedziałek). Do zapłaty = składki − zasiłki wypłacone w lutym.\nPIT: zaliczki od wypłat lutowych do 20.03 (sobota) → 22.03 (poniedziałek); PIT-11 za 2026 pracownikom do 28.02 (niedziela) → 1.03 (poniedziałek).\nPFRON: DEK-I-0 za luty do 20.03 → 22.03; Wn-D do 25.03. ZFŚS: plan odpisu na 2027 zatwierdzony (przelew 75% dopiero do 31.05).\nKowalczyk (ustanie 28.02): świadectwo 28.02 (niedziela — wydajesz ostatniego dnia pracy lub najpóźniej w 7 dni pocztą), ekwiwalent i pensja za luty 10.03 (termin wypłaty po ustaniu), bez kwoty zmniejszającej; RCA 03 2027 kod 30 00 dla wypłaty po ustaniu; PIT-11 za 2027 — do końca lutego 2028 lub 14 dni na wniosek."},
            {"rodzaj": "samodzielne",
             "tresc": "Audyt roczny wykazał: (1) Joanna Michalska miała 3 „dzieła” → ZUS uznał za zlecenia (decyzja prawomocna 10.01.2027); (2) w 2026 r. płacono SOD na osobę, która od września pracowała na 1/2 etatu (dofinansowanie proporcjonalne!); (3) odpis ZFŚS przelano na 60 etatów, a faktyczna średnia to 57,2. Zdecyduj dla każdego: jakie dokumenty i korekty, w jakich terminach, jakie kwoty (SOD umiarkowany 1 550; odpis 2 943,23) i gdzie w PIT. Plik: cwiczenia/tydzien_09/powtorka_etap_3_2.md. Czas: 20 minut.",
             "wynik": "(1) ZUA 04 11 od dat umów, ZWUA po; komplety 02 za miesiące wypłat; składki 2 753 + odsetki; korekta PIT-11 2025/2026 (KUP 20%); termin korekt 7 dni od prawomocności (17.01); (2) SOD za IX–XII: 1 550 × 1/2 = 775/mies. → nadpłata 4 × 775 = 3 100 do zwrotu do PFRON z odsetkami (korekta Wn-D/INF-D-P); (3) korekta odpisu do 31.12: (60 − 57,2) × 2 943,23 = 8 241,04 — nadwyżka zostaje na rachunku funduszu jako środki roku następnego i pomniejsza przelew 2027; bez PIT.",
             "wskazowki": ["Które z trzech spraw dotyczą ZUS, które PFRON, a które funduszu — i jakie mają terminy korekt?",
                           "Lekcje „Korekty ZUS” (7 dni, 5 lat), „ZFŚS i PFRON” (SOD proporcjonalny do etatu; korekta odpisu 31.12).",
                           "Szkic: (1) komplety 02 + PIT; (2) 775 × 4 = 3 100 zwrotu; (3) 2,8 × 2 943,23 = 8 241,04…"],
             "rozwiazanie": "(1) Michalska: decyzja ZUS prawomocna 10.01.2027 → w 7 dni (do 17.01) ZUA 04 11 00 z datami zawarcia umów (2025 ×2, 2.11.2026) i ZWUA (dzień po zakończeniu każdej); komplety korygujące 02 za miesiące wypłat (DRA + RCA Michalskiej); składki: ubezpieczona 11,26% × 7 500 = 844,50, zleceniodawca 17,46% = 1 309,50, zdrowotna 599,00 → 2 753,00 + odsetki od każdej raty; płaci firma, zwrot części ubezpieczonej — tylko za zgodą/w sądzie. PIT: korekta PIT-11 za 2025 i 2026 (przychód z art. 13 pkt 8, KUP 20% od przychodu po składkach zamiast 50%), korekta PIT-4R, dopłata zaliczek z odsetkami.\n(2) SOD: dofinansowanie przysługuje proporcjonalnie do wymiaru etatu (art. 26a ust. 1 — kwota na pełny etat; przy 1/2 etatu — 50%): od września 775 zamiast 1 550 → nadpłata 4 × 775 = 3 100 zł; korekta Wn-D i INF-D-P za IX–XII, zwrot do PFRON z odsetkami jak od zaległości podatkowych; przy wykryciu w kontroli PFRON — zwrot nienależnej kwoty z odsetkami jak od zaległości podatkowych i odpowiedzialność za nieprawdziwe dane (art. 49e ustawy o rehabilitacji); korekta z własnej inicjatywy ogranicza odsetki.\n(3) ZFŚS: korekta odpisu do 31.12 wg faktycznego przeciętnego zatrudnienia: (60 − 57,2) × 2 943,23 = 8 241,04 zł nadwyżki; środki pozostają na rachunku funduszu (art. 11 ustawy o ZFŚS: niewykorzystane przechodzą na rok następny; nie wycofujesz ich do firmy) — w planie 2027 pomniejszasz pierwszy przelew o nadwyżkę. Bez skutków PIT/ZUS."},
        ],
        "typowe_bledy": [
            {"komunikat": "Komplet „za grudzień” wysłany z wypłatą styczniową.", "przyczyna": "Miesiąc kompletu = miesiąc wypłaty.", "diagnoza": "Data wypłaty 8.01 → komplet 01 2027.", "poprawka": "Zasada kasowa w ZUS i PIT."},
            {"komunikat": "RSA z zasiłkiem za luty w komplecie lutowym, choć wypłata była w marcu.", "przyczyna": "Świadczenia — za miesiąc wypłaty.", "diagnoza": "Kiedy wypłacono?", "poprawka": "RSA 312 w komplecie 03 z okresem lutowym."},
            {"komunikat": "PIT-4R nie zgadza się z przelewami o kwotę ryczałtu 12%.", "przyczyna": "Ryczałt należy do PIT-8AR.", "diagnoza": "Umowy ≤ 200 zł z osobami spoza etatu?", "poprawka": "Przenieś do PIT-8AR."},
        ],
        "pulapki": ["Korekty rób w 7 dni od stwierdzenia — każdy miesiąc zwłoki to odsetki i gorsza pozycja przy kontroli.", "Przy każdym terminie w kalendarzu zapisz, czy to miesiąc pracy, czy wypłaty."],
        "zadania": ["Powtórz testy 6 lekcji etapu 3.", "Wyślij w symulatorze pełną sekwencję: ZUA → komplet 01 → korekta 02 → ZWUA — i zapisz Rejestr do projektu.", "Wygeneruj PIT-11 dla 3 osób i PIT-4R w Warsztacie; uzgodnij z listami."],
        "pytania": [["Co odejmujesz w DRA od składek do zapłaty?", "Tylko zasiłki wypłacone przez płatnika (313, 312, 314, 327…), nie wynagrodzenie chorobowe (331)."],
                    ["Kiedy termin ZUS się przesuwa, a kiedy termin wypłaty?", "ZUS/PIT — na następny dzień roboczy; wypłata — na poprzedni."],
                    ["Od kiedy liczysz 75% odpisu ZFŚS i do kiedy przelewasz?", "Odpis planowany na etaty z 1.01; 75% do 31.05, reszta do 30.09; korekta do 31.12."]],
        "podsumowanie": "Zamknąć miesiąc i rok w ZUS/US/PFRON/ZFŚS we właściwych terminach, przypisać świadczenia i przerwy do właściwego kompletu, przeprowadzić korekty i uzgodnić deklaracje roczne.",
        "test": [
            {"p": "Zasiłek za 3–5.02 wypłacony 10.03. W którym komplecie RSA?", "o": ["02 (luty — miesiąc przerwy)", "03 (marzec — miesiąc wypłaty), z okresem lutowym", "W obu", "W rocznym"], "odp": 1, "w": "Świadczenia — za miesiąc wypłaty; przerwy bez świadczeń — za miesiąc wystąpienia."},
            {"p": "Korekta kompletu wymaga wysłania:", "o": ["Tylko zmienionych RCA", "DRA + zmienionych RCA/RSA z identyfikatorem 02", "Całego kompletu z identyfikatorem 01", "Pisma do ZUS"], "odp": 1, "w": "DRA zawsze; numer kolejny."},
            {"p": "Pracodawca zatrudnia 24,5 etatu i 0 osób z orzeczeniem. Wpłata na PFRON:", "o": ["6% × 24,5 × 40,65% × przeciętne", "Brak — poniżej 25 etatów", "1 550 zł miesięcznie", "Zależy od PKD"], "odp": 1, "w": "Obowiązek od 25 etatów (art. 21 ustawy o rehabilitacji)."},
        ],
    },
    {
        "id": "powtorka_etap_4", "tydzien": 11, "czas_min": 45, "etap": 4,
        "nazwa": "Powtórka etapu 4 i całego kursu: ustanie zatrudnienia, compliance, kontrola — audyt firmy",
        "cel": "przeprowadzasz pracownika przez ustanie zatrudnienia (tryb, okres, pismo, świadectwo, rozliczenie), rozpoznajesz mobbing/dyskryminację i lukę płacową, masz procedury 2026/2027 i potrafisz przygotować firmę do kontroli — a z całego kursu umiesz wskazać, gdzie szukać każdej odpowiedzi.",
        "po_co": "etap 4 domyka kurs: wszystko, czego nauczyłeś się o zatrudnieniu, czasie pracy, płacach i ZUS, wraca w rozliczeniu końcowym i w kontroli — to Twój projekt końcowy (audyt firmy).",
        "slowa": ["powtórka", "etap 4", "podsumowanie kursu", "audyt"],
        "wymagania": ["Zaliczone testy lekcji tygodni 10–11 i powtórek etapów 0–3.", "Pliki: pisma rozwiązujące, świadectwo, procedury (mobbing, sygnaliści, zdalna), teczka kontrolna, audyt 60 pytań.", "Cały Warsztat."],
        "wyjasnienie":
            "## Ustanie zatrudnienia\n"
            "- Tryby art. 30; okres ze stażu zakładowego (2 tyg./1/3 mies.; próbna 3 dni/1 tydz./2 tyg.); koniec: sobota / ostatni dzień miesiąca; przyczyna konkretna (także określona); pouczenie 21 dni; ochrona art. 41, 39 (4 lata), 177; art. 52 — 1 miesiąc od wiedzy, L4 nie chroni.\n"
            "- Grupowe: próg 10/10%/30 w 30 dniach (porozumienia ≥ 5 liczą się); 20 dni + PUP; odprawy 1/2/3 (limit 15 × min.), bez ZUS, z PIT; ochrona przy grupowym tylko zmieniające + dodatek.\n"
            "- Świadectwo w dniu ustania (bez przyczyny; urlop z ekwiwalentem; 33 dni; nieskładkowe; zajęcia); sprostowanie 14/7/14 dni; rozliczenie końcowe: pensja za część, ekwiwalent (termin wypłaty / 10 dni), odprawa, PIT bez oświadczeń, ZWUA 7 dni, PIT-11 na wniosek 14 dni.\n"
            "## Compliance 2026/2027\n"
            "- Mobbing: nowa definicja od 5.11.2026 (uporczywe nękanie, bez wymogu skutku zdrowotnego), odszkodowanie ≥ 6 × min., procedura do 5.05.2027; dyskryminacja — kryterium, ciężar dowodu na pracodawcy; nierówne traktowanie — bez kryterium.\n"
            "- Jawność: obowiązuje — widełki (24.12.2025), zakaz pytań o zarobki; projekt UC127 — informacja 2 mies., raportowanie, luka > 5%; luka liczona w kategoriach, rozkładana na kryteria obiektywne.\n"
            "- Sygnaliści (≥ 50): procedura, 7 dni / 3 mies., rejestr, ochrona; zdalna: wniosek wiążący (dziecko do 4 lat), 7 dni, porozumienie, ryczałt z kalkulacją; monitoring/trzeźwość: regulamin, 2 tygodnie, retencja; RODO: upoważnienia, RCPD, powierzenia, retencja, 72 h.\n"
            "- Kontrola: PIP bez zapowiedzi (protokół — 7 dni zastrzeżeń; nakaz płacowy natychmiast; wystąpienie 30 dni; mandat/sąd do 30 000); ZUS/US z zawiadomieniem 7–30 dni (zastrzeżenia 14 dni; decyzja — odwołanie 1 mies.); teczka kontrolna, książka kontroli, audyt roczny.",
        "przyklad":
            "Projekt końcowy — audyt AGRO-MLEKO (fragment): 10 pytań, 10 odpowiedzi, 10 działań:\n"
            "1. Umowy terminowe w limicie 33/3? → 1 przekroczenie (aneks) → umowa nieokreślona z mocy prawa, informacja dla pracownika.\n"
            "2. Ewidencja z godzinami od–do? → biuro tak, produkcja tylko „12 h” → nowy wzór karty od 1.01.\n"
            "3. Dodatki 100% za niedziele? → błąd parametru → wyrównanie 36 mies. + RPA.\n"
            "4. Podstawy zasiłków z regulaminem (stażowy pomijany)? → 2 błędy → korekta kwot i RSA.\n"
            "5. Zleceniobiorcy — stawka ≥ 31,40 i oświadczenia? → Pawlak 25 zł/h → aneks; Dąbrowski — brak weryfikacji statusu → procedura.\n"
            "6. Komplety ZUS = listy? → zgodne; 1 RSA za zły miesiąc → korekta 02.\n"
            "7. PIT-4R = przelewy? → różnica 470 → 2 listy dodatkowe nieujęte → korekta.\n"
            "8. ZFŚS kryterium, PFRON wskaźnik? → paczki po równo → regulamin z progami; PFRON 2,0/3,51 etatu → plan zatrudnienia.\n"
            "9. Procedury: mobbing (do 5.05.2027), sygnaliści, zdalna, trzeźwość? → brak 3 z 4 → harmonogram wdrożeń.\n"
            "10. Teczka kontrolna i kalendarz? → brak → zbudowane w tygodniach 12 i 15.",
        "demonstracja": {
            "tytul": "Audyt firmy — jak z 60 pytań zrobić plan naprawczy, który obroni się przed PIP i ZUS",
            "kroki": ["Pytania grupujesz wg obszarów = etapów kursu (zatrudnienie, czas pracy, płace, zasiłki, ZUS/US, ZFŚS/PFRON, ustanie, compliance); każde pytanie ma podstawę prawną i dowód (dokument), który pokazałbyś inspektorowi.",
                      "Odpowiedź TAK/NIE/CZĘŚCIOWO z liczbą (ile osób, ile miesięcy, jaka kwota) — nie „raczej tak”.",
                      "Ryzyko: kwota (wyrównania, składki, odsetki) + sankcja (mandat, grzywna, nakaz, kara UODO) + termin przedawnienia (3 lata roszczenia, 5 lat ZUS/PIT).",
                      "Działanie: konkretne (dokument, korekta, aneks, procedura), właściciel, termin, koszt; priorytet: najpierw to, co jest nielegalne „dziś” (trzeźwość bez regulaminu, nielegalny cudzoziemiec, niewypłacone wynagrodzenie), potem terminy ustawowe (mobbing 5.05.2027), potem optymalizacje (PFRON, benefity).",
                      "Dowody realizacji: wpis w rejestrze, zrzuty parametrów, listy dodatkowe z UPP — to one bronią firmę w kontroli (art. 94³ — „przeciwdziałanie”, PIP — „usunięto przed kontrolą”).",
                      "Raport dla zarządu na 1 stronę: 5 największych ryzyk z kwotami, 5 działań na 30 dni, koszt całości, harmonogram."],
            "wynik": "plan naprawczy z priorytetami i kwotami + raport dla zarządu — projekt końcowy kursu."},
        "jak_uruchomic": ["Otwórz cwiczenia/tydzien_11/powtorka_etap_4_1.md — audyt skrócony (20 pytań) z kolumnami: obszar | pytanie | podstawa | dowód | stan | ryzyko | działanie | termin | właściciel.", "Do każdej odpowiedzi użyj Warsztatu (Przepisy — podstawa; Lista płac/Zasiłki — kwoty; eZUS — Rejestr).", "Oczekiwany wynik: 20 wierszy + raport 1 strony (szablon w Prompty → Szablony → „Raport z audytu”)."],
        "cwiczenia": [
            {"rodzaj": "prowadzone",
             "tresc": "Wypełnij 10 wierszy audytu (obszary: umowy, ewidencja, nadgodziny, zasiłki, zlecenia, ZUS, PIT, ZFŚS, procedury, teczka) dla AGRO-MLEKO na podstawie wszystkiego, co zrobiłeś w kursie (Twoje pliki w katalogu projektu) — jak w demonstracji: stan, kwota ryzyka, działanie, termin. Plik: cwiczenia/tydzien_11/powtorka_etap_4_1.md. Czas: 25 minut.",
             "wynik": "10 wierszy z liczbami (np. nadgodziny: 11 osób × 4 380 łącznie + odsetki; zlecenie Pawlak: niedopłata 768/mies. × miesiące; PFRON 5 524/mies. możliwe do wyzerowania; ZFŚS: ryzyko składek od 18 600), priorytety 1–3 i harmonogram 30/60/90 dni.",
             "wskazowki": ["Dla każdego obszaru: jaki dokument pokazałbyś inspektorowi w 5 minut? Jeśli nie wiesz — to jest wiersz „NIE”.",
                           "Demonstracja, kroki 1–4; liczby z lekcji: PIP (4 380), zlecenia (31,40 × 120 − 3 000 = 768), ZFŚS (62 × 300), PFRON (5 524,34).",
                           "Szkic wiersza: „Nadgodziny | dodatki 100% za niedziele | art. 151¹ | listy płac, ewidencja | NIE (3 mies., 11 osób) | 4 380 + odsetki + mandat | lista dodatkowa + parametr | 30.11 | kadry”."],
             "rozwiazanie": "| Obszar | Pytanie | Podstawa | Dowód | Stan | Ryzyko | Działanie | Termin | Właściciel |\n|---|---|---|---|---|---|---|---|---|\n| Umowy | Czy umowy terminowe mieszczą się w 33/3? | art. 25¹ | kartoteka umów | CZĘŚCIOWO (1 aneks) | umowa bezterminowa z mocy prawa; spór | informacja pracownikowi, korekta kartoteki | 14 dni | kadry |\n| Ewidencja | Godziny od–do, polecenia nadgodzin? | §6 rozp. dokum. | karty ewidencji | NIE (produkcja) | przegrane spory o nadgodziny; grzywna | nowy wzór karty; RCP | 1.01.2027 | kadry + produkcja |\n| Nadgodziny | Dodatki 100% za niedziele/noc? | art. 151¹ | listy płac | NIE (3 mies., 11 osób) | 4 380 + odsetki + mandat/nakaz | lista dodatkowa, parametr programu, RPA | 30.11.2026 | kadry |\n| Zasiłki | Podstawy wg regulaminu (stażowy pomijany, premia uzupełniana)? | art. 36–45 zasiłkowej | kartoteki zasiłkowe | CZĘŚCIOWO (2 błędy) | nienależne/zaniżone zasiłki; korekty RSA | przeliczenie, korekta 02, wyrównanie | 15.12 | kadry |\n| Zlecenia | Stawka ≥ 31,40, oświadczenia, status studenta? | art. 8a; art. 6 ust. 4 syst. | umowy, ewidencje godzin | NIE (Pawlak 25 zł/h; brak weryfikacji studenta) | 768/mies. niedopłaty + mandat PIP; składki wstecz | aneks; procedura weryfikacji co semestr | 30.11 | kadry |\n| ZUS | Komplety = listy; RSA we właściwym miesiącu? | ustawa systemowa | Rejestr UPP, listy | CZĘŚCIOWO (1 RSA) | odsetki, korekty | komplet 02 | 7 dni | kadry |\n| PIT | PIT-4R = przelewy? | art. 38 PIT | zestawienie miesięczne | NIE (470 zł) | odsetki, KKS | uzgodnienie, dopłata | 31.01 | księgowa |\n| ZFŚS/PFRON | Kryterium socjalne; wskaźnik 6%? | art. 8 ZFŚS; art. 21 rehab. | regulamin, DEK | NIE / 2,0 z 3,51 | składki od 18 600; 5 524/mies. | progi dochodowe; plan zatrudnienia 2 osób z orzeczeniem | 31.01 / 30.06 | komisja / zarząd |\n| Procedury | Mobbing, sygnaliści, zdalna, trzeźwość? | KP, ustawy 2024/2026 | regulaminy | NIE (3 z 4) | odszkodowania ≥ 28 836; grzywny; nielegalna kontrola | harmonogram: trzeźwość 45 dni, sygnaliści 45 dni, mobbing do 5.05.2027 | j.w. | kadry + zarząd |\n| Teczka/kalendarz | Teczka kontrolna i kalendarz z właścicielami? | — | — | TAK (z kursu) | — | aktualizacja kwartalna | co kwartał | kadry |\nPriorytety: 1) nadgodziny + zlecenia (nielegalne niedopłaty), 2) ZUS/PIT korekty (odsetki rosną), 3) procedury (terminy ustawowe). Koszt: ok. 10 000 zł wyrównań + ok. 3 000 odsetek; oszczędność: PFRON do 66 000 zł/rok."},
            {"rodzaj": "samodzielne",
             "tresc": "Napisz raport z audytu dla zarządu (1 strona, max 12 zdań + tabela 5 ryzyk): kontekst, 5 największych ryzyk z kwotami i terminami przedawnienia, 5 działań na 30 dni, koszt i oszczędność, prośba o decyzje (3 punkty: np. zatrudnienie 2 osób z orzeczeniem, aneksy, budżet na szkolenia). Użyj liczb z ćwiczenia 1. Plik: cwiczenia/tydzien_11/powtorka_etap_4_2.md. Czas: 20 minut.",
             "wynik": "raport z tabelą: nadgodziny (4 380 + odsetki; 3 lata), zlecenia (768/mies.; mandat do 30 000), ZFŚS (składki od 18 600 + 5 lat), PFRON (5 524/mies. — do uniknięcia), procedury (odszkodowanie ≥ 28 836 za jedno zgłoszenie); działania 30 dni; koszt ~13 000, oszczędność ~66 000/rok; 3 decyzje do podjęcia.",
             "wskazowki": ["Co zarząd musi wiedzieć w pierwszym zdaniu? (Największe ryzyko w złotych i co to kosztuje, jeśli nic nie zrobimy.)",
                           "Demonstracja, krok 6; Prompty → Szablony → „Raport z audytu”.",
                           "Szkic: akapit 1 — kontekst i wynik ogólny; tabela 5 ryzyk (kwota, sankcja, przedawnienie); akapit 2 — 5 działań; akapit 3 — koszt/oszczędność; akapit 4 — decyzje…"],
             "rozwiazanie": "RAPORT Z AUDYTU KADROWO-PŁACOWEGO — AGRO-MLEKO sp. z o.o. (stan: listopad 2026)\nAudyt 60 pytań objął zatrudnienie, czas pracy, płace, zasiłki, ZUS/US, ZFŚS/PFRON, ustanie zatrudnienia i procedury compliance. Firma prowadzi dokumentację w większości poprawnie; zidentyfikowano 5 ryzyk o łącznej wartości ok. 95 000 zł (w tym 66 000 zł rocznie możliwych oszczędności) i 3 obszary wymagające decyzji zarządu.\n| # | Ryzyko | Kwota | Sankcja | Przedawnienie |\n|---|---|---|---|---|\n| 1 | Brak dodatków 100% za niedziele (11 osób, 3 mies.) | 4 380 zł + odsetki ok. 400 zł; ten sam błąd mógł dotyczyć 36 mies. (do ok. 50 000) | nakaz płacowy, mandat 1 500 / grzywna do 30 000 | 3 lata (art. 291) |\n| 2 | Zlecenie poniżej stawki minimalnej (25 zł/h) | 768 zł/mies. od II 2026 (ok. 7 700) | mandat PIP do 30 000 | 3 lata |\n| 3 | Świadczenia z ZFŚS bez kryterium | składki od 18 600 zł (ok. 6 300 + odsetki) | decyzja ZUS, wykroczenie art. 12a | 5 lat |\n| 4 | Wpłaty PFRON przy 2,0 z 3,51 etatu | 5 524 zł/mies. (66 000/rok) — do uniknięcia | — | — |\n| 5 | Brak procedur: trzeźwość, sygnaliści, mobbing (termin 5.05.2027) | jedno zgłoszenie mobbingu bez procedury: ≥ 28 836 zł + zadośćuczynienie | grzywny PIP; nielegalna kontrola trzeźwości | — |\nDziałania na 30 dni: (1) lista dodatkowa z wyrównaniem nadgodzin + korekta parametru (do 30.11); (2) aneks do umowy zlecenia Pawlak (do 30.11); (3) regulamin ZFŚS z progami dochodowymi (do 31.12) i korekta paczek; (4) wstrzymanie kontroli trzeźwości do zmiany regulaminu + projekt procedur sygnalistów i antymobbingowej (konsultacje do 31.12); (5) komplet korygujący ZUS i uzgodnienie PIT-4R (do 15.12).\nKoszt: wyrównania i odsetki ok. 13 000 zł, szkolenia kierowników ok. 3 000 zł. Oszczędność: PFRON do 66 000 zł rocznie po zatrudnieniu 2 osób z orzeczeniem (plus SOD 3 100 zł/mies.).\nDecyzje zarządu: (a) zgoda na zatrudnienie 2 osób z orzeczeniem o umiarkowanym stopniu (pakowanie/magazyn) od 1.02.2027; (b) aneksy do 4 950 zł od 1.01.2027 dla 2 osób; (c) budżet na szkolenia kierowników (nadgodziny, mobbing, kontrola L4) w I kwartale 2027."},
        ],
        "typowe_bledy": [
            {"komunikat": "Audyt pełen „raczej tak”.", "przyczyna": "Brak dowodu przy odpowiedzi.", "diagnoza": "Czy przy każdym TAK jest nazwa dokumentu?", "poprawka": "TAK tylko z dokumentem; inaczej NIE/CZĘŚCIOWO."},
            {"komunikat": "Plan naprawczy bez kwot.", "przyczyna": "Zarząd nie podejmie decyzji bez liczb.", "diagnoza": "Policz w Warsztacie (listy, składki, odsetki).", "poprawka": "Każde ryzyko w złotych z terminem przedawnienia."},
            {"komunikat": "Świadectwo z przyczyną, pismo bez pouczenia — w pliku z zadania tygodnia 13.", "przyczyna": "Powtórka nie objęła własnych plików.", "diagnoza": "Przejrzyj pisma z zadań pod kątem listy kontrolnej (tryb, podstawa, przyczyna, okres, data, pouczenie, podpis).", "poprawka": "Popraw wzory w katalogu projektu — będą Twoimi szablonami w pracy."},
        ],
        "pulapki": ["Powtórka końcowa to audyt — nie czytanie; każda lekcja kursu ma w nim jedno pytanie.", "Jeśli nie wiesz, gdzie w Warsztacie sprawdzić daną liczbę — wróć do lekcji „Narzędzia kadrowca”."],
        "zadania": ["Powtórz testy 7 lekcji etapu 4 i 4 powtórek etapów 0–3.", "Wykonaj projekt końcowy: audyt 60 pytań + raport dla zarządu (zadanie tygodnia 15).", "Odpytaj się w Asystencie: „odpytaj mnie jak rekruter” — 10 pytań; zapisz, na które nie odpowiedziałeś pewnie."],
        "pytania": [["Jaki środek PIP jest wykonalny natychmiast i co grozi za jego niewykonanie?", "Nakaz wypłaty wynagrodzenia — odwołanie nie wstrzymuje; grzywna w celu przymuszenia i wykroczenie."],
                    ["Co musi wykazać pracodawca, by nie odpowiadać za mobbing kierownika?", "Że rzeczywiście przeciwdziałał: procedura, szkolenia, reakcja na zgłoszenie — udokumentowane."],
                    ["Od czego zależy, czy zwolnienie 9 + 4 osób jest grupowe?", "Czy porozumienia z inicjatywy pracodawcy liczą się (≥ 5) i czy suma w 30 dniach ≥ 10 (firma < 100)."]],
        "podsumowanie": "Przeprowadzić audyt firmy we wszystkich obszarach kursu, wycenić ryzyka, ułożyć plan naprawczy z priorytetami i napisać raport, na podstawie którego zarząd podejmie decyzje — to jest umiejętność końcowa kursu.",
        "test": [
            {"p": "Nowa definicja mobbingu (od 5.11.2026) nie wymaga już:", "o": ["Uporczywości", "Wykazania długotrwałości i skutku w postaci zaniżonej oceny przydatności/rozstroju zdrowia", "Naruszenia godności", "Zgłoszenia do PIP"], "odp": 1, "w": "Ustawa z 19.06.2026 — uporczywe nękanie; odszkodowanie ≥ 6 × minimalne."},
            {"p": "Inspektor PIP przyszedł bez zawiadomienia. Recepcja powinna:", "o": ["Odmówić wejścia do czasu zawiadomienia", "Sprawdzić legitymację, wpuścić, wezwać osobę kontaktową, wpisać do książki kontroli", "Zadzwonić po policję", "Poprosić o przyjście za 7 dni"], "odp": 1, "w": "PIP kontroluje bez uprzedzenia; upoważnienie może być doręczone do 7 dni."},
            {"p": "Odprawa z ustawy o zwolnieniach grupowych:", "o": ["Oskładkowana i opodatkowana", "Bez ZUS, z PIT, limit 15 × minimalne", "Bez ZUS i PIT", "Z ZUS, bez PIT"], "odp": 1, "w": "§2 ust. 1 pkt 3 rozp. składkowego; brak zwolnienia w PIT."},
        ],
    },
]
