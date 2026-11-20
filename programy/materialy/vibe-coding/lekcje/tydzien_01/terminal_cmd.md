# Terminal bez strachu: CMD i PowerShell
Tydzień 1 · lekcja 4 z 48 · ≈ 50 min

**Po tej lekcji potrafisz:** otwierasz terminal w katalogu projektu, poruszasz się po folderach (cd, dir), tworzysz foldery i pliki, odróżniasz CMD od PowerShell i bezpiecznie przerywasz komendę.

**Po co mi to?** Agenci kodujący (Claude Code, Codex) działają w terminalu i wykonują w nim komendy — musisz rozumieć, co tam się dzieje, zanim cokolwiek zaakceptujesz.

## Czego potrzebujesz
- Mentor → Mój projekt → „⌨ Otwórz terminal tutaj” (otwiera CMD w katalogu PRACA ze środowiskiem Pythona kursu).
- Lekcja „Pliki, foldery, rozszerzenia i ścieżki”.

## 1 · Wyjaśnienie od podstaw
### Terminal to rozmowa z komputerem tekstem
Zamiast klikać, wpisujesz polecenie i naciskasz Enter. Terminal pokazuje znak zachęty (prompt) — miejsce, w którym czeka na polecenie. Windows ma dwa terminale: CMD (Wiersz polecenia) i PowerShell. Rozpoznasz je po zachęcie:
| terminal | zachęta wygląda tak | gdzie go spotkasz |
|---|---|---|
| CMD | `C:\Users\Anna\Documents\Mentor\vibe-coding\PRACA>` | przycisk Mentora „Otwórz terminal tutaj”, „Otwórz Claude Code tutaj” |
| PowerShell | `PS C:\Users\Anna>` (z literami PS na początku) | Win + X → Terminal / Windows PowerShell — tu instalujesz Claude Code i Codex |
Komendy instalacyjne z dokumentacji są pisane pod konkretny terminal. Dokumentacja Claude Code podaje dwie wskazówki: błąd „The token '&&' is not a valid statement separator” oznacza, że jesteś w PowerShell, a „'irm' is not recognized” — że jesteś w CMD.
### Komendy, których potrzebujesz (CMD)
| komenda | co robi | przykład |
|---|---|---|
| `cd` | pokazuje bieżący folder (bez argumentu) albo przechodzi do folderu | `cd dane` · `cd ..` (piętro wyżej) |
| `dir` | lista plików i folderów | `dir` · `dir *.py` (tylko pliki .py) |
| `mkdir` | tworzy folder | `mkdir notatki` |
| `type` | wyświetla zawartość pliku tekstowego | `type dziennik.md` |
| `cls` | czyści ekran | `cls` |
| `python plik.py` | uruchamia program w Pythonie | `python witaj.py` |
W PowerShell działają też `ls` (lista) i `cat` (zawartość) — to skróty. Agenci często używają ich zamiennie.
### Triki, które oszczędzają czas
- Tab dopełnia nazwę pliku lub folderu: wpisz `cd da` i naciśnij Tab → `cd dane`.
- Strzałka w górę przywołuje poprzednią komendę.
- Ctrl + C przerywa działający program (np. zapętlony). Ctrl + C w terminalu to NIE „kopiuj” — kopiujesz zaznaczając myszą i Enter albo prawym przyciskiem.
- Wklejanie: prawy przycisk myszy albo Ctrl + V (w nowym Terminalu Windows).
- Ścieżkę ze spacją bierz w cudzysłów: `cd "Moje projekty"`.
### Bezpieczeństwo: czytaj, zanim naciśniesz Enter
Terminal wykonuje dokładnie to, co wpiszesz, bez kosza i bez „Cofnij”. Komendy usuwające (`del`, `rmdir /s`, w PowerShell `Remove-Item -Recurse`) usuwają od razu. Gdy agent proponuje komendę, czytasz ją tak jak przelew w banku: co, gdzie, na czym. Jeśli nie rozumiesz komendy — pytasz agenta „wyjaśnij tę komendę i co się stanie”, zanim zatwierdzisz.

