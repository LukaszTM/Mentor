# print i input — rozmowa programu z użytkownikiem
Tydzień 1 · lekcja 7 z 16 · ≈ 45 min

**Po tej lekcji potrafisz:** wypisujesz dane czytelnie (print z sep i end, f-string) i wczytujesz je od użytkownika input(), zamieniając na liczby int()/float() — wiedząc, że input() zawsze zwraca napis.

**Po co mi to?** Każdy program z formularzem przyjmuje tekst od człowieka. Tester sprawdza, co się dzieje, gdy człowiek wpisze coś innego niż oczekiwano.

## Czego potrzebujesz
- Lekcja „Zmienne i typy”.
- W Mentorze dane dla input() wpisujesz w polu nad wynikiem — jedna linia = jedna odpowiedź.

## 1 · Wyjaśnienie od podstaw
### print — wypisywanie
`print("a", "b", 3)` wypisuje `a b 3` — argumenty rozdziela spacją. `sep=";"` zmienia separator, `end=""` usuwa przejście do nowej linii. Pusty `print()` wstawia pustą linię.
### input — wczytywanie
`imie = input("Jak masz na imię? ")` — program wyświetla pytanie i czeka, aż użytkownik wpisze tekst i naciśnie Enter. **input() zawsze zwraca str**, nawet gdy wpiszesz 12.
Liczbę trzeba zamienić: `ilosc = int(input("Ilość: "))`, `cena = float(input("Cena: "))`. Kolejność: najpierw input (napis), potem int (liczba).
### Spacje i wielkość liter
Użytkownicy dopisują spacje. `.strip()` usuwa je z początku i końca: `input().strip()`. `.lower()` zamienia na małe litery — przydatne przy porównaniach „TAK”/„tak”.
### Program, który można przetestować
Mentor uruchamia Twój program z danymi wpisanymi w polu nad wynikiem — każda linia to kolejna odpowiedź dla input(). Weryfikatory robią to samo automatycznie z wieloma zestawami danych, także błędnymi.

## 2 · Demonstracja — krok po kroku
**Tabelka z print i wersja z input()**

```
nazwa = "Długopis niebieski"
cena = 2.3
ilosc = 4
print("Produkt:", nazwa)
print("Cena", "Ilość", "Razem", sep=" | ")
print(cena, ilosc, cena * ilosc, sep=" | ")
print("Wczytuję", end="")
print("...", end="")
print(" gotowe")
print(f"{nazwa}: {ilosc} szt. × {cena:.2f} zł = {cena * ilosc:.2f} zł")

```

1. `print("Produkt:", nazwa)` — dwa argumenty, spacja między nimi.
2. `sep=" | "` — zamiast spacji wstawia „ | ” między argumentami: powstaje tabelka.
3. `end=""` — print nie przechodzi do nowej linii; trzy printy dają jedną linię „Wczytuję... gotowe”.
4. Ostatni print: f-string z trzema wstawkami; `{cena:.2f}` → 2.30.
5. Wersja interaktywna: zamień linie 2–3 na `cena = float(input("Cena: "))` i `ilosc = int(input("Ilość: "))`. W Mentorze w polu danych wpisz dwie linie: `2.3` i `4`.
6. Wpisz `cztery` zamiast 4 → ValueError. To jest dokładnie to, co tester sprawdza: co robi program przy złych danych? (Obsługę błędów poznasz w tygodniu 3.)

✔ **Oczekiwany wynik:** Pięć linii; ostatnia: „Długopis niebieski: 4 szt. × 2.30 zł = 9.20 zł”.

## 3 · Jak to uruchomić
1. Zapisz jako paragon.py → ▶ Uruchom.
2. Wersja z input(): pole „Dane dla input()” nad wynikiem → wpisz 2.3 (Enter) 4 → ▶ Uruchom.

