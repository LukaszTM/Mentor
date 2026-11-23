# Git w zespole: gałęzie, diff, log, cofanie zmian i pull request
Tydzień 4 · lekcja 19 z 39 · ≈ 45 min

**Po tej lekcji potrafisz:** pracujesz na gałęzi (git switch -c), przeglądasz zmiany (git diff, git log), cofasz zmiany w pliku (git restore), odkładasz je (git stash), scalasz gałąź i otwierasz pull request na GitHubie.

**Po co mi to?** W zespole nikt nie pracuje bezpośrednio na main. Tester recenzuje pull requesty, uruchamia testy na gałęzi i zgłasza uwagi przed scaleniem.

## Czego potrzebujesz
- Lekcja „Git i GitHub — pierwszy commit”.
- Repozytorium w PRACA wysłane na GitHub.

## 1 · Wyjaśnienie od podstaw
### Gałąź
Gałąź to osobna linia zmian. Na main jest działająca wersja; nową funkcję robisz na gałęzi `feature/csv`, a po sprawdzeniu scalasz. `git switch -c feature/csv` tworzy gałąź i przechodzi na nią; `git switch main` wraca; `git branch` pokazuje listę (gwiazdka = bieżąca).
### Co się zmieniło
- `git diff` — zmiany niezacommitowane, linia po linii: `-` usunięte, `+` dodane;
- `git diff --staged` — zmiany w poczekalni;
- `git log --oneline --graph --all` — historia wszystkich gałęzi w skrócie.
### Cofanie
| sytuacja | polecenie |
|---|---|
| zepsułem plik, nie commitowałem | `git restore plik.py` (wraca do ostatniego commita; zmiany przepadają!) |
| dodałem do poczekalni przez pomyłkę | `git restore --staged plik.py` |
| muszę na chwilę przełączyć gałąź, zmiany niegotowe | `git stash` → … → `git stash pop` |
| zły commit już wysłany | `git revert <sha>` — nowy commit odwracający |
Starsze instrukcje używają `git checkout -- plik` — działa tak samo jak restore.
### Scalanie i pull request
1. Na gałęzi: commity → `git push -u origin feature/csv`. 2. GitHub pokaże „Compare & pull request” → opis: co, dlaczego, jak sprawdzić. 3. Recenzja (Files changed, komentarze). 4. „Merge pull request”. 5. Lokalnie: `git switch main` → `git pull`.
Lokalne scalenie bez GitHuba: na main `git merge feature/csv`.
### Konflikt
Gdy dwie gałęzie zmieniły tę samą linię, Git wstawia znaczniki `<<<<<<<`, `=======`, `>>>>>>>`. Wybierasz właściwą wersję, usuwasz znaczniki, `git add` i `git commit`.

## 2 · Demonstracja — krok po kroku
**Funkcja na gałęzi i pull request**

```
PS …\PRACA> git switch -c feature/csv
Switched to a new branch 'feature/csv'
PS …\PRACA> git add csv_odczyt.py
PS …\PRACA> git commit -m "Dodaj odczyt produktów z CSV"
PS …\PRACA> git diff HEAD~1 --stat
 csv_odczyt.py | 18 ++++++++++++++++++
PS …\PRACA> git push -u origin feature/csv
remote: Create a pull request for 'feature/csv' on GitHub by visiting: …/pull/new/feature/csv
(GitHub: Compare & pull request → opis → Create → Merge pull request)
PS …\PRACA> git switch main
PS …\PRACA> git pull
PS …\PRACA> git log --oneline --graph
*   9c1d2e4 Merge pull request #1 from anna-nowak/feature/csv
|\
| * 5b7a3f0 Dodaj odczyt produktów z CSV
|/
* 3f2a1c9 Dodaj pierwszy program hello.py
```

1. `git switch -c feature/csv` — nowa gałąź od bieżącego main; od teraz commity trafiają na nią.
2. add + commit jak zwykle — main się nie zmienia.
3. `git diff HEAD~1 --stat` — podsumowanie: który plik i ile linii zmienił ostatni commit (HEAD~1 = commit przed bieżącym).
4. `git push -u origin feature/csv` — gałąź trafia na GitHub; terminal podaje link do utworzenia PR.
5. Na GitHubie: tytuł PR jak opis commita, w opisie „Co / Dlaczego / Jak sprawdzić”, zakładka Files changed — recenzja linii.
6. Merge pull request — GitHub tworzy commit scalający na main.
7. Lokalnie `git switch main` i `git pull` — Twoje main dogania GitHub.
8. `git log --oneline --graph` — rozgałęzienie i scalenie widoczne jako „gałązka”.

✔ **Oczekiwany wynik:** Na GitHubie zamknięty (scalony) PR #1, a w historii main commit „Merge pull request #1…”.

