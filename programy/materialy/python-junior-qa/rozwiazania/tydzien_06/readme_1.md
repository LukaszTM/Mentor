# Rozwiązanie — ćwiczenie 1 (prowadzone) — README, docstringi, PEP 8 i refaktoryzacja

Najpierw własna próba. Podpowiedzi odkrywaj po kolei.

## Podpowiedź 1
Najpierw brutto każdej ceny (× 1.23, round 2).

## Podpowiedź 2
Porównaj sumę brutto z progiem 100.

## Podpowiedź 3
81.31 × 1.23 = 100.0113 → 100.01.

## Rozwiązanie
(1) 50 × 1.23 = 61.50 i 31.3 × 1.23 = 38.499 → 38.50; suma 100.00 ≥ 100 → dostawa darmowa → 100.00. (2) 81.31 × 1.23 = 100.0113 → 100.01, dostawa darmowa → 100.01. (3) 81.30 × 1.23 = 99.999 → round do groszy daje 100.00 → próg osiągnięty → 100.00. Wniosek testera: zaokrąglenie przed porównaniem z progiem zmienia wynik — to warto opisać w wymaganiach.

## Oczekiwany wynik
(1) 100.00 (darmowa dostawa); (2) 100.01; (3) 100.00 — po zaokrągleniu brutto do groszy próg 100 zł jest osiągnięty.

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co się zmieni, gdy zmienisz jedną daną (granicę, typ, plik)?
