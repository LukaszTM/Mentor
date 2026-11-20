# Czytanie kodu 2: listy, pętle, słowniki i funkcje
Tydzień 2 · lekcja 7 z 48 · ≈ 55 min

**Po tej lekcji potrafisz:** czytasz funkcję z parametrami i return, pętlę for po liście, słownik i rzucanie wyjątku — i umiesz powiedzieć, co funkcja zwróci dla podanych danych.

**Po co mi to?** Prawie każdy kod od AI to funkcje działające na listach i słownikach. Testy w tym kursie wywołują Twoje funkcje — musisz rozumieć, co znaczy „funkcja zwraca”.

## Czego potrzebujesz
- Lekcja „Czytanie kodu 1”.
- Plik do eksperymentów w PRACA (np. proby.py).

## 1 · Wyjaśnienie od podstaw
### Lista — wiele wartości pod jedną nazwą
`goscie = ["Anna", "Piotr", "Ewa"]` — lista w nawiasach kwadratowych. Numeracja od ZERA: `goscie[0]` to "Anna", `goscie[-1]` to ostatni element. `len(goscie)` → 3, `goscie.append("Jan")` dopisuje na końcu, `"Ewa" in goscie` → True.
### Pętla for — zrób coś dla każdego elementu
`for g in goscie:` + wcięty blok wykonuje się raz dla każdego elementu; w kolejnych obrotach `g` to kolejne imiona. `for i in range(3):` daje i = 0, 1, 2 (bez 3!). Typowy wzór „zbierz sumę”: przed pętlą `suma = 0`, w pętli `suma = suma + x` (krócej `suma += x`).
### Słownik — wartości pod nazwami (kluczami)
`rezerwacja = {"gosc": "Anna", "noce": 3, "pokoj": "Lipowy"}` — klucz: wartość. `rezerwacja["noce"]` → 3. Brak klucza → błąd KeyError; bezpiecznie: `rezerwacja.get("rabat", 0)` (0, gdy brak). Dane z plików CSV i JSON, odpowiedzi z internetu (API) — to prawie zawsze listy słowników.
### Funkcja — nazwany kawałek pracy
```
def koszt_pobytu(noce, osoby, cena=120):
    return noce * osoby * cena
```
- `def` definiuje funkcję; `noce, osoby` to parametry, `cena=120` — parametr z wartością domyślną.
- `return` ODDAJE wynik temu, kto wywołał funkcję, i kończy funkcję. `print` tylko wypisuje na ekran — testy sprawdzają to, co funkcja ZWRACA. Funkcja bez return zwraca `None` — to najczęstsza przyczyna, gdy test mówi „oczekiwano 480.0, otrzymano None”.
- Wywołanie: `koszt_pobytu(2, 2)` → 480; z inną ceną: `koszt_pobytu(2, 2, cena=150)` → 600.
### raise — funkcja odmawia złych danych
`if noce < 1: raise ValueError("noce muszą być ≥ 1")` przerywa funkcję z błędem. To dobrze: lepiej głośny błąd niż cicha zła cena. Test może sprawdzić, że dla złych danych funkcja rzuca ValueError.
### if __name__ == "__main__":
Agent często dopisuje na końcu pliku ten blok. Kod w nim wykonuje się tylko, gdy uruchamiasz plik bezpośrednio (▶ Uruchom), a NIE wtedy, gdy test importuje funkcję. Dzięki temu input() w tym bloku nie blokuje testów.
### Jak czytać funkcję od AI w 4 pytaniach
| pytanie | gdzie patrzysz |
|---|---|
| co przyjmuje? | parametry w linii def |
| co zwraca? | każda linia return (może być kilka!) |
| kiedy odmawia? | raise i warunki przed nim |
| co zmienia poza sobą? | zapisy do plików, print, zmiany list przekazanych z zewnątrz |

## 2 · Demonstracja — krok po kroku
**Śledzenie pętli po liście słowników**

```
def koszt_pobytu(noce, osoby, cena=120):
    if noce < 1 or osoby < 1:
        raise ValueError("noce i osoby muszą być co najmniej 1")
    koszt = noce * osoby * cena
    if noce >= 7:
        koszt = koszt * 0.9
    return round(koszt, 2)


rezerwacje = [{"gosc": "Anna", "noce": 2, "osoby": 2}, {"gosc": "Piotr", "noce": 7, "osoby": 1}]
suma = 0
for r in rezerwacje:
    k = koszt_pobytu(r["noce"], r["osoby"])
    print(r["gosc"], k)
    suma += k
print("Razem:", suma)

```

1. Najpierw definicja funkcji — Python ją tylko zapamiętuje, nic nie liczy.
2. rezerwacje to lista dwóch słowników. suma = 0.
3. Obrót 1: r = słownik Anny. koszt_pobytu(2, 2): warunek raise nie zachodzi, koszt = 2*2*120 = 480, 2 >= 7 to False, return round(480, 2) → 480 (int, bo nic nie mnożyło przez 0.9). Wypisuje „Anna 480”, suma = 480.
4. Obrót 2: Piotr: 7*1*120 = 840, 7 >= 7 → koszt = 756.0 (float). Wypisuje „Piotr 756.0”, suma = 1236.0.
5. Po pętli: „Razem: 1236.0”. Zauważ: raz 480, raz 756.0 — typ wyniku zależy od ścieżki. Testy porównują liczby (480 == 480.0 to True), więc to nie błąd, ale na fakturze formatujesz {k:.2f}.
6. Spróbuj: dopisz rezerwację z noce = 0 — program kończy się ValueError z Twoim komunikatem. Tak ma być.

