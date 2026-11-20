# -*- coding: utf-8 -*-
"""Etap 1, tygodnie 6–7: Git, GitHub, przegląd zmian agenta, kontekst i limity, gdy agent się myli, powtórka."""

from wspolne import (TN, B, C, L, T, bl, kod, kw, li, tx, wy)
from etap1 import (D, Z_CC_BEST, Z_CC_CHECK, Z_CC_COSTS, Z_CC_MODES, Z_CX_SLASH)

Z_GIT_BOOK = ["Pro Git (książka, wyd. 2, git-scm.com) — rozdz. 2: Podstawy Gita; dostępne tłumaczenie na polski", "https://git-scm.com/book/pl/v2", D]
Z_GIT_WIN = ["Git for Windows — pobieranie (git-scm.com)", "https://git-scm.com/downloads/win", D]
Z_GH_REPO = ["GitHub Docs — Quickstart for repositories (tworzenie repozytorium)", "https://docs.github.com/en/repositories/creating-and-managing-repositories/quickstart-for-repositories", D]
Z_GH_2FA = ["GitHub Docs — Configuring two-factor authentication", "https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication", D]
Z_GH_IGN = ["GitHub Docs — Ignoring files (.gitignore)", "https://docs.github.com/en/get-started/git-basics/ignoring-files", D]
Z_GIT_DIFF = ["Git — dokumentacja polecenia git diff", "https://git-scm.com/docs/git-diff", D]
Z_GIT_RESTORE = ["Git — dokumentacja polecenia git restore", "https://git-scm.com/docs/git-restore", D]
Z_VER = ["Veracode — GenAI Code Security Report (30.07.2025): 45% próbek kodu z AI z lukami", "https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/", D]


# =========================================================================== TYDZIEŃ 6
GIT = L(
    id="git_podstawy", nazwa="Git: zapisujesz wersje i cofasz się w czasie", tydzien=6,
    slowa=["git", "repozytorium", "commit", "status", "add", "log", "diff", "restore", ".gitignore"],
    cel="Po tej lekcji instalujesz Git, zakładasz repozytorium w PRACA, zapisujesz wersje (add + commit), oglądasz historię (log) i zmiany (diff) oraz cofasz niechciane zmiany (restore).",
    po_co="Git to trwała historia projektu i główna siatka bezpieczeństwa przy pracy z agentem — checkpointy agenta znikają, commity zostają.",
    wymagania=["Windows 10/11, ok. 300 MB miejsca.", "Terminal Mentora (CMD) albo PowerShell.", "Lekcja „Sesja z agentem”."],
    wyjasnienie=(
        "## Pojęcia w 5 zdaniach\n"
        "Repozytorium (repo) to folder projektu z ukrytym podfolderem `.git`, w którym Git trzyma historię. Commit to zapisana wersja wszystkich plików z opisem i autorem — jak punkt w grze, do którego można wrócić. "
        "Zanim zapiszesz commit, wskazujesz, które zmiany do niego wchodzą (`git add` — „poczekalnia”, staging). Gałąź (branch) to osobna linia zmian — w tym kursie pracujesz głównie na `main`. "
        "Git działa lokalnie, bez internetu; GitHub (następna lekcja) to kopia repozytorium w sieci.\n"
        "## Instalacja\n"
        "Git for Windows ze strony git-scm.com (przycisk Download) albo `winget install --id Git.Git -e --source winget`. Domyślne opcje instalatora są dobre. Nowe okno terminala → `git --version`. "
        "Raz na komputerze ustaw podpis: `git config --global user.name \"Imię Nazwisko\"` i `git config --global user.email \"adres@…\"` (adres będzie widoczny w historii publicznych repozytoriów — GitHub oferuje adres zastępczy typu noreply).\n"
        "## Siedem poleceń na co dzień\n"
        "| polecenie | co robi |\n"
        "|---|---|\n"
        "| `git init` | zakłada repozytorium w bieżącym folderze (raz) |\n"
        "| `git status` | co się zmieniło, co jest w poczekalni — używaj CIĄGLE |\n"
        "| `git add plik.py` / `git add .` | dodaje zmiany do poczekalni (kropka = wszystko, uważaj!) |\n"
        "| `git commit -m \"opis\"` | zapisuje wersję z opisem |\n"
        "| `git log --oneline` | historia: jedna linia na commit |\n"
        "| `git diff` | co zmieniło się od ostatniego commita (linie - usunięte, + dodane) |\n"
        "| `git restore plik.py` | cofa NIEZAPISANE zmiany w pliku do ostatniego commita (nieodwracalne!) |\n"
        "## .gitignore — czego nie zapisywać\n"
        "Plik `.gitignore` w korzeniu repozytorium wymienia, czego Git ma nie śledzić: `.venv/`, `__pycache__/`, `.env` (tajemnice!), pliki tymczasowe. Dodaj go PRZED pierwszym `git add .`.\n"
        "## Dobry opis commita\n"
        "Krótko, w trybie rozkazującym, co zmienia: „Dodaj walidację telefonu z +48”, „Popraw rabat od 7 nocy (>= zamiast >)”. Zły: „zmiany”, „fix”, „asdf”. Agenci piszą dobre opisy, jeśli o to poprosisz — ale czytasz je przed zatwierdzeniem.\n"
        "## Rytm pracy z agentem\n"
        "Zielony test → `git status` → `git diff` (przegląd) → `git add` wybranych plików → `git commit -m`. Agent może robić commity za Ciebie (prosi o zgodę na komendę) — w kursie robisz je sam, dopóki nie czytasz diffów płynnie.\n"
        "## Cofanie — trzy sytuacje\n"
        "- Zmiana niezapisana, chcesz ją wyrzucić: `git restore plik.py`.\n"
        "- Dodałeś do poczekalni za dużo: `git restore --staged plik.py` (zmiana zostaje w pliku, wypada z poczekalni).\n"
        "- Ostatni commit był zły: `git revert HEAD` tworzy NOWY commit odwracający poprzedni — bezpieczne, historia zostaje. Komend `git reset --hard` i `git push --force` w kursie nie używasz (tryb auto Claude Code też je blokuje)."),
    przyklad=("C:\\...\\PRACA>git init\nInitialized empty Git repository in C:/.../PRACA/.git/\n\n"
              "C:\\...\\PRACA>git status\nOn branch main\nUntracked files:\n  .gitignore\n  kalkulator_pobytu.py\n  ...\n\n"
              "C:\\...\\PRACA>git add .gitignore kalkulator_pobytu.py\nC:\\...\\PRACA>git commit -m \"Dodaj kalkulator pobytu z rabatem od 7 nocy\"\n"
              "[main (root-commit) 3f2a1c9] Dodaj kalkulator pobytu z rabatem od 7 nocy\n 2 files changed, 24 insertions(+)\n\n"
              "C:\\...\\PRACA>git log --oneline\n3f2a1c9 (HEAD -> main) Dodaj kalkulator pobytu z rabatem od 7 nocy"),
    demonstracja={"tytul": "Repozytorium w PRACA i ratunek po złej zmianie", "kroki": [
        "Terminal Mentora w PRACA: `git --version` (jest), `git init`. Utwórz .gitignore z liniami `.venv/`, `__pycache__/`, `.env`, `*.tmp`.",
        "`git status` — lista nieśledzonych plików. Commit 1: `git add .gitignore` + `git commit -m \"Dodaj .gitignore\"`.",
        "Commit 2: `git add kalkulator_pobytu.py lista_gosci.py` + opis. Commit 3: pozostałe pliki zadań z tygodni 1–3 (sprawdź status, czy nie ma tam niczego prywatnego).",
        "Symulacja błędu: w rabaty.py zmień 150 na 15 i zapisz. „✔ Sprawdź wynik” — czerwone.",
        "`git diff` pokazuje: `-    return 150 if …` / `+    return 15 if …`. `git restore rabaty.py` → plik wraca, test zielony.",
        "`git log --oneline` — 3 commity. To jest Twoja historia; agent może zepsuć pliki, ale nie historię."],
        "wynik": "Repozytorium z 3 commitami i .gitignore; zła zmiana znaleziona przez diff i cofnięta restore w 10 sekund."},
    jak_uruchomic=["`winget install --id Git.Git -e --source winget` albo instalator z git-scm.com → nowe okno → `git --version`.", "W PRACA: `git init`, potem rytm status → diff → add → commit."],
    cwiczenia=[
        C("prowadzone",
          "Uporządkuj polecenia pierwszego zapisu wersji: A) `git commit -m \"Dodaj kalkulator\"`, B) `git init`, C) `git add kalkulator_pobytu.py`, D) `git status`. Podaj kolejność liter. "
          "Które polecenie cofa niezapisane zmiany w pliku (bez commita)? Czas: 15 minut.",
          "BDCA; git restore plik.",
          ["Najpierw repozytorium musi istnieć.", "Status przed dodaniem — wiesz, co dodajesz.", "Commit na końcu."],
          "init → status → add → commit = BDCA. Cofnięcie niezapisanych zmian: git restore <plik>.",
          [tx("kol", "Kolejność liter", ["BDCA"]), tx("restore", "Polecenie cofające niezapisane zmiany (bez nazwy pliku)", ["git restore"])]),
        C("samodzielne",
          "Które pliki NIE powinny trafić do repozytorium? (1) rabaty.py (2) .env z kluczem API (3) folder .venv (4) AGENTS.md (5) __pycache__. Podaj numery rosnąco jako ciąg cyfr. "
          "Który opis commita jest najlepszy: (A) „zmiany” (B) „Popraw rabat: >= 7 nocy zamiast > 7” (C) „fix fix fix”? Czas: 15 minut.",
          "Nie powinny: 2, 3, 5 → „235”; najlepszy opis: B.",
          ["Tajemnice nigdy w repozytorium.", "Środowisko .venv i pamięć podręczna Pythona odtwarzają się same.", "Opis mówi CO i DLACZEGO."],
          ".env (tajemnica), .venv i __pycache__ (pliki generowane) → 235. Opis B mówi, co i dlaczego zmieniono.",
          [tx("ign", "Numery plików do .gitignore", ["235"], bledy=[bl("35", "plik .env z kluczem to najważniejsza pozycja .gitignore")]),
           wy("opis", "Najlepszy opis commita", ["A", "B", "C"], "B")]),
    ],
    typowe_bledy=[
        B("„Author identity unknown — Please tell me who you are”.", "Brak git config user.name / user.email.", "`git config --global --list`.", "Ustaw oba: git config --global user.name \"…\" i user.email \"…\"."),
        B("„fatal: not a git repository”.", "Terminal nie jest w folderze z repozytorium.", "`cd` — gdzie jesteś? Czy jest folder .git (dir /a)?", "Przejdź do PRACA albo zrób git init."),
        B("Do repozytorium trafił .env albo .venv.", "`git add .` przed utworzeniem .gitignore.", "`git status`, `git log --stat`.", "`git rm --cached .env`, dopisz do .gitignore, commit; jeśli klucz trafił do GitHuba — UNIEWAŻNIJ klucz u dostawcy (historia go pamięta)."),
    ],
    pulapki=["`git restore` i usunięcie niezapisanych zmian są nieodwracalne — najpierw `git diff`, żeby wiedzieć, co tracisz.",
             "`git add .` dodaje wszystko, także pliki, których nie chcesz. Na początku dodawaj pliki po nazwie."],
    zadania=["Załóż repozytorium w PRACA z .gitignore i 3 commitami (zadanie tygodnia).", "Przećwicz diff + restore na celowo złej zmianie.", "Napisz 3 opisy commitów według zasady „co i dlaczego”."],
    pytania=[["Czym jest commit?", "Zapisaną wersją plików z opisem i autorem, do której można wrócić."],
             ["Po co .gitignore?", "Żeby Git nie śledził tajemnic (.env) i plików generowanych (.venv, __pycache__)."],
             ["Jak bezpiecznie odwrócić zły commit?", "git revert HEAD — nowy commit odwracający zmiany, historia zostaje."]],
    podsumowanie="Instalujesz Git, zakładasz repozytorium, zapisujesz wersje z dobrymi opisami, czytasz historię i diff, cofasz restore i revert, chronisz tajemnice .gitignore.",
    test=[T("Polecenie pokazujące, co się zmieniło i co jest w poczekalni:", ["git log", "git status", "git init", "git push"], 1, "Używaj ciągle."),
          T("W `git diff` linie zaczynające się od + to:", ["Usunięte", "Dodane", "Komentarze", "Błędy"], 1, "- usunięte, + dodane."),
          T("Plik .env z kluczem API:", ["Commitujesz", "Dodajesz do .gitignore", "Wysyłasz agentowi", "Wklejasz do README"], 1, "Tajemnica."),
          T("Bezpieczne odwrócenie ostatniego commita:", ["git reset --hard", "git revert HEAD", "git push --force", "Usunięcie folderu .git"], 1, "Historia zostaje.")],
    w_praktyce=["Commit po każdym zielonym kroku.", "Przed każdą sesją agenta: git status czysty."],
    zrodla=[Z_GIT_BOOK, Z_GIT_WIN, Z_GH_IGN, Z_GIT_RESTORE],
)

