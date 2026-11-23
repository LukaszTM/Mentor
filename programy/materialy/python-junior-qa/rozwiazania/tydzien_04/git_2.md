# Rozwiązanie — ćwiczenie 2 (samodzielne) — Git w zespole: gałęzie, diff, log, cofanie zmian i pull request

Najpierw własna próba. Podpowiedzi odkrywaj po kolei.

## Podpowiedź 1
Restore wraca do stanu z ostatniego commita.

## Podpowiedź 2
Stash odkłada zmiany na półkę.

## Podpowiedź 3
Revert nie przepisuje historii, którą inni już mają.

## Rozwiązanie
(1) `git restore raport.py`; (2) `git stash` (potem `git stash pop`); (3) `git revert <sha>`; (4) `git diff`.

## Oczekiwany wynik
(1) git restore raport.py; (2) git stash; (3) git revert <sha>; (4) git diff.

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co się zmieni, gdy zmienisz jedną daną (granicę, typ, plik)?
