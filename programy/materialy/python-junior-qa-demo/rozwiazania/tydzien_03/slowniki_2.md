# Rozwiązanie — ćwiczenie 2 (samodzielne) — Słowniki i krotki: klucz → wartość

Najpierw własna próba. Podpowiedzi odkrywaj po kolei.

## Podpowiedź 1
Pętla po liście, z każdego słownika z["kwota"].

## Podpowiedź 2
max(zamowienia, key=lambda z: z["kwota"]).

## Podpowiedź 3
Brakujący klucz w [] daje błąd; get() — nie.

## Rozwiązanie
(1) 45.0 + 120.5 + 99.99 = 265.49; (2) nr 2; (3) tylko 120.5 → 1; (4) KeyError: 'klient' — bezpiecznie: z.get("klient").

## Oczekiwany wynik
(1) 265.49; (2) 2; (3) 1; (4) KeyError.

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co się zmieni, gdy zmienisz jedną daną (granicę, typ, plik)?
