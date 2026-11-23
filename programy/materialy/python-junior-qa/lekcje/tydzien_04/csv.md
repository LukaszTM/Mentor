# Moduł csv: DictReader, DictWriter i statystyki z pliku
Tydzień 4 · lekcja 18 z 39 · ≈ 55 min

**Po tej lekcji potrafisz:** czytasz plik CSV jako listę słowników (DictReader), zamieniasz pola na liczby, liczysz statystyki (suma, średnia, maksimum, filtr) i zapisujesz CSV (DictWriter) z newline="".

**Po co mi to?** Eksporty z systemów, dane testowe i raporty to najczęściej CSV. Tester porównuje eksport z oczekiwanym — i sprawdza separator, polskie znaki i puste pola.

## Czego potrzebujesz
- Lekcje „Pliki” i „Słowniki”.
- Plik dane/produkty.csv z paczki kursu (Mój projekt → „Skopiuj materiały kursu tutaj”).

## 1 · Wyjaśnienie od podstaw
### Czym jest CSV
Tekst, w którym każda linia to wiersz tabeli, a pola rozdziela przecinek (albo średnik — polski Excel często zapisuje średnikiem). Pierwsza linia to zwykle **nagłówek**:
```
id,nazwa,kategoria,cena,ilosc
1,Zeszyt A5 w kratkę,zeszyty,4.50,120
```
### DictReader — wiersz jako słownik
```
import csv
with open("dane/produkty.csv", encoding="utf-8", newline="") as f:
    wiersze = list(csv.DictReader(f))
```
Każdy wiersz to słownik `{"id": "1", "nazwa": "Zeszyt…", "cena": "4.50", …}` — **wszystkie wartości są napisami**; liczby zamieniasz `float(w["cena"])`, `int(w["ilosc"])`. Separator inny niż przecinek: `csv.DictReader(f, delimiter=";")`.
### Dlaczego csv, a nie split(",")
Nazwa „Papier, 500 ark.” w cudzysłowie zawiera przecinek — moduł csv rozumie cudzysłowy, split nie.
### Zapis — DictWriter
```
with open("raport.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["nazwa", "wartosc"])
    w.writeheader()
    w.writerow({"nazwa": "Zeszyt", "wartosc": 540.0})
```
`newline=""` — bez tego w Windows pojawiają się puste linie co drugi wiersz.
### Statystyki
Suma: akumulator w pętli albo `sum(float(w["cena"]) for w in wiersze)`. Średnia: suma / len (pilnuj pustej listy). Maksimum: `max(wiersze, key=lambda w: float(w["cena"]))`. Filtr: lista składana z warunkiem.

## 2 · Demonstracja — krok po kroku
**Statystyki magazynu z CSV**

```
import csv
import io

DANE = """id,nazwa,kategoria,cena,ilosc
1,Zeszyt A5 w kratkę,zeszyty,4.50,120
3,Długopis niebieski,pisaki,2.30,300
9,"Papier ksero A4, 500 ark.",papier,24.99,35
17,Zszywki 1000 szt.,biuro,3.90,0
"""
wiersze = list(csv.DictReader(io.StringIO(DANE)))
print("Produktów:", len(wiersze), "| pierwszy:", wiersze[0]["nazwa"])
ceny = [float(w["cena"]) for w in wiersze]
print(f"Średnia cena: {sum(ceny) / len(ceny):.2f}")
najdrozszy = max(wiersze, key=lambda w: float(w["cena"]))
print("Najdroższy:", najdrozszy["nazwa"])
brak = [w["nazwa"] for w in wiersze if int(w["ilosc"]) == 0]
print("Brak na stanie:", brak)
wartosc = sum(float(w["cena"]) * int(w["ilosc"]) for w in wiersze)
print(f"Wartość magazynu: {wartosc:.2f} zł")
wyjscie = io.StringIO()
pisarz = csv.DictWriter(wyjscie, fieldnames=["nazwa", "wartosc"], lineterminator="\n")
pisarz.writeheader()
pisarz.writerow({"nazwa": "Zeszyt A5 w kratkę", "wartosc": 540.0})
print(wyjscie.getvalue(), end="")

```

1. `DANE` — fragment pliku dane/produkty.csv wpisany w kod, żeby przykład działał bez pliku; `io.StringIO(DANE)` udaje otwarty plik. W zadaniu użyjesz `open("dane/produkty.csv", encoding="utf-8", newline="")`.
2. `list(csv.DictReader(...))` — 4 słowniki; klucze z nagłówka.
3. Wiersz 9 ma nazwę w cudzysłowie z przecinkiem — csv poprawnie czyta „Papier ksero A4, 500 ark.” jako jedno pole.
4. `[float(w["cena"]) for w in wiersze]` — lista cen jako liczby; średnia (4.50 + 2.30 + 24.99 + 3.90) / 4 = 8.92.
5. `max(..., key=lambda w: float(w["cena"]))` — porównanie jako liczb. Bez float porównałbyś napisy: „4.50” > „24.99”!
6. Filtr: produkty z ilością 0.
7. Wartość magazynu: suma cena × ilość = 4.50×120 + 2.30×300 + 24.99×35 + 3.90×0 = 540 + 690 + 874.65 + 0 = 2104.65 zł.
8. DictWriter: nagłówek + wiersz; `lineterminator="\n"` tylko dla StringIO — przy pliku wystarczy newline="".

