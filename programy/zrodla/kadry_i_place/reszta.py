# -*- coding: utf-8 -*-
"""Kadry i płace — quizy tygodniowe, rytm dnia, prompty, szablony, checklisty, ściąga, linki, pojęcia, „błędy”, pytania rekrutacyjne."""

# ---------------------------------------------------------------- QUIZY (klucz = tydzień)
QUIZY = {
    0: [
        {"p": "Minimalne wynagrodzenie za pracę w 2026 r.:", "o": ["4 666 zł", "4 806 zł", "4 950 zł", "5 000 zł"], "odp": 1, "w": "4 950 zł obowiązuje od 1.01.2027."},
        {"p": "Gdzie znajdziesz obwieszczenie o limicie 30-krotności?", "o": ["Dziennik Ustaw", "Monitor Polski", "ISAP", "Strona PIP"], "odp": 1, "w": "Obwieszczenia ministra — M.P."},
        {"p": "Kto podpisuje pełnomocnictwo PEL dla pracownika kadr?", "o": ["Pracownik kadr", "Osoba uprawniona do reprezentacji płatnika (zarząd)", "ZUS", "Główny księgowy zawsze"], "odp": 1, "w": "Pełnomocnictwo udziela płatnik."},
        {"p": "Składka zdrowotna pracownika wynosi:", "o": ["7,75%", "9%", "2,45%", "13,71%"], "odp": 1, "w": "9% od podstawy po odliczeniu składek społecznych."},
        {"p": "Zasada uprzywilejowania pracownika (art. 18 KP) oznacza, że:", "o": ["Pracownik może żądać dowolnych warunków", "Postanowienia umowy mniej korzystne niż przepisy są nieważne — stosuje się przepisy", "Regulamin jest ważniejszy od ustawy", "Umowa może wyłączyć Kodeks pracy"], "odp": 1, "w": "Umowa/regulamin mogą być tylko korzystniejsze."},
    ],
    1: [
        {"p": "Kandydat na rozmowie: czy możesz zapytać o wysokość ostatniej pensji?", "o": ["Tak", "Nie — zakaz od 24.12.2025", "Tylko pisemnie", "Tylko za zgodą"], "odp": 1, "w": "Art. 22¹ §1 pkt 6 KP."},
        {"p": "Łączny limit umów na czas określony:", "o": ["24 miesiące / 2 umowy", "33 miesiące / 3 umowy", "36 miesięcy / 3 umowy", "Brak limitu"], "odp": 1, "w": "Art. 25¹ KP."},
        {"p": "Zgłoszenie nowego pracownika do ZUS (ZUA) składasz w ciągu:", "o": ["3 dni", "7 dni od rozpoczęcia pracy", "14 dni", "Do końca miesiąca"], "odp": 1, "w": "Od powstania obowiązku ubezpieczenia."},
        {"p": "Informację o warunkach zatrudnienia (art. 29 §3) przekazujesz:", "o": ["W dniu podpisania umowy", "W 7 dni od dopuszczenia do pracy", "W 30 dni", "Po okresie próbnym"], "odp": 1, "w": "Rozszerzony zakres od 2023."},
        {"p": "Okres przechowywania akt pracownika zatrudnionego w 2024 r.:", "o": ["50 lat", "10 lat od końca roku ustania zatrudnienia", "5 lat", "3 lata"], "odp": 1, "w": "Zatrudnieni od 1.01.2019."},
    ],
    2: [
        {"p": "Dobowy odpoczynek pracownika wynosi co najmniej:", "o": ["8 h", "11 h", "12 h", "24 h"], "odp": 1, "w": "Art. 132 KP; tygodniowy 35 h."},
        {"p": "Dodatek za nadgodziny w niedzielę (niebędącą dniem pracy wg rozkładu):", "o": ["50%", "100%", "150%", "Brak dodatku"], "odp": 1, "w": "Art. 151¹ §1 pkt 1 KP."},
        {"p": "Dodatek za godzinę pracy w nocy w 2026 r. to 20% stawki godzinowej z:", "o": ["Wynagrodzenia pracownika", "Minimalnego wynagrodzenia", "Przeciętnego wynagrodzenia", "Stawki z umowy"], "odp": 1, "w": "4 806 zł / wymiar miesiąca × 20%."},
        {"p": "Harmonogram czasu pracy przekazujesz pracownikowi co najmniej:", "o": ["1 dzień wcześniej", "1 tydzień przed okresem, na który jest sporządzony (min. 1 miesiąc)", "3 dni", "W pierwszym dniu miesiąca"], "odp": 1, "w": "Art. 129 §3 KP."},
        {"p": "Ewidencja czasu pracy musi zawierać:", "o": ["Tylko liczbę godzin", "Godziny rozpoczęcia i zakończenia pracy, nadgodziny, nocne, dyżury, nieobecności", "Tylko nieobecności", "Tylko nadgodziny"], "odp": 1, "w": "§6 rozporządzenia o dokumentacji pracowniczej."},
    ],
    3: [
        {"p": "Wymiar urlopu przy stażu ≥ 10 lat:", "o": ["20 dni", "26 dni", "30 dni", "24 dni"], "odp": 1, "w": "Art. 154 KP."},
        {"p": "Od 1.05.2026 prywatny pracodawca wlicza do stażu:", "o": ["Tylko umowy o pracę", "Także zlecenia i działalność z opłaconymi składkami", "Umowy o dzieło", "Wolontariat"], "odp": 1, "w": "Dokumentowane zaświadczeniem ZUS."},
        {"p": "Urlop rodzicielski — część nieprzenoszalna dla każdego z rodziców:", "o": ["4 tygodnie", "9 tygodni", "12 tygodni", "20 tygodni"], "odp": 1, "w": "Z 41 tygodni łącznie."},
        {"p": "Zwolnienie z powodu siły wyższej (art. 148¹) jest płatne w wysokości:", "o": ["100%", "80%", "50%", "Bezpłatne"], "odp": 2, "w": "2 dni lub 16 h w roku."},
        {"p": "Urlop na żądanie w roku to:", "o": ["4 dni dodatkowe", "4 dni z puli urlopu wypoczynkowego", "2 dni", "Nie ma takiego urlopu"], "odp": 1, "w": "Art. 167² KP."},
    ],
    4: [
        {"p": "Składki społeczne finansowane przez pracownika łącznie:", "o": ["9,76%", "11,26%", "13,71%", "22,71%"], "odp": 2, "w": "9,76 + 1,5 + 2,45."},
        {"p": "Koszty uzyskania przychodu dla pracownika dojeżdżającego (oświadczenie):", "o": ["250 zł", "300 zł", "20%", "50%"], "odp": 1, "w": "Miejsce zamieszkania poza miejscowością zakładu."},
        {"p": "Kwota zmniejszająca podatek przy PIT-2 (1/12):", "o": ["250 zł", "300 zł", "425 zł", "600 zł"], "odp": 1, "w": "30 000 × 12% / 12."},
        {"p": "Podstawę opodatkowania zaokrąglasz do:", "o": ["Grosza", "10 groszy", "Pełnego złotego", "10 złotych"], "odp": 2, "w": "Zaliczkę również."},
        {"p": "Za którego pracownika nie płacisz FP i FGŚP?", "o": ["Za 40-letnią pracownicę", "Za 57-letnią pracownicę", "Za 25-letniego pracownika", "Za nikogo"], "odp": 1, "w": "Kobiety 55+, mężczyźni 60+."},
    ],
    5: [
        {"p": "Składniki zmienne do wynagrodzenia urlopowego bierzesz z:", "o": ["1 miesiąca", "3 miesięcy poprzedzających (do 12)", "12 miesięcy", "Całego roku"], "odp": 1, "w": "§8 rozporządzenia urlopowego."},
        {"p": "Współczynnik ekwiwalentu 2026 (pełny etat):", "o": ["20,83", "20,92", "21,08", "20,75"], "odp": 1, "w": "(365 − 52 − 52 − 10)/12."},
        {"p": "Granica potrąceń na alimenty:", "o": ["1/2 wynagrodzenia", "3/5 wynagrodzenia, bez kwoty wolnej", "1/3", "100%"], "odp": 1, "w": "Art. 87 §3 KP."},
        {"p": "Pomniejszenie pensji za chorobę liczysz dzieląc przez:", "o": ["Liczbę dni roboczych miesiąca", "30", "Wymiar godzin", "Liczbę dni kalendarzowych miesiąca"], "odp": 1, "w": "§11 rozporządzenia z 1996 r."},
        {"p": "Zwolnienie z PIT świadczeń z ZFŚS w roku (bez bonów):", "o": ["500 zł", "1 000 zł", "2 000 zł", "Bez limitu"], "odp": 1, "w": "Art. 21 ust. 1 pkt 67."},
    ],
    6: [
        {"p": "Wynagrodzenie chorobowe od pracodawcy dla pracownika 45-letniego:", "o": ["14 dni", "33 dni w roku kalendarzowym", "90 dni", "182 dni"], "odp": 1, "w": "Art. 92 KP."},
        {"p": "Okres zasiłkowy (poza ciążą i gruźlicą):", "o": ["90 dni", "182 dni", "270 dni", "365 dni"], "odp": 1, "w": "Art. 8 ustawy zasiłkowej."},
        {"p": "Podstawę wymiaru zasiłku liczysz z wynagrodzenia wypłaconego za:", "o": ["3 miesiące", "6 miesięcy", "12 miesięcy kalendarzowych poprzedzających", "Rok kalendarzowy"], "odp": 2, "w": "Po odliczeniu 13,71%."},
        {"p": "Zasiłek opiekuńczy na chore dziecko 10-letnie — limit roczny:", "o": ["14 dni", "30 dni", "60 dni", "Bez limitu"], "odp": 2, "w": "Łącznie 60 dni na wszystkich."},
        {"p": "Nowe zasady kontroli zwolnień (praca zarobkowa, aktywność niezgodna z celem) obowiązują od:", "o": ["1.01.2026", "13.04.2026", "1.01.2027", "5.11.2026"], "odp": 1, "w": "Dz.U. 2026 poz. 26."},
    ],
    7: [
        {"p": "Zleceniobiorca-student (24 lata) — składki ZUS:", "o": ["Pełne", "Tylko zdrowotna", "Brak", "Tylko wypadkowa"], "odp": 2, "w": "Nie podlega ubezpieczeniom do 26. roku życia."},
        {"p": "Minimalna stawka godzinowa na zleceniu w 2026 r.:", "o": ["30,50 zł", "31,40 zł", "32,30 zł", "28,10 zł"], "odp": 1, "w": "Obowiązek ewidencji godzin."},
        {"p": "Umowę o dzieło zgłaszasz do ZUS na formularzu:", "o": ["ZUA", "RUD w 7 dni", "ZZA", "Nie zgłaszasz"], "odp": 1, "w": "Dzieło z osobą niebędącą pracownikiem."},
        {"p": "Wpłata podstawowa pracownika do PPK:", "o": ["0,5%", "1,5%", "2%", "4%"], "odp": 2, "w": "Obniżenie do 0,5% przy wynagrodzeniu ≤ 120% minimalnego."},
        {"p": "Powiadomienie PUP o zatrudnieniu obywatela Ukrainy (status UKR) składasz w:", "o": ["3 dni", "7 dni", "14 dni", "30 dni"], "odp": 2, "w": "Przez praca.gov.pl."},
    ],
    8: [
        {"p": "Kod tytułu ubezpieczenia pracownika:", "o": ["01 10", "04 11", "05 10", "12 11"], "odp": 0, "w": "04 11 — zleceniobiorca."},
        {"p": "Raport o przerwach i zasiłkach:", "o": ["RCA", "RSA", "RPA", "DRA"], "odp": 1, "w": "RCA — składki; RPA — przychody za inny rok itp."},
        {"p": "Spółka z o.o. rozlicza i opłaca składki do:", "o": ["5.", "10.", "15.", "20."], "odp": 2, "w": "Osoby fizyczne — do 20."},
        {"p": "Pierwsza korekta kompletu za marzec 2026 ma identyfikator:", "o": ["01 03 2026", "02 03 2026", "03 03 2026", "K1 03 2026"], "odp": 1, "w": "Kolejne 03, 04…"},
        {"p": "Po przekroczeniu 30-krotności nie naliczasz:", "o": ["Zdrowotnej", "Emerytalnej i rentowej", "Chorobowej", "Wypadkowej"], "odp": 1, "w": "282 600 zł w 2026."},
    ],
    9: [
        {"p": "PIT-11 do urzędu skarbowego składasz do:", "o": ["20 stycznia", "31 stycznia", "Końca lutego", "30 kwietnia"], "odp": 1, "w": "Pracownikowi — do końca lutego."},
        {"p": "Odpis podstawowy ZFŚS 2026 na etat:", "o": ["2 417,14", "2 723,40", "2 943,23", "3 100,00"], "odp": 2, "w": "37,5% × 7 848,60."},
        {"p": "Wpłaty na PFRON obowiązują pracodawcę zatrudniającego co najmniej:", "o": ["10 etatów", "25 etatów (przy wskaźniku < 6%)", "50 etatów", "100 etatów"], "odp": 1, "w": "DEK-I-0 do 20."},
        {"p": "75% odpisu ZFŚS przelewasz do:", "o": ["31 marca", "31 maja", "30 czerwca", "30 września"], "odp": 1, "w": "Reszta do 30 września."},
        {"p": "Zaległy urlop należy udzielić do:", "o": ["31 marca", "30 czerwca", "30 września następnego roku", "31 grudnia"], "odp": 2, "w": "Art. 168 KP."},
    ],
    10: [
        {"p": "Okres wypowiedzenia przy stażu 8 miesięcy:", "o": ["2 tygodnie", "1 miesiąc", "3 miesiące", "1 tydzień"], "odp": 1, "w": "Art. 36 §1 pkt 2."},
        {"p": "Rozwiązanie z art. 52 musisz wręczyć w ciągu:", "o": ["7 dni", "14 dni", "1 miesiąca od uzyskania wiadomości", "3 miesięcy"], "odp": 2, "w": "Art. 52 §2 KP."},
        {"p": "Odprawa z ustawy o zwolnieniach grupowych przy stażu 5 lat:", "o": ["1-miesięczna", "2-miesięczna", "3-miesięczna", "Nie przysługuje"], "odp": 1, "w": "< 2 lata: 1; 2–8: 2; > 8: 3."},
        {"p": "Świadectwo pracy wydajesz:", "o": ["W 7 dni po ustaniu", "W dniu ustania stosunku pracy", "Na wniosek", "Do końca miesiąca"], "odp": 1, "w": "Gdy niemożliwe — 7 dni pocztą."},
        {"p": "Pracownik może odwołać się od wypowiedzenia do sądu pracy w ciągu:", "o": ["7 dni", "14 dni", "21 dni", "30 dni"], "odp": 2, "w": "Art. 264 KP."},
    ],
    11: [
        {"p": "Minimalne odszkodowanie za mobbing po nowelizacji 2026:", "o": ["Minimalne wynagrodzenie", "3-krotność minimalnego", "6-krotność minimalnego wynagrodzenia", "12-krotność"], "odp": 2, "w": "28 836 zł w 2026."},
        {"p": "Dyrektywa 2023/970 przewiduje coroczne raportowanie luki płacowej od:", "o": ["50 pracowników", "100 pracowników", "150 pracowników", "250 pracowników"], "odp": 3, "w": "150–249 i 100–149 co 3 lata."},
        {"p": "Procedura zgłoszeń wewnętrznych (sygnaliści) — próg:", "o": ["20 osób", "50 osób", "100 osób", "250 osób"], "odp": 1, "w": "Ustawa z 14.06.2024."},
        {"p": "Inspektor PIP może rozpocząć kontrolę:", "o": ["Po zawiadomieniu 7 dni wcześniej", "Bez uprzedzenia, po okazaniu legitymacji", "Tylko w dni robocze 8–16", "Tylko po zgodzie pracodawcy"], "odp": 1, "w": "Konwencja MOP nr 81."},
        {"p": "Nagrania z monitoringu wizyjnego przechowujesz:", "o": ["30 dni", "Do 3 miesięcy", "1 rok", "10 lat"], "odp": 1, "w": "Art. 22² KP; dłużej tylko jako dowód."},
    ],
}

