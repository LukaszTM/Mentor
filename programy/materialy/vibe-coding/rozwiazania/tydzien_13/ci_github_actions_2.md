# Rozwiązanie — ćwiczenie 2 (samodzielne) — Automatyczne testy w chmurze: GitHub Actions (CI)

Najpierw własna próba. Podpowiedzi odkrywaj po kolei.

## Podpowiedź 1
Linux nie rozumie \ jako separatora.

## Podpowiedź 2
CI instaluje tylko to, co w requirements.

## Podpowiedź 3
Linux rozróżnia wielkość liter.

## Rozwiązanie
(1) pathlib zamiast \, (2) dopisać flask do requirements, (3) ujednolicić nazwę.

## Oczekiwany wynik
(1) ścieżka z ukośnikiem wstecznym (lub brak pliku w repo); (2) brak w requirements.txt; (3) wielkość liter.

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co się zmieni, gdy zmienisz jedną daną (granicę, typ, plik)?
