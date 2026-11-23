# Terminal, katalogi i pierwszy program w Pythonie
Tydzień 0 · lekcja 2 z 16 · ≈ 40 min

**Po tej lekcji potrafisz:** poruszasz się po katalogach w terminalu (cd, ls, mkdir), rozumiesz ścieżkę pliku i uruchamiasz pierwszy program Pythona — w terminalu i przyciskiem ▶ w Mentorze.

**Po co mi to?** Testy, Git i serwery uruchamia się z terminala. Tester, który nie boi się wiersza poleceń, pracuje szybciej i rozumie, co robi CI.

## Czego potrzebujesz
- Windows 10/11 z Mentorem.
- Środowisko kursu zainstalowane w Mentorze (lekcja „Narzędzia”) — przycisk ▶ Uruchom działa po instalacji.

## 1 · Wyjaśnienie od podstaw
### Plik, katalog, ścieżka
Plik to dokument (np. hello.py), katalog (folder) to szuflada na pliki. **Ścieżka** to adres pliku: `C:\Users\Ania\Documents\PRACA\hello.py` — dysk, potem kolejne katalogi oddzielone `\`, na końcu nazwa pliku. Rozszerzenie `.py` mówi, że to program w Pythonie.
### Terminal
Terminal to okno, w którym wpisujesz polecenia zamiast klikać. W Windows: Start → wpisz „PowerShell” → Enter (albo zakładka Terminal w Mentorze). Zachęta `PS C:\Users\Ania>` pokazuje **katalog roboczy** — miejsce, w którym teraz „stoisz”.
| polecenie | co robi | przykład |
|---|---|---|
| `pwd` | pokazuje, gdzie jesteś | `pwd` |
| `ls` (albo `dir`) | lista plików w katalogu | `ls` |
| `cd nazwa` | wejdź do katalogu | `cd Documents` |
| `cd ..` | wyjdź piętro wyżej | `cd ..` |
| `mkdir nazwa` | utwórz katalog | `mkdir PRACA` |
| `python plik.py` | uruchom program | `python hello.py` |
Klawisz **Tab** dopełnia nazwę pliku, strzałka ↑ przywraca poprzednie polecenie. Ścieżkę ze spacją bierzesz w cudzysłów: `cd "Moje dokumenty"`.
### Pierwszy program
Program w Pythonie to zwykły plik tekstowy. `print("Cześć")` wypisuje tekst. `import datetime` dołącza moduł z datami, a `datetime.date.today()` zwraca dzisiejszą datę. Python wykonuje linie **od góry do dołu**.
### Mentor bez terminala
Pod każdym zadaniem z kodem jest pasek „Ćwiczenie w Mentorze”: **Utwórz plik ćwiczenia** → piszesz w edytorze → **Ctrl+S** → **▶ Uruchom** (wynik pod spodem, dane dla `input()` wpisujesz w polu nad wynikiem) → **✔ Sprawdź wynik**. Plik trafia do Twojego katalogu roboczego PRACA. Terminal przyda się od tygodnia 4 (Git) i 7 (pytest).

## 2 · Demonstracja — krok po kroku
**Od pustego katalogu do działającego programu**

```
import datetime

print("Cześć! To mój pierwszy program.")
dzis = datetime.date(2026, 11, 23)
print("Data:", dzis)
print("Rok:", dzis.year)

```

1. W terminalu: `cd Documents` → `mkdir PRACA` → `cd PRACA` → `pwd`. Zobaczysz `...\Documents\PRACA` — tu będą Twoje pliki.
2. W Mentorze (albo w Notatniku) utwórz plik `hello.py` w PRACA i wpisz kod z ramki.
3. `import datetime` — na górze pliku dołączasz moduł z datami. Bez tej linii następna dałaby błąd NameError.
4. `print("Cześć! …")` — tekst w cudzysłowie to napis; print wypisuje go w nowej linii.
5. `dzis = datetime.date(2026, 11, 23)` — tworzysz datę (rok, miesiąc, dzień) i zapisujesz w zmiennej `dzis`. W zadaniu użyjesz `datetime.date.today()` — wtedy data będzie dzisiejsza.
6. `print("Data:", dzis)` — print z dwoma argumentami wstawia między nie spację; data wypisuje się w formacie ROK-MIESIĄC-DZIEŃ.
7. `dzis.year` — z daty wyciągasz sam rok.
8. W terminalu w katalogu PRACA: `python hello.py`. W Mentorze: ▶ Uruchom.

✔ **Oczekiwany wynik:** Trzy linie: powitanie, „Data: 2026-11-23” i „Rok: 2026”.

## 3 · Jak to uruchomić
1. Mentor → zadanie t0z3 → pasek „Ćwiczenie w Mentorze” → Utwórz plik ćwiczenia → wklej/napisz kod → Ctrl+S → ▶ Uruchom.
2. Albo terminal: `cd` do katalogu PRACA → `python hello.py` (w terminalu Mentora polecenie `python` wskazuje środowisko kursu).

## W praktyce
- Każdy projekt w osobnym katalogu w PRACA.
- Przed uruchomieniem: pwd — czy jestem tam, gdzie plik?

## 4 · Ćwiczenie prowadzone
Jesteś w `C:\Users\Ania`. Wpisujesz kolejno: `cd Documents`, `mkdir PRACA`, `cd PRACA`, `mkdir testy`, `cd testy`, `cd ..`. (1) W jakim katalogu jesteś na końcu (pełna ścieżka)? (2) Ile nowych katalogów utworzyłaś? Czas: 10 minut.

📄 `cwiczenia/tydzien_00/terminal_1.md` · rozwiązanie: `rozwiazania/tydzien_00/terminal_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Dopasuj polecenie do celu: (1) zobaczyć pliki w katalogu; (2) wyjść piętro wyżej; (3) uruchomić program raport.py; (4) wejść do katalogu „Moje projekty” (ze spacją). Opcje: `ls`, `cd ..`, `python raport.py`, `cd "Moje projekty"`. Czas: 10 minut.

