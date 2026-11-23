# Pliki: open, read, write, with i kodowanie utf-8
Tydzień 4 · lekcja 17 z 39 · ≈ 45 min

**Po tej lekcji potrafisz:** zapisujesz i odczytujesz pliki tekstowe (tryby r, w, a) w bloku with z encoding="utf-8", czytasz plik linia po linii i obsługujesz brak pliku.

**Po co mi to?** Dane testowe, logi i raporty to pliki. Tester czyta logi aplikacji, a skrypty testowe zapisują wyniki do plików.

## Czego potrzebujesz
- Lekcje etapu 1, zwłaszcza „Napisy” (strip, split) i „Obsługa błędów”.

## 1 · Wyjaśnienie od podstaw
### Otwieranie pliku
`open("produkty.txt", "w", encoding="utf-8")` — nazwa, **tryb** i kodowanie znaków. Tryby: `"r"` czytanie (domyślny; brak pliku → FileNotFoundError), `"w"` zapis (tworzy plik albo **kasuje** jego zawartość!), `"a"` dopisywanie na końcu.
### Zawsze with
```
with open("produkty.txt", "w", encoding="utf-8") as f:
    f.write("zeszyt\n")
```
Blok with sam zamyka plik po wyjściu — także gdy wystąpi błąd. Bez zamknięcia zapis może nie trafić na dysk.
### Kodowanie utf-8
Polskie litery w Windows bez `encoding="utf-8"` mogą zamienić się w „krzaki” albo dać UnicodeDecodeError. Od Pythona 3.15 utf-8 jest domyślne (PEP 686), ale kurs używa 3.11–3.13 — pisz encoding zawsze; to też dobry nawyk dla czytelności.
### Czytanie
- `f.read()` — cały plik jako jeden napis;
- `for linia in f:` — linia po linii (oszczędza pamięć); każda linia kończy się `\n`, więc `linia.strip()`;
- `f.readlines()` — lista linii.
### write nie dodaje nowej linii
`f.write("a")` dwa razy da „aa”. Nową linię dopisujesz sam: `f.write(tekst + "\n")`. write przyjmuje tylko str — liczbę zamień `str(liczba)`.
### Ścieżki
Względna nazwa (`"produkty.txt"`) oznacza plik w **katalogu roboczym** (tam, skąd uruchomiono program). `from pathlib import Path` daje wygodne operacje: `Path("dane") / "produkty.csv"`, `.exists()`, `.read_text(encoding="utf-8")`.

## 2 · Demonstracja — krok po kroku
**Zapis, dopisanie i odczyt listy produktów**

```
from pathlib import Path

produkty = ["Zeszyt A5", "Długopis niebieski", "Gumka"]
with open("produkty.txt", "w", encoding="utf-8") as f:
    for p in produkty:
        f.write(p + "\n")
with open("produkty.txt", "a", encoding="utf-8") as f:
    f.write("Klej w sztyfcie\n")
with open("produkty.txt", encoding="utf-8") as f:
    for nr, linia in enumerate(f, 1):
        print(nr, linia.strip())
print("Linii:", len(Path("produkty.txt").read_text(encoding="utf-8").splitlines()))
try:
    open("brak.txt", encoding="utf-8")
except FileNotFoundError:
    print("Nie ma pliku brak.txt")
Path("produkty.txt").unlink()

```

1. Tryb `"w"` tworzy produkty.txt (albo czyści istniejący) i zapisuje 3 linie — `+ "\n"` w każdej.
2. Tryb `"a"` dopisuje czwartą linię na końcu, nie kasując poprzednich.
3. Odczyt: `for nr, linia in enumerate(f, 1)` — enumerate numeruje od 1; `linia.strip()` usuwa `\n`.
4. `Path(...).read_text(...).splitlines()` — cały plik naraz i podział na linie: 4.
5. `open("brak.txt")` w trybie r → FileNotFoundError, złapany except.
6. `unlink()` usuwa plik — przykład sprząta po sobie (w zadaniu plik zostaw!).
7. Zmień `"a"` na `"w"` w drugim bloku i przewidź wynik: zostanie tylko „Klej w sztyfcie”.

✔ **Oczekiwany wynik:** 4 ponumerowane produkty, „Linii: 4”, „Nie ma pliku brak.txt”.

## 3 · Jak to uruchomić
1. Zapisz jako pliki_demo.py w PRACA → ▶ Uruchom.
2. Usuń ostatnią linię (unlink) i otwórz produkty.txt w Eksploratorze — sprawdź polskie litery.

