# Rozwiązanie — ćwiczenie 1 (prowadzone) — Czas pracy: normy, systemy, okresy rozliczeniowe, odpoczynek
Plik startowy: `cwiczenia/tydzien_02/czas_pracy_systemy_1.md`

Zasada: najpierw własna próba. Podpowiedzi odkrywaj po kolei — rozwiązanie dopiero na końcu.

## Podpowiedź 1 — pytanie naprowadzające
Które święta 2027 wypadają w dni inne niż niedziela? (1.01 pt, 6.01 śr, 29.03 pon, 1.05 sb, 3.05 pon, 27.05 czw, 15.08 nd — nie obniża, 1.11 pon, 11.11 czw, 24.12 pt, 25.12 sb, 26.12 nd — nie obniża.)

## Podpowiedź 2 — gdzie szukać
Warsztat → Czas pracy pokazuje w wyniku listę świąt obniżających w danym miesiącu — użyj do kontroli, nie zamiast rachunku.

## Podpowiedź 3 — częściowy przykład
Styczeń 2027: 1.01 piątek → pełne tygodnie 1–28.01 = 4 × 40 = 160; 29.01 (pt) wystaje = +8 → 168; święta: 1.01 (pt) i 6.01 (śr) = −16 → 152 h.

## Pełne rozwiązanie
```
Styczeń 2027: 1–28.01 = 4 tygodnie × 40 = 160; 29.01 piątek +8 = 168; święta 1.01 (pt), 6.01 (śr): −16 → 152 h; dni pracy 19.
Kwiecień 2027: 1–28.04 = 160; 29.04 (czw), 30.04 (pt) +16 = 176; święta: brak (Wielkanoc 28.03, Poniedziałek Wielkanocny 29.03 — marzec) → 176 h; dni pracy 22.
Maj 2027: 1–28.05 = 160; 31.05 (pon) +8 = 168; święta: 1.05 (sobota — obniża i daje dzień wolny), 3.05 (pon), 27.05 Boże Ciało (czw): −24 → 144 h; dni pracy 19 (+1 dzień wolny do oddania za 1.05).
Kontrola: Warsztat → Czas pracy → 152 / 176 / 144.
```

## Oczekiwany wynik
styczeń 2027: 168 − 8 (1.01 pt) − 8 (6.01 śr) = 152 h; kwiecień 2027: 22 dni pon–pt × 8 = 176 h (Wielkanoc 28.03 i Poniedziałek Wielkanocny 29.03 są w marcu); maj 2027: 21 dni pon–pt × 8 = 168 − 8 (1.05 sobota) − 8 (3.05 pon) − 8 (Boże Ciało 27.05 czw) = 144 h.

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co by się zmieniło, gdyby zmienił się jeden fakt (etat, staż, data, kwota)?
