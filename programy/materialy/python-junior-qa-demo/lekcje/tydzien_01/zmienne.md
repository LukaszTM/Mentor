# Zmienne i typy danych: int, float, str, bool
Tydzień 1 · lekcja 6 z 16 · ≈ 50 min

**Po tej lekcji potrafisz:** tworzysz zmienne, rozpoznajesz typy int, float, str i bool funkcją type(), liczysz operatorami + - * / // % ** i zamieniasz typy (int(), float(), str()).

**Po co mi to?** Każdy test porównuje wartości określonego typu: „5” to nie 5. Połowa błędów w aplikacjach (i w zgłoszeniach testerów) to złe typy danych.

## Czego potrzebujesz
- Lekcja „Terminal i pierwszy program”.
- Środowisko kursu w Mentorze (przycisk ▶ Uruchom).

## 1 · Wyjaśnienie od podstaw
### Zmienna = pudełko z etykietą
`cena = 4.50` — Python tworzy pudełko o nazwie cena i wkłada do niego 4.50. Znak `=` to **przypisanie** („włóż do pudełka”), nie porównanie. Nowe przypisanie podmienia zawartość.
Nazwy: małe litery i podkreślenia (`cena_brutto`), bez spacji i polskich znaków, nie zaczynają się cyfrą. Wielkość liter ma znaczenie: `Cena` i `cena` to dwie różne zmienne.
### Cztery podstawowe typy
| typ | co to | przykład |
|---|---|---|
| `int` | liczba całkowita | `ilosc = 120` |
| `float` | liczba z częścią ułamkową (kropka!) | `cena = 4.50` |
| `str` | napis (tekst w cudzysłowie) | `nazwa = "Zeszyt A5"` |
| `bool` | prawda/fałsz | `dostepny = True` |
`type(x)` mówi, jakiego typu jest wartość: `type(4.5)` → `<class 'float'>`.
### Operatory
`+ - *` jak w matematyce; `/` dzielenie zawsze daje float (`7 / 2` → 3.5); `//` dzielenie całkowite (`7 // 2` → 3); `%` reszta (`7 % 2` → 1); `**` potęga (`2 ** 3` → 8). Na napisach: `+` skleja (`"ab" + "cd"` → "abcd"), `*` powtarza (`"-" * 5`).
### Zamiana typów (rzutowanie)
`int("12")` → 12, `float("4.5")` → 4.5, `str(12)` → "12". `int("4,5")` da błąd ValueError — Python używa kropki. `"5" + 5` da TypeError: nie dodasz napisu do liczby.
### f-string — liczby w tekście
`f"Razem: {razem:.2f} zł"` wstawia wartość zmiennej w napis; `:.2f` to 2 miejsca po przecinku. Uwaga: float bywa niedokładny (`0.1 + 0.2` → 0.30000000000000004), dlatego kwoty wypisujesz z `:.2f`, a w testach porównujesz z tolerancją.

## 2 · Demonstracja — krok po kroku
**Paragon za 3 zeszyty — cztery typy w jednym programie**

```
nazwa = "Zeszyt A5 w kratkę"
cena = 4.50
ilosc = 3
dostepny = True

razem = cena * ilosc
print(nazwa, type(nazwa))
print(cena, type(cena))
print(ilosc, type(ilosc))
print(dostepny, type(dostepny))
print(f"Do zapłaty: {razem:.2f} zł")
print("Paczki po 4 szt.:", 10 // 4, "reszta:", 10 % 4)

```

1. `nazwa = "Zeszyt A5 w kratkę"` — napis (str) w cudzysłowie; polskie litery w napisach są w porządku.
2. `cena = 4.50` — float; Python wypisze go jako 4.5 (zera na końcu znikają).
3. `ilosc = 3` — int, liczba całkowita.
4. `dostepny = True` — bool; zawsze z wielkiej litery: True / False.
5. `razem = cena * ilosc` — wynik mnożenia float × int to float (13.5).
6. `print(nazwa, type(nazwa))` — wypisuje wartość i jej typ: `<class 'str'>`.
7. `f"Do zapłaty: {razem:.2f} zł"` — f-string: w klamrach wartość zmiennej, `:.2f` = dwa miejsca po przecinku → 13.50.
8. `10 // 4` → 2 pełne paczki, `10 % 4` → 2 sztuki reszty. Zmień 10 na 13 i przewidź wynik (3 i 1).

✔ **Oczekiwany wynik:** Sześć linii: cztery wartości z typami, „Do zapłaty: 13.50 zł” i „Paczki po 4 szt.: 2 reszta: 2”.

