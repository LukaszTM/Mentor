# Ćwiczenie 2 (samodzielne) — Baza danych SQLite: tabela, zapis, wyszukiwanie — bez SQL injection
Tydzień 10 · lekcja `baza_sqlite`

## Zadanie
Które zapisy są bezpieczne? (1) `execute("DELETE FROM goscie WHERE id = ?", (gid,))` (2) `execute("DELETE FROM goscie WHERE id = " + str(gid))` (3) `execute("SELECT * FROM goscie WHERE imie = '%s'" % imie)` (4) `execute("SELECT * FROM goscie WHERE imie = ?", (imie,))`. Podaj numery bezpiecznych rosnąco. Jaki wyjątek rzuci sqlite3 przy drugim gościu z tym samym e-mailem (UNIQUE)? Czas: 15 minut.

## Jak sprawdzić
1. Zrób ćwiczenie (w Mentorze: Lekcje → ta lekcja → pola „Twoje odpowiedzi”; kod uruchamiasz w pliku .py w PRACA).
2. Utknąłeś? Podpowiedzi po kolei w Mentorze albo w pliku rozwiązania — najpierw podpowiedź 1.
3. Po własnej próbie: `rozwiazania/tydzien_10/baza_sqlite_2.md`.

## Twoja odpowiedź

(pisz tutaj)
