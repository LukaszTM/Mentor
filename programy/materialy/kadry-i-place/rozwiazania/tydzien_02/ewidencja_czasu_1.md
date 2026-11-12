# Rozwiązanie — ćwiczenie 1 (prowadzone) — Ewidencja czasu pracy i nieobecności
Plik startowy: `cwiczenia/tydzien_02/ewidencja_czasu_1.md`

Zasada: najpierw własna próba. Podpowiedzi odkrywaj po kolei — rozwiązanie dopiero na końcu.

## Podpowiedź 1 — pytanie naprowadzające
Ile godzin nocnych ma zmiana 18–6, jeśli pora nocna to 22–6?

## Podpowiedź 2 — gdzie szukać
Demonstracja, wiersz 3 i 4: nocne = część zmiany w porze nocnej; urlop = godziny z planu dnia.

## Podpowiedź 3 — częściowy przykład
Pierwsze wiersze: „01.12 wt | 06–18 | 12 | 0 | — | — | grafik”; „02.12 śr | — | 0 | — | — | W5 | —”; „03.12 czw | 18–06 | 12 | 8 | — | — | grafik”…

## Pełne rozwiązanie
```
| Data | Od–do | Godz. | Nocne | Nadg. | Kod | Uwagi |
|---|---|---|---|---|---|---|
| 01.12 wt | 06:00–18:00 | 12 | 0 | — | — | grafik |
| 02.12 śr | — | 0 | — | — | W5 | wolne z 5-dn. tygodnia |
| 03.12 czw | 18:00–06:00 | 12 | 8 | — | — | grafik |
| 04.12 pt | — | 0 | — | — | W5 | po nocy — odpoczynek |
| 05.12 sb | — | 0 | — | — | UW 12 h | urlop w dniu zaplanowanym na 12 h |
| 06.12 nd | — | 0 | — | — | WN | wolna niedziela |
| 07.12 pn | 06:00–18:00 | 12 | 0 | — | — | grafik |
| 08.12 wt | — | 0 | — | — | CH | e-ZLA nr … |
| 09.12 śr | — | 0 | — | — | CH | e-ZLA |
| 10.12 czw | 18:00–06:00 | 12 | 8 | — | — | grafik |
| 11.12 pt | — | 0 | — | — | W5 | |
| 12.12 sb | 06:00–20:00 | 14 | 0 | 2 (dobowe) | — | polecenie 7/12 |
| 13.12 nd | — | 0 | — | — | WN | |
| 14.12 pn | 06:00–18:00 | 12 | 0 | — | — | grafik |
| 15.12 wt | — | 0 | — | — | W5 | |
Suma 1–15.12: praca 74 h (w tym 2 nadgodziny), UW 12 h, CH 8–9.12 (2 dni), nocne 16 h.
```

## Oczekiwany wynik
15 wierszy; nocne tylko przy zmianach 18–6 (po 8 h); UW 12 h; CH 2 dni; nadgodziny 2 h z numerem polecenia; dni wolne z kodem W5/WN/WŚ.

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co by się zmieniło, gdyby zmienił się jeden fakt (etat, staż, data, kwota)?
