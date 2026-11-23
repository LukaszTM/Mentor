# Narzędzia: środowisko kursu w Mentorze, Git, edytor i (opcjonalnie) Claude Code
Tydzień 0 · lekcja 3 z 39 · ≈ 40 min

**Po tej lekcji potrafisz:** masz zainstalowane środowisko kursu (Python + pytest, requests, selenium, flask) w Mentorze, Git for Windows i wiesz, jak sprawdzić każde narzędzie — oraz co zrobić przy typowym błędzie instalacji.

**Po co mi to?** Połowa problemów początkujących to „u mnie nie działa” przez złą wersję Pythona albo brak biblioteki. Środowisko kursu jest takie samo u każdego ucznia — błędy dotyczą kodu, nie instalacji.

## Czego potrzebujesz
- Windows 10/11, ok. 1 GB wolnego miejsca, internet przy pierwszej instalacji.
- Uprawnienia administratora NIE są potrzebne.

## 1 · Wyjaśnienie od podstaw
### Środowisko kursu (Mentor → Środowisko)
Mentor tworzy **osobne środowisko wirtualne** (.venv) tylko dla tego kursu. Jeśli na komputerze nie ma odpowiedniego Pythona (3.11–3.13), Mentor za Twoją zgodą pobiera Pythona 3.12 z zaufanego, podpisanego sumą archiwum. Biblioteki instaluje z pliku blokady (lock) — dokładne wersje sprawdzone sumami SHA-256: pytest 9.2, requests 2.34, selenium 4.52, flask 3.1. Dzięki temu nie trafisz na „najnowszą” wersję, która akurat coś zmieniła.
- Status zielony = gotowe. Żółty = brak elementu, przycisk „Napraw”. Czerwony = opis błędu po polsku i następny krok.
- Środowisko możesz usunąć i odtworzyć jednym przyciskiem — Twoje pliki w PRACA zostają.
### Wersje Pythona — skąd różnica?
Na python.org najnowszy jest Python 3.15 (wydany 9.10.2026). Kurs używa 3.11–3.13, bo dla tych wersji zablokowano i przetestowano biblioteki. Wszystko, czego się uczysz, działa tak samo w 3.15.
### Git for Windows (potrzebny od tygodnia 0)
Git zapisuje historię zmian w projekcie. Instalacja: oficjalna strona git-scm.com → Download for Windows → instalator 64-bit; w kreatorze zostaw domyślne opcje (edytor możesz zmienić na Notepad). Albo w PowerShell: `winget install --id Git.Git -e`. Sprawdzenie w NOWYM oknie terminala: `git --version` → np. `git version 2.5x.x.windows.1`.
### Edytor
Wystarczy edytor Mentora. Jeśli chcesz IDE: **PyCharm** — od 2025 r. jeden produkt; podstawowe funkcje (edytor, debugger, uruchamianie testów) są darmowe, funkcje Pro wymagają subskrypcji (30 dni próbnych). W PyCharm wskaż interpreter środowiska kursu: Settings → Python Interpreter → Add → Existing → `…\.venv\Scripts\python.exe` (ścieżkę pokazuje Mentor → Środowisko).
### Claude Code (opcjonalny)
Asystent AI w terminalu. Wymaga płatnego planu (Pro lub wyższy) albo konta API. Kurs **nie wymaga** Claude Code — Asystent Offline w Mentorze i darmowy czat wystarczą. Jeśli chcesz: instalacja według oficjalnej dokumentacji (PowerShell: `irm https://claude.ai/install.ps1 | iex`), sprawdzenie `claude --version`.
### Sprawdzanie każdego narzędzia
| narzędzie | polecenie | dobry wynik |
|---|---|---|
| środowisko kursu | Mentor → Środowisko → Sprawdź | wszystkie pozycje zielone |
| Python kursu | terminal Mentora: `python --version` | Python 3.11–3.13 |
| Git | `git --version` | git version 2.… |
| pytest | terminal Mentora: `python -m pytest --version` | pytest 9.2.0 |

