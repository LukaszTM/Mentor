# Rozwiązanie — ćwiczenie 2 (samodzielne) — Moduł csv: DictReader, DictWriter i statystyki z pliku

Najpierw własna próba. Podpowiedzi odkrywaj po kolei.

## Podpowiedź 1
Napisy porównuje się jak w słowniku — od pierwszego znaku.

## Podpowiedź 2
„7” > „4” > „2”.

## Podpowiedź 3
Zamień na liczbę w key.

## Rozwiązanie
(1) „7.50” — jako napis zaczyna się od 7, największego pierwszego znaku; (2) porównanie napisów; (3) `key=lambda w: float(w["cena"])` → 24.99.

## Oczekiwany wynik
(1) 7.50; (2) porównuje napisy znak po znaku; (3) key=lambda w: float(w["cena"]).

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co się zmieni, gdy zmienisz jedną daną (granicę, typ, plik)?
