# Rozwiązanie — ćwiczenie 2 (samodzielne) — Lista płac krok po kroku: od brutto do netto
Plik startowy: `cwiczenia/tydzien_04/lista_plac_krok_2.md`

Zasada: najpierw własna próba. Podpowiedzi odkrywaj po kolei — rozwiązanie dopiero na końcu.

## Podpowiedź 1 — pytanie naprowadzające
Które obciążenie NIE dotyczy wynagrodzenia chorobowego: składki społeczne, zdrowotna czy PIT?

## Podpowiedź 2 — gdzie szukać
Lekcja, sekcja „Zaokrąglenia”: chorobowe — podstawa zdrowotnej i PIT, bez społecznych; Warsztat → Lista płac ma osobne pole „Wynagrodzenie chorobowe”.

## Podpowiedź 3 — częściowy przykład
Szkic: pensja 5 400 − 1 800 = 3 600 (dzielnik 30 przy chorobie); społeczne od 3 600 = 493,56; zdrowotna od (3 600 − 493,56 + 1 334,60); podstawa PIT = 3 600 + 1 334,60 + 54 − 493,56 − 250…

## Pełne rozwiązanie
```
1. Pensja za przepracowaną część: 5 400 − 5 400/30 × 10 = 3 600,00 (§11 rozp. urlopowego — choroba: dzielnik 30).
2. Składki społeczne TYLKO od 3 600: 351,36 + 54,00 + 88,20 = 493,56 (wynagrodzenie chorobowe wyłączone — §2 ust. 1 pkt 24 rozp. składkowego).
3. Zdrowotna od 3 600 − 493,56 + 1 334,60 = 4 441,04 → 399,69 (chorobowe podlega zdrowotnej).
4. PPK: pracodawca 1,5% × 3 600 = 54,00; pracownik 2% × 3 600 = 72,00 (od podstawy składek emerytalnych — chorobowe nie wchodzi).
5. Podstawa PIT = 3 600 + 1 334,60 + 54,00 − 493,56 − 250 = 4 245,04 → 4 245; 12% = 509,40 − 300 = 209,40 → 209.
6. Netto = (3 600 + 1 334,60) − 493,56 − 399,69 − 209 − 72 = 3 760,35 zł.
7. FP/FGŚP: podstawa w przeliczeniu na miesiąc = 5 400 ≥ 4 806 → należne od 3 600 (88,20 + 3,60). W Warsztacie wpisz „Pensja wg umowy 5400”.
```

## Oczekiwany wynik
pensja za część miesiąca 5 400 − 5 400/30 × 10 = 3 600; składki społeczne tylko od 3 600 (351,36 + 54,00 + 88,20 = 493,56); zdrowotna od 3 600 − 493,56 + 1 334,60 = 4 441,04 → 399,69; PIT: przychód 3 600 + 1 334,60 + 54,00 (PPK) − 493,56 − 250 = 4 245,04 → 4 245 → 509,40 − 300 → 209; PPK pracownika 72,00 (od 3 600); netto 3 600 + 1 334,60 − 493,56 − 399,69 − 209 − 72 = 3 760,35; FP/FGŚP należne (pensja umowna 5 400 ≥ minimalne).

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co by się zmieniło, gdyby zmienił się jeden fakt (etat, staż, data, kwota)?
