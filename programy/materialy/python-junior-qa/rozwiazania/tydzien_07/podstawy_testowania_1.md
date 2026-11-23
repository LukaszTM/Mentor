# Rozwiązanie — ćwiczenie 1 (prowadzone) — Podstawy testowania: pomyłka, defekt, awaria, poziomy testów, klasy równoważności i wartości brzegowe

Najpierw własna próba. Podpowiedzi odkrywaj po kolei.

## Podpowiedź 1
Granice to 8 i 20.

## Podpowiedź 2
Do każdej granicy jej sąsiad po złej stronie.

## Podpowiedź 3
Ile grup traktowanych tak samo: poniżej, w zakresie, powyżej.

## Rozwiązanie
Granice 8 i 20 plus sąsiedzi poza zakresem: 7, 8, 20, 21. Klasy: < 8, 8–20, > 20 → 3.

## Oczekiwany wynik
Wartości brzegowe: 7, 8, 20, 21; klasy równoważności: 3 (za krótkie, poprawne, za długie).

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co się zmieni, gdy zmienisz jedną daną (granicę, typ, plik)?
