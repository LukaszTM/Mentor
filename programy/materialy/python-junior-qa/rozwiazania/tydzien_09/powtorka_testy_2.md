# Rozwiązanie — ćwiczenie 2 (samodzielne) — Powtórka etapu 3: strategia testów małego projektu

Najpierw własna próba. Podpowiedzi odkrywaj po kolei.

## Podpowiedź 1
Proporcje odwrotne niż w piramidzie.

## Podpowiedź 2
Reguły biznesowe nie potrzebują przeglądarki.

## Podpowiedź 3
Granice 1 i 50 z sąsiadami + jedna klasa „nie-liczba”.

## Rozwiązanie
(1) odwrócona piramida (tzw. rożek lodów); (2) reguły → testy jednostkowe, E2E tylko krytyczne ścieżki; (3) 0, 1, 50, 51 i np. "abc" → 5.

## Oczekiwany wynik
(1) odwrócona piramida (rożek lodów); (2) przenieś sprawdzanie reguł do testów jednostkowych; (3) 5 (0, 1, 50, 51, nie-liczba).

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co się zmieni, gdy zmienisz jedną daną (granicę, typ, plik)?