## 2 · Demonstracja — krok po kroku
**Program, który sprawdza środowisko kursu**

```
import sys
import importlib.util

print("Python:", sys.version_info.major, sys.version_info.minor)
for nazwa in ["pytest", "requests", "selenium", "flask"]:
    jest = importlib.util.find_spec(nazwa) is not None
    print(nazwa, "OK" if jest else "BRAK")

```

1. `import sys` — moduł z informacjami o uruchomionym Pythonie; `sys.version_info.major` i `.minor` to np. 3 i 12.
2. `import importlib.util` — narzędzie do sprawdzania, czy moduł da się zaimportować, bez importowania go.
3. `for nazwa in [...]` — pętla przechodzi po czterech nazwach bibliotek (pętle poznasz w tygodniu 2; tu wystarczy: „dla każdej nazwy zrób…”).
4. `importlib.util.find_spec(nazwa) is not None` — prawda, gdy biblioteka jest zainstalowana w TYM Pythonie.
5. `"OK" if jest else "BRAK"` — wybór jednego z dwóch napisów.
6. Uruchom przyciskiem ▶ w Mentorze (środowisko kursu): wszystkie 4 = OK. Uruchom zwykłym `python` spoza Mentora: często zobaczysz BRAK — to dowód, że środowisko kursu jest osobne.

✔ **Oczekiwany wynik:** Python: 3 12 (albo 3 11 / 3 13) i cztery linie „… OK”.

## 3 · Jak to uruchomić
1. Mentor → Środowisko → „Sprawdź” → jeśli trzeba „Zainstaluj / Napraw” → potwierdź.
2. Git: git-scm.com → Download for Windows → instalator → domyślne opcje → nowe okno terminala → `git --version`.
3. Program z demonstracji: zapisz jako srodowisko.py w PRACA → ▶ Uruchom.

## W praktyce
- Po każdej większej aktualizacji Windows: Mentor → Środowisko → Sprawdź.
- Zgłaszając problem, zawsze podaj wynik `python --version` i `git --version`.

## 4 · Ćwiczenie prowadzone
Odczytaj wyniki sprawdzenia: `python --version` → „Python 3.12.12”, `python -m pytest --version` → „pytest 9.2.0”, `git --version` → „'git' is not recognized…”. (1) Czy Python kursu jest w obsługiwanej wersji? (2) Którego narzędzia brakuje? Czas: 10 minut.

📄 `cwiczenia/tydzien_00/instalacja_1.md` · rozwiązanie: `rozwiazania/tydzien_00/instalacja_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Dobierz naprawę: (1) zainstalowałeś(-aś) Gita, ale terminal dalej mówi „git is not recognized”; (2) Mentor → Środowisko: „Brak gotowego pakietu (wheel) dla tej wersji Pythona”; (3) PyCharm podkreśla `import pytest` na czerwono, a w Mentorze testy działają. Opcje: otwórz nowe okno terminala / pozwól Mentorowi pobrać Pythona 3.12 / wskaż w PyCharm interpreter z .venv kursu. Czas: 10 minut.

📄 `cwiczenia/tydzien_00/instalacja_2.md` · rozwiązanie: `rozwiazania/tydzien_00/instalacja_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **'git' is not recognized as an internal or external command**
  - Przyczyna: Git niezainstalowany albo terminal otwarty przed instalacją.
  - Jak sprawdzić: Nowe okno → `git --version`.
  - Poprawka: Zainstaluj Git for Windows z git-scm.com (domyślne opcje) i otwórz nowe okno.
- ✘ **ModuleNotFoundError: No module named 'pytest'**
  - Przyczyna: Program uruchomiony innym Pythonem niż środowisko kursu.
  - Jak sprawdzić: W tym samym terminalu: `python -c "import sys; print(sys.executable)"` — czy ścieżka zawiera .venv kursu?
  - Poprawka: Uruchamiaj przyciskiem ▶ w Mentorze albo w terminalu Mentora.
