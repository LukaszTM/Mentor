# Rozwiązanie — ćwiczenie 1 (prowadzone) — Aplikacja internetowa we Flask: trasy, parametry, JSON i testy

Najpierw własna próba. Podpowiedzi odkrywaj po kolei.

## Podpowiedź 1
Poprawne dane — OK.

## Podpowiedź 2
type=int zwraca None dla „abc” → gałąź 400.

## Podpowiedź 3
Zły adres trasy — nie ma takiej strony.

## Rozwiązanie
200, 400 (abc → None), 400 (ValueError z koszt_pobytu → 400), 404 (brak trasy /api/cenaa).

## Oczekiwany wynik
(1) 200; (2) 400; (3) 400; (4) 404.

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co się zmieni, gdy zmienisz jedną daną (granicę, typ, plik)?
