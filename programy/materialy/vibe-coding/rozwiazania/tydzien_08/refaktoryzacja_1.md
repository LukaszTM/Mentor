# Rozwiązanie — ćwiczenie 1 (prowadzone) — Refaktoryzacja z agentem: lepszy kod, to samo zachowanie

Najpierw własna próba. Podpowiedzi odkrywaj po kolei.

## Podpowiedź 1
Pytanie kontrolne: czy zmienił się wynik dla jakichkolwiek danych?

## Podpowiedź 2
Zmiana rabatu zmienia wynik.

## Podpowiedź 3
Poprawka błędu też zmienia wynik — może być dobra, ale to nie refaktoryzacja.

## Rozwiązanie
Refaktoryzacja: 1 i 3 (wyniki bez zmian) = 2. Zmiana rabatu i poprawka zaokrąglenia zmieniają zachowanie — osobne, świadome commity.

## Oczekiwany wynik
Tak: 1 i 3 → 2 odpowiedzi „tak”; 2 i 4 zmieniają zachowanie (to zmiana funkcji / poprawka błędu — osobny commit).

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co się zmieni, gdy zmienisz jedną daną (granicę, typ, plik)?