## 2 · Demonstracja — krok po kroku
**Pięć komend w katalogu roboczym**

```
Sesja w CMD (to, co wpisujesz, jest po znaku >):

C:\Users\Anna\Documents\Mentor\vibe-coding\PRACA>cd
C:\Users\Anna\Documents\Mentor\vibe-coding\PRACA

C:\Users\Anna\Documents\Mentor\vibe-coding\PRACA>mkdir dane

C:\Users\Anna\Documents\Mentor\vibe-coding\PRACA>cd dane

C:\Users\Anna\Documents\Mentor\vibe-coding\PRACA\dane>cd ..

C:\Users\Anna\Documents\Mentor\vibe-coding\PRACA>dir *.md
 ...
18.11.2026  20:14               142 dziennik.md
               1 plik(ów)            142 bajtów
```

1. Mentor → Mój projekt → „⌨ Otwórz terminal tutaj”. Otwiera się czarne okno CMD; pierwsza linia mówi „Katalog roboczy: …”, druga pokazuje wersję Pythona kursu (albo prośbę o przygotowanie środowiska).
2. Wpisz `cd` i Enter — terminal wypisuje bieżący folder. To ta sama ścieżka, którą widzisz w Mój projekt.
3. Wpisz `mkdir dane` — powstaje folder. `dir` — widzisz go na liście z oznaczeniem <DIR>.
4. `cd dane` → zachęta kończy się na `\dane>`. `cd ..` wraca piętro wyżej. Spróbuj `cd da` + Tab — terminal dopełnia nazwę.
5. `type dziennik.md` (jeśli plik istnieje) wyświetla jego treść. Na koniec `cls` czyści ekran, strzałka w górę przywołuje poprzednie komendy.

✔ **Oczekiwany wynik:** Umiesz sprawdzić, gdzie jesteś, przejść do folderu i z powrotem, utworzyć folder i obejrzeć plik — bez klikania.

## 3 · Jak to uruchomić
1. Mentor → Mój projekt → „⌨ Otwórz terminal tutaj” (CMD w PRACA).
2. PowerShell: Win + X → „Terminal” albo „Windows PowerShell” (zachęta zaczyna się od PS).

## W praktyce
- Zawsze `cd` przed pracą — wiesz, w jakim folderze działa agent.
- Każdą komendę usuwającą czytaj dwa razy.

## 4 · Ćwiczenie prowadzone
Jesteś w `C:\Users\Anna\Documents\Mentor\vibe-coding\PRACA` (CMD). Wpisujesz po kolei: `mkdir raporty`, `cd raporty`, `cd ..`, `cd dane`. W jakim folderze jesteś na końcu (sama nazwa ostatniego folderu)? Jaką komendą wyświetlisz zawartość pliku `goscie.csv` w tym folderze? Którą komendą przerwiesz zawieszony program? Czas: 15 minut.

📄 `cwiczenia/tydzien_01/terminal_cmd_1.md` · rozwiązanie: `rozwiazania/tydzien_01/terminal_cmd_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Dokumentacja podaje dwie komendy instalacyjne Claude Code: dla PowerShell `irm https://claude.ai/install.ps1 | iex` i dla CMD `curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd`. Masz okno z zachętą `C:\Users\Anna>` (bez PS). Którą komendę wkleisz? Jaki błąd zobaczysz, jeśli wkleisz tę drugą? Czas: 15 minut. (Niczego jeszcze nie instaluj — instalacja w tygodniu 4.)

