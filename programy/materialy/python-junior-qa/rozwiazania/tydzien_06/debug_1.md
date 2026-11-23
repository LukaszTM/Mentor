# Rozwiązanie — ćwiczenie 1 (prowadzone) — Debugowanie: print, breakpoint() i debugger krok po kroku

Najpierw własna próba. Podpowiedzi odkrywaj po kolei.

## Podpowiedź 1
2 × 3 + 5 × 2.

## Podpowiedź 2
= nadpisuje, += dodaje.

## Podpowiedź 3
Po pierwszym obrocie suma = 2.0 × 3.

## Rozwiązanie
(1) 6 + 10 = 16.0; (2) `suma += cena * ilosc` — `=` nadpisywało sumę; (3) po pierwszym obrocie suma = 6.0.

## Oczekiwany wynik
(1) 16.0; (2) suma += cena * ilosc; (3) 6.0.

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co się zmieni, gdy zmienisz jedną daną (granicę, typ, plik)?