GITHUB = L(
    id="github_konto_repo", nazwa="GitHub: konto z 2FA, repozytorium prywatne i wysyłanie zmian", tydzien=6,
    slowa=["GitHub", "konto", "2FA", "repozytorium", "remote", "push", "pull", "prywatne", "README"],
    cel="Po tej lekcji masz konto GitHub z weryfikacją dwuetapową, prywatne repozytorium pod-lipa, połączenie z lokalnym repo (remote origin) i wysyłasz commity `git push`.",
    po_co="GitHub to kopia zapasowa, portfolio dla rekrutera i miejsce, gdzie działają automatyczne testy (tydzień 13) oraz publikacja stron (tydzień 9).",
    wymagania=["Lekcja „Git”.", "Adres e-mail i aplikacja uwierzytelniająca w telefonie (np. Microsoft Authenticator, Google Authenticator) albo klucz bezpieczeństwa."],
    wyjasnienie=(
        "## Konto\n"
        "github.com → Sign up. Darmowe konto (GitHub Free) pozwala tworzyć repozytoria publiczne i prywatne. Nazwa użytkownika będzie w adresach Twoich projektów (github.com/nazwa/pod-lipa) — wybierz profesjonalną.\n"
        "## Weryfikacja dwuetapowa (2FA)\n"
        "Settings → Password and authentication → Enable two-factor authentication. Zeskanuj kod QR aplikacją uwierzytelniającą i ZAPISZ kody odzyskiwania (recovery codes) w bezpiecznym miejscu — bez nich utrata telefonu = utrata konta. "
        "GitHub wymaga 2FA od osób publikujących kod — i tak go włączysz.\n"
        "## Repozytorium prywatne czy publiczne?\n"
        "| | prywatne | publiczne |\n"
        "|---|---|---|\n"
        "| kto widzi | Ty i zaproszeni | wszyscy w internecie |\n"
        "| kiedy | praca w toku, dane klienta (nawet fikcyjne — do czasu przeglądu) | portfolio, projekt końcowy po przeglądzie bezpieczeństwa |\n"
        "| GitHub Pages w planie Free | nie | tak (tydzień 9) |\n"
        "Zasada: zaczynasz od prywatnego; publiczne dopiero po sprawdzeniu, że nie ma tajemnic ani danych osobowych (tydzień 12–14).\n"
        "## Połączenie lokalnego repo z GitHubem\n"
        "- github.com → New repository → nazwa `pod-lipa`, Private, BEZ README (masz już lokalne commity).\n"
        "- GitHub pokaże polecenia „…or push an existing repository from the command line”. W PRACA:\n"
        "`git remote add origin https://github.com/NAZWA/pod-lipa.git`\n`git branch -M main`\n`git push -u origin main`\n"
        "- Przy pierwszym push Git for Windows otworzy okno logowania (Git Credential Manager) — logujesz się w przeglądarce. Hasła do GitHuba NIE wpisujesz w terminalu.\n"
        "- Potem już tylko `git push` po commitach. `git pull` pobiera zmiany z GitHuba (np. gdy coś poprawisz na stronie).\n"
        "## README.md — wizytówka repozytorium\n"
        "GitHub pokazuje README na stronie projektu. Na razie 5 linii: co to jest, jak uruchomić, jak uruchomić testy, status („projekt szkoleniowy, dane fikcyjne”). Pełne README w tygodniu 13.\n"
        "## gh — opcjonalnie\n"
        "GitHub CLI (`winget install --id GitHub.cli`, potem `gh auth login`) pozwala agentom zakładać repozytoria i zgłoszenia z terminala. W kursie nieobowiązkowe; aplikacja Codex zaleca je do pracy z GitHubem."),
    przyklad=("C:\\...\\PRACA>git remote add origin https://github.com/anna-dev/pod-lipa.git\n"
              "C:\\...\\PRACA>git branch -M main\nC:\\...\\PRACA>git push -u origin main\n"
              "(okno logowania GitHub w przeglądarce)\nEnumerating objects: 14, done.\n...\nTo https://github.com/anna-dev/pod-lipa.git\n * [new branch]      main -> main\n"
              "branch 'main' set up to track 'origin/main'."),
    demonstracja={"tytul": "Od nowego konta do pierwszego push", "kroki": [
        "Załóż konto, potwierdź e-mail, włącz 2FA i pobierz kody odzyskiwania (plik .txt → przenieś do menedżera haseł lub wydrukuj; nie trzymaj go w PRACA).",
        "New repository: pod-lipa, Private, bez README/licencji/.gitignore (masz je lokalnie).",
        "W PRACA: `git remote -v` (pusto) → `git remote add origin …` → `git remote -v` pokazuje adres.",
        "`git push -u origin main` → logowanie w przeglądarce → odśwież stronę repozytorium: widzisz pliki i 3 commity.",
        "Dodaj README.md lokalnie (5 linii), commit, `git push`. Na GitHubie README wyświetla się pod listą plików.",
        "Sprawdź na GitHubie, że nie ma .env ani .venv — jeśli są, wróć do lekcji „Git” (git rm --cached) i unieważnij klucze."],
        "wynik": "Prywatne repozytorium pod-lipa na GitHubie z historią commitów i README; konto zabezpieczone 2FA."},
    jak_uruchomic=["github.com → New repository → Private.", "W PRACA: `git remote add origin <adres>` → `git push -u origin main`."],
    cwiczenia=[
        C("prowadzone",
          "Uporządkuj: A) `git push -u origin main`, B) utworzenie repozytorium na github.com, C) `git remote add origin https://github.com/…`, D) włączenie 2FA. Podaj kolejność liter. "
          "Gdzie wpisujesz hasło GitHuba przy pierwszym push — w terminalu czy w oknie przeglądarki? Czas: 15 minut.",
          "DBCA; w oknie przeglądarki (Git Credential Manager).",
          ["Najpierw bezpieczeństwo konta.", "Remote możesz dodać, gdy repozytorium na GitHubie istnieje.", "Git for Windows ma menedżer logowania."],
          "2FA → repo na GitHubie → remote add → push = DBCA. Logowanie w przeglądarce, nie hasło w terminalu.",
          [tx("kol", "Kolejność liter", ["DBCA"]), wy("haslo", "Gdzie logowanie?", ["w terminalu", "w oknie przeglądarki"], "w oknie przeglądarki")]),
        C("samodzielne",
          "Repozytorium prywatne czy publiczne? (1) praca w toku z danymi „Pod Lipą” przed przeglądem, (2) projekt końcowy po przeglądzie bezpieczeństwa do portfolio, (3) repo, w którym przez pomyłkę był plik z kluczem API (klucz już usunięty w nowym commicie). "
          "W (3): czy usunięcie pliku w nowym commicie wystarczy (tak/nie)? Czas: 15 minut.",
          "(1) prywatne; (2) publiczne; (3) prywatne — i NIE wystarczy: klucz jest w historii, trzeba go unieważnić u dostawcy.",
          ["Publiczne = cały internet, także historia commitów.", "Portfolio musi być widoczne.", "Historia Gita pamięta każdą wersję pliku."],
          "(1) prywatne, (2) publiczne po przeglądzie, (3) prywatne + unieważnienie klucza — usunięcie pliku nie usuwa go z historii.",
          [wy("r1", "(1)", ["prywatne", "publiczne"], "prywatne"), wy("r2", "(2)", ["prywatne", "publiczne"], "publiczne"), wy("r3", "(3)", ["prywatne", "publiczne"], "prywatne"),
           wy("wyst", "Usunięcie pliku w nowym commicie wystarczy?", TN, "nie", bledy=[bl("tak", "historia commitów pamięta stary plik — klucz trzeba unieważnić u dostawcy")])]),
    ],
    typowe_bledy=[
        B("„remote origin already exists”.", "Remote dodany wcześniej (może z literówką).", "`git remote -v`.", "`git remote set-url origin <poprawny adres>`."),
        B("„failed to push some refs … Updates were rejected”.", "Na GitHubie są commity, których nie masz lokalnie (np. README utworzone na stronie).", "Czy tworzyłeś pliki na github.com?", "`git pull --rebase origin main`, potem `git push`. Na przyszłość: repo bez README przy tworzeniu."),
        B("„Repository not found” przy push.", "Literówka w adresie albo zalogowane inne konto.", "Adres w `git remote -v` vs strona repo.", "Popraw adres; w Menedżerze poświadczeń Windows usuń stare dane github.com i zaloguj ponownie."),
    ],
    pulapki=["Kody odzyskiwania 2FA nie mogą leżeć w repozytorium ani w PRACA.", "Publiczne repozytorium pokazuje CAŁĄ historię, także stare wersje plików."],
    zadania=["Konto z 2FA, prywatne repo pod-lipa, push (zadanie tygodnia).", "README.md z 5 liniami.", "Sprawdź na GitHubie brak .env i .venv."],
    pytania=[["Dlaczego zaczynasz od repozytorium prywatnego?", "Bo publiczne widzi cały internet razem z historią — najpierw przegląd tajemnic i danych."],
             ["Co robi git push -u origin main?", "Wysyła lokalne commity gałęzi main na GitHub i zapamiętuje powiązanie."],
             ["Co zrobić, gdy klucz API trafił do repo?", "Unieważnić go u dostawcy (i usunąć z plików) — historia go pamięta."]],
    podsumowanie="Masz konto GitHub z 2FA, prywatne repozytorium połączone z lokalnym, wysyłasz commity i rozumiesz, kiedy repo może być publiczne.",
    test=[T("Kody odzyskiwania 2FA przechowujesz:", ["W README", "W bezpiecznym miejscu poza projektem", "W AGENTS.md", "W mailu do siebie w repo"], 1, "Poza projektem."),
          T("Polecenie pobierające zmiany z GitHuba:", ["git push", "git pull", "git init", "git add"], 1, "pull = pobierz."),
          T("GitHub Pages w planie Free działa dla repozytoriów:", ["prywatnych", "publicznych", "żadnych", "tylko firmowych"], 1, "Tydzień 9."),
          T("Plik pokazywany na stronie repozytorium jako opis:", ["AGENTS.md", "README.md", ".gitignore", "LICENSE"], 1, "Wizytówka.")],
    w_praktyce=["Push na koniec każdego dnia nauki.", "Repozytorium publiczne dopiero po przeglądzie bezpieczeństwa."],
    zrodla=[Z_GH_REPO, Z_GH_2FA, Z_GIT_BOOK],
)