📄 `cwiczenia/tydzien_01/terminal_cmd_2.md` · rozwiązanie: `rozwiazania/tydzien_01/terminal_cmd_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **„'python' is not recognized as an internal or external command”.**
  - Przyczyna: Python nie jest zainstalowany albo terminal nie ma go w PATH.
  - Jak sprawdzić: Mentor → Środowisko → stan Pythona; terminal otwarty z Mentora pokazuje wersję w drugiej linii.
  - Poprawka: Środowisko → „⬇ Zainstaluj brakujące”, potem otwórz terminal przyciskiem Mentora (ustawia Pythona kursu na początku PATH).
- ✘ **„The system cannot find the path specified.” po `cd`.**
  - Przyczyna: Literówka albo folder nie istnieje w bieżącym miejscu.
  - Jak sprawdzić: `dir` — czy folder jest na liście?
  - Poprawka: Użyj Tab do dopełniania nazwy; sprawdź `cd`, gdzie jesteś.
- ✘ **Terminal „wisi” — kursor miga, nic się nie dzieje.**
  - Przyczyna: Program czeka na dane (input) albo zapętlił się.
  - Jak sprawdzić: Czy program prosi o wpisanie czegoś?
  - Poprawka: Wpisz dane i Enter, a jeśli to pętla — Ctrl + C.

## Pułapki
- Ctrl + C w terminalu przerywa program, a nie kopiuje (w nowym Terminalu Windows kopiuje tylko, gdy coś jest zaznaczone).
- Nigdy nie wklejaj do terminala komendy z nieznanej strony bez zrozumienia — zwłaszcza zaczynającej się od `irm … | iex` lub `curl … | bash`: one pobierają i od razu uruchamiają program. Instalujesz tak tylko z oficjalnego adresu producenta.

## Dodatkowe zadania
1. Utwórz komendami foldery `notatki`, `dane`, `raporty` w PRACA i sprawdź `dir`.
2. Otwórz PowerShell i CMD obok siebie — zapisz w dzienniku, po czym je rozpoznajesz.
3. Przećwicz Tab i strzałkę w górę na 5 komendach.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Po czym poznasz, że jesteś w PowerShell?**
  - Zachęta zaczyna się od liter PS, np. `PS C:\Users\Anna>`.
- **Jak przejdziesz o jeden folder wyżej?**
  - `cd ..`
- **Co zrobisz, zanim zatwierdzisz komendę zaproponowaną przez agenta?**
  - Przeczytam ją i — jeśli jej nie rozumiem — poproszę agenta o wyjaśnienie, co zrobi i na jakich plikach.

## Co potrafię teraz bez patrzenia na przykład?
Otwierasz terminal w PRACA, poruszasz się cd/dir, tworzysz foldery, czytasz pliki type, odróżniasz CMD od PowerShell i przerywasz program Ctrl + C.

## Źródła (data dostępu w nawiasie)
Narzędzia, ceny i przepisy zmieniają się — przed użyciem w pracy otwórz źródło.
- Claude Code — przewodnik po terminalu dla nowych użytkowników (oficjalna dokumentacja) (dostęp 19.11.2026) — <https://code.claude.com/docs/en/terminal-guide>
- Claude Code — instalacja i wymagania systemowe (oficjalna dokumentacja) (dostęp 19.11.2026) — <https://code.claude.com/docs/en/setup>
- Microsoft Learn — polecenia wiersza poleceń Windows (cd, dir, mkdir, type) (dostęp 19.11.2026) — <https://learn.microsoft.com/windows-server/administration/windows-commands/windows-commands>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Komenda `cd ..` w CMD:
  - A) Usuwa folder
  - B) Przechodzi o jeden folder wyżej
  - C) Pokazuje pliki
  - D) Tworzy folder ..
- Zachęta `PS C:\Users\Anna>` oznacza:
  - A) CMD
  - B) PowerShell
  - C) Python
  - D) Claude Code
- Jak przerwiesz zapętlony program w terminalu?
  - A) Ctrl + C
  - B) Ctrl + S
  - C) Alt + F4 na pulpicie
  - D) Enter
- Co oznacza błąd „'irm' is not recognized…”?
  - A) Brak internetu
  - B) Wkleiłeś komendę PowerShell do CMD
  - C) Brak uprawnień administratora
  - D) Zła wersja Windows

Odpowiedzi: B, B, A, B
