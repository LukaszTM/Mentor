# Rozwiązanie — ćwiczenie 2 (samodzielne) — Komunikat błędu (traceback) — czytanie od dołu

Najpierw własna próba. Podpowiedzi odkrywaj po kolei.

## Podpowiedź 1
int() dostał napis, ale nie liczbę — dobry typ, zła wartość.

## Podpowiedź 2
Brak pliku ma własny wyjątek z „File” w nazwie.

## Podpowiedź 3
Nieznana nazwa zmiennej → „is not defined”.

## Rozwiązanie
(1) ValueError: invalid literal for int(); (2) FileNotFoundError; (3) ModuleNotFoundError: No module named 'pandass'; (4) NameError: name 'cena_kocowa' is not defined.

## Oczekiwany wynik
(1) ValueError, (2) FileNotFoundError, (3) ModuleNotFoundError, (4) NameError.

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co się zmieni, gdy zmienisz jedną daną (granicę, typ, plik)?
