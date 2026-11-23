# Rozwiązanie — ćwiczenie 2 (samodzielne) — GitHub Actions i pytest-html: testy uruchamiane przy każdym pushu

Najpierw własna próba. Podpowiedzi odkrywaj po kolei.

## Podpowiedź 1
CI instaluje TYLKO to, co jest w requirements.txt.

## Podpowiedź 2
Lokalnie pakiet masz „od dawna”.

## Podpowiedź 3
YAML nie akceptuje tabulatorów we wcięciach.

## Rozwiązanie
(1) brak requests w requirements.txt — lokalnie był zainstalowany ręcznie; (2) dopisz (albo `pip freeze` w .venv projektu) i push; (3) znak Tab we wcięciu linii 9 — YAML wymaga spacji.

## Oczekiwany wynik
(1) requests nie ma w requirements.txt; (2) dopisz requests do requirements.txt i push; (3) Tab zamiast spacji (albo zła składnia) w YAML.

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co się zmieni, gdy zmienisz jedną daną (granicę, typ, plik)?