## W praktyce
- Testując pole liczbowe: liczba, liczba z przecinkiem, tekst, puste pole, spacje — 5 przypadków na start.
- Komunikaty w input() piszesz tak, by człowiek wiedział, co wpisać (jednostka, format).

## 4 · Ćwiczenie prowadzone
Program: `a = input("Pierwsza: ")`, `b = input("Druga: ")`, `print(a + b)`. Użytkownik wpisuje 12 i 5. (1) Co wypisze program? (2) Jak poprawić pierwszą linię, żeby dodawał liczby (wpisz linię)? (3) Co wtedy wypisze? Czas: 15 minut.

📄 `cwiczenia/tydzien_01/input_print_1.md` · rozwiązanie: `rozwiazania/tydzien_01/input_print_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Napisz w głowie (potem w Mentorze) program: pyta o nazwę produktu i ilość, wypisuje „Dodano: <ilość> × <nazwa>”. Użytkownik wpisuje „  zeszyt A5 ” (ze spacjami) i 3. (1) Jak wczytać nazwę bez spacji na brzegach (wpisz wyrażenie)? (2) Co wypisze program? Czas: 15 minut.

📄 `cwiczenia/tydzien_01/input_print_2.md` · rozwiązanie: `rozwiazania/tydzien_01/input_print_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **TypeError: unsupported operand type(s) for *: 'float' and 'str'**
  - Przyczyna: Liczba z input() nie została zamieniona: `cena * input()`.
  - Jak sprawdzić: `print(type(ilosc))`.
  - Poprawka: `ilosc = int(input(...))`.
- ✘ **EOFError: EOF when reading a line**
  - Przyczyna: Program czeka na dane, a nikt ich nie podał (pole danych w Mentorze puste).
  - Jak sprawdzić: Ile razy wywołujesz input()? Tyle linii danych potrzeba.
  - Poprawka: Wpisz dane w polu nad wynikiem — po jednej linii na każde input().

## Pułapki
- int(input()) przy wpisie „3.5” → ValueError; dla kwot używaj float().
- Komunikat w input() bez spacji na końcu: „Ilość:3” — dodaj spację po dwukropku.

## Dodatkowe zadania
1. Program pyta o cenę i ilość, wypisuje razem z :.2f.
2. Wypisz tabelkę 3 produktów z sep=" | ".
3. Sprawdź, co robi program przy wpisie „abc” — zapisz komunikat błędu.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Jakiego typu jest wynik input()?**
  - Zawsze str.
- **Co robi end="" w print?**
  - Nie przechodzi do nowej linii.
- **Po co .strip()?**
  - Usuwa spacje z początku i końca napisu.

## Co potrafię teraz bez patrzenia na przykład?
Wypisujesz czytelnie (sep, end, f-string), wczytujesz dane input() i zamieniasz je na liczby; wiesz, co dzieje się przy złym wpisie.

## Źródła (data dostępu w nawiasie)
Wersje narzędzi i dane rynkowe zmieniają się — przed użyciem w pracy otwórz źródło.
- Python — Poradnik: Wejście i wyjście (f-stringi, pliki) (dostęp 23.11.2026) — <https://docs.python.org/pl/3/tutorial/inputoutput.html>
- Python — Poradnik: Nieformalne wprowadzenie (liczby, napisy, listy) (dostęp 23.11.2026) — <https://docs.python.org/pl/3/tutorial/introduction.html>

## Test (w Mentorze: Lekcje → Sprawdź się)
- x = input() — użytkownik wpisał 7. type(x)?
  - A) int
  - B) str
  - C) float
  - D) zależy
- print(1, 2, sep="-") wypisze:
  - A) 1 2
  - B) 1-2
  - C) 12
  - D) -1-2-
- Brak danych dla input() w Mentorze kończy się:
  - A) ValueError
  - B) EOFError
  - C) TypeError
  - D) niczym
- "  abc ".strip() to:
  - A) "abc"
  - B) "  abc"
  - C) "abc "
  - D) "ABC"

Odpowiedzi: B, B, B, A
