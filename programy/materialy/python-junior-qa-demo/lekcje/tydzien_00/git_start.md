# Git i GitHub — pierwszy commit i push
Tydzień 0 · lekcja 4 z 16 · ≈ 45 min

**Po tej lekcji potrafisz:** tworzysz repozytorium Git, zapisujesz zmiany commitem (add → commit), czytasz git status i git log oraz wysyłasz projekt na GitHub (remote, push).

**Po co mi to?** Każdy zespół trzyma kod w Gicie, a rekruter ogląda Twój GitHub zanim zaprosi na rozmowę. Historia commitów pokazuje, jak pracujesz.

## Czego potrzebujesz
- Git for Windows (lekcja „Narzędzia”).
- Darmowe konto na github.com (e-mail, hasło, nazwa użytkownika; włącz weryfikację dwuetapową).
- Katalog PRACA z plikiem hello.py.

## 1 · Wyjaśnienie od podstaw
### Repozytorium i commit
**Repozytorium** to katalog, w którym Git pamięta historię. **Commit** to zapisany punkt historii: zestaw zmian + opis + autor + data — jak zapis gry, do którego zawsze możesz wrócić.
### Trzy miejsca
1. katalog roboczy — pliki, które edytujesz; 2. **poczekalnia** (staging) — zmiany wybrane do commita (`git add`); 3. historia — commity (`git commit`).
### Pierwsza konfiguracja (raz na komputer)
`git config --global user.name "Anna Nowak"` i `git config --global user.email "anna@example.com"` — te dane będą w każdym commicie. Na GitHubie możesz użyć adresu prywatności `…@users.noreply.github.com`.
### Codzienny cykl
| polecenie | co robi |
|---|---|
| `git init` | zamienia katalog w repozytorium (raz) |
| `git status` | co się zmieniło, co jest w poczekalni |
| `git add hello.py` | dodaje plik do poczekalni (`git add .` — wszystkie) |
| `git commit -m "Dodaj hello.py"` | zapisuje commit z opisem |
| `git log --oneline` | historia w skrócie |
Opis commita: tryb rozkazujący, co zmienia — „Dodaj kalkulator”, „Popraw dzielenie przez zero”.
### GitHub — kopia w internecie
1. github.com → New repository → nazwa `nauka-python`, Public, BEZ README (repo puste). 2. W PRACA: `git remote add origin https://github.com/TWOJA-NAZWA/nauka-python.git` — `origin` to skrót adresu. 3. `git branch -M main` — główna gałąź nazywa się main. 4. `git push -u origin main` — wysyła commity. Przy pierwszym push okno logowania (Git Credential Manager) otworzy przeglądarkę — logujesz się do GitHuba, hasło nie trafia do terminala.
### Czego NIE commitować
Haseł, tokenów, plików .env, katalogu .venv. Od tygodnia 5 pilnuje tego plik `.gitignore`.

## 2 · Demonstracja — krok po kroku
**Pierwszy commit i wysłanie na GitHub**

```
PS C:\Users\Ania\Documents\PRACA> git init
Initialized empty Git repository in C:/Users/Ania/Documents/PRACA/.git/
PS …\PRACA> git status
Untracked files:
  hello.py
PS …\PRACA> git add hello.py
PS …\PRACA> git commit -m "Dodaj pierwszy program hello.py"
[master (root-commit) 3f2a1c9] Dodaj pierwszy program hello.py
 1 file changed, 6 insertions(+)
PS …\PRACA> git branch -M main
PS …\PRACA> git remote add origin https://github.com/anna-nowak/nauka-python.git
PS …\PRACA> git push -u origin main
To https://github.com/anna-nowak/nauka-python.git
 * [new branch]      main -> main
```

1. `git init` — w katalogu PRACA powstaje ukryty folder .git (tam jest cała historia). Nie usuwaj go.
2. `git status` — hello.py jest „Untracked”: Git go widzi, ale jeszcze nie śledzi.
3. `git add hello.py` — plik trafia do poczekalni. `git status` pokaże go teraz na zielono w „Changes to be committed”.
4. `git commit -m "…"` — zapis w historii. 3f2a1c9 to początek identyfikatora commita (skrót SHA).
5. `git branch -M main` — zmiana nazwy gałęzi na main (GitHub używa tej nazwy domyślnie).
6. `git remote add origin <adres>` — zapamiętanie adresu repozytorium na GitHubie pod nazwą origin.
7. `git push -u origin main` — wysłanie commitów; `-u` zapamiętuje, że main wysyłasz do origin (później wystarczy `git push`).
8. Odśwież stronę repozytorium na GitHubie — widzisz hello.py i opis commita.

