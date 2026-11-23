# Klasy i obiekty: __init__, self, metody, __str__
Tydzień 5 · lekcja 20 z 39 · ≈ 45 min

**Po tej lekcji potrafisz:** definiujesz klasę z __init__ i atrybutami, piszesz metody zmieniające stan obiektu (z walidacją), tworzysz kilka obiektów i czytelnie je wypisujesz przez __str__.

**Po co mi to?** Page Object Model w Selenium (tydzień 8) to klasy; frameworki testowe i biblioteki są zbudowane z klas. Tester musi je czytać i pisać.

## Czego potrzebujesz
- Lekcje „Funkcje”, „Słowniki”, „Obsługa błędów”.

## 1 · Wyjaśnienie od podstaw
### Klasa i obiekt
**Klasa** to wzór (formularz „Produkt”: nazwa, cena, ilość), **obiekt** to wypełniony egzemplarz (Zeszyt A5, 4.50, 120). Z jednej klasy tworzysz wiele obiektów.
```
class Produkt:
    def __init__(self, nazwa, cena, ilosc=0):
        self.nazwa = nazwa
        self.cena = cena
        self.ilosc = ilosc
```
`__init__` uruchamia się przy tworzeniu obiektu: `z = Produkt("Zeszyt A5", 4.5, 120)`. **self** to „ten konkretny obiekt” — `self.ilosc` to ilość TEGO produktu, nie wszystkich.
### Metody
Funkcja w klasie, pierwszym parametrem zawsze `self`: `def wartosc(self): return self.cena * self.ilosc`. Wywołanie: `z.wartosc()` (self przekazuje Python).
Metoda może zmieniać stan i pilnować reguł: `def wydaj(self, n): if n > self.ilosc: raise ValueError(...)`, potem `self.ilosc -= n`.
### __str__
`print(z)` bez `__str__` pokaże `<__main__.Produkt object at 0x…>`. Metoda `__str__(self)` zwraca czytelny napis: „Zeszyt A5 — 4.50 zł, 120 szt.”.
### Kiedy klasa, a kiedy słownik
Słownik — same dane. Klasa — dane **i** operacje z regułami (wydaj nie zejdzie poniżej zera). W testach łatwiej sprawdzić metodę klasy niż rozproszone funkcje.
### dataclass (dla ciekawych)
`from dataclasses import dataclass` i `@dataclass` nad klasą generuje __init__ i __repr__ automatycznie. W kursie piszesz __init__ ręcznie — żeby rozumieć, co się dzieje.

## 2 · Demonstracja — krok po kroku
**Klasa Produkt z regułami magazynu**

```
class Produkt:
    def __init__(self, nazwa, cena, ilosc=0):
        self.nazwa = nazwa
        self.cena = cena
        self.ilosc = ilosc

    def wartosc(self):
        return round(self.cena * self.ilosc, 2)

    def przyjmij(self, n):
        if n <= 0:
            raise ValueError("ilość musi być dodatnia")
        self.ilosc += n

    def wydaj(self, n):
        if n <= 0 or n > self.ilosc:
            raise ValueError(f"nie można wydać {n} szt. (stan: {self.ilosc})")
        self.ilosc -= n

    def __str__(self):
        return f"{self.nazwa} — {self.cena:.2f} zł, {self.ilosc} szt."


zeszyt = Produkt("Zeszyt A5", 4.5, 120)
klej = Produkt("Klej w sztyfcie", 3.4)
klej.przyjmij(50)
zeszyt.wydaj(20)
for p in [zeszyt, klej]:
    print(p, "| wartość:", p.wartosc())
try:
    klej.wydaj(80)
except ValueError as e:
    print("Błąd:", e)

```

1. `class Produkt:` — definicja wzoru; nazwy klas wielką literą (PEP 8).
2. `__init__(self, nazwa, cena, ilosc=0)` — zapisuje dane w atrybutach `self.…`; ilość domyślnie 0.
3. `wartosc(self)` — liczy z atrybutów tego obiektu; round do groszy.
4. `przyjmij` i `wydaj` zmieniają `self.ilosc`, ale najpierw walidują — wydanie więcej niż stan rzuca ValueError.
5. `__str__` — co pokaże print(obiekt).
6. Dwa obiekty z jednej klasy mają osobne ilości: wydanie zeszytów nie zmienia kleju.
7. Próba wydania 80 sztuk kleju przy stanie 50 → komunikat błędu, stan bez zmian.

