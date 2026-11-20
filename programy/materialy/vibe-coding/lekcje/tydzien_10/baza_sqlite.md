# Baza danych SQLite: tabela, zapis, wyszukiwanie — bez SQL injection
Tydzień 10 · lekcja 33 z 48 · ≈ 50 min

**Po tej lekcji potrafisz:** tworzysz tabelę SQLite, zapisujesz i wyszukujesz dane z Pythona zapytaniami z parametrami (?), rozumiesz SQL injection i rozpoznajesz niebezpieczny kod od agenta.

**Po co mi to?** Lista gości w pliku przestaje wystarczać, gdy aplikacja ma zapisywać rezerwacje. SQLite jest wbudowany w Pythona — a SQL injection to jedna z najstarszych i wciąż częstych dziur w kodzie, także generowanym przez AI.

## Czego potrzebujesz
- Lekcja „Aplikacja Flask”.
- Moduł sqlite3 (wbudowany w Pythona — nic nie instalujesz).

## 1 · Wyjaśnienie od podstaw
### Baza = plik z tabelami
SQLite trzyma całą bazę w jednym pliku (np. pod_lipa.db). Tabela ma kolumny i wiersze — jak arkusz, ale z typami i regułami. Język zapytań to SQL.
```
CREATE TABLE IF NOT EXISTS goscie (
  id INTEGER PRIMARY KEY,
  imie TEXT NOT NULL,
  email TEXT NOT NULL UNIQUE,
  noce INTEGER NOT NULL CHECK (noce >= 1)
)
```
### Python + sqlite3
```
import sqlite3
con = sqlite3.connect("pod_lipa.db")
con.execute(CREATE_GOSCIE)
with con:   # zatwierdza (commit) albo wycofuje przy błędzie
    cur = con.execute("INSERT INTO goscie (imie, email, noce) VALUES (?, ?, ?)", (imie, email, noce))
nowe_id = cur.lastrowid
wiersz = con.execute("SELECT id, imie, email, noce FROM goscie WHERE email = ?", (email,)).fetchone()
```
### SQL injection — dlaczego znaki ? są obowiązkowe
Niebezpieczne (agent czasem tak pisze):
`con.execute(f"SELECT * FROM goscie WHERE email = '{email}'")`
Jeśli ktoś wpisze w formularzu e-mail `x' OR '1'='1`, zapytanie staje się `… WHERE email = 'x' OR '1'='1'` — zwraca WSZYSTKICH gości. Inne wpisy mogą usunąć dane. Dokumentacja sqlite3 mówi wprost: używaj placeholderów zamiast formatowania napisów. OWASP: zapytania parametryzowane to główna obrona.
| zapis | bezpieczny? |
|---|---|
| `execute("… WHERE email = ?", (email,))` | tak |
| `execute(f"… WHERE email = '{email}'")` | NIE |
| `execute("… WHERE email = '%s'" % email)` | NIE |
| `execute("… WHERE email = '" + email + "'")` | NIE |
Uwaga na krotkę jednoelementową: `(email,)` — z przecinkiem.
### Reguły w bazie
NOT NULL, UNIQUE i CHECK pilnują danych nawet, gdy kod się pomyli: drugi gość z tym samym e-mailem → sqlite3.IntegrityError. Twój kod zamienia go na czytelny komunikat (albo ValueError).
### Testy z bazą
W testach baza w pamięci: `sqlite3.connect(":memory:")` — szybka, znika po teście, nie miesza danych. Dlatego funkcje przyjmują połączenie (`con`) jako parametr.

## 2 · Demonstracja — krok po kroku
**Atak na wyszukiwarkę gości i jego zablokowanie**

```
import sqlite3

con = sqlite3.connect(":memory:")
con.execute("CREATE TABLE goscie (id INTEGER PRIMARY KEY, imie TEXT, email TEXT UNIQUE)")
with con:
    con.execute("INSERT INTO goscie (imie, email) VALUES (?, ?)", ("Anna", "anna@pod-lipa.pl"))
    con.execute("INSERT INTO goscie (imie, email) VALUES (?, ?)", ("Piotr", "piotr@pod-lipa.pl"))

zly = "x' OR '1'='1"
print(con.execute("SELECT COUNT(*) FROM goscie WHERE email = ?", (zly,)).fetchone()[0])
print(con.execute(f"SELECT COUNT(*) FROM goscie WHERE email = '{zly}'").fetchone()[0])

```

1. Agent napisał znajdz_po_emailu z f-stringiem. Test normalny: anna@pod-lipa.pl → Anna. Działa.
2. Wpisujesz e-mail `x' OR '1'='1` → funkcja zwraca pierwszego gościa z bazy, choć taki e-mail nie istnieje. W wersji „lista wyników” — wszystkich.
3. Przykład lekcji pokazuje to liczbowo: zapytanie z ? zwraca 0, z f-stringiem — 2.
4. Prośba: „wszystkie zapytania wyłącznie z placeholderami ?, żadnego formatowania SQL”. Test: zapis gościa z e-mailem `x' OR '1'='1` zapisuje dokładnie ten napis, a wyszukiwanie innego e-maila zwraca None.
5. Dopisujesz zasadę do AGENTS.md: „SQL tylko z parametrami ?”.

