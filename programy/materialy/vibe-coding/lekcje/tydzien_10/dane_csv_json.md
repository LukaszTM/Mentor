# Dane: CSV z arkusza i JSON — wczytaj, policz, zapisz
Tydzień 10 · lekcja 31 z 48 · ≈ 55 min

**Po tej lekcji potrafisz:** wczytujesz polski plik CSV z arkusza (średnik, przecinek dziesiętny, polskie znaki), liczysz z niego raport (sumy miesięczne, najczęstsza wartość) i zapisujesz wynik do JSON.

**Po co mi to?** Klienci trzymają dane w arkuszach. „Zrób mi raport z tego pliku” to najczęstsze małe zlecenie — i najczęstsze źródło cichych błędów AI (zły separator, zła liczba).

## Czego potrzebujesz
- Lekcje „Czytanie kodu 2” i „Debugowanie”.
- Plik dane/rezerwacje.csv z materiałów kursu.

## 1 · Wyjaśnienie od podstaw
### CSV po polsku
CSV to tabela w pliku tekstowym: jedna linia = jeden wiersz. Polski Excel zapisuje CSV ze ŚREDNIKIEM jako separatorem (bo przecinek jest dziesiętny) i często z niewidocznym znacznikiem BOM na początku (kodowanie „UTF-8 z BOM”).
```
data_przyjazdu;pokoj;noce;osoby;kwota
2026-07-03;Lipowy;3;2;1080,00
2026-07-10;Dębowy;7;4;3528,00
```
### Wczytanie bez pułapek
```
import csv
with open(sciezka, encoding="utf-8-sig", newline="") as f:
    wiersze = list(csv.DictReader(f, delimiter=";"))
```
- `utf-8-sig` usuwa BOM — bez tego pierwsza kolumna nazywa się „\ufeffdata_przyjazdu” i KeyError murowany.
- `delimiter=";"` — bez tego cały wiersz to jedna kolumna.
- DictReader daje słowniki z NAPISAMI: `"1080,00"`. Liczby zamieniasz: `float(w["kwota"].replace(",", "."))`, `int(w["noce"])`.
### Raport: grupowanie
Suma na miesiąc: klucz to pierwsze 7 znaków daty (`"2026-07"`), słownik sum: `sumy[m] = sumy.get(m, 0) + kwota`. Najczęstsza wartość: `collections.Counter(pokoje).most_common(1)` — ale przy remisie zdecyduj regułę (np. alfabetycznie) i zapisz ją w specyfikacji.
### JSON — format wymiany
JSON wygląda jak słowniki i listy Pythona. `json.dump(dane, f, ensure_ascii=False, indent=2)` zapisuje czytelnie z polskimi znakami (bez ensure_ascii=False „Dębowy” zapisze się jako „D\u0119bowy”). `json.load(f)` wczytuje.
### Sprawdzenie raportu od agenta
- Policz ręcznie jedną liczbę (np. lipiec) z 3–4 wierszy — zgadza się?
- Sprawdź liczbę wczytanych wierszy (`len`) z liczbą wierszy w pliku minus nagłówek.
- Sprawdź wiersz z polskimi znakami i największą kwotą.
- Pusty wiersz na końcu pliku nie może wywracać programu.
### Dane osobowe w plikach
Plik klienta z imionami, telefonami i e-mailami to dane osobowe (RODO). Do agenta i czatu wysyłasz plik z danymi zastąpionymi przykładowymi albo tylko nagłówek i 3 zmyślone wiersze (tydzień 12).

## 2 · Demonstracja — krok po kroku
**Raport, który „działał”, ale liczył źle**

```
import csv
import io

plik = io.StringIO("\ufeffdata_przyjazdu;pokoj;noce;kwota\n2026-07-03;Lipowy;3;1080,00\n2026-07-10;Dębowy;7;3528,00\n2026-08-01;Lipowy;2;720,00\n")
wiersze = list(csv.DictReader(plik, delimiter=";"))
print(repr(list(wiersze[0].keys())[0]))     # niewidoczny BOM z Excela
wiersze = [{k.lstrip("\ufeff"): v for k, v in w.items()} for w in wiersze]   # przy open() zrobi to encoding="utf-8-sig"
sumy = {}
for w in wiersze:
    m = w["data_przyjazdu"][:7]
    sumy[m] = sumy.get(m, 0) + float(w["kwota"].replace(",", "."))
print(sumy)

```

1. Prośba do agenta: „raport przychodu miesięcznego z dane/rezerwacje.csv”. Wynik uruchomienia: KeyError: 'data_przyjazdu'.
2. print(wiersze[0].keys()) pokazuje '\ufeffdata_przyjazdu' — BOM z Excela. Poprawka: encoding="utf-8-sig".
3. Drugie uruchomienie: lipiec = 4608.0 — sprawdzasz ręcznie dwa wiersze lipca: 1080 + 3528 = 4608 ✔. Ale łączna liczba wierszy: 40 zamiast 41 — agent pomija wiersze, w których kwota ma spację tysięcy („1 080,00”) przez `except ValueError: continue`.
4. To cichy błąd (pulapka z tygodnia 2): poprawka parsowania (usuń spacje) i usunięcie „except: continue” — zamiast pomijać, raport ma zgłaszać zły wiersz z numerem.
5. Zapis do raport.json z ensure_ascii=False — „Dębowy” czytelny.

