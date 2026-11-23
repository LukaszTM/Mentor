# Rozwiązanie — ćwiczenie 2 (samodzielne) — Biblioteka requests i API: GET, kody HTTP, JSON

Najpierw własna próba. Podpowiedzi odkrywaj po kolei.

## Podpowiedź 1
5xx przy złych danych od klienta to zawsze błąd serwera.

## Podpowiedź 2
Filtr bez wyników to poprawna, pusta odpowiedź.

## Podpowiedź 3
Argument ograniczający czas czekania.

## Rozwiązanie
(1) tak — 500 dla błędnego parametru to bug, a traceback ujawnia szczegóły serwera; (2) 200 z pustą listą `[]` (dopuszczalne też 400/404, jeśli tak mówi specyfikacja); (3) `timeout`.

## Oczekiwany wynik
(1) tak; (2) 200 z pustą listą (albo 404 — zależnie od specyfikacji; nigdy 500); (3) timeout.

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co się zmieni, gdy zmienisz jedną daną (granicę, typ, plik)?
