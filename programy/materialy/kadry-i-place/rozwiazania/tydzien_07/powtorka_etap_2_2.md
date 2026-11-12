# Rozwiązanie — ćwiczenie 2 (samodzielne) — Powtórka etapu 2: płace od brutto do netto — lista, PIT, zasiłki, umowy cywilne, PPK
Plik startowy: `cwiczenia/tydzien_07/powtorka_etap_2_2.md`

Zasada: najpierw własna próba. Podpowiedzi odkrywaj po kolei — rozwiązanie dopiero na końcu.

## Podpowiedź 1 — pytanie naprowadzające
Czy 30-krotność liczysz od przychodu, czy od podstawy E/R narastająco — i czy premia roczna się wlicza? (Tak, w miesiącu wypłaty.)

## Podpowiedź 2 — gdzie szukać
Lekcje „Zaliczka PIT” (32% od całości po progu), „Chorobowe” (pula wyczerpana → zasiłek od 1. dnia), „Potrącenia” (alimenty 3/5 bez kwoty wolnej).

## Podpowiedź 3 — częściowy przykład
Szkic: podstawa E/R narastająco po listopadzie 154 000; grudzień 41 666,67 → 195 666,67 < 282 600; zasiłek 402,69 × 0,8 = 322,15 × 5; 32% od (… ) − 300…

## Pełne rozwiązanie
```
30-krotność: podstawa E/R narastająco po listopadzie 11 × 14 000 = 154 000; grudzień: pensja 11 666,67 + premia 30 000 = 41 666,67 → 195 666,67 < 282 600 → składki E/R od całości.
Pensja: 14 000 − 14 000/30 × 5 = 11 666,67 (choroba — /30). Przychód oskładkowany 41 666,67.
Składki: 4 066,67 + 625,00 + 1 020,83 = 5 712,50. Zdrowotna 9% × 35 954,17 = 3 235,88 (zasiłek nie wchodzi).
Świadczenie: pula 33 dni wyczerpana → zasiłek chorobowy od 1. dnia: 12 080,60/30 = 402,69; × 80% = 322,15; × 5 dni = 1 610,75 (płatnik wypłaca, odlicza w DRA; RSA 313); tylko PIT bez KUP.
PPK: pracodawcy 625,00 (przychód), pracownika 833,33.
Podstawa PIT: 41 666,67 + 625,00 − 5 712,50 − 250 + 1 610,75 = 37 939,92 → 37 940; po progu całość 32%: 12 140,80 − 300 = 11 840,80 → 11 841.
Netto: (41 666,67 + 1 610,75) − 5 712,50 − 3 235,88 − 11 841 − 833,33 = 21 654,71.
Alimenty: granica 3/5 netto = 12 992,83; bez kwoty wolnej → 3 000 w całości → do wypłaty 18 654,71 zł.
Dochód narastająco po grudniu: 132 451 + 37 940 = 170 391 → PIT-11.
```

## Oczekiwany wynik
30-krotność: 154 000 + (14 000 − 2 333,33 + 30 000) = 195 666,67 < 282 600 → bez ograniczenia; pensja 14 000 − 14 000/30 × 5 = 11 666,67; oskładkowane 41 666,67; składki 4 066,67 + 625,00 + 1 020,83 = 5 712,50; zasiłek (pula 33 wyczerpana → zasiłek od 1. dnia): 12 080,60/30 = 402,69 × 80% = 322,15 × 5 = 1 610,75 (tylko PIT); zdrowotna 9% × (41 666,67 − 5 712,50) = 3 235,88; PPK pracod. 625,00; podstawa = 41 666,67 + 625 − 5 712,50 − 250 + 1 610,75 (zasiłek) = 37 939,92 → 37 940 × 32% = 12 140,80 − 300 = 11 840,80 → 11 841; PPK prac. 833,33; netto = (41 666,67 + 1 610,75) − 5 712,50 − 3 235,88 − 11 841 − 833,33 = 21 654,71; alimenty: 3/5 × 21 654,71 = 12 992,83 ≥ 3 000, bez kwoty wolnej → potrącenie 3 000 → do wypłaty 18 654,71.

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co by się zmieniło, gdyby zmienił się jeden fakt (etat, staż, data, kwota)?
