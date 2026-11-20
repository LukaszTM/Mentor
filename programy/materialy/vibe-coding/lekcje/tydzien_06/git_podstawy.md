# Git: zapisujesz wersje i cofasz się w czasie
Tydzień 6 · lekcja 19 z 48 · ≈ 50 min

**Po tej lekcji potrafisz:** instalujesz Git, zakładasz repozytorium w PRACA, zapisujesz wersje (add + commit), oglądasz historię (log) i zmiany (diff) oraz cofasz niechciane zmiany (restore).

**Po co mi to?** Git to trwała historia projektu i główna siatka bezpieczeństwa przy pracy z agentem — checkpointy agenta znikają, commity zostają.

## Czego potrzebujesz
- Windows 10/11, ok. 300 MB miejsca.
- Terminal Mentora (CMD) albo PowerShell.
- Lekcja „Sesja z agentem”.

## 1 · Wyjaśnienie od podstaw
### Pojęcia w 5 zdaniach
Repozytorium (repo) to folder projektu z ukrytym podfolderem `.git`, w którym Git trzyma historię. Commit to zapisana wersja wszystkich plików z opisem i autorem — jak punkt w grze, do którego można wrócić. Zanim zapiszesz commit, wskazujesz, które zmiany do niego wchodzą (`git add` — „poczekalnia”, staging). Gałąź (branch) to osobna linia zmian — w tym kursie pracujesz głównie na `main`. Git działa lokalnie, bez internetu; GitHub (następna lekcja) to kopia repozytorium w sieci.
### Instalacja
Git for Windows ze strony git-scm.com (przycisk Download) albo `winget install --id Git.Git -e --source winget`. Domyślne opcje instalatora są dobre. Nowe okno terminala → `git --version`. Raz na komputerze ustaw podpis: `git config --global user.name "Imię Nazwisko"` i `git config --global user.email "adres@…"` (adres będzie widoczny w historii publicznych repozytoriów — GitHub oferuje adres zastępczy typu noreply).
### Siedem poleceń na co dzień
| polecenie | co robi |
|---|---|
| `git init` | zakłada repozytorium w bieżącym folderze (raz) |
| `git status` | co się zmieniło, co jest w poczekalni — używaj CIĄGLE |
| `git add plik.py` / `git add .` | dodaje zmiany do poczekalni (kropka = wszystko, uważaj!) |
| `git commit -m "opis"` | zapisuje wersję z opisem |
| `git log --oneline` | historia: jedna linia na commit |
| `git diff` | co zmieniło się od ostatniego commita (linie - usunięte, + dodane) |
| `git restore plik.py` | cofa NIEZAPISANE zmiany w pliku do ostatniego commita (nieodwracalne!) |
### .gitignore — czego nie zapisywać
Plik `.gitignore` w korzeniu repozytorium wymienia, czego Git ma nie śledzić: `.venv/`, `__pycache__/`, `.env` (tajemnice!), pliki tymczasowe. Dodaj go PRZED pierwszym `git add .`.
### Dobry opis commita
Krótko, w trybie rozkazującym, co zmienia: „Dodaj walidację telefonu z +48”, „Popraw rabat od 7 nocy (>= zamiast >)”. Zły: „zmiany”, „fix”, „asdf”. Agenci piszą dobre opisy, jeśli o to poprosisz — ale czytasz je przed zatwierdzeniem.
### Rytm pracy z agentem
Zielony test → `git status` → `git diff` (przegląd) → `git add` wybranych plików → `git commit -m`. Agent może robić commity za Ciebie (prosi o zgodę na komendę) — w kursie robisz je sam, dopóki nie czytasz diffów płynnie.
### Cofanie — trzy sytuacje
- Zmiana niezapisana, chcesz ją wyrzucić: `git restore plik.py`.
- Dodałeś do poczekalni za dużo: `git restore --staged plik.py` (zmiana zostaje w pliku, wypada z poczekalni).
- Ostatni commit był zły: `git revert HEAD` tworzy NOWY commit odwracający poprzedni — bezpieczne, historia zostaje. Komend `git reset --hard` i `git push --force` w kursie nie używasz (tryb auto Claude Code też je blokuje).

## 2 · Demonstracja — krok po kroku
**Repozytorium w PRACA i ratunek po złej zmianie**

```
C:\...\PRACA>git init
Initialized empty Git repository in C:/.../PRACA/.git/

C:\...\PRACA>git status
On branch main
Untracked files:
  .gitignore
  kalkulator_pobytu.py
  ...

C:\...\PRACA>git add .gitignore kalkulator_pobytu.py
C:\...\PRACA>git commit -m "Dodaj kalkulator pobytu z rabatem od 7 nocy"
[main (root-commit) 3f2a1c9] Dodaj kalkulator pobytu z rabatem od 7 nocy
 2 files changed, 24 insertions(+)

C:\...\PRACA>git log --oneline
3f2a1c9 (HEAD -> main) Dodaj kalkulator pobytu z rabatem od 7 nocy
```

1. Terminal Mentora w PRACA: `git --version` (jest), `git init`. Utwórz .gitignore z liniami `.venv/`, `__pycache__/`, `.env`, `*.tmp`.
2. `git status` — lista nieśledzonych plików. Commit 1: `git add .gitignore` + `git commit -m "Dodaj .gitignore"`.
3. Commit 2: `git add kalkulator_pobytu.py lista_gosci.py` + opis. Commit 3: pozostałe pliki zadań z tygodni 1–3 (sprawdź status, czy nie ma tam niczego prywatnego).
4. Symulacja błędu: w rabaty.py zmień 150 na 15 i zapisz. „✔ Sprawdź wynik” — czerwone.
5. `git diff` pokazuje: `-    return 150 if …` / `+    return 15 if …`. `git restore rabaty.py` → plik wraca, test zielony.
6. `git log --oneline` — 3 commity. To jest Twoja historia; agent może zepsuć pliki, ale nie historię.

