# Rozwiązanie — ćwiczenie 2 (samodzielne) — Powtórka etapu 1: podstawy Pythona w jednym programie

Najpierw własna próba. Podpowiedzi odkrywaj po kolei.

## Podpowiedź 1
Indeks = nr - 1.

## Podpowiedź 2
pop(indeks) usuwa i zwraca element.

## Podpowiedź 3
Po usunięciu elementy się przesuwają.

## Rozwiązanie
`if not 1 <= nr <= len(zadania): raise ValueError(...)`; `return zadania.pop(nr - 1)["tytul"]`. Wynik: (1) „B”; (2) 2; (3) „C” — elementy przesunęły się w lewo.

## Oczekiwany wynik
(1) B; (2) 2; (3) C.

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co się zmieni, gdy zmienisz jedną daną (granicę, typ, plik)?