✔ **Oczekiwany wynik:** Dwie linie produktów z wartościami (450.0 i 170.0) i „Błąd: nie można wydać 80 szt. (stan: 50)”.

## 3 · Jak to uruchomić
1. Zapisz jako produkt.py → ▶ Uruchom.
2. Usuń `__str__` i uruchom — zobacz, co wypisuje print bez niego.

## W praktyce
- Klasa strony (Page Object) = lokatory + metody akcji; testy wołają metody, nie lokatory.
- Testujesz metody klasy: poprawne dane, granice, wyjątki.

## 4 · Ćwiczenie prowadzone
Dla klasy z demonstracji: `p = Produkt("Kredki", 12.9, 40)`, potem `p.wydaj(15)`, `p.przyjmij(5)`. Podaj: (1) `p.ilosc`, (2) `p.wartosc()`, (3) co zwróci `str(p)`. Czas: 15 minut.

📄 `cwiczenia/tydzien_05/klasy_1.md` · rozwiązanie: `rozwiazania/tydzien_05/klasy_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Kolega dopisał metodę `def rabat(procent): return self.cena * (1 - procent / 100)`. Wywołanie `p.rabat(10)` daje błąd. (1) Jaki (wybierz)? (2) Czego brakuje w def (wpisz poprawną pierwszą linię)? (3) Co powinna zwrócić poprawiona metoda dla ceny 12.9 i 10% (z round do 2 miejsc)? Czas: 15 minut.

📄 `cwiczenia/tydzien_05/klasy_2.md` · rozwiązanie: `rozwiazania/tydzien_05/klasy_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **TypeError: wydaj() takes 1 positional argument but 2 were given**
  - Przyczyna: Brak self w definicji metody.
  - Jak sprawdzić: Pierwszy parametr metody?
  - Poprawka: def wydaj(self, n):
- ✘ **AttributeError: 'Produkt' object has no attribute 'ilosc'**
  - Przyczyna: W __init__ zabrakło self.ilosc = … (albo literówka).
  - Jak sprawdzić: Wypisz `vars(obiekt)`.
  - Poprawka: Ustaw wszystkie atrybuty w __init__.
- ✘ **NameError: name 'ilosc' is not defined w metodzie**
  - Przyczyna: Użycie `ilosc` zamiast `self.ilosc`.
  - Jak sprawdzić: Czy atrybut ma self.?
  - Poprawka: Atrybuty obiektu zawsze przez self.

## Pułapki
- Atrybut klasy (poza __init__) wspólny dla wszystkich obiektów — dane obiektu zawsze w __init__ przez self.
- Metoda zmieniająca stan bez walidacji — ujemne stany w magazynie.

## Dodatkowe zadania
1. Klasa Produkt: atrybuty, metoda opis(), 3 obiekty.
2. Metody przyjmij/wydaj z ValueError.
3. __str__ i wypisanie listy obiektów pętlą.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Czym różni się klasa od obiektu?**
  - Klasa to wzór, obiekt — konkretny egzemplarz.
- **Co oznacza self?**
  - Obiekt, na którym wywołano metodę.
- **Po co __str__?**
  - Czytelny napis przy print(obiekt).

## Co potrafię teraz bez patrzenia na przykład?
Definiujesz klasy z __init__, atrybutami i metodami z walidacją, tworzysz wiele obiektów i wypisujesz je czytelnie.

## Źródła (data dostępu w nawiasie)
Wersje narzędzi i dane rynkowe zmieniają się — przed użyciem w pracy otwórz źródło.
- Python — Poradnik: Klasy (dostęp 23.11.2026) — <https://docs.python.org/pl/3/tutorial/classes.html>
- PEP 8 — Style Guide for Python Code (dostęp 23.11.2026) — <https://peps.python.org/pep-0008/>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Co oznacza self w metodzie?
  - A) Klasę
  - B) Konkretny obiekt, na którym wywołano metodę
  - C) Moduł
  - D) Nic
- __init__ uruchamia się:
  - A) przy imporcie
  - B) przy tworzeniu obiektu
  - C) przy print
  - D) nigdy
- print(obiekt) bez __str__ wypisze:
  - A) atrybuty
  - B) <…object at 0x…>
  - C) błąd
  - D) nic
- Nazwa klasy wg PEP 8:
  - A) produkt
  - B) Produkt
  - C) PRODUKT
  - D) produkt_klasa

Odpowiedzi: B, B, B, B
