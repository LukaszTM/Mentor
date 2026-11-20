# Rozwiązanie — ćwiczenie 2 (samodzielne) — Przegląd zmian agenta: czytasz diff jak recenzent

Najpierw własna próba. Podpowiedzi odkrywaj po kolei.

## Podpowiedź 1
Plus = dodane = nowa wersja.

## Podpowiedź 2
Różnica między >= a > dotyczy tylko wartości równej granicy.

## Podpowiedź 3
Poczekalnia po angielsku: staged.

## Rozwiązanie
Nowa: noce > 7; różnica tylko dla 7 nocy (rabat znika); git diff --staged pokazuje zmiany w poczekalni.

## Oczekiwany wynik
(1) `if noce > 7:` (z plusem); (2) dla 7 nocy; (3) git diff --staged.

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co się zmieni, gdy zmienisz jedną daną (granicę, typ, plik)?
