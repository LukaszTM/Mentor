# Rozwiązanie — ćwiczenie 2 (samodzielne) — SQLite i plan projektu: tabele, CREATE/INSERT/SELECT/UPDATE/DELETE, zapytania z parametrami

Najpierw własna próba. Podpowiedzi odkrywaj po kolei.

## Podpowiedź 1
Dane wklejone w tekst SQL stają się kodem.

## Podpowiedź 2
Znak zapytania i krotka z wartością.

## Podpowiedź 3
Ograniczenia tabeli zgłaszają IntegrityError.

## Rozwiązanie
(1) tak; (2) `return con.execute("SELECT * FROM produkty WHERE nazwa = ?", (nazwa,)).fetchall()`; (3) pustą listę — nie ma produktu o takiej dosłownej nazwie; (4) `sqlite3.IntegrityError: CHECK constraint failed`.

## Oczekiwany wynik
(1) tak; (2) return con.execute("SELECT * FROM produkty WHERE nazwa = ?", (nazwa,)).fetchall(); (3) pustą listę; (4) sqlite3.IntegrityError.

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co się zmieni, gdy zmienisz jedną daną (granicę, typ, plik)?
