# Debugowanie: print, breakpoint() i debugger krok po kroku
Tydzień 6 · lekcja 24 z 39 · ≈ 50 min

**Po tej lekcji potrafisz:** szukasz błędów metodą: odtwórz → zawęź → hipoteza → sprawdź; używasz print z repr, breakpoint() (pdb: n, s, p, c, q) i debuggera w PyCharm (punkt przerwania, Step Over/Into, podgląd zmiennych).

**Po co mi to?** Tester, który potrafi wskazać linię i przyczynę, pisze zgłoszenia, które programista naprawia w minuty, a nie w dni.

## Czego potrzebujesz
- Lekcje etapu 1 (funkcje, pętle, wyjątki).
- Opcjonalnie PyCharm z interpreterem środowiska kursu.

## 1 · Wyjaśnienie od podstaw
### Metoda zamiast zgadywania
1. **Odtwórz**: jakie dane dają zły wynik? Zapisz je. 2. **Zawęź**: która funkcja/linia? 3. **Hipoteza**: „suma liczona jest od 1, nie od 0”. 4. **Sprawdź** jedną zmianą, uruchom ponownie. Zmieniaj jedną rzecz naraz.
### print z repr
`print("DEBUG ilosc=", repr(ilosc), type(ilosc))` — repr pokazuje cudzysłowy i ukryte znaki (`'12\n'`). Usuń printy po naprawie.
### breakpoint() — debugger w terminalu
Wstaw `breakpoint()` w linii, przed którą program ma się zatrzymać, uruchom w terminalu (`python plik.py`). Zobaczysz `(Pdb)`. Polecenia:
| polecenie | co robi |
|---|---|
| `p zmienna` | pokaż wartość |
| `n` (next) | wykonaj linię, nie wchodząc do funkcji |
| `s` (step) | wejdź do wywoływanej funkcji |
| `l` (list) | pokaż kod wokół |
| `c` (continue) | biegnij do następnego breakpointu |
| `q` (quit) | zakończ |
### Debugger w PyCharm
Kliknij na marginesie przy numerze linii — czerwona kropka (breakpoint). Prawy klik → Debug. Program zatrzyma się na kropce; panel Variables pokazuje wszystkie zmienne. **Step Over** (F8) — następna linia, **Step Into** (F7) — do środka funkcji, **Resume** (F9) — dalej. Warunkowy breakpoint (prawy klik na kropce → Condition: `i == 7`) zatrzyma pętlę dopiero przy 7. obrocie.
### Typowe źródła błędów logicznych
Pomyłka o jeden (`range(1, n)` zamiast `range(1, n + 1)`), zła kolejność warunków, akumulator w pętli, porównanie napisu z liczbą, zmienna nadpisana w pętli, `=` zamiast `+=`.

## 2 · Demonstracja — krok po kroku
**Średnia, która „gubi” pierwszy produkt**

```
def srednia_ceny(ceny):
    suma = 0
    for i in range(1, len(ceny)):
        suma += ceny[i]
    return suma / len(ceny)


def srednia_ceny_poprawiona(ceny):
    if not ceny:
        return 0
    suma = 0
    for cena in ceny:
        suma += cena
    return suma / len(ceny)


ceny = [4.0, 2.0, 6.0]
print("Oczekiwane 4.0, otrzymane:", srednia_ceny(ceny))
for i in range(1, len(ceny)):
    print("DEBUG i =", i, "cena =", repr(ceny[i]))
print("Po poprawce:", srednia_ceny_poprawiona(ceny), srednia_ceny_poprawiona([]))

```

1. Odtworzenie: dla [4.0, 2.0, 6.0] oczekujesz 4.0, program daje 2.67. Dane zapisane — błąd jest powtarzalny.
2. Zawężenie: dzielenie jest dobre (przez 3), więc zła jest suma: 8 zamiast 12.
3. Hipoteza: pętla pomija jakiś element. Print debugujący wypisuje i = 1 i 2 — brak i = 0!
4. Przyczyna: `range(1, len(ceny))` zaczyna od 1 — pomyłka o jeden.
5. To samo w pdb: wstaw `breakpoint()` przed `for`, uruchom w terminalu, `n` kilka razy i `p i` — zobaczysz 1 jako pierwszą wartość.
6. Poprawka: pętla po elementach (`for cena in ceny`) i obsługa pustej listy (bez niej `[]` dałoby ZeroDivisionError).
7. Sprawdzenie: 4.0 dla danych z błędu i 0 dla pustej listy. Usuń printy DEBUG.

✔ **Oczekiwany wynik:** „otrzymane: 2.6666666666666665”, dwie linie DEBUG (i = 1, i = 2) i „Po poprawce: 4.0 0”.

