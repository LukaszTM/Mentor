# Rozwiązanie — ćwiczenie 1 (prowadzone) — Wynagrodzenie chorobowe i zasiłek chorobowy: 33/14 dni, okres zasiłkowy, e-ZLA
Plik startowy: `cwiczenia/tydzien_07/chorobowe_podstawy_1.md`

Zasada: najpierw własna próba. Podpowiedzi odkrywaj po kolei — rozwiązanie dopiero na końcu.

## Podpowiedź 1 — pytanie naprowadzające
Co zeruje pulę 33 dni, a co zeruje okres zasiłkowy 182 dni? (Nowy rok vs przerwa > 60 dni.)

## Podpowiedź 2 — gdzie szukać
Demonstracja, kroki 2–5; Warsztat → Zasiłki → karta B z trzema nieobecnościami i stawką 133,46.

## Podpowiedź 3 — częściowy przykład
Szkic: 12 + 12 = 24 → zostaje 9; listopad 15 dni = 9 + 6; kwoty = dni × 133,46; przerwy: 20.03→20.07 (> 60), 31.07→16.11 (> 60) → trzy osobne okresy zasiłkowe…

## Pełne rozwiązanie
```
| Zwolnienie | Dni | Chorobowe (pracodawca) | Zasiłek (ZUS) | Kwoty | Okres zasiłkowy | RSA |
|---|---|---|---|---|---|---|
| 9–20.03 | 12 | 12 (pula: użyto 12/33) | 0 | 12 × 133,46 = 1 601,52 | 1. okres: 12/182 | 331 |
| 20–31.07 | 12 | 12 (użyto 24/33) | 0 | 1 601,52 | przerwa 121 dni > 60 → 2. okres: 12/182 | 331 |
| 16–30.11 | 15 | 9 (użyto 33/33) | 6 (25–30.11) | 9 × 133,46 = 1 201,14 + 6 × 133,46 = 800,76 | przerwa 107 dni > 60 → 3. okres: 15/182 (kod A nie ma znaczenia przy przerwie > 60 dni) | 331 (16–24.11), 313 (25–30.11) |
Pensja listopadowa: 5 400 − 5 400/30 × 15 = 2 700 + 1 201,14 (zdrowotna + PIT) + 800,76 (tylko PIT). Zasiłek 800,76 firma odlicza w DRA 12/2026 (wypłata 10.12).
```

## Oczekiwany wynik
marzec 12 dni chorobowego (1 601,52; pula 21); lipiec 12 dni chorobowego (1 601,52; pula 9); listopad 15 dni: 9 chorobowego (1 201,14) + 6 zasiłku (800,76); okresy zasiłkowe: marzec (12), lipiec — przerwa 20.03→20.07 = 121 dni → nowy (12), listopad — przerwa 31.07→16.11 = 107 dni → nowy okres mimo kodu A (ta sama choroba liczy się do jednego okresu tylko przy przerwie ≤ 60 dni) (15); RSA: 331 (III, VII, 16–24.11) i 313 (25–30.11).

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co by się zmieniło, gdyby zmienił się jeden fakt (etat, staż, data, kwota)?
