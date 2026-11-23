# Rozwiązanie — ćwiczenie 1 (prowadzone) — Flask: strony, szablony, formularze z walidacją i komunikaty

Najpierw własna próba. Podpowiedzi odkrywaj po kolei.

## Podpowiedź 1
Sukces kończy się przekierowaniem.

## Podpowiedź 2
float("abc") → ValueError → komunikat.

## Podpowiedź 3
strip() z samych spacji daje pusty napis.

## Rozwiązanie
(1) 302 — zapis i redirect; (2) 400 — cena nie-liczba; (3) 400 — po strip() nazwa pusta; (4) 200.

## Oczekiwany wynik
(1) 302; (2) 400; (3) 400; (4) 200.

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co się zmieni, gdy zmienisz jedną daną (granicę, typ, plik)?