# ---------------------------------------------------------------- RYTM DNIA
RYTM_DNIA = [
    {"nazwa": "Nowy temat", "minuty": 20, "ikona": "📖",
     "opis": "Czytasz lekcję dnia (zakładka Lekcje) i jeden przepis z Warsztat → Przepisy. Notujesz 3 liczby/terminy, które musisz zapamiętać.",
     "prompt": "Uczę się [temat]. Wytłumacz na 2 przykładach z firmy produkcyjnej (62 pracowników), podaj podstawę prawną każdej liczby i daj mi 3 kazusy od łatwego do trudnego. Nie podawaj rozwiązań."},
    {"nazwa": "Kazus w Warsztacie", "minuty": 50, "ikona": "🧮",
     "opis": "Rozwiązujesz zadanie dnia: liczysz na kartce i sprawdzasz w Warsztacie, piszesz pismo lub wypełniasz dokument w symulatorze. Najpierw własna próba i podpowiedzi z lekcji po kolei; gdy nie wiesz, jak zacząć — pytasz Asystenta od razu o wskazówkę, nie o wynik.",
     "prompt": "Utknąłem na kazusie: [opis]. Oto mój tok rozumowania i liczby: [wklej]. Nie rozwiązuj za mnie — wskaż, który krok lub którą podstawę prawną sprawdzić."},
    {"nazwa": "Weryfikacja u źródła", "minuty": 15, "ikona": "🔍",
     "opis": "Sprawdzasz wynik: Warsztat → Przepisy, narzędzie Warsztatu lub druga metoda liczenia. Zapisujesz źródło przy każdej liczbie.",
     "prompt": "Oto mój wynik: [wynik] i podstawa: [przepis]. Zadaj mi 3 pytania, które wykryją, czy rozumiem, skąd wzięła się każda liczba. Nie oceniaj, tylko pytaj."},
    {"nazwa": "Wpis do dziennika", "minuty": 5, "ikona": "📝",
     "opis": "Zamykasz sesję: 3 pytania sprawdzające z lekcji, notatka „czego się nauczyłem” w kadry-praktyka/dziennik.md, commit.",
     "prompt": "Zadaj mi 3 krótkie pytania sprawdzające z tematu [temat] — jedno o liczbę, jedno o termin, jedno o podstawę prawną. Oceń odpowiedzi dopiero, gdy odpowiem na wszystkie."},
]

