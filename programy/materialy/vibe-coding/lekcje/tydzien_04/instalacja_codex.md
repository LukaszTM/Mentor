# Codex: CLI i aplikacja na Windows, logowanie i tryby pracy
Tydzień 4 · lekcja 15 z 48 · ≈ 50 min

**Po tej lekcji potrafisz:** instalujesz Codex (CLI w PowerShell albo aplikację ChatGPT desktop), logujesz się kontem ChatGPT, rozumiesz piaskownicę workspace-write i wybierasz bezpieczny tryb uprawnień.

**Po co mi to?** Codex to drugi wiodący agent kodujący. Kto zna oba, umie przenieść nawyki między narzędziami — a rynek pracy wymaga elastyczności.

## Czego potrzebujesz
- Windows 10/11, internet.
- Plan ChatGPT Plus lub wyższy dla CLI (Free i Go — ograniczony dostęp tylko w aplikacji, wdrażany stopniowo).
- Lekcja „Instalacja Claude Code” (analogiczne kroki).

## 1 · Wyjaśnienie od podstaw
### Dwie formy Codex
| | Codex CLI (terminal) | Codex w aplikacji ChatGPT desktop |
|---|---|---|
| instalacja | PowerShell: `powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 \| iex"` albo `npm install -g @openai/codex` (wymaga Node.js) | Microsoft Store albo `winget install --id 9PLM9XGG6VKS -s msstore` |
| start | `codex` w katalogu projektu | wybierasz folder projektu w aplikacji |
| izolacja na Windows | natywna piaskownica Windows albo WSL2 | natywna piaskownica Windows albo WSL2 |
Logowanie: „Sign in with ChatGPT” (konta Plus, Pro, Business, Edu, Enterprise) albo klucz API (płatność za tokeny — lekcja o kosztach). Codex CLI jest otwartym oprogramowaniem (licencja Apache-2.0).
### Piaskownica (sandbox) — co agent może dotknąć
| tryb piaskownicy | co wolno |
|---|---|
| read-only | tylko czytać pliki |
| workspace-write | czytać i zmieniać pliki w katalogu projektu; wyjście poza katalog lub internet wymaga zgody |
| danger-full-access | wszystko na komputerze i w sieci — tylko w izolowanych maszynach |
### Tryby uprawnień (aplikacja i CLI)
- „Ask for approval” — pracuje w katalogu projektu, pyta przed wyjściem poza niego i przed dostępem do internetu. Tryb startowy w kursie.
- „Approve for me” — Codex sam ocenia prośby o zgodę (automatyczny przegląd). Wygodniej, mniej kontroli.
- „Full access” — cały komputer i internet bez pytania. W kursie: nigdy.
W CLI tryb zmienisz poleceniem `/permissions`; przy starcie możesz go podać jawnie: `codex --sandbox workspace-write --ask-for-approval on-request`.
### Polecenia w sesji Codex CLI
| polecenie | co robi |
|---|---|
| `/init` | tworzy szkielet pliku AGENTS.md (instrukcje projektu — tydzień 5) |
| `/diff` | pokazuje zmiany w plikach (Git) |
| `/status` | ustawienia sesji, model, tryb zgód, zużycie tokenów |
| `/compact` | streszcza rozmowę, by zwolnić kontekst |
| `/new` | nowa rozmowa bez wychodzenia |
| `/review` | prośba o przegląd zmian w katalogu (ryzyka, brakujące testy) |
| `/model` | zmiana modelu |
### Claude Code i Codex — ta sama praca, inne przyciski
| czynność | Claude Code | Codex |
|---|---|---|
| instrukcje projektu | CLAUDE.md (czyta też AGENTS.md, gdy nie ma CLAUDE.md) | AGENTS.md |
| zmiana trybu zgód | Shift + Tab, `/permissions` (reguły) | `/permissions` |
| limity i zużycie | `/usage`, `/context` | `/status` |
| podsumowanie rozmowy | `/compact` | `/compact` |
| przerwanie | Esc | Esc |
Nazwy modeli zmieniają się często — kurs ich nie wpisuje; sprawdzisz je w `/model`.

## 2 · Demonstracja — krok po kroku
**Codex w trybie „pytaj o zgodę” — pierwsza sesja tylko do odczytu**

```
PS C:\Users\Anna> powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"
(nowe okno)
PS C:\Users\Anna> cd Documents\Mentor\vibe-coding\PRACA
PS C:\...\PRACA> codex --sandbox workspace-write --ask-for-approval on-request
> Sign in with ChatGPT  (przeglądarka)
> Opisz w 2 zdaniach pliki w tym katalogu. Niczego nie zmieniaj.
```

1. PowerShell → komenda instalacyjna z chatgpt.com/codex/install.ps1 (z dokumentacji). Nowe okno → `codex --version`.
2. Przejdź do PRACA (`cd` ze ścieżką z Mój projekt) i uruchom `codex --sandbox workspace-write --ask-for-approval on-request`.
3. Zaloguj się „Sign in with ChatGPT”. Sprawdź `/status`: katalog roboczy to PRACA, tryb zgód on-request.
4. Prośba tylko do odczytu: „Wypisz pliki i powiedz, co robi rabaty.py. Niczego nie zmieniaj.” Odczyt w katalogu nie wymaga zgody.
5. Poproś o coś poza katalogiem, np. „pokaż pliki na Pulpicie” — Codex zapyta o zgodę. Odmów. Tak wygląda granica piaskownicy.
6. Wyjdź (Ctrl + C dwa razy albo /quit). Zapisz `codex --version` w instalacja.txt, jeśli to Twoje narzędzie.

