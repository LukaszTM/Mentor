# Rozwiązanie — ćwiczenie 2 (samodzielne) — Powtórka etapu 2: projekt jak w zespole — struktura, Git, środowisko, czytanie cudzego kodu

Najpierw własna próba. Podpowiedzi odkrywaj po kolei.

## Podpowiedź 1
Co jest zagrożeniem bezpieczeństwa, a co tylko estetyką?

## Podpowiedź 2
Klucz w publicznym repo boty znajdują w minuty.

## Podpowiedź 3
Usunięcie pliku nie usuwa klucza z historii.

## Rozwiązanie
(1)–(4) nie, (5) tak. Pierwszy: (4) — unieważnij klucz u dostawcy, usuń z kodu, przenieś do .env w .gitignore. Potem .venv (git rm --cached), README, a stare commity zostaw — nowe pisz porządnie.

## Oczekiwany wynik
(1) nie; (2) nie; (3) nie; (4) nie; (5) tak; pierwszy: 4 (klucz API — natychmiast unieważnić i usunąć).

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co się zmieni, gdy zmienisz jedną daną (granicę, typ, plik)?