✔ **Oczekiwany wynik:** Anna 480 / Piotr 756.0 / Razem: 1236.0; dla noce = 0 — ValueError z czytelnym komunikatem.

## 3 · Jak to uruchomić
1. Wklej przykład do proby.py w PRACA i uruchom (zadanie z paskiem albo `python proby.py`).

## W praktyce
- Przy każdej funkcji od AI: co przyjmuje, co zwraca, kiedy odmawia.
- Szukaj return w pętlach.

## 4 · Ćwiczenie prowadzone
Co zwróci funkcja i co wypisze program?

def policz_dorosłych(goscie):
    n = 0
    for g in goscie:
        if g["wiek"] >= 18:
            n += 1
    return n

lista = [{"imie": "Ola", "wiek": 34}, {"imie": "Kuba", "wiek": 12}, {"imie": "Ewa", "wiek": 18}]
print(policz_dorosłych(lista))
print(lista[1]["imie"])
print(len(lista))

Wpisz trzy linie wyniku. Czas: 20 minut.

📄 `cwiczenia/tydzien_02/czytanie_kodu_2_1.md` · rozwiązanie: `rozwiazania/tydzien_02/czytanie_kodu_2_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
AI napisało funkcję, a test mówi: „assert None == 480”. Znajdź błąd:

def koszt(noce, osoby):
    wynik = noce * osoby * 120
    print(wynik)

Co zwraca ta funkcja? Jakie słowo trzeba wstawić zamiast print, żeby test przeszedł? Czas: 15 minut.

📄 `cwiczenia/tydzien_02/czytanie_kodu_2_2.md` · rozwiązanie: `rozwiazania/tydzien_02/czytanie_kodu_2_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **„IndexError: list index out of range”.**
  - Przyczyna: Sięgasz po element o numerze, którego nie ma (np. lista[3] w liście 3-elementowej).
  - Jak sprawdzić: len(lista) i numer, którego używasz.
  - Poprawka: Pamiętaj: ostatni element to lista[len(lista) - 1] albo lista[-1].
- ✘ **„KeyError: 'nocy'”.**
  - Przyczyna: Klucz w słowniku nazywa się inaczej (literówka, wielkość liter).
  - Jak sprawdzić: print(slownik.keys()) — jakie są klucze?
  - Poprawka: Popraw nazwę klucza albo użyj .get("klucz", domyślna).
- ✘ **Test: „assert None == …”.**
  - Przyczyna: Funkcja nie ma return (albo return jest w złym miejscu, np. w pętli).
  - Jak sprawdzić: Czy każda ścieżka funkcji kończy się return?
  - Poprawka: Dodaj return z wynikiem; nie zastępuj return przez print.

## Pułapki
- return w środku pętli kończy funkcję po pierwszym obrocie — częsty błąd AI przy „zsumuj wszystkie”.
- Lista przekazana do funkcji to ta sama lista — jeśli funkcja ją zmienia (append, sort), zmienia się też na zewnątrz.

## Dodatkowe zadania
1. Napisz w proby.py listę 4 cen i pętlę liczącą sumę i średnią.
2. Zmień przykład tak, żeby funkcja dawała 5% rabatu dla 4+ osób i przewidź wyniki.
3. Zapytaj czat AI: „wyjaśnij różnicę między print a return na przykładzie” i oceń odpowiedź.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Czym różni się return od print?**
  - return oddaje wartość wywołującemu (np. testowi), print tylko wypisuje tekst na ekran.
- **Jaki numer ma pierwszy element listy?**
  - 0.
- **Po co funkcji raise ValueError?**
  - Żeby głośno odmówić błędnych danych zamiast policzyć złą wartość.

## Co potrafię teraz bez patrzenia na przykład?
Czytasz listy, pętle, słowniki i funkcje; rozróżniasz return i print; rozumiesz raise i blok __main__.

## Źródła (data dostępu w nawiasie)
Narzędzia, ceny i przepisy zmieniają się — przed użyciem w pracy otwórz źródło.
- Python tutorial — 4.8 Defining Functions (def, return) (dostęp 19.11.2026) — <https://docs.python.org/3/tutorial/controlflow.html#defining-functions>
- Python tutorial — 5. Data Structures (listy, słowniki) (dostęp 19.11.2026) — <https://docs.python.org/3/tutorial/datastructures.html>
- Python — oficjalny tutorial (python.org, wersja polskojęzyczna częściowo; tłumaczenie robocze w lekcji) (dostęp 19.11.2026) — <https://docs.python.org/3/tutorial/>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Co zwraca funkcja bez return?
  - A) 0
  - B) None
  - C) Pusty napis
  - D) Błąd
- `for i in range(3)` daje kolejno:
  - A) 1, 2, 3
  - B) 0, 1, 2
  - C) 0, 1, 2, 3
  - D) 3
- `d = {"noce": 3}`; `d.get("osoby", 1)` zwraca:
  - A) KeyError
  - B) None
  - C) 1
  - D) 3
- Kod pod `if __name__ == "__main__":` wykonuje się:
  - A) Zawsze
  - B) Gdy plik uruchamiasz bezpośrednio, nie przy imporcie przez test
  - C) Tylko w testach
  - D) Nigdy

Odpowiedzi: B, B, C, B
