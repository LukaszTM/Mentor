# Instalacja Claude Code w Windows i pierwsze uruchomienie
Tydzień 4 · lekcja 14 z 48 · ≈ 50 min

**Po tej lekcji potrafisz:** masz zainstalowany Claude Code, sprawdzasz go `claude --version` i `claude doctor`, logujesz się i uruchamiasz pierwszą sesję w katalogu PRACA — albo wiesz, jak naprawić najczęstsze błędy instalacji.

**Po co mi to?** Agent musi działać w Twoim katalogu projektu. Instalacja z oficjalnego adresu i sprawdzenie wersji to też pierwsza lekcja bezpieczeństwa.

## Czego potrzebujesz
- Windows 10 w wersji 1809 lub nowszej (albo Windows 11), 4 GB RAM, internet.
- Plan Claude Pro lub wyższy (do logowania; samą instalację możesz zrobić bez planu).
- Lekcja „Terminal bez strachu”.

## 1 · Wyjaśnienie od podstaw
### Trzy sposoby instalacji (wybierz jeden)
| sposób | gdzie wpisujesz | polecenie |
|---|---|---|
| PowerShell (zalecany) | Windows PowerShell — zachęta `PS C:\…>` | `irm https://claude.ai/install.ps1 \| iex` |
| CMD | Wiersz polecenia (np. terminal Mentora) | `curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd` |
| WinGet | PowerShell lub CMD | `winget install Anthropic.ClaudeCode` (bez automatycznych aktualizacji) |
Uprawnienia administratora NIE są potrzebne. Instalator nie pokazuje paska postępu — poczekaj, aż wróci zachęta. Dokumentacja: w PowerShell błąd „The token '&&' is not a valid statement separator” znaczy, że wkleiłeś komendę CMD; „'irm' is not recognized” — że jesteś w CMD.
### Sprawdzenie
Zamknij i otwórz NOWE okno terminala (nowe okno wczytuje zaktualizowaną ścieżkę PATH). Wpisz `claude --version` — zobaczysz numer wersji i „(Claude Code)”. `claude doctor` sprawdza instalację i ustawienia (tylko odczyt, niczego nie zmienia).
### Najczęstsze problemy (z dokumentacji)
- „'claude' is not recognized…” — folder `%USERPROFILE%\.local\bin` nie jest w PATH. Dokumentacja podaje dwie linie PowerShell dopisujące go do PATH użytkownika (są w sekcji Typowe błędy). Potem nowe okno.
- Błędy SSL/TLS na starszym Windows 10 — w PowerShell najpierw `[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12`, potem instalacja.
- Komunikat o architekturze 32-bit — otworzyłeś „Windows PowerShell (x86)”; użyj zwykłego PowerShell.
### Git for Windows — opcjonalny teraz, potrzebny w tygodniu 6
Claude Code działa bez Gita (używa wtedy PowerShell jako narzędzia powłoki). Z zainstalowanym Git for Windows może używać Git Bash. W tygodniu 6 i tak zainstalujesz Gita.
### Pierwsze uruchomienie
- Mentor → Mój projekt → „Otwórz Claude Code tutaj” (uruchamia `claude` w PRACA). Albo terminal Mentora → `claude`.
- Przy pierwszym starcie: wybór motywu i logowanie w przeglądarce (konto z planem Pro/Max albo konto Console).
- Claude Code zapyta, czy ufasz temu folderowi — potwierdzasz tylko dla katalogu PRACA, nie dla całego dysku ani folderu Użytkownika.
- `/help` — lista poleceń; Esc — przerwanie pracy agenta; `exit` albo dwa razy Ctrl + D — wyjście.
### Bez terminala?
Claude Code jest też w aplikacji desktop Claude, w rozszerzeniu VS Code i w przeglądarce (claude.ai/code). Kurs uczy terminala, bo tam najlepiej widać, co agent robi — ale umiejętności są te same.
### Na natywnym Windows nie ma piaskownicy
Dokumentacja: izolacja (sandboxing) komend nie jest obsługiwana na natywnym Windows (działa w WSL2). Dlatego tryby uprawnień i Twoja kontrola zmian są tu jeszcze ważniejsze (tydzień 5).

## 2 · Demonstracja — krok po kroku
**Instalacja i pierwsza sesja w PRACA**

```
PS C:\Users\Anna> irm https://claude.ai/install.ps1 | iex
... (instalacja, kilka minut bez paska postępu)
PS C:\Users\Anna> exit

(nowe okno)
PS C:\Users\Anna> claude --version
2.1.290 (Claude Code)
PS C:\Users\Anna> claude doctor
(raport: wersja, metoda instalacji, ustawienia — bez błędów)
```

1. Win + X → „Terminal” (albo „Windows PowerShell”). Zachęta zaczyna się od PS. Wklej komendę z adresem https://claude.ai/install.ps1 — dokładnie z dokumentacji, nie z forum.
2. Poczekaj na powrót zachęty. Zamknij okno, otwórz nowe, `claude --version` — numer wersji. `claude doctor` — bez czerwonych pozycji.
3. Mentor → Środowisko → „🔍 Sprawdź ponownie”: narzędzie „claude” ma zielony znacznik.
4. Mój projekt → „Otwórz Claude Code tutaj”. Zaloguj się w przeglądarce. Na pytanie o zaufanie folderowi sprawdź ścieżkę — ma kończyć się na \PRACA.
5. Pierwsza prośba (tylko odczyt): „Wypisz pliki w tym katalogu i w jednym zdaniu powiedz, co robi kalkulator_pobytu.py. Niczego nie zmieniaj.” Agent czyta pliki bez pytania o zgodę (odczyt w katalogu roboczym nie wymaga zgody) i odpowiada.
6. Wyjdź: `exit`. Zapisz w instalacja.txt wynik `claude --version` (zadanie tygodnia).

