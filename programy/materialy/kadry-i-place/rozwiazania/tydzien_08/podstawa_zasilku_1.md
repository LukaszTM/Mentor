# Rozwiązanie — ćwiczenie 1 (prowadzone) — Podstawa wymiaru zasiłku: 12 miesięcy, uzupełnianie, składniki, minimum
Plik startowy: `cwiczenia/tydzien_08/podstawa_zasilku_1.md`

Zasada: najpierw własna próba. Podpowiedzi odkrywaj po kolei — rozwiązanie dopiero na końcu.

## Podpowiedź 1 — pytanie naprowadzające
Dlaczego marzec (11/22) zostaje, a lipiec (5/23) wypada? Jaki jest próg?

## Podpowiedź 2 — gdzie szukać
Demonstracja, kroki 3–5; Warsztat karta A: marzec — dni przepr. 11, zmienne 200; lipiec — dni przepr. 5, zmienne 87.

## Podpowiedź 3 — częściowy przykład
Szkic: 11 miesięcy po 5 800 (marzec po uzupełnieniu też 5 800) = 63 800 × 0,8629 = 55 053,02 / 11 = 5 004,82 → / 30 = 166,83 → × 0,8 = 133,46…

## Pełne rozwiązanie
```
Okres: XI 2025 – X 2026 (12 miesięcy przed listopadem).
Składniki: stałe 5 400 ✔, premia regulaminowa (pomniejszana proporcjonalnie za chorobę) ✔, dodatek stażowy 108 — wypłacany w pełnej wysokości za czas choroby → NIE wchodzi (art. 41 ust. 1).
Miesiące: 10 pełnych: 5 400 + 400 = 5 800; marzec 2026: 11/22 dni = dokładnie 50% → NIE jest „mniej niż połowa” → zostaje, uzupełniony: stałe 5 400 w pełnej kwocie + premia 200/11 × 22 = 400 → 5 800; lipiec 2026: 5/23 < 50% → WYŁĄCZONY.
Suma 11 miesięcy: 63 800 × (1 − 0,1371) = 55 053,02; średnia 55 053,02 / 11 = 5 004,82 ≥ minimum 4 147,10 ✔.
Stawka dzienna: 5 004,82 / 30 = 166,83; 80% = 133,46 zł; za 15 dni listopada: 9 dni chorobowego 1 201,14 + 6 dni zasiłku 800,76.
Ta sama podstawa obowiązuje przy kolejnym zwolnieniu, jeśli przerwa między zwolnieniami jest krótsza niż 1 pełny miesiąc kalendarzowy (art. 43).
```

## Oczekiwany wynik
okres XI 2025–X 2026; dodatek stażowy pomijasz; lipiec wyłączony (5/23 < 50%); marzec uzupełniony: 5 400 + 200/11 × 22 = 5 800; 11 miesięcy × 5 800 = 63 800 × 0,8629 → średnia 5 004,82; stawka dzienna 166,83; 80% = 133,46 zł/dzień — to stawka dla zwolnienia listopadowego; dla marca i lipca podstawę liczyłeś z ich własnych 12 miesięcy.

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co by się zmieniło, gdyby zmienił się jeden fakt (etat, staż, data, kwota)?
