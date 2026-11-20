# Rozwiązanie — ćwiczenie 2 (samodzielne) — Testy jako umowa z agentem: pytest od zera

Najpierw własna próba. Podpowiedzi odkrywaj po kolei.

## Podpowiedź 1
Blok z kontekstem zaczyna się od with.

## Podpowiedź 2
Funkcja pomocnicza pytest dla wyjątków ma w nazwie „raises”.

## Podpowiedź 3
Różnica >= i > ujawnia się tylko na samej granicy.

## Rozwiązanie
`with pytest.raises(ValueError):` + wywołanie w środku; mutant >= → > złapie tylko przypadek 7 nocy.

## Oczekiwany wynik
`with pytest.raises(ValueError):`; test musi zawierać dokładnie 7 nocy.

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co się zmieni, gdy zmienisz jedną daną (granicę, typ, plik)?
