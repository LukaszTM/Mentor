# Rozwiązanie — ćwiczenie 2 (samodzielne) — pytest: test_, assert, uruchamianie, pytest.raises i pytest.approx

Najpierw własna próba. Podpowiedzi odkrywaj po kolei.

## Podpowiedź 1
Test bez assert sprawdza tylko, że nie było wyjątku.

## Podpowiedź 2
Mutant różni się zachowaniem dokładnie na granicy.

## Podpowiedź 3
Opcja wyboru po nazwie: -k.

## Rozwiązanie
(1) tak — bez assert test niczego nie sprawdza; (2) `assert rabat(200) == 5` (mutant zwróci 0); (3) `python -m pytest -k rabat`.

## Oczekiwany wynik
(1) tak; (2) assert rabat(200) == 5; (3) python -m pytest -k rabat.

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co się zmieni, gdy zmienisz jedną daną (granicę, typ, plik)?
