# GitHub: konto z 2FA, repozytorium prywatne i wysyłanie zmian
Tydzień 6 · lekcja 20 z 48 · ≈ 50 min

**Po tej lekcji potrafisz:** masz konto GitHub z weryfikacją dwuetapową, prywatne repozytorium pod-lipa, połączenie z lokalnym repo (remote origin) i wysyłasz commity `git push`.

**Po co mi to?** GitHub to kopia zapasowa, portfolio dla rekrutera i miejsce, gdzie działają automatyczne testy (tydzień 13) oraz publikacja stron (tydzień 9).

## Czego potrzebujesz
- Lekcja „Git”.
- Adres e-mail i aplikacja uwierzytelniająca w telefonie (np. Microsoft Authenticator, Google Authenticator) albo klucz bezpieczeństwa.

## 1 · Wyjaśnienie od podstaw
### Konto
github.com → Sign up. Darmowe konto (GitHub Free) pozwala tworzyć repozytoria publiczne i prywatne. Nazwa użytkownika będzie w adresach Twoich projektów (github.com/nazwa/pod-lipa) — wybierz profesjonalną.
### Weryfikacja dwuetapowa (2FA)
Settings → Password and authentication → Enable two-factor authentication. Zeskanuj kod QR aplikacją uwierzytelniającą i ZAPISZ kody odzyskiwania (recovery codes) w bezpiecznym miejscu — bez nich utrata telefonu = utrata konta. GitHub wymaga 2FA od osób publikujących kod — i tak go włączysz.
### Repozytorium prywatne czy publiczne?
| | prywatne | publiczne |
|---|---|---|
| kto widzi | Ty i zaproszeni | wszyscy w internecie |
| kiedy | praca w toku, dane klienta (nawet fikcyjne — do czasu przeglądu) | portfolio, projekt końcowy po przeglądzie bezpieczeństwa |
| GitHub Pages w planie Free | nie | tak (tydzień 9) |
Zasada: zaczynasz od prywatnego; publiczne dopiero po sprawdzeniu, że nie ma tajemnic ani danych osobowych (tydzień 12–14).
### Połączenie lokalnego repo z GitHubem
- github.com → New repository → nazwa `pod-lipa`, Private, BEZ README (masz już lokalne commity).
- GitHub pokaże polecenia „…or push an existing repository from the command line”. W PRACA:
`git remote add origin https://github.com/NAZWA/pod-lipa.git`
`git branch -M main`
`git push -u origin main`
- Przy pierwszym push Git for Windows otworzy okno logowania (Git Credential Manager) — logujesz się w przeglądarce. Hasła do GitHuba NIE wpisujesz w terminalu.
- Potem już tylko `git push` po commitach. `git pull` pobiera zmiany z GitHuba (np. gdy coś poprawisz na stronie).
### README.md — wizytówka repozytorium
GitHub pokazuje README na stronie projektu. Na razie 5 linii: co to jest, jak uruchomić, jak uruchomić testy, status („projekt szkoleniowy, dane fikcyjne”). Pełne README w tygodniu 13.
### gh — opcjonalnie
GitHub CLI (`winget install --id GitHub.cli`, potem `gh auth login`) pozwala agentom zakładać repozytoria i zgłoszenia z terminala. W kursie nieobowiązkowe; aplikacja Codex zaleca je do pracy z GitHubem.

## 2 · Demonstracja — krok po kroku
**Od nowego konta do pierwszego push**

```
C:\...\PRACA>git remote add origin https://github.com/anna-dev/pod-lipa.git
C:\...\PRACA>git branch -M main
C:\...\PRACA>git push -u origin main
(okno logowania GitHub w przeglądarce)
Enumerating objects: 14, done.
...
To https://github.com/anna-dev/pod-lipa.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
```

1. Załóż konto, potwierdź e-mail, włącz 2FA i pobierz kody odzyskiwania (plik .txt → przenieś do menedżera haseł lub wydrukuj; nie trzymaj go w PRACA).
2. New repository: pod-lipa, Private, bez README/licencji/.gitignore (masz je lokalnie).
3. W PRACA: `git remote -v` (pusto) → `git remote add origin …` → `git remote -v` pokazuje adres.
4. `git push -u origin main` → logowanie w przeglądarce → odśwież stronę repozytorium: widzisz pliki i 3 commity.
5. Dodaj README.md lokalnie (5 linii), commit, `git push`. Na GitHubie README wyświetla się pod listą plików.
6. Sprawdź na GitHubie, że nie ma .env ani .venv — jeśli są, wróć do lekcji „Git” (git rm --cached) i unieważnij klucze.

✔ **Oczekiwany wynik:** Prywatne repozytorium pod-lipa na GitHubie z historią commitów i README; konto zabezpieczone 2FA.

