# Rozwiązanie — ćwiczenie 1 (prowadzone) — Dane: CSV z arkusza i JSON — wczytaj, policz, zapisz

Najpierw własna próba. Podpowiedzi odkrywaj po kolei.

## Podpowiedź 1
repr pokazuje ukryte znaki w zapisie \u….

## Podpowiedź 2
Lipiec: 1080 + 3528.

## Podpowiedź 3
Klucze słownika sum: lipiec i sierpień.

## Rozwiązanie
Pierwsza kolumna ma na początku BOM \ufeff — w prawdziwym pliku usuwa go encoding="utf-8-sig". Lipiec 4608,00 zł, 2 miesiące.

## Oczekiwany wynik
(1) \ufeff (BOM); (2) 4608,00; (3) 2.

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co się zmieni, gdy zmienisz jedną daną (granicę, typ, plik)?
