# Czytanie kodu 1: zmienne, napisy, liczby i warunki
Tydzień 1 · lekcja 6 z 48 · ≈ 55 min

**Po tej lekcji potrafisz:** czytasz krótki program ze zmiennymi, liczbami i warunkiem if/elif/else i przewidujesz, co wypisze — zanim go uruchomisz.

**Po co mi to?** Agent pisze kod szybciej niż Ty czytasz — ale tylko czytając rozumiesz, czy zrobił to, o co prosiłeś. Czytanie jest ważniejsze niż pisanie.

## Czego potrzebujesz
- Środowisko kursu zainstalowane (lekcja „Python: instalacja…”).
- Plik ćwiczeń: PRACA (dowolny .py do sprawdzania przewidywań).

## 1 · Wyjaśnienie od podstaw
### Zmienna — etykieta na wartości
`noce = 3` oznacza: zapamiętaj wartość 3 pod nazwą `noce`. Znak = w Pythonie to „przypisz”, nie „równa się”. Później `noce` w kodzie oznacza 3, dopóki ktoś nie przypisze nowej wartości.
### Typy wartości, które spotkasz najczęściej
| typ | przykład | uwaga |
|---|---|---|
| int (liczba całkowita) | `3`, `-10` | dzielenie `/` zawsze daje float: `7 / 2` → 3.5 |
| float (liczba z kropką) | `120.0`, `0.9` | w kodzie kropka, nie przecinek; `0.1 + 0.2` daje 0.30000000000000004 — dlatego kwoty zaokrąglamy round(x, 2) |
| str (napis) | `"Pod Lipą"` | `"3" + "4"` daje `"34"` (sklejenie), a `3 + 4` daje 7 |
| bool (prawda/fałsz) | `True`, `False` | wynik porównań: `noce >= 7` |
### Działania
`+ - * /` jak w matematyce, `//` dzielenie całkowite (7 // 2 → 3), `%` reszta z dzielenia (7 % 2 → 1), `**` potęga. Kolejność jak w szkole: najpierw * i /, potem + i -; nawiasy zmieniają kolejność.
### f-string — napis z wstawionymi wartościami
`f"Koszt: {koszt} zł"` — litera f przed cudzysłowem i zmienne w klamrach. `{koszt:.2f}` wypisze liczbę z dwoma miejscami po przecinku (kropką).
### input — dane od użytkownika
`imie = input("Imię: ")` czeka, aż użytkownik coś wpisze, i ZAWSZE zwraca napis. Żeby liczyć, trzeba zamienić: `noce = int(input("Noce: "))`. To jedno z najczęstszych źródeł błędów w kodzie początkujących — i w kodzie AI, gdy prośba była niejasna.
### Warunek if / elif / else
Kod wcięty pod `if` wykonuje się tylko, gdy warunek jest prawdziwy. `elif` to „w przeciwnym razie, jeśli…”, `else` — „we wszystkich pozostałych przypadkach”. Python sprawdza od góry i wykonuje PIERWSZY pasujący blok — kolejność warunków ma znaczenie. Wcięcie (4 spacje) jest częścią składni: pokazuje, co należy do bloku.
| porównanie | znaczy |
|---|---|
| `==` | równe (dwa znaki =!) |
| `!=` | różne |
| `<`, `<=`, `>`, `>=` | mniejsze, mniejsze lub równe… |
| `and`, `or`, `not` | i, lub, nie |
### Jak czytać kod jak recenzent
- Idź linia po linii i zapisuj na kartce wartości zmiennych (tzw. „śledzenie”).
- Przy każdym if zapytaj: co się stanie na granicy (np. dokładnie 7 nocy)?
- Przewiduj wynik, potem uruchom. Różnica między przewidywaniem a wynikiem to dokładnie to, czego się uczysz.

## 2 · Demonstracja — krok po kroku
**Śledzenie programu z rabatem — linia po linii**

```
noce = 7
osoby = 2
cena = 120

koszt = noce * osoby * cena
if noce >= 7:
    koszt = koszt * 0.9
    print("Rabat 10% za długi pobyt")
else:
    print("Bez rabatu")

print(f"Do zapłaty: {koszt:.2f} zł")

```

1. Linie 1–3: trzy zmienne: noce = 7, osoby = 2, cena = 120 (wszystkie int).
2. Linia 5: koszt = 7 * 2 * 120 = 1680 (int).
3. Linia 6: warunek noce >= 7 → 7 >= 7 → True (granica WCHODZI, bo >=). Wykonują się dwie wcięte linie: koszt = 1680 * 0.9 = 1512.0 (teraz float) i wypisanie „Rabat 10% za długi pobyt”.
4. Blok else jest pomijany, bo pierwszy warunek był prawdziwy.
5. Ostatnia linia: f-string z {koszt:.2f} → „Do zapłaty: 1512.00 zł”.
6. Zmień noce = 6 i przewidź wynik przed uruchomieniem: 6 * 2 * 120 = 1440, warunek False → „Bez rabatu”, „Do zapłaty: 1440.00 zł”. Gdyby w warunku było > zamiast >=, 7 nocy nie dostałoby rabatu — to typowy błąd granicy.

✔ **Oczekiwany wynik:** Rabat 10% za długi pobyt / Do zapłaty: 1512.00 zł; po zmianie na 6 nocy: Bez rabatu / Do zapłaty: 1440.00 zł.

## 3 · Jak to uruchomić
1. Wklej przykład do pliku `rabat.py` w PRACA → zadanie z paskiem albo terminal `python rabat.py`.
2. Przewiduj wynik ZANIM uruchomisz — zapisz go w dzienniku.

## W praktyce
- Przy każdym if od AI zapytaj: co na granicy?
- Kwoty zawsze z zaokrągleniem do groszy.

## 4 · Ćwiczenie prowadzone
Przewidź wynik (najpierw na kartce, potem uruchom):

osoby = 3
noce = 2
koszt = osoby * noce * 100
if koszt > 500:
    print("Duża rezerwacja")
elif koszt > 300:
    print("Średnia rezerwacja")
else:
    print("Mała rezerwacja")
print(koszt)

Wpisz pierwszą linię wyniku i wartość koszt. Czas: 15 minut.

📄 `cwiczenia/tydzien_01/czytanie_kodu_1_1.md` · rozwiązanie: `rozwiazania/tydzien_01/czytanie_kodu_1_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
AI napisało fragment:

noce = input("Ile nocy? ")
print(noce * 2)

Użytkownik wpisuje 3. Co wypisze program (bez spacji, dokładnie)? Jak poprawisz pierwszą linię, żeby wynik był 6? Czas: 20 minut.

📄 `cwiczenia/tydzien_01/czytanie_kodu_1_2.md` · rozwiązanie: `rozwiazania/tydzien_01/czytanie_kodu_1_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **„TypeError: can only concatenate str (not "int") to str”.**
  - Przyczyna: Sklejasz napis z liczbą: "Koszt: " + 100.
  - Jak sprawdzić: Która linia? Jakie typy po obu stronach +?
  - Poprawka: Użyj f-stringa: f"Koszt: {koszt}" albo str(koszt).
- ✘ **„IndentationError: expected an indented block”.**
  - Przyczyna: Po if/else brakuje wciętej linii albo wcięcia są niespójne.
  - Jak sprawdzić: Linia pod if — czy ma 4 spacje?
  - Poprawka: Wcięcie 4 spacje pod każdym if/elif/else; nie mieszaj tabulatora ze spacjami.
- ✘ **„SyntaxError: invalid syntax” przy `if noce = 7:`.**
  - Przyczyna: Pojedyncze = to przypisanie; porównanie to ==.
  - Jak sprawdzić: Szukaj = w warunku.
  - Poprawka: `if noce == 7:`

## Pułapki
- Granice warunków (> czy >=) to miejsce, gdzie AI i ludzie mylą się najczęściej. Zawsze testuj wartość dokładnie na granicy.
- 0.1 + 0.2 nie daje dokładnie 0.3 — przy pieniądzach zaokrąglaj round(x, 2) albo licz w groszach (int).

## Dodatkowe zadania
1. Zmień w przykładzie rabat na 15% od 10 nocy i przewidź wynik dla 10 nocy.
2. Napisz (sam albo z czatem AI) 3 linie z input() i int(), które liczą koszt dla wpisanej liczby nocy.
3. Znajdź w kodzie z tej lekcji wszystkie miejsca, gdzie typ zmiennej się zmienia.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Co zwraca input()?**
  - Zawsze napis (str); liczbę trzeba zamienić int() lub float().
- **Dlaczego kolejność warunków if/elif ma znaczenie?**
  - Python wykonuje pierwszy pasujący blok i pomija resztę.
- **Co wypisze print(f"{2/3:.2f}")?**
  - 0.67

## Co potrafię teraz bez patrzenia na przykład?
Czytasz zmienne, typy, działania, f-stringi, input i warunki; przewidujesz wynik linia po linii i sprawdzasz granice warunków.

## Źródła (data dostępu w nawiasie)
Narzędzia, ceny i przepisy zmieniają się — przed użyciem w pracy otwórz źródło.
- Python — oficjalny tutorial (python.org, wersja polskojęzyczna częściowo; tłumaczenie robocze w lekcji) (dostęp 19.11.2026) — <https://docs.python.org/3/tutorial/>
- Python tutorial — 3. An Informal Introduction to Python (liczby, napisy) (dostęp 19.11.2026) — <https://docs.python.org/3/tutorial/introduction.html>
- Python tutorial — 4.1 if Statements (dostęp 19.11.2026) — <https://docs.python.org/3/tutorial/controlflow.html>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Co wypisze `print("3" + "4")`?
  - A) 7
  - B) 34
  - C) 3 4
  - D) Błąd
- Ile wynosi `7 // 2`?
  - A) 3.5
  - B) 3
  - C) 4
  - D) 1
- Dla noce = 7 warunek `noce > 7` jest:
  - A) True
  - B) False
  - C) Błędem
  - D) Zależy od osób
- Jak zamienić napis z input() na liczbę całkowitą?
  - A) str()
  - B) int()
  - C) print()
  - D) round()

Odpowiedzi: B, B, B, B
