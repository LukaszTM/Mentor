# Przykład — Korekty ZUS: po błędzie, po 30-krotności, po kontroli; nadpłaty i zwroty
Tydzień 10

**Dyrektor 28 000 zł — przekroczenie 30-krotności w listopadzie, którego nikt nie zauważył**

```
Dyrektor 28 000 zł brutto/mies.; limit 282 600: po 10 miesiącach podstawa 280 000; listopad: do limitu 2 600 (emerytalna/rentowa od 2 600), od 25 400 tylko chorobowa, wypadkowa; grudzień — od całości bez emerytalno-rentowej. Kadry nie zauważyły i naliczyły pełne składki w listopadzie: korekta 02 12 2026 (RCA listopad wypłacony w grudniu): nadpłata pracownika 11,26% × 25 400 = 2 860,04 (zwrot), pracodawcy 16,26% × 25 400 = 4 130,04 (zaliczenie); zdrowotna wzrośnie o 9% × 2 860,04 = 257,40, podatek o 32% × 2 860,04 ≈ 915 → pracownik dostaje netto ok. 1 687,64; zwrot wykazujesz jako przychód w miesiącu wypłaty zwrotu.
```

## Omówienie — co robi każdy krok i dlaczego
1. „po 10 miesiącach podstawa 280 000; listopad: do limitu 2 600”: limit rocznej podstawy emerytalno-rentowej 282 600 (30 × prognozowane przeciętne 9 420); w listopadzie składki emerytalne i rentowe tylko od 2 600, od 25 400 — tylko chorobowa, wypadkowa, zdrowotna; w grudniu — od całości bez emerytalnej i rentowej.
2. „kadry naliczyły pełne składki w listopadzie → korekta 02 12 2026”: pensja listopadowa wypłacona 10.12 → komplet 01 12 2026 był błędny → komplet korygujący z identyfikatorem 02 12 2026: DRA (cały, z nowymi sumami) + RCA tylko dyrektora (zmieniony); RSA bez zmian — nie dołączasz.
3. „nadpłata pracownika 11,26% × 25 400 = 2 860,04 (zwrot), pracodawcy 16,26% × 25 400 = 4 130,04 (zaliczenie)”: pracownik: emerytalna 9,76 + rentowa 1,5; pracodawca: 9,76 + 6,5; nadpłatę pracodawca może zaliczyć na bieżące składki lub wnioskować o zwrot (RZS-P); część pracownika musi mu zwrócić.
4. „zdrowotna wzrośnie o 9% × 2 860,04 = 257,40, podatek o 32% × 2 860,04 ≈ 915”: zwrócone składki były odliczone od podstawy zdrowotnej i PIT → zwrot jest przychodem pracownika w miesiącu wypłaty zwrotu: zdrowotna 9% od zwrotu, zaliczka wg stawki pracownika (dyrektor — 32%); netto zwrotu ≈ 2 860,04 − 257,40 − 915 = 1 687,64.
5. „zwrot wykazujesz jako przychód w miesiącu wypłaty zwrotu”: nie korygujesz PIT-11 wstecz — zwrot jest przychodem bieżącym (art. 12 ust. 1 PIT, interpretacje); w RCA bieżącym — bez składek społecznych od zwrotu (to nie wynagrodzenie), tylko zdrowotna.
6. Gdyby pracownik miał dwóch pracodawców: limit pilnuje sam przez oświadczenie o przekroczeniu (art. 19 ust. 6); ZUS zawiadamia o przekroczeniu i wskazuje, który płatnik koryguje.

✔ Oczekiwany wynik: komplet 02 12 2026 (DRA + RCA dyrektora), zwrot pracownikowi 2 860,04 brutto (netto ≈ 1 687,64), zaliczenie 4 130,04 u pracodawcy, pismo do pracownika z informacją o PIT.

## Jak to uruchomić
1. Warsztat → Lista płac: Zasadnicze 28000, Podst. emer.-rent. narast. 280000 → „Policz” → krok „Podstawa emerytalno-rentowa ograniczona limitem 30-krotności (282 600,00) → 2 600,00”.
2. Warsztat → eZUS / Płatnik → Rozliczenie: miesiąc 2026-12, identyfikator 01 → Wyślij (komplet pierwotny); potem identyfikator 02 → „Pokaż komplet” → Weryfikuj → Wyślij — symulator sprawdza, że 01 już istnieje i że 02 nie był użyty.
3. Spróbuj wysłać ponownie 01 → błąd „Identyfikator 01 12 2026 został już użyty — korekta wymaga kolejnego numeru”.
4. Oczekiwany wynik: Rejestr z kompletami 01 i 02 za 12/2026; w pliku cwiczenia/tydzien_10/zus_korekty_1.md rozliczenie nadpłat.
