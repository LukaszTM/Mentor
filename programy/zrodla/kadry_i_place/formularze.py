# -*- coding: utf-8 -*-
"""Formularze — ćwiczenia na wzorach prawdziwych druków (Warsztat → Formularze): uczeń wypełnia pola o numerach z urzędowego wzoru,
Mentor sprawdza każde pole (moduł odpowiedzi.py). Numeracja bloków i pól: ZUS ZUA, ZWUA, RCA — wg wzorów ZUS; PIT-2 (wersja 9) i PIT-11 (wersja 29) — wg wzorów MF;
świadectwo pracy — wg pomocniczego wzoru z rozporządzenia MRPiPS (t.j. Dz.U. 2024 poz. 1016). Dane osób — fikcyjna firma AGRO-MLEKO (FIRMA.md)."""

from odpowiedzi_cw import TN, bl, da, kw, li, tx, wy

WYP = ["wypełniam", "nie wypełniam"]
KW_ZM = ["1/12 (300 zł)", "1/24 (150 zł)", "1/36 (100 zł)", "nie wypełniam"]
PODST = ["art. 30 §1 pkt 1 KP — porozumienie stron", "art. 30 §1 pkt 2 KP — wypowiedzenie", "art. 30 §1 pkt 3 KP — bez wypowiedzenia", "art. 30 §1 pkt 4 KP — upływ czasu"]
# kwadraty poz. 28 urzędowego wzoru PIT-11(29): 1 — z jednego stosunku pracy, 2 — z więcej niż jednego, 3 i 4 — to samo z kosztami podwyższonymi (dojazd z innej miejscowości)
KUP_PIT11 = ["1 — jeden stosunek pracy", "2 — kilka stosunków pracy", "3 — jeden, podwyższone", "4 — kilka, podwyższone"]


def s(tytul, *pola):
    return {"tytul": tytul, "pola": list(pola)}


