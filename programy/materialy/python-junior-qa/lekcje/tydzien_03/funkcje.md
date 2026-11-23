# Funkcje: def, parametry, return, docstring, if __name__ == "__main__"
Tydzień 3 · lekcja 12 z 39 · ≈ 45 min

**Po tej lekcji potrafisz:** piszesz funkcje z parametrami i return, dokumentujesz je docstringiem, odróżniasz return od print, używasz wartości domyślnych i chronisz kod bloku `if __name__ == "__main__":` — żeby funkcje dało się testować.

**Po co mi to?** Testy jednostkowe (tydzień 7) wywołują funkcje i sprawdzają, co zwracają. Kod bez funkcji jest prawie nietestowalny — tester to od razu widzi.

## Czego potrzebujesz
- Lekcje tygodni 1–2 (warunki, pętle, listy).

## 1 · Wyjaśnienie od podstaw
### Funkcja = przepis z nazwą
```
def brutto(netto, vat=23):
    """Zwraca cenę brutto z netto i stawki VAT w procentach."""
    return round(netto * (1 + vat / 100), 2)
```
`def` definiuje funkcję, w nawiasie **parametry** (wejście), `return` oddaje **wynik** i kończy funkcję. Wywołanie: `brutto(10)` → 12.3. Wartości w wywołaniu to **argumenty**.
### Wartość domyślna
`vat=23` — gdy nie podasz drugiego argumentu, użyje 23. `brutto(10, 8)` → 10.8. Można nazwać argument: `brutto(netto=10, vat=5)`.
### return a print
`print` tylko pokazuje tekst na ekranie; `return` oddaje wartość, którą można zapisać, porównać i przetestować. Funkcja bez return zwraca `None` — klasyczny błąd: `wynik = funkcja_z_printem()` → None.
### Docstring
Pierwszy napis w potrójnym cudzysłowie w funkcji opisuje, co robi, co przyjmuje i co zwraca (konwencja PEP 257). `help(brutto)` go wyświetli.
### Zasięg zmiennych
Zmienne utworzone w funkcji istnieją tylko w niej. Dane przekazuj parametrami, wynik — return (nie zmiennymi globalnymi).
### if __name__ == "__main__":
Kod w tym bloku wykonuje się tylko przy uruchomieniu pliku (▶ Uruchom), a NIE przy imporcie. Test importuje Twój plik, żeby wywołać funkcje — gdyby input() był poza tym blokiem, test zatrzymałby się w oczekiwaniu na dane. Dlatego w zadaniach od tygodnia 3: funkcje na górze, rozmowa z użytkownikiem (input/print) w bloku main.

## 2 · Demonstracja — krok po kroku
**Ceny brutto w sklepie — trzy funkcje i blok main**

```
def brutto(netto, vat=23):
    """Zwraca cenę brutto (2 miejsca po przecinku) z ceny netto i stawki VAT w %."""
    return round(netto * (1 + vat / 100), 2)


def czy_parzysta(n):
    """True, gdy n jest parzyste."""
    return n % 2 == 0


def wypisz_brutto(netto):
    print("Brutto:", brutto(netto))


if __name__ == "__main__":
    print(brutto(10), brutto(10, 8), brutto(netto=100, vat=5))
    print(czy_parzysta(4), czy_parzysta(7))
    wynik = wypisz_brutto(20)
    print("Funkcja bez return zwraca:", wynik)

```

1. `def brutto(netto, vat=23):` — dwa parametry, drugi z wartością domyślną 23.
2. Docstring w potrójnym cudzysłowie — opis dla ludzi i dla `help(brutto)`.
3. `return round(netto * (1 + vat / 100), 2)` — 10 × 1.23 = 12.3; `round(…, 2)` zaokrągla do groszy.
4. `czy_parzysta` zwraca bool: wynik porównania `n % 2 == 0`.
5. `wypisz_brutto` używa print i NIE ma return — dlatego `wynik` to None. Do testów nadaje się `brutto`, nie `wypisz_brutto`.
6. `if __name__ == "__main__":` — wywołania i print tylko przy uruchomieniu. Test zaimportuje plik i wywoła `brutto(10)` bez wypisywania czegokolwiek.
7. Eksperyment: wywołaj `brutto()` bez argumentu → TypeError: missing 1 required positional argument: 'netto'.

✔ **Oczekiwany wynik:** „12.3 10.8 105.0”, „True False”, „Brutto: 24.6”, „Funkcja bez return zwraca: None”.

