# Dokumentacja: README, które pozwala uruchomić projekt w 10 minut
Tydzień 13 · lekcja 41 z 48 · ≈ 45 min

**Po tej lekcji potrafisz:** piszesz README z sekcjami: opis, funkcje, wymagania, instalacja, uruchomienie, testy, konfiguracja (zmienne środowiskowe), ograniczenia, jak powstał, licencja — i sprawdzasz je testem „obcej osoby”.

**Po co mi to?** README to pierwsza rzecz, którą widzi rekruter i klient. Dokumentacja jest też najtańszym kontekstem dla agenta w następnej sesji.

## Czego potrzebujesz
- Repozytorium pod-lipa.
- Lekcja „Prawo” (licencja, sekcja „Jak powstał”).

## 1 · Wyjaśnienie od podstaw
### Sekcje README
| sekcja | treść | błąd agenta, który poprawiasz |
|---|---|---|
| Opis | 2–3 zdania: co, dla kogo, status (szkoleniowy, dane fikcyjne) | marketingowe ogólniki |
| Funkcje | lista tego, co działa | funkcje, których nie ma |
| Wymagania | Windows 10/11, Python 3.12, Git | brak wersji |
| Instalacja | polecenia krok po kroku (venv, pip install -r requirements.txt) | polecenia z Linuksa (source venv/bin/activate) |
| Uruchomienie | `flask --app app run` + adres | brak przykładu |
| Testy | `python -m pytest -q` + co sprawdzają | brak |
| Konfiguracja | zmienne środowiskowe (nazwy, nie wartości!) | prawdziwe klucze w README |
| Ograniczenia | czego nie robi, znane problemy | „brak ograniczeń” |
| Jak powstał | AI + Twój wkład, przegląd, testy | brak |
| Licencja | link do LICENSE | brak |
### Polecenia dla Windows
`py -m venv .venv` → `.venv\Scripts\activate` (CMD) albo `.venv\Scripts\Activate.ps1` (PowerShell) → `pip install -r requirements.txt`. Agenci często wklejają wersję z Linuksa/macOS — sprawdzasz na swoim komputerze.
### Test „obcej osoby”
Klonujesz repozytorium do NOWEGO folderu i wykonujesz README dokładnie krok po kroku, nie korzystając z wiedzy w głowie. Każde miejsce, w którym musiałeś coś zgadnąć, to brakująca linia README. Wersja z AI: nowa sesja agenta w świeżym klonie — „Postępuj wyłącznie według README i zgłoś, gdzie instrukcja jest niejasna”.
### Inne dokumenty projektu
- CHANGELOG.md — co zmieniło się w wersjach (tydzień 15).
- docs/decyzje.md — krótkie zapisy decyzji („dlaczego SQLite, a nie plik JSON”).
- AGENTS.md — instrukcje dla agentów (już masz).
Dokumentacja dzieli się na samouczki, instrukcje, opisy referencyjne i wyjaśnienia (model Diátaxis) — README łączy krótko wszystkie cztery; większe projekty rozdzielają je na osobne strony.

## 2 · Demonstracja — krok po kroku
**Test obcej osoby wykrywa 3 luki**

```
# Pod Lipą — mini system rezerwacji

Projekt szkoleniowy (dane fikcyjne): kalkulator ceny, kalendarz pokoi i API rezerwacji we Flask.

## Wymagania
- Windows 10/11, Python 3.12, Git

## Instalacja
```
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Uruchomienie
```
set FLASK_SECRET_KEY=...
flask --app system run
```
Otwórz http://127.0.0.1:5000

