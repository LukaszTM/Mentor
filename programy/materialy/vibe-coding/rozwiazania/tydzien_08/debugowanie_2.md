# Rozwiązanie — ćwiczenie 2 (samodzielne) — Debugowanie z AI: odtwórz, zawęź, wyjaśnij, napraw, zabezpiecz testem

Najpierw własna próba. Podpowiedzi odkrywaj po kolei.

## Podpowiedź 1
%m to miesiąc, %d dzień — tu na odwrót.

## Podpowiedź 2
05 trafia jako miesiąc.

## Podpowiedź 3
Miesiąc 20 nie istnieje.

## Rozwiązanie
Bez wyjątku, ale miesiąc 5 zamiast 7 (cichy błąd); dla 20.12 — ValueError (miesiąc 20).

## Oczekiwany wynik
(1) nie; (2) 5 (maj); (3) ValueError.

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co się zmieni, gdy zmienisz jedną daną (granicę, typ, plik)?
