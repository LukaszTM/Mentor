# Rozwiązanie — ćwiczenie 2 (samodzielne) — Dane: CSV z arkusza i JSON — wczytaj, policz, zapisz

Najpierw własna próba. Podpowiedzi odkrywaj po kolei.

## Podpowiedź 1
Niewidoczny znak na początku pliku.

## Podpowiedź 2
Domyślny separator csv to przecinek.

## Podpowiedź 3
float() rozumie tylko kropkę.

## Rozwiązanie
(1) BOM → utf-8-sig, (2) delimiter=";", (3) replace(",", "."), (4) ensure_ascii=False.

## Oczekiwany wynik
(1) BOM; (2) brak delimiter; (3) przecinek dziesiętny; (4) brak ensure_ascii=False.

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co się zmieni, gdy zmienisz jedną daną (granicę, typ, plik)?