## 3 · Jak to uruchomić
1. Zapisz jako debug_demo.py → ▶ Uruchom.
2. Wersja z pdb: dopisz `breakpoint()` na początku srednia_ceny → terminal Mentora → `python debug_demo.py` → `n`, `p i`, `p suma`, `c`.

## W praktyce
- W bug raporcie: dane wejściowe, które odtwarzają błąd, i (jeśli znasz) linia przyczyny.
- Dane z każdego znalezionego błędu → nowy test regresji.

## 4 · Ćwiczenie prowadzone
Funkcja `def razem(koszyk): suma = 0` / `for cena, ilosc in koszyk: suma = cena * ilosc` / `return suma`. Dla koszyka [(2.0, 3), (5.0, 2)] zwraca 10.0 zamiast 16.0. (1) Ile powinna zwrócić? (2) W której instrukcji jest błąd (wpisz poprawioną linię)? (3) Jaką wartość pokazałoby `p suma` w pdb po pierwszym obrocie pętli? Czas: 15 minut.

📄 `cwiczenia/tydzien_06/debug_1.md` · rozwiązanie: `rozwiazania/tydzien_06/debug_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Pętla 1000 zamówień czasem daje zły wynik dla jednego z nich (nr 742). (1) Który sposób jest najszybszy do zbadania: breakpoint w pętli i 742 razy Continue / breakpoint warunkowy `nr == 742` / print wszystkich 1000 zamówień? (2) Jakie polecenie pdb wejdzie do środka wywoływanej funkcji (wpisz literę)? (3) Po znalezieniu błędu — co robisz najpierw: poprawiasz kod / zapisujesz dane, które go wywołują (do testu)? Czas: 15 minut.

📄 `cwiczenia/tydzien_06/debug_2.md` · rozwiązanie: `rozwiazania/tydzien_06/debug_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **breakpoint() nic nie robi w Mentorze**
  - Przyczyna: Przycisk ▶ uruchamia program bez interaktywnej konsoli pdb.
  - Jak sprawdzić: Gdzie uruchamiasz?
  - Poprawka: Uruchom w terminalu (`python plik.py`) albo w debuggerze PyCharm.
- ✘ **PyCharm: Debug nie zatrzymuje się na kropce**
  - Przyczyna: Linia nigdy nie jest wykonywana albo uruchomiono Run zamiast Debug.
  - Jak sprawdzić: Czy kod dochodzi do tej linii?
  - Poprawka: Debug (ikona robaka); kropka w linii, która na pewno się wykona.

## Pułapki
- Zmiana kilku rzeczy naraz — nie wiesz, co naprawiło błąd.
- Zostawione printy DEBUG w kodzie oddanym do recenzji.

## Dodatkowe zadania
1. Program z 3 ukrytymi błędami z paczki kursu: znajdź każdy debuggerem i zapisz przyczynę.
2. Dla każdego błędu zapisz dane, które go wywołują.
3. Przećwicz pdb: n, s, p, c, q.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Jakie są 4 kroki debugowania?**
  - Odtwórz, zawęź, hipoteza, sprawdź.
- **Czym różni się step od next?**
  - step wchodzi do funkcji, next wykonuje linię w całości.
- **Po co repr() w printach?**
  - Pokazuje typ/ukryte znaki (cudzysłowy, \n).

## Co potrafię teraz bez patrzenia na przykład?
Szukasz błędów metodą odtwórz–zawęź–hipoteza–sprawdź, używasz print z repr, pdb i debuggera PyCharm (także warunkowego breakpointu).

## Źródła (data dostępu w nawiasie)
Wersje narzędzi i dane rynkowe zmieniają się — przed użyciem w pracy otwórz źródło.
- Python — pdb: The Python Debugger (breakpoint()) (dostęp 23.11.2026) — <https://docs.python.org/3/library/pdb.html>
- JetBrains — Unified PyCharm (darmowe funkcje podstawowe, Pro w subskrypcji, Community włączony do jednego produktu) (dostęp 23.11.2026) — <https://www.jetbrains.com/help/pycharm/2026.3/unified-pycharm.html>
- ISTQB Glossary — słownik terminów testowania (dostępny w języku polskim) (dostęp 23.11.2026) — <https://glossary.istqb.org/>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Pierwszy krok debugowania:
  - A) zmienić kod
  - B) odtworzyć błąd na konkretnych danych
  - C) przeinstalować Pythona
  - D) zapytać AI
- Polecenie pdb pokazujące wartość zmiennej x:
  - A) show x
  - B) p x
  - C) x?
  - D) print x()
- range(1, len(l)) w sumie pomija:
  - A) ostatni element
  - B) pierwszy element
  - C) nic
  - D) co drugi
- Warunkowy breakpoint przydaje się, gdy:
  - A) program jest krótki
  - B) błąd występuje przy konkretnej iteracji
  - C) nie ma błędu
  - D) zawsze

Odpowiedzi: B, B, B, B
