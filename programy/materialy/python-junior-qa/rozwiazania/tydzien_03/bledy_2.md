# Rozwiązanie — ćwiczenie 2 (samodzielne) — Obsługa błędów: try / except / else / finally i raise

Najpierw własna próba. Podpowiedzi odkrywaj po kolei.

## Podpowiedź 1
Numer linii jest w linii File.

## Podpowiedź 2
Nazwa po „in”.

## Podpowiedź 3
len(koszyk) == 0 oznacza…

## Rozwiązanie
(1) linia 14; (2) cena_koszyka; (3) pusty koszyk (len = 0); (4) `if not koszyk: return 0` (albo jasny komunikat) — except: pass ukryłby problem.

## Oczekiwany wynik
(1) 14; (2) cena_koszyka; (3) pusty koszyk; (4) sprawdzenie pustego koszyka.

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co się zmieni, gdy zmienisz jedną daną (granicę, typ, plik)?