# ---------------------------------------------------------------- PROMPTY
PROMPTY = [
    {"nazwa": "Nowy temat kadrowy", "kiedy": "Początek dnia (pon–czw)",
     "tresc": "Uczę się [temat, np. podstawy wymiaru zasiłku]. Wytłumacz na 2 przykładach z firmy produkcyjnej zatrudniającej 62 osoby. Przy każdej liczbie podaj podstawę prawną i gdzie ją sprawdzić. Potem daj 3 kazusy rosnącej trudności — bez rozwiązań."},
    {"nazwa": "Sprawdź moje obliczenie", "kiedy": "Po policzeniu listy płac / zasiłku / ekwiwalentu",
     "tresc": "Policzyłem [co] dla pracownika: [dane wejściowe]. Mój wynik: [kwoty krok po kroku]. Nie podawaj poprawnego wyniku. Wskaż, który krok jest podejrzany i jaki przepis lub zasadę zaokrąglania powinienem sprawdzić."},
    {"nazwa": "Kazus prawny — pytania naprowadzające", "kiedy": "Gdy nie wiesz, jak rozstrzygnąć sytuację",
     "tresc": "Stan faktyczny: [opis sytuacji]. Pytanie: [co mam ustalić]. Zamiast odpowiedzi zadaj mi 4 pytania, które muszę sobie zadać, i wskaż artykuły Kodeksu pracy lub ustawy, które mam przeczytać. Na końcu zapytaj, jaką decyzję bym podjął."},
    {"nazwa": "Zrób mi test", "kiedy": "Koniec dnia, po lekcji",
     "tresc": "Zadaj mi 5 pytań zamkniętych (A–D) z tematu [temat] na poziomie specjalisty ds. kadr i płac, w tym 2 z liczbami obowiązującymi w 2026 r. Pokaż odpowiedzi dopiero po moich odpowiedziach, z uzasadnieniem i podstawą prawną."},
    {"nazwa": "Przegląd pisma kadrowego", "kiedy": "Po napisaniu wypowiedzenia, informacji, odpowiedzi do komornika…",
     "tresc": "Oto moje pismo: @[plik.md]. Sprawdź jako PIP i jako pełnomocnik pracownika: czy ma wszystkie elementy obowiązkowe (podstawa, przyczyna, pouczenie, terminy, podpis), czy jakieś sformułowanie da się podważyć. Nie przepisuj pisma — wypunktuj braki i zadaj pytania."},
    {"nazwa": "Czy to już obowiązuje?", "kiedy": "Gdy czytasz o „zmianach w prawie pracy”",
     "tresc": "Temat: [np. jawność wynagrodzeń]. Rozdziel wyraźnie: (1) co obowiązuje dziś z datą i numerem Dz.U., (2) co jest projektem i na jakim etapie, (3) czego nie wiesz na pewno. Podaj, gdzie mam to zweryfikować (ISAP, legislacja.gov.pl, sejm.gov.pl)."},
    {"nazwa": "Symulacja kontroli", "kiedy": "Tydzień 11 i przed audytem",
     "tresc": "Wciel się w inspektora PIP / kontrolera ZUS. Kontrolujesz [obszar: czas pracy / umowy cywilnoprawne / zasiłki] w firmie opisanej w @FIRMA.md. Zadawaj mi po jednym pytaniu o dokumenty i liczby; po każdej odpowiedzi powiedz, co byś sprawdził dalej. Na końcu wypisz ustalenia i środki prawne."},
    {"nazwa": "Wytłumacz pracownikowi", "kiedy": "Gdy musisz przekazać trudną informację",
     "tresc": "Muszę wyjaśnić pracownikowi [sytuacja, np. potrącenie komornicze / niższe netto po przekroczeniu progu]. Pomóż mi ułożyć 5-zdaniowe wyjaśnienie prostym językiem, bez żargonu, z jedną liczbą i jednym przepisem. Zapytaj mnie najpierw o 2 fakty, których brakuje."},
]

CLAUDE_MD = """# Zasady pracy — nauka kadr i płac

- Uczę się kadr i płac od podstaw do poziomu specjalisty. Pracuję na fikcyjnej firmie z pliku FIRMA.md.
- Nie rozwiązuj kazusów ani nie licz list płac za mnie. Dawaj pytania naprowadzające, wskazuj przepisy i zasady.
- Każdą liczbę (stawka, limit, kwota) podawaj z podstawą prawną i rokiem obowiązywania. Jeśli nie jesteś pewien, że dana wartość obowiązuje w 2026 r. — powiedz to wprost i wskaż, gdzie sprawdzić (ISAP, zus.pl, podatki.gov.pl).
- Rozróżniaj zawsze: „obowiązuje od…” / „projekt” / „nie wiem”.
- Tłumacz po polsku, prostym językiem, na przykładach z firmy produkcyjnej.
- Gdy poprawiasz moje pismo lub obliczenie — najpierw wypunktuj, co jest nie tak, i zapytaj, czy chcę zobaczyć poprawną wersję.
- Nie kopiuj treści przepisów w całości — cytuj fragment i podawaj artykuł.
- Pliki w tym katalogu: FIRMA.md (dane firmy), dziennik.md (moje notatki), listy płac i dokumenty ZUS/PIT zapisane z Warsztatu (.md/.csv), pisma .md.
- Dane osobowe w ćwiczeniach są fikcyjne. Nie wprowadzaj prawdziwych danych pracowników.
"""

