# Rozwiązanie — ćwiczenie 2 (samodzielne) — Pliki: open, read, write, with i kodowanie utf-8

Najpierw własna próba. Podpowiedzi odkrywaj po kolei.

## Podpowiedź 1
write przyjmuje tylko str.

## Podpowiedź 2
Argument z nazwą kodowania.

## Podpowiedź 3
Co się stanie, gdy błąd wystąpi przed f.close()?

## Rozwiązanie
(1) TypeError: can only concatenate str (not "float") — `str(123.5)` albo f-string; (2) `encoding="utf-8"`; (3) `with open(...) as f:` zamyka plik nawet przy błędzie.

## Oczekiwany wynik
(1) TypeError; (2) encoding="utf-8"; (3) blok with.

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co się zmieni, gdy zmienisz jedną daną (granicę, typ, plik)?
