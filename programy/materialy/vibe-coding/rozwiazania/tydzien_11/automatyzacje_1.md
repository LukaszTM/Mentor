# Rozwiązanie — ćwiczenie 1 (prowadzone) — Automatyzacje: skrypt porządkujący pliki z trybem próby i harmonogram

Najpierw własna próba. Podpowiedzi odkrywaj po kolei.

## Podpowiedź 1
suffix to rozszerzenie z kropką.

## Podpowiedź 2
Brak rozszerzenia → pusty suffix → domyślnie inne.

## Podpowiedź 3
Reguły mają małe litery.

## Rozwiązanie
zdjecia (dzięki .lower()), inne (brak rozszerzenia), inne (.txt nie ma reguły).

## Oczekiwany wynik
(1) zdjecia; (2) inne; (3) inne; .lower() zamienia .JPG na .jpg.

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co się zmieni, gdy zmienisz jedną daną (granicę, typ, plik)?