# ---------------------------------------------------------------- SZABLONY
SZABLONY = {
    "notatka_kazusu": {"nazwa": "Notatka z kazusu (jak dokumentować decyzję)", "kiedy": "Każdy kazus, każda niestandardowa decyzja kadrowa",
                       "tresc": """# Kazus: [tytuł]
Data: [RRRR-MM-DD]   Dotyczy: [pracownik / dział — dane fikcyjne]

## Stan faktyczny
[3–5 zdań: kto, co, kiedy, jakie dokumenty mamy]

## Pytanie
[co trzeba rozstrzygnąć — jedno zdanie]

## Podstawa prawna
- [art. … ustawy … — fragment]
- [rozporządzenie / orzeczenie SN / stanowisko PIP, ZUS, MF — link]

## Rozstrzygnięcie i obliczenia
[krok po kroku; każda liczba ze źródłem]

## Ryzyka i alternatywy
[co może zakwestionować PIP/ZUS/sąd; wariant bezpieczniejszy]

## Decyzja i działania
[kto, co, do kiedy; dokumenty do akt (część A/B/C/D/E)]
"""},
    "wypowiedzenie": {"nazwa": "Wypowiedzenie umowy o pracę przez pracodawcę", "kiedy": "Tydzień 10 — zawsze z przyczyną i pouczeniem",
                      "tresc": """[Miejscowość], [data]
[Nazwa pracodawcy, adres]

Pan/Pani [imię i nazwisko]
[stanowisko]

ROZWIĄZANIE UMOWY O PRACĘ ZA WYPOWIEDZENIEM

Rozwiązuję z Panem/Panią umowę o pracę zawartą w dniu [data] na czas [nieokreślony / określony do …] z zachowaniem [2-tygodniowego / 1-miesięcznego / 3-miesięcznego] okresu wypowiedzenia, który upłynie w dniu [data].

Przyczyną wypowiedzenia jest: [konkretna, prawdziwa i zrozumiała przyczyna — fakty, daty, dokumenty; przy redukcji: przyczyna organizacyjna + kryteria doboru].

[Jeżeli dotyczy:] W okresie wypowiedzenia zobowiązuję Pana/Panią do wykorzystania urlopu wypoczynkowego w wymiarze [… dni] w terminie […] (art. 167¹ KP). / Zwalniam Pana/Panią z obowiązku świadczenia pracy od [data] do końca okresu wypowiedzenia z zachowaniem prawa do wynagrodzenia (art. 36² KP).
Przysługuje Panu/Pani zwolnienie na poszukiwanie pracy w wymiarze [2 / 3] dni roboczych z zachowaniem prawa do wynagrodzenia (art. 37 KP).

POUCZENIE: Od niniejszego wypowiedzenia przysługuje Panu/Pani prawo wniesienia odwołania do Sądu Rejonowego – Sądu Pracy w [miejscowość], [adres], w terminie 21 dni od dnia doręczenia niniejszego pisma (art. 264 §1 KP).

[podpis osoby uprawnionej do reprezentacji pracodawcy — imię, nazwisko, funkcja]

Potwierdzam otrzymanie: [data, podpis pracownika] / Notatka o odmowie przyjęcia: [data, świadek]
"""},
    "odpowiedz_komornik": {"nazwa": "Odpowiedź na zajęcie wynagrodzenia (art. 882 KPC)", "kiedy": "W 7 dni od otrzymania zajęcia",
                           "tresc": """[Nazwa pracodawcy, adres, NIP]            [Miejscowość], [data]

Komornik Sądowy przy Sądzie Rejonowym w [miejscowość]
[imię i nazwisko komornika], [adres]
Sygn. akt: [KM …/…]

Dotyczy: zajęcia wynagrodzenia za pracę dłużnika [imię i nazwisko, PESEL]

W odpowiedzi na zajęcie z dnia [data], doręczone [data], informuję (art. 882 §1 KPC):
1. Dłużnik jest zatrudniony u nas od [data] na podstawie umowy o pracę [rodzaj, wymiar etatu]. Wynagrodzenie za ostatnie 3 miesiące wyniosło: [mies. 1: brutto / netto], [mies. 2], [mies. 3]. Termin wypłaty: [np. do 10. dnia następnego miesiąca].
2. Kwota możliwa do potrącenia w najbliższym terminie wypłaty: [kwota] (granica [1/2 / 3/5], kwota wolna [kwota] — [uzasadnienie: KUP, PIT-2, PPK, wymiar etatu]).
3. Inne zajęcia: [brak / sygn. …, komornik …, kwota … — zbieg egzekucji, przekazuję do …].
4. Przeszkody w realizacji: [brak / dłużnik na urlopie bezpłatnym / zasiłek wypłaca ZUS…].
Potrącone kwoty będziemy przekazywać na rachunek [nr] w terminach wypłat.

[podpis osoby upoważnionej]
"""},
    "protokol_kontroli_l4": {"nazwa": "Protokół kontroli prawidłowości wykorzystywania zwolnienia", "kiedy": "Tydzień 6 — po reformie 13.04.2026",
                             "tresc": """PROTOKÓŁ KONTROLI PRAWIDŁOWOŚCI WYKORZYSTYWANIA ZWOLNIENIA LEKARSKIEGO

Płatnik: [nazwa]   Upoważnienie nr [..] z dnia [..] dla: [imię i nazwisko kontrolującego/-ych]
Ubezpieczony: [imię i nazwisko]   e-ZLA seria/nr [..] na okres [od–do], adres pobytu z e-ZLA: [..]
Data i godzina kontroli: [..]   Miejsce: [..]

Ustalenia (opis zastanej sytuacji, bez ocen stanu zdrowia):
[np. ubezpieczony obecny / nieobecny; wykonywane czynności; wyjaśnienia ubezpieczonego; dokumenty okazane]

Ocena: [ ] nie stwierdzono nieprawidłowości
       [ ] praca zarobkowa w rozumieniu art. 17 ustawy zasiłkowej: [opis]
       [ ] aktywność niezgodna z celem zwolnienia: [opis]

Pouczenie: ubezpieczony może wnieść uwagi do protokołu w terminie 3 dni od jego otrzymania. W razie sporu sprawę rozstrzyga ZUS w drodze decyzji.

Podpisy kontrolujących: [..]      Podpis ubezpieczonego / adnotacja o odmowie: [..]
Uwagi ubezpieczonego: [..]
"""},
}

# ---------------------------------------------------------------- CHECKLISTA (po etapach)
CHECKLISTA = [
    {"po": "Po tygodniu 0 — warsztat", "punkty": [
        "Mam tabelę 25 wskaźników 2026 z linkami do źródeł",
        "Znajduję przepis w Warsztat → Przepisy i wiem, czym jest tekst ujednolicony w ISAP",
        "Znam 10 narzędzi Warsztatu i wiem, do czego służą PEL i UPL-1 w prawdziwym eZUS/e-Deklaracjach",
        "Mam katalog kadry-praktyka z FIRMA.md i dziennik.md (commit w Git)"]},
    {"po": "Po etapie 1 — prawo pracy (tyg. 1–3)", "punkty": [
        "Piszę ogłoszenie zgodne z jawnością wynagrodzeń i klauzulę RODO",
        "Liczę limity 33/3 i okres próbny; znam treść art. 29 i terminy onboardingu",
        "Układam grafik z zachowaniem 11/35 h i liczę nadgodziny 50/100%",
        "Liczę urlop proporcjonalny i staż z zleceniami (2026); rozpisuję urlopy rodzicielskie"]},
    {"po": "Po etapie 2 — płace (tyg. 4–7)", "punkty": [
        "Liczę brutto→netto ręcznie w 4 wariantach (i potwierdzam w Warsztacie) oraz pełny koszt pracodawcy",
        "Liczę wynagrodzenie urlopowe, ekwiwalent (20,92) i potrącenia komornicze z kwotą wolną",
        "Rozliczam 33 dni, podstawę zasiłku z uzupełnianiem i zasiłek opiekuńczy; znam reformę kontroli L4",
        "Rozliczam zlecenie ze zbiegiem, dzieło (RUD), PPK (2%/1,5%) i zatrudnienie cudzoziemca"]},
    {"po": "Po etapie 3 — ZUS, US, kalendarz (tyg. 8–9)", "punkty": [
        "Składam w symulatorze eZUS/Płatnik komplet ZUA/ZWUA/ZCNA i DRA/RCA/RSA z właściwymi kodami i identyfikatorami (bez błędów weryfikacji)",
        "Robię korektę po 30-krotności z rozliczeniem PIT",
        "Generuję PIT-4R/PIT-11 z kartoteki w Warsztacie, liczę odpis ZFŚS i wpłatę PFRON",
        "Mam kalendarz roczny z 60 terminami i alertami"]},
    {"po": "Po etapie 4 — zakończenie, compliance, projekt (tyg. 10–11)", "punkty": [
        "Piszę wypowiedzenie z przyczyną i pouczeniem, rozwiązanie z art. 52 w terminie 1 miesiąca",
        "Liczę odprawy (limit 72 090) i rozliczam pracownika końcowo; wypełniam świadectwo",
        "Mam procedurę antymobbingową (ustawa z 19.06.2026), sygnalistów i regulamin pracy zdalnej",
        "Przeszedłem audyt 60 pytań i mam teczkę kontrolną; projekt końcowy w repozytorium"]},
]

