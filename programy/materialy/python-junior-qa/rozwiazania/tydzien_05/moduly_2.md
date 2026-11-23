# Rozwiązanie — ćwiczenie 2 (samodzielne) — Podział kodu na moduły i import własnych plików

Najpierw własna próba. Podpowiedzi odkrywaj po kolei.

## Podpowiedź 1
Zapis/odczyt to praca z plikiem.

## Podpowiedź 2
Operacje na zadaniach to logika.

## Podpowiedź 3
input() tylko w interfejsie.

## Rozwiązanie
(1) plik.py; (2) zadania.py; (3) main.py; (4) plik.py; (5) Twój csv.py przykryje moduł csv — błędy typu AttributeError: module 'csv' has no attribute 'DictReader'.

## Oczekiwany wynik
(1) plik.py; (2) zadania.py; (3) main.py; (4) plik.py; (5) Python zaimportuje Twój csv.py zamiast modułu standardowego.

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co się zmieni, gdy zmienisz jedną daną (granicę, typ, plik)?
