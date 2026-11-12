# -*- coding: utf-8 -*-
"""
Nadpisania zadań tak, aby wszystko dało się wykonać w Mentorze (Warsztat), bez kont zewnętrznych, instalacji i arkuszy.
NADPISZ[id] = {pole: nowa wartość} — tylko podane pola są zastępowane w zbuduj.py. ISAP/Git pojawiają się wyłącznie jako opcja.
"""

W = "Warsztat → "

NADPISZ = {
    "k0z1": {
        "kroki": [
            "Utwórz folder kadry-praktyka (np. w Dokumentach: prawy przycisk → Nowy → Folder) i wskaż go w Mentorze: Mój projekt → „Wybierz katalog…”. Wewnątrz utwórz podfoldery: 01-zatrudnienie, 02-czas-pracy, 03-urlopy, 04-place, 05-zus-us, 06-zakonczenie, 07-procedury, 99-notatki.",
            "Mój projekt → „Skopiuj materiały kursu tutaj” → potwierdź. W folderze pojawią się START_TUTAJ.md oraz katalogi cwiczenia/, rozwiazania/, przyklady/, lekcje/, pomoc/ (pliki startowe do ćwiczeń z każdej lekcji; nic nie nadpisuje Twoich plików).",
            "Utwórz FIRMA.md — najprościej: Warsztat → Firma ćwiczeniowa → „Zapisz FIRMA.md do projektu” (plik z opisem firmy, 12 osobami z PESEL, parametrami 2026 i regulaminami). Alternatywa ręczna: szablon cwiczenia/tydzien_00/start_jak_sie_uczyc_2.md i dane z Warsztatu.",
            "Otwórz FIRMA.md i sprawdź, że są w nim: opis firmy (62 pracowników, 3 zmiany, zleceniobiorcy, dzieło), tabela osób (w tym: próbna, określona, 50+, 1/2 etatu, pensja minimalna 4 806, powyżej progu 14 000, orzeczenie, do 26 lat) i sekcja Regulaminy (wypłata do 10., systemy czasu pracy, dodatek nocny, premia 10%, ZFŚS, PPK, wypadkowa 1,20%). Dopisz pod tabelą jedno zdanie: która osoba będzie „Twoim” pracownikiem do kazusów w tygodniu 1.",
            "Zapisz w 99-notatki/notatki.md pierwszą notatkę: „Czego będę się uczył i po co” — 5 zdań; w dziennik.md (Mentor → Dziennik) jedno zdanie o dniu 1.",
        ],
        "sprawdz": "Mój projekt pokazuje Twój folder, START_TUTAJ.md i FIRMA.md jako wykryte; FIRMA.md ma opis firmy, tabelę osób i sekcję Regulaminy; Plan → Tydzień 0 → zadanie 1 → ✔.",
        "problemy": ["„Skopiuj materiały” mówi „Najpierw wskaż katalog projektu” → kliknij Tak i wybierz folder; potem kliknij kopiowanie ponownie.",
                     "FIRMA.md „nie wykryty” → Mój projekt → „Odśwież”; sprawdź, czy plik nie nazywa się FIRMA.md.txt (Eksplorator → Widok → Rozszerzenia nazw plików).",
                     "Nie wiesz, jakie wynagrodzenia są realne → w Warsztat → Firma ćwiczeniowa są stawki 4 806–14 000 zł; w 2026 żadne nie może być niższe niż 4 806 zł na pełny etat (1/2 etatu: 2 403)."],
    },
    # ============================================================ TYDZIEŃ 0
    "k0z2": {
        "tytul": "Narzędzia kadrowca w Warsztacie: eZUS/Płatnik, e-Urząd, kalkulatory",
        "opis": "Poznajesz symulatory wbudowane w Mentora — tu będziesz zgłaszać, rozliczać i liczyć przez cały kurs. Bez kont i instalacji.",
        "kroki": [
            "Otwórz zakładkę Warsztat (pasek boczny). Kliknij po kolei każde narzędzie: Firma ćwiczeniowa, Lista płac, Zasiłki i chorobowe, Urlopy i ekwiwalent, Czas pracy, Potrącenia, eZUS / Płatnik, e-Urząd: PIT, Przepisy. W każdym przeczytaj szary opis pod tytułem — mówi, co narzędzie liczy i co zapisuje.",
            "Warsztat → Firma ćwiczeniowa: przejrzyj 12 osób (8 pracowników, 3 zleceniobiorców, 1 dzieło) i założenia regulaminów. Kliknij „Zapisz FIRMA.md do projektu” — plik trafi do Twojego katalogu (uzupełnia to, co zrobiłeś w zadaniu 1).",
            "Warsztat → eZUS / Płatnik: zakładka „Ubezpieczeni” to rejestr płatnika (w prawdziwym życiu: eZUS → Płatnik → Ubezpieczeni). Wszyscy mają status NIEZGŁOSZONY — bo w symulacji nic jeszcze nie wysłałeś. Zakładka „e-ZLA” to skrzynka zwolnień lekarskich, którą w prawdziwej firmie widzisz po zalogowaniu do eZUS pełnomocnictwem PEL.",
            "Warsztat → e-Urząd: PIT — tu w tygodniu 9 wygenerujesz PIT-11 i PIT-4R z kartoteki; w prawdziwym życiu wysyła się je przez e-Deklaracje z pełnomocnictwem UPL-1. Warsztat → Lista płac: kliknij „Policz” dla domyślnych 6 000 zł i prześledź kroki obliczenia (od składek do kosztu pracodawcy).",
            "Zapisz w dostepy.md (katalog 99-notatki): dla każdego z 4 prawdziwych systemów (eZUS, Płatnik, e-Urząd Skarbowy, program kadrowy) — jedno zdanie „do czego służy” i „jaki dokument daje dostęp pracownikowi kadr” (PEL do ZUS, UPL-1 do e-Deklaracji, nadanie uprawnień w programie, certyfikat kwalifikowany do Płatnika). Dopisz, które narzędzie Warsztatu go zastępuje w kursie.",
        ],
        "sprawdz": "Otworzyłeś wszystkie 9 narzędzi; FIRMA.md zapisany z Warsztatu; dostepy.md opisuje PEL i UPL-1 oraz mapuje systemy na narzędzia Warsztatu.",
        "problemy": ["„Zapisz do projektu” pisze „Najpierw wskaż katalog projektu” → Mój projekt → Wybierz katalog (folder kadry-praktyka z zadania 1).",
                     "Chcesz zobaczyć prawdziwe eZUS? To opcja, nie wymóg: zus.pl → eZUS, logowanie profilem zaufanym — kurs tego nie wymaga."],
        "pliki": ["FIRMA.md", "dostepy.md"],
    },
    "k0z3": {
        "tytul": "Biblioteka przepisów: Warsztat → Przepisy (i ISAP jako opcja)",
        "opis": "Nawyk sprawdzania u źródła — na wbudowanej bibliotece 48 przepisów; ISAP tylko, jeśli masz internet.",
        "kroki": [
            "Warsztat → Przepisy. W polu „Szukaj” wpisz kolejno: „33 dni”, „7 dni”, „odprawa”, „próg” — zobacz, jak biblioteka filtruje po treści. Kliknij wpis — po prawej masz akt, artykuł, streszczenie i lekcję, do której należy.",
            "Zapisz w przepisy.md listę 10 aktów prawnych kadrowca (nazwa, data uchwalenia, do czego go używasz): Kodeks pracy, ustawa o systemie ubezpieczeń społecznych, ustawa zasiłkowa, ustawa o PIT, o ZFŚS, o PPK, o zwolnieniach grupowych, o ochronie sygnalistów, rozporządzenie o dokumentacji pracowniczej, rozporządzenie o minimalnym wynagrodzeniu. Wszystkie znajdziesz w bibliotece (pole „akt”).",
            "Dla 5 wpisów z biblioteki zapisz własnymi słowami, co mówi przepis (2 zdania) — np. art. 92 KP, art. 25¹ KP, art. 36 ustawy zasiłkowej, art. 94³ KP (mobbing od 5.11.2026), art. 87 KP.",
            "Zasada hierarchii: w przepisy.md wpisz w kolejności od najważniejszego: Konstytucja → ustawa → rozporządzenie → układ/regulamin → umowa, i zdanie o art. 18 KP (co się dzieje, gdy umowa daje mniej niż ustawa).",
            "Opcjonalnie (jeśli masz internet): pod każdym wpisem w bibliotece jest link do ISAP — otwórz Kodeks pracy i zobacz pole „Stan prawny na dzień”. Kurs tego nie wymaga; biblioteka ma stan prawny z listopada 2026.",
            "Poproś Asystenta (działa też offline): „co to jest zasada uprzywilejowania pracownika”.",
        ],
        "sprawdz": "przepisy.md ma 10 aktów z przeznaczeniem, 5 streszczeń własnymi słowami i hierarchię źródeł.",
        "problemy": ["Nie znajdujesz wpisu w bibliotece → szukaj po liczbie lub słowie z treści (np. „182”), nie po numerze artykułu z indeksem górnym."],
    },
    "k0z5": {
        "kroki": [
            "W mapa_procesow.md narysuj (jako listę numerowaną w Markdown) cykl życia pracownika: rekrutacja → oferta → umowa → onboarding (badania, BHP, ZUS, PPK, informacja o warunkach) → czas pracy i nieobecności → lista płac co miesiąc → ZUS/US co miesiąc → roczne (PIT-11, IMIR, ZFŚS, PFRON) → zmiany (aneksy, awanse) → zakończenie (wypowiedzenie, świadectwo, ZWUA, ekwiwalent).",
            "Przy każdym etapie dopisz: dokument, termin ustawowy, kto odpowiada (kadry / płace / kierownik / pracownik), narzędzie w kursie (Warsztat → eZUS/Płatnik, e-Urząd: PIT, Lista płac…) i jego odpowiednik w prawdziwej firmie (Płatnik, e-Deklaracje, program kadrowy). Np. zgłoszenie ZUS ZUA — 7 dni od zatrudnienia — kadry — Warsztat → eZUS/Płatnik (w firmie: Płatnik).",
            "Pogrubieniem zaznacz 10 terminów, których przekroczenie grozi karą lub odsetkami: ZUA 7 dni, DRA do 15./20., PIT-4R do 31.01, PIT-11 do 31.01 (US) i 28.02 (pracownik), ZFŚS 31.05/30.09, PFRON do 20., świadectwo w dniu ustania, ekwiwalent w terminie wypłaty, badania okresowe przed upływem ważności, informacja o warunkach zatrudnienia 7 dni. Sprawdź każdy w Warsztat → Przepisy.",
            "Poproś Asystenta o recenzję mapy: „Przejrzyj @mapa_procesow.md jak doświadczony kadrowiec: czego brakuje, co jest w złej kolejności, które terminy są błędne”. Każdą uwagę zweryfikuj w bibliotece przepisów, zanim ją przyjmiesz.",
            "Sobota: quiz z tygodnia 0 i checklista „Po tygodniu 0”.",
        ],
        "sprawdz": "Mapa ma ≥ 12 etapów z dokumentem, terminem, odpowiedzialnym i narzędziem; 10 terminów krytycznych wyróżnionych.",
    },
    # ============================================================ TYDZIEŃ 1
    "k1z4": {
        "kroki": [
            "Checklista PRZED pierwszym dniem: skierowanie na wstępne badania lekarskie (czynniki szkodliwe ze stanowiska — hałas, praca zmianowa/nocna, dźwiganie), orzeczenie bez przeciwwskazań PRZED dopuszczeniem; umowa podpisana; kwestionariusz osobowy pracownika (art. 22¹ §3: PESEL, adres, dane do ZUS, osoba do kontaktu, wykształcenie i przebieg zatrudnienia do stażu); oświadczenia: PIT-2, KUP podwyższone (dojazd), PPK (rezygnacja albo nic = autozapis 18–55 lat), konto bankowe, informacja RODO.",
            "Dzień pierwszy: szkolenie BHP wstępne — instruktaż ogólny (służba BHP) i stanowiskowy (kierownik), karta szkolenia do akt B; zapoznanie z regulaminem pracy, oceną ryzyka, informacją o monitoringu; oświadczenie o zapoznaniu się.",
            "Do 7 dni: ZUS ZUA (kod 01 10 + 5. i 6. znak). Zrób to w Warsztat → eZUS / Płatnik → „Dokument zgłoszeniowy”: osoba Anna Kowalczyk, typ ZUA, kod 011000, data 2026-10-01 → „Weryfikuj” → „Wyślij”. Zobacz, jak zmienił się jej status w „Ubezpieczeni” i jaki numer UPP dostałeś. Spróbuj też celowo złego kodu (np. 011009) i ZZA zamiast ZUA — przeczytaj komunikaty błędów.",
            "Do 7 dni od wniosku: ZCNA dla członka rodziny (w Warsztacie: typ ZCNA, PESEL dziecka — wygeneruj poprawny: Warsztat weryfikuje sumę kontrolną). Do 7 dni: informacja art. 29 §3. Do 3 miesięcy: umowa o prowadzenie PPK (do 10. dnia miesiąca po upływie 3 miesięcy).",
            "W onboarding_checklista.md zbuduj tabelę: dokument | termin | kto | gdzie trafia (akta A/B/C) | podstawa prawna (z Warsztat → Przepisy). Minimum 15 wierszy. Wykonaj onboarding „na sucho” dla Anny Kowalczyk: kwestionariusz, skierowanie, karta BHP jako pliki .md w 01-zatrudnienie.",
        ],
        "sprawdz": "Checklista ≥ 15 pozycji; ZUA Anny Kowalczyk przyjęte w symulatorze (status „zgłoszony od 2026-10-01”); komplet dokumentów w 01-zatrudnienie.",
    },
    # ============================================================ TYDZIEŃ 2
    "k2z1": {
        "pliki": ["wymiar_czasu_pracy.md"],
        "kroki": [
            "Lekcja „Czas pracy: normy, systemy, okresy rozliczeniowe”. Algorytm art. 130 KP: (pełne tygodnie × 40 h) + (dni od poniedziałku do piątku pozostałe × 8 h) − (8 h za każde święto w dniu innym niż niedziela). Święto w sobotę OBNIŻA wymiar (dajesz inny dzień wolny).",
            "Policz RĘCZNIE (kartka) wymiar dla 3 miesięcy 2026: styczeń, sierpień (15.08 w sobotę!), grudzień (24, 25.12 w czwartek i piątek, 26.12 w sobotę). Zapisz obliczenia w wymiar_czasu_pracy.md.",
            "Warsztat → Czas pracy → wpisz rok 2026, miesiąc 1 → „Policz”: pod spodem jest tabela całego roku. Porównaj ze swoimi 3 wynikami; każdą różnicę wyjaśnij (zwykle: sobotnie święto albo liczba dni pon–pt). Przepisz tabelę roku 2026 do pliku. Zmień rok na 2027 i zapisz drugą tabelę.",
            "Okresy 3-miesięczne produkcji (I–III, IV–VI, VII–IX, X–XII 2026): zsumuj miesiące. Dla 1/2 etatu — połowa; dla orzeczenia umiarkowanego (Ewa Sobczak) norma 7 h/35 h — policz osobną kolumnę dla listopada (wymiar × 7/8).",
            "Dopisz, które miesiące 2026 i 2027 mają święto w sobotę i jaki dzień wolny byś wyznaczył w firmie produkcyjnej.",
        ],
        "sprawdz": "Styczeń 2026 = 160 h (20 dni), sierpień 2026 = 160 h (21 dni roboczych − 8 h za 15.08 w sobotę), grudzień 2026 = 160 h (20 dni); rok 2026 = 2008 h / 251 dni; obie tabele w pliku.",
        "problemy": ["Pomijasz sobotnie święto → wymiar za wysoki o 8 h i pracownikowi należy się dzień wolny albo nadgodziny."],
    },
    "k2z4": {
        "pliki": ["ewidencja_czasu_pracy.md"],
        "kroki": [
            "Lekcja „Ewidencja czasu pracy i nieobecności”. W ewidencja_czasu_pracy.md zbuduj tabelę Markdown (jeden wiersz = dzień) z kolumnami: data | od | do | godziny | nadgodziny | nocne | nd/święto | dyżur | dzień wolny (W5 / WN / WŚ / wolne za nadgodziny) | nieobecność (UW, CH, OP, SW, UO…) | uwagi (polecenie nr, wniosek).",
            "Wypełnij dla operatora Marka Zielińskiego za grudzień 2026 z grafiku z zadania 2 (z 1 dniem urlopu, 2 dniami L4 i 4 nadgodzinami). Suma godzin ma się zgodzić z wymiarem z Warsztat → Czas pracy (160 h) po uwzględnieniu nieobecności.",
            "Dla pracownika zadaniowego i kierownika wyodrębnionej komórki: nie ewidencjonujesz godzin (art. 149 §2), ale nieobecności i dni wolne — dodaj drugą, uproszczoną tabelę.",
            "Dokumenty towarzyszące: wnioski o czas wolny za nadgodziny, zgody opiekuna dziecka do 8 lat, wnioski o wyjścia prywatne (odpracowanie nie jest nadgodziną), polecenia nadgodzin, harmonogramy. Okres przechowywania — jak akta (10 lat po ustaniu). Wypisz je pod tabelą.",
            "Praca zdalna: ewidencja nadal obowiązuje, okazjonalna 24 dni/rok — osobna kolumna. Opcjonalnie: jeśli masz arkusz kalkulacyjny, możesz przenieść tabelę tam — kurs tego nie wymaga.",
        ],
        "sprawdz": "Tabela ma wszystkie elementy §6 rozporządzenia; grudzień wypełniony spójnie z grafikiem i wymiarem 160 h; wersja dla zadaniowego.",
    },
    "k2z5": {
        "pliki": ["audyt_czasu_pracy.md"],
        "kroki": [
            "Z grafiku z zadania 2 wypisz w audyt_czasu_pracy.md rzeczywiste czasy pracy 4 operatorów za X–XII 2026 + zdarzenia: 1 osoba chorowała 10 dni, 1 miała 8 dni urlopu, 1 została wezwana 2× w dzień wolny (8 h), 1 pracowała 30 h nocnych więcej niż planowano.",
            "Warsztat → Czas pracy: wymiar okresu X–XII 2026 (suma trzech miesięcy). Dla każdego operatora: wymiar pomniejszony o nieobecności (urlop i choroba obniżają wymiar o godziny z planu), godziny przepracowane, nadgodziny dobowe (miesięcznie) i średniotygodniowe (po okresie), dni wolne udzielone/nieudzielone.",
            "Kwoty: Warsztat → Czas pracy → „Nadgodziny” (zasadnicze 5 400, wymiar DANEGO miesiąca, h50 / h100) i „Dodatek nocny” (30 h w listopadzie). Przepisz wyniki z kroków do raportu; stawka godzinowa = zasadnicze / wymiar miesiąca.",
            "Znajdź naruszenia: czy ktoś przekroczył 48 h średnio, czy odpoczynek 35 h był zachowany w tygodniu wezwania, czy niedziela wolna raz na 4 tygodnie. Opisz z artykułami KP (Warsztat → Przepisy: „odpoczynek”, „150 h”) i propozycją naprawy.",
            "Raport 1 strona dla zarządu: tabela (osoba | wymiar | przepracowane | nadgodziny 50% | 100% | nocne h | koszt dodatków) + 3 rekomendacje. Asystent: „Oceń @audyt_czasu_pracy.md jak inspektor PIP”. Sobota: quiz 2, checklista.",
        ],
        "sprawdz": "4 rozliczenia z kwotami policzonymi w Warsztacie, wykryte ≥ 2 naruszenia z artykułami, raport z rekomendacjami; sumy zgodne z ewidencją.",
    },
    # ============================================================ TYDZIEŃ 3
    "k3z2": {
        "kroki": [
            "Lekcja „Staż pracy 2026: zlecenia i działalność”. Zapisz: od 1.01.2026 sektor publiczny, od 1.05.2026 prywatny; zaliczane: zlecenia z ubezpieczeniem emerytalno-rentowym, działalność z opłaconymi składkami (także ulga na start), współpraca, zasiłki z tych tytułów, praca za granicą w innych formach; NIE: dzieło, praktyki, wolontariat, działalność nierejestrowana; nakładające się okresy — jeden.",
            "Dokument: zaświadczenie ZUS o okresach ubezpieczenia — pracownik składa wniosek w eZUS (elektronicznie, bez załączników); gdy ZUS nie ma danych — postępowanie wyjaśniające z dowodami (umowy, faktury). Student na zleceniu bez ubezpieczenia — umowa od zleceniodawcy. W kursie przyjmij, że zaświadczenie dostarczył pracownik (wzór treści: okres od–do, tytuł 04 11, płatnik).",
            "Termin dla już zatrudnionych: 24 miesiące od 1.01/1.05.2026; uprawnienia od dnia nabycia, nie wcześniej niż od wejścia przepisów. Okres wypowiedzenia — tylko zlecenia u TEGO SAMEGO pracodawcy.",
            "Kazus: Halina Mazur (umowy o pracę od 2009 = 17 lat → już 26 dni) — zamień na Katarzynę Wójcik: staż z umów o pracę 7 lat (2019–2026, w tym poprzedni pracodawca) + zaświadczenie ZUS o 3 latach zlecenia (2015–2018) dostarczone 1.06.2026 → 10 lat → 26 dni. Warsztat → Urlopy: staż 10, etat 1 → 26 dni; w 2026 wykorzystała 12 z 20 → urlop uzupełniający 6 dni od 1.06. Okres wypowiedzenia u Ciebie bez zmian (zlecenie u innego podmiotu).",
            "Napisz procedurę 1 strona w staz_pracy_procedura.md: komunikat dla pracowników, wzór wniosku do kadr, kto przelicza, gdzie wpiąć zaświadczenie (akta B), aktualizacja stażu w kartotece.",
        ],
        "sprawdz": "Procedura z datami 1.01/1.05.2026 i 24 miesiącami; kazus policzony w Warsztacie (26 dni, uzupełniający 6); lista „zaliczane / niezaliczane”.",
    },

    # ============================================================ TYDZIEŃ 4
    "k4z2": {
        "tytul": "Lista płac dla 8 pracowników w Warsztacie — każdy wiersz najpierw ręcznie",
        "opis": "Warsztat → Lista płac: 8 osób z firmy, każda najpierw policzona na kartce, potem sprawdzona w „Trybie ćwiczenia” i dodana do listy miesiąca.",
        "pliki": ["lista_plac_2026-11.md", "lista_plac_2026-11.csv", "lista_plac_notatki.md"],
        "kroki": [
            "Warsztat → Lista płac. Z listy „Osoba” wybierz Annę Kowalczyk — pola (zasadnicze, KUP, PIT-2, PPK, ulga) wypełnią się z kartoteki firmy. Miesiąc: 2026-11. NIE klikaj „Policz”. Policz na kartce w kolejności: 3 składki osobno (zaokrąglenie do grosza) → suma → podstawa zdrowotnej → zdrowotna 9% → PPK pracodawcy 1,5% (przychód) → podstawa PIT = brutto + PPK pracodawcy − składki − KUP, do pełnych zł → 12% − 300 → zaokrąglenie → PPK pracownika 2% → netto.",
            "Wpisz swój wynik w polu „Tryb ćwiczenia — moje netto” → „Sprawdź”. Jeśli się nie zgadza, Warsztat powie, która kwota odpowiada różnicy (np. „PPK pracownika”) — popraw i sprawdź ponownie. Gdy się zgadza, kliknij „Policz” i porównaj swoje kroki z 14 krokami Warsztatu. Zapisz w lista_plac_notatki.md, na którym kroku się pomyliłeś.",
            "Powtórz dla pozostałych 7 pracowników. Specjalne przypadki: Tomasz Lis (14 000) — w polu „Dochód narastająco” wpisz 118 306 (dochód I–X) i zobacz zaliczkę z 32% od nadwyżki; Jakub Krawczyk — ulga dla młodych (zaliczka 0, składki normalnie); Piotr Nowak (1/2 etatu, 2 500, PIT-2 u drugiego pracodawcy) — zobacz, czy zdrowotna nie została obniżona do hipotetycznej zaliczki; Halina Mazur — KUP 300 i bez PPK.",
            "Po każdym „Policz” kliknij „Dodaj do listy miesiąca”. Na koniec „Pokaż listę miesiąca” — sprawdź bilans: suma brutto = suma netto + składki pracownika + zdrowotna + zaliczki + PPK pracownika. „Zapisz listę (MD + CSV)” → pliki w 04-place.",
            "Koszt pracodawcy: w liście jest kolumna „Koszt”. Zapisz w notatkach sumę za miesiąc — to kwota, którą zobaczy zarząd — i sprawdź, że dla Katarzyny Wójcik (4 806 zł, z PPK) koszt = 4 806 + składki pracodawcy (wypadkowa firmy 1,20%!) + 72,09 PPK.",
        ],
        "sprawdz": "8 wierszy w liście 2026-11 (każdy najpierw sprawdzony w Trybie ćwiczenia); lista_plac_2026-11.md i .csv w 04-place; notatki z błędami; zaliczka Tomasza Lisa liczona 12%/32%.",
        "problemy": ["PPK pracodawcy pomniejsza netto → nie; tylko zwiększa podstawę PIT (podatek od niej zmniejsza netto).",
                     "Próg liczysz od brutto → od dochodu (brutto − składki społeczne − KUP) narastająco — pole „Dochód narastająco”.",
                     "„Sprawdź” mówi, że różnica to kwota zdrowotnej → policzyłeś zdrowotną od brutto zamiast od (brutto − składki)."],
    },
    "k4z3": {
        "kroki": [
            "Lekcja „Zaliczka na PIT: PIT-2, KUP, ulgi”. Z lekcji i Warsztat → Przepisy („PIT-2”) wypisz treść oświadczeń PIT-2: kwota zmniejszająca 1/12 (300 zł), 1/24 (150 — dwóch płatników), 1/36 (100); podwyższone KUP 300 zł; ulga dla młodych (wniosek o NIEstosowanie), ulga na powrót, dla rodzin 4+, dla pracujących seniorów (do 85 528 zł); rezygnacja z KUP; wniosek o niepobieranie zaliczek (dochód do 30 000 zł); wspólne rozliczenie z małżonkiem.",
            "Tabela w oswiadczenia_pit.md: oświadczenie | kiedy pracownik składa | od kiedy stosujesz (najpóźniej od następnego miesiąca) | wpływ na listę | do kiedy obowiązuje (do odwołania). Po ustaniu zatrudnienia przy wypłatach pomijasz oświadczenia (bez 300 zł, bez KUP 300) — poza wnioskami o niestosowanie KUP/ulgi dla młodych (art. 31a ust. 7 PIT).",
            "Sprawdź każdy wpływ w Warsztat → Lista płac na przykładzie 6 000 zł: (a) PIT-2 300 vs 0; (b) KUP 250 vs 300; (c) ulga dla młodych zaznaczona; (d) PIT-2 150. Zapisz cztery wartości netto i różnice.",
            "Kazus 1: Tomasz Lis składa w lipcu wniosek o 32% — od sierpnia 32%; w Warsztacie zasymuluj listopad z „Dochód narastająco” 118 306. Kazus 2: pracownica wraca z Niemiec — ulga na powrót (4 lata, do 85 528 zł) — jak udokumentować. Kazus 3: emeryt 66 lat pracujący bez pobierania emerytury — ulga dla seniorów; zdrowotna liczona normalnie z ograniczeniem do hipotetycznej zaliczki (Warsztat pokazuje to w krokach).",
            "Przygotuj kartotekę podatkową pracownika (1 strona): zastosowane oświadczenia z datami, KUP, próg, narastające przychody — tak, by w styczniu dało się z niej zrobić PIT-11 (w tygodniu 9 zrobi to Warsztat → e-Urząd: PIT z Twojej listy płac).",
        ],
        "sprawdz": "Tabela ≥ 8 oświadczeń; 4 warianty netto z Warsztatu; 3 kazusy z rozwiązaniem; kartoteka podatkowa pracownika.",
    },
    "k4z5": {
        "pliki": ["lista_plac_2026-11.md", "paski_11_2026.md", "przelewy_11_2026.csv", "zestawienie_11_2026.md"],
        "kroki": [
            "Warsztat → Lista płac → „Wyczyść listę miesiąca” dla 2026-11 i policz ją od nowa z listopadowymi składnikami: w polu „Nadgodziny/premie/nocne” wpisz dla operatorów nadgodziny i dodatek nocny z audytu czasu pracy (tydzień 2, Warsztat → Czas pracy), premię regulaminową 10% dla 3 osób. Każdą osobę — najpierw na kartce, potem „Sprawdź”, „Policz”, „Dodaj do listy miesiąca”.",
            "„Pokaż listę miesiąca” → „Zapisz listę (MD + CSV)”. Z pliku .md zrób w paski_11_2026.md pasek dla każdej osoby (składniki brutto → składki → podatek → PPK → potrącenia → netto → dni/godz. przepracowane, urlop wykorzystany/pozostały). Pasek nie jest obowiązkowy, ale na żądanie pracownika udostępniasz dokumenty, z których policzono wynagrodzenie (art. 85 §5).",
            "Plik przelewów przelewy_11_2026.csv (nazwisko; konto — wymyślone 26 cyfr; kwota netto; tytuł „Wynagrodzenie 11/2026”) z datą 10.12.2026 — termin stały, z dołu, nie później niż 10. dnia następnego miesiąca (art. 85); gdy 10. to dzień wolny — dzień wcześniej.",
            "Zestawienie dla księgowości (zestawienie_11_2026.md) z wiersza RAZEM listy: suma brutto, składki pracownika, składki pracodawcy wg funduszy (z kolumn kosztów w CSV), zaliczka PIT (do US do 20 grudnia), PPK (do instytucji do 15 grudnia), zdrowotna — to kwoty, które w tygodniu 8 zobaczysz w DRA. Zgodność: netto + składki pracownika + zdrowotna + zaliczka + PPK pracownika = brutto.",
            "Asystent: „Oto moja lista płac (wklej 2 wiersze). Zadaj mi 5 pytań kontrolnych, które zadałby audytor.” Odpowiedz w notatkach. Sobota: quiz 4.",
        ],
        "sprawdz": "Lista 2026-11 w Warsztacie z listopadowymi składnikami i bilansem; paski 8 osób; CSV przelewów; zestawienie z terminami US/ZUS/PPK.",
    },
    # ============================================================ TYDZIEŃ 6
    "k6z1": {
        "kroki": [
            "Lekcja „Wynagrodzenie chorobowe i zasiłek”. Zasady: pracodawca płaci wynagrodzenie chorobowe (art. 92 KP) za pierwsze 33 dni w roku kalendarzowym (14 — po 50. roku życia, od roku następnego po urodzinach), 80% (100%: ciąża, wypadek w drodze, dawca); od 34./15. dnia — zasiłek chorobowy (80%; szpital 80% od 2022). Stan na XI 2026: reforma „ZUS od 1. dnia” NIE weszła w życie.",
            "Liczenie dni: za każdy dzień kalendarzowy; stawka dzienna = podstawa / 30. Okres wyczekiwania 30 dni ubezpieczenia — nowo zatrudniony od 14.12 chory 20.12 → brak prawa (chyba że 10 lat ubezpieczenia lub ciągłość do 30 dni od poprzedniego tytułu).",
            "Kazus 1 (Marek Zieliński, 38 lat, 5 400 zł; podstawa po składkach 5 400 × 0,8629 = 4 659,66; stawka dzienna 155,32): L4 1–12.03, 5–24.06, 10–25.10. Najpierw na kartce: które dni to wynagrodzenie chorobowe (pula 33), od którego dnia zasiłek, kwoty. Potem Warsztat → Zasiłki i chorobowe → B: wpisz 3 nieobecności (rodzaj „choroba”), stawkę dzienną 155,32 → sprawdź dzień przejścia na zasiłek i kwoty.",
            "Kazus 2 (Halina Mazur, 54 lata): zaznacz „pracownik 50+” — 14 dni, potem zasiłek. Kazus 3: choroba na przełomie roku (28.12–10.01) — nieprzerwana niezdolność z grudnia → zasiłek dalej bez nowych 33 dni; dodaj ją w Warsztacie i zobacz pulę.",
            "Okres zasiłkowy 182 dni (270 ciąża/gruźlica); przerwa < 60 dni wlicza się; po 182 — świadczenie rehabilitacyjne (wniosek ZNp-7 6 tygodni przed końcem). Dodaj w Warsztacie chorobę 1.07–31.12 i zobacz ostrzeżenie o przekroczeniu 182 dni. Zapisz wszystko w chorobowe.md („Zapisz do projektu”).",
        ],
        "sprawdz": "Kazus 1: dzień przejścia na zasiłek i kwoty zgodne z Warsztatem; kazus 2 i 3 rozwiązane; ostrzeżenie o 182 dniach uzyskane; chorobowe.md zapisany.",
        "problemy": ["Liczysz 33 dni robocze → kalendarzowe.", "50-latek w roku 50. urodzin ma 14 dni → dopiero od następnego roku."],
    },
    "k6z2": {
        "pliki": ["podstawa_zasilku.md"],
        "kroki": [
            "Lekcja „Podstawa wymiaru zasiłku”. Podstawa = przeciętne miesięczne wynagrodzenie (podstawa składki chorobowej po odjęciu 13,71%) z 12 miesięcy przed miesiącem zachorowania (krócej — z pełnych miesięcy). Nie wchodzą składniki, do których pracownik zachowuje prawo w okresie choroby (w firmie: dodatek stażowy); wchodzą: nadgodziny, nocne, premia regulaminowa pomniejszana za chorobę. Kwartalne — 1/12 z 4 kwartałów; roczne — 1/12.",
            "Miesiąc niepełny z przyczyn usprawiedliwionych: uzupełnienie — stałe w pełnej wysokości, zmienne (wypłacone / dni przepracowane) × dni obowiązujące; miesiąc z < 50% dni — wyłączasz.",
            "Warsztat → Zasiłki i chorobowe → A: wypełnij 12 miesięcy XII 2025–XI 2026 dla Marka Zielińskiego (stałe 5 400; zmienne: nadgodziny + nocne + premia 10%, np. 300–700 zł; dni obowiązujące z Warsztat → Czas pracy): w marcu chorował 12 dni (wpisz dni przepracowane mniejsze — Warsztat uzupełni), w lipcu urlop bezpłatny 20 dni (< 50% — wyłączy), od 1.09 podwyżka do 5 700 (zmiana wynagrodzenia nie przerywa podstawy; zmiana ETATU — tak).",
            "Zanim klikniesz „Policz podstawę”, policz na kartce średnią z uwzględnionych miesięcy i stawkę dzienną. Potem porównaj z krokami Warsztatu: które miesiące uzupełnił, który wyłączył, ile wyszło. Dni niezdolności 10, 80% → kwota za 10 dni grudnia.",
            "Minimalna podstawa: 4 806 × 0,8629 = 4 147,10 (proporcjonalnie do etatu) — sprawdź, wpisując etat 0,5 i niskie kwoty. Zasada ciągłości: nowej podstawy nie ustala się, gdy przerwa między zasiłkami była krótsza niż miesiąc kalendarzowy (art. 43, od 2022). Zapisz wynik („Zapisz do projektu” → podstawa_zasilku.md).",
            "Asystent: „Sprawdź, które składniki z regulaminu firmy ćwiczeniowej wchodzą do podstawy — zadaj mi pytania o treść regulaminu premiowania”.",
        ],
        "sprawdz": "12 miesięcy w Warsztacie z uzupełnieniem marca i wyłączeniem lipca; podstawa i zasiłek za 10 dni zgodne z rachunkiem ręcznym; zasada miesiąca przerwy; plik zapisany.",
        "problemy": ["Premia „zachowywana w chorobie” w podstawie → podwójne świadczenie; wyłącz (w firmie: dodatek stażowy)."],
    },
    "k6z3": {
        "tytul": "e-ZLA, Z-3, wypłata zasiłku przez płatnika, RSA i kody — w symulatorze",
        "kroki": [
            "Lekcja „Zasiłki w dokumentach ZUS”. e-ZLA: lekarz wystawia, pracodawca widzi w eZUS (profil płatnika) — pracownik nie dostarcza papieru; obowiązek pracownika: poinformować o nieobecności (regulamin: do 2. dnia). Kody: A — ta sama choroba do 60 dni, B — ciąża, C — alkohol (5 dni bez zasiłku), D — gruźlica, E — po ustaniu.",
            "Warsztat → eZUS / Płatnik → zakładka „e-ZLA”: w skrzynce są zwolnienia pracowników firmy. Dla każdego ustal: dni, kod, kto płaci (firma zgłasza > 20 ubezpieczonych → SAMA wypłaca zasiłki i rozlicza w DRA), czy to wynagrodzenie chorobowe (331) czy zasiłek (313/312/314) — użyj puli 33/14 z narzędzia Zasiłki. Pobierz każde do RSA właściwym kodem (dla zasiłków wpisz kwotę z Warsztat → Zasiłki).",
            "Z-3 składa się tylko, gdy zasiłek wypłaca ZUS (płatnik ≤ 20 ubezpieczonych; po ustaniu zatrudnienia; świadczenie rehabilitacyjne). W z3_procedura.md wypełnij treść Z-3 jako tabelę dla osoby, która choruje od 5.01.2027 po rozwiązaniu umowy 31.12.2026 (zasiłek po ustaniu tytułu: niezdolność do 14 dni po ustaniu, trwająca ≥ 30 dni): 12 miesięcy przychodu z Twojej listy płac, składniki, okresy nieobecności, liczba ubezpieczonych.",
            "Warsztat → eZUS / Płatnik → „Rozliczenie DRA/RCA/RSA”: dla miesiąca z e-ZLA zobacz RSA i jak zasiłki pomniejszają kwotę do zapłaty w DRA. Terminy: płatnik wypłaca zasiłek w terminie wypłaty wynagrodzeń; ZUS — 30 dni od dokumentów.",
            "Napisz procedurę 1 strona „Pracownik na L4” od powiadomienia po RSA, z terminami, kodami i osobami.",
        ],
        "sprawdz": "Wszystkie e-ZLA ze skrzynki pobrane do RSA z właściwym kodem i kwotą; Z-3 wypełniony kompletnie; procedura rozróżnia płatnik/ZUS.",
        "problemy": ["Wystawiasz Z-3 mimo > 20 ubezpieczonych → nie; sam wypłacasz. Wyjątek: po ustaniu zatrudnienia i świadczenie rehabilitacyjne (orzeka ZUS)."],
    },
    "k6z4": {
        "kroki": [
            "Lekcja „Kontrola L4 po 13 kwietnia 2026”. Ustawa z 18.12.2025 (Dz.U. 2026 poz. 26): płatnik uprawniony do wypłaty zasiłków (> 20 ubezpieczonych) kontroluje prawidłowość wykorzystywania zwolnień; utrata zasiłku: praca zarobkowa (poza incydentalnymi czynnościami wymuszonymi okolicznościami) albo aktywność niezgodna z celem (utrudniająca/wydłużająca leczenie; czynności dnia codziennego dozwolone). Kontroler: imienne upoważnienie, protokół, 3 dni na uwagi, spory → ZUS.",
            "Napisz procedurę kontroli w kontrola_l4.md: kto (2 osoby z upoważnieniem), kiedy (częste krótkie L4, L4 po odmowie urlopu, „okołoświąteczne”), jak (wizyta, protokół — szablon w zakładce Prompty: „Protokół kontroli…”), skutek (wstrzymanie, decyzja ZUS), ochrona danych.",
            "Zasiłek opiekuńczy: 80%; dziecko do 14 lat — 60 dni/rok (do 8 lat także zamknięcie żłobka/szkoły, choroba niani); 14+ i inny członek rodziny — 14 dni; łącznie max 60; brak innego domownika (poza dzieckiem do 2 lat); dokumenty Z-15A/Z-15B. Kazus: Katarzyna Wójcik (dziecko 5 lat) — opieka 10 dni + 5 dni na dziecko męża (9 lat): Warsztat → Zasiłki → B: dwie nieobecności rodzaju „opieka” ze stawką dzienną z podstawy 4 147,10 (minimalna) → kwoty.",
            "Zasiłek macierzyński: 100% / 70% / 81,5%, podstawa jak chorobowy, bez wyczekiwania, płatnik wypłaca; dokumenty: wniosek, akt urodzenia, oświadczenia. Świadczenie rehabilitacyjne: po 182 dniach, orzeczenie lekarza orzecznika, 90% przez 3 mies., 75% dalej, 100% ciąża — orzeka ZUS, wypłaca płatnik zasiłków.",
            "Treść Z-15A dla kazusu opiekuńczego wypisz jako tabelę pól w zasilki_inne.md (dane dziecka, okres, oświadczenie o braku innego opiekuna); zapisz różnice dokumentów opieka/choroba/macierzyństwo. Skrzynka e-ZLA w Warsztacie ma zwolnienie na opiekę Katarzyny Wójcik — pobierz je do RSA kodem 312 z kwotą.",
        ],
        "sprawdz": "Procedura kontroli zgodna z ustawą z 18.12.2025; kazus opiekuńczy policzony w Warsztacie (15 dni × 80% stawki); Z-15A jako tabela; e-ZLA opieki w RSA.",
    },
    # ============================================================ TYDZIEŃ 7
    "k7z2": {
        "kroki": [
            "Dzieło: rezultat (utwór, projekt, naprawa), odpowiedzialność za wynik, brak ZUS (chyba że z własnym pracodawcą — pełne składki jak etat), zgłoszenie ZUS RUD w 7 dni od zawarcia (nie dotyczy dzieła z własnym pracownikiem), KUP 20% lub 50% (prawa autorskie, limit 120 000 zł rocznie), podatek 12%.",
            "Oceń 4 sytuacje w dzielo_b2b.md: (a) Joanna Michalska projektuje etykietę mleka — dzieło OK; (b) „dzieło”: comiesięczne sprzątanie hali — zlecenie (czynności, nie rezultat) — ZUS przekwalifikuje; (c) kierowca na B2B jeżdżący firmowym autem wg grafiku brygadzisty — stosunek pracy (art. 22 §1¹) — składki 5 lat wstecz + odsetki; (d) były pracownik na B2B świadczy te same usługi — utrata podatku liniowego w roku rozpoczęcia (art. 9a ust. 3 PIT). Napisz 5-punktowy test „etat czy nie”.",
            "Rachunek do dzieła 4 000 zł z KUP 50%: podstawa 2 000 → podatek 240 → netto 3 760. Z KUP 20%: 3 200 → 384 → 3 616. Policz na kartce, potem sprawdź: Warsztat → Lista płac nie liczy dzieł (to nie etat) — więc zapisz rachunek ręcznie w pliku jako tabelę: wynagrodzenie | KUP | podstawa | zaliczka | netto.",
            "RUD: w Warsztacie dzieło nie jest zgłaszane do ubezpieczeń (zobacz status Joanny Michalskiej w „Ubezpieczeni”: „nie podlega — RUD”). Treść RUD wypisz jako tabelę pól: dane zamawiającego, wykonawcy, data zawarcia, data rozpoczęcia i zakończenia, przedmiot, liczba umów — termin 7 dni od 2.11.2026 → do 9.11.2026.",
            "B2B kontrakt: co zmniejsza ryzyko (swoboda czasu i miejsca, własne narzędzia, podwykonawca, ryzyko gospodarcze, wielu klientów), czego nie wolno (grafik, „udzielany” urlop, polecenia). Status projektu PIP (decyzja administracyjna o stosunku pracy) — projekt, nieuchwalony; dziś tylko sąd. Asystent: „Oceń @dzielo_b2b.md jak inspektor ZUS — które umowy zakwestionujesz i na jakiej podstawie?”",
        ],
        "sprawdz": "4 sytuacje ocenione z podstawą; rachunek 3 760 / 3 616; treść RUD z terminem 9.11.2026; test „etat czy nie”.",
    },
    "k7z3": {
        "pliki": ["ppk_procedura.md", "ppk_naliczenie.md"],
        "kroki": [
            "Lekcja „PPK”. Nowy pracownik: umowa o prowadzenie po 3 miesiącach zatrudnienia — do 10. dnia miesiąca po 3. miesiącu (Anna Kowalczyk od 1.10.2026 → 90 dni mija 29.12 → termin do 10.01.2027); 18–55 lat automatycznie, 55–70 na wniosek, > 70 nie; deklaracja rezygnacji ważna do ponownego autozapisu (1.04.2027; informacja do końca lutego 2027).",
            "Wpłaty: pracownik 2% (0,5%, gdy wynagrodzenie ≤ 120% minimalnej = 5 767,20 zł), pracodawca 1,5%; powitalna 250 zł, roczna 240 zł (wpłaty ≥ 3,5% × 6 × minimalna); wpłata pracodawcy — przychód do PIT, bez ZUS; pracownika — z netto; przekazanie do 15. dnia następnego miesiąca.",
            "Naliczenie w Warsztat → Lista płac (miesiąc 2026-12) dla 4 wariantów: Anna Kowalczyk (jeszcze bez PPK: oba pola 0%), Halina Mazur (54 lata, bez PPK — rezygnacja), Katarzyna Wójcik (4 806 zł — obniżona 0,5% / 1,5%), Marek Zieliński (5 400 zł — 2% / 1,5%). Dla każdego zapisz w ppk_naliczenie.md: wpłata pracownika, pracodawcy, o ile wzrosła zaliczka, o ile spadło netto; kolumna „do przekazania do 15.01.2027”.",
            "Sankcje: brak umowy o zarządzanie — do 1,5% funduszu wynagrodzeń; nakłanianie do rezygnacji — j.w.; brak wpłat — 1 000–1 000 000 zł. Do akt B: deklaracje, wnioski; informacja o PPK dla nowo zatrudnionych.",
            "Procedura 1 strona + kalendarz PPK 2027 (autozapis: do 28.02 informacja, 1–31.03 ponowne deklaracje rezygnacji, od 1.04 wpłaty; nowi — terminy umów; miesięczne — 15.).",
        ],
        "sprawdz": "Termin umowy dla Anny Kowalczyk (10.01.2027) wyznaczony; naliczenie 4 wariantów z Warsztatu; kalendarz autozapisu 2027.",
    },
    "k7z4": {
        "kroki": [
            "Lekcja „Cudzoziemcy i B2B” (część o cudzoziemcach). Ścieżki: obywatel UE — jak Polak; Ukraina (status UKR): powiadomienie PUP w 14 dni (w prawdziwym życiu: praca.gov.pl — w kursie wypisujesz treść powiadomienia jako tabelę pól), bez zezwolenia; inni: oświadczenie o powierzeniu pracy (5 krajów, do 24 mies.) lub zezwolenie typu A (wojewoda) / jednolite zezwolenie; ustawa z 20.03.2025 (od 1.06.2025): wnioski elektroniczne, nowe przesłanki odmowy. Zawsze: legalny pobyt + legalna praca; kopia dokumentu pobytowego w aktach.",
            "Umowa w języku zrozumiałym (tłumaczenie), zgłoszenie ZUS (PESEL lub paszport — Warsztat → eZUS/Płatnik: zgłoś nowego pracownika jako ZUA, wpisując PESEL wygenerowany z daty urodzenia), PIT: rezydencja (183 dni / centrum interesów) → PIT-11 lub IFT-1R (ryczałt 20% dla zleceń nierezydentów, art. 29 PIT, chyba że certyfikat rezydencji); PESEL do PIT-11.",
            "Checklista 15 punktów w cudzoziemcy.md dla operatora z Ukrainy: dokument pobytowy i ważność (przypomnienie w kalendarzu!), treść powiadomienia PUP, umowa, badania, BHP w zrozumiałym języku, ZUS, PESEL, konto, PPK (jak Polak), zmiana stanowiska/etatu = nowe powiadomienie w 14 dni.",
            "Delegowanie do Niemiec na 6 tygodni: A1 z ZUS (wniosek US-3 — treść jako tabela pól), informacja art. 29 §3 (państwo, czas, waluta, świadczenia), płaca minimalna państwa przyjmującego, diety zagraniczne wg rozporządzenia (Niemcy 49 EUR), zwolnienie z PIT i ZUS diet do limitu.",
            "Asystent: „Jakie kary grożą za nielegalne zatrudnienie cudzoziemca i kto je nakłada?” — zapisz z podstawą (ustawa z 20.03.2025: 3 000–50 000 zł; Straż Graniczna, PIP). Sprawdź w Warsztat → Przepisy („cudzoziemcy”).",
        ],
        "sprawdz": "Dwie ścieżki (UA / spoza UE) z dokumentami i terminami; ZUA cudzoziemca w symulatorze; rozliczenie PIT rezydent/nierezydent; A1 i diety.",
    },

    # ============================================================ TYDZIEŃ 8
    "k8z1": {
        "tytul": "Zgłoszenia w symulatorze eZUS/Płatnik: ZUA, ZZA, ZCNA, ZIUA, ZWUA dla całej firmy",
        "opis": "Komplet dokumentów zgłoszeniowych z właściwymi kodami — każdy zweryfikowany i wysłany w Warsztacie, z numerem UPP.",
        "kroki": [
            "Lekcja „Zgłoszenia do ZUS”. Kody tytułu: 01 10 pracownik (5. znak: 0 brak / 1 emerytura / 2 renta; 6. znak: niepełnosprawność 0–3); 04 11 zleceniobiorca; 05 10 przedsiębiorca; 12 11 urlop wychowawczy; 30 00 — rozliczenie po ustaniu. Pełna lista jest pod formularzem w Warsztacie.",
            "Warsztat → eZUS / Płatnik → „Dokument zgłoszeniowy”. Dla każdego z 8 pracowników: ZUA, kod 011000 (Ewa Sobczak: 011002 — umiarkowany stopień), data = pierwszy dzień pracy z karty firmy → „Weryfikuj” → „Wyślij”. Zwróć uwagę na ostrzeżenia „po terminie 7 dni” — w symulacji daty są historyczne, w pracy to byłaby grzywna.",
            "Zleceniobiorcy: Agnieszka Pawlak (etat gdzie indziej ≥ minimalnej) → ZZA, kod 041100 (tylko zdrowotne); Robert Król (bez innego tytułu) → ZUA 041100 z zaznaczonym dobrowolnym chorobowym; Michał Dąbrowski (student) → spróbuj ZUA 041100 i przeczytaj błąd — studenta nie zgłaszasz. Joanna Michalska (dzieło) — nie zgłaszasz; RUD opisałeś w tygodniu 7.",
            "ZCNA: dziecko Katarzyny Wójcik (wygeneruj poprawny PESEL dziecka urodzonego w 2021 — Warsztat sprawdza sumę kontrolną; kod pokrewieństwa 11). ZIUA: zmiana nazwiska Anny Kowalczyk. ZWUA: Anna Kowalczyk — umowa próbna kończy się 31.12.2026 → data 2027-01-01, kod 100, tryb 7 (upływ czasu) → Weryfikuj (ostrzeżenie o dacie, jeśli pomylisz dzień).",
            "Zakładka „Ubezpieczeni”: wszyscy, którzy podlegają, mają status „zgłoszony”; student i dzieło — „nie podlega”. „Rejestr wysłanych” → „Zapisz rejestr do projektu”. W zus_zgloszenia.md zrób tabelę: osoba | dokument | kod | data | termin 7 dni | UPP, oraz 5 komunikatów błędów/ostrzeżeń, które zobaczyłeś, i jak je usunąłeś. Dodaj skutki spóźnienia (grzywna do 5 000 zł, art. 98 ustawy systemowej; brak zgłoszenia pracownika — składki wstecz).",
        ],
        "sprawdz": "W „Ubezpieczeni” 10 osób zgłoszonych (8 pracowników + 2 zleceniobiorców), student i dzieło „nie podlega”; ZCNA, ZIUA i ZWUA przyjęte; rejestr_zus.md zapisany; tabela z UPP i 5 komunikatów.",
        "problemy": ["ZUA zleceniobiorcy z etatem u innego pracodawcy → ZZA (tylko zdrowotne), chyba że tam zarabia < minimalnej.",
                     "„Osoba jest już zgłoszona” → najpierw ZWUA (albo użyj innej osoby); w prawdziwym Płatniku byłaby to korekta ZUA."],
    },
    "k8z2": {
        "kroki": [
            "Lekcja „Rozliczenia miesięczne: DRA, RCA, RSA, RPA”. RCA — imienny raport składek; RSA — przerwy i świadczenia (331, 313, 312, 327/319/325, 111, 121, 151, 152) z okresami i kwotami zasiłków; RPA — przychody za inne okresy (premia roczna za 2025 wypłacona w grudniu 2026); DRA — zbiorcza: składki wg funduszy, pomniejszenie o wypłacone zasiłki (płatnik > 20), kwota do zapłaty.",
            "Warsztat → Lista płac: upewnij się, że lista 2026-12 ma 8 pracowników (policz grudzień: pensje + dla Marka Zielińskiego wynagrodzenie chorobowe/zasiłek z tygodnia 6; Tomasz Lis z dochodem narastająco powyżej progu). Każdy wiersz „Dodaj do listy miesiąca”.",
            "Warsztat → eZUS / Płatnik → „Rozliczenie DRA/RCA/RSA”: miesiąc 2026-12, identyfikator 01 → „Pokaż komplet” — RCA powstało z Twojej listy. Dodaj RSA: choroba Marka Zielińskiego (331 za dni z wynagrodzeniem chorobowym, 313 za dni zasiłku z kwotą), urlop wychowawczy Ewy Sobczak od 1.12 (121) — i pobierz z e-ZLA zwolnienie z grudnia. „Weryfikuj” → przeczytaj błędy (np. RSA z innego miesiąca, osoba bez ZUA) → popraw → „Wyślij (symulacja)”.",
            "Porównaj DRA z zestawieniem dla księgowości z tygodnia 4/5: suma składek społecznych, zdrowotna, FP, FGŚP — co do grosza (różnice to zaokrąglenia per osoba). Terminy: 15.01.2027 (spółka z o.o.; 20. — płatnicy bez osobowości prawnej; 5. — budżet), jeden przelew na NRS; zasiłki pomniejszają przelew; PPK — nie w DRA.",
            "Odsetki za zwłokę (stopa odsetek podatkowych; nie nalicza się, gdy ≤ 1% minimalnej = 48,06 zł), opłata dodatkowa do 100%. „Zapisz do projektu” → zus_2026-12.md; w zus_dra_12_2026.md objaśnij każdy wiersz DRA własnymi słowami (skąd kwota).",
        ],
        "sprawdz": "Komplet 01 12 2026 wysłany bez błędów (UPP); kwota DRA zgodna z zestawieniem; RSA z 331/313/121; zus_2026-12.md zapisany; wiersze DRA objaśnione.",
        "problemy": ["Zasiłek chorobowy w RCA jako podstawa → nie; zasiłek idzie w RSA z kwotą, a RCA ma podstawę bez zasiłku (wynagrodzenie chorobowe — tylko w podstawie zdrowotnej).",
                     "„Komplet bez żadnego RCA” → lista płac tego miesiąca jest pusta; dodaj wiersze w narzędziu Lista płac."],
    },
    "k8z3": {
        "kroki": [
            "Lekcja „Korekty ZUS”. Scenariusz 1: e-ZLA wpłynęło po wysłaniu kompletu (zapłacone pełne wynagrodzenie za grudzień, a od 28.12 choroba): w Warsztacie policz Marka Zielińskiego od nowa z wynagrodzeniem chorobowym za 28–31.12 (Lista płac → ten sam miesiąc nadpisuje wiersz), dodaj RSA 331, a w „Rozliczenie” wybierz identyfikator 02 → Weryfikuj → Wyślij. Nadpłata składek — zwrot na wniosek RZS-P lub zaliczenie; nadpłacone wynagrodzenie — art. 87 §7 (odliczenie w najbliższym terminie) albo zgoda z art. 91.",
            "Scenariusz 2: błędny kod — Agnieszka Pawlak zgłoszona ZUA 041100 zamiast ZZA: w symulatorze wyślij ZWUA (data = data pierwotnego zgłoszenia, kod 600) i nowe ZZA; opisz korektę RCA za każdy miesiąc i rozliczenie nadpłaty społecznych (zdrowotna była prawidłowa).",
            "Scenariusz 3: niewykazana premia roczna (brak RPA): komplet 02 za grudzień z wyższą podstawą; niedopłata z odsetkami od 16.01 — policz odsetki dla 1 500 zł za 40 dni przy stopie odsetek za zwłokę (zapisz, skąd wziąłeś stopę — np. z lekcji/ściągi, albo przyjmij 14,5% i zaznacz, że to założenie).",
            "Scenariusz 4: przedawnienie — korekty możliwe 5 lat od terminu wymagalności (art. 24 i 48d ustawy systemowej); ZUS sam koryguje drobne błędy i wysyła zawiadomienie — masz 7 dni na reakcję. W Warsztacie spróbuj wysłać komplet 01 za miesiąc, za który już jest 01 — przeczytaj błąd.",
            "Procedura „korekta w 5 krokach” + rejestr korekt (data, okres, przyczyna, dokumenty, skutek kwotowy, kto zatwierdził). IMIR: roczna informacja dla ubezpieczonego do 28.02 — po korekcie wydajesz skorygowaną.",
        ],
        "sprawdz": "Komplet 02 12 2026 wysłany w symulatorze; ZWUA + ZZA dla Agnieszki Pawlak; 4 scenariusze z dokumentami i skutkiem kwotowym; odsetki policzone; rejestr korekt; przedawnienie 5 lat.",
        "problemy": ["Korekta tylko DRA bez RCA → ZUS odrzuci; zawsze komplet imienny + zbiorcza z tym samym identyfikatorem.",
                     "„Identyfikator 01 już użyty” → korekta to 02, 03…"],
    },
    "k8z4": {
        "tytul": "eZUS dla płatnika: panel, PEL, e-ZLA, zaświadczenia — na symulatorze i z opisu",
        "kroki": [
            "Warsztat → eZUS / Płatnik: pięć zakładek symulatora odpowiada panelowi płatnika w prawdziwym eZUS: „Ubezpieczeni” (lista z zakresem ubezpieczeń), „Dokument zgłoszeniowy” (ePłatnik/Płatnik), „Rozliczenie” (Płatnik + Płatność/NRS), „e-ZLA” (Zaświadczenia lekarskie), „Rejestr wysłanych” (Dokumenty i wiadomości). W ezus_przewodnik.md opisz każdą sekcję prawdziwego eZUS i jej odpowiednik w Warsztacie; dopisz sekcje, których symulator nie ma: Zaświadczenia (RWN — o niezaleganiu), Wnioski (interpretacja indywidualna, US-3 → A1, RD-3 — saldo), Płatność (NRS, saldo).",
            "Pełnomocnictwo PEL: kadrowa działa w imieniu spółki — formularz PEL (zakres: płatnik, wszystkie sprawy / wybrane), podpis zarządu; PEL-K do odwołania. Zapisz procedurę nadania/odwołania przy zmianie pracownika kadr (tego samego dnia!).",
            "e-ZLA: codzienny nawyk — Warsztat → e-ZLA: sprawdź skrzynkę, pobierz nowe do RSA, zanotuj kody. Zapisz, jak pracownik widzi e-ZLA po swojej stronie i co zrobić, gdy lekarz popełnił błąd (anulowanie i nowe e-ZLA).",
            "Zaświadczenia dla pracownika: ZUS ERP-7 (o zatrudnieniu i wynagrodzeniu do emerytury) — wypełnij jako tabelę dla Haliny Mazur za 2026 z danymi z Twoich list płac (podstawy wymiaru składek miesiąc po miesiącu, wynagrodzenie chorobowe/zasiłki osobno); zaświadczenie o zarobkach do banku (wzór); zaświadczenie o stażu z ZUS (pracownik wnioskuje sam).",
            "Zapisz 10 najczęstszych pism z ZUS do płatnika (wezwanie do korekty, zawiadomienie o kontroli, decyzja o stopie wypadkowej, zawiadomienie o nieprawidłowym kodzie…) i co z nimi robisz w jakim terminie (7/14/30 dni).",
        ],
        "sprawdz": "Przewodnik mapuje sekcje eZUS na symulator (+ sekcje bez odpowiednika); procedura PEL; ERP-7 z list płac; tabela pism ZUS z terminami.",
    },
    "k8z5": {
        "tytul": "Zadanie tygodnia: rok w symulatorze ZUS — od ZUA po IWA i IMIR",
        "kroki": [
            "Warsztat → eZUS / Płatnik → „Ubezpieczeni” → „Wyczyść wszystkie zgłoszenia”. Zgłoś od nowa 3 osoby (ZUA ze styczniem 2026 lub datą zatrudnienia): Marek Zieliński (choroby z tygodnia 6), Ewa Sobczak (wychowawczy od 1.07.2026), Anna Kowalczyk (ustanie 31.12.2026).",
            "Warsztat → Lista płac: policz te 3 osoby dla każdego miesiąca 2026-01 … 2026-12 (zmieniaj tylko miesiąc i odchylenia: chorobowe/zasiłek Marka w miesiącach L4; Ewa od lipca — zasadnicze 0, bo wychowawczy). Po każdym — „Dodaj do listy miesiąca”.",
            "Dla każdego miesiąca: „Rozliczenie DRA/RCA/RSA” → RSA (331/313 Marka z e-ZLA i puli 33 dni; 121 Ewy od lipca — w prawdziwym RCA miałaby kod 12 11 z podstawą 60% prognozowanego = 5 652 zł i zdrowotną od 620 zł finansowaną z budżetu — opisz to w pliku, symulator wykazuje przerwę) → Weryfikuj → Wyślij. 12 kompletów, 12 numerów UPP.",
            "Grudzień: ZWUA dla Anny Kowalczyk (2027-01-01, kod 100, tryb 7); premia roczna — w pliku opisz RPA (symulator go nie ma). IWA za 2026 do 31.01.2027 — wypisz pola (liczba ubezpieczonych, wypadki: 1 w 2026 — dopisz do FIRMA.md, zatrudnieni w warunkach zagrożenia). IMIR do 28.02.2027 — dla 3 osób z „Rejestru wysłanych”: sumy podstaw i składek z kartoteki.",
            "Rejestr terminów ZUS na 2027 (15. miesięcznie, IWA 31.01, IMIR 28.02, nowa wypadkowa od 1.04 — zawiadomienie do 20.04, ZSWA 31.03 jeśli dotyczy, kontrola 30-krotności). Asystent: „Zadaj mi 10 pytań z kodów ZUS i terminów — po jednym, oceniaj”. Sobota: quiz 8.",
        ],
        "sprawdz": "12 kompletów wysłanych w symulatorze (rejestr z 12 UPP); 3 zgłoszenia + ZWUA; wychowawczy opisany z kodem 12 11; IWA i IMIR; rejestr terminów 2027.",
        "problemy": ["Wychowawczy jako wyrejestrowanie z 01 10 → nie; pracownik nadal pracownik; w RCA dodajesz tytuł 12 11 na czas urlopu.",
                     "12 kompletów to dużo klikania → tak ma być: w pracy to 12 miesięcy; w symulatorze lista płac zapamiętuje osoby, zmieniasz tylko miesiąc."],
    },
    # ============================================================ TYDZIEŃ 9
    "k9z1": {
        "tytul": "PIT-11 za 2026 i PIT-4R firmy — z kartoteki w Warsztacie",
        "kroki": [
            "Lekcja „PIT roczny płatnika”. Terminy: PIT-4R i PIT-11 do urzędu do 31.01.2027 (elektronicznie, UPL-1), PIT-11 pracownikowi do 28.02.2027; IFT-1R dla nierezydentów do 28.02. Treść PIT-11: przychody wg źródeł, KUP, zaliczki, składki społeczne (bez zdrowotnej), przychody zwolnione (ulga dla młodych), zasiłki jako „inne źródła”.",
            "Warsztat → e-Urząd: PIT → rok 2026 → podatnik: Tomasz Lis → „Generuj PIT-11” (dane z Twojej listy płac — kartoteka z 12 miesięcy z zadania tygodnia 8; jeśli Tomasza tam nie ma, policz jego miesiące w Lista płac z rosnącym „Dochód narastająco” — w listopadzie pojawi się 32%). Zapisz PIT-11 do projektu; to samo dla Jakuba Krawczyka (sekcja G — przychody zwolnione, ulga dla młodych) i Marka Zielińskiego (zasiłki w „innych źródłach”, wynagrodzenie chorobowe w przychodach ze stosunku pracy).",
            "„Generuj PIT-4R”: suma zaliczek NALEŻNYCH miesięcznie, liczba podatników, terminy wpłat (20. następnego miesiąca na mikrorachunek NIP). Sprawdź: suma zaliczek z PIT-4R = suma zaliczek ze wszystkich PIT-11 (zapisz obliczenie w pit4r_2026.md).",
            "„Wyślij (symulacja, UPO)” dla PIT-4R i jednego PIT-11 — zapisz numery UPO. Zwolnienia i zaokrąglenia: świadczenia ZFŚS do 1 000 zł nie w PIT-11; diety do limitu nie; ekwiwalent za pranie nie; odprawa tak. Korekta PIT-11 — gdy błąd; PESEL obowiązkowy.",
            "Asystent: „Sprawdź @pit11_2026.md — czy przychody zwolnione dla osoby do 26 lat są w dobrym polu?”",
        ],
        "sprawdz": "3 PIT-11 wygenerowane z kartoteki i zapisane; PIT-4R z 12 kwotami i uzgodnieniem z PIT-11; UPO dla PIT-4R; terminy opisane.",
        "pliki": ["pit_tomasz_2026.md", "pit_4r_2026.md", "pit4r_2026.md"],
    },
    "k9z3": {
        "kroki": [
            "PFRON: obowiązek przy ≥ 25 etatach, gdy wskaźnik niepełnosprawnych < 6%. Wpłata = 40,65% × przeciętne wynagrodzenie (GUS, poprzedni kwartał — przyjmij 9 000 zł i zaznacz, że to założenie do aktualizacji) × (6% × 58,5 etatu − 1 etat Ewy Sobczak). Policz na kartce i zapisz w pfron_gus.md; termin do 20. dnia następnego miesiąca; deklaracja DEK-I-0 (w pracy: e-PFRON2 — wypisz jej pola jako tabelę). Schorzenia szczególne liczą się ×2/×3 do wskaźnika.",
            "Ulgi: faktury od pracodawców uprawnionych (do 50% wpłaty), dofinansowanie do wynagrodzeń (SOD, Wn-D do 25.): znaczny 2 760 zł, umiarkowany 1 550, lekki 575 + dodatki za schorzenia szczególne (kwoty z lekcji — sprawdzaj co roku). Policz, czy opłaca się zatrudnić 3 osoby z orzeczeniem umiarkowanym (oszczędność wpłaty + dofinansowanie vs koszt z Warsztat → Lista płac dla 4 806 zł).",
            "Uprawnienia pracownika z orzeczeniem: 7 h/35 h (umiarkowany/znaczny), dodatkowa przerwa 15 min, 10 dni dodatkowego urlopu po roku, turnus 21 dni, zakaz nocnej i nadgodzin (chyba że lekarz zgodzi). Sprawdź w Warsztacie: Czas pracy (wymiar × 7/8) i Urlopy (norma dobowa 7) dla Ewy Sobczak.",
            "GUS: Z-06 (roczne, początek lutego), Z-03 (kwartalne — wylosowane), Z-12 (co 2 lata — wylosowane), DG-1 (miesięczne — wylosowane); portal sprawozdawczy GUS. Wypisz, skąd bierzesz dane do Z-06 (przeciętne zatrudnienie w etatach, wynagrodzenia brutto z list płac w Warsztacie, czas przepracowany, nadgodziny).",
            "Dodaj do kalendarza firmy (zadanie 5) terminy PFRON (20.), GUS (2.02, kwartalne 10 dni po kwartale), Wn-D (25.).",
        ],
        "sprawdz": "Wpłata PFRON policzona z wzorem (założenie przeciętnego zaznaczone); kalkulacja 3 osób z orzeczeniem; uprawnienia Ewy Sobczak sprawdzone w Warsztacie; lista sprawozdań GUS.",
    },
    "k9z4": {
        "pliki": ["rejestr_terminow.md"],
        "kroki": [
            "Badania okresowe: częstotliwość z orzeczenia lekarza medycyny pracy (typowo 2–4 lata; nocne/hałas — częściej); kontrolne po ≥ 30 dniach choroby (przed dopuszczeniem!); skierowanie z czynnikami szkodliwymi; koszt pracodawcy, w godzinach pracy. Zbuduj w rejestr_terminow.md tabelę: osoba | stanowisko | data badania | ważne do | alert (data − 60 dni) — daty policz ręcznie (kalendarz w Warsztat → Czas pracy pokazuje dni robocze).",
            "Szkolenia BHP okresowe: robotnicze co 3 lata (co rok przy szczególnie niebezpiecznych), administracyjno-biurowi co 6 lat (zwolnieni przy ryzyku ≤ 3 kategorii, decyzja pracodawcy), kierownicy co 5 lat (pierwsze do 6 mies.). Dodaj do rejestru; wstępne — dzień 1.",
            "Uprawnienia: wózki jezdniowe (zaświadczenia UDT — 5 lub 10 lat), SEP (5 lat), prawo jazdy C + kod 95 (5 lat) — dla osób z karty firmy. Dokumenty cudzoziemca: ważność pobytu; orzeczenia o niepełnosprawności (data ważności → PFRON i uprawnienia).",
            "Ocena ryzyka i instrukcje — kto, kiedy aktualizuje; wypadek: zespół, protokół 14 dni, Z-KW, rejestr; choroby zawodowe — zgłoszenie.",
            "Procedura przypomnień: kto sprawdza rejestr (co tydzień), jak zgłasza przełożonemu, co gdy pracownik nie stawił się na badanie (niedopuszczenie bez wynagrodzenia). Opcjonalnie: tę tabelę możesz przenieść do arkusza z formułą alertu — kurs tego nie wymaga.",
        ],
        "sprawdz": "Rejestr z datami alertów dla 8 osób; częstotliwości BHP i badań poprawne; procedura przypomnień.",
    },
    "k9z5": {
        "pliki": ["kalendarz_2027.md"],
        "kroki": [
            "W kalendarz_2027.md zbuduj tabelę: miesiąc | dzień | obowiązek | podstawa prawna (Warsztat → Przepisy) | odpowiedzialny | dokument / narzędzie | ryzyko (kara/odsetki/wykroczenie). Minimum 60 wierszy.",
            "Miesięczne: lista płac (do 10.), PPK (15.), ZUS (15.), PIT zaliczki (20.), PFRON (20.), Wn-D (25.), e-ZLA (codziennie), kontrola 30-krotności, zmiany PIT-2 od następnego miesiąca.",
            "Roczne: styczeń — minimalna 4 950 zł (aneksy, kwoty wolne, dodatek nocny), PIT-4R i PIT-11 do US (31.01), IWA (31.01), plan urlopów; luty — PIT-11 pracownikom (28.02), IMIR, informacja o autozapisie PPK; marzec — deklaracje rezygnacji PPK, ZSWA (31.03), nowa wypadkowa od 1.04 (decyzja do 20.04); kwiecień — autozapis PPK (1.04); maj — ZFŚS 75% (31.05), PROCEDURY ANTYMOBBINGOWE do 5.05.2027; wrzesień — ZFŚS reszta i urlopy zaległe (30.09), minimalna 2028 (do 15.09); listopad — stan ubezpieczonych na 30.11; grudzień — korekta ZFŚS, zamknięcie list, 24.12 wolne. Jawność wynagrodzeń (UC127) — wpisz jako „projekt — sprawdzić status”.",
            "Cykliczne: badania i BHP z rejestru (zadanie 4), dokumenty cudzoziemców, przegląd danych ZFŚS (RODO), kary porządkowe po roku, archiwizacja akt po 10 latach, umowy na czas określony (33/3), ocena ryzyka, staż — termin 24 mies. (1.05.2028).",
            "Asystent: „Przejrzyj @kalendarz_2027.md — czego brakuje w kalendarzu firmy 62-osobowej?”. Zweryfikuj każdą podpowiedź w bibliotece przepisów. Sobota: quiz 9 i CHECKLISTA etapu 3.",
        ],
        "sprawdz": "≥ 60 wierszy z podstawą i odpowiedzialnym; wszystkie terminy z lekcji; 5.05.2027 i 1.04.2027 obecne.",
    },
    # ============================================================ TYDZIEŃ 10
    "k10z2": {
        "kroki": [
            "Art. 52: ciężkie naruszenie podstawowych obowiązków (wina umyślna/rażące niedbalstwo), przestępstwo oczywiste lub stwierdzone wyrokiem, zawiniona utrata uprawnień; termin 1 miesiąc od uzyskania wiadomości przez osobę decyzyjną; konsultacja związkowa (3 dni); pismo z przyczyną i pouczeniem; możliwe także w czasie choroby/urlopu. Kazus: Marek Zieliński ujęty na kradzieży 10 kg sera 3.11, zarząd wie 4.11 → ostatni dzień 4.12.",
            "Napisz pismo (szablon: Prompty → „Wypowiedzenie…”, zmień tryb na rozwiązanie bez wypowiedzenia), notatkę służbową, oświadczenia świadków. Warsztat → eZUS / Płatnik: ZWUA dla Marka — data = dzień po doręczeniu, kod 100, tryb 4 (art. 52 §1 pkt 1) → Weryfikuj → Wyślij. Świadectwo: tryb z art. 30 §1 pkt 3 w zw. z art. 52 §1 pkt 1.",
            "Alternatywy: kara porządkowa (upomnienie/nagana/pieniężna — 2 tygodnie od wiedzy, 3 mies. od zdarzenia, wysłuchanie, sprzeciw 7 dni; część D akt), porozumienie stron (szybkie, bez „kary”, ale zasiłek dla bezrobotnych dopiero po 90 dniach, chyba że z przyczyn pracodawcy), wypowiedzenie zwykłe (Warsztat → Czas pracy → „Okres wypowiedzenia”: staż Marka 20 mies. → 1 miesiąc → data).",
            "Art. 53: bez wypowiedzenia, gdy niezdolność trwa dłużej niż 3 mies. (staż < 6 mies.) lub dłużej niż okres zasiłkowy + 3 mies. świadczenia rehabilitacyjnego (staż ≥ 6 mies.) — kazus z tygodnia 6: 182 dni (od 1.07 → 29.12) + rehabilitacyjne 3 mies. → data; nie można rozwiązać, gdy pracownik stawi się po ustaniu przyczyny; ponowne zatrudnienie w 6 mies. w miarę możliwości. Pismo, konsultacja.",
            "Ryzyka: 52 bez dowodów → sąd; odszkodowanie; porozumienie „pod presją” — wada oświadczenia woli. 5 zasad „bezpiecznej dyscyplinarki”. Asystent: „Oceń ryzyko sądowe mojego art. 52 w @art52_53.md — co by zrobił pełnomocnik pracownika?”",
        ],
        "sprawdz": "Oba pisma; ZWUA z trybem 4 przyjęte w symulatorze; termin 1 miesiąca i data z art. 53 policzone; alternatywy z datą wypowiedzenia z Warsztatu; 5 zasad.",
    },
    # ============================================================ TYDZIEŃ 11
    "k11z3": {
        "kroki": [
            "Lekcja „Sygnaliści, praca zdalna, RODO”. Sygnaliści (ustawa z 14.06.2024): procedura zgłoszeń wewnętrznych u pracodawców ≥ 50 osób — firma 62: TAK; konsultacje 5–10 dni; kanały pisemny/ustny, potwierdzenie 7 dni, informacja zwrotna 3 mies., bezstronna osoba, rejestr (3 lata), zakaz odwetu; zakres z ustawy (rozszerz o prawo pracy — zdecyduj). Procedura 1 strona + rejestr w procedury_compliance.md.",
            "Praca zdalna: porozumienie/regulamin lub umowa, BHP (oświadczenie, ocena ryzyka), ryczałt (bez PIT i ZUS, jeśli odpowiada kosztom — wylicz: prąd 3 dni × 8 h × 0,25 kWh × cena + część internetu), kontrola uzgodniona, okazjonalna 24 dni, wnioski wiążące — odmowa tylko z organizacji/rodzaju pracy, w 7 dni. Regulamin 1 strona dla biura firmy.",
            "Kontrola trzeźwości (art. 22¹ᶜ KP): tylko gdy niezbędna dla ochrony życia/zdrowia/mienia; w regulaminie: grupa, metoda (alkomat z kalibracją), częstotliwość; informacja 2 tygodnie przed; niedopuszczenie bez wynagrodzenia; akta E (rok). Zasady dla produkcji i kierowców.",
            "RODO w kadrach: podstawy (art. 6 ust. 1 lit. b, c; art. 9 ust. 2 lit. b), rejestr czynności (rekrutacja, kadry-płace, ZFŚS, monitoring, trzeźwość, PPK), retencja (CV — koniec rekrutacji / 12 mies. za zgodą; akta — 10 lat; ewidencja — jak akta; ZFŚS — do przedawnienia; monitoring — 3 mies.), upoważnienia, umowy powierzenia (biuro rachunkowe, instytucja PPK; medycyna pracy — odrębny administrator), obowiązek informacyjny, prawo dostępu (kopia w 30 dni), naruszenie (72 h do UODO). Rejestr czynności 6 wierszy i tabela retencji 10 wierszy. Podstawy sprawdzaj w Warsztat → Przepisy („sygnaliści”, „zdalna”, „monitoring”).",
            "Asystent: „Które z 4 procedur są u mnie fasadowe? Zadaj mi po 2 pytania do każdej.”",
        ],
    },
    "k11z4": {
        "kroki": [
            "Lekcja „Kontrola PIP i ZUS”. PIP: bez zapowiedzi, legitymacja (upoważnienie w 7 dni), dostęp do dokumentów i pomieszczeń, przesłuchania; protokół (zastrzeżenia 7 dni), wystąpienie (30 dni), nakaz (BHP, wypłata — natychmiast wykonalny), mandat 1 000–2 000 zł (5 000 recydywa), sąd — do 30 000 zł; projekt zmian w ustawie o PIP (decyzje o stosunku pracy) — nieuchwalony, sprawdzaj status.",
            "Lista dokumentów „na kontrolę” (30 pozycji) w kontrola_pip_zus.md: regulaminy, akta, umowy, ewidencja z 3 lat, listy płac (Twoje z Warsztatu: 04-place), potwierdzenia wypłat, zgody na nadgodziny, badania, BHP, ocena ryzyka, rejestr wypadków, ZFŚS, procedury (sygnaliści, antymobbingowa do 5.05.2027, trzeźwość, zdalna), umowy cywilnoprawne z ewidencją godzin (31,40), dokumenty cudzoziemców, PPK, monitoring, rejestr dokumentów ZUS (05-zus-us).",
            "Symulacja: Prompty → „Symulacja kontroli” — Asystent jako inspektor zadaje 10 pytań o czas pracy i wynagrodzenia na podstawie Twoich plików (@audyt_czasu_pracy.md, @lista_plac_2026-11.md). Odpowiadasz dokumentem, nie słowem. Zapisz, czego nie umiałeś pokazać.",
            "ZUS: zawiadomienie 7–30 dni przed, upoważnienie, zakres (zgłaszanie, podstawy, zasiłki, ZFŚS, umowy cywilnoprawne), limit dni 12/18/24/48, protokół, zastrzeżenia 14 dni, decyzja — odwołanie do sądu w miesiąc; typowe ustalenia: dzieło = zlecenie, ZFŚS po równo, benefity bez składek, zbiegi. Przygotuj odpowiedź na 3 ustalenia z audytu form zatrudnienia (tydzień 7) — dokumentami z Warsztatu (rejestr ZUS, RUD jako tabela).",
            "Plan naprawczy po kontroli: tabela ustalenie | termin | działanie | odpowiedzialny | koszt; komunikacja do zarządu.",
        ],
    },
    "k11z5": {
        "kroki": [
            "Zbierz wszystkie pliki z folderów 01–07 i 99 w PORTFOLIO.md: spis z opisem (co to, kiedy używać, podstawa prawna, data aktualizacji) — w tym pliki zapisane z Warsztatu (listy płac MD/CSV, zus_*.md, rejestr_zus.md, pit_*.md, podstawa_zasilku.md). To Twój dowód kompetencji na rozmowie.",
            "Audyt 20 obszarów firmy ćwiczeniowej: umowy i limity 33/3, dokumentacja/akta, informacja art. 29 §3, czas pracy i ewidencja, nadgodziny i wolne, urlopy i zaległe, staż 2026, listy płac i oświadczenia PIT, benefity i ZFŚS, potrącenia, chorobowe i zasiłki, kontrola L4, umowy cywilnoprawne i B2B, PPK, ZUS (zgłoszenia, korekty, IWA), PIT roczny, PFRON/GUS, badania/BHP/uprawnienia, rozwiązania umów i odprawy, compliance (mobbing 5.05.2027, jawność, sygnaliści, zdalna, trzeźwość, RODO). Dla każdego: stan (zielony/żółty/czerwony), ustalenie, podstawa, ryzyko w zł, działanie, termin, koszt. Kwoty ryzyka licz w Warsztacie (składki wstecz z Lista płac, odprawy z Urlopy/ekwiwalent, odsetki).",
            "Plan naprawczy na 12 miesięcy z priorytetami (5.05.2027 procedury; 1.04.2027 PPK; staż 24 mies.) i budżetem; 1-stronicowe streszczenie dla zarządu (3 największe ryzyka w zł, 3 szybkie wygrane).",
            "Prezentacja 10 slajdów w Markdown (plik prezentacja.md: jeden nagłówek = slajd): kim jestem, co zbadałem, 5 kluczowych ustaleń, plan, koszt vs ryzyko. Nagraj (telefonem) 3-minutową opowieść o audycie — jak na rozmowie. CV: sekcja „Projekty” — audyt + portfolio; „Umiejętności”: lista z kursu, narzędzia (eZUS/Płatnik, e-Deklaracje, program kadrowy — poznane na symulatorze), stan prawny 2026/2027.",
            "Asystent: „Oceń @AUDYT_KONCOWY.md jak senior kadrowy przed przekazaniem zarządowi — 3 najpoważniejsze błędy merytoryczne”. Zweryfikuj uwagi w bibliotece przepisów, popraw. Sobota: quiz 11, CHECKLISTA etapu 4 i próbna rozmowa (Asystent: „odpytaj mnie jak rekruter”).",
        ],
        "sprawdz": "Audyt 20 obszarów z ocenami i kwotami ryzyka; plan 12 mies.; PORTFOLIO ≥ 40 plików (w tym z Warsztatu); prezentacja.md; nagranie; CV.",
        "pliki": ["AUDYT_KONCOWY.md", "PORTFOLIO.md", "prezentacja.md"],
    },

    # ============================================================ DOPISKI „W WARSZTACIE” do zadań liczonych ręcznie (kontrola wyniku)
}

