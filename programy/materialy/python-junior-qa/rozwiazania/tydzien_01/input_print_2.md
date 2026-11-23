# Rozwiązanie — ćwiczenie 2 (samodzielne) — print i input — rozmowa programu z użytkownikiem

Najpierw własna próba. Podpowiedzi odkrywaj po kolei.

## Podpowiedź 1
Metoda usuwająca spacje z brzegów napisu.

## Podpowiedź 2
Ilość zamień na int, nazwę zostaw jako str.

## Podpowiedź 3
f"Dodano: {ilosc} × {nazwa}".

## Rozwiązanie
`nazwa = input("Produkt: ").strip()`, `ilosc = int(input("Ilość: "))`, `print(f"Dodano: {ilosc} × {nazwa}")` → „Dodano: 3 × zeszyt A5”.

## Oczekiwany wynik
(1) input("Produkt: ").strip(); (2) Dodano: 3 × zeszyt A5.

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co się zmieni, gdy zmienisz jedną daną (granicę, typ, plik)?
