# -*- coding: utf-8 -*-
"""Pytania quizowe dopisane po zmianie harmonogramu na 16 tygodni (klucz = NOWY numer tygodnia).
Każde pytanie wskazuje lekcję do powtórki — lekcję z tego tygodnia albo wcześniejszą. Fakty zgodne z testami lekcji (stan XI 2026)."""

QUIZY_DODATKOWE = {
    4: [
        {"p": "Urlop ojcowski — wymiar i termin wykorzystania:", "o": ["1 tydzień, do ukończenia przez dziecko 24 miesięcy", "2 tygodnie, do ukończenia przez dziecko 12 miesięcy", "2 tygodnie, do ukończenia 24 miesięcy", "4 tygodnie, do ukończenia 12 miesięcy"],
         "odp": 1, "w": "Art. 182³ KP: 2 tygodnie, do ukończenia przez dziecko 12. miesiąca życia (od 26.04.2023).", "lekcja": "urlopy_rodzicielskie"},
        {"p": "Zwolnienie od pracy z powodu siły wyższej (art. 148¹ KP) — wymiar i wynagrodzenie:", "o": ["2 dni lub 16 godzin w roku, 50% wynagrodzenia", "2 dni w roku, 100% wynagrodzenia", "5 dni w roku, bez wynagrodzenia", "1 dzień w roku, 80% wynagrodzenia"],
         "odp": 0, "w": "2 dni albo 16 godzin w roku kalendarzowym; za ten czas 50% wynagrodzenia liczonego jak urlopowe.", "lekcja": "nieobecnosci_inne"},
        {"p": "Pracownica w 5. miesiącu ciąży ma umowę na czas określony do 30.11. Umowa:", "o": ["Rozwiązuje się 30.11 — termin jest terminem", "Przedłuża się z mocy prawa do dnia porodu", "Przedłuża się do końca urlopu macierzyńskiego", "Wymaga aneksu, inaczej wygasa"],
         "odp": 1, "w": "Art. 177 §3 KP — przedłużenie do dnia porodu (poza umową na zastępstwo i próbną do 1 miesiąca).", "lekcja": "urlopy_rodzicielskie"},
    ],
    7: [
        {"p": "Delegacja krajowa 23.11 07:00 → 24.11 16:00 (33 h), organizator zapewnił obiad w oba dni. Diety do wypłaty:", "o": ["90,00 zł", "67,50 zł", "45,00 zł", "22,50 zł"],
         "odp": 2, "w": "1 pełna doba + 9 h (ponad 8 h) = 2 diety × 45 = 90; − 2 obiady × 50% × 45 = 45 → 45,00 zł.", "lekcja": "delegacje"},
        {"p": "Ryczałt za nocleg w podróży krajowej, gdy pracownik nie ma rachunku:", "o": ["45,00 zł", "67,50 zł (150% diety)", "90,00 zł (200% diety)", "900,00 zł (20 diet)"],
         "odp": 1, "w": "§ 8 ust. 3: 150% diety = 67,50 zł, jeśli nocleg trwał co najmniej 6 h między 21:00 a 7:00; 900 zł to limit rachunku.", "lekcja": "delegacje"},
    ],
    8: [
        {"p": "Okres wyczekiwania na zasiłek chorobowy pracownika (ubezpieczenie obowiązkowe):", "o": ["Nie ma — od pierwszego dnia", "30 dni nieprzerwanego ubezpieczenia", "90 dni nieprzerwanego ubezpieczenia", "180 dni"],
         "odp": 1, "w": "Art. 4 ust. 1 pkt 1 ustawy zasiłkowej — 30 dni (dobrowolne chorobowe: 90 dni); wyjątki w art. 4 ust. 3.", "lekcja": "podstawa_zasilku"},
        {"p": "Ubezpieczony po kontroli prawidłowości wykorzystywania zwolnienia (od 13.04.2026) ma na uwagi do protokołu:", "o": ["1 dzień", "3 dni", "7 dni", "14 dni"],
         "odp": 1, "w": "3 dni na uwagi; spór rozstrzyga ZUS decyzją, od której przysługuje odwołanie do sądu.", "lekcja": "kontrola_l4_2026"},
    ],
    11: [
        {"p": "PIT-11 za 2026 r.: do kiedy do urzędu skarbowego, a do kiedy do pracownika?", "o": ["Oba do 31 stycznia 2027", "US — 31 stycznia 2027; pracownik — koniec lutego 2027", "US — koniec lutego; pracownik — 31 stycznia", "Oba do 30 kwietnia 2027"],
         "odp": 1, "w": "Art. 39 ust. 1 PIT: do US do końca stycznia, do podatnika do końca lutego; po ustaniu zatrudnienia na wniosek — 14 dni.", "lekcja": "pit_roczny"},
        {"p": "Zasiłek chorobowy wypłacony przez pracodawcę (płatnika) wykazujesz w PIT-11:", "o": ["W przychodach ze stosunku pracy z KUP", "W przychodach z innych źródeł, bez KUP", "Wcale — zasiłek wykazuje ZUS", "W PIT-8AR"],
         "odp": 1, "w": "Zasiłki pieniężne z ubezpieczenia społecznego to inne źródła (art. 20 PIT) — bez kosztów uzyskania.", "lekcja": "pit_roczny"},
        {"p": "ZUS IWA (dane do ustalenia składki wypadkowej) składasz do:", "o": ["31 stycznia", "28 lutego", "31 marca", "20 kwietnia"],
         "odp": 0, "w": "IWA — do 31 stycznia; ZSWA — do 31 marca; stopę procentową na nowy rok składkowy ZUS podaje do 20 kwietnia.", "lekcja": "zus_rozliczenia"},
        {"p": "Składkę zdrowotną w PIT-11:", "o": ["Wykazujesz w osobnej pozycji do odliczenia", "Nie wykazujesz — od 2022 nie podlega odliczeniu", "Wykazujesz tylko w części 7,75%", "Wykazujesz razem ze składkami społecznymi"],
         "odp": 1, "w": "Od 1.01.2022 (Polski Ład) składka zdrowotna nie jest odliczana; formularz nie ma tego pola.", "lekcja": "pit_roczny"},
    ],
    12: [
        {"p": "Zaległy urlop za 2026 r. pracownik musi wykorzystać najpóźniej do:", "o": ["31 marca 2027", "30 czerwca 2027", "30 września 2027", "31 grudnia 2027"],
         "odp": 2, "w": "Art. 168 KP — do 30 września następnego roku (nie dotyczy 4 dni na żądanie).", "lekcja": "kalendarz_roczny"},
        {"p": "Pracodawca wpłaca na PFRON, gdy:", "o": ["Zatrudnia co najmniej 25 etatów i wskaźnik osób niepełnosprawnych jest niższy niż 6%", "Zatrudnia co najmniej 50 osób, niezależnie od wskaźnika", "Nie zatrudnia żadnej osoby z orzeczeniem", "Zatrudnia poniżej 25 etatów"],
         "odp": 0, "w": "Art. 21 ustawy o rehabilitacji — ≥ 25 etatów i wskaźnik < 6%; wpłata do 20. dnia następnego miesiąca (DEK-I-0).", "lekcja": "zfss_pfron"},
    ],
    15: [
        {"p": "Zastrzeżenia do protokołu kontroli PIP możesz wnieść w terminie:", "o": ["3 dni", "7 dni", "14 dni", "30 dni"],
         "odp": 1, "w": "PIP — 7 dni od przedstawienia protokołu; ZUS — 14 dni.", "lekcja": "kontrola_pip_zus"},
        {"p": "Nakaz PIP dotyczący wypłaty należnego wynagrodzenia:", "o": ["Podlega natychmiastowemu wykonaniu", "Jest wykonalny po 30 dniach", "To tylko zalecenie", "Wymaga potwierdzenia przez sąd pracy"],
         "odp": 0, "w": "Art. 11 pkt 7 ustawy o PIP — nakaz płacowy jest decyzją podlegającą natychmiastowemu wykonaniu.", "lekcja": "kontrola_pip_zus"},
        {"p": "Procedura zgłoszeń wewnętrznych (sygnaliści) jest obowiązkowa od:", "o": ["20 osób", "25 etatów", "50 osób wykonujących pracę zarobkową", "250 osób"],
         "odp": 2, "w": "Stan zatrudnienia na 1 stycznia lub 1 lipca; w sektorze finansowym — zawsze.", "lekcja": "sygnalisci_zdalna_rodo"},
        {"p": "Limit dni kontroli ZUS u średniego przedsiębiorcy w roku kalendarzowym:", "o": ["12 dni", "18 dni", "24 dni", "48 dni"],
         "odp": 2, "w": "Mikro 12, mały 18, średni 24, duży 48 dni (ustawa Prawo przedsiębiorców).", "lekcja": "kontrola_pip_zus"},
    ],
}