FORMULARZE = [
    # ------------------------------------------------------------------ ZUS ZUA
    {"id": "zua_kowalczyk", "nazwa": "ZUS ZUA — zgłoszenie nowej pracownicy", "wzor": "ZUS ZUA (bloki I–XV)", "lekcja": "zus_zgloszenia",
     "scenariusz": "Anna Kowalczyk (ur. 14.05.1991, PESEL 91051410003, obywatelstwo polskie) zaczyna pracę 1.10.2026 na umowie o pracę (pełny etat, 6 000 zł). "
                   "Nie ma prawa do emerytury ani renty i nie ma orzeczenia o niepełnosprawności. Mieszka w województwie mazowieckim. Płatnik: AGRO-MLEKO sp. z o.o. "
                   "Wypełnij ZUA w pierwszym dniu pracy i ustal ostatni dzień na jego przekazanie.",
     "sekcje": [
         s("I. Dane organizacyjne", wy("i01", "Rodzaj zgłoszenia", ["01 — zgłoszenie do ubezpieczeń", "02 — zgłoszenie zmiany / korekty danych"], "01 — zgłoszenie do ubezpieczeń")),
         s("II. Dane identyfikacyjne płatnika składek", tx("ii06", "06. Nazwa skrócona płatnika", ["AGRO-MLEKO", "AGRO-MLEKO sp. z o.o.", "AGRO MLEKO"])),
         s("III. Dane identyfikacyjne osoby zgłaszanej", tx("iii01", "01. PESEL", "91051410003"), tx("iii05", "05. Nazwisko", "Kowalczyk"), tx("iii06", "06. Imię pierwsze", "Anna"),
           da("iii07", "07. Data urodzenia", "1991-05-14")),
         s("IV. Dane ewidencyjne osoby zgłaszanej", tx("iv03", "03. Obywatelstwo", ["polskie", "PL", "Polska"]), wy("iv04", "04. Płeć", ["K", "M"], "K")),
         s("V. Tytuł ubezpieczenia", tx("v01", "01. Kod tytułu ubezpieczenia (6 cyfr)", "011000",
                                        bledy=[bl("0110", "kod ma 6 znaków: 4 cyfry tytułu + prawo do emerytury/renty + stopień niepełnosprawności"),
                                               bl("011002", "ostatnia cyfra 2 oznacza umiarkowany stopień niepełnosprawności — Anna nie ma orzeczenia")])),
         s("VI. Dane o obowiązkowych ubezpieczeniach społecznych", da("vi01", "01. Data powstania obowiązku ubezpieczeń", "2026-10-01"),
           wy("vi02", "02. Emerytalne", TN, "tak"), wy("vi03", "03. Rentowe", TN, "tak"), wy("vi04", "04. Chorobowe", TN, "tak"), wy("vi05", "05. Wypadkowe", TN, "tak")),
         s("VII. Dane o obowiązkowym ubezpieczeniu zdrowotnym", da("vii01", "01. Data powstania obowiązku ubezpieczenia zdrowotnego", "2026-10-01"),
           tx("vii02", "02. Kod oddziału NFZ", "07R", bledy=[bl("07", "kod oddziału NFZ ma 3 znaki: dwie cyfry i literę R")])),
         s("VIII–IX. Ubezpieczenia dobrowolne", wy("viii", "Czy wypełniasz bloki VIII–IX (ubezpieczenia dobrowolne)?", TN, "nie")),
         s("XIV. Oświadczenie płatnika i termin", da("xiv01", "01. Data wypełnienia", "2026-10-01"),
           da("termin", "Ostatni dzień na przekazanie ZUA do ZUS", "2026-10-08", bledy=[bl("2026-10-07", "7 dni liczysz od dnia powstania obowiązku: 1.10 + 7 dni = 8.10")])),
     ],
     "po": "W prawdziwej firmie: program kadrowy eksportuje ZUA do Płatnika (plik KEDU) albo wypełniasz go w ePłatniku na eZUS; po wysyłce archiwizujesz numer UPP. "
           "To samo zgłoszenie „wyślij” w Warsztat → eZUS / Płatnik → Dokument zgłoszeniowy."},
    # ------------------------------------------------------------------ ZUS ZWUA
    {"id": "zwua_mazur", "nazwa": "ZUS ZWUA — wyrejestrowanie po wypowiedzeniu przez pracodawcę", "wzor": "ZUS ZWUA (bloki I–VIII)", "lekcja": "rozwiazanie_umowy",
     "scenariusz": "Halina Mazur (PESEL 72080310047, w firmie od 1.04.2009, kod tytułu 01 10 00) dostała 17.11.2026 wypowiedzenie umowy na czas nieokreślony złożone przez pracodawcę "
                   "(okres 3 miesiące, art. 30 §1 pkt 2 KP). Wypełnij ZWUA razem z blokiem V i ustal termin przekazania.",
     "sekcje": [
         s("I. Dane organizacyjne", wy("i01", "Rodzaj dokumentu", ["01 — wyrejestrowanie", "02 — korekta wyrejestrowania"], "01 — wyrejestrowanie")),
         s("III. Dane identyfikacyjne osoby wyrejestrowywanej", tx("iii01", "01. PESEL", "72080310047"), tx("iii05", "05. Nazwisko", "Mazur")),
         s("IV. Wyrejestrowanie z ubezpieczeń", tx("iv01", "01. Kod tytułu ubezpieczenia", "011000"),
           da("iv02", "02. Data wyrejestrowania", "2027-03-01", bledy=[bl("2027-02-28", "data wyrejestrowania to dzień NASTĘPNY po ostatnim dniu ubezpieczenia")]),
           tx("iv03", "03. Kod przyczyny wyrejestrowania", "100")),
         s("V. Rozwiązanie / wygaśnięcie stosunku pracy", da("v01", "01. Data rozwiązania stosunku pracy", "2027-02-28"),
           tx("v02", "02. Kod trybu rozwiązania", "23R", bledy=[bl("22R", "22R to porozumienie stron; wypowiedzenie złożone przez pracodawcę ma kod 23R"),
                                                              bl("24R", "24R to wypowiedzenie złożone przez pracownika")]),
           tx("v03", "03. Kod podstawy prawnej", "403"), wy("v05", "05. Strona inicjująca", ["1 — pracownik", "2 — pracodawca"], "2 — pracodawca")),
         s("Termin", da("termin", "Ostatni dzień na przekazanie ZWUA", "2027-03-08", bledy=[bl("2027-03-07", "7.03.2027 to niedziela — termin przesuwa się na poniedziałek")])),
     ],
     "po": "Kody z bloku V muszą się zgadzać ze świadectwem pracy (ust. 4). Członkowie rodziny zgłoszeni do ubezpieczenia zdrowotnego wyrejestrowują się automatycznie."},
    {"id": "zwua_art52", "nazwa": "ZUS ZWUA — rozwiązanie bez wypowiedzenia (art. 52)", "wzor": "ZUS ZWUA (bloki I–VIII)", "lekcja": "rozwiazanie_umowy",
     "scenariusz": "Pracownikowi magazynu (kod tytułu 01 10 00) doręczono w czwartek 3.12.2026 oświadczenie o rozwiązaniu umowy bez wypowiedzenia z jego winy (art. 52 §1 pkt 1 KP). "
                   "Stosunek pracy ustaje z dniem doręczenia. Wypełnij bloki IV i V.",
     "sekcje": [
         s("IV. Wyrejestrowanie z ubezpieczeń", da("iv02", "02. Data wyrejestrowania", "2026-12-04"), tx("iv03", "03. Kod przyczyny wyrejestrowania", "100")),
         s("V. Rozwiązanie / wygaśnięcie stosunku pracy", da("v01", "01. Data rozwiązania stosunku pracy", "2026-12-03"),
           tx("v02", "02. Kod trybu rozwiązania", "25R", bledy=[bl("23R", "23R to wypowiedzenie złożone przez pracodawcę; rozwiązanie bez wypowiedzenia przez pracodawcę ma kod 25R")]),
           tx("v03", "03. Kod podstawy prawnej", "404"), wy("v05", "05. Strona inicjująca", ["1 — pracownik", "2 — pracodawca"], "2 — pracodawca")),
         s("Termin", da("termin", "Ostatni dzień na przekazanie ZWUA", "2026-12-10")),
     ],
     "po": "Świadectwo pracy wydajesz w dniu ustania (3.12), z podstawą art. 30 §1 pkt 3 w zw. z art. 52 §1 pkt 1 KP — bez opisu przyczyny."},
    # ------------------------------------------------------------------ ZUS RCA
    {"id": "rca_zielinski", "nazwa": "ZUS RCA — imienny raport o składkach", "wzor": "ZUS RCA (bloki I–V; III.B i III.C)", "lekcja": "zus_rozliczenia",
     "scenariusz": "Marek Zieliński (pełny etat, kod 01 10 00, uczestnik PPK 2% / 1,5%) dostał za październik 2026 pensję 5 400 zł brutto, wypłaconą 10.11.2026. "
                   "Stopa wypadkowa firmy: 1,20%. Wypełnij jego RCA w komplecie, do którego trafia ta wypłata.",
     "sekcje": [
         s("I. Dane organizacyjne", tx("i01", "01. Identyfikator raportu (numer — miesiąc — rok)", "01 11 2026",
                                       bledy=[bl("01 10 2026", "zasada kasowa: pensja za październik wypłacona 10.11 trafia do kompletu za LISTOPAD")])),
         s("III.B. Zestawienie należnych składek na ubezpieczenia społeczne", tx("b01", "01. Kod tytułu ubezpieczenia", "011000"),
           tx("b03", "03. Wymiar czasu pracy", ["1/1", "001/001"]), kw("b04", "04. Podstawa wymiaru — emerytalne i rentowe", 5400), kw("b05", "05. Podstawa wymiaru — chorobowe", 5400),
           kw("b06", "06. Podstawa wymiaru — wypadkowe", 5400), kw("b07", "07. Emerytalna — ubezpieczony", 527.04), kw("b08", "08. Rentowe — ubezpieczony", 81.00),
           kw("b09", "09. Chorobowa — ubezpieczony", 132.30), kw("b11", "11. Emerytalna — płatnik", 527.04),
           kw("b12", "12. Rentowe — płatnik", 351.00, bledy=[bl(81.00, "płatnik finansuje 6,5% składki rentowej, ubezpieczony 1,5%")]),
           kw("b14", "14. Wypadkowa — płatnik", 64.80, bledy=[bl(90.18, "to 1,67% — AGRO-MLEKO ma stopę 1,20% ustaloną przez ZUS")]),
           kw("b28", "28. Wpłata na PPK finansowana przez płatnika", 81.00, bledy=[bl(108.00, "108,00 to wpłata uczestnika (2%); w RCA wykazujesz tylko wpłatę płatnika (1,5%)")]),
           kw("b29", "29. Łączna kwota składek (suma pól 07–26)", 1683.18)),
         s("III.C. Zestawienie należnych składek na ubezpieczenie zdrowotne", kw("c01", "01. Podstawa wymiaru składki zdrowotnej", 4659.66,
                                                                               bledy=[bl(5400, "podstawa zdrowotnej to brutto pomniejszone o składki społeczne ubezpieczonego")]),
           kw("c04", "04. Składka finansowana przez ubezpieczonego", 419.37)),
     ],
     "po": "FP i FGŚP nie ma w RCA — są w deklaracji DRA. Komplet za listopad (DRA + RCA + RSA) wysyłasz do 15.12.2026 — zrób to w Warsztat → eZUS / Płatnik → Rozliczenie."},
    # ------------------------------------------------------------------ ZUS RSA
    {"id": "rsa_zielinski", "nazwa": "ZUS RSA — wynagrodzenie chorobowe i zasiłek", "wzor": "ZUS RSA (blok III.B — świadczenia i przerwy)", "lekcja": "chorobowe_podstawy",
     "scenariusz": "Marek Zieliński chorował 16–30.11.2026 (15 dni). Wcześniej w 2026 r. wykorzystał 24 dni z puli 33. Stawka dzienna 80%: 133,46 zł. "
                   "Świadczenia wypłacono z listą płac 10.12.2026. Wypełnij dwa wiersze RSA.",
     "sekcje": [
         s("I. Dane organizacyjne", tx("i01", "01. Identyfikator raportu", "01 12 2026", bledy=[bl("01 11 2026", "świadczenia wykazujesz w komplecie za miesiąc WYPŁATY — tu grudzień")])),
         s("III.B. Wiersz 1 — wynagrodzenie za czas choroby", tx("w1kod", "Kod świadczenia / przerwy", "331"), da("w1od", "Okres od", "2026-11-16"), da("w1do", "Okres do", "2026-11-24"),
           li("w1dni", "Liczba dni", 9), kw("w1kw", "Kwota", 1201.14)),
         s("III.B. Wiersz 2 — zasiłek chorobowy", tx("w2kod", "Kod świadczenia / przerwy", "313"), da("w2od", "Okres od", "2026-11-25"), da("w2do", "Okres do", "2026-11-30"),
           li("w2dni", "Liczba dni", 6), kw("w2kw", "Kwota", 800.76)),
         s("Rozliczenie w DRA", wy("odl331", "Czy kwotę z wiersza 331 odliczasz od składek w DRA?", TN, "nie"), wy("odl313", "Czy kwotę z wiersza 313 odliczasz od składek w DRA?", TN, "tak")),
     ],
     "po": "Wynagrodzenie chorobowe (331) finansuje pracodawca — w RSA jest tylko informacją. Zasiłek (313) wypłacasz w imieniu ZUS i odliczasz w DRA."},
    # ------------------------------------------------------------------ PIT-2
    {"id": "pit2_mazur", "nazwa": "PIT-2 — oświadczenia pracownicy (dojazd z innej miejscowości)", "wzor": "PIT-2 (wersja 9), części C–K", "lekcja": "zaliczka_pit",
     "scenariusz": "Halina Mazur pracuje tylko w AGRO-MLEKO, mieszka w innej miejscowości niż zakład i nie dostaje dodatku za rozłąkę. Nie korzysta z ulg (powrót, 4+, senior), "
                   "nie ma kosztów autorskich i nie chce rozliczać się z mężem już w trakcie roku. Składa PIT-2 w czwartek 12.11.2026. Zdecyduj, które części wypełnia.",
     "sekcje": [
         s("C. Kwota zmniejszająca podatek", wy("c6", "Poz. 6 — pomniejszenie zaliczki", KW_ZM, "1/12 (300 zł)")),
         s("D. Oświadczenie dla płatnika z art. 42e", wy("d8", "Poz. 8", WYP, "nie wypełniam")),
         s("E. Wspólne rozliczenie / samotny rodzic", wy("e10", "Poz. 10", WYP, "nie wypełniam")),
         s("F. Podwyższone koszty uzyskania przychodów", wy("f12", "Poz. 12 — miejsce zamieszkania poza miejscowością zakładu pracy", WYP, "wypełniam")),
         s("G. Zwolnienia (ulga na powrót, 4+, senior)", wy("g14", "Poz. 14", WYP, "nie wypełniam")),
         s("H. Rezygnacja z ulgi dla młodych / kosztów pracowniczych", wy("h16", "Poz. 16", WYP, "nie wypełniam")),
         s("J. Wniosek o niepobieranie zaliczek", wy("j20", "Poz. 20", WYP, "nie wypełniam")),
         s("Skutek w liście płac", kw("kup", "Miesięczne koszty uzyskania (zł)", 300), kw("zm", "Miesięczna kwota zmniejszająca (zł)", 300),
           wy("od", "Od której wypłaty najpóźniej stosujesz to oświadczenie?", ["10.11.2026", "10.12.2026", "8.01.2027"], "10.12.2026")),
     ],
     "po": "PIT-2 trafia do części B akt osobowych. Po ustaniu zatrudnienia pomijasz oświadczenia — poza wnioskami z części H i I."},
    {"id": "pit2_nowak", "nazwa": "PIT-2 — pracownik z dwoma pracodawcami", "wzor": "PIT-2 (wersja 9), część C", "lekcja": "zaliczka_pit",
     "scenariusz": "Piotr Nowak pracuje u Ciebie na 1/2 etatu (2 500 zł) i u innego pracodawcy na 1/4 etatu, gdzie złożył PIT-2 z pełnym pomniejszeniem 1/12. "
                   "Mieszka w miejscowości zakładu. Pyta, co ma zaznaczyć w PIT-2 u Ciebie, jeśli niczego nie zmienia u drugiego pracodawcy.",
     "sekcje": [
         s("C. Kwota zmniejszająca podatek", wy("c6", "Poz. 6 — pomniejszenie zaliczki u Ciebie", KW_ZM, "nie wypełniam",
                                                 bledy=[bl("1/12 (300 zł)", "łącznie u wszystkich płatników nie można przekroczyć 1/12 — pełną kwotę stosuje już drugi pracodawca"),
                                                        bl("1/24 (150 zł)", "po 1/24 mogliby mieć obaj płatnicy, ale wtedy musiałby zmienić oświadczenie u drugiego pracodawcy")])),
         s("F. Podwyższone koszty uzyskania przychodów", wy("f12", "Poz. 12", WYP, "nie wypełniam")),
         s("Skutek w liście płac", kw("kup", "Koszty uzyskania u Ciebie (zł/mies.)", 250, bledy=[bl(125, "koszty 250 zł przysługują w pełnej wysokości u każdego pracodawcy, niezależnie od etatu")]),
           kw("zal", "Zaliczka PIT od 2 500 zł u Ciebie (pełne zł)", 229)),
     ],
     "po": "W zeznaniu rocznym pracownik z kilkoma etatami odlicza koszty z wielu stosunków pracy (limit roczny wyższy niż 3 000 zł) — to już jego rozliczenie, nie płatnika."},
    # ------------------------------------------------------------------ PIT-11
    {"id": "pit11_kowalczyk", "nazwa": "PIT-11 — informacja za 2026 r.", "wzor": "PIT-11 (wersja 29), części D, E i G", "lekcja": "pit_roczny",
     "scenariusz": "Anna Kowalczyk pracuje od 1.10.2026 (6 000 zł, KUP 250, PIT-2: 300 zł; w 2026 r. bez PPK). Wypłaty: 10.11.2026 (za październik), 10.12.2026 (za listopad) "
                   "i 8.01.2027 (za grudzień). Z każdej listy: składki społeczne 822,60, zdrowotna 465,97, zaliczka 291. Wypełnij PIT-11 za 2026 r.",
     "sekcje": [
         s("D. Koszty uzyskania przychodów", wy("p28", "Poz. 28 — koszty uzyskania uwzględniono w wysokości (numer kwadratu)", KUP_PIT11, "1 — jeden stosunek pracy",
            bledy=[bl("3 — jeden, podwyższone", "podwyższone koszty (300 zł) ma tylko osoba dojeżdżająca z innej miejscowości — Anna ma 250 zł")])),
         s("E. Wiersz 1 — należności ze stosunku pracy", kw("p29", "Poz. 29 — przychód", 12000, bledy=[bl(18000, "zasada kasowa: pensja za grudzień wypłacona 8.01.2027 to przychód roku 2027")]),
           kw("p30", "Poz. 30 — koszty uzyskania przychodów", 500),
           kw("p31", "Poz. 31 — dochód", 11500, bledy=[bl(9854.80, "w PIT-11 dochód to przychód minus koszty; składki społeczne wykazujesz osobno w poz. 95")]),
           kw("p33", "Poz. 33 — zaliczka pobrana przez płatnika", 582)),
         s("E. Składki", kw("p95", "Poz. 95 — składki na ubezpieczenia społeczne podlegające odliczeniu", 1645.20)),
         s("G. Informacje dodatkowe", kw("p122", "Poz. 122 — składka na ubezpieczenie zdrowotne pobrana przez płatnika", 931.94,
                                         bledy=[bl(0, "PIT-11 w wersji 29 ma pozycję 122 — wykazujesz pobraną składkę informacyjnie, choć nie odlicza się jej od podatku")])),
         s("Terminy", da("us", "Do urzędu skarbowego (elektronicznie) — ostatni dzień", "2027-02-01", bledy=[bl("2027-01-31", "31.01.2027 to niedziela — termin przesuwa się na poniedziałek")]),
           da("pod", "Podatnikowi — ostatni dzień", "2027-03-01", bledy=[bl("2027-02-28", "28.02.2027 to niedziela — termin przesuwa się na poniedziałek")])),
     ],
     "po": "Ten sam PIT-11 wygeneruj z kartoteki w Warsztat → e-Urząd: PIT i porównaj pozycje. Suma poz. 33 ze wszystkich PIT-11 musi się zgadzać z PIT-4R i wpłatami na mikrorachunek."},
    # ------------------------------------------------------------------ świadectwo pracy
    {"id": "swiadectwo_zielinski", "nazwa": "Świadectwo pracy — rozwiązanie za porozumieniem stron", "wzor": "Świadectwo pracy (wzór MRPiPS: ust. 1–8, ust. 6 pkt 1–16)", "lekcja": "swiadectwo_rozliczenie",
     "scenariusz": "Marek Zieliński (operator linii, pełny etat, w firmie od 1.03.2025) odchodzi 30.11.2026 na mocy porozumienia stron zawartego z inicjatywy pracodawcy — likwidacja stanowiska. "
                   "W 2026 r.: wykorzystał 14 dni urlopu, w tym 2 na żądanie, a za 5 dni dostaje ekwiwalent; urlop bezpłatny 2–3.11.2026; chorował 9–20.03, 20–31.07 i 16–30.11 "
                   "(wynagrodzenie chorobowe za 33 dni, potem zasiłek); ma zajęcie komornicze KM 123/26. Wypełnij kluczowe pozycje świadectwa.",
     "sekcje": [
         s("Ust. 1 — okres zatrudnienia", da("u1od", "Zatrudniony od", "2025-03-01"), da("u1do", "do", "2026-11-30"),
           wy("u1wym", "Wymiar czasu pracy", ["pełny wymiar", "1/2 etatu", "3/4 etatu"], "pełny wymiar")),
         s("Ust. 4 — ustanie stosunku pracy", wy("u4", "Podstawa prawna rozwiązania", PODST, "art. 30 §1 pkt 1 KP — porozumienie stron"),
           wy("u4d", "Czy dopisujesz „w zw. z art. 10 ust. 1 ustawy z 13.03.2003”?", TN, "tak"), wy("u4p", "Czy opisujesz przyczynę (likwidacja stanowiska)?", TN, "nie")),
         s("Ust. 6 — w okresie zatrudnienia pracownik", li("u6p2", "pkt 2. Urlop wypoczynkowy wykorzystany w roku ustania (dni)", 19,
                                                          bledy=[bl(14, "urlop, za który wypłacasz ekwiwalent, wykazujesz jako wykorzystany: 14 + 5")]),
           li("u6p2z", "pkt 2. W tym urlop na żądanie (dni)", 2), da("u6p4od", "pkt 4. Urlop bezpłatny od", "2026-11-02"), da("u6p4do", "pkt 4. Urlop bezpłatny do", "2026-11-03"),
           li("u6p11", "pkt 11. Dni niezdolności z wynagrodzeniem z art. 92 KP w roku ustania", 33),
           li("u6p16", "pkt 16. Ile okresów nieskładkowych wpisujesz?", 3), da("u6p16od", "pkt 16. Początek pierwszego okresu", "2026-03-09")),
         s("Ust. 7 i wydanie", wy("u7", "Ust. 7. Czy wpisujesz informację o zajęciu wynagrodzenia?", TN, "tak"), da("wyd", "Dzień wydania świadectwa", "2026-11-30")),
     ],
     "po": "Świadectwo: papier z podpisem albo postać elektroniczna z kwalifikowanym podpisem. Dane o trybie muszą się zgadzać z blokiem V ZWUA (tu 46R + 402 + strona 2)."},
    # ------------------------------------------------------------------ PROJEKT KOŃCOWY (część rachunkowa)
    {"id": "projekt_zamkniecie_roku", "nazwa": "Projekt końcowy — zamknięcie roku 2026 w AGRO-MLEKO", "wzor": "lista płac → ZUS (DRA/RCA/RSA/RPA) → PIT → wskaźniki i terminy 2027 → ZFŚS", "lekcja": "powtorka_etap_4",
     "scenariusz": "Jest początek stycznia 2027 r. Zamykasz rok 2026 w AGRO-MLEKO (stopa wypadkowa 1,20%; wszyscy troje mają KUP 250 zł i PIT-2 na 300 zł). Lista płac za grudzień 2026: "
                   "(1) Tomasz Lis — pensja 14 000 zł i premia roczna za 2026 r. 16 800 zł, PPK 2% / 1,5%; (2) Katarzyna Wójcik — pensja 4 806 zł, PPK 2% / 1,5%, choroba 28–31.12.2026 "
                   "(pierwsza w tym roku; stawka dzienna 80%: 110,59 zł); (3) Anna Kowalczyk — pensja 6 000 zł, jeszcze bez PPK; jej umowa próbna kończy się 31.12.2026, a od 1.01.2027 ma umowę na czas określony. "
                   "Regulamin: wypłata do 10. dnia następnego miesiąca. Odpis na ZFŚS za 2026 r. naliczono dla 60 etatów, a faktyczne przeciętne zatrudnienie wyniosło 57,2 etatu "
                   "(odpis podstawowy 2 943,23 zł). Policz listę, przypisz dokumenty do właściwych okresów i ustal terminy — wszystko, czego nauczył Cię kurs, w jednym zamknięciu roku.",
     "sekcje": [
         s("1. Lista płac za grudzień 2026", da("wyplata", "Dzień wypłaty", "2027-01-08", bledy=[bl("2027-01-11", "wynagrodzenie wypłacasz dzień WCZEŚNIEJ, gdy termin wypada w dzień wolny (art. 85 §3 KP)"),
                                                                                                    bl("2027-01-10", "10.01.2027 to niedziela — wypłata w poprzedzającym dniu roboczym")]),
           kw("lis_spol", "Lis — składki społeczne (zł)", 4222.68), kw("lis_zdr", "Lis — składka zdrowotna (zł)", 2391.96),
           kw("lis_zal", "Lis — zaliczka PIT (pełne zł)", 2915, bledy=[bl(8272, "to pierwsza wypłata roku podatkowego 2027 — dochód narastająco zaczyna się od zera, więc stawka 12%")]),
           kw("lis_netto", "Lis — netto (zł)", 20654.36),
           kw("woj_pensja", "Wójcik — pensja za przepracowaną część miesiąca (zł)", 4165.20), kw("woj_chor", "Wójcik — wynagrodzenie chorobowe (zł)", 442.36),
           kw("woj_spol", "Wójcik — składki społeczne (zł)", 571.05), kw("woj_zdr", "Wójcik — składka zdrowotna (zł)", 363.29, bledy=[bl(323.47, "wynagrodzenie chorobowe wchodzi do podstawy składki zdrowotnej")]),
           kw("woj_zal", "Wójcik — zaliczka PIT (pełne zł)", 162), kw("woj_netto", "Wójcik — netto (zł)", 3427.92),
           kw("kow_netto", "Kowalczyk — netto (zł)", 4420.43), kw("przelewy", "Suma przelewów netto dla trojga (zł)", 28502.71)),
         s("2. ZUS — do którego kompletu i co jeszcze", tx("ident", "Identyfikator kompletu DRA/RCA/RSA z tą listą", "01 01 2027",
                                                         bledy=[bl("01 12 2026", "zasada kasowa: wypłata w styczniu 2027 → komplet za styczeń 2027")]),
           da("zus_termin", "Termin kompletu i składek", "2027-02-15"), tx("rsa_kod", "RSA Wójcik — kod świadczenia", "331"), li("rsa_dni", "RSA Wójcik — liczba dni", 4),
           wy("rsa_odl", "Czy kwotę z tego wiersza RSA odliczasz od składek w DRA?", TN, "nie"),
           wy("rpa", "Czy dla Tomasza Lisa wypełniasz RPA (premia za 2026 r. wypłacona w 2027)?", TN, "tak"),
           wy("zwua", "Kowalczyk — kolejna umowa bez dnia przerwy: czy składasz ZWUA i nowe ZUA?", TN, "nie")),
         s("3. PIT", kw("pit_suma", "Suma zaliczek z tej listy (zł)", 3368), da("pit_termin", "Termin wpłaty tych zaliczek", "2027-02-22", bledy=[bl("2027-02-20", "20.02.2027 to sobota — termin przesuwa się na poniedziałek")]),
           li("pit_rok", "W PIT-11 za który rok wykażesz wypłaty z tej listy?", 2027, bledy=[bl(2026, "decyduje data wypłaty, nie miesiąc, za który jest pensja")]),
           kw("kow_pit11", "Kowalczyk — przychód w PIT-11 za 2026 r. (zł)", 12000), da("pit_us", "PIT-4R i PIT-11 za 2026 r. do urzędu — ostatni dzień", "2027-02-01"),
           da("pit_pod", "PIT-11 za 2026 r. pracownikom — ostatni dzień", "2027-03-01")),
         s("4. Nowy rok — wskaźniki i terminy", kw("min", "Minimalne wynagrodzenie od 1.01.2027 (zł)", 4950), wy("aneks", "Czy Katarzyna Wójcik potrzebuje aneksu od 1.01.2027?", TN, "tak"),
           kw("wolna", "Kwota wolna od potrąceń w 2027 r. — pełny etat, KUP 250, PIT-2, bez PPK (zł)", 3703.93, bledy=[bl(3605.85, "to kwota z 2026 r. — policz netto od nowego minimalnego 4 950 zł")]),
           kw("limit", "Limit 30-krotności w 2027 r. (zł)", 300990),
           da("ppk", "Umowa o prowadzenie PPK dla Anny Kowalczyk — zawrzyj najpóźniej (dzień roboczy)", "2027-01-08"),
           da("dekr", "PFRON — deklaracja roczna DEK-R", "2027-01-20"), da("urlop", "Urlop zaległy za 2026 r. — udziel najpóźniej", "2027-09-30")),
         s("5. ZFŚS — korekta roczna", kw("zfss", "Nadwyżka odpisu ponad należny (zł)", 8241.04),
           wy("zfss_co", "Co robisz z nadwyżką?", ["wycofuję z rachunku funduszu albo zaliczam na odpis 2027", "zostawiam bez korekty"], "wycofuję z rachunku funduszu albo zaliczam na odpis 2027")),
     ],
     "po": "To rachunkowa część projektu końcowego. Część opisową — raport z audytu, plan naprawczy i portfolio — robisz w zadaniu „PROJEKT KOŃCOWY” tygodnia 15. "
           "Zapisz ten formularz do projektu i dołącz do portfolio."},
]

