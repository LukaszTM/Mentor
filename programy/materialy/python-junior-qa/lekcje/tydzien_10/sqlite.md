# SQLite i plan projektu: tabele, CREATE/INSERT/SELECT/UPDATE/DELETE, zapytania z parametrami
Tydzień 10 · lekcja 35 z 39 · ≈ 50 min

**Po tej lekcji potrafisz:** planujesz zakres projektu w PLAN.md, tworzysz bazę SQLite z dwiema tabelami, wykonujesz zapytania CREATE, INSERT, SELECT (WHERE, ORDER BY), UPDATE i DELETE z modułu sqlite3 — zawsze z parametrami `?` — i testujesz kod bazy na bazie w pamięci albo w tmp_path.

**Po co mi to?** Każda aplikacja trzyma dane w bazie, a tester sprawdza je zapytaniem SQL („czy zamówienie naprawdę się zapisało?”). Podstawy SQL są w większości ogłoszeń Junior QA.

## Czego potrzebujesz
- Lekcje „Funkcje”, „Słowniki”, „Obsługa błędów”, „parametrize i fixtures”.
- sqlite3 jest w bibliotece standardowej Pythona — nic nie instalujesz.

## 1 · Wyjaśnienie od podstaw
### Plan projektu przed kodem (PLAN.md)
Projekt portfolio to **Magazyn sklepu** „Papierowy Kot” (dane fikcyjne): produkty (nazwa, kategoria, cena, ilość) i operacje magazynowe (przyjęcie, wydanie, data). PLAN.md: cel w 2 zdaniach, zakres (co TAK, czego NIE), struktura plików, kolejność kroków (baza → logika → testy → web → testy E2E → README), ryzyka.
### Baza, tabela, wiersz
Baza SQLite to jeden plik (magazyn.db). Tabela jak arkusz: kolumny z typami, wiersze z danymi. **Klucz główny** (`id INTEGER PRIMARY KEY`) jednoznacznie identyfikuje wiersz — baza nadaje go sama.
```
CREATE TABLE IF NOT EXISTS produkty (
    id INTEGER PRIMARY KEY,
    nazwa TEXT NOT NULL UNIQUE,
    kategoria TEXT NOT NULL,
    cena REAL NOT NULL CHECK (cena >= 0),
    ilosc INTEGER NOT NULL DEFAULT 0
);
```
### Cztery podstawowe operacje (CRUD)
| operacja | SQL |
|---|---|
| dodaj | `INSERT INTO produkty (nazwa, kategoria, cena) VALUES (?, ?, ?)` |
| czytaj | `SELECT nazwa, cena FROM produkty WHERE kategoria = ? ORDER BY cena DESC` |
| zmień | `UPDATE produkty SET ilosc = ilosc + ? WHERE id = ?` |
| usuń | `DELETE FROM produkty WHERE id = ?` |
### sqlite3 w Pythonie
`con = sqlite3.connect("magazyn.db")` (w testach `":memory:"` albo `tmp_path / "test.db"`), `con.execute(sql, (wartosci,))`, `con.commit()` — zapisuje zmiany; `cur.fetchall()` / `fetchone()` — wyniki. `con.row_factory = sqlite3.Row` — wiersze dostępne po nazwie kolumny jak słownik. Blok `with con:` sam robi commit (albo wycofanie przy błędzie).
### Zawsze parametry `?` — nigdy f-string
`f"SELECT * FROM produkty WHERE nazwa = '{nazwa}'"` dla nazwy `x' OR '1'='1` zwróci WSZYSTKIE wiersze — to **SQL injection** (OWASP: jedna z najgroźniejszych podatności). Z `?` sterownik bezpiecznie przekazuje wartość jako dane, nie jako kod SQL.
### Testy bazy
Fixture tworzy pustą bazę w tmp_path, wywołuje funkcję tworzącą tabele i oddaje połączenie; każdy test dostaje świeżą bazę. Testujesz: dodanie i odczyt, UNIQUE (duplikat → sqlite3.IntegrityError), wydanie więcej niż stan (ValueError z logiki), kolejność ORDER BY.

## 2 · Demonstracja — krok po kroku
**Magazyn w bazie: tabela, CRUD i lekcja o SQL injection**

