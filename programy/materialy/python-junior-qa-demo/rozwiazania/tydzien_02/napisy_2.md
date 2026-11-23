# Rozwiązanie — ćwiczenie 2 (samodzielne) — Napisy i ich metody: upper, lower, strip, split, replace, len, wycinki

Najpierw własna próba. Podpowiedzi odkrywaj po kolei.

## Podpowiedź 1
„d” i „D” to różne znaki.

## Podpowiedź 2
Sprowadź oba napisy do małych liter.

## Podpowiedź 3
strip() usuwa spacje z frazy.

## Rozwiązanie
(1) False — wielkość liter; (2) `return fraza.strip().lower() in nazwa.lower()`; (3) True.

## Oczekiwany wynik
(1) False; (2) fraza.strip().lower() in nazwa.lower(); (3) True.

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co się zmieni, gdy zmienisz jedną daną (granicę, typ, plik)?