# ---------------------------------------------------------------- ŚCIĄGA
SCIAGA_WSKAZNIKI = [
    ("Minimalne wynagrodzenie", "4 806 zł (2026) · 4 950 zł (2027)"),
    ("Minimalna stawka godzinowa", "31,40 zł (2026) · 32,30 zł (2027)"),
    ("Składki pracownika", "emerytalna 9,76 · rentowa 1,5 · chorobowa 2,45 = 13,71% · zdrowotna 9% (od podstawy − 13,71%)"),
    ("Składki pracodawcy", "emerytalna 9,76 · rentowa 6,5 · wypadkowa 0,67–3,33 (1,67 do 9 ubezp.) · FP 2,45 · FGŚP 0,10 · FEP 1,5"),
    ("Limit 30-krotności", "282 600 zł (2026)"),
    ("PIT", "12% do 120 000 zł dochodu · 32% ponad · kwota zmniejszająca 300 zł/mies. (PIT-2) · KUP 250/300 · ulga dla młodych 85 528"),
    ("Współczynnik ekwiwalentu", "20,92 (2026, pełny etat)"),
    ("Odpis ZFŚS", "2 943,23 zł (37,5% × 7 848,60) · 75% do 31.05 · reszta do 30.09"),
    ("Odprawa — limit", "72 090 zł (15 × minimalne)"),
    ("Mobbing — min. odszkodowanie", "28 836 zł (6 × minimalne) od 5.11.2026"),
    ("Dodatek nocny", "20% × (4 806 / wymiar miesiąca) za godzinę"),
    ("Wynagrodzenie chorobowe", "33 dni (14 dla 50+) · 80% (100% ciąża, wypadek w drodze) · okres zasiłkowy 182/270"),
    ("Minimalna podstawa zasiłku", "4 147,10 zł (4 806 − 13,71%)"),
    ("PPK", "pracownik 2% (0,5% gdy ≤ 5 767,20) · pracodawca 1,5% · powitalna 250 · roczna 240 · autozapis 1.04.2027"),
    ("Urlop", "20/26 dni · na żądanie 4 · opiekuńczy 5 (bezpłatny) · siła wyższa 2 dni/16 h (50%) · art. 188 2 dni/16 h (100%)"),
    ("Rodzicielskie", "macierzyński 20 tyg. · rodzicielski 41 (9+9 nieprzenoszalne) · ojcowski 2 tyg. do 12 mies. · 81,5% przy wniosku w 21 dni"),
]
SCIAGA_TERMINY = [
    ("7 dni", "ZUA/ZZA, ZWUA, ZCNA, RUD, zmiana danych; informacja art. 29 §3; odpowiedź komornikowi; uwagi do protokołu PIP"),
    ("10. dnia miesiąca", "Najpóźniejszy termin wypłaty wynagrodzenia za miesiąc poprzedni (art. 85)"),
    ("15. / 20.", "ZUS DRA/RCA/RSA + składki: 15. osoby prawne, 20. pozostali, 5. budżet · PPK do 15. · PIT zaliczka i DEK-I-0 do 20. · Wn-D do 25."),
    ("14 dni", "Powiadomienie PUP (Ukraina) · protokół powypadkowy · wniosek o sprostowanie świadectwa · zastrzeżenia do protokołu ZUS · PIT-11 na wniosek po ustaniu"),
    ("21 dni", "Odwołanie do sądu pracy · wniosek o rodzicielski dla 81,5% · wniosek o wychowawczy / elastyczną organizację"),
    ("31 stycznia", "PIT-4R, PIT-8AR, PIT-11 do US · ZUS IWA · informacja o nietworzeniu ZFŚS (< 50) · DEK-R do 20.01"),
    ("koniec lutego", "PIT-11 pracownikom · IFT-1R · IMIR · informacja o autozapisie PPK (2027)"),
    ("31 marca / 20 kwietnia", "ZSWA · decyzja ZUS o stopie wypadkowej (od 1.04)"),
    ("31 maja / 30 września", "75% odpisu ZFŚS · reszta odpisu i urlopy zaległe"),
    ("30 listopada / 31 grudnia", "Stan ubezpieczonych do chorobowego (płatnik zasiłków) · korekta ZFŚS, plan urlopów, limit nadgodzin"),
    ("1 miesiąc", "Art. 52 od uzyskania wiadomości · odwołanie od decyzji ZUS · wypowiedzenie przy stażu ≥ 6 mies."),
    ("5 lat / 10 lat", "Przedawnienie składek ZUS i korekt; dokumentacja podatkowa · akta osobowe (od 2019) i dokumentacja pracownicza"),
]
SCIAGA_ZUS = [
    ("ZUA / ZZA", "zgłoszenie do ubezpieczeń społecznych i zdrowotnego / tylko zdrowotnego"),
    ("ZWUA / ZCNA / ZIUA", "wyrejestrowanie (data = dzień po ustaniu) / członek rodziny / zmiana danych identyfikacyjnych"),
    ("DRA / RCA / RSA / RPA", "deklaracja zbiorcza / składki imienne / przerwy i zasiłki / przychody za inny rok, składniki obok chorobowego"),
    ("Kody tytułu", "01 10 pracownik · 04 11 zleceniobiorca · 05 10 działalność · 05 70 preferencyjne · 05 40 ulga na start · 12 11 wychowawczy · 30 00 po ustaniu"),
    ("Kody przerw RSA", "111 bezpłatny · 121 wychowawczy · 151 usprawiedliwiona bez wynagr. · 152 nieusprawiedliwiona · 313 zasiłek chorobowy · 314 wypadkowy · 312 opiekuńczy · 327/319/325 macierzyński/rodzicielski/ojcowski · 321 rehabilitacyjne · 331 wynagrodzenie chorobowe"),
    ("Identyfikator", "01 MM RRRR pierwotny · 02–39 korekty"),
    ("Z-3 / Z-3a / Z-15A / Z-15B", "zaświadczenie płatnika (pracownik / zleceniobiorca) · wniosek o opiekuńczy (dziecko / inny członek rodziny)"),
    ("ZNp-7 / US-3 / RD-3 / RZS-P / RSR", "świadczenie rehabilitacyjne · A1 · saldo · zwrot nadpłaty · układ ratalny"),
    ("IWA / ZSWA / IMIR", "wypadkowa do 31.01 · prace w szczególnych warunkach do 31.03 · roczna informacja dla ubezpieczonego do 28.02"),
    ("PIT-2 / PIT-4R / PIT-11 / PIT-8AR / IFT-1R", "oświadczenia pracownika · zaliczki roczne · informacja o przychodach · ryczałt · nierezydenci"),
    ("DEK-I-0 / Wn-D / INF-D-P", "PFRON wpłata do 20. · dofinansowanie do 25. · załącznik za pracownika"),
    ("UPL-1 / PEL / e-Doręczenia", "pełnomocnictwo podatkowe · pełnomocnictwo ZUS · skrzynka do pism urzędowych"),
]