PRZEGLAD = L(
    id="przeglad_zmian", nazwa="Przegląd zmian agenta: czytasz diff jak recenzent", tydzien=6,
    slowa=["diff", "przegląd", "recenzja", "zakres", "test", "zależność", "git diff", "/diff"],
    cel="Po tej lekcji czytasz diff zmian agenta i przechodzisz listę kontrolną 8 pytań (zakres, testy, nowe zależności, tajemnice, ukryte błędy) zanim zrobisz commit.",
    po_co="Raport Veracode (2025): w 45% próbek kodu wygenerowanego przez modele były luki bezpieczeństwa. Przegląd zmian to moment, w którym je łapiesz — taniej niż u klienta.",
    wymagania=["Lekcje „Git” i „Sesja z agentem”.", "Plik pomoc/diff_agenta.md z materiałów (zadanie tygodnia)."],
    wyjasnienie=(
        "## Jak czytać diff\n"
        "```\n--- a/rabaty.py\n+++ b/rabaty.py\n@@ -14,7 +14,9 @@ def rabat(noce, osoby):\n-    if noce >= 7:\n+    if noce > 7:\n         r += 10\n```\n"
        "- `---` stara wersja, `+++` nowa. `@@ -14,7 +14,9 @@` — fragment zaczyna się w linii 14.\n"
        "- Linie z `-` usunięte, z `+` dodane, bez znaku — kontekst bez zmian.\n"
        "- Gdzie oglądać: `git diff` (zmiany niezapisane), `git diff --staged` (w poczekalni), `/diff` w Codex, w Claude Code — okno zgody pokazuje zmianę przed zapisem; w VS Code — zakładka Source Control.\n"
        "## Lista kontrolna 8 pytań (przed każdym commitem)\n"
        "| # | pytanie | czerwona flaga |\n"
        "|---|---|---|\n"
        "| 1 | Czy zmiana dotyczy tylko tego, o co prosiłem? | zmienione pliki spoza zadania |\n"
        "| 2 | Czy testy zostały zmienione? | usunięty test, osłabiony assert, `pytest.skip` — „naprawa” przez zmianę testu |\n"
        "| 3 | Czy doszły nowe zależności (import, requirements)? | nieznana paczka — sprawdź na pypi.org, czy istnieje i kto ją wydaje |\n"
        "| 4 | Czy w kodzie są tajemnice? | klucze, hasła, adresy z tokenem |\n"
        "| 5 | Czy błędy nie są ukrywane? | `except: pass`, `except Exception: return None` bez komunikatu |\n"
        "| 6 | Czy granice i przypadki brzegowe są zachowane? | `>=` → `>`, usunięte `raise ValueError` |\n"
        "| 7 | Czy coś zostało usunięte bez powodu? | znikające funkcje, komentarze z ważną informacją |\n"
        "| 8 | Czy rozumiem każdą dodaną linię? | linie „magiczne” — zapytaj agenta, zanim zatwierdzisz |\n"
        "## Wielkość zmian ma znaczenie\n"
        "Diff powyżej ok. 200 linii przestaje być czytany uważnie — przez ludzi i przez modele recenzujące. To kolejny argument za małymi krokami. "
        "Gdy agent oddał dużą zmianę, poproś: „podziel to na 3 commity tematycznie i opisz każdy”.\n"
        "## Recenzja z pomocą AI — dodatek, nie zastępstwo\n"
        "Codex ma `/review` (przegląd zmian w katalogu pod kątem zmian zachowania i brakujących testów); Claude Code możesz poprosić: „zrób przegląd diffu według tej listy 8 pytań”. "
        "Dobry pomysł: recenzja w NOWEJ sesji (agent, który pisał kod, chętniej go broni). Decyzja i tak należy do Ciebie."),
    przyklad=("Fragment diffu od agenta (zadanie: „popraw komunikat błędu w czy_email”):\n\n"
              "--- a/walidacja.py\n+++ b/walidacja.py\n"
              "-def czy_email(tekst):\n-    t = (tekst or \"\").strip()\n+import email_validator_pl\n+\n+def czy_email(tekst):\n+    try:\n+        return email_validator_pl.check(tekst)\n+    except Exception:\n+        return True\n"
              "--- a/test_walidacja.py\n+++ b/test_walidacja.py\n-    assert czy_email(\"anna@\") is False\n\n"
              "Czerwone flagi: 3 (nieznana paczka), 5 (except zwraca True — każdy błąd = „poprawny e-mail”), 2 (usunięty test), 1 (zadanie dotyczyło komunikatu, nie logiki)."),
    demonstracja={"tytul": "Przegląd diffu z listą 8 pytań", "kroki": [
        "Agent zgłasza: „Gotowe, testy przechodzą”. Zanim uwierzysz: `git status` — zmienione 3 pliki, choć zadanie dotyczyło jednego.",
        "`git diff` pliku z zadania: zmiana sensowna. Pytanie 6 — granica `>= 7` zachowana. OK.",
        "`git diff` pliku testów: agent usunął assert dla przypadku brzegowego, „bo był sprzeczny”. Czerwona flaga 2.",
        "`git diff` trzeciego pliku (requirements.txt): nowa paczka o nieznanej nazwie. Sprawdzasz na pypi.org — brak takiej paczki. Czerwona flaga 3 (możliwa halucynacja lub pułapka — tydzień 12).",
        "Decyzja: `git restore test_rabaty.py requirements.txt`, commit tylko pliku z zadania. Do agenta: „Nie zmieniaj testów ani zależności; jeśli test wydaje się błędny — opisz dlaczego, nie usuwaj”. Dopisujesz tę zasadę do AGENTS.md."],
        "wynik": "Zatwierdzona tylko właściwa zmiana; usunięty test i zmyślona zależność odrzucone przed commitem."},
    jak_uruchomic=["`git status` → `git diff <plik>` → lista 8 pytań → `git add <wybrane>` → commit.", "Codex: `/diff`, `/review`."],
    cwiczenia=[
        C("prowadzone",
          "Przeczytaj diff z przykładu lekcji. Ile czerwonych flag z listy 8 pytań w nim jest? Który numer pytania dotyczy linii `except Exception: return True`? "
          "Czy zatwierdzisz tę zmianę w całości (tak/nie)? Czas: 20 minut.",
          "4 flagi (1, 2, 3, 5); except → pytanie 5; nie zatwierdzasz.",
          ["Zakres: zadanie dotyczyło komunikatu.", "Usunięty assert w pliku testów.", "Nowy import nieznanej paczki i except zwracający True."],
          "Flagi: 1 (zakres), 2 (usunięty test), 3 (nowa nieznana zależność), 5 (ukryty błąd) = 4. Zmiana do odrzucenia.",
          [li("flagi", "Liczba czerwonych flag", 4), li("nr", "Numer pytania dla except: return True", 5), wy("ok", "Zatwierdzasz w całości?", TN, "nie")]),
        C("samodzielne",
          "Diff ma linię `-    if noce >= 7:` i pod nią `+    if noce > 7:`. (1) Która wersja jest nowa? (2) Dla ilu nocy zmienia się wynik funkcji (podaj jedną liczbę)? "
          "(3) Którym poleceniem zobaczysz zmiany już dodane do poczekalni? Czas: 15 minut.",
          "(1) `if noce > 7:` (z plusem); (2) dla 7 nocy; (3) git diff --staged.",
          ["Plus = dodane = nowa wersja.", "Różnica między >= a > dotyczy tylko wartości równej granicy.", "Poczekalnia po angielsku: staged."],
          "Nowa: noce > 7; różnica tylko dla 7 nocy (rabat znika); git diff --staged pokazuje zmiany w poczekalni.",
          [wy("nowa", "(1) Nowa wersja", ["if noce >= 7:", "if noce > 7:"], "if noce > 7:"), li("noce", "(2) Dla ilu nocy zmienia się wynik?", 7),
           tx("staged", "(3) Polecenie", ["git diff --staged", "git diff --cached"])]),
    ],
    typowe_bledy=[
        B("Commit zawiera zmiany, których nie przeglądałeś.", "`git add .` po pracy agenta.", "`git show --stat` ostatniego commita.", "Dodawaj pliki po nazwie po przeglądzie; jeśli trzeba — `git revert HEAD`."),
        B("Testy zielone, ale klient zgłasza błąd.", "Agent osłabił lub usunął test.", "`git log -p -- test_*.py` — historia zmian testów.", "Przywróć test, zasada „nie zmieniaj testów” w AGENTS.md, przegląd pytania 2 przy każdym commicie."),
    ],
    pulapki=["„Testy przechodzą” od agenta to informacja do sprawdzenia, nie zwolnienie z przeglądu.", "Recenzja AI w tej samej sesji, która napisała kod, łatwo przeoczy własne błędy — używaj nowej sesji."],
    zadania=["Przejrzyj diff z materiałów listą 8 pytań (zadanie tygodnia).", "Przed każdym commitem w tym tygodniu — lista 8 pytań.", "Dopisz do AGENTS.md: „nie zmieniaj testów ani zależności bez pytania”."],
    pytania=[["Co oznaczają + i - w diffie?", "Linie dodane i usunięte."], ["Dlaczego zmiana testu przez agenta to czerwona flaga?", "Bo może „naprawić” problem, osłabiając sprawdzenie zamiast poprawiać kod."],
             ["Jak sprawdzisz nową zależność?", "Na pypi.org: czy istnieje, kto ją wydaje, czy jest używana — i czy w ogóle jest potrzebna."]],
    podsumowanie="Czytasz diff, przechodzisz listę 8 pytań, odrzucasz zmiany poza zakresem, osłabione testy, nieznane zależności i ukryte błędy przed commitem.",
    test=[T("Linia `-    raise ValueError(...)` w diffie oznacza:", ["Dodanie walidacji", "Usunięcie walidacji", "Komentarz", "Nic"], 1, "Czerwona flaga 6."),
          T("Agent „naprawił” test, usuwając assert. Pytanie z listy:", ["1", "2", "4", "8"], 1, "Zmiana testów."),
          T("`except Exception: pass` w nowym kodzie to:", ["Dobra praktyka", "Ukrywanie błędów", "Szybsze działanie", "Wymóg Pythona"], 1, "Pytanie 5."),
          T("Gdzie najlepiej zlecić recenzję AI?", ["W tej samej sesji, która pisała kod", "W nowej sesji", "Nigdzie", "Na forum"], 1, "Świeże spojrzenie.")],
    w_praktyce=["Lista 8 pytań wisi obok monitora.", "Diff > 200 linii → poproś o podział."],
    zrodla=[Z_GIT_DIFF, Z_VER, Z_CX_SLASH, Z_CC_BEST],
)


