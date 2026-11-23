# Podział kodu na moduły i import własnych plików
Tydzień 5 · lekcja 21 z 39 · ≈ 40 min

**Po tej lekcji potrafisz:** dzielisz program na kilka plików z jedną odpowiedzialnością (dane, logika, interfejs), importujesz własne moduły (import / from … import) i uruchamiasz całość z main.py.

**Po co mi to?** Projekt testowy ma osobno strony (pages/), testy (tests/) i konfigurację. Rekruter po strukturze katalogów widzi, czy umiesz organizować kod.

## Czego potrzebujesz
- Lekcje „Funkcje” i „Klasy”.
- Menedżer zadań z tygodnia 3 (zadanie t3z5).

## 1 · Wyjaśnienie od podstaw
### Moduł = plik .py
Każdy plik .py jest modułem. Jeśli w PRACA masz `zadania.py` z funkcją `dodaj`, w `main.py` piszesz `import zadania` i wołasz `zadania.dodaj(...)` albo `from zadania import dodaj` i wołasz `dodaj(...)`.
### Jedna odpowiedzialność
| plik | odpowiada za | nie robi |
|---|---|---|
| `zadania.py` | logika: dodaj, oznacz, usuń, otwarte | input/print, pliki |
| `plik.py` | zapis/odczyt listy do pliku | logika zadań |
| `main.py` | menu: input/print, wywołuje dwa pozostałe | obliczeń |
Zmiana formatu pliku (txt → JSON) dotyka tylko plik.py; testy logiki dotyczą tylko zadania.py.
### Gdzie Python szuka modułów
Najpierw w katalogu uruchamianego skryptu, potem w bibliotece standardowej i zainstalowanych pakietach. Dlatego **nie nazywaj plików jak moduły standardowe** (random.py, csv.py, json.py) — przykryjesz je.
### Import uruchamia moduł
Import wykonuje cały plik od góry. Wywołania i input() w modułach trzymasz w `if __name__ == "__main__":` — inaczej import (np. w teście) uruchomi menu.
### Pakiet
Katalog z plikami .py (np. `pages/`) i plikiem `__init__.py` (może być pusty) to pakiet: `from pages.login_page import LoginPage`.
### Zapis do pliku: JSON
Listę słowników najprościej zapisać modułem json: `json.dump(lista, f, ensure_ascii=False, indent=2)` i odczytać `json.load(f)` — zachowa typy (liczby, True/False).

## 2 · Demonstracja — krok po kroku
**Trzy pliki zamiast jednego (zapisane i zaimportowane w locie)**

```
import json
import tempfile
from pathlib import Path

katalog = Path(tempfile.mkdtemp())
(katalog / "zadania.py").write_text(
    "def dodaj(lista, tytul):\n"
    "    lista.append({'tytul': tytul.strip(), 'zrobione': False})\n", encoding="utf-8")
(katalog / "plik.py").write_text(
    "import json\n"
    "def zapisz(lista, sciezka):\n"
    "    with open(sciezka, 'w', encoding='utf-8') as f:\n"
    "        json.dump(lista, f, ensure_ascii=False)\n"
    "def wczytaj(sciezka):\n"
    "    with open(sciezka, encoding='utf-8') as f:\n"
    "        return json.load(f)\n", encoding="utf-8")

import sys
sys.path.insert(0, str(katalog))
import zadania
from plik import zapisz, wczytaj

lista = []
zadania.dodaj(lista, " Zamówić zszywki ")
zapisz(lista, katalog / "zadania.json")
print(wczytaj(katalog / "zadania.json"))
print(sorted(p.name for p in katalog.iterdir() if p.suffix in (".py", ".json")))

```

1. Przykład sam tworzy w katalogu tymczasowym dwa moduły — żeby dało się go uruchomić jednym plikiem. W zadaniu po prostu masz w PRACA trzy pliki: zadania.py, plik.py, main.py.
2. `zadania.py` — tylko logika (dodaj).
3. `plik.py` — tylko zapis/odczyt JSON; `ensure_ascii=False` zachowuje polskie litery w pliku.
4. `sys.path.insert(0, …)` — dodaje katalog do miejsc, gdzie Python szuka modułów (w PRACA niepotrzebne — main.py i moduły są obok siebie).
5. `import zadania` → wołasz `zadania.dodaj`; `from plik import zapisz, wczytaj` → wołasz bez przedrostka.
6. Zapis i odczyt: lista wraca z pliku z tymi samymi typami (False zostało bool).

✔ **Oczekiwany wynik:** Lista z jednym zadaniem wczytana z pliku JSON i lista trzech plików w katalogu.

