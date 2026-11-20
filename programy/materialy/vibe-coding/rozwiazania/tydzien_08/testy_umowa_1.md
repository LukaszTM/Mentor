# Rozwiązanie — ćwiczenie 1 (prowadzone) — Testy jako umowa z agentem: pytest od zera

Najpierw własna próba. Podpowiedzi odkrywaj po kolei.

## Podpowiedź 1
Każdy znak to jeden test.

## Podpowiedź 2
F na trzeciej pozycji.

## Podpowiedź 3
200 to cena wysoka, 150 niska — który sezon policzyła funkcja?

## Rozwiązanie
5 testów, pierwszy F na pozycji 3; 150 = cena sezonu niskiego → w kodzie brakuje 12 na liście sezonu wysokiego.

## Oczekiwany wynik
(1) 5; (2) trzeci; (3) tak — grudzień potraktowany jak sezon niski (150 to cena niska Klonowego).

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co się zmieni, gdy zmienisz jedną daną (granicę, typ, plik)?