# =========================================================================== TYDZIEŃ 7
KONTEKST = L(
    id="kontekst_limity", nazwa="Kontekst, limity i koszt sesji: /context, /clear, /compact, /usage", tydzien=7,
    slowa=["kontekst", "/context", "/clear", "/compact", "/usage", "/status", "model", "effort", "limit"],
    cel="Po tej lekcji mierzysz zajętość kontekstu, czyścisz i streszczasz rozmowę, dobierasz model i wysiłek do zadania oraz planujesz pracę tak, by nie przekraczać limitów.",
    po_co="Dokumentacja Claude Code: koszt rośnie z rozmiarem kontekstu, a `/clear` to najtańsza praktyka. Kto zarządza kontekstem, robi więcej w tym samym planie i dostaje lepsze odpowiedzi.",
    wymagania=["Lekcje „Konta, plany i koszty” i „Małe kroki”."],
    wyjasnienie=(
        "## Dlaczego kontekst kosztuje\n"
        "Przy każdej Twojej wiadomości agent wysyła modelowi całą dotychczasową rozmowę: instrukcje (CLAUDE.md/AGENTS.md), przeczytane pliki, wyniki komend, swoje odpowiedzi. "
        "Godzinna sesja to dziesiątki tysięcy tokenów przy KAŻDEJ wiadomości. Dlatego długie sesje szybciej zużywają limit i — gdy okno się zapełnia — gorzej pamiętają wcześniejsze ustalenia.\n"
        "## Polecenia\n"
        "| cel | Claude Code | Codex |\n"
        "|---|---|---|\n"
        "| ile kontekstu zajęte | `/context` (wykres: instrukcje, pliki, rozmowa) | `/status` |\n"
        "| limity planu | `/usage` | `/status` |\n"
        "| nowy temat, czysta kartka | `/clear` | `/new` |\n"
        "| streszczenie zamiast kasowania | `/compact` (można dodać, co zachować: `/compact zachowaj decyzje o rabatach`) | `/compact` |\n"
        "| zmiana modelu | `/model` | `/model` |\n"
        "| wysiłek rozumowania | `/effort` | (wybór modelu/ustawień) |\n"
        "| powrót do starej sesji | `/resume`, nazwanie `/rename` | (historia sesji w aplikacji) |\n"
        "## Strategie z dokumentacji (w skrócie)\n"
        "- `/clear` między niezwiązanymi zadaniami — najtańsze.\n"
        "- Konkretne prośby zamiast „popraw cały projekt” — agent czyta mniej plików.\n"
        "- Tryb planu przy złożonych zadaniach — mniej prób i błędów.\n"
        "- Lżejszy model do prostych zadań, mocniejszy do trudnych (nazwy modeli sprawdzasz w `/model` — zmieniają się).\n"
        "- Krótkie pliki instrukcji (każda linia CLAUDE.md jest wysyłana przy każdej wiadomości).\n"
        "## Notatka przekazania (handoff)\n"
        "Przed `/clear` po dłuższej pracy poproś: „Zapisz w notatki/stan.md: co zrobione, decyzje, co dalej, otwarte pytania — maks. 15 linii”. Nowa sesja: „Przeczytaj notatki/stan.md i AGENTS.md”. "
        "To tańsze i pewniejsze niż wielogodzinna rozmowa.\n"
        "## Planowanie dnia pod limity\n"
        "Okno ok. 5 godzin: rozkładaj trudne zadania na początek okna, nie zostawiaj ich na koniec. Gdy limit się kończy — przejdź do pracy bez agenta: przegląd diffów, testy, README, dziennik."),
    przyklad=("Sesja przed i po porządkach (wartości przykładowe):\n\n"
              "/context → 142 tys. tokenów: instrukcje 3 tys., pliki 61 tys., rozmowa 78 tys.\n"
              "Prośba: „Zapisz notatki/stan.md (maks. 15 linii)”.\n/clear\n"
              "„Przeczytaj notatki/stan.md i AGENTS.md, potem zrób punkt 3 planu.”\n/context → 18 tys. tokenów."),
    demonstracja={"tytul": "Sesja, która „zgłupiała”, i jej naprawa", "kroki": [
        "Po 2 godzinach pracy agent zaczyna przywracać rozwiązanie, które 40 minut temu odrzuciłeś. `/context` pokazuje okno zapełnione w ok. 80%.",
        "Zamiast się kłócić: „Zapisz notatki/stan.md: zrobione, decyzje (w tym: NIE używamy biblioteki X), następny krok”. Przeglądasz plik, poprawiasz jedną decyzję ręcznie.",
        "Commit stanu kodu (git), `/clear`.",
        "Nowa prośba z odwołaniem do stan.md. Agent pracuje zgodnie z decyzjami; `/context` — kilkanaście tysięcy tokenów.",
        "`/usage` — widzisz, ile okna 5-godzinnego zostało; planujesz resztę dnia."],
        "wynik": "Agent znów trzyma się ustaleń, koszt kolejnych wiadomości spadł kilkukrotnie, a decyzje są zapisane w repozytorium."},
    jak_uruchomic=["Claude Code: `/context`, `/usage`, `/clear`, `/compact`, `/model`.", "Codex: `/status`, `/new`, `/compact`, `/model`."],
    cwiczenia=[
        C("prowadzone",
          "Okno kontekstu ma 200 000 tokenów. `/context` pokazuje: instrukcje 4 000, pliki 56 000, rozmowa 100 000. (1) Ile tokenów jest zajętych? (2) Jaki to procent okna? "
          "(3) Po `/clear` i wczytaniu instrukcji oraz notatki stan.md (1 000 tokenów) — ile będzie zajęte? Czas: 15 minut.",
          "(1) 160 000; (2) 80%; (3) 5 000 (instrukcje 4 000 + notatka 1 000).",
          ["Zsumuj trzy części.", "Procent: zajęte / 200 000 × 100.", "Po /clear zostają tylko instrukcje + to, co wczytasz."],
          "4 000 + 56 000 + 100 000 = 160 000 = 80% okna. Po /clear: 4 000 instrukcji + 1 000 notatki = 5 000.",
          [li("zajete", "(1) Zajęte tokeny", 160000), li("proc", "(2) Procent okna", 80), li("po", "(3) Po /clear + notatka", 5000, bledy=[bl(1000, "instrukcje (CLAUDE.md/AGENTS.md) wczytują się w każdej sesji — 4 000 tokenów")])]),
        C("samodzielne",
          "Dobierz polecenie Claude Code: (1) kończysz zadanie o rabatach, zaczynasz niezwiązane — formularz; (2) w połowie dużego zadania kontekst ma 85%, chcesz zachować decyzje; "
          "(3) chcesz sprawdzić, ile limitu planu zostało; (4) proste zadanie — zmiana tekstu komunikatu; chcesz tańszy model. Opcje: /clear, /compact, /usage, /model. Czas: 15 minut.",
          "(1) /clear; (2) /compact; (3) /usage; (4) /model.",
          ["Niezwiązany temat — czysta kartka.", "W połowie zadania — streszczenie z zachowaniem decyzji.", "Limity i model mają własne polecenia."],
          "(1) /clear, (2) /compact (np. „/compact zachowaj decyzje”), (3) /usage, (4) /model.",
          [wy(f"p{i}", t, ["/clear", "/compact", "/usage", "/model"], w) for i, t, w in
           ((1, "(1) Nowy, niezwiązany temat", "/clear"), (2, "(2) 85% w połowie zadania", "/compact"), (3, "(3) Ile limitu zostało", "/usage"), (4, "(4) Tańszy model do prostego zadania", "/model"))]),
    ],
    typowe_bledy=[
        B("Agent „zapomina” ustalenia z początku sesji.", "Zapełnione okno — wcześniejsze fragmenty streszczone lub rozmyte.", "`/context`.", "Notatka stan.md + /clear; ważne decyzje do AGENTS.md."),
        B("Limit kończy się w 2 godziny.", "Długie sesje, ogólne prośby, mocny model do wszystkiego.", "`/usage`, `/context`.", "/clear między zadaniami, konkretne prośby, lżejszy model do prostych zmian."),
    ],
    pulapki=["/compact streszcza — streszczenie może zgubić szczegół. Decyzje ważne na dłużej zapisuj w plikach, nie licz na pamięć rozmowy.",
             "Wklejanie długich logów i całych plików do rozmowy zapycha kontekst — wskaż agentowi plik i fragment zamiast wklejać."],
    zadania=["Zmierz /context na początku i końcu sesji (zadanie tygodnia).", "Przećwicz notatkę stan.md i /clear.", "Zapisz w dzienniku stan /usage na koniec dnia przez 3 dni."],
    pytania=[["Dlaczego długa sesja kosztuje więcej?", "Bo przy każdej wiadomości wysyłana jest cała rozmowa z plikami i instrukcjami."],
             ["Czym różni się /clear od /compact?", "/clear czyści rozmowę; /compact zastępuje ją streszczeniem."], ["Co to jest notatka przekazania?", "Krótki plik ze stanem pracy, decyzjami i następnym krokiem, czytany na początku nowej sesji."]],
    podsumowanie="Mierzysz kontekst, czyścisz i streszczasz rozmowę, przekazujesz stan przez plik, dobierasz model i planujesz pracę pod okna limitów.",
    test=[T("Najtańsza praktyka według dokumentacji Claude Code:", ["Większy model", "/clear między niezwiązanymi zadaniami", "Dłuższe prośby", "Wklejanie całych plików"], 1, "Czysta kartka."),
          T("Polecenie pokazujące zajętość kontekstu w Claude Code:", ["/context", "/memory", "/status", "/tokens"], 0, "W Codex — /status."),
          T("Notatka przekazania powinna mieć:", ["Całą rozmowę", "Zrobione, decyzje, następny krok — krótko", "Hasła", "Kod wszystkich plików"], 1, "Maks. kilkanaście linii."),
          T("Gdzie zapisujesz decyzję ważną dla całego projektu?", ["W rozmowie", "W AGENTS.md lub specyfikacji", "Nigdzie", "W komentarzu na GitHubie"], 1, "Pliki przetrwają sesje.")],
    w_praktyce=["Każda sesja kończy się notatką stan.md albo commitem.", "Raz w tygodniu porównaj /usage z planem."],
    zrodla=[Z_CC_COSTS, Z_CX_SLASH, Z_CC_BEST],
)