✔ **Oczekiwany wynik:** Na GitHubie repozytorium nauka-python z plikiem hello.py i jednym commitem.

## 3 · Jak to uruchomić
1. Terminal (PowerShell albo terminal Mentora) w katalogu PRACA → polecenia z ramki po kolei.
2. Po każdym poleceniu `git status` — to najlepszy sposób, żeby wiedzieć, co się stało.

## W praktyce
- Commit po każdym działającym kroku, push na koniec dnia.
- git status przed każdym commitem.

## 4 · Ćwiczenie prowadzone
Ułóż w kolejności (wpisz numery po przecinku): 1 `git commit -m "Dodaj kalkulator"`, 2 `git add kalkulator.py`, 3 `git push`, 4 `git status`. Zaczynasz od sprawdzenia stanu. Czas: 10 minut.

📄 `cwiczenia/tydzien_00/git_start_1.md` · rozwiązanie: `rozwiazania/tydzien_00/git_start_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Co się stanie? (1) Zmieniasz hello.py i od razu robisz `git commit -m "Zmiana"` bez `git add`; (2) robisz commit, ale nie push — czy zmiana jest na GitHubie?; (3) commitujesz plik haslo.txt z hasłem i potem go usuwasz nowym commitem — czy hasło zniknęło z historii? Opcje dla każdego: tak / nie. (1) Czy zmiana trafi do commita? Czas: 15 minut.

📄 `cwiczenia/tydzien_00/git_start_2.md` · rozwiązanie: `rozwiazania/tydzien_00/git_start_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **Author identity unknown *** Please tell me who you are.**
  - Przyczyna: Brak user.name / user.email.
  - Jak sprawdzić: `git config --global --list`.
  - Poprawka: `git config --global user.name "…"` i `user.email "…"`.
- ✘ **fatal: not a git repository (or any of the parent directories): .git**
  - Przyczyna: Polecenie wpisane poza repozytorium.
  - Jak sprawdzić: `pwd` — czy jesteś w PRACA?
  - Poprawka: `cd` do katalogu projektu albo `git init`.
- ✘ **! [rejected] main -> main (fetch first)**
  - Przyczyna: Na GitHubie są commity, których nie masz (np. repo założone z README).
  - Jak sprawdzić: Strona repozytorium — czy jest README?
  - Poprawka: `git pull --rebase origin main`, potem `git push`. Na przyszłość zakładaj puste repozytorium.

## Pułapki
- Commit „wszystkiego” z opisem „zmiany” — po tygodniu nie wiesz, co zmieniłeś. Mały commit = jedna rzecz.
- Hasło lub token w repozytorium publicznym — boty skanują GitHub w ciągu minut.

## Dodatkowe zadania
1. Skonfiguruj user.name i user.email.
2. Utwórz repozytorium w PRACA, zrób commit z hello.py.
3. Wyślij na GitHub i sprawdź stronę repozytorium.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Co robi git add?**
  - Dodaje zmiany do poczekalni — wybiera, co trafi do commita.
- **Różnica między commit a push?**
  - Commit zapisuje lokalnie; push wysyła commity na serwer (GitHub).
- **Czy usunięcie pliku z hasłem nowym commitem usuwa hasło z historii?**
  - Nie — trzeba zmienić hasło.

## Co potrafię teraz bez patrzenia na przykład?
Tworzysz repozytorium, zapisujesz commity (status → add → commit), czytasz historię i wysyłasz projekt na GitHub.

## Źródła (data dostępu w nawiasie)
Wersje narzędzi i dane rynkowe zmieniają się — przed użyciem w pracy otwórz źródło.
- Pro Git (wydanie 2, wersja polska) — Scott Chacon, Ben Straub (dostęp 23.11.2026) — <https://git-scm.com/book/pl/v2>
- Pro Git PL — Podstawy Gita (rejestrowanie zmian, historia, cofanie) (dostęp 23.11.2026) — <https://git-scm.com/book/pl/v2/Podstawy-Gita-Rejestrowanie-zmian-w-repozytorium>
- GitHub Docs — About READMEs (dostęp 23.11.2026) — <https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Które polecenie dodaje plik do poczekalni?
  - A) git commit
  - B) git add
  - C) git push
  - D) git log
- Co pokazuje git status?
  - A) historię commitów
  - B) co zmienione i co w poczekalni
  - C) adres GitHuba
  - D) wersję Gita
- Commit bez push:
  - A) jest na GitHubie
  - B) jest tylko na Twoim komputerze
  - C) znika po zamknięciu terminala
  - D) jest błędem
- Dobry opis commita:
  - A) zmiany
  - B) asdf
  - C) Dodaj walidację wieku w wiek.py
  - D) commit 5

Odpowiedzi: B, B, B, C
