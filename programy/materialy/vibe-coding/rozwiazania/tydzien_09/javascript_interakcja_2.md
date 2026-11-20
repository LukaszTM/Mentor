# Rozwiązanie — ćwiczenie 2 (samodzielne) — JavaScript na stronie: formularz liczy koszt bez serwera

Najpierw własna próba. Podpowiedzi odkrywaj po kolei.

## Podpowiedź 1
„of null” — nie znalazł elementu.

## Podpowiedź 2
Specyfikacja mówi: pola noce i osoby.

## Podpowiedź 3
Formularz domyślnie przeładowuje stronę.

## Rozwiązanie
querySelector zwrócił null (brak #noc) → popraw selektor na #noce; miganie = brak e.preventDefault().

## Oczekiwany wynik
(1) null; (2) selektor w JS na "#noce"; (3) e.preventDefault().

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co się zmieni, gdy zmienisz jedną daną (granicę, typ, plik)?