GDY_MYLI = L(
    id="gdy_agent_sie_myli", nazwa="Gdy agent się myli: pętle, zmyślenia, „gotowe” bez dowodu", tydzien=7,
    slowa=["pętla", "zmyślenie", "dryf", "diagnoza", "test", "cofnięcie", "reguła trzech", "nadgorliwość"],
    cel="Po tej lekcji rozpoznajesz 6 typowych porażek agenta (pętla poprawek, zmyślone API, zmiana testów, dryf zakresu, fałszywe „gotowe”, nadgorliwość) i dla każdej znasz ruch naprawczy.",
    po_co="Badanie METR (2025) pokazało, że doświadczeni programiści z AI pracowali wolniej, m.in. przez czas na poprawianie i przeglądanie wyników. Szybkie rozpoznanie porażki to największa oszczędność czasu.",
    wymagania=["Lekcje „Przegląd zmian” i „Kontekst, limity…”.", "Plik zepsute_raporty.py z materiałów (zadanie tygodnia)."],
    wyjasnienie=(
        "## Sześć porażek i ruch naprawczy\n"
        "| porażka | jak ją poznać | ruch |\n"
        "|---|---|---|\n"
        "| pętla poprawek | ten sam błąd wraca po 2–3 poprawkach, agent przeprasza i próbuje „inaczej” | Esc → cofnij (/rewind lub git restore) → nowa sesja z opisem problemu i hipotezą |\n"
        "| zmyślone API / paczka | ImportError, AttributeError: module has no attribute…, paczki brak na pypi.org | każ użyć biblioteki standardowej albo pokaż fragment oficjalnej dokumentacji |\n"
        "| „naprawa” przez test | testy zielone, ale w diffie zmieniony plik test_* | przywróć test, zasada w AGENTS.md, ewentualnie reguła blokująca edycję folderu testów |\n"
        "| dryf zakresu | zmiany w plikach spoza zadania, nowe funkcje „przy okazji” | git restore tych plików, prośba z listą dozwolonych plików, tryb planu |\n"
        "| fałszywe „gotowe” | „Done! Wszystko działa” bez uruchomienia testów | „Pokaż wynik uruchomienia testów” / sam ✔ Sprawdź wynik |\n"
        "| nadgorliwość | dodaje logowanie, klasy, konfigurację, których nie potrzebujesz | „minimalna zmiana spełniająca test; bez nowych plików” |\n"
        "## Najpierw diagnoza, potem kod\n"
        "Gdy błąd jest uparty, zmień prośbę z „popraw” na „zdiagnozuj”: „Nie zmieniaj plików. Uruchom test, przeczytaj traceback, wypisz 3 możliwe przyczyny i jak sprawdzić każdą”. "
        "Potem wybierasz hipotezę i dopiero wtedy prosisz o jedną poprawkę. To zatrzymuje zgadywanie.\n"
        "## Daj agentowi czerwony test\n"
        "Najskuteczniejsza informacja dla agenta to test, który nie przechodzi, i polecenie do jego uruchomienia: „python -m pytest -q test_raporty.py::test_top_pokoje — napraw kod, nie test”. "
        "Agent sam uruchomi test po zmianie i zobaczy, czy się udało.\n"
        "## Reguła trzech (wersja dla agenta)\n"
        "Trzy nieudane próby na tym samym błędzie → stop. Commit tego, co działa, notatka stan.md z opisem problemu, `/clear`, nowa sesja — albo zmniejsz zadanie o połowę. "
        "Czasem najlepszy ruch to napisać jedną funkcję samodzielnie i dać agentowi resztę.\n"
        "## Twoja część winy\n"
        "Wiele porażek agenta zaczyna się od niejasnej specyfikacji. Po każdej porażce zapisz w dzienniku: czego brakowało w prośbie lub instrukcjach — i dopisz to do szablonu."),
    przyklad=kod("gdy_agent_sie_myli:przyklad",
                 "# Fragment z zepsute_raporty.py — trzy klasyczne błędy kodu od AI\n"
                 "def suma_przychodu(rezerwacje):\n    suma = 0\n    for r in rezerwacje:\n        suma =+ r[\"kwota\"]      # =+ zamiast +=\n    return suma\n\n"
                 "print(suma_przychodu([{\"kwota\": 100}, {\"kwota\": 250}]))\n",
                 "250\n"),
    demonstracja={"tytul": "Z pętli poprawek do diagnozy", "kroki": [
        "Zadanie: napraw top_pokoje w zepsute_raporty.py. Agent poprawia, test dalej czerwony; druga poprawka — inny błąd; trzecia — wraca pierwszy. To pętla.",
        "Esc. `git restore zepsute_raporty.py` (albo /rewind) — czysty stan.",
        "Nowa sesja: „Nie zmieniaj plików. Uruchom python -m pytest -q -k top i wypisz 3 możliwe przyczyny z traceback”. Agent: (1) sortowanie rosnąco zamiast malejąco, (2) remisy w złej kolejności, (3) n większe niż liczba pokoi.",
        "Sprawdzasz hipotezy na danych testu: przyczyny 1 i 2 się potwierdzają.",
        "Jedna prośba: „Sortuj malejąco po liczbie nocy, przy remisie alfabetycznie po nazwie pokoju. Tylko funkcja top_pokoje. Napraw kod, nie test. Uruchom test.” Zielono."],
        "wynik": "Zamiast czwartej losowej poprawki — diagnoza, dwie potwierdzone przyczyny i jedna trafna zmiana."},
    jak_uruchomic=["Zadanie tygodnia „zepsute_raporty.py” → przy uporczywym błędzie: prośba o diagnozę bez zmian w plikach."],
    cwiczenia=[
        C("prowadzone",
          "Co wypisze kod z przykładu lekcji (suma_przychodu z `=+`)? Jaka jest poprawna suma? Jak nazywa się ta porażka, jeśli agent przy „naprawie” zmieni w teście oczekiwaną wartość na wypisaną? "
          "Opcje: pętla poprawek, „naprawa” przez test, dryf zakresu, nadgorliwość. Czas: 15 minut.",
          "Wypisze 250 (`=+` przypisuje +kwotę, nie dodaje); poprawnie 350; „naprawa” przez test.",
          ["`suma =+ x` to `suma = +x` — przypisanie.", "Ostatnia kwota to 250.", "Zmiana oczekiwanej wartości w teście to…"],
          "`=+` zastępuje sumę ostatnią kwotą → 250; poprawnie 100 + 250 = 350. Zmiana testu pod wynik to „naprawa” przez test.",
          [li("wypisze", "Co wypisze?", 250, bledy=[bl(350, "to wynik POPRAWNEGO kodu; `=+` to przypisanie, nie dodawanie")]), li("suma", "Poprawna suma", 350),
           wy("porazka", "Nazwa porażki", ["pętla poprawek", "„naprawa” przez test", "dryf zakresu", "nadgorliwość"], "„naprawa” przez test")]),
        C("samodzielne",
          "Dopasuj ruch: (1) ImportError dla paczki, której nie ma na pypi.org; (2) czwarta poprawka tego samego błędu; (3) agent pisze „Done!”, nie uruchomił testów; (4) agent dodał 3 nowe pliki konfiguracyjne do prostej funkcji. "
          "Ruchy: stop i diagnoza w nowej sesji / biblioteka standardowa / „pokaż wynik testów” / minimalna zmiana bez nowych plików. Czas: 15 minut.",
          "(1) biblioteka standardowa; (2) stop i diagnoza w nowej sesji; (3) „pokaż wynik testów”; (4) minimalna zmiana bez nowych plików.",
          ["Zmyślona paczka — zastąp czymś, co istnieje.", "Reguła trzech.", "Deklaracja bez dowodu."],
          "(1) standardowa biblioteka, (2) stop + diagnoza, (3) dowód z testów, (4) minimalna zmiana.",
          [wy(f"r{i}", t, ["stop i diagnoza w nowej sesji", "biblioteka standardowa", "„pokaż wynik testów”", "minimalna zmiana bez nowych plików"], w) for i, t, w in
           ((1, "(1) Nieistniejąca paczka", "biblioteka standardowa"), (2, "(2) Czwarta poprawka", "stop i diagnoza w nowej sesji"),
            (3, "(3) „Done!” bez testów", "„pokaż wynik testów”"), (4, "(4) 3 pliki konfiguracji", "minimalna zmiana bez nowych plików"))]),
    ],
    typowe_bledy=[
        B("„AttributeError: module 'csv' has no attribute 'read_table'”.", "Zmyślona funkcja w prawdziwym module.", "docs.python.org → csv: lista funkcji.", "Pokaż agentowi właściwą funkcję (csv.DictReader) albo każ sprawdzić dokumentację."),
        B("Agent mówi, że test „ma błąd” i proponuje go zmienić.", "Agent optymalizuje „zielony wynik”, nie poprawność.", "Czy test zgadza się ze specyfikacją?", "Jeśli tak — „napraw kod, nie test”; jeśli test naprawdę jest zły — zmieniasz go Ty, świadomie."),
    ],
    pulapki=["Przeprosiny agenta („Masz rację, przepraszam!”) nie są poprawką. Patrz na diff i test.",
             "Nie każ agentowi „spróbować jeszcze raz” bez nowej informacji — dostaniesz losową odmianę tego samego."],
    zadania=["Napraw zepsute_raporty.py z agentem (zadanie tygodnia), stosując diagnozę przy uporczywym błędzie.", "Zapisz w dzienniku, która z 6 porażek Ci się przydarzyła.", "Dopisz do AGENTS.md jedną zasadę wynikającą z porażki."],
    pytania=[["Czym różni się prośba „zdiagnozuj” od „popraw”?", "Diagnoza nie zmienia plików — daje hipotezy i sposób sprawdzenia; poprawka przychodzi po wyborze hipotezy."],
             ["Co robisz po trzeciej nieudanej poprawce?", "Stop: commit tego, co działa, notatka stanu, nowa sesja albo mniejsze zadanie."],
             ["Jaka informacja najbardziej pomaga agentowi?", "Czerwony test z poleceniem uruchomienia i zasadą „napraw kod, nie test”."]],
    podsumowanie="Rozpoznajesz 6 porażek agenta, przechodzisz z pętli poprawek do diagnozy, dajesz agentowi czerwony test i stosujesz regułę trzech.",
    test=[T("Ten sam błąd wraca po 3 poprawkach. Ruch:", ["Czwarta poprawka", "Stop, cofnięcie, diagnoza w nowej sesji", "Większy model bez zmian prośby", "Usunięcie testu"], 1, "Reguła trzech."),
          T("„Done!” bez wyniku testów to:", ["Dowód", "Fałszywe „gotowe” — poproś o wynik lub sprawdź sam", "Błąd składni", "Limit planu"], 1, "Deklaracja to nie dowód."),
          T("ImportError dla paczki spoza pypi.org sugeruje:", ["Brak internetu", "Zmyśloną zależność", "Złą wersję Windows", "Błąd Gita"], 1, "Halucynacja paczki."),
          T("Najlepsza informacja zwrotna dla agenta:", ["„Źle”", "Czerwony test z poleceniem uruchomienia", "Zrzut ekranu pulpitu", "„Postaraj się”"], 1, "Agent sam sprawdzi poprawkę.")],
    w_praktyce=["Przy uporczywym błędzie — zawsze najpierw diagnoza.", "Zasady z porażek trafiają do AGENTS.md."],
    zrodla=[Z_CC_BEST, Z_CC_CHECK, ["METR (2025): badanie RCT — doświadczeni programiści z AI 19% wolniej (omówienie DX)", "https://getdx.com/blog/metr-study-on-how-ai-affects-developer-productivity/", D]],
)