## 3 · Jak to uruchomić
1. Mentor → zadanie t1z1 → „Utwórz plik ćwiczenia” → przepisz przykład (nie kopiuj — ręka uczy się składni) → Ctrl+S → ▶ Uruchom.
2. Albo terminal Mentora w PRACA: `python zmienne.py`.

## W praktyce
- Testując formularz: wpisz liczbę z przecinkiem i z kropką — to klasyczne źródło błędów.
- W zgłoszeniu błędu podawaj typ: „pole przyjmuje tekst zamiast liczby”.

## 4 · Ćwiczenie prowadzone
Na wzór demonstracji: długopis kosztuje 2.30 zł, kupujesz 7 sztuk. (1) Ile wynosi razem (z f-stringiem :.2f)? (2) Jaki typ ma `7`? (3) Ile pełnych opakowań po 5 szt. i ile sztuk reszty? Czas: 15 minut.

📄 `cwiczenia/tydzien_01/zmienne_1.md` · rozwiązanie: `rozwiazania/tydzien_01/zmienne_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Przewidź wynik (bez uruchamiania), potem sprawdź w Mentorze: (1) `7 / 2`; (2) `7 // 2`; (3) `"2" * 3`; (4) `int("12") + 3`; (5) co da `"5" + 5` — wybierz: 10 / 55 / TypeError. Czas: 15 minut.

📄 `cwiczenia/tydzien_01/zmienne_2.md` · rozwiązanie: `rozwiazania/tydzien_01/zmienne_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **TypeError: can only concatenate str (not "int") to str**
  - Przyczyna: Sklejanie napisu z liczbą: `"Ilość: " + 3`.
  - Jak sprawdzić: Sprawdź typy: `type(...)` obu stron +.
  - Poprawka: `"Ilość: " + str(3)` albo f-string `f"Ilość: {3}"`.
- ✘ **ValueError: invalid literal for int() with base 10: '4,5'**
  - Przyczyna: Przecinek zamiast kropki albo tekst w int().
  - Jak sprawdzić: Wypisz wartość przed zamianą: `print(repr(x))`.
  - Poprawka: `float(x.replace(",", "."))` — albo wpisuj z kropką.
- ✘ **NameError: name 'Cena' is not defined**
  - Przyczyna: Literówka lub wielkość liter w nazwie zmiennej.
  - Jak sprawdzić: Porównaj nazwę w linii błędu z miejscem przypisania.
  - Poprawka: Ujednolić nazwę: `cena` wszędzie małymi literami.

## Pułapki
- `=` to przypisanie, `==` porównanie (tydzień 1, warunki).
- Kwoty na float: 0.1 + 0.2 ≠ 0.3 dokładnie — wypisuj z :.2f, a w testach porównuj z tolerancją (pytest.approx).

## Dodatkowe zadania
1. Zapisz 5 zmiennych różnych typów o produkcie ze sklepu i wypisz je z type().
2. Policz cenę 3 produktów razem z f-stringiem :.2f.
3. Sprawdź w Mentorze, co dają 13 // 4 i 13 % 4.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Co robi znak = w Pythonie?**
  - Przypisuje wartość zmiennej (nie porównuje).
- **Jaki typ ma wynik 6 / 3?**
  - float (2.0) — dzielenie / zawsze daje float.
- **Jak wstawić liczbę w tekst?**
  - f-string: f"Cena: {cena:.2f} zł" albo str(liczba).

## Co potrafię teraz bez patrzenia na przykład?
Tworzysz zmienne, rozpoznajesz 4 typy, liczysz operatorami (w tym // i %), zamieniasz typy i wypisujesz kwoty f-stringiem.

## Źródła (data dostępu w nawiasie)
Wersje narzędzi i dane rynkowe zmieniają się — przed użyciem w pracy otwórz źródło.
- Python — Poradnik: Nieformalne wprowadzenie (liczby, napisy, listy) (dostęp 23.11.2026) — <https://docs.python.org/pl/3/tutorial/introduction.html>
- Python — Built-in Types (str, list, dict: metody) (dostęp 23.11.2026) — <https://docs.python.org/3/library/stdtypes.html>
- Python — Poradnik: Wejście i wyjście (f-stringi, pliki) (dostęp 23.11.2026) — <https://docs.python.org/pl/3/tutorial/inputoutput.html>

## Test (w Mentorze: Lekcje → Sprawdź się)
- type(4.5) zwraca:
  - A) int
  - B) float
  - C) str
  - D) bool
- Wynik 9 % 4:
  - A) 2.25
  - B) 2
  - C) 1
  - D) 0
- Co da "3" + "4"?
  - A) 7
  - B) "34"
  - C) TypeError
  - D) 12
- f"{2.5:.2f}" daje:
  - A) 2.5
  - B) 2.50
  - C) 3
  - D) 2,50

Odpowiedzi: B, C, B, B