```
import sqlite3

con = sqlite3.connect(":memory:")
con.row_factory = sqlite3.Row
con.execute("""CREATE TABLE produkty (
    id INTEGER PRIMARY KEY, nazwa TEXT NOT NULL UNIQUE, kategoria TEXT NOT NULL,
    cena REAL NOT NULL CHECK (cena >= 0), ilosc INTEGER NOT NULL DEFAULT 0)""")
with con:
    con.executemany("INSERT INTO produkty (nazwa, kategoria, cena, ilosc) VALUES (?, ?, ?, ?)",
                    [("Zeszyt A5", "zeszyty", 4.5, 120), ("Segregator A4", "biuro", 11.9, 45), ("Zszywacz", "biuro", 19.9, 15)])
for w in con.execute("SELECT nazwa, cena FROM produkty WHERE kategoria = ? ORDER BY cena DESC", ("biuro",)):
    print(w["nazwa"], w["cena"])
with con:
    con.execute("UPDATE produkty SET ilosc = ilosc - ? WHERE nazwa = ?", (5, "Zszywacz"))
print("Zszywacz:", con.execute("SELECT ilosc FROM produkty WHERE nazwa = ?", ("Zszywacz",)).fetchone()["ilosc"])
try:
    with con:
        con.execute("INSERT INTO produkty (nazwa, kategoria, cena) VALUES (?, ?, ?)", ("Zeszyt A5", "zeszyty", 4.5))
except sqlite3.IntegrityError as e:
    print("Duplikat:", e)
zla = "x' OR '1'='1"
print("f-string:", len(con.execute(f"SELECT * FROM produkty WHERE nazwa = '{zla}'").fetchall()), "wierszy")
print("parametr ?:", len(con.execute("SELECT * FROM produkty WHERE nazwa = ?", (zla,)).fetchall()), "wierszy")

```

1. `sqlite3.connect(":memory:")` — baza w pamięci (znika po zakończeniu) — idealna do przykładów i testów. W projekcie: `"magazyn.db"`.
2. `row_factory = sqlite3.Row` — `w["nazwa"]` zamiast `w[0]`.
3. CREATE TABLE z ograniczeniami: NOT NULL, UNIQUE (nazwa nie może się powtórzyć), CHECK (cena ≥ 0), DEFAULT 0.
4. `with con:` + `executemany` — trzy INSERT-y w jednej transakcji, commit automatycznie.
5. SELECT z WHERE i ORDER BY cena DESC — produkty z kategorii biuro od najdroższego. Wartość kategorii przekazana jako parametr `?` w krotce `("biuro",)` (przecinek = krotka jednoelementowa!).
6. UPDATE `ilosc = ilosc - ?` — zmiana względem obecnej wartości; 15 − 5 = 10.
7. Drugi „Zeszyt A5” → IntegrityError z UNIQUE — baza pilnuje reguły nawet, gdy kod zapomni.
8. SQL injection: f-string zamienia dane w kod SQL i warunek `OR '1'='1'` zwraca wszystkie 3 wiersze; z `?` — 0 wierszy (szukana jest nazwa dosłownie).

✔ **Oczekiwany wynik:** Dwa produkty biurowe od najdroższego, „Zszywacz: 10”, komunikat UNIQUE i porównanie 3 wierszy (f-string) vs 0 (parametr).

## 3 · Jak to uruchomić
1. Zapisz jako baza_demo.py → ▶ Uruchom.
2. Podgląd pliku bazy (opcjonalnie): DB Browser for SQLite (sqlitebrowser.org) albo w terminalu Pythona `sqlite3.connect("magazyn.db").execute("SELECT * FROM produkty").fetchall()`.

## W praktyce
- Tester po akcji w aplikacji sprawdza SELECT-em, czy dane zapisały się poprawnie.
- W bug raporcie dotyczącym danych: zapytanie SQL i wynik.

## 4 · Ćwiczenie prowadzone
Tabela produkty z demonstracji (stan po UPDATE). Podaj wynik: (1) `SELECT COUNT(*) FROM produkty` , (2) `SELECT nazwa FROM produkty ORDER BY cena LIMIT 1`, (3) `SELECT SUM(ilosc) FROM produkty WHERE kategoria = 'biuro'`. Czas: 15 minut.

