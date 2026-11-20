# Rozwiązanie — ćwiczenie 1 (prowadzone) — Baza danych SQLite: tabela, zapis, wyszukiwanie — bez SQL injection

Najpierw własna próba. Podpowiedzi odkrywaj po kolei.

## Podpowiedź 1
Z ? cały napis jest porównywany jako e-mail — takiego nie ma.

## Podpowiedź 2
W f-stringu napis staje się częścią SQL: OR '1'='1' jest zawsze prawdą.

## Podpowiedź 3
Krotka jednoelementowa ma przecinek.

## Rozwiązanie
0 (bezpiecznie), 2 (atak zwrócił wszystkich); podatna wersja z f-stringiem; (email,).

## Oczekiwany wynik
0 i 2; podatna druga (f-string); krotka (email,).

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co się zmieni, gdy zmienisz jedną daną (granicę, typ, plik)?
