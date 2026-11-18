# Przykład — Korekty ZUS: po błędzie, po 30-krotności, po kontroli; nadpłaty i zwroty
Tydzień 10

**Dyrektor 28 000 zł — przekroczenie 30-krotności w listopadzie, którego nikt nie zauważył**

```
Dyrektor zatrudniony od 1.01.2026, 28 000 zł brutto/mies., wypłata 10. dnia następnego miesiąca. Limit 282 600: po 10 wypłatach roku (10.02–10.11) podstawa 280 000; wypłata 10.12 (pensja za listopad): emerytalna i rentowa tylko od 2 600, od pozostałych 25 400 — chorobowa, wypadkowa, zdrowotna, FP, FGŚP. Kadry nie zauważyły i naliczyły pełne składki: korekta 02 12 2026: nadpłata pracownika 11,26% × 25 400 = 2 860,04 (zwrot), pracodawcy 16,26% × 25 400 = 4 130,04 (zaliczenie); zdrowotna wzrośnie o 9% × 2 860,04 = 257,40, podatek o 32% × 2 860,04 ≈ 915 → pracownik dostaje netto ok. 1 687,64. Wypłata 8.01.2027 to już nowy rok: limit 2027 (300 990 zł) liczysz od zera.
```

## Omówienie — co robi każdy krok i dlaczego
1. „po 10 wypłatach roku podstawa 280 000; wypłata 10.12: do limitu 2 600”: limit rocznej podstawy emerytalno-rentowej 282 600 (30 × prognozowane przeciętne 9 420) liczysz według wypłat w roku kalendarzowym; przy wypłacie 10.12 składki emerytalne i rentowe tylko od 2 600, od 25 400 — tylko chorobowa, wypadkowa, zdrowotna (i FP, FGŚP); wypłata 8.01.2027 otwiera nowy limit (300 990 zł).
2. „kadry naliczyły pełne składki → korekta 02 12 2026”: pensja listopadowa wypłacona 10.12 → komplet 01 12 2026 był błędny → komplet korygujący z identyfikatorem 02 12 2026: DRA (cały, z nowymi sumami) + RCA tylko dyrektora (zmieniony); RSA bez zmian — nie dołączasz.
3. „nadpłata pracownika 11,26% × 25 400 = 2 860,04 (zwrot), pracodawcy 16,26% × 25 400 = 4 130,04 (zaliczenie)”: pracownik: emerytalna 9,76 + rentowa 1,5; pracodawca: 9,76 + 6,5; nadpłatę pracodawca może zaliczyć na bieżące składki lub wnioskować o zwrot (RZS-P); część pracownika musi mu zwrócić.
4. „zdrowotna wzrośnie o 9% × 2 860,04 = 257,40, podatek o 32% × 2 860,04 ≈ 915”: zwrócone składki były odliczone od podstawy zdrowotnej i od dochodu. Zdrowotna: podstawa grudniowej wypłaty rośnie o 2 860,04 → dopłata 257,40 w RCA korygującym 02 12 2026. PIT: zwrot w tym samym roku zwiększa dochód przy najbliższej liście (odliczasz mniej składek) → zaliczka wyższa o 32% × 2 860,04 ≈ 915 (dyrektor jest po progu); do ręki ≈ 2 860,04 − 257,40 − 915 = 1 687,64.
5. Zwrot po zamknięciu roku: nie korygujesz PIT-11 wstecz — zwrot jest wtedy przychodem ze stosunku pracy w miesiącu wypłaty (art. 12 ust. 1 PIT, interpretacje KIS); od samego zwrotu nie ma składek społecznych (to nie wynagrodzenie), a zdrowotną dopłacasz w korekcie RCA za miesiąc nadpłaty.
6. Gdyby pracownik miał dwóch pracodawców: limit pilnuje sam przez oświadczenie o przekroczeniu (art. 19 ust. 6); ZUS zawiadamia o przekroczeniu i wskazuje, który płatnik koryguje.

✔ Oczekiwany wynik: komplet 02 12 2026 (DRA + RCA dyrektora), zwrot pracownikowi 2 860,04 brutto (netto ≈ 1 687,64), zaliczenie 4 130,04 u pracodawcy, pismo do pracownika z informacją o PIT.

## Jak to uruchomić
1. Warsztat → Lista płac: Zasadnicze 28000, Podst. emer.-rent. narast. 280000 → „Policz” → krok „Podstawa emerytalno-rentowa ograniczona limitem 30-krotności (282 600,00) → 2 600,00”.
2. Warsztat → eZUS / Płatnik → Rozliczenie: miesiąc 2026-12, identyfikator 01 → Wyślij (komplet pierwotny); potem identyfikator 02 → „Pokaż komplet” → Weryfikuj → Wyślij — symulator sprawdza, że 01 już istnieje i że 02 nie był użyty.
3. Spróbuj wysłać ponownie 01 → błąd „Identyfikator 01 12 2026 został już użyty — korekta wymaga kolejnego numeru”.
4. Oczekiwany wynik: Rejestr z kompletami 01 i 02 za 12/2026; w pliku cwiczenia/tydzien_10/zus_korekty_1.md rozliczenie nadpłat.