✔ **Oczekiwany wynik:** Wyszukiwarka odporna na SQL injection, potwierdzona testem z „podejrzanym” e-mailem; zasada utrwalona w instrukcjach agenta.

## 3 · Jak to uruchomić
1. Zadanie tygodnia „baza.py” → testy użyją bazy :memory: → „✔ Sprawdź wynik”.

## W praktyce
- Każde zapytanie SQL od agenta — szukasz f" i + w execute.
- Funkcje bazy przyjmują połączenie jako parametr.

## 4 · Ćwiczenie prowadzone
Co wypisze przykład lekcji (dwie liczby)? Która linia jest podatna na SQL injection: pierwsza (z ?) czy druga (z f-stringiem)? Jak zapiszesz krotkę z jednym parametrem email? Czas: 15 minut.

📄 `cwiczenia/tydzien_10/baza_sqlite_1.md` · rozwiązanie: `rozwiazania/tydzien_10/baza_sqlite_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Które zapisy są bezpieczne? (1) `execute("DELETE FROM goscie WHERE id = ?", (gid,))` (2) `execute("DELETE FROM goscie WHERE id = " + str(gid))` (3) `execute("SELECT * FROM goscie WHERE imie = '%s'" % imie)` (4) `execute("SELECT * FROM goscie WHERE imie = ?", (imie,))`. Podaj numery bezpiecznych rosnąco. Jaki wyjątek rzuci sqlite3 przy drugim gościu z tym samym e-mailem (UNIQUE)? Czas: 15 minut.

📄 `cwiczenia/tydzien_10/baza_sqlite_2.md` · rozwiązanie: `rozwiazania/tydzien_10/baza_sqlite_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **„sqlite3.ProgrammingError: Incorrect number of bindings supplied”.**
  - Przyczyna: `(email)` zamiast `(email,)` — napis traktowany jak sekwencja znaków.
  - Jak sprawdzić: Liczba ? vs elementy krotki.
  - Poprawka: Krotka z przecinkiem: (email,).
- ✘ **Dane „znikają” po zamknięciu programu.**
  - Przyczyna: Brak commit (zapis bez with con: ani con.commit()).
  - Jak sprawdzić: Czy INSERT jest w bloku with con:?
  - Poprawka: with con: wokół zapisów.
- ✘ **„sqlite3.OperationalError: no such table: goscie”.**
  - Przyczyna: Tabela nie utworzona w tej bazie (inna ścieżka pliku, :memory: w innym połączeniu).
  - Jak sprawdzić: Ścieżka pliku bazy, kolejność wywołań.
  - Poprawka: CREATE TABLE IF NOT EXISTS przy połączeniu (funkcja polacz).

## Pułapki
- Plik bazy z danymi gości nie trafia do Gita (.gitignore: *.db) — to dane osobowe.
- Agent „naprawia” IntegrityError przez usunięcie UNIQUE z tabeli — to osłabienie reguły, nie poprawka.

## Dodatkowe zadania
1. Zbuduj baza.py z polacz, dodaj_goscia, znajdz_po_emailu, lista_gosci (zadanie tygodnia).
2. Dopisz *.db do .gitignore.
3. Zasada „SQL tylko z ?” w AGENTS.md.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Czym jest SQL injection?**
  - Wstrzyknięciem fragmentu SQL przez dane użytkownika wklejone do zapytania jako tekst.
- **Jak się przed nim bronisz?**
  - Zapytania parametryzowane (?) zamiast formatowania napisów.
- **Po co baza :memory: w testach?**
  - Szybka, izolowana baza znikająca po teście.

## Co potrafię teraz bez patrzenia na przykład?
Tworzysz tabelę z regułami, zapisujesz i wyszukujesz zapytaniami z ?, rozpoznajesz SQL injection w kodzie agenta i testujesz na bazie w pamięci.

## Źródła (data dostępu w nawiasie)
Narzędzia, ceny i przepisy zmieniają się — przed użyciem w pracy otwórz źródło.
- Python — sqlite3 (placeholders ?, ostrzeżenie o SQL injection) (dostęp 20.11.2026) — <https://docs.python.org/3/library/sqlite3.html>
- OWASP — SQL Injection Prevention Cheat Sheet (dostęp 20.11.2026) — <https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html>
- Veracode — GenAI Code Security Report (30.07.2025) (dostęp 20.11.2026) — <https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Bezpieczne zapytanie w sqlite3:
  - A) f"… = '{x}'"
  - B) "… = ?", (x,)
  - C) "… = '" + x + "'"
  - D) "… = '%s'" % x
- `x' OR '1'='1` w podatnym wyszukiwaniu po e-mailu:
  - A) Nic nie zwraca
  - B) Zwraca wszystkich gości
  - C) Usuwa bazę zawsze
  - D) Błąd składni zawsze
- Reguła blokująca dwa takie same e-maile:
  - A) NOT NULL
  - B) UNIQUE
  - C) CHECK
  - D) PRIMARY
- Plik bazy z danymi gości w Gicie:
  - A) Commitujesz
  - B) Dodajesz *.db do .gitignore
  - C) Wysyłasz na Pages
  - D) Wklejasz do README

Odpowiedzi: B, B, B, B
