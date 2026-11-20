# Rozwiązanie — ćwiczenie 1 (prowadzone) — Specyfikacja: „Gotowe, gdy…” — zamówienie, które da się sprawdzić

Najpierw własna próba. Podpowiedzi odkrywaj po kolei.

## Podpowiedź 1
2 osoby × 3 dni × 35 zł.

## Podpowiedź 2
4 × 7 × 35.

## Podpowiedź 3
Zero osób to wartość na granicy dopuszczalnych danych.

## Rozwiązanie
2·3·35 = 210; 1·1·35 = 35; 4·7·35 = 980. Osoby = 0 to przypadek brzegowy (sekcja „Przypadki brzegowe”).

## Oczekiwany wynik
(1) 210; (2) 35; (3) 980; „osoby = 0 → ValueError” → Przypadki brzegowe.

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co się zmieni, gdy zmienisz jedną daną (granicę, typ, plik)?