✔ **Oczekiwany wynik:** Raport liczy wszystkie wiersze, poprawnie czyta polski CSV i głośno zgłasza złe wiersze zamiast je pomijać.

## 3 · Jak to uruchomić
1. Skopiuj dane/rezerwacje.csv z materiałów do PRACA\dane.
2. Zadanie tygodnia → raport.py → „✔ Sprawdź wynik”.

## W praktyce
- Raport zawsze z liczbą wczytanych wierszy na końcu.
- Specyfikacja formatu pliku (separator, kodowanie, format liczb) przed kodem.

## 4 · Ćwiczenie prowadzone
Przeczytaj przykład lekcji (dane jak z Excela: BOM, średnik, przecinek dziesiętny). (1) Jaki niewidoczny znak pokazuje pierwsza linia wyniku przed nazwą kolumny — wpisz jego zapis z repr (zaczyna się od \u)? (2) Suma dla „2026-07”. (3) Liczba miesięcy w słowniku. Czas: 20 minut.

📄 `cwiczenia/tydzien_10/dane_csv_json_1.md` · rozwiązanie: `rozwiazania/tydzien_10/dane_csv_json_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Dopasuj objaw do przyczyny: (1) KeyError: 'data_przyjazdu' mimo że kolumna jest w pliku, (2) każdy wiersz ma jedną kolumnę z całym tekstem, (3) ValueError: could not convert string to float: '1080,00', (4) w JSON widać „D\u0119bowy”. Przyczyny: BOM (utf-8-sig) / brak delimiter=";" / przecinek dziesiętny / brak ensure_ascii=False. Czas: 15 minut.

📄 `cwiczenia/tydzien_10/dane_csv_json_2.md` · rozwiązanie: `rozwiazania/tydzien_10/dane_csv_json_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **„UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb9”.**
  - Przyczyna: Plik zapisany w Windows-1250 (stary Excel „CSV (rozdzielany przecinkami)”).
  - Jak sprawdzić: Otwórz w Notatniku → Zapisz jako → kodowanie.
  - Poprawka: Zapisz plik jako „CSV UTF-8” w Excelu albo wczytaj encoding="cp1250" (i zapisz to w specyfikacji).
- ✘ **Raport ma mniej wierszy niż plik.**
  - Przyczyna: Ciche pomijanie (except: continue) albo puste wiersze.
  - Jak sprawdzić: len(wiersze) vs liczba linii.
  - Poprawka: Zgłaszaj zły wiersz z numerem zamiast pomijać; puste wiersze pomijaj jawnie (if not any(w.values())).
- ✘ **Kwoty 10 razy za duże/małe.**
  - Przyczyna: Kropka jako separator tysięcy („1.080,00”).
  - Jak sprawdzić: Przykładowa kwota przed i po konwersji.
  - Poprawka: Usuń kropki i spacje tysięcy, potem przecinek → kropka.

## Pułapki
- Agent często zakłada amerykański CSV (przecinek, kropka). Zawsze pokaż mu nagłówek i 2–3 prawdziwe (zanonimizowane) wiersze.
- Nie wysyłaj do AI całego pliku klienta z danymi osobowymi.

## Dodatkowe zadania
1. Zbuduj raport.py dla dane/rezerwacje.csv (zadanie tygodnia).
2. Policz ręcznie jeden miesiąc i porównaj.
3. Zapisz raport.json z ensure_ascii=False.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Dlaczego encoding="utf-8-sig"?**
  - Usuwa BOM z plików z Excela — inaczej nazwa pierwszej kolumny ma niewidoczny znak.
- **Jak zamienić „1 080,00” na liczbę?**
  - Usunąć spacje (także twarde), przecinek zamienić na kropkę, float().
- **Po co ensure_ascii=False?**
  - Żeby polskie znaki w JSON były czytelne.

## Co potrafię teraz bez patrzenia na przykład?
Wczytujesz polski CSV (średnik, BOM, przecinek), liczysz raport z grupowaniem, zapisujesz JSON i sprawdzasz wyniki ręcznym rachunkiem.

## Źródła (data dostępu w nawiasie)
Narzędzia, ceny i przepisy zmieniają się — przed użyciem w pracy otwórz źródło.
- Python — moduł csv (DictReader, delimiter) — oficjalna dokumentacja (dostęp 20.11.2026) — <https://docs.python.org/3/library/csv.html>
- Python — moduł json (dump, load, ensure_ascii) (dostęp 20.11.2026) — <https://docs.python.org/3/library/json.html>
- Python — pathlib (ścieżki niezależne od systemu) (dostęp 20.11.2026) — <https://docs.python.org/3/library/pathlib.html>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Separator w CSV z polskiego Excela to zwykle:
  - A) przecinek
  - B) średnik
  - C) tabulator
  - D) spacja
- KeyError dla pierwszej kolumny mimo poprawnej nazwy — przyczyna:
  - A) BOM — użyj utf-8-sig
  - B) Za duży plik
  - C) Brak internetu
  - D) Zła wersja Pythona
- Raport pomija błędne wiersze przez except: continue. To:
  - A) Dobra praktyka
  - B) Cichy błąd — zgłaszaj wiersz z numerem
  - C) Wymóg RODO
  - D) Szybsze
- Polskie znaki w JSON czytelne dzięki:
  - A) indent=2
  - B) ensure_ascii=False
  - C) sort_keys
  - D) encoding=ascii

Odpowiedzi: B, A, B, B