✔ **Oczekiwany wynik:** Działający Claude Code w PRACA, potwierdzony wersją i claude doctor; pierwsza sesja tylko do odczytu.

## 3 · Jak to uruchomić
1. PowerShell → `irm https://claude.ai/install.ps1 | iex` → nowe okno → `claude --version`.
2. Mentor → Mój projekt → „Otwórz Claude Code tutaj”.

## W praktyce
- Raz w miesiącu `claude doctor`.
- Wersję narzędzia zapisuj w README projektu przy zgłaszaniu błędów.

## 4 · Ćwiczenie prowadzone
Masz okno z zachętą `PS C:\Users\Anna>`. (1) Którą komendę instalacji wkleisz: ps1 czy cmd? (2) Po instalacji `claude --version` daje „'claude' is not recognized”. Co robisz NAJPIERW: nowe okno czy reinstalacja? (3) Jakim poleceniem sprawdzisz instalację bez zmieniania czegokolwiek? Czas: 15 minut.

📄 `cwiczenia/tydzien_04/instalacja_claude_code_1.md` · rozwiązanie: `rozwiazania/tydzien_04/instalacja_claude_code_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Claude Code przy pierwszym uruchomieniu pyta, czy ufasz folderowi. Ścieżka to (A) `C:\Users\Anna`, (B) `C:\Users\Anna\Documents\Mentor\vibe-coding\PRACA`, (C) `C:\`. Który potwierdzisz? Druga sprawa: czy na natywnym Windows Claude Code izoluje komendy w piaskownicy (tak/nie)? Czas: 15 minut.

📄 `cwiczenia/tydzien_04/instalacja_claude_code_2.md` · rozwiązanie: `rozwiazania/tydzien_04/instalacja_claude_code_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **„'claude' is not recognized as an internal or external command” w nowym oknie.**
  - Przyczyna: Folder %USERPROFILE%\.local\bin nie trafił do PATH.
  - Jak sprawdzić: `claude doctor` nie działa; sprawdź, czy istnieje plik %USERPROFILE%\.local\bin\claude.exe.
  - Poprawka: PowerShell: `$currentPath = [Environment]::GetEnvironmentVariable('PATH', 'User')` i `[Environment]::SetEnvironmentVariable('PATH', "$currentPath;$env:USERPROFILE\.local\bin", 'User')`, potem nowe okno (polecenia z dokumentacji).
- ✘ **„The token '&&' is not a valid statement separator”.**
  - Przyczyna: Komenda CMD wklejona do PowerShell.
  - Jak sprawdzić: Zachęta zaczyna się od PS?
  - Poprawka: Użyj wersji irm … install.ps1 | iex albo otwórz CMD.
- ✘ **Błąd SSL/TLS przy pobieraniu.**
  - Przyczyna: Starszy Windows 10 bez TLS 1.2 domyślnie.
  - Jak sprawdzić: Wersja Windows (winver).
  - Poprawka: W PowerShell: `[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12`, potem instalacja.

## Pułapki
- Instaluj wyłącznie z adresu claude.ai/install… lub przez winget z identyfikatorem Anthropic.ClaudeCode. Strony „Claude Code za darmo” i paczki o podobnych nazwach to częsta pułapka.
- Nie uruchamiaj Claude Code w C:\ ani w folderze użytkownika — agent widzi wtedy wszystkie Twoje pliki.

## Dodatkowe zadania
1. Zainstaluj Claude Code i zapisz wynik `claude --version` w instalacja.txt.
2. Uruchom `claude doctor` i przeczytaj raport.
3. Pierwsza sesja tylko do odczytu w PRACA.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Jak sprawdzisz, że instalacja się udała?**
  - Nowe okno → `claude --version` (numer wersji) i `claude doctor`.
- **Dlaczego otwierasz nowe okno po instalacji?**
  - Stare okno ma starą wartość PATH i nie widzi programu.
- **Jakiemu folderowi ufasz przy pierwszym uruchomieniu?**
  - Tylko katalogowi projektu (PRACA).

## Co potrafię teraz bez patrzenia na przykład?
Instalujesz Claude Code z oficjalnego adresu, sprawdzasz wersję i claude doctor, naprawiasz PATH i TLS, uruchamiasz pierwszą sesję tylko w PRACA.

## Źródła (data dostępu w nawiasie)
Narzędzia, ceny i przepisy zmieniają się — przed użyciem w pracy otwórz źródło.
- Claude Code — Set up Claude Code (instalacja, wymagania, Windows) (dostęp 19.11.2026) — <https://code.claude.com/docs/en/setup>
- Claude Code — Terminal guide for new users (dostęp 19.11.2026) — <https://code.claude.com/docs/en/terminal-guide>
- Claude Help Center — Using Claude Code with your Pro or Max plan (dostęp 19.11.2026) — <https://support.claude.com/en/articles/14552983>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Zalecana komenda instalacji w PowerShell:
  - A) pip install claude
  - B) irm https://claude.ai/install.ps1 | iex
  - C) npm i claude-free
  - D) winget install claude-pl
- Czy instalacja Claude Code wymaga uprawnień administratora?
  - A) Tak
  - B) Nie
  - C) Tylko na Windows 11
  - D) Tylko przez WinGet
- Polecenie wyjścia z sesji Claude Code:
  - A) exit
  - B) quit!
  - C) Alt + F4 zawsze
  - D) logout
- „'irm' is not recognized” znaczy:
  - A) Brak internetu
  - B) Jesteś w CMD, a komenda jest dla PowerShell
  - C) Zły plan
  - D) Za stary Python

Odpowiedzi: B, B, A, B