📄 `cwiczenia/tydzien_10/sqlite_1.md` · rozwiązanie: `rozwiazania/tydzien_10/sqlite_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Kolega napisał: `def znajdz(con, nazwa): return con.execute(f"SELECT * FROM produkty WHERE nazwa = '{nazwa}'").fetchall()`. (1) Czy to podatne na SQL injection (tak/nie)? (2) Wpisz poprawioną linię return. (3) Co zwróci poprawiona funkcja dla nazwy „Zeszyt A5' --”: wszystkie / pustą listę? (4) Jaki wyjątek rzuci INSERT z ceną -1 przy CHECK (cena >= 0) — wybierz. Czas: 15 minut.

📄 `cwiczenia/tydzien_10/sqlite_2.md` · rozwiązanie: `rozwiazania/tydzien_10/sqlite_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **Dane „znikają” po zamknięciu programu**
  - Przyczyna: Brak con.commit() (albo with con:).
  - Jak sprawdzić: Czy po INSERT/UPDATE jest commit?
  - Poprawka: `with con:` wokół zmian albo con.commit().
- ✘ **sqlite3.OperationalError: no such table: produkty**
  - Przyczyna: Tabela nie utworzona albo inny plik bazy (np. inny katalog roboczy).
  - Jak sprawdzić: Ścieżka do pliku .db.
  - Poprawka: CREATE TABLE IF NOT EXISTS przy starcie; ścieżka względem pliku programu.
- ✘ **sqlite3.ProgrammingError: Incorrect number of bindings supplied**
  - Przyczyna: `("biuro")` to napis, nie krotka.
  - Jak sprawdzić: Czy po pojedynczej wartości jest przecinek?
  - Poprawka: `("biuro",)`.

## Pułapki
- f-string w SQL — SQL injection; zawsze `?`.
- Testy na prawdziwym magazyn.db — testy zmieniają dane; zawsze :memory: albo tmp_path.

## Dodatkowe zadania
1. PLAN.md: cel, zakres TAK/NIE, struktura, kolejność, ryzyka.
2. baza.py: utworz_baze, dodaj_produkt, pobierz_produkty, zmien_ilosc, usun_produkt — z parametrami ?.
3. Testy bazy z fixturą tworzącą bazę w tmp_path.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Po co klucz główny?**
  - Jednoznacznie identyfikuje wiersz.
- **Jak bronisz się przed SQL injection?**
  - Zapytania parametryzowane (?), nigdy f-string z danymi.
- **Co robi with con:?**
  - Commit po bloku albo wycofanie zmian przy błędzie.

## Co potrafię teraz bez patrzenia na przykład?
Planujesz projekt, tworzysz tabele z ograniczeniami, wykonujesz CRUD w sqlite3 z parametrami ?, rozumiesz SQL injection i testujesz bazę na danych tymczasowych.

## Źródła (data dostępu w nawiasie)
Wersje narzędzi i dane rynkowe zmieniają się — przed użyciem w pracy otwórz źródło.
- Python — sqlite3: DB-API 2.0 interface for SQLite (placeholders ?) (dostęp 23.11.2026) — <https://docs.python.org/3/library/sqlite3.html>
- OWASP — SQL Injection Prevention Cheat Sheet (zapytania parametryzowane) (dostęp 23.11.2026) — <https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html>
- OWASP — Query Parameterization Cheat Sheet (dostęp 23.11.2026) — <https://cheatsheetseries.owasp.org/cheatsheets/Query_Parameterization_Cheat_Sheet.html>
- pytest — How to use temporary directories and files in tests (tmp_path) (dostęp 23.11.2026) — <https://docs.pytest.org/how-to/tmp_path.html>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Zapytanie bezpieczne przed SQL injection:
  - A) f"…WHERE id = {id}"
  - B) "…WHERE id = ?" z (id,)
  - C) "…WHERE id = " + str(id)
  - D) żadne
- SELECT … ORDER BY cena DESC zwraca:
  - A) od najtańszego
  - B) od najdroższego
  - C) losowo
  - D) tylko najdroższy
- Zmiany po INSERT trafiają do pliku bazy po:
  - A) SELECT
  - B) commit
  - C) close bez commit
  - D) print
- Baza w testach jednostkowych:
  - A) produkcyjna magazyn.db
  - B) :memory: albo tmp_path
  - C) na serwerze
  - D) w README

Odpowiedzi: B, B, B, B
