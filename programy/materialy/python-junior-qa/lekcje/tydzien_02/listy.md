# Listy: indeksy, append, remove, sortowanie, len, sum, max
Tydzień 2 · lekcja 10 z 39 · ≈ 45 min

**Po tej lekcji potrafisz:** tworzysz listy, czytasz elementy po indeksie (także ujemnym i wycinkiem), dodajesz i usuwasz elementy, sortujesz i liczysz len/sum/max/min oraz sprawdzasz `in`.

**Po co mi to?** Koszyk, lista zamówień, wyniki testów — wszystko to listy. Tester sprawdza też skrajności: pusta lista, jeden element, duplikaty.

## Czego potrzebujesz
- Lekcja „Pętle”.

## 1 · Wyjaśnienie od podstaw
### Lista
`koszyk = ["zeszyt", "długopis", "klej"]` — uporządkowany ciąg elementów w nawiasach kwadratowych. Elementy mogą być dowolnego typu.
### Indeksy
Numeracja od **0**: `koszyk[0]` → "zeszyt", `koszyk[2]` → "klej". Ujemne od końca: `koszyk[-1]` → ostatni. Indeks poza listą → IndexError.
Wycinek: `koszyk[0:2]` → elementy 0 i 1 (bez 2). `koszyk[:2]` — od początku, `koszyk[1:]` — do końca.
### Zmiany
| operacja | co robi |
|---|---|
| `koszyk.append("gumka")` | dodaje na koniec |
| `koszyk.insert(0, "blok")` | wstawia na pozycję 0 |
| `koszyk.remove("klej")` | usuwa pierwsze wystąpienie wartości (brak → ValueError) |
| `koszyk.pop()` | usuwa i zwraca ostatni (`pop(0)` — pierwszy) |
| `koszyk[1] = "ołówek"` | podmienia element |
### Liczenie i sortowanie
`len(lista)` — liczba elementów; `sum`, `max`, `min` — dla liczb. `lista.sort()` sortuje **tę listę** (zwraca None!), `sorted(lista)` zwraca **nową** posortowaną. `reverse=True` — malejąco.
### Sprawdzanie
`"klej" in koszyk` → True/False. Pusta lista `[]` ma len 0 — `max([])` da ValueError, więc sprawdzaj `if lista:` przed max/średnią.

## 2 · Demonstracja — krok po kroku
**Koszyk w sklepie: dodaj, usuń, policz**

```
koszyk = ["zeszyt", "długopis", "klej"]
ceny = [4.5, 2.3, 3.4]
koszyk.append("gumka")
ceny.append(1.5)
print(koszyk[0], koszyk[-1], len(koszyk))
print(koszyk[1:3])
koszyk.remove("klej")
print(koszyk, "klej" in koszyk)
print("Suma:", sum(ceny), "max:", max(ceny), "min:", min(ceny))
print(sorted(ceny), sorted(ceny, reverse=True)[0])
print(f"Średnia: {sum(ceny) / len(ceny):.2f}")

```

1. `koszyk = [...]`, `ceny = [...]` — dwie listy; pozycja 0 w obu dotyczy tego samego produktu.
2. `append` — gumka i jej cena trafiają na koniec obu list.
3. `koszyk[0]` → zeszyt, `koszyk[-1]` → gumka, `len` → 4.
4. `koszyk[1:3]` → elementy 1 i 2: długopis, klej.
5. `remove("klej")` — usunięcie po wartości; `"klej" in koszyk` → False.
6. `sum`, `max`, `min` na liście liczb. Uwaga: lista ceny wciąż ma 4 pozycje — usunęliśmy klej tylko z koszyka! To błąd danych równoległych list; w tygodniu 3 zastąpi je słownik.
7. `sorted(ceny)` nowa lista rosnąco; `sorted(..., reverse=True)[0]` — największa.
8. Średnia = suma / liczba elementów, z :.2f.

✔ **Oczekiwany wynik:** Sześć linii — od „zeszyt gumka 4” do „Średnia: 2.92”.

## 3 · Jak to uruchomić
1. Zapisz jako koszyk.py → ▶ Uruchom.
2. Dopisz `print(max([]))` i zobacz ValueError — potem usuń tę linię.

