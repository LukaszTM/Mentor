# Przykład — Rozliczenia miesięczne: DRA, RCA, RSA, RPA, terminy, NRS, zasada kasowa
Tydzień 8

**Komplet 01 12 2026 AGRO-MLEKO: wypłata za listopad 10.12 — kto trafia do RCA, co do RSA, ile do zapłaty**

```
AGRO-MLEKO (sp. z o.o. → do 15.), wypłata za listopad 10.12.2026, 62 pracowników + 6 zleceniobiorców (3 ze zbiegiem — tylko zdrowotna, 1 student — poza ZUS), 1 osoba na wychowawczym (12 11), 1 na macierzyńskim (zasiłek od płatnika — RSA 327, kwota w DRA do odliczenia), nadgodziny listopadowe i trzynastka za 2025 wypłacona w grudniu (RPA — przychód za inny rok dla 62 osób).
Komplet 01 12 2026: DRA + 68 RCA (62 × 01 10, 5 × 04 11, 1 × 12 11; student bez raportu) + RSA (chorobowe 331, zasiłki 313/312, macierzyński 327, bezpłatny 111 — za okresy GRUDNIOWE) + RPA (trzynastka). Wysyłka i przelew na NRS do 15.01.2027 (do zapłaty = składki − zasiłki wypłacone). Zasiłki za listopad wypłacone 10.12 — rozliczane w DRA 12/2026.
```

## Omówienie — co robi każdy krok i dlaczego
1. „wypłata za listopad 10.12.2026 → komplet 01 12 2026, wysyłka i przelew do 15.01.2027”: zasada kasowa — składki rozliczasz w miesiącu WYPŁATY (grudzień), nie za miesiąc pracy; spółka z o.o. ma termin 15. dnia następnego miesiąca (15.01.2027 — piątek).
2. „DRA + 68 RCA (62 × 01 10, 5 × 04 11, 1 × 12 11; student bez raportu)”: każda osoba z podstawą składek ma RCA z kodem tytułu; osoba na wychowawczym — RCA z kodem 12 11 (składki finansowane z budżetu); student na zleceniu — w ogóle poza kompletem; 3 zleceniobiorców ze zbiegiem — RCA tylko ze zdrowotną.
3. „RSA (chorobowe 331, zasiłki 313/312, macierzyński 327, bezpłatny 111)”: dwie reguły — ŚWIADCZENIA (331, 313, 312, 327…) wykazujesz w komplecie za miesiąc, w którym je WYPŁACONO (10.12 → komplet 12/2026), z faktycznym okresem (np. 16–30.11); PRZERWY bez świadczeń (111 urlop bezpłatny, 151, 152) — w komplecie za miesiąc, w którym przerwa WYSTĄPIŁA (bezpłatny z grudnia → 12/2026, z listopada → 11/2026). Symulator ostrzega przy okresie z innego miesiąca — dla świadczeń to normalne.
4. „RPA (trzynastka za 2025 wypłacona w grudniu)”: przychód za inny rok kalendarzowy niż rok wypłaty wykazujesz dodatkowo w RPA (dla celów emerytalnych) — składki normalnie w RCA.
5. „do zapłaty = składki − zasiłki wypłacone”: płatnik zasiłków odejmuje w DRA zasiłki (313/312/327…), NIE wynagrodzenie chorobowe (331) — to koszt pracodawcy; przelew jedną kwotą na NRS firmy.
6. Kontrola przed wysyłką: liczba RCA = liczba ubezpieczonych w DRA; suma podstaw w RCA = suma w DRA; podstawy w RCA = lista płac (przychód oskładkowany); zasiłki w RSA = zasiłki na liście; zachowaj UPP.

✔ Oczekiwany wynik: komplet 01 12 2026: DRA + 68 RCA + RSA + RPA, wysłany i opłacony do 15.01.2027; do zapłaty = składki − zasiłki (bez wynagrodzenia chorobowego).

## Jak to uruchomić
1. Warsztat → Lista płac: dla miesiąca 2026-11 dodaj do listy co najmniej 4 osoby (w tym Zielińskiego z wynagrodzeniem chorobowym 1 201,14 i zasiłkiem 800,76) → „Zapisz listę”.
2. Warsztat → eZUS / Płatnik → Rozliczenie DRA/RCA/RSA: miesiąc 2026-12 (wypłata 10.12!), identyfikator 01 → „Dodaj RSA”: Zieliński 331 16–24.11 kwota 1 201,14; 313 25–30.11 kwota 800,76 → „Pokaż komplet” → sumy DRA → „Weryfikuj” → „Wyślij (symulacja)” → UPP; „Zapisz do projektu” → 05-zus-us/komplet_2026-12.md.
3. Zwróć uwagę na ostrzeżenie o przerwie z innego miesiąca (listopad w komplecie grudniowym) — to zamierzone: wypłata była w grudniu.
4. Oczekiwany wynik: DRA z liczbą ubezpieczonych = liczba wierszy listy, składki = suma z listy, zasiłki odjęte = 800,76 (nie 2 001,90).
