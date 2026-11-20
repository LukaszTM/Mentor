# Rozwiązanie — ćwiczenie 2 (samodzielne) — Refaktoryzacja z agentem: lepszy kod, to samo zachowanie

Najpierw własna próba. Podpowiedzi odkrywaj po kolei.

## Podpowiedź 1
Każda powtarzana „magiczna” wartość → jedna stała.

## Podpowiedź 2
Stałe wielkimi literami, funkcje małymi z podkreśleniami.

## Podpowiedź 3
PEP 8: lowercase_with_underscores dla funkcji.

## Rozwiązanie
Dwie stałe; nazwa funkcji oblicz_przychod_miesieczny (PEP 8).

## Oczekiwany wynik
2 stałe (np. RABAT_DLUGI i SEZON_WYSOKI); funkcja: oblicz_przychod_miesieczny.

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co się zmieni, gdy zmienisz jedną daną (granicę, typ, plik)?