## 3 · Jak to uruchomić
1. W PRACA: zadania.py, plik.py, main.py obok siebie → otwórz main.py → ▶ Uruchom.
2. Terminal: `python main.py` w PRACA.

## W praktyce
- Projekt testów: pages/ (Page Objects), tests/ (testy), conftest.py (fixtures) — każdy z jedną rolą.
- Czytając cudzy projekt, zaczynasz od struktury katalogów i importów w main.

## 4 · Ćwiczenie prowadzone
W PRACA są: `ceny.py` z funkcją `brutto(netto)` i `main.py`. (1) Jak zaimportować samą funkcję (wpisz linię)? (2) Jak ją wtedy wywołać dla 10 (wpisz)? (3) Jak wywołać po `import ceny` (wpisz)? Czas: 10 minut.

📄 `cwiczenia/tydzien_05/moduly_1.md` · rozwiązanie: `rozwiazania/tydzien_05/moduly_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Rozmieść funkcje w plikach zadania.py / plik.py / main.py: (1) `zapisz_json(lista, sciezka)`, (2) `oznacz(lista, nr)`, (3) pętla `while True` z input("Wybór: "), (4) `wczytaj_json(sciezka)`. Dodatkowo: (5) co się stanie po `import csv` w projekcie, w którym masz własny plik csv.py (wybierz)? Czas: 15 minut.

📄 `cwiczenia/tydzien_05/moduly_2.md` · rozwiązanie: `rozwiazania/tydzien_05/moduly_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **ModuleNotFoundError: No module named 'zadania'**
  - Przyczyna: main.py uruchomiony z innego katalogu albo literówka w nazwie pliku.
  - Jak sprawdzić: `ls` — czy zadania.py leży obok main.py?
  - Poprawka: Uruchamiaj z katalogu projektu; nazwa pliku = nazwa w import (bez .py).
- ✘ **ImportError: cannot import name 'dodaj' from 'zadania'**
  - Przyczyna: Brak funkcji o tej nazwie (literówka) albo import cykliczny.
  - Jak sprawdzić: Otwórz zadania.py — czy jest def dodaj?
  - Poprawka: Popraw nazwę; moduły nie importują się nawzajem w kółko.
- ✘ **Import uruchamia menu**
  - Przyczyna: Kod menu poza blokiem __main__ w module.
  - Jak sprawdzić: Co jest poza funkcjami?
  - Poprawka: Przenieś do if __name__ == "__main__":.

## Pułapki
- Plik nazwany jak moduł standardowy (random.py, json.py, test.py) — przykrywa oryginał.
- from modul import * — nie wiesz, skąd pochodzą nazwy; importuj jawnie.

## Dodatkowe zadania
1. Menedżer zadań w 3 plikach z jasną odpowiedzialnością.
2. Zapis i odczyt listy zadań w JSON.
3. Sprawdź, że import zadania nie uruchamia menu.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Co jest modułem w Pythonie?**
  - Każdy plik .py.
- **Dlaczego input() tylko w main.py?**
  - Logika i zapis mają być testowalne i niezależne od interfejsu.
- **Po co __init__.py?**
  - Oznacza katalog jako pakiet (import pages.login_page).

## Co potrafię teraz bez patrzenia na przykład?
Dzielisz program na moduły z jedną odpowiedzialnością, importujesz je i unikasz typowych pułapek nazw i importu uruchamiającego kod.

## Źródła (data dostępu w nawiasie)
Wersje narzędzi i dane rynkowe zmieniają się — przed użyciem w pracy otwórz źródło.
- Python — Poradnik: Moduły (dostęp 23.11.2026) — <https://docs.python.org/pl/3/tutorial/modules.html>
- Python — json: JSON encoder and decoder (dostęp 23.11.2026) — <https://docs.python.org/3/library/json.html>
- PEP 8 — Style Guide for Python Code (dostęp 23.11.2026) — <https://peps.python.org/pep-0008/>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Po `from zadania import dodaj` wywołujesz:
  - A) zadania.dodaj()
  - B) dodaj()
  - C) import.dodaj()
  - D) zadania::dodaj()
- Plik random.py w projekcie:
  - A) przyspiesza losowanie
  - B) przykrywa moduł standardowy random
  - C) jest wymagany
  - D) nic nie zmienia
- Gdzie zapisywanie do pliku w menedżerze zadań?
  - A) main.py
  - B) zadania.py
  - C) plik.py
  - D) wszędzie
- json.dump(..., ensure_ascii=False):
  - A) szyfruje plik
  - B) zachowuje polskie litery czytelne w pliku
  - C) usuwa polskie litery
  - D) kompresuje

Odpowiedzi: B, B, C, B
