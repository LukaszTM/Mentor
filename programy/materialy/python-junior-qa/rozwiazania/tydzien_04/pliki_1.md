# Rozwiązanie — ćwiczenie 1 (prowadzone) — Pliki: open, read, write, with i kodowanie utf-8

Najpierw własna próba. Podpowiedzi odkrywaj po kolei.

## Podpowiedź 1
int() radzi sobie z "10\n" — ignoruje końcową nową linię.

## Podpowiedź 2
Tryb w kasuje zawartość.

## Podpowiedź 3
\n przed 8 zaczyna nową linię.

## Rozwiązanie
(1) 10 + 25 + 5 = 40; (2) tryb w skasował wszystko → „7”; (3) „7\n8” = 2 linie.

## Oczekiwany wynik
(1) 40; (2) tylko 7; (3) 2 linie.

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co się zmieni, gdy zmienisz jedną daną (granicę, typ, plik)?