LINKI = [
    ["ISAP — teksty ujednolicone ustaw (Kodeks pracy, zasiłkowa, systemowa, PIT)", "https://isap.sejm.gov.pl"],
    ["Dziennik Ustaw", "https://dziennikustaw.gov.pl"],
    ["ZUS — eZUS, Płatnik, poradniki, kody, wskaźniki", "https://www.zus.pl"],
    ["podatki.gov.pl — PIT dla płatników, formularze, objaśnienia MF", "https://www.podatki.gov.pl"],
    ["Państwowa Inspekcja Pracy — poradniki, stanowiska, prawo pracy", "https://www.pip.gov.pl"],
    ["gov.pl — Ministerstwo Rodziny, Pracy i Polityki Społecznej", "https://www.gov.pl/web/rodzina"],
    ["praca.gov.pl — cudzoziemcy, powiadomienia, zezwolenia", "https://www.praca.gov.pl"],
    ["PFRON — wpłaty, dofinansowania, SODiR", "https://www.pfron.org.pl"],
    ["PFR — Moje PPK (pracodawca)", "https://www.mojeppk.pl"],
    ["GUS — przeciętne wynagrodzenie, sprawozdania", "https://stat.gov.pl"],
    ["Rządowy proces legislacyjny — status projektów (UC127, PIP)", "https://legislacja.gov.pl"],
    ["Sąd Najwyższy — orzecznictwo (Izba Pracy)", "https://www.sn.pl"],
]

WSKAZOWKI = [
    "Każda liczba ma źródło. Jeśli nie umiesz podać artykułu albo obwieszczenia — jeszcze jej nie znasz.",
    "Rozróżniaj trzy słowa: obowiązuje, projekt, nie wiem. Zarząd i PIP usłyszą różnicę.",
    "Licz ręcznie zanim zaufasz programowi. Program liczy to, co mu wpisałeś — Ty odpowiadasz za to, co wpisałeś.",
    "Zasada kasowa ZUS i PIT: liczy się miesiąc wypłaty, nie miesiąc, „za który” jest wynagrodzenie.",
    "Termin to data w kalendarzu z alertem 7 dni wcześniej — nie „pamiętam”.",
    "Zanim coś potrącisz z pensji, sprawdź art. 87–91 KP. Zanim czegoś nie wypłacisz — art. 85 i nakaz płacowy PIP.",
    "Dokumentuj decyzje notatką z kazusu: stan faktyczny, pytanie, podstawa, rozstrzygnięcie, ryzyka. Po 3 latach nie będziesz pamiętać dlaczego.",
    "Każdy kazus z zadań przelicz na fikcyjnej firmie — nigdy na prawdziwych danych pracowników.",
    "Z nowelizacją pracujesz w trzech krokach: data wejścia w życie, przepisy przejściowe, co zmienić w regulaminie i programie.",
    "Gdy ZUS, MF i PIP mówią co innego — zapisz wszystkie trzy stanowiska i wybierz bezpieczniejsze dla pracownika.",
    "Lista płac bilansuje się co do grosza: brutto = netto + wszystkie obciążenia pracownika. Jeśli nie — szukaj zaokrągleń.",
    "Dzień bez nauki to nie katastrofa. Dwa tygodnie bez nauki to zapomniane wskaźniki — wróć choć na 20 minut.",
    "Czytaj przepis do końca paragrafu — wyjątek jest zwykle w ostatnim zdaniu.",
    "Ucz się par: wynagrodzenie chorobowe ↔ zasiłek, urlopowe ↔ ekwiwalent, dyskryminacja ↔ nierówne traktowanie, nakaz ↔ wystąpienie.",
]

MOTYWACJA_POWROT = [
    "Dobrze, że wracasz. Przepisy się nie zmieniły aż tak bardzo — a Ty pamiętasz więcej, niż Ci się wydaje.",
    "Nie nadrabiaj wszystkiego naraz. Jedna lekcja, jeden kazus, jeden wpis w dzienniku — i seria rusza od nowa.",
    "Zacznij od ściągi wskaźników: 5 minut powtórki liczb przywraca pewność.",
    "Specjaliści kadr uczą się całe życie — każdy styczeń przynosi nowe stawki. Powrót po przerwie to normalny rytm tego zawodu.",
    "Otwórz ostatni kazus, który rozwiązałeś, i przeczytaj swoją notatkę. To najszybszy sposób, żeby wrócić do kontekstu.",
    "Wybierz dziś najłatwiejsze zadanie z tygodnia. Zaliczone małe zadanie buduje więcej niż nierozpoczęte duże.",
]

