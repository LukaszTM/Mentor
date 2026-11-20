# Rozwiązanie — ćwiczenie 1 (prowadzone) — Pierwszy program z AI: od specyfikacji do zielonego testu

Najpierw własna próba. Podpowiedzi odkrywaj po kolei.

## Podpowiedź 1
Policz 7 × 2 × 120.

## Podpowiedź 2
Porównaj z „otrzymano”.

## Podpowiedź 3
Dla 7 nocy rabat nie działa, a od 8 pewnie tak — który znak wyklucza samą granicę?

## Rozwiązanie
1680 = cena bez rabatu, czyli warunek nie objął 7 nocy → zamiast >= jest >. 1680·0,9 = 1512.0.

## Oczekiwany wynik
Bez rabatu: 7·2·120 = 1680 (to otrzymano) → rabat nie został naliczony; warunek najpewniej `noce > 7` zamiast `noce >= 7`.

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co się zmieni, gdy zmienisz jedną daną (granicę, typ, plik)?