## W praktyce
- Testy zapisujące pliki używają katalogu tymczasowego (tmp_path w pytest, tydzień 7).
- Logi aplikacji czytasz od końca — najnowsze wpisy są na dole.

## 4 · Ćwiczenie prowadzone
Plik `stan.txt` zawiera 3 linie: „10”, „25”, „5”. Kod: `with open("stan.txt", encoding="utf-8") as f: suma = sum(int(l) for l in f)`. (1) Ile wynosi suma? (2) Co będzie w pliku po `open("stan.txt", "w", encoding="utf-8").write("7")`? (3) Ile linii będzie po kolejnym `with open("stan.txt", "a", encoding="utf-8") as f: f.write("\n8")`? Czas: 15 minut.

📄 `cwiczenia/tydzien_04/pliki_1.md` · rozwiązanie: `rozwiazania/tydzien_04/pliki_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Raport zapisuje się tak: `f = open("raport.txt", "w")` / `f.write("Razem: " + 123.5)` / (brak close). Wskaż: (1) jaki błąd rzuci druga linia (wybierz), (2) czego brakuje w pierwszej linii, żeby polskie litery zawsze działały (wpisz argument), (3) jak bezpiecznie zamknąć plik — wybierz: f.close() na końcu / blok with. Czas: 15 minut.

📄 `cwiczenia/tydzien_04/pliki_2.md` · rozwiązanie: `rozwiazania/tydzien_04/pliki_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **FileNotFoundError: [Errno 2] No such file or directory: 'dane.csv'**
  - Przyczyna: Plik w innym katalogu niż katalog roboczy.
  - Jak sprawdzić: `import os; print(os.getcwd())` i `ls`.
  - Poprawka: Uruchom z katalogu z plikiem albo podaj ścieżkę Path(__file__).parent / "dane.csv".
- ✘ **UnicodeDecodeError: 'charmap' codec can't decode byte…**
  - Przyczyna: Plik utf-8 czytany domyślnym kodowaniem Windows.
  - Jak sprawdzić: Czy jest encoding="utf-8"?
  - Poprawka: open(…, encoding="utf-8").
- ✘ **Plik pusty po uruchomieniu**
  - Przyczyna: Tryb "w" przy każdym uruchomieniu kasuje dane / plik nie zamknięty.
  - Jak sprawdzić: Który tryb? Czy jest with?
  - Poprawka: "a" do dopisywania; zawsze with.

## Pułapki
- Tryb w na pliku z danymi — jedno uruchomienie i dane znikają; rób kopię przed eksperymentem.
- Nazwy plików z polskimi znakami i spacjami działają, ale w projektach używaj prostych nazw.

## Dodatkowe zadania
1. Zapisz listę produktów do produkty.txt i odczytaj ją z numerami.
2. Zrób to samo raz bez with i raz z with — zanotuj różnicę.
3. Obsłuż brak pliku komunikatem.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Co robi tryb "w" z istniejącym plikiem?**
  - Kasuje jego zawartość i zapisuje od nowa.
- **Dlaczego with?**
  - Zamyka plik automatycznie, także przy błędzie.
- **Po co encoding="utf-8"?**
  - Żeby polskie znaki zapisywały się i czytały poprawnie w Windows.

## Co potrafię teraz bez patrzenia na przykład?
Zapisujesz, dopisujesz i czytasz pliki w bloku with z utf-8, czytasz linia po linii i obsługujesz brak pliku.

## Źródła (data dostępu w nawiasie)
Wersje narzędzi i dane rynkowe zmieniają się — przed użyciem w pracy otwórz źródło.
- Python — Poradnik: Wejście i wyjście (f-stringi, pliki) (dostęp 23.11.2026) — <https://docs.python.org/pl/3/tutorial/inputoutput.html>
- Python — Poradnik: Błędy i wyjątki (dostęp 23.11.2026) — <https://docs.python.org/pl/3/tutorial/errors.html>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Tryb dopisywania na końcu pliku:
  - A) r
  - B) w
  - C) a
  - D) x
- f.write(5) rzuci:
  - A) nic
  - B) TypeError
  - C) ValueError
  - D) IOError
- for linia in f: — każda linia kończy się:
  - A) spacją
  - B) \n (oprócz ewentualnie ostatniej)
  - C) przecinkiem
  - D) niczym
- Plik względny "dane.txt" jest szukany:
  - A) na pulpicie
  - B) w katalogu roboczym
  - C) w folderze Pythona
  - D) w internecie

Odpowiedzi: C, B, B, B