✔ **Oczekiwany wynik:** Repozytorium z 3 commitami i .gitignore; zła zmiana znaleziona przez diff i cofnięta restore w 10 sekund.

## 3 · Jak to uruchomić
1. `winget install --id Git.Git -e --source winget` albo instalator z git-scm.com → nowe okno → `git --version`.
2. W PRACA: `git init`, potem rytm status → diff → add → commit.

## W praktyce
- Commit po każdym zielonym kroku.
- Przed każdą sesją agenta: git status czysty.

## 4 · Ćwiczenie prowadzone
Uporządkuj polecenia pierwszego zapisu wersji: A) `git commit -m "Dodaj kalkulator"`, B) `git init`, C) `git add kalkulator_pobytu.py`, D) `git status`. Podaj kolejność liter. Które polecenie cofa niezapisane zmiany w pliku (bez commita)? Czas: 15 minut.

📄 `cwiczenia/tydzien_06/git_podstawy_1.md` · rozwiązanie: `rozwiazania/tydzien_06/git_podstawy_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Które pliki NIE powinny trafić do repozytorium? (1) rabaty.py (2) .env z kluczem API (3) folder .venv (4) AGENTS.md (5) __pycache__. Podaj numery rosnąco jako ciąg cyfr. Który opis commita jest najlepszy: (A) „zmiany” (B) „Popraw rabat: >= 7 nocy zamiast > 7” (C) „fix fix fix”? Czas: 15 minut.

📄 `cwiczenia/tydzien_06/git_podstawy_2.md` · rozwiązanie: `rozwiazania/tydzien_06/git_podstawy_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **„Author identity unknown — Please tell me who you are”.**
  - Przyczyna: Brak git config user.name / user.email.
  - Jak sprawdzić: `git config --global --list`.
  - Poprawka: Ustaw oba: git config --global user.name "…" i user.email "…".
- ✘ **„fatal: not a git repository”.**
  - Przyczyna: Terminal nie jest w folderze z repozytorium.
  - Jak sprawdzić: `cd` — gdzie jesteś? Czy jest folder .git (dir /a)?
  - Poprawka: Przejdź do PRACA albo zrób git init.
- ✘ **Do repozytorium trafił .env albo .venv.**
  - Przyczyna: `git add .` przed utworzeniem .gitignore.
  - Jak sprawdzić: `git status`, `git log --stat`.
  - Poprawka: `git rm --cached .env`, dopisz do .gitignore, commit; jeśli klucz trafił do GitHuba — UNIEWAŻNIJ klucz u dostawcy (historia go pamięta).

## Pułapki
- `git restore` i usunięcie niezapisanych zmian są nieodwracalne — najpierw `git diff`, żeby wiedzieć, co tracisz.
- `git add .` dodaje wszystko, także pliki, których nie chcesz. Na początku dodawaj pliki po nazwie.

## Dodatkowe zadania
1. Załóż repozytorium w PRACA z .gitignore i 3 commitami (zadanie tygodnia).
2. Przećwicz diff + restore na celowo złej zmianie.
3. Napisz 3 opisy commitów według zasady „co i dlaczego”.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Czym jest commit?**
  - Zapisaną wersją plików z opisem i autorem, do której można wrócić.
- **Po co .gitignore?**
  - Żeby Git nie śledził tajemnic (.env) i plików generowanych (.venv, __pycache__).
- **Jak bezpiecznie odwrócić zły commit?**
  - git revert HEAD — nowy commit odwracający zmiany, historia zostaje.

## Co potrafię teraz bez patrzenia na przykład?
Instalujesz Git, zakładasz repozytorium, zapisujesz wersje z dobrymi opisami, czytasz historię i diff, cofasz restore i revert, chronisz tajemnice .gitignore.

## Źródła (data dostępu w nawiasie)
Narzędzia, ceny i przepisy zmieniają się — przed użyciem w pracy otwórz źródło.
- Pro Git (książka, wyd. 2, git-scm.com) — rozdz. 2: Podstawy Gita; dostępne tłumaczenie na polski (dostęp 19.11.2026) — <https://git-scm.com/book/pl/v2>
- Git for Windows — pobieranie (git-scm.com) (dostęp 19.11.2026) — <https://git-scm.com/downloads/win>
- GitHub Docs — Ignoring files (.gitignore) (dostęp 19.11.2026) — <https://docs.github.com/en/get-started/git-basics/ignoring-files>
- Git — dokumentacja polecenia git restore (dostęp 19.11.2026) — <https://git-scm.com/docs/git-restore>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Polecenie pokazujące, co się zmieniło i co jest w poczekalni:
  - A) git log
  - B) git status
  - C) git init
  - D) git push
- W `git diff` linie zaczynające się od + to:
  - A) Usunięte
  - B) Dodane
  - C) Komentarze
  - D) Błędy
- Plik .env z kluczem API:
  - A) Commitujesz
  - B) Dodajesz do .gitignore
  - C) Wysyłasz agentowi
  - D) Wklejasz do README
- Bezpieczne odwrócenie ostatniego commita:
  - A) git reset --hard
  - B) git revert HEAD
  - C) git push --force
  - D) Usunięcie folderu .git

Odpowiedzi: B, B, B, B