POJECIA = {
    "brutto": "Wynagrodzenie przed odliczeniem składek ZUS pracownika, składki zdrowotnej i zaliczki PIT — kwota z umowy.",
    "netto": "To, co pracownik dostaje na konto: brutto minus składki społeczne (13,71%), zdrowotna (9%), zaliczka PIT i wpłata PPK pracownika.",
    "koszt pracodawcy": "Brutto plus składki finansowane przez pracodawcę (emerytalna 9,76, rentowa 6,5, wypadkowa, FP 2,45, FGŚP 0,10) i PPK 1,5% — ok. 1,21–1,25 × brutto.",
    "podstawa wymiaru składek": "Przychód ze stosunku pracy bez wyłączeń z rozporządzenia składkowego (odprawy, ekwiwalenty, ZFŚS…), od którego liczy się składki.",
    "limit 30-krotności": "Roczny limit podstawy składek emerytalnej i rentowej (2026: 282 600 zł); po przekroczeniu nalicza się tylko chorobową, wypadkową, zdrowotną, FP/FGŚP.",
    "płatnik": "Podmiot zobowiązany do obliczenia, pobrania i wpłacenia składek (płatnik składek — ZUS) lub zaliczek (płatnik podatku — US); w kadrach to pracodawca.",
    "płatnik zasiłków": "Pracodawca, który sam wypłaca zasiłki, bo na 30 listopada poprzedniego roku zgłaszał do chorobowego ponad 20 osób; mniejsi — zasiłki wypłaca ZUS.",
    "zasada kasowa": "Przychód i składki rozlicza się w miesiącu wypłaty (postawienia do dyspozycji), nie w miesiącu, za który wynagrodzenie przysługuje.",
    "wymiar czasu pracy": "Liczba godzin do przepracowania w miesiącu/okresie: tygodnie × 40 + dni pon–pt × 8 − 8 za każde święto w dniu innym niż niedziela (art. 130 KP).",
    "okres rozliczeniowy": "Okres (do 4 mies., wyjątkowo 12), w którym przeciętnie 40 h tygodniowo musi się zbilansować; po jego końcu rozliczasz nadgodziny średniotygodniowe.",
    "doba pracownicza": "24 kolejne godziny od rozpoczęcia pracy wg rozkładu; ponowne rozpoczęcie pracy w tej dobie to nadgodziny (poza ruchomym czasem pracy).",
    "system równoważny": "System czasu pracy z dobowym wymiarem do 12 h (16/24 w szczególnych przypadkach), równoważonym krótszymi dniami lub dniami wolnymi w okresie rozliczeniowym.",
    "wynagrodzenie chorobowe": "Płatne przez pracodawcę za pierwsze 33 (14 dla 50+) dni niezdolności w roku — 80%, bez składek społecznych, ze zdrowotną i PIT (art. 92 KP).",
    "zasiłek chorobowy": "Świadczenie z ubezpieczenia chorobowego od 34./15. dnia niezdolności — 80% (100% ciąża, wypadek w drodze), bez składek, z PIT; okres zasiłkowy 182/270 dni.",
    "podstawa wymiaru zasiłku": "Przeciętne miesięczne wynagrodzenie (po odliczeniu 13,71%) wypłacone za 12 miesięcy poprzedzających niezdolność, z uzupełnianiem niepełnych miesięcy.",
    "okres zasiłkowy": "Maksymalny czas pobierania zasiłku chorobowego: 182 dni (270 — ciąża, gruźlica); przerwa krótsza niż 60 dni nie otwiera nowego okresu.",
    "e-ZLA": "Elektroniczne zwolnienie lekarskie wystawiane przez lekarza w systemie ZUS; płatnik widzi je w eZUS, pracownik nie dostarcza papieru.",
    "ekwiwalent za urlop": "Pieniądze za niewykorzystany urlop przy ustaniu zatrudnienia: podstawa / współczynnik (20,92 w 2026) / 8 × godziny urlopu.",
    "współczynnik ekwiwalentu": "(365 − niedziele − soboty − święta w dni inne niż niedziela) / 12 — w 2026: 20,92; dla niepełnego etatu proporcjonalnie.",
    "kwota wolna od potrąceń": "Część wynagrodzenia, której komornik nie może zająć: minimalne wynagrodzenie netto (100% — inne długi, 75% zaliczki, 90% kary); brak przy alimentach.",
    "PIT-2": "Formularz oświadczeń pracownika: kwota zmniejszająca (300/150/100 zł), podwyższone KUP, ulgi, wspólne rozliczenie, niepobieranie zaliczek.",
    "KUP": "Koszty uzyskania przychodu: 250 zł (300 dojeżdżający) miesięcznie dla pracownika, 20% zlecenia, 50% prawa autorskie — odejmowane od przychodu przed opodatkowaniem.",
    "ulga dla młodych": "Zwolnienie z PIT przychodów ze stosunku pracy i zleceń do 85 528 zł rocznie dla osób do 26. roku życia; składki ZUS normalnie.",
    "PPK": "Pracownicze Plany Kapitałowe — prywatne oszczędzanie: 2% pracownik (z netto), 1,5% pracodawca (przychód do PIT, bez ZUS), 250 + 240 zł od państwa; autozapis co 4 lata.",
    "ZFŚS": "Zakładowy Fundusz Świadczeń Socjalnych — obowiązkowy od 50 etatów; odpis 2 943,23 zł (2026); świadczenia wg kryterium socjalnego, bez ZUS i PIT do 1 000 zł.",
    "kryterium socjalne": "Sytuacja życiowa, rodzinna i materialna pracownika (dochód na osobę) — jedyna dopuszczalna podstawa różnicowania świadczeń z ZFŚS.",
    "zbieg tytułów": "Sytuacja, gdy osoba ma kilka tytułów do ubezpieczeń (etat + zlecenie, dwa zlecenia); ustawa wskazuje, od którego składki są obowiązkowe, a od którego tylko zdrowotna.",
    "RUD": "Zgłoszenie do ZUS umowy o dzieło zawartej z osobą niebędącą pracownikiem — w 7 dni od zawarcia, przez eZUS.",
    "art. 22 KP": "Definicja stosunku pracy: praca pod kierownictwem, w miejscu i czasie wyznaczonym, osobiście, za wynagrodzeniem — niezależnie od nazwy umowy (B2B, zlecenie).",
    "akta osobowe": "Dokumentacja pracownika w 5 częściach: A (rekrutacja), B (przebieg), C (ustanie), D (kary), E (trzeźwość); 10 lat po ustaniu (od 2019).",
    "świadectwo pracy": "Dokument wydawany w dniu ustania zatrudnienia: okres, stanowiska, tryb rozwiązania, urlop, nieobecności, zajęcia — bez przyczyny i ocen.",
    "odprawa": "Świadczenie przy rozwiązaniu z przyczyn niedotyczących pracownika (1/2/3-miesięczne, do 72 090 zł; bez ZUS, z PIT) — pracodawca ≥ 20 pracowników; także emerytalna i pośmiertna.",
    "mobbing": "Od 5.11.2026: uporczywe (powtarzalne lub długotrwałe) nękanie pracownika — poniżanie, izolowanie, zastraszanie…; odszkodowanie min. 6× minimalne wynagrodzenie.",
    "dyskryminacja": "Gorsze traktowanie ze względu na cechę (płeć, wiek, niepełnosprawność…) — bezpośrednie lub pośrednie; odszkodowanie nie niższe niż minimalne wynagrodzenie.",
    "jawność wynagrodzeń": "Od 24.12.2025: widełki dla kandydata i zakaz pytania o historię zarobków; dyrektywa 2023/970 (raporty luki płacowej, prawo do informacji) — projekt UC127.",
    "luka płacowa": "Różnica średnich/median wynagrodzeń kobiet i mężczyzn w tej samej kategorii pracy: (M − K)/M × 100%; ≥ 5% nieuzasadnione → wspólna ocena wynagrodzeń.",
    "sygnalista": "Osoba zgłaszająca naruszenie prawa w kontekście pracy, chroniona przed odwetem (ustawa z 14.06.2024); procedura wewnętrzna od 50 osób.",
    "nakaz płacowy": "Decyzja inspektora PIP nakazująca wypłatę należnego wynagrodzenia lub świadczenia — podlega natychmiastowemu wykonaniu.",
    "IWA": "Roczna informacja do ZUS (do 31.01) o wypadkach i zatrudnieniu — po 3 latach ZUS ustala indywidualną stopę składki wypadkowej.",
    "mikrorachunek": "Indywidualny rachunek podatkowy firmy (NIP) do wpłat zaliczek PIT, CIT i VAT; składki ZUS idą na NRS.",
    "NRS": "Numer rachunku składkowego — indywidualny rachunek płatnika w ZUS, na który jednym przelewem wpłaca wszystkie składki.",
    "wartościowanie stanowisk": "Metoda porównania stanowisk wg umiejętności, wysiłku, odpowiedzialności i warunków pracy — podstawa kategorii „pracy tej samej wartości” i siatki płac.",
}

BLEDY = {
    "Płatnik odrzucił dokument": {"co": "Weryfikacja w Płatniku zgłasza błąd krytyczny (czerwony) — najczęściej: zły kod tytułu, data poza zakresem zgłoszenia, brak zgłoszenia osoby, identyfikator kompletu już użyty, suma RCA ≠ DRA.",
                                  "pytanie": "Który dokument i jaki numer błędu? Czy osoba jest zgłoszona (ZUA) na dzień, którego dotyczy raport? Czy identyfikator (01/02…) jest właściwy dla tego miesiąca?"},
    "netto się nie zgadza": {"co": "Lista płac nie bilansuje się: różnica zwykle wynika z zaokrągleń (składki osobno do grosza, podstawa PIT i zaliczka do złotego), złej podstawy zdrowotnej (po odliczeniu społecznych) albo nieuwzględnienia PPK pracodawcy w PIT.",
                             "pytanie": "Policz od nowa w kolejności: brutto → 3 składki osobno → zdrowotna od (brutto − składki) → podstawa PIT zaokrąglona → zaliczka − 300 → PPK. Na którym kroku różnica się pojawia?"},
    "nadpłata składek": {"co": "Zapłaciłeś więcej niż wynika z korekty (np. 30-krotność, student na zleceniu). Nadpłatę ZUS zalicza na przyszłe składki lub zwraca na wniosek RZS-P; część pracownika oddajesz pracownikowi i rozliczasz PIT w miesiącu zwrotu.",
                         "pytanie": "Czy złożyłeś komplet korygujący (02 MM RRRR) z DRA? Która część nadpłaty jest pracownika (11,26% / 13,71%), a która pracodawcy?"},
    "niedopłata składek": {"co": "Składki zapłacone za nisko lub po terminie — ZUS nalicza odsetki (nie, gdy ≤ 1% minimalnej) i zalicza wpłaty na najstarsze zaległości, co „przesuwa” kolejne miesiące.",
                           "pytanie": "Za który miesiąc i z jakiego powodu (zbieg, benefit, dzieło=zlecenie)? Policz odsetki kalkulatorem ZUS i sprawdź, czy wpłata trafiła na NRS."},
    "ZUS odrzucił": {"co": "ZUS nie przyjął dokumentu lub wezwał do korekty — zawiadomienie przychodzi do eZUS (Dokumenty i wiadomości). Masz 7 dni na korektę od zawiadomienia.",
                     "pytanie": "Co dokładnie jest w zawiadomieniu ZUS? Czy chodzi o dokument zgłoszeniowy (ZUA/ZWUA) czy rozliczeniowy (RCA/RSA)?"},
    "brak e-ZLA": {"co": "Pracownik twierdzi, że ma zwolnienie, a nie widzisz go w eZUS — lekarz mógł wystawić papierowe (awaria), wpisać zły NIP płatnika lub zwolnienie jeszcze nie spłynęło.",
                   "pytanie": "Czy pracownik ma wydruk/numer ZLA? Sprawdź w eZUS po PESEL w zakładce Zaświadczenia lekarskie i zweryfikuj NIP płatnika na zwolnieniu."},
    "komornik": {"co": "Zajęcie wynagrodzenia wymaga odpowiedzi w 7 dni (art. 882 KPC) i potrącania od chwili doręczenia w granicach 1/2 (3/5 alimenty) z kwotą wolną. Brak odpowiedzi — grzywna do 5 000 zł.",
                 "pytanie": "Czy to alimenty czy inne należności? Jaką kwotę wolną ma ten pracownik (KUP, PIT-2, PPK, etat)? Czy są inne zajęcia (zbieg)?"},
    "PIP": {"co": "Kontrola PIP przychodzi bez zapowiedzi. Udostępniasz dokumenty, notujesz zakres, nie podpisujesz oświadczeń „na szybko”, zastrzeżenia do protokołu w 7 dni.",
            "pytanie": "Jaki obszar kontroluje inspektor i jakie dokumenty poprosił? Czy masz ewidencję czasu pracy z godzinami rozpoczęcia i zakończenia za 3 lata?"},
    "PIT-11 błędny": {"co": "Błąd w PIT-11 (przychód, KUP, zaliczka, składki) poprawiasz korektą — nowy PIT-11 z zaznaczeniem „korekta” do US i do podatnika, nawet po latach (do przedawnienia).",
                      "pytanie": "Co jest błędne i czy wpływa na zeznanie pracownika? Czy suma zaliczek nadal zgadza się z PIT-4R i wpłatami na mikrorachunek?"},
    "30-krotność": {"co": "Przekroczenie limitu 282 600 zł (2026): od nadwyżki nie naliczasz emerytalnej i rentowej; przy spóźnionym wykryciu — korekta, zwrot części pracownika, wzrost zdrowotnej i PIT.",
                    "pytanie": "W którym miesiącu podstawa narastająco przekroczyła limit? Czy pracownik ma innego płatnika (oświadczenie)?"},
    "ekwiwalent": {"co": "Ekwiwalent liczysz: podstawa (stałe + średnia zmiennych z 3 mies. + 1/12 rocznych) / 20,92 / 8 × godziny; wypłata w terminie wypłaty wynagrodzenia (10 dni od ustania, gdy termin wypłaty przypada przed rozwiązaniem).",
                   "pytanie": "Ile godzin urlopu zostało (wg planu pracownika, nie 8 h zawsze)? Jaki współczynnik dla etatu pracownika?"},
    "świadectwo": {"co": "Świadectwo wydajesz w dniu ustania; błędy poprawiasz na wniosek w 7 dni; nie wpisujesz przyczyny ani ocen; kopia do akt C.",
                   "pytanie": "Która pozycja jest kwestionowana: tryb/podstawa, urlop (dni i godziny), okresy nieskładkowe czy zajęcie komornicze?"},
}