📄 `cwiczenia/tydzien_00/terminal_2.md` · rozwiązanie: `rozwiazania/tydzien_00/terminal_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **python: can't open file '…\hello.py': [Errno 2] No such file or directory**
  - Przyczyna: Jesteś w innym katalogu niż plik.
  - Jak sprawdzić: `pwd` i `ls` — czy widzisz hello.py?
  - Poprawka: `cd` do katalogu z plikiem albo podaj pełną ścieżkę.
- ✘ **'python' is not recognized as an internal or external command**
  - Przyczyna: Python nie jest dostępny w tym terminalu.
  - Jak sprawdzić: Mentor → Środowisko: status Pythona.
  - Poprawka: Użyj terminala Mentora albo przycisku ▶ Uruchom — korzystają ze środowiska kursu.
- ✘ **SyntaxError: unterminated string literal**
  - Przyczyna: Brakuje zamykającego cudzysłowu.
  - Jak sprawdzić: Sprawdź linię wskazaną w komunikacie.
  - Poprawka: Każdy napis zaczyna się i kończy tym samym cudzysłowem: "…".

## Pułapki
- Plik zapisany jako hello.py.txt (Notatnik dopisuje .txt) — w Eksploratorze włącz „Rozszerzenia nazw plików”.
- Spacja w nazwie pliku programu — nazywaj pliki małymi literami z podkreśleniem: lista_zakupow.py.

## Dodatkowe zadania
1. Utwórz katalog PRACA i sprawdź jego pełną ścieżkę poleceniem pwd.
2. Uruchom hello.py w terminalu i przyciskiem ▶ w Mentorze.
3. Zmień datę w przykładzie i przewidź wynik przed uruchomieniem.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Co pokazuje zachęta PS C:\Users\Ania>?**
  - Katalog roboczy — miejsce, w którym działają polecenia.
- **Jak wejść do katalogu ze spacją w nazwie?**
  - cd "Nazwa ze spacją" — w cudzysłowie.
- **W jakiej kolejności Python wykonuje linie?**
  - Od góry do dołu.

## Co potrafię teraz bez patrzenia na przykład?
Poruszasz się po katalogach (pwd, ls, cd, mkdir), rozumiesz ścieżkę pliku i uruchamiasz program w terminalu oraz w Mentorze.

## Źródła (data dostępu w nawiasie)
Wersje narzędzi i dane rynkowe zmieniają się — przed użyciem w pracy otwórz źródło.
- Python — Using Python on Windows (dostęp 23.11.2026) — <https://docs.python.org/3/using/windows.html>
- Python — Poradnik: Nieformalne wprowadzenie (liczby, napisy, listy) (dostęp 23.11.2026) — <https://docs.python.org/pl/3/tutorial/introduction.html>
- Python — datetime: Basic date and time types (dostęp 23.11.2026) — <https://docs.python.org/3/library/datetime.html>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Które polecenie wychodzi piętro wyżej?
  - A) cd ..
  - B) cd /
  - C) ls ..
  - D) up
- Co zrobi `python hello.py`, gdy pliku nie ma w bieżącym katalogu?
  - A) uruchomi go i tak
  - B) błąd No such file or directory
  - C) utworzy plik
  - D) otworzy edytor
- Po co `import datetime` na górze pliku?
  - A) dla ozdoby
  - B) żeby móc użyć modułu z datami
  - C) żeby przyspieszyć program
  - D) to komentarz

Odpowiedzi: A, B, B
