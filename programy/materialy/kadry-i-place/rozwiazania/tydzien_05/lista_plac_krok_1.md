# Rozwiązanie — ćwiczenie 1 (prowadzone) — Lista płac krok po kroku: od brutto do netto
Plik startowy: `cwiczenia/tydzien_05/lista_plac_krok_1.md`

Zasada: najpierw własna próba. Podpowiedzi odkrywaj po kolei — rozwiązanie dopiero na końcu.

## Podpowiedź 1 — pytanie naprowadzające
Od jakiej kwoty liczysz składki — od 5 200 czy od 5 773,75? (Nadgodziny są oskładkowane.)

## Podpowiedź 2 — gdzie szukać
Demonstracja, kroki 1–7, z brutto 5 773,75; „Tryb ćwiczenia” powie, której kwocie równa się ewentualna różnica.

## Podpowiedź 3 — częściowy przykład
Częściowy rachunek: 5 773,75 × 9,76% = 563,52; × 1,5% = 86,61; × 2,45% = 141,46 → 791,59; zdrowotna 9% × 4 982,16 = 448,39; PPK pracod. 86,61; podstawa 5 773,75 + 86,61 − 791,59 − 250 = 4 818,77 → 4 819…

## Pełne rozwiązanie
```
Brutto = 5 200 + 573,75 = 5 773,75
Emerytalna 563,52; rentowa 86,61; chorobowa 141,46 → społeczne 791,59
Podstawa zdrowotnej 5 773,75 − 791,59 = 4 982,16 → zdrowotna 448,39
PPK pracodawcy 1,5% = 86,61 (przychód)
Podstawa PIT = 5 773,75 + 86,61 − 791,59 − 250 = 4 818,77 → 4 819
Podatek 12% = 578,28 − 300 = 278,28 → zaliczka 278
PPK pracownika 2% = 115,48
Netto = 5 773,75 − 791,59 − 448,39 − 278 − 115,48 = 4 140,29 zł
Bilans: 4 140,29 + 791,59 + 448,39 + 278 + 115,48 = 5 773,75 ✔
Koszt pracodawcy (wypadkowa 1,20%): 5 773,75 + 563,52 + 375,29 + 69,29 + 141,46 + 5,77 + 86,61 = 7 015,69
```

## Oczekiwany wynik
brutto 5 773,75; społeczne 563,52 + 86,61 + 141,46 = 791,59; zdrowotna 448,39; PPK pracodawcy 86,61; podstawa PIT 4 819; zaliczka 278; PPK pracownika 115,48; netto 4 140,29 zł (bilans: 4 140,29 + 791,59 + 448,39 + 278 + 115,48 = 5 773,75).

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co by się zmieniło, gdyby zmienił się jeden fakt (etat, staż, data, kwota)?