## W praktyce
- Test każdej funkcji na liście: pusta, jeden element, kilka, duplikaty.
- W raporcie błędu podaj dokładne dane wejściowe (całą listę).

## 4 · Ćwiczenie prowadzone
Lista `stany = [120, 80, 300, 0, 45]`. Podaj: (1) `stany[2]`, (2) `stany[-2]`, (3) `stany[1:4]`, (4) `len(stany)` po `stany.append(10)`, (5) `max(stany)`. Czas: 15 minut.

📄 `cwiczenia/tydzien_02/listy_1.md` · rozwiązanie: `rozwiazania/tydzien_02/listy_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Kod: `ceny = [7.5, 2.3, 4.5]` / `wynik = ceny.sort()` / `print(wynik)`. (1) Co wypisze? (2) Jak dostać nową posortowaną listę w zmiennej wynik (wpisz wyrażenie)? (3) Co zwróci `sum([])` i czy `max([])` zadziała (tak/nie)? Czas: 15 minut.

📄 `cwiczenia/tydzien_02/listy_2.md` · rozwiązanie: `rozwiazania/tydzien_02/listy_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **IndexError: list index out of range**
  - Przyczyna: Indeks ≥ len(lista) (np. lista[3] dla 3 elementów).
  - Jak sprawdzić: Wypisz len(lista) i indeks.
  - Poprawka: Ostatni element to lista[-1] albo lista[len(lista) - 1].
- ✘ **ValueError: list.remove(x): x not in list**
  - Przyczyna: Usuwasz wartość, której nie ma.
  - Jak sprawdzić: `print(x in lista)`.
  - Poprawka: `if x in lista: lista.remove(x)`.
- ✘ **TypeError: 'NoneType' object is not subscriptable**
  - Przyczyna: Wynik lista.sort() (None) użyty jak lista.
  - Jak sprawdzić: Gdzie przypisujesz wynik sort()?
  - Poprawka: sorted(lista) albo samo lista.sort() bez przypisania.

## Pułapki
- Dwie równoległe listy (nazwy i ceny) łatwo rozjechać — w tygodniu 3 słownik/lista słowników.
- lista2 = lista1 nie kopiuje — obie nazwy wskazują tę samą listę; kopia: lista1.copy().

## Dodatkowe zadania
1. Lista zakupów: dodaj 5 produktów, usuń jeden, wypisz z numerami od 1.
2. Średnia i maksimum cen z obsługą pustej listy.
3. Sprawdź `in` dla produktu, którego nie ma.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Jaki indeks ma pierwszy element?**
  - 0.
- **Różnica sort() i sorted()?**
  - sort() zmienia listę i zwraca None; sorted() zwraca nową.
- **Jak sprawdzić, czy lista jest pusta?**
  - if not lista: albo len(lista) == 0.

## Co potrafię teraz bez patrzenia na przykład?
Tworzysz i zmieniasz listy, indeksujesz (także -1 i wycinki), sortujesz, liczysz len/sum/max/min i pilnujesz pustej listy.

## Źródła (data dostępu w nawiasie)
Wersje narzędzi i dane rynkowe zmieniają się — przed użyciem w pracy otwórz źródło.
- Python — Poradnik: Struktury danych (listy, krotki, słowniki) (dostęp 23.11.2026) — <https://docs.python.org/pl/3/tutorial/datastructures.html>
- Python — Poradnik: Nieformalne wprowadzenie (liczby, napisy, listy) (dostęp 23.11.2026) — <https://docs.python.org/pl/3/tutorial/introduction.html>
- Python — Built-in Types (str, list, dict: metody) (dostęp 23.11.2026) — <https://docs.python.org/3/library/stdtypes.html>

## Test (w Mentorze: Lekcje → Sprawdź się)
- [10, 20, 30][-1] to:
  - A) 10
  - B) 20
  - C) 30
  - D) błąd
- Co zwraca lista.sort()?
  - A) posortowaną listę
  - B) None
  - C) True
  - D) długość
- len([]) to:
  - A) 0
  - B) 1
  - C) None
  - D) błąd
- [1, 2, 3, 4][1:3] to:
  - A) [1, 2]
  - B) [2, 3]
  - C) [2, 3, 4]
  - D) [1, 2, 3]

Odpowiedzi: C, B, A, B
