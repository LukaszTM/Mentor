# Słowniki i krotki: klucz → wartość
Tydzień 3 · lekcja 13 z 39 · ≈ 45 min

**Po tej lekcji potrafisz:** przechowujesz dane jako klucz → wartość w słowniku (dodaj, zmień, usuń, get, in), przechodzisz po items(), sortujesz po wartości, używasz krotek i listy słowników jako prostej „tabeli”.

**Po co mi to?** Dane z API, plików JSON i baz przychodzą jako słowniki. Tester porównuje oczekiwany słownik z otrzymanym w każdym teście API.

## Czego potrzebujesz
- Lekcje „Listy” i „Funkcje”.

## 1 · Wyjaśnienie od podstaw
### Słownik
`stany = {"zeszyt": 120, "klej": 110}` — pary **klucz: wartość** w nawiasach klamrowych. Klucz (najczęściej napis) jest unikalny, po nim szybko znajdujesz wartość: `stany["zeszyt"]` → 120.
### Operacje
| operacja | co robi |
|---|---|
| `stany["gumka"] = 150` | dodaje albo podmienia |
| `del stany["klej"]` | usuwa (brak klucza → KeyError) |
| `stany.get("farby", 0)` | wartość albo 0, gdy brak klucza — bez błędu |
| `"klej" in stany` | czy jest taki KLUCZ |
| `len(stany)` | liczba par |
| `for nazwa, ilosc in stany.items():` | pętla po parach |
`keys()` — same klucze, `values()` — same wartości (`sum(stany.values())`).
### Sortowanie po wartości
`sorted(stany.items(), key=lambda p: p[1])` — lista par (krotek) posortowana po drugim elemencie, czyli po ilości. `lambda p: p[1]` to mała funkcja „weź element 1 pary”.
### Krotka
`para = ("zeszyt", 120)` — jak lista, ale niezmienna, w nawiasach okrągłych. Rozpakowanie: `nazwa, ilosc = para`. items() zwraca właśnie krotki.
### Lista słowników — prosta tabela
`produkty = [{"nazwa": "zeszyt", "cena": 4.5}, {"nazwa": "klej", "cena": 3.4}]` — każdy słownik to wiersz, klucze to kolumny. Tak wyglądają dane z API i z csv.DictReader (tydzień 4).

## 2 · Demonstracja — krok po kroku
**Stany magazynowe w słowniku**

```
stany = {"zeszyt": 120, "klej": 110, "zszywki": 0}
stany["gumka"] = 150
stany["klej"] = 100
del stany["zszywki"]
print(stany)
print(stany.get("farby", 0), "klej" in stany, len(stany))
for nazwa, ilosc in sorted(stany.items(), key=lambda p: p[1]):
    print(f"{nazwa:<8}{ilosc:>5}")
print("Razem sztuk:", sum(stany.values()))
produkty = [{"nazwa": "zeszyt", "cena": 4.5}, {"nazwa": "klej", "cena": 3.4}]
najtanszy = min(produkty, key=lambda p: p["cena"])
print("Najtańszy:", najtanszy["nazwa"])

```

1. Słownik z 3 parami; `stany["gumka"] = 150` dodaje nową parę, `stany["klej"] = 100` podmienia wartość.
2. `del stany["zszywki"]` — usunięcie pary.
3. `get("farby", 0)` — brak klucza, więc 0 (bez KeyError); `"klej" in stany` → True; 3 pary.
4. `sorted(stany.items(), key=lambda p: p[1])` — pary rosnąco po ilości: klej 100, zeszyt 120, gumka 150.
5. `f"{nazwa:<8}{ilosc:>5}"` — wyrównanie: nazwa do lewej na 8 znakach, ilość do prawej na 5 — czytelna tabelka.
6. `sum(stany.values())` — suma samych wartości.
7. Lista słowników: `min(..., key=lambda p: p["cena"])` wybiera słownik z najniższą ceną.

✔ **Oczekiwany wynik:** Słownik po zmianach, „0 True 3”, tabelka posortowana po ilości, „Razem sztuk: 370”, „Najtańszy: klej”.

## 3 · Jak to uruchomić
1. Zapisz jako magazyn_demo.py → ▶ Uruchom.
2. Dopisz `print(stany["farby"])` → KeyError; zamień na get.