## 3 · Jak to uruchomić
1. Terminal w PRACA → polecenia z ramki.
2. GitHub → zakładka Pull requests → Compare & pull request.

## W praktyce
- Recenzując PR jako tester: uruchom testy na gałęzi, sprawdź opis „jak sprawdzić”, przetestuj przypadki brzegowe.
- Jeden PR = jedna zmiana, którą da się przejrzeć w 15 minut.

## 4 · Ćwiczenie prowadzone
Ułóż kroki pracy z gałęzią (numery po przecinku): 1 `git push -u origin feature/raport`, 2 `git switch -c feature/raport`, 3 Merge pull request na GitHubie, 4 `git commit -m "Dodaj raport"`, 5 `git switch main` i `git pull`. Czas: 10 minut.

📄 `cwiczenia/tydzien_04/git_1.md` · rozwiązanie: `rozwiazania/tydzien_04/git_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Dobierz polecenie: (1) zepsułeś(-aś) raport.py, nie było commita od rana, chcesz wrócić do ostatniej zapisanej wersji; (2) w połowie pracy musisz przełączyć gałąź, zmian nie chcesz commitować; (3) zły commit jest już na GitHubie i inni go pobrali; (4) chcesz zobaczyć, co dokładnie zmieniłeś przed commitem. Opcje: git restore raport.py / git stash / git revert <sha> / git diff. Czas: 15 minut.

📄 `cwiczenia/tydzien_04/git_2.md` · rozwiązanie: `rozwiazania/tydzien_04/git_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **error: Your local changes to the following files would be overwritten by checkout**
  - Przyczyna: Niezacommitowane zmiany przy przełączaniu gałęzi.
  - Jak sprawdzić: `git status`.
  - Poprawka: commit albo `git stash`, potem switch.
- ✘ **CONFLICT (content): Merge conflict in csv_odczyt.py**
  - Przyczyna: Ta sama linia zmieniona na dwóch gałęziach.
  - Jak sprawdzić: Otwórz plik, szukaj <<<<<<<.
  - Poprawka: Zostaw właściwą wersję, usuń znaczniki, git add, git commit.
- ✘ **fatal: The current branch feature/csv has no upstream branch**
  - Przyczyna: Pierwszy push gałęzi bez -u.
  - Jak sprawdzić: Komunikat podaje gotowe polecenie.
  - Poprawka: `git push -u origin feature/csv`.

## Pułapki
- git restore bezpowrotnie kasuje niezacommitowane zmiany w pliku — najpierw git diff.
- Praca tygodniami na jednej gałęzi bez scalania = duże konflikty; scalaj małe zmiany często.

## Dodatkowe zadania
1. Gałąź feature/csv → commit → push → PR → merge.
2. Celowo zepsuj plik i odzyskaj go git restore; potem przetestuj git stash.
3. Opisz w notatki.md różnicę restore / stash / revert.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Po co gałęzie?**
  - Żeby rozwijać zmianę osobno, nie psując działającego main.
- **Czym różni się revert od restore?**
  - revert tworzy commit odwracający wysłany commit; restore cofa niezacommitowane zmiany w pliku.
- **Co zawiera dobry opis PR?**
  - Co, dlaczego, jak sprawdzić.

## Co potrafię teraz bez patrzenia na przykład?
Pracujesz na gałęziach, przeglądasz diff i log, cofasz zmiany właściwym poleceniem, rozwiązujesz konflikt i przeprowadzasz pull request do scalenia.

## Źródła (data dostępu w nawiasie)
Wersje narzędzi i dane rynkowe zmieniają się — przed użyciem w pracy otwórz źródło.
- Pro Git PL — Gałęzie Gita (dostęp 23.11.2026) — <https://git-scm.com/book/pl/v2/Ga%C5%82%C4%99zie-Gita-Czym-jest-ga%C5%82%C4%85%C5%BA>
- Pro Git (wydanie 2, wersja polska) — Scott Chacon, Ben Straub (dostęp 23.11.2026) — <https://git-scm.com/book/pl/v2>
- Git — Reference (git restore, git stash, git log) (dostęp 23.11.2026) — <https://git-scm.com/docs>
- GitHub Docs — About pull requests (dostęp 23.11.2026) — <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Nowa gałąź i przejście na nią:
  - A) git branch -d x
  - B) git switch -c x
  - C) git merge x
  - D) git log x
- git stash:
  - A) usuwa commit
  - B) odkłada niezacommitowane zmiany
  - C) wysyła na GitHub
  - D) tworzy gałąź
- Znaczniki <<<<<<< w pliku oznaczają:
  - A) błąd Pythona
  - B) konflikt scalania
  - C) komentarz
  - D) nową gałąź
- Zły commit już pobrany przez innych cofasz:
  - A) git reset --hard i push --force
  - B) git revert
  - C) usuwając repozytorium
  - D) git stash

Odpowiedzi: B, B, B, B