- ✘ **Instalacja środowiska przerwana (brak internetu / miejsca)**
  - Przyczyna: Pobieranie nie mogło się dokończyć.
  - Jak sprawdzić: Mentor → Środowisko → opis błędu.
  - Poprawka: Zwolnij miejsce / podłącz sieć → „Napraw”. Instalację można powtórzyć bez szkody.

## Pułapki
- Instalowanie bibliotek „na ślepo” poleceniem pip do systemowego Pythona — w kursie robi to wyłącznie Mentor, do .venv kursu.
- Pobieranie instalatorów z nieoficjalnych stron — tylko git-scm.com, python.org, jetbrains.com, claude.ai.

## Dodatkowe zadania
1. Zainstaluj środowisko kursu w Mentorze (wszystko zielone).
2. Zainstaluj Git for Windows i sprawdź git --version.
3. Uruchom program z demonstracji i porównaj wynik z uruchomieniem spoza Mentora.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Dlaczego kurs ma osobne środowisko .venv?**
  - Żeby wersje bibliotek były takie same u wszystkich i nie mieszały się z innymi programami.
- **Co zrobić, gdy po instalacji Gita polecenie nie działa?**
  - Otworzyć nowe okno terminala (nowy PATH).
- **Czy Claude Code jest wymagany?**
  - Nie — Asystent Offline i darmowy czat wystarczą.

## Co potrafię teraz bez patrzenia na przykład?
Masz środowisko kursu z dokładnymi wersjami bibliotek, Gita i edytor; umiesz sprawdzić każde narzędzie i naprawić typowe błędy instalacji.

## Źródła (data dostępu w nawiasie)
Wersje narzędzi i dane rynkowe zmieniają się — przed użyciem w pracy otwórz źródło.
- Python — Using Python on Windows (dostęp 23.11.2026) — <https://docs.python.org/3/using/windows.html>
- Python 3.15.0 — informacja o wydaniu (9.10.2026; instalator Windows, Python install manager) (dostęp 23.11.2026) — <https://python.org/downloads/release/python-3150/>
- Python — Poradnik: Środowiska wirtualne i pakiety (dostęp 23.11.2026) — <https://docs.python.org/pl/3/tutorial/venv.html>
- JetBrains — Unified PyCharm (darmowe funkcje podstawowe, Pro w subskrypcji, Community włączony do jednego produktu) (dostęp 23.11.2026) — <https://www.jetbrains.com/help/pycharm/2026.3/unified-pycharm.html>
- Claude Code — Set up Claude Code (instalacja, Windows) (dostęp 23.11.2026) — <https://code.claude.com/docs/en/setup>
- Pro Git (wydanie 2, wersja polska) — Scott Chacon, Ben Straub (dostęp 23.11.2026) — <https://git-scm.com/book/pl/v2>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Gdzie Mentor instaluje biblioteki kursu?
  - A) do systemowego Pythona
  - B) do osobnego .venv kursu
  - C) do folderu Windows
  - D) nigdzie — są w chmurze
- Po co plik blokady (lock)?
  - A) żeby nikt nie zmienił kodu
  - B) dokładne, sprawdzone wersje bibliotek z sumami SHA-256
  - C) żeby kurs był płatny
  - D) blokuje internet
- Git zainstalowany, ale „not recognized”. Pierwszy krok?
  - A) reinstalacja Windows
  - B) nowe okno terminala
  - C) usunąć Mentora
  - D) zainstalować Pythona
- PyCharm w 2026 r.:
  - A) jest tylko płatny
  - B) ma darmowe funkcje podstawowe, Pro w subskrypcji
  - C) nie obsługuje Pythona
  - D) wymaga Linuksa

Odpowiedzi: B, B, B, B