# krok dopisywany na końcu listy kroków (sprawdzenie ręcznego wyniku w narzędziu) — klucz: id zadania
DOPISZ_KROK = {
    "k2z2": "Kontrola: Warsztat → Czas pracy pokazuje wymiar każdego miesiąca i dni robocze — sprawdź, czy grafik sumuje się do wymiaru okresu.",
    "k2z3": "Kontrola: Warsztat → Czas pracy → „Nadgodziny” (zasadnicze, wymiar, h50, h100) i „Dodatek nocny” (64 h w listopadzie) — porównaj z rachunkiem ręcznym; w pliku zapisz, gdzie się różniłeś.",
    "k3z1": "Kontrola: Warsztat → Urlopy i ekwiwalent → „Wymiar urlopu” (staż, etat, miesiące w roku, pierwsza praca) dla każdej z 8 osób — porównaj z rachunkiem ręcznym.",
    "k3z5": "Kontrola: plan urlopów sprawdź z wymiarami z Warsztat → Urlopy i ekwiwalent; dni robocze 2027 — Warsztat → Czas pracy (rok 2027).",
    "k4z4": "Kontrola: Warsztat → Lista płac liczy koszt pracodawcy każdej osoby (ostatni krok; wypadkowa firmy 1,20% z parametrów) — zsumuj 8 wierszy listy miesiąca × 12 i porównaj ze swoim budżetem.",
    "k5z2": "Kontrola: Warsztat → Urlopy i ekwiwalent — „Ekwiwalent” (6 000 + zmienne 1 200 z 3 mies., 56 h) i „Pomniejszenie” (6 000, 10 dni choroby, 24 h bezpłatnego, wymiar 160) — porównaj z rachunkiem.",
    "k5z3": "Kontrola: Warsztat → Potrącenia — dla każdego kazusu wpisz netto, rodzaj i parametry pracownika (KUP, PIT-2, PPK, etat); porównaj kwotę wolną i potrącenie z rachunkiem ręcznym.",
    "k5z5": "Wykonanie: całą listę 2026-12 zbuduj w Warsztat → Lista płac (wiersz za wierszem, z „Tryb ćwiczenia”): urlop A — zmienne z Urlopy; bezpłatny B — pomniejszenie; komornik C — kwota z Potrącenia w polu „Potrącenia”; D — ekwiwalent i premia roczna w polu „Nadgodziny/premie”; E — 400 w „Świadczenia w naturze”; F — pensja za część miesiąca. „Zapisz listę (MD + CSV)”.",
    "k6z5": "Kontrola: Warsztat → Zasiłki i chorobowe → B: wpisz wszystkie nieobecności roku (choroba, opieka, wypadek_droga) ze stawką dzienną z podstawy — porównaj kwoty i dzień przejścia na zasiłek; dodatkowo w Lista płac policz wrzesień z wynagrodzeniem chorobowym i zasiłkiem.",
    "k7z1": "Kontrola: dla zleceniobiorców Warsztat → Lista płac nie liczy (KUP 20%), policz ręcznie w tabeli w pliku; zgłoszenia do ZUS wykonaj w Warsztat → eZUS / Płatnik (ZUA 041100 / ZZA / brak dla studenta) i sprawdź komunikaty.",
    "k9z2": "Kontrola: odpis ZFŚS licz ręcznie (etaty × 2 943,23 + zwiększenia) — parametr odpisu jest w Warsztat → Przepisy („ZFŚS”); etaty pracowników z Warsztat → Firma ćwiczeniowa.",
    "k10z3": "Kontrola: odprawę liczysz jak ekwiwalent — Warsztat → Urlopy i ekwiwalent → „Ekwiwalent” daje podstawę (stałe + zmienne 3 mies. + 1/12 rocznych); odprawa = podstawa × 1/2/3, limit 72 090.",
    "k11z2": "Kontrola: luka płacowa — stawki zasadnicze 8 osób masz w Warsztat → Firma ćwiczeniowa; kategorie z regulaminu (I–V) tam samo; policz średnie i mediany K/M ręcznie w tabeli.",
}