✔ **Oczekiwany wynik:** Działający Codex w PRACA z piaskownicą workspace-write; widziałeś prośbę o zgodę przy wyjściu poza katalog.

## 3 · Jak to uruchomić
1. PowerShell → instalacja → nowe okno → w PRACA: `codex --sandbox workspace-write --ask-for-approval on-request`.
2. Albo: aplikacja ChatGPT desktop → Codex → wybór folderu PRACA → tryb „Ask for approval”.

## W praktyce
- Ustaw tryb jawnie przy starcie — nie licz na domyślny.
- Jedno narzędzie na zadanie; porównuj je na tych samych specyfikacjach.

## 4 · Ćwiczenie prowadzone
Dopasuj tryb piaskownicy do sytuacji: (1) chcesz, żeby agent tylko przeczytał kod i wyjaśnił go, (2) zwykła praca nad zadaniem w PRACA, (3) ktoś radzi „ustaw pełny dostęp, będzie szybciej”. Opcje: read-only, workspace-write, danger-full-access, żaden z nich. Czas: 15 minut.

📄 `cwiczenia/tydzien_04/instalacja_codex_1.md` · rozwiązanie: `rozwiazania/tydzien_04/instalacja_codex_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Przetłumacz polecenia między narzędziami: (1) w Codex chcesz zobaczyć zużycie tokenów — polecenie? (2) w Codex chcesz szkielet pliku instrukcji projektu — polecenie? (3) jak nazywa się plik instrukcji, który czytają OBA narzędzia (Claude Code — gdy nie ma CLAUDE.md)? Czas: 15 minut.

📄 `cwiczenia/tydzien_04/instalacja_codex_2.md` · rozwiązanie: `rozwiazania/tydzien_04/instalacja_codex_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **„running scripts is disabled on this system” przy instalacji.**
  - Przyczyna: Zasady wykonywania skryptów PowerShell.
  - Jak sprawdzić: Czy użyłeś pełnej komendy z -ExecutionPolicy ByPass?
  - Poprawka: Skopiuj komendę z dokumentacji w całości: powershell -ExecutionPolicy ByPass -c "irm … | iex".
- ✘ **`npm` is not recognized.**
  - Przyczyna: Brak Node.js (wariant instalacji przez npm).
  - Jak sprawdzić: `node --version`.
  - Poprawka: Użyj instalatora PowerShell albo zainstaluj Node.js LTS z nodejs.org.
- ✘ **Codex po zalogowaniu nie daje dostępu w CLI.**
  - Przyczyna: Plan Free/Go — CLI wymaga Plus lub wyższego.
  - Jak sprawdzić: Ustawienia konta ChatGPT → plan.
  - Poprawka: Plus albo aplikacja desktop (ograniczony dostęp) albo ścieżka bez konta.

## Pułapki
- „Approve for me” jest wygodne, ale to model ocenia zgody za Ciebie. W kursie zaczynasz od „Ask for approval” i zmieniasz świadomie.
- Klucz API wklejony do logowania to płatność za tokeny — trzymaj go z dala od plików projektu (tydzień 11).

## Dodatkowe zadania
1. Zainstaluj Codex (jeśli to Twoje narzędzie) i zapisz `codex --version`.
2. Pierwsza sesja tylko do odczytu w trybie on-request.
3. Przetestuj granicę: prośba o plik spoza PRACA → odmów zgody.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Co oznacza workspace-write?**
  - Agent czyta i zmienia pliki w katalogu projektu; wyjście poza niego i internet wymagają zgody.
- **Którego trybu nie używasz na swoim komputerze?**
  - Full access / danger-full-access.
- **Jak sprawdzisz zużycie tokenów w Codex?**
  - /status.

## Co potrafię teraz bez patrzenia na przykład?
Instalujesz Codex CLI albo aplikację, logujesz się ChatGPT, pracujesz w piaskownicy workspace-write z trybem „pytaj o zgodę” i znasz odpowiedniki poleceń z Claude Code.

## Źródła (data dostępu w nawiasie)
Narzędzia, ceny i przepisy zmieniają się — przed użyciem w pracy otwórz źródło.
- OpenAI Codex CLI — README (instalacja, logowanie, licencja Apache-2.0) (dostęp 19.11.2026) — <https://cdn.jsdelivr.net/gh/openai/codex@main/README.md>
- Codex — aplikacja na Windows (ChatGPT desktop, sandbox Windows, WSL2) (dostęp 19.11.2026) — <https://learn.chatgpt.com/docs/app/windows>
- Codex — Permission modes (Ask for approval, Approve for me, Full access) (dostęp 19.11.2026) — <https://learn.chatgpt.com/docs/permission-modes>
- Codex — Sandboxing (read-only, workspace-write, danger-full-access) (dostęp 19.11.2026) — <https://learn.chatgpt.com/docs/sandboxing?surface=cli>
- Codex CLI — slash commands (/init, /diff, /status, /compact, /new, /review, /permissions) (dostęp 20.11.2026) — <https://developers.openai.com/codex/cli/slash-commands>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Codex CLI w PowerShell instalujesz:
  - A) pip install codex
  - B) powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"
  - C) winget install codex-free
  - D) Ze strony z torrentami
- Tryb piaskownicy do zwykłej pracy w projekcie:
  - A) read-only
  - B) workspace-write
  - C) danger-full-access
  - D) brak
- Plik instrukcji projektu dla Codex:
  - A) README.txt
  - B) AGENTS.md
  - C) codex.ini
  - D) CLAUDE.md wyłącznie
- Polecenie Codex pokazujące zmiany w plikach:
  - A) /diff
  - B) /show
  - C) /git
  - D) /changes

Odpowiedzi: B, B, B, A
