# Rozwiązanie — ćwiczenie 1 (prowadzone) — Komunikat błędu (traceback) — czytanie od dołu

Najpierw własna próba. Podpowiedzi odkrywaj po kolei.

## Podpowiedź 1
Ostatnia linia: nazwa przed dwukropkiem.

## Podpowiedź 2
Przedostatni wpis File…: line i in …

## Podpowiedź 3
Który z dwóch kluczy w tej linii może być liczbą nocy?

## Rozwiązanie
TypeError w line 8, in raport: napis + g["noce"] (int). Poprawka: f-string f"Gość: {g['imie']}, noce: {g['noce']}".

## Oczekiwany wynik
TypeError; linia 8; funkcja raport; klucz noce (liczba) — sklejanie napisu z int.

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co się zmieni, gdy zmienisz jedną daną (granicę, typ, plik)?
