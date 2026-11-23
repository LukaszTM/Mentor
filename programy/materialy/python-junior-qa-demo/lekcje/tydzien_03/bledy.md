# Obsługa błędów: try / except / else / finally i raise
Tydzień 3 · lekcja 14 z 16 · ≈ 45 min

**Po tej lekcji potrafisz:** czytasz traceback (typ błędu, plik, linia), łapiesz konkretne wyjątki try/except, ponawiasz pytanie w pętli przy złym wpisie i sam zgłaszasz błąd raise ValueError przy niepoprawnych danych.

**Po co mi to?** Program sklepu nie może paść, gdy klient wpisze „dwa” zamiast 2. Tester celowo wpisuje złe dane — i ocenia, czy komunikat jest zrozumiały.

## Czego potrzebujesz
- Lekcja „Funkcje”.

## 1 · Wyjaśnienie od podstaw
### Traceback — czytaj od dołu
```
Traceback (most recent call last):
  File "kalk.py", line 3, in <module>
    ilosc = int(wpis)
ValueError: invalid literal for int() with base 10: 'dwa'
```
Ostatnia linia: **typ błędu** i opis. Wyżej: plik i **numer linii**. To pierwsze, co wklejasz do zgłoszenia lub asystentowi.
### try / except
```
try:
    ilosc = int(wpis)
except ValueError:
    print("Podaj liczbę całkowitą")
```
Python próbuje wykonać blok try; jeśli wystąpi ValueError, przechodzi do except zamiast kończyć program. Łap **konkretne** wyjątki — samo `except:` ukrywa też Twoje literówki.
### Najczęstsze wyjątki
| wyjątek | kiedy |
|---|---|
| `ValueError` | zła wartość: int("dwa") |
| `ZeroDivisionError` | dzielenie przez zero |
| `KeyError` | brak klucza w słowniku |
| `IndexError` | indeks poza listą |
| `TypeError` | zły typ: "a" + 1 |
| `FileNotFoundError` | brak pliku (tydzień 4) |
### else i finally
`else:` wykonuje się, gdy w try NIE było błędu; `finally:` — zawsze (np. komunikat „koniec”).
### Pętla do skutku
`while True: try: return int(input(...)) except ValueError: print("To nie liczba")` — pyta, aż dostanie poprawny wpis.
### raise — zgłaszasz błąd sam
Funkcja nie powinna po cichu liczyć bzdur: `if ilosc <= 0: raise ValueError("ilość musi być dodatnia")`. Wywołujący (albo test) dostaje jasny sygnał. W tygodniu 7 sprawdzisz to `pytest.raises(ValueError)`.

## 2 · Demonstracja — krok po kroku
**Wydawanie towaru: trzy rodzaje złych danych**

```
def wydaj(stan, ilosc):
    """Zwraca nowy stan po wydaniu towaru; zła ilość → ValueError."""
    if ilosc <= 0:
        raise ValueError("ilość musi być dodatnia")
    if ilosc > stan:
        raise ValueError(f"brak towaru: na stanie {stan}")
    return stan - ilosc


for wpis in ["5", "dwa", "0", "200"]:
    try:
        ilosc = int(wpis)
        nowy = wydaj(120, ilosc)
    except ValueError as e:
        print(f"{wpis!r}: błąd — {e}")
    else:
        print(f"{wpis!r}: wydano, zostało {nowy}")
    finally:
        print("---")

```

1. `wydaj(stan, ilosc)` — sama logika: dwie reguły walidacji z `raise ValueError("…")` i return nowego stanu.
2. Pętla po 4 wpisach — jak 4 przypadki testowe: poprawny, tekst, zero, za dużo.
3. `int(wpis)` dla „dwa” rzuca ValueError od Pythona; `wydaj` dla 0 i 200 rzuca ValueError z naszym komunikatem.
4. `except ValueError as e:` — `e` to obiekt błędu, `{e}` wypisuje jego opis.
5. `else:` — tylko dla „5”: wydano, zostało 115.
6. `finally:` — linia „---” po każdym wpisie, z błędem i bez.
7. `{wpis!r}` — wypisuje wartość z cudzysłowem ('5'), widać, że to napis.

✔ **Oczekiwany wynik:** Cztery bloki: '5' wydano (115), 'dwa' błąd int(), '0' ilość musi być dodatnia, '200' brak towaru — każdy zakończony „---”.