## Testy
```
python -m pytest -q
```
```

1. Agent napisał README. Klonujesz repo do Dokumenty\test-readme i wykonujesz instrukcje.
2. Luka 1: `source .venv/bin/activate` — polecenie z Linuksa. Zamieniasz na wersję CMD/PowerShell.
3. Luka 2: aplikacja nie startuje — README nie mówi o FLASK_SECRET_KEY. Dopisujesz sekcję Konfiguracja (nazwa zmiennej i jak wygenerować wartość).
4. Luka 3: testy wymagają dane/rezerwacje.csv, którego nie ma w repo (był w .gitignore). Decyzja: dodajesz fikcyjny plik przykładowy dane/rezerwacje_przyklad.csv i opisujesz go.
5. Drugi test obcej osoby — przechodzi bez zgadywania.

✔ **Oczekiwany wynik:** README, według którego projekt uruchamia się od zera na czystym Windows bez wiedzy autora.

## 3 · Jak to uruchomić
1. `git clone <adres> test-readme` w nowym folderze → wykonaj README krok po kroku.
2. Zadanie tygodnia → „✔ Sprawdź wynik” (sekcje README).

## W praktyce
- README aktualizujesz w tym samym PR co funkcję.
- Raz na wydanie — test obcej osoby.

## 4 · Ćwiczenie prowadzone
Agent napisał w README: (1) `source .venv/bin/activate`, (2) `POGODA_API_KEY=abc123xyz` w sekcji Konfiguracja, (3) „Brak znanych ograniczeń”, (4) `python -m pytest -q`. Ile linii wymaga poprawy? Którą usuniesz natychmiast i dlaczego (numer)? Czas: 15 minut.

📄 `cwiczenia/tydzien_13/dokumentacja_readme_1.md` · rozwiązanie: `rozwiazania/tydzien_13/dokumentacja_readme_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Uporządkuj sekcje README w kolejności czytania przez nową osobę: A) Testy, B) Opis, C) Instalacja, D) Uruchomienie, E) Wymagania. Ciąg liter. Polecenie aktywacji venv w PowerShell (ścieżka do pliku)? Czas: 15 minut.

📄 `cwiczenia/tydzien_13/dokumentacja_readme_2.md` · rozwiązanie: `rozwiazania/tydzien_13/dokumentacja_readme_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **„'source' is not recognized”.**
  - Przyczyna: Polecenie Linuksa w README.
  - Jak sprawdzić: Sekcja Instalacja.
  - Poprawka: Wersje dla CMD i PowerShell.
- ✘ **„Activate.ps1 cannot be loaded because running scripts is disabled”.**
  - Przyczyna: Zasady wykonywania skryptów PowerShell.
  - Jak sprawdzić: Komunikat w PowerShell.
  - Poprawka: Użyj CMD (`.venv\Scripts\activate`) albo `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` (świadomie) — opisz w README.

## Pułapki
- README z funkcjami „w planach” opisanymi jak gotowe to wprowadzanie w błąd — oddziel „Działa” od „Planowane”.
- Zrzuty ekranu z prawdziwymi danymi — zamaskuj albo użyj danych fikcyjnych.

## Dodatkowe zadania
1. Napisz pełne README (zadanie tygodnia).
2. Test obcej osoby w świeżym klonie.
3. Dodaj docs/decyzje.md z 2 decyzjami.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Co to jest test obcej osoby?**
  - Wykonanie README krok po kroku w świeżym klonie bez wiedzy autora.
- **Co wpisujesz w sekcji Konfiguracja?**
  - Nazwy zmiennych środowiskowych i jak je ustawić — nigdy wartości sekretów.
- **Dlaczego README jest ważne dla agenta?**
  - To tani, stały kontekst projektu w każdej nowej sesji.

## Co potrafię teraz bez patrzenia na przykład?
Piszesz README z 10 sekcjami dla Windows, bez sekretów, z uczciwymi ograniczeniami i informacją o AI, i weryfikujesz je testem obcej osoby.

## Źródła (data dostępu w nawiasie)
Narzędzia, ceny i przepisy zmieniają się — przed użyciem w pracy otwórz źródło.
- GitHub Docs — About READMEs (dostęp 20.11.2026) — <https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes>
- Diátaxis — systematyczne podejście do dokumentacji technicznej (dostęp 20.11.2026) — <https://diataxis.fr/>
- Python — venv w Windows (aktywacja: Scripts\activate) (dostęp 20.11.2026) — <https://docs.python.org/3/library/venv.html>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Aktywacja venv w CMD:
  - A) source .venv/bin/activate
  - B) .venv\Scripts\activate
  - C) activate venv
  - D) pip venv
- Sekcja Konfiguracja zawiera:
  - A) Wartości kluczy
  - B) Nazwy zmiennych i sposób ustawienia
  - C) Hasła testowe
  - D) Nic
- Test obcej osoby wykonujesz:
  - A) W swoim folderze roboczym
  - B) W świeżym klonie, ściśle według README
  - C) W przeglądarce
  - D) Tylko z agentem

Odpowiedzi: B, B, B
