# Przykład — Lista płac krok po kroku: od brutto do netto
Tydzień 4

**Brutto 7 200 zł (6 000 + 800 nadgodzin + 400 premii) z PPK — osiem kroków w stałej kolejności**

```
Brutto 7 200 zł (6 000 zasadnicze + 800 nadgodziny + 400 premia), KUP 250, PIT-2, PPK 2%/1,5%:
społeczne: 702,72 + 108,00 + 176,40 = 987,12 → podst. zdrow. 6 212,88 → zdrowotna 559,16
PPK pracodawcy 108,00 (przychód) → podstawa PIT = 7 200 + 108 − 987,12 − 250 = 6 070,88 → 6 071 → 12% = 728,52 − 300 = 428,52 → 429
PPK pracownika 144,00 → netto = 7 200 − 987,12 − 559,16 − 429 − 144 = 5 080,72 zł
```

## Omówienie — co robi każdy krok i dlaczego
1. „społeczne: 702,72 + 108,00 + 176,40 = 987,12”: podstawa składek = wszystkie składniki oskładkowane (7 200); emerytalna 9,76%, rentowa 1,5%, chorobowa 2,45% — każda osobno do grosza; gdyby pracownik przekroczył 282 600 zł narastająco, emerytalnej i rentowej nie byłoby od nadwyżki.
2. „podst. zdrow. 6 212,88 → zdrowotna 559,16”: 7 200 − 987,12; 9%. Wynagrodzenie chorobowe (gdyby było) wchodzi tu, choć nie ma składek społecznych.
3. „PPK pracodawcy 108,00 (przychód)”: 1,5% × 7 200 — pracodawca wpłaca do instytucji, pracownik nie dostaje gotówki, ale to jego przychód do PIT (bez ZUS). Dlatego podstawa PIT zaczyna się od 7 200 + 108.
4. „podstawa PIT = 7 308 − 987,12 − 250 = 6 070,88 → 6 071”: odejmujesz składki społeczne pracownika i KUP; zaokrąglasz do pełnych złotych (art. 63 Ordynacji).
5. „12% = 728,52 − 300 = 428,52 → 429”: stawka 12% (dochód narastająco poniżej 120 000), kwota zmniejszająca 300 (PIT-2), zaliczka do pełnego złotego.
6. „PPK pracownika 144,00”: 2% × 7 200 — schodzi z netto (po podatku).
7. „netto = 7 200 − 987,12 − 559,16 − 429 − 144 = 5 080,72”: odejmujesz tylko to, co pracownik rzeczywiście płaci; PPK pracodawcy nie odejmujesz (nie było wypłacone).
8. Bilans kontrolny: netto + społeczne + zdrowotna + zaliczka + PPK pracownika = 7 200 → 5 080,72 + 987,12 + 559,16 + 429 + 144 = 7 200,00 ✔. Koszt pracodawcy: 7 200 + składki pracodawcy (wypadkowa 1,2%) + 108 = 8 748,72.

✔ Oczekiwany wynik: netto 5 080,72 zł; zaliczka 429; bilans brutto = netto + obciążenia pracownika zgadza się co do grosza.

## Jak to uruchomić
1. Warsztat → Lista płac → Osoba „— własne dane —”, Zasadnicze 6000, Nadgodziny/premie 1200, PPK 2 / 1,5, KUP 250, PIT-2 300 → pole „Tryb ćwiczenia — moje netto”: wpisz swoje 5 080,72 → „Sprawdź”.
2. Jeśli się zgadza — zobaczysz ✔ i kroki; jeśli nie — Mentor podpowie, jakiej kwocie równa się różnica (np. „różnica równa się: PPK pracodawcy”).
3. „Dodaj do listy miesiąca” → powtórz dla kolejnych osób → „Pokaż listę miesiąca” → „Zapisz listę (MD + CSV)” → plik 04-place/lista_plac_2026-11.md w katalogu projektu.
4. Oczekiwany wynik: tabela listy z wierszem RAZEM; suma zaliczek = kwota do US do 20. następnego miesiąca.