## 3 · Jak to uruchomić
1. Zapisz jako wydawanie.py → ▶ Uruchom.
2. Usuń try/except i uruchom — zobaczysz pełny traceback i zatrzymanie programu na „dwa”.

## W praktyce
- W bug raporcie zawsze ostatnia linia tracebacku i numer linii.
- Test negatywny = sprawdzenie, że zła dana daje czytelny błąd, nie awarię.

## 4 · Ćwiczenie prowadzone
Na wzór demonstracji: `def podziel(a, b): return a / b`, wywołania w try z `except ZeroDivisionError: print("Nie dzielimy przez zero")`. Co wypisze dla: (1) podziel(10, 4), (2) podziel(5, 0)? (3) Jaki wyjątek rzuci podziel("10", 2)? Czas: 15 minut.

📄 `cwiczenia/tydzien_03/bledy_1.md` · rozwiązanie: `rozwiazania/tydzien_03/bledy_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Traceback: `File "sklep.py", line 14, in cena_koszyka` / `return suma / len(koszyk)` / `ZeroDivisionError: division by zero`. (1) W której linii jest błąd? (2) W jakiej funkcji? (3) Jaki stan danych go wywołał (wybierz)? (4) Co jest lepszą poprawką: except: pass / sprawdzenie pustego koszyka przed dzieleniem? Czas: 15 minut.

📄 `cwiczenia/tydzien_03/bledy_2.md` · rozwiązanie: `rozwiazania/tydzien_03/bledy_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **Program „działa”, ale wynik bez sensu i bez komunikatu**
  - Przyczyna: `except:` albo `except Exception: pass` połknęło błąd.
  - Jak sprawdzić: Usuń tymczasowo try i zobacz traceback.
  - Poprawka: Łap konkretny wyjątek i reaguj komunikatem.
- ✘ **UnboundLocalError / NameError po bloku try**
  - Przyczyna: Zmienna przypisana w try, który się nie udał, użyta dalej.
  - Jak sprawdzić: Czy zmienna ma wartość, gdy był wyjątek?
  - Poprawka: Użyj zmiennej w else albo nadaj wartość przed try.

## Pułapki
- Zbyt szeroki try (cała funkcja) — nie wiesz, która linia rzuciła błąd. Obejmuj tylko ryzykowną linię.
- raise bez komunikatu — zawsze pisz, CO jest nie tak i jakie są dozwolone wartości.

## Dodatkowe zadania
1. Funkcja wczytaj_liczbe() pytająca do skutku.
2. Kalkulator z obsługą ValueError i ZeroDivisionError.
3. Funkcja z raise ValueError dla ilości ≤ 0.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Gdzie w tracebacku jest typ błędu?**
  - W ostatniej linii.
- **Dlaczego nie except: pass?**
  - Ukrywa błędy, także Twoje literówki.
- **Kiedy wykonuje się else w try?**
  - Gdy w try nie było wyjątku.

## Co potrafię teraz bez patrzenia na przykład?
Czytasz traceback, łapiesz konkretne wyjątki, ponawiasz pytanie przy złym wpisie i zgłaszasz błędy raise z jasnym komunikatem.

## Źródła (data dostępu w nawiasie)
Wersje narzędzi i dane rynkowe zmieniają się — przed użyciem w pracy otwórz źródło.
- Python — Poradnik: Błędy i wyjątki (dostęp 23.11.2026) — <https://docs.python.org/pl/3/tutorial/errors.html>
- SJSI — Egzamin przykładowy CTFL 4.0, wersja polska (terminologia: pomyłka, defekt, awaria, klasy równoważności, wartości brzegowe) (dostęp 23.11.2026) — <https://testerzy.pl/pliki/certyfikacja/egzamin-przykladowy-ctfl-ver-4-0-pytania-pl.pdf/podglad>

## Test (w Mentorze: Lekcje → Sprawdź się)
- int("3.5") rzuci:
  - A) TypeError
  - B) ValueError
  - C) nic — da 3
  - D) ZeroDivisionError
- Gdzie szukasz numeru linii w tracebacku?
  - A) w pierwszej linii
  - B) w linii File "…", line N
  - C) w ostatniej linii
  - D) nigdzie
- finally wykonuje się:
  - A) tylko przy błędzie
  - B) tylko bez błędu
  - C) zawsze
  - D) nigdy
- Funkcja dostała ilość -3. Najlepiej:
  - A) zwrócić 0 po cichu
  - B) raise ValueError z opisem
  - C) print i dalej liczyć
  - D) zakończyć Pythona

Odpowiedzi: B, B, C, B