PYTANIA_REKRUTACYJNE = [
    ("płace", "Jak policzysz netto z brutto 6 000 zł dla pracownika z PIT-2 i KUP 250? Podaj kolejność kroków.", "Składki 13,71% osobno → zdrowotna 9% od (6 000 − 822,60) → podstawa PIT = 6 000 − 822,60 − 250 → ×12% − 300 → zaokrąglenia → netto ≈ 4 420."),
    ("płace", "Czym różni się wynagrodzenie chorobowe od zasiłku chorobowego?", "Chorobowe — pracodawca, 33/14 dni, bez składek społecznych, ze zdrowotną; zasiłek — ubezpieczenie chorobowe od 34./15. dnia, bez składek, z PIT; oba 80% podstawy z 12 miesięcy."),
    ("płace", "Co to jest limit 30-krotności i co się dzieje po jego przekroczeniu?", "282 600 zł w 2026 — podstawa roczna składek emerytalno-rentowych; po przekroczeniu naliczasz tylko chorobową, wypadkową, zdrowotną, FP/FGŚP; przy błędzie — korekta i zwrot."),
    ("płace", "Jak liczysz ekwiwalent za urlop w 2026 r.?", "Podstawa (stałe + średnia zmiennych 3 mies. + 1/12 rocznych) / współczynnik 20,92 / 8 h × godziny niewykorzystanego urlopu; wypłata w terminie wypłaty wynagrodzenia."),
    ("prawo pracy", "Jakie są limity umów na czas określony i wyjątki?", "33 miesiące i 3 umowy; wyjątki: zastępstwo, prace dorywcze/sezonowe, kadencja, obiektywne przyczyny (zapis + PIP w 5 dni)."),
    ("prawo pracy", "Pracownik na zwolnieniu lekarskim — czy możesz go zwolnić?", "Art. 41 chroni przed wypowiedzeniem w czasie usprawiedliwionej nieobecności; po upływie okresów z art. 53 — rozwiązanie bez wypowiedzenia; art. 52 dopuszczalny zawsze (1 miesiąc)."),
    ("prawo pracy", "Co musi zawierać wypowiedzenie umowy na czas określony od 2023 r.?", "Pismo, konkretna i prawdziwa przyczyna, pouczenie o odwołaniu do sądu w 21 dni, konsultacja związkowa (jeśli dotyczy) — jak przy umowie na czas nieokreślony."),
    ("czas pracy", "Jak rozliczysz pracę w sobotę (dzień wolny z 5-dniowego tygodnia)?", "Najpierw inny dzień wolny do końca okresu rozliczeniowego; brak — nadgodziny średniotygodniowe z dodatkiem 100% (ponad 8 h w tym dniu — dobowe 50%)."),
    ("czas pracy", "Ile wynosi dodatek za pracę w nocy i jak go liczysz?", "20% stawki godzinowej z minimalnego wynagrodzenia: 4 806 / wymiar danego miesiąca × 20% za każdą godzinę w porze nocnej."),
    ("ZUS", "Jakie dokumenty składasz co miesiąc do ZUS i w jakim terminie?", "DRA + RCA + RSA (+ RPA, gdy przychód za inny rok itp.) do 15. (osoby prawne) lub 20. (pozostali); jedna wpłata na NRS; zasada kasowa."),
    ("ZUS", "Zleceniobiorca ma etat 5 000 zł u innego pracodawcy. Jakie składki od zlecenia?", "Tylko zdrowotna (etat ≥ minimalnej); gdyby etat < 4 806 — pełne składki; zlecenie z własnym pracodawcą — jak etat."),
    ("ZUS", "Jak dokumentuje się staż ze zlecenia po nowelizacji 2026?", "Zaświadczeniem ZUS o okresach ubezpieczenia (eZUS); obecni pracownicy mają 24 miesiące; nie wlicza się dzieła; okres wypowiedzenia — tylko zlecenia u tego pracodawcy."),
    ("zasiłki", "Pracownik chorował 20 dni w marcu i 15 dni w czerwcu. Jak liczysz 33 dni i okres zasiłkowy?", "33 dni w roku kalendarzowym: marzec 20 + czerwiec 13 chorobowe, od 14. dnia czerwca zasiłek; przerwa > 60 dni → nowy okres zasiłkowy, ale pula 33 jest roczna."),
    ("compliance", "Co zmieniła nowelizacja mobbingu z 2026 r. i co musi zrobić pracodawca?", "Definicja: uporczywe nękanie bez wymogu zamiaru i skutku; odszkodowanie min. 6× minimalne bez rozwiązywania umowy; zasady przeciwdziałania w regulaminie/obwieszczeniu do 5.05.2027."),
    ("compliance", "Co już obowiązuje z jawności wynagrodzeń, a co jest projektem?", "Obowiązuje od 24.12.2025: widełki dla kandydata, zakaz pytania o historię zarobków, neutralne ogłoszenia; projekt UC127 (dyrektywa 2023/970): prawo do informacji, raporty luki, zakaz klauzul poufności."),
    ("kontrola", "Jak przygotujesz firmę do kontroli PIP?", "Teczka kontrolna (regulaminy, ewidencja z godzinami, listy płac, umowy cywilnoprawne, BHP), książka kontroli, osoba kontaktowa, audyt wewnętrzny; podczas kontroli — kopie, notatki, zastrzeżenia w 7 dni."),
]