POWTORKA_1 = L(
    id="powtorka_etap_1", nazwa="Powtórka etapu 1 i mini-projekt z agentem: kalendarz dostępności", tydzien=7,
    slowa=["powtórka", "kalendarz", "dostępność", "daty", "nakładanie", "mini-projekt", "etap 1"],
    cel="Po tej lekcji prowadzisz agenta przez mały projekt od specyfikacji, przez plan i małe kroki, do commitów na GitHubie — i oceniasz gotowość do budowania aplikacji.",
    po_co="Etap 2 to większe aplikacje (strona, Flask, baza). Bez nawyku plan → krok → test → przegląd → commit będą się sypać.",
    wymagania=["Wszystkie lekcje tygodni 4–7.", "Repozytorium pod-lipa na GitHubie."],
    wyjasnienie=(
        "## Lista kontrolna etapu 1\n"
        "| umiejętność | sprawdzian |\n"
        "|---|---|\n"
        "| narzędzie | agent zainstalowany (albo ścieżka bez konta), znasz tryby i /rewind |\n"
        "| instrukcje | AGENTS.md + CLAUDE.md z @AGENTS.md, krótkie i aktualne |\n"
        "| małe kroki | plan w punktach, jedna zmiana, test po każdej |\n"
        "| Git/GitHub | commit po każdym zielonym kroku, push, .gitignore z .env |\n"
        "| przegląd | lista 8 pytań przed commitem |\n"
        "| kontekst | /context, /clear, notatka stan.md |\n"
        "| porażki | diagnoza zamiast pętli, reguła trzech |\n"
        "## Mini-projekt: kalendarz.py\n"
        "Gospodarstwo ma 3 pokoje: Lipowy, Dębowy, Klonowy. Rezerwacja to słownik `{\"pokoj\": \"Lipowy\", \"od\": \"2026-12-20\", \"do\": \"2026-12-23\"}` — daty jako napisy RRRR-MM-DD, `do` to dzień wyjazdu (noc z 22 na 23 jest ostatnia; tego dnia pokój może przyjąć nowego gościa).\n"
        "- `noce(od, do)` → liczba nocy; do ≤ od → ValueError.\n"
        "- `koliduje(a, b)` → True, gdy dwie rezerwacje tego samego pokoju nakładają się (wyjazd w dniu przyjazdu następnej NIE jest kolizją).\n"
        "- `czy_wolny(rezerwacje, pokoj, od, do)` → True, gdy pokój wolny w całym okresie.\n"
        "- `wolne_pokoje(rezerwacje, od, do)` → lista wolnych pokoi w kolejności Lipowy, Dębowy, Klonowy.\n"
        "Moduł `datetime` (wbudowany) zamienia napis na datę: `date.fromisoformat(\"2026-12-20\")`; różnica dat `.days` to liczba nocy.\n"
        "## Proces (to jest sprawdzian, nie tylko kod)\n"
        "- Tryb planu → plan 4 punktów → commit po każdym punkcie (min. 4 commity).\n"
        "- Lista 8 pytań przed każdym commitem.\n"
        "- push na GitHub; w dzienniku: liczba iteracji, porażki agenta, zasady dopisane do AGENTS.md.\n"
        "Bez konta: zapis pracy agenta w przyklady/odpowiedzi_agenta/v7z3.md (z jednym błędem) — znajdź błąd testem, popraw, zrób te same commity."),
    przyklad=kod("powtorka_etap_1:przyklad",
                 "from datetime import date\n\nod = date.fromisoformat(\"2026-12-20\")\ndo = date.fromisoformat(\"2026-12-23\")\nprint((do - od).days)\n"
                 "# nakładanie przedziałów [od, do): a.od < b.do and b.od < a.do\n"
                 "print(date(2026, 12, 20) < date(2026, 12, 25) and date(2026, 12, 23) < date(2026, 12, 23))\n",
                 "3\nFalse\n"),
    demonstracja={"tytul": "Przypadki brzegowe kolizji — test w głowie przed agentem", "kroki": [
        "A: Lipowy 20–23.12, B: Lipowy 23–25.12. Wyjazd A = przyjazd B → nie kolizja (a.od < b.do: 20 < 25 prawda; b.od < a.do: 23 < 23 fałsz → False).",
        "C: Lipowy 22–24.12 vs A → kolizja (20 < 24 i 22 < 23).",
        "D: Dębowy 20–23.12 vs A → inny pokój — nie kolizja (warunek pokoju sprawdzasz pierwszy!).",
        "E: Lipowy 18–26.12 vs A (obejmuje całą A) → kolizja.",
        "Te 4 przypadki wpisujesz do specyfikacji przed prośbą do agenta. Jeśli agent użyje <= zamiast <, przypadek A–B to wyłapie."],
        "wynik": "Masz 4 przypadki brzegowe kolizji, które obejmują typowe błędy: <= zamiast <, brak sprawdzenia pokoju, przedział obejmujący."},
    jak_uruchomic=["Zadanie tygodnia „kalendarz.py” → tryb planu → kroki → „✔ Sprawdź wynik” → commity → push."],
    cwiczenia=[
        C("prowadzone",
          "Policz: (1) noce(\"2026-12-28\", \"2027-01-02\"), (2) czy koliduje Lipowy 20–23.12 z Lipowy 23–25.12 (tak/nie), (3) czy koliduje Lipowy 20–23.12 z Lipowy 21–22.12 (tak/nie). Czas: 15 minut.",
          "(1) 5 nocy; (2) nie; (3) tak.",
          ["Grudzień ma 31 dni: 28→29→30→31→1→2.", "Wyjazd w dniu przyjazdu to nie kolizja.", "21–22 leży w środku 20–23."],
          "28.12–2.01 = 5 nocy (przez Sylwestra); 20–23 i 23–25 — brak kolizji; 21–22 wewnątrz 20–23 — kolizja.",
          [li("noce", "(1) Liczba nocy", 5, bledy=[bl(4, "policz noce: 28/29, 29/30, 30/31, 31/1, 1/2 — pięć")]), wy("k1", "(2) Kolizja 20–23 i 23–25?", TN, "nie"), wy("k2", "(3) Kolizja 20–23 i 21–22?", TN, "tak")]),
        C("samodzielne",
          "Samoocena procesu. Policz, ile commitów minimum wymaga mini-projekt (plan ma 4 punkty, commit po każdym). Który plik sprawdzisz na GitHubie, by upewnić się, że nie wysłałeś tajemnic (nazwa pliku z kluczami, której NIE powinno tam być)? "
          "I wynik `wolne_pokoje` dla rezerwacji [Lipowy 20–23.12] w okresie 21–22.12 — ile pokoi jest wolnych? Czas: 15 minut.",
          "Minimum 4 commity; plik .env (nie może go być); 2 wolne pokoje (Dębowy, Klonowy).",
          ["Commit po każdym z 4 punktów.", "Tajemnice trzymasz w pliku, który jest w .gitignore.", "Lipowy zajęty, pozostałe dwa wolne."],
          "4 commity; .env nie może być w repozytorium; wolne: Dębowy i Klonowy = 2.",
          [li("commity", "Minimalna liczba commitów", 4), tx("plik", "Plik, którego nie może być w repo", [".env", "env"]), li("wolne", "Ile pokoi wolnych?", 2)]),
    ],
    typowe_bledy=[
        B("Wyjazd w dniu przyjazdu wykrywany jako kolizja.", "<= zamiast < w warunku nakładania.", "Przypadek A–B z demonstracji.", "Warunek przedziałów półotwartych: a.od < b.do and b.od < a.do."),
        B("Kolizja między różnymi pokojami.", "Brak sprawdzenia pokoju.", "Przypadek A–D.", "Najpierw: jeśli pokoje różne → False."),
        B("„TypeError: '<' not supported between instances of 'str' and 'datetime.date'”.", "Porównanie napisu z datą.", "Typy zmiennych w warunku.", "Zamieniaj napisy na daty date.fromisoformat() na początku funkcji."),
    ],
    pulapki=["Porównywanie dat jako napisów „RRRR-MM-DD” przypadkiem działa, ale „2026-12-5” (bez zera) już nie — zawsze konwertuj na date.",
             "Mini-projekt ocenia też proces: 1 commit z całością = proces niezaliczony, nawet przy zielonych testach."],
    zadania=["Zbuduj kalendarz.py z agentem w 4 krokach i 4 commitach.", "Samoocena etapu 1 (zadanie tygodnia).", "Quiz tygodnia 7."],
    pytania=[["Kiedy dwie rezerwacje tego samego pokoju kolidują?", "Gdy a.od < b.do i b.od < a.do (wyjazd w dniu przyjazdu nie koliduje)."],
             ["Dlaczego daty konwertujesz na obiekty date?", "Żeby poprawnie porównywać i liczyć różnice, niezależnie od zapisu napisu."], ["Co sprawdza mini-projekt poza kodem?", "Proces: plan, małe kroki, commity po każdym kroku, przegląd, push."]],
    podsumowanie="Zbudowałeś z agentem moduł z datami i przypadkami brzegowymi, w małych krokach z commitami — i oceniłeś gotowość do etapu aplikacji.",
    test=[T("Rezerwacje Lipowy 10–12 i Lipowy 12–15:", ["Kolidują", "Nie kolidują", "Błąd", "Zależy od godziny"], 1, "Wyjazd w dniu przyjazdu."),
          T("noce(\"2026-12-30\", \"2027-01-01\") to:", ["1", "2", "3", "Błąd"], 1, "30/31 i 31/1."),
          T("Minimalny proces mini-projektu to:", ["Jeden commit", "Plan, kroki z testem, commit po każdym, push", "Tylko testy", "Tylko kod"], 1, "Proces jest częścią zaliczenia.")],
    w_praktyce=["Przedziały dat zawsze półotwarte [od, do).", "Przypadki brzegowe przed prośbą do agenta."],
    zrodla=[["Python — datetime: date.fromisoformat (oficjalna dokumentacja)", "https://docs.python.org/3/library/datetime.html#datetime.date.fromisoformat", D], Z_CC_BEST, Z_GIT_BOOK],
)