## W praktyce
- W testach API porównujesz słowniki: assert odpowiedz["status"] == "ok".
- Brakujące pole w danych — test na KeyError lub get z wartością domyślną.

## 4 · Ćwiczenie prowadzone
`c = {"zeszyt": 4.5, "długopis": 2.3}`. Po kolei: `c["klej"] = 3.4`, `c["zeszyt"] = 4.9`, `del c["długopis"]`. Podaj: (1) `len(c)`, (2) `c["zeszyt"]`, (3) `c.get("długopis", 0)`, (4) `round(sum(c.values()), 2)`. Czas: 15 minut.

📄 `cwiczenia/tydzien_03/slowniki_1.md` · rozwiązanie: `rozwiazania/tydzien_03/slowniki_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Lista `zamowienia = [{"nr": 1, "kwota": 45.0}, {"nr": 2, "kwota": 120.5}, {"nr": 3, "kwota": 99.99}]`. (1) Suma kwot (wyrażenie lub wynik)? (2) Numer zamówienia z największą kwotą? (3) Ile zamówień ma kwotę ≥ 100? (4) Co da `zamowienia[0]["klient"]` — wybierz: None / KeyError / pusty napis. Czas: 15 minut.

📄 `cwiczenia/tydzien_03/slowniki_2.md` · rozwiązanie: `rozwiazania/tydzien_03/slowniki_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **KeyError: 'farby'**
  - Przyczyna: Odczyt nieistniejącego klucza nawiasem [].
  - Jak sprawdzić: `print(stany.keys())`.
  - Poprawka: `stany.get("farby", 0)` albo `if "farby" in stany:`.
- ✘ **RuntimeError: dictionary changed size during iteration**
  - Przyczyna: Usuwanie kluczy w pętli po tym samym słowniku.
  - Jak sprawdzić: Czy w pętli jest del?
  - Poprawka: Pętla po `list(stany.keys())` albo zbuduj nowy słownik.
- ✘ **TypeError: unhashable type: 'list'**
  - Przyczyna: Lista jako klucz słownika.
  - Jak sprawdzić: Jakiego typu jest klucz?
  - Poprawka: Kluczem może być napis, liczba albo krotka.

## Pułapki
- `in` na słowniku sprawdza klucze, nie wartości (`120 in stany` → False).
- Kolejność kluczy = kolejność dodania; do raportu sortuj jawnie.

## Dodatkowe zadania
1. Słownik produkt → ilość: dodaj, zmień, usuń, wypisz posortowane po ilości.
2. Lista 3 słowników zamówień: suma, największe, filtr ≥ 100.
3. Zamień dwie równoległe listy z lekcji „Listy” na słownik.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Co zwraca d.get("x", 0), gdy klucza x nie ma?**
  - 0.
- **Jak przejść po parach słownika?**
  - for k, v in d.items():
- **Czym krotka różni się od listy?**
  - Jest niezmienna; nawiasy okrągłe.

## Co potrafię teraz bez patrzenia na przykład?
Przechowujesz dane klucz → wartość, bezpiecznie je odczytujesz (get, in), sortujesz po wartości i budujesz prostą tabelę z listy słowników.

## Źródła (data dostępu w nawiasie)
Wersje narzędzi i dane rynkowe zmieniają się — przed użyciem w pracy otwórz źródło.
- Python — Poradnik: Struktury danych (listy, krotki, słowniki) (dostęp 23.11.2026) — <https://docs.python.org/pl/3/tutorial/datastructures.html>
- Python — Built-in Types (str, list, dict: metody) (dostęp 23.11.2026) — <https://docs.python.org/3/library/stdtypes.html>

## Test (w Mentorze: Lekcje → Sprawdź się)
- d = {"a": 1}; d["a"] = 5; d["a"] to:
  - A) 1
  - B) 5
  - C) [1, 5]
  - D) błąd
- "b" in {"a": "b"} daje:
  - A) True
  - B) False
  - C) błąd
  - D) None
- Bezpieczny odczyt klucza, którego może nie być:
  - A) d[k]
  - B) d.get(k)
  - C) d.k
  - D) del d[k]
- d.items() zwraca:
  - A) same klucze
  - B) same wartości
  - C) pary (klucz, wartość)
  - D) długość

Odpowiedzi: B, B, B, C
