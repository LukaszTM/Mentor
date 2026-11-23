# Rozwiązanie — ćwiczenie 2 (samodzielne) — Moduły standardowe: random i datetime

Najpierw własna próba. Podpowiedzi odkrywaj po kolei.

## Podpowiedź 1
Co sprawia, że random daje te same wyniki?

## Podpowiedź 2
Ziarno ustawiasz przed losowaniem.

## Podpowiedź 3
choice może trafić dwa razy w to samo.

## Rozwiązanie
(1) losowość bez seed — test niepowtarzalny (flaky); (2) `random.seed(1)` (wartość dowolna, byle stała) i oczekiwany wynik dopasowany do tego ziarna; (3) sample.

## Oczekiwany wynik
(1) losowanie bez ziarna; (2) random.seed(1); (3) sample.

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co się zmieni, gdy zmienisz jedną daną (granicę, typ, plik)?
