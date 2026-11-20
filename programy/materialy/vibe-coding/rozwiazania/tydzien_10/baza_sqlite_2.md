# Rozwiązanie — ćwiczenie 2 (samodzielne) — Baza danych SQLite: tabela, zapis, wyszukiwanie — bez SQL injection

Najpierw własna próba. Podpowiedzi odkrywaj po kolei.

## Podpowiedź 1
Bezpieczne mają ? i krotkę parametrów.

## Podpowiedź 2
Sklejanie i % to formatowanie napisu SQL.

## Podpowiedź 3
Naruszenie reguły UNIQUE — błąd integralności.

## Rozwiązanie
1 i 4 (parametry). Duplikat UNIQUE → sqlite3.IntegrityError.

## Oczekiwany wynik
Bezpieczne: 1 i 4 → „14”; IntegrityError.

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co się zmieni, gdy zmienisz jedną daną (granicę, typ, plik)?