## 3 · Jak to uruchomić
1. github.com → New repository → Private.
2. W PRACA: `git remote add origin <adres>` → `git push -u origin main`.

## W praktyce
- Push na koniec każdego dnia nauki.
- Repozytorium publiczne dopiero po przeglądzie bezpieczeństwa.

## 4 · Ćwiczenie prowadzone
Uporządkuj: A) `git push -u origin main`, B) utworzenie repozytorium na github.com, C) `git remote add origin https://github.com/…`, D) włączenie 2FA. Podaj kolejność liter. Gdzie wpisujesz hasło GitHuba przy pierwszym push — w terminalu czy w oknie przeglądarki? Czas: 15 minut.

📄 `cwiczenia/tydzien_06/github_konto_repo_1.md` · rozwiązanie: `rozwiazania/tydzien_06/github_konto_repo_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Repozytorium prywatne czy publiczne? (1) praca w toku z danymi „Pod Lipą” przed przeglądem, (2) projekt końcowy po przeglądzie bezpieczeństwa do portfolio, (3) repo, w którym przez pomyłkę był plik z kluczem API (klucz już usunięty w nowym commicie). W (3): czy usunięcie pliku w nowym commicie wystarczy (tak/nie)? Czas: 15 minut.

📄 `cwiczenia/tydzien_06/github_konto_repo_2.md` · rozwiązanie: `rozwiazania/tydzien_06/github_konto_repo_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **„remote origin already exists”.**
  - Przyczyna: Remote dodany wcześniej (może z literówką).
  - Jak sprawdzić: `git remote -v`.
  - Poprawka: `git remote set-url origin <poprawny adres>`.
- ✘ **„failed to push some refs … Updates were rejected”.**
  - Przyczyna: Na GitHubie są commity, których nie masz lokalnie (np. README utworzone na stronie).
  - Jak sprawdzić: Czy tworzyłeś pliki na github.com?
  - Poprawka: `git pull --rebase origin main`, potem `git push`. Na przyszłość: repo bez README przy tworzeniu.
- ✘ **„Repository not found” przy push.**
  - Przyczyna: Literówka w adresie albo zalogowane inne konto.
  - Jak sprawdzić: Adres w `git remote -v` vs strona repo.
  - Poprawka: Popraw adres; w Menedżerze poświadczeń Windows usuń stare dane github.com i zaloguj ponownie.

## Pułapki
- Kody odzyskiwania 2FA nie mogą leżeć w repozytorium ani w PRACA.
- Publiczne repozytorium pokazuje CAŁĄ historię, także stare wersje plików.

## Dodatkowe zadania
1. Konto z 2FA, prywatne repo pod-lipa, push (zadanie tygodnia).
2. README.md z 5 liniami.
3. Sprawdź na GitHubie brak .env i .venv.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Dlaczego zaczynasz od repozytorium prywatnego?**
  - Bo publiczne widzi cały internet razem z historią — najpierw przegląd tajemnic i danych.
- **Co robi git push -u origin main?**
  - Wysyła lokalne commity gałęzi main na GitHub i zapamiętuje powiązanie.
- **Co zrobić, gdy klucz API trafił do repo?**
  - Unieważnić go u dostawcy (i usunąć z plików) — historia go pamięta.

## Co potrafię teraz bez patrzenia na przykład?
Masz konto GitHub z 2FA, prywatne repozytorium połączone z lokalnym, wysyłasz commity i rozumiesz, kiedy repo może być publiczne.

## Źródła (data dostępu w nawiasie)
Narzędzia, ceny i przepisy zmieniają się — przed użyciem w pracy otwórz źródło.
- GitHub Docs — Quickstart for repositories (tworzenie repozytorium) (dostęp 19.11.2026) — <https://docs.github.com/en/repositories/creating-and-managing-repositories/quickstart-for-repositories>
- GitHub Docs — Configuring two-factor authentication (dostęp 19.11.2026) — <https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication>
- Pro Git (książka, wyd. 2, git-scm.com) — rozdz. 2: Podstawy Gita; dostępne tłumaczenie na polski (dostęp 19.11.2026) — <https://git-scm.com/book/pl/v2>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Kody odzyskiwania 2FA przechowujesz:
  - A) W README
  - B) W bezpiecznym miejscu poza projektem
  - C) W AGENTS.md
  - D) W mailu do siebie w repo
- Polecenie pobierające zmiany z GitHuba:
  - A) git push
  - B) git pull
  - C) git init
  - D) git add
- GitHub Pages w planie Free działa dla repozytoriów:
  - A) prywatnych
  - B) publicznych
  - C) żadnych
  - D) tylko firmowych
- Plik pokazywany na stronie repozytorium jako opis:
  - A) AGENTS.md
  - B) README.md
  - C) .gitignore
  - D) LICENSE

Odpowiedzi: B, B, B, B