# krok „Formularz” dopisywany do zadań tygodniowych (id zadania → tekst)
KROKI_FORMULARZY = {
    "k4z3": "Formularz: Warsztat → Formularze → „PIT-2 — oświadczenia pracownicy…” i „PIT-2 — pracownik z dwoma pracodawcami” — zaznacz części jak na prawdziwym druku i kliknij „Sprawdź odpowiedzi”.",
    "k6z3": "Formularz: Warsztat → Formularze → „ZUS RSA — wynagrodzenie chorobowe i zasiłek” — wypełnij oba wiersze i sprawdź.",
    "k8z1": "Formularz: Warsztat → Formularze → „ZUS ZUA — zgłoszenie nowej pracownicy” — wypełnij bloki I–XIV pole po polu (numery jak na druku ZUS) i sprawdź; dopiero potem „wyślij” zgłoszenie w symulatorze.",
    "k8z2": "Formularz: Warsztat → Formularze → „ZUS RCA — imienny raport o składkach” — policz ręcznie każde pole bloku III.B i III.C, sprawdź, a potem porównaj z RCA z symulatora.",
    "k9z1": "Formularz: Warsztat → Formularze → „PIT-11 — informacja za 2026 r.” — wypełnij pozycje 28–33, 95 i 122 i sprawdź; porównaj z PIT-11 wygenerowanym w e-Urząd: PIT.",
    "k10z2": "Formularz: Warsztat → Formularze → „ZUS ZWUA — rozwiązanie bez wypowiedzenia (art. 52)” — bloki IV i V z kodami trybu i podstawy.",
    "k11z5": "Część rachunkowa projektu: Warsztat → Formularze → „Projekt końcowy — zamknięcie roku 2026 w AGRO-MLEKO” — 35 pól: lista płac, ZUS, PIT, wskaźniki 2027 i ZFŚS. Policz wszystko sam, sprawdź i zapisz do portfolio.",
    "k10z4": "Formularz: Warsztat → Formularze → „Świadectwo pracy — rozwiązanie za porozumieniem stron” i „ZUS ZWUA — wyrejestrowanie po wypowiedzeniu przez pracodawcę” — wypełnij i sprawdź; wynik zapisz do projektu.",
}