## 3 · Jak to uruchomić
1. Zapisz jako ceny.py → ▶ Uruchom.
2. W terminalu Mentora: `python -c "import ceny; print(ceny.brutto(50))"` — import NIE uruchamia bloku main.

## W praktyce
- Każda reguła biznesowa = osobna funkcja z return — łatwa do przetestowania.
- Czytając cudzy kod, zaczynasz od docstringów i nazw funkcji.

## 4 · Ćwiczenie prowadzone
Na wzór `brutto` napisz `def netto(brutto, vat=23): return round(brutto / (1 + vat / 100), 2)`. Podaj wyniki: (1) `netto(12.3)`, (2) `netto(10.8, 8)`, (3) `netto(123)`. Czas: 15 minut.

📄 `cwiczenia/tydzien_03/funkcje_1.md` · rozwiązanie: `rozwiazania/tydzien_03/funkcje_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Funkcja: `def rabat(razem):` / `    if razem >= 100:` / `        print(razem * 0.95)` / `    else:` / `        print(razem)`. Test: `assert rabat(200) == 190`. (1) Co zwraca `rabat(200)`? (2) Czy test przejdzie (tak/nie)? (3) Którą instrukcję zamieniasz w obu gałęziach (wpisz słowo)? Czas: 15 minut.

📄 `cwiczenia/tydzien_03/funkcje_2.md` · rozwiązanie: `rozwiazania/tydzien_03/funkcje_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **TypeError: brutto() missing 1 required positional argument: 'netto'**
  - Przyczyna: Wywołanie bez wymaganego argumentu.
  - Jak sprawdzić: Porównaj wywołanie z def.
  - Poprawka: Podaj argument albo dodaj wartość domyślną.
- ✘ **Wynik funkcji to None**
  - Przyczyna: Brak return (jest tylko print) albo return w złym miejscu.
  - Jak sprawdzić: Dodaj `print(repr(wynik))`.
  - Poprawka: return w każdej gałęzi, która ma oddać wynik.
- ✘ **Test „wisi” albo EOFError przy imporcie**
  - Przyczyna: input() poza blokiem `if __name__ == "__main__":`.
  - Jak sprawdzić: Czy coś poza funkcjami pyta użytkownika?
  - Poprawka: Przenieś input()/print() programu do bloku main.

## Pułapki
- Kod po return w tej samej gałęzi nigdy się nie wykona.
- Lista jako wartość domyślna (def f(x=[])) jest wspólna dla wywołań — używaj None.

## Dodatkowe zadania
1. 5 funkcji z docstringami: pole prostokąta, czy parzysta, maksimum listy bez max(), odwróć napis, silnia.
2. Każda funkcja zwraca wynik (return), wywołania w bloku main.
3. Sprawdź help() jednej funkcji.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Czym różni się return od print?**
  - return oddaje wartość do dalszego użycia i testów; print tylko pokazuje.
- **Co zwraca funkcja bez return?**
  - None.
- **Po co if __name__ == "__main__"?**
  - Żeby kod programu nie wykonywał się przy imporcie (np. przez testy).

## Co potrafię teraz bez patrzenia na przykład?
Piszesz funkcje z parametrami, wartościami domyślnymi, return i docstringiem; oddzielasz logikę (funkcje) od rozmowy z użytkownikiem (blok main) — kod staje się testowalny.

## Źródła (data dostępu w nawiasie)
Wersje narzędzi i dane rynkowe zmieniają się — przed użyciem w pracy otwórz źródło.
- Python — Poradnik: Więcej narzędzi kontroli przepływu (if, for, range, funkcje) (dostęp 23.11.2026) — <https://docs.python.org/pl/3/tutorial/controlflow.html>
- PEP 257 — Docstring Conventions (dostęp 23.11.2026) — <https://peps.python.org/pep-0257/>
- Python — Poradnik: Moduły (dostęp 23.11.2026) — <https://docs.python.org/pl/3/tutorial/modules.html>

## Test (w Mentorze: Lekcje → Sprawdź się)
- def f(x): x * 2 — co zwraca f(3)?
  - A) 6
  - B) None
  - C) 3
  - D) błąd
- def f(a, b=2): return a * b — f(5) to:
  - A) 5
  - B) 10
  - C) 7
  - D) błąd
- Kod w if __name__ == "__main__": wykonuje się:
  - A) zawsze
  - B) tylko przy uruchomieniu pliku
  - C) tylko przy imporcie
  - D) nigdy
- Docstring to:
  - A) komentarz #
  - B) napis z opisem na początku funkcji
  - C) nazwa funkcji
  - D) typ zwracany

Odpowiedzi: B, B, B, B