✔ **Oczekiwany wynik:** Liczba produktów, średnia 8.92, najdroższy papier, lista braków, wartość magazynu i 2 linie CSV z DictWriter.

## 3 · Jak to uruchomić
1. Zapisz jako csv_demo.py → ▶ Uruchom.
2. Wersja z plikiem: Mój projekt → „Skopiuj materiały kursu tutaj” → w PRACA jest dane/produkty.csv → zamień StringIO na open(...).

## W praktyce
- Testując eksport CSV: separator, kodowanie, polskie znaki, liczby z przecinkiem, puste pola.
- Dane testowe w CSV — łatwo dopisać nowy przypadek bez zmiany kodu.

## 4 · Ćwiczenie prowadzone
Plik: nagłówek `nazwa,cena,ilosc` i wiersze `Klej,3.40,110`, `Nożyczki,8.90,30`, `Zszywacz,19.90,15`. Na wzór demonstracji policz: (1) liczbę wierszy danych (bez nagłówka), (2) średnią cenę z 2 miejscami, (3) nazwę produktu o najmniejszej ilości, (4) wartość magazynu (cena × ilość, suma). Czas: 20 minut.

📄 `cwiczenia/tydzien_04/csv_1.md` · rozwiązanie: `rozwiazania/tydzien_04/csv_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Kolega liczy maksimum: `max(wiersze, key=lambda w: w["cena"])` dla cen „4.50”, „24.99”, „7.50”. (1) Który produkt wskaże (podaj cenę)? (2) Dlaczego (wybierz)? (3) Jak poprawić key (wpisz)? Czas: 15 minut.

📄 `cwiczenia/tydzien_04/csv_2.md` · rozwiązanie: `rozwiazania/tydzien_04/csv_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **KeyError: 'cena'**
  - Przyczyna: Separator ; w pliku — DictReader widzi jeden klucz „nazwa;cena;ilosc”; albo literówka/BOM w nagłówku.
  - Jak sprawdzić: `print(wiersze[0].keys())`.
  - Poprawka: `delimiter=";"`; plik z Excela zapisuj jako CSV UTF-8 i otwieraj encoding="utf-8-sig".
- ✘ **ValueError: could not convert string to float: '4,50'**
  - Przyczyna: Przecinek dziesiętny z polskiego Excela.
  - Jak sprawdzić: `print(repr(w["cena"]))`.
  - Poprawka: `float(w["cena"].replace(",", "."))`.
- ✘ **Puste linie między wierszami w zapisanym CSV**
  - Przyczyna: Brak newline="" przy zapisie w Windows.
  - Jak sprawdzić: Otwórz plik w Notatniku.
  - Poprawka: open(…, "w", encoding="utf-8", newline="").

## Pułapki
- Wartości z CSV to napisy — porównania i sortowanie bez float/int dają złe wyniki.
- Puste pole (`,,`) to pusty napis "" — float("") → ValueError; obsłuż je.

## Dodatkowe zadania
1. Wczytaj dane/produkty.csv i policz średnią cenę.
2. Lista produktów z ilością 0.
3. Zapisz raport wartości magazynu do raport.csv.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Jakiego typu są wartości z DictReader?**
  - Napisy (str).
- **Po co newline="" przy zapisie?**
  - Żeby w Windows nie było pustych linii.
- **Jak czytać CSV ze średnikami?**
  - csv.DictReader(f, delimiter=";").

## Co potrafię teraz bez patrzenia na przykład?
Czytasz CSV jako listę słowników, zamieniasz pola na liczby, liczysz statystyki i filtry oraz zapisujesz raport DictWriter.

## Źródła (data dostępu w nawiasie)
Wersje narzędzi i dane rynkowe zmieniają się — przed użyciem w pracy otwórz źródło.
- Python — csv: CSV File Reading and Writing (dostęp 23.11.2026) — <https://docs.python.org/3/library/csv.html>
- Python — Poradnik: Wejście i wyjście (f-stringi, pliki) (dostęp 23.11.2026) — <https://docs.python.org/pl/3/tutorial/inputoutput.html>

## Test (w Mentorze: Lekcje → Sprawdź się)
- DictReader zwraca wiersz jako:
  - A) listę
  - B) słownik
  - C) krotkę
  - D) napis
- float("4,50") daje:
  - A) 4.5
  - B) ValueError
  - C) 450
  - D) 4
- "7.50" > "24.99" (napisy):
  - A) True
  - B) False
  - C) błąd
  - D) None
- Plik z polskiego Excela ze średnikami czytasz z:
  - A) delimiter=";"
  - B) sep=";"
  - C) split(";")
  - D) nic nie trzeba

Odpowiedzi: B, B, A, A
