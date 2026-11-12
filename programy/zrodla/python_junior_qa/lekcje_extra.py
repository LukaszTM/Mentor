# -*- coding: utf-8 -*-
"""
Lekcje tygodnia 0 (konfiguracja od zera) + mini-testy (3 pytania A–D) do każdej lekcji programu.
TESTY: klucz = id lekcji (z wiedza.TEMATY lub stąd). Używane przy ręcznym wpisie czasu nauki i w zakładce Lekcje.
"""

LEKCJE_TYDZIEN_0 = [
    {"id": "start_jak_sie_uczyc", "tydzien": 0, "czas_min": 15,
     "nazwa": "Start: jak uczyć się z tego programu (przeczytaj najpierw)",
     "cel": "wiesz, co robić każdego dnia, gdzie co jest w Mentorze, jak czytać lekcję i jak odhaczać postępy.",
     "slowa": ["jak zacząć", "jak zaczac", "od czego zacząć", "start", "wprowadzeni", "jak się uczyć", "jak sie uczyc", "jak działa program", "mentor"],
     "wyjasnienie":
         "## Co to za program i dla kogo\n"
         "13 tygodni (0–12): Python od zera, Git, testy automatyczne (pytest, Selenium) i projekt portfolio na GitHubie — pod rolę Junior QA. "
         "Zaczynasz bez żadnej wiedzy o programowaniu; potrzebujesz komputera z Windows/macOS/Linux, 90 minut dziennie i cierpliwości na pierwsze dwa tygodnie, "
         "gdy wszystko jest nowe (pliki .py, uruchamianie, commit). Pythona i biblioteki przygotowuje Mentor (zakładka Środowisko) — nie musisz niczego szukać ani instalować z terminala. "
         "Uczysz się z asystentem AI na zasadzie 70/30: 70% kodu piszesz sam.\n"
         "## Jak wygląda dzień nauki\n"
         "- Panel → karta „Dzisiaj”: Mentor pokazuje zadanie dnia i lekcję do niego (pon–czw zadania 1–4, piątek — zadanie tygodnia, sobota — quiz, niedziela — wolne).\n"
         "- Lekcje → czytasz lekcję dnia (15–25 min): cel, wyjaśnienie, przykład kodu, pułapki, 3 zadania, pytania, test.\n"
         "- Plan → zadanie dnia → rozwijasz „Jak to zrobić”: kompletne kroki (jak nazwać plik, co wpisać, jak sprawdzić, że działa). Pod zadaniem z plikiem .py jest pasek "
         "„Ćwiczenie w Mentorze”: Utwórz plik ćwiczenia → ▶ Uruchom → ✔ Sprawdź wynik — kod uruchamia się przyciskiem, bez terminala, a wynik sprawdza test zadania.\n"
         "- Sesja nauki → timer 4 faz: nowy temat 20 min → kodowanie 50 → recenzja 15 → podsumowanie 5; sam zapisuje czas i serię.\n"
         "- Plan → ✔ przy zadaniu, gdy kod działa i jest w commicie (+10 XP; zadanie tygodnia +25). Zadania z testem odhaczają się same po „Sprawdź wynik”; "
         "bez testu Mentor mówi „Plik istnieje — wymaga sprawdzenia” i odhaczasz sam. Dziennik → zdanie, czego się nauczyłeś (+3 XP).\n"
         "- Sobota: Quiz tygodnia. Po każdym etapie: Checklista — co masz umieć.\n"
         "## Twój warsztat: Środowisko i katalog roboczy\n"
         "Zakładka Środowisko: Mentor sprawdza, czy Python, biblioteki (pytest, requests, selenium, flask), Git i przeglądarka naprawdę działają, i instaluje brakujące za Twoją zgodą "
         "— do osobnego środowiska kursu, bez uprawnień administratora. „Gotowe” pojawia się dopiero, gdy testy końcowe przejdą.\n"
         "Katalog roboczy (Mój projekt → „Utwórz katalog roboczy kursu”, domyślnie Dokumenty\\Mentor\\python-junior-qa\\PRACA, albo własny „nauka-python”): tam są wszystkie pliki .py, "
         "CLAUDE.md z zasadami pracy asystenta i repozytorium Git. Mentor wykrywa pliki z zadań i pokazuje liczbę commitów — to Twój dowód postępu.\n"
         "## Jak czytać lekcję (5 kroków)\n"
         "- 1. Cel — jeśli już to umiesz, od razu test.\n"
         "- 2. Wyjaśnienie — czytaj z otwartym edytorem i przepisuj (nie kopiuj!) fragmenty kodu, uruchamiaj je (▶ Uruchom w Mentorze albo python plik.py).\n"
         "- 3. Przykład — zanim przeczytasz do końca, zgadnij, co wypisze; potem uruchom i porównaj.\n"
         "- 4. Pułapki — zapisz w dzienniku; to błędy, które każdy robi w pierwszym miesiącu.\n"
         "- 5. Zadania (w katalogu projektu, bez rozwiązań), pytania na głos, test 3 pytań (2/3 zalicza).\n"
         "## Asystent — nauczyciel, nie wykonawca\n"
         "Trzy karty: Subskrypcja (Claude Code w terminalu — pełny model, czyta Twoje pliki), API (własny klucz), Offline (wbudowany: „uczę się pętli”, "
         "„przejrzyj @plik.py”, „utknąłem… błąd: …”, „uruchom @plik.py”, „zadaj mi 3 pytania”, „quiz z tygodnia 2”). Zasada: 15 minut własnej walki, potem "
         "prośba o podpowiedź, nie o rozwiązanie; każdy kod od asystenta przepisujesz ręcznie. Gotowe prompty — zakładka Prompty.\n"
         "## Jeśli coś nie idzie\n"
         "- Nie wiesz, co dziś robić → Panel → „Dzisiaj”.\n"
         "- Błąd, którego nie rozumiesz → skopiuj ostatnią linię (np. „TypeError: …”) do Asystenta: „utknąłem: [błąd]” — wytłumaczy, nie poprawi.\n"
         "- Brak czasu → Ustawienia → skala sesji 50%; wpis ręczny czasu z testem. 30 minut dziennie bije 3 godziny w weekend.\n"
         "- Przerwa → Panel pokaże, ile dni minęło; XP i odznaki zostają, seria rusza od nowa.",
     "przyklad":
         "Dzień 1 (tydzień 0):\n"
         "1. Panel → „Dzisiaj”: „Środowisko kursu w Mentorze + Git”.\n"
         "2. Lekcje → ta lekcja → test.  3. Plan → tydzień 0 → zadanie 1 → „Jak to zrobić”: Środowisko → Sprawdź ponownie → Zainstaluj brakujące → zgoda → Git z git-scm.com.\n"
         "4. Sesja nauki → start timera.  5. Plan → ✔ (+10 XP).  6. Dziennik: „Mentor pobrał Pythona i biblioteki; Git zainstalowałem sam; nie rozumiem jeszcze, co to .venv”.",
     "zadania": ["Otwórz każdą zakładkę w pasku bocznym (także Środowisko) i zapisz w dzienniku jednym zdaniem, do czego służy.",
                 "Ustaw imię i katalog roboczy (Mój projekt → „Utwórz katalog roboczy kursu”); sprawdź, czy Mentor go widzi.",
                 "Uruchom Sesję nauki na 2 minuty i zatrzymaj — zobacz na Panelu zapisany czas."],
     "pytania": [["Gdzie sprawdzisz, co masz dziś zrobić?", "Panel → „Dzisiaj”: zadanie, „Jak to zrobić” i lekcja."],
                 ["Co oznacza zasada 70/30?", "70% czasu piszę kod sam, 30% rozmawiam z asystentem o tym, co napisałem."],
                 ["Kiedy odhaczasz zadanie?", "Gdy kod działa (uruchomiony — „▶ Uruchom” lub terminal) i jest w commicie — nie po przeczytaniu. Zadania z testem odhacza „Sprawdź wynik”."]],
     "pulapki": ["Kopiowanie kodu od asystenta zamiast przepisywania — po tygodniu nie umiesz napisać pętli bez pomocy.",
                 "Czytanie lekcji bez uruchamiania przykładów — Python uczy się palcami, nie oczami."],
     "test": [
         {"p": "Ile zadań ma tydzień i które jest „zadaniem tygodnia”?", "o": ["3 — ostatnie", "5 — piąte (piątek), +25 XP", "7", "Zależy od tygodnia"], "odp": 1, "w": "Zadania 1–4 pon–czw, 5 — piątek."},
         {"p": "Gdzie jest kompletna instrukcja wykonania zadania?", "o": ["W lekcji", "Plan → zadanie → „Jak to zrobić”", "W Ściądze", "W Quizie"], "odp": 1, "w": "Lekcja tłumaczy temat, Plan mówi, co zrobić."},
         {"p": "Co robisz z kodem, który pokazał asystent?", "o": ["Kopiuję do pliku", "Przepisuję ręcznie i tłumaczę sobie każdą linię", "Ignoruję", "Wysyłam do Gita"], "odp": 1, "w": "Zasada z CLAUDE.md i rytmu dnia."},
     ]},
    {"id": "terminal", "tydzien": 0, "nazwa": "Terminal i katalogi — pierwsze kroki",
     "slowa": ["terminal", "powershell", "cd ", "pwd", "katalog", "folder", "ścieżk", "sciezk"],
     "wyjasnienie":
         "Terminal to okno, w którym rozmawiasz z komputerem tekstem: wpisujesz komendę, naciskasz Enter, komputer odpowiada. "
         "Na Windows otwierasz go tak: Start → wpisz „PowerShell” → Enter. Zobaczysz ścieżkę, np. C:\\Users\\Lukasz> — to katalog roboczy, "
         "czyli folder, w którym terminal „stoi”. Wszystko, co uruchamiasz, dzieje się w tym folderze.\n"
         "Trzy komendy wystarczą na początek: pwd (gdzie jestem), ls (co tu jest — lista plików), cd nazwa (wejdź do folderu; cd .. — wyjdź poziom wyżej). "
         "Klawisz Tab dopełnia nazwy — wpisz „cd Doc” i Tab → „cd Documents”. Strzałka w górę przywołuje poprzednią komendę. Ctrl+C przerywa program, który się zapętlił.\n"
         "Terminal w PyCharm (zakładka Terminal na dole) to to samo okno, tylko otwarte od razu w folderze projektu. W Mentorze: Mój projekt → „Otwórz terminal tutaj” — "
         "otwiera się w katalogu roboczym i ma na początku PATH Pythona z zakładki Środowisko, więc  python plik.py  i  pytest  działają od razu.\n"
         "W tygodniach 0–3 terminal nie jest konieczny: przycisk „▶ Uruchom” pod zadaniem robi dokładnie to, co komenda python plik.py. Od tygodnia 4 (Git) terminal staje się codziennym narzędziem — dlatego ćwiczysz go już teraz.",
     "przyklad":
         "PS C:\\Users\\Lukasz> cd Documents\n"
         "PS C:\\Users\\Lukasz\\Documents> ls\n"
         "    nauka-python\n"
         "PS C:\\Users\\Lukasz\\Documents> cd nauka-python\n"
         "PS C:\\Users\\Lukasz\\Documents\\nauka-python> python hello.py\n"
         "Cześć, tu Łukasz\n"
         "PS ...> cd ..        # wracasz do Documents",
     "zadania": ["Otwórz PowerShell, wejdź do Dokumentów (cd Documents), wypisz zawartość (ls), wróć (cd ..). Powtórz 3 razy bez patrzenia w notatki.",
                 "Utwórz folder z terminala: mkdir proba, wejdź do niego, sprawdź pwd, wyjdź, usuń: rmdir proba.",
                 "Mój projekt → „Otwórz terminal tutaj” → sprawdź pwd (czy to katalog roboczy?) i python --version (czy to Python z zakładki Środowisko?)."],
     "pytania": [("Co pokazuje komenda pwd?", "Katalog roboczy — folder, w którym terminal teraz stoi."),
                 ("Jak wyjść o jeden folder wyżej?", "cd .."),
                 ("Co robi klawisz Tab w terminalu?", "Dopełnia nazwę pliku lub folderu.")],
     "pulapki": ["Nazwy ze spacjami ujmuj w cudzysłów: cd \"Moje pliki\".", "Terminal otwarty PRZED instalacją Pythona nie widzi nowego PATH — zamknij i otwórz nowy."],
     "test": [
         {"p": "Co to jest katalog roboczy?", "o": ["Folder z Pythonem", "Folder, w którym terminal aktualnie stoi i w którym uruchamia komendy", "Folder Dokumenty", "Pulpit"],
          "odp": 1, "w": "Komendy (np. python plik.py) szukają plików w katalogu roboczym."},
         {"p": "Jak wejść do folderu nauka-python?", "o": ["open nauka-python", "cd nauka-python", "go nauka-python", "run nauka-python"],
          "odp": 1, "w": "cd = change directory."},
         {"p": "Co zrobić, gdy program w terminalu się zapętlił?", "o": ["Zamknąć komputer", "Nacisnąć Ctrl+C", "Czekać", "Wpisać stop"],
          "odp": 1, "w": "Ctrl+C przerywa bieżący program."},
     ]},

    {"id": "instalacja", "tydzien": 0, "nazwa": "Narzędzia: środowisko kursu w Mentorze, Git, edytor, Claude Code",
     "slowa": ["instal", "środowisko", "srodowisko", "venv", "python.org", "path", "pycharm", "git-scm", "claude doctor", "wersj", "zainstaluj brakujące"],
     "wyjasnienie":
         "Do kursu potrzebujesz czterech rzeczy, ale tylko jedną instalujesz sam. PYTHON — interpreter, czyli program, który czyta Twoje pliki .py i je wykonuje; bez niego kod to tylko tekst. "
         "BIBLIOTEKI — gotowe moduły (pytest, requests, selenium, flask), których użyjesz od tygodnia 5. GIT — dziennik zmian w projekcie i most do GitHuba. "
         "EDYTOR — Notatnik wystarczy na start; PyCharm/VS Code kolorują kod, podpowiadają i mają terminal. CLAUDE CODE — asystent w terminalu (wymaga płatnego planu; bez niego używasz zakładki Asystent).\n"
         "Pythona i biblioteki przygotowuje MENTOR: zakładka Środowisko sprawdza, co naprawdę działa (uruchamia python --version, importuje biblioteki, pyta git --version — nie wierzy samej liście PATH), "
         "pokazuje plan instalacji (co, skąd, ile MB) i po Twojej zgodzie tworzy OSOBNE środowisko kursu (.venv) w katalogu Twojego użytkownika, bez uprawnień administratora. "
         "Gdy w systemie nie ma Pythona, pobiera oficjalną wersję 3.12 tylko dla kursów. Na końcu uruchamia testy: interpreter, importy, przykładowy pytest, lokalne API — dopiero wtedy mówi „Gotowe”.\n"
         "Dlaczego osobne środowisko? Bo biblioteki różnych projektów nie mogą się mieszać (poznasz to w tygodniu 5 jako venv). Python „z Windows Store” to tylko skrót — Mentor go pomija.\n"
         "Git instalujesz sam z git-scm.com (domyślne ustawienia). Sprawdzasz tak samo jak wszystko: Środowisko → „Sprawdź ponownie” → GOTOWE z numerem wersji. "
         "PATH to lista folderów, w których Windows szuka programów wpisywanych w terminalu; Mentor nie potrzebuje PATH, bo zna pełne ścieżki — ale terminal już tak, dlatego nowo zainstalowany program widać dopiero w NOWYM oknie terminala.",
     "przyklad":
         "Zakładka Środowisko po „Sprawdź ponownie” na czystym komputerze:\n"
         "  BRAK     Python                — Mentor może pobrać Python 3.12 do swojego katalogu\n"
         "  BRAK     Środowisko kursu (.venv)\n"
         "  BRAK     pytest · requests · selenium · flask\n"
         "  BRAK     Git (od tygodnia 0)   — oficjalny instalator: git-scm.com\n"
         "  OPCJON.  Microsoft Edge (Selenium od tygodnia 8)\n"
         "„Zainstaluj brakujące” → plan: Python 3.12 (46 MB, github.com/astral-sh), .venv (15 MB), biblioteki z PyPI (15–25 MB), testy → Tak.\n"
         "Po kilku minutach: GOTOWE przy Pythonie, .venv i bibliotekach; testy zielone; Git nadal BRAK — instalujesz sam → Sprawdź ponownie → GOTOWE.",
     "zadania": ["Zakładka Środowisko → „Sprawdź ponownie” → zapisz w dzienniku, co było BRAK. Potem „Zainstaluj brakujące” i przeczytaj plan, zanim klikniesz Tak.",
                 "Zainstaluj Git z domyślnymi ustawieniami; Środowisko → „Sprawdź ponownie” → numer wersji Gita.",
                 "Mój projekt → „Otwórz terminal tutaj” → python --version i git --version — porównaj z tym, co pokazuje zakładka Środowisko."],
     "pytania": [("Dlaczego Mentor uruchamia programy, zamiast patrzeć na PATH?", "Bo wpis w PATH nie gwarantuje, że program działa (np. skrót ze Store); dopiero python --version z wynikiem to dowód."),
                 ("Co to jest środowisko kursu (.venv)?", "Osobny folder z Pythonem i bibliotekami tylko dla tego kursu — nie miesza się z innymi projektami ani z systemem."),
                 ("Kiedy Mentor pokazuje „Gotowe”?", "Dopiero gdy testy końcowe (interpreter, importy, pytest, API) przejdą — nie po samej instalacji.")],
     "pulapki": ["Python ze Sklepu Windows to skrót, nie interpreter — Mentor go pomija; pozwól mu pobrać własnego.",
                 "Git zainstalowany, a Mentor dalej BRAK → „Sprawdź ponownie”, w ostateczności zamknij i otwórz Mentora.",
                 "Claude Code bez planu Pro/Max nie zaloguje się — to nie błąd instalacji; użyj Asystenta Offline/API."],
     "test": [
         {"p": "Kto instaluje Pythona i biblioteki kursu?", "o": ["Ty, z python.org, zaznaczając PATH", "Mentor — zakładka Środowisko → „Zainstaluj brakujące”, po Twojej zgodzie", "PyCharm", "GitHub"],
          "odp": 1, "w": "Mentor pokazuje plan, pobiera oficjalne pliki i tworzy osobne środowisko kursu; Ty instalujesz tylko Git (i opcjonalnie edytor, Claude Code)."},
         {"p": "Co oznacza status GOTOWE przy Pythonie w zakładce Środowisko?", "o": ["Jest wpis w PATH", "Mentor naprawdę uruchomił interpreter i dostał numer wersji zgodny z wymaganiem kursu", "Python jest w Sklepie Windows", "Nic"],
          "odp": 1, "w": "Statusy pochodzą z realnych uruchomień, nie z listy PATH."},
         {"p": "Jak sprawdzić, czy Git jest zainstalowany?", "o": ["Środowisko → „Sprawdź ponownie” (albo git --version w nowym terminalu)", "Otworzyć GitHub", "Szukać folderu Git", "Uruchomić PyCharm"],
          "odp": 0, "w": "Każde narzędzie: realne uruchomienie z numerem wersji."},
     ]},

    {"id": "git_start", "tydzien": 0, "nazwa": "Git i GitHub — pierwszy commit i push",
     "slowa": ["git init", "pierwszy commit", "github", "push", "remote", "origin", "repozytorium"],
     "wyjasnienie":
         "Git to dziennik zmian: w dowolnej chwili robisz „zdjęcie” wszystkich plików projektu z podpisem (commit) i możesz do niego wrócić. GitHub to serwer, "
         "na który wysyłasz te zdjęcia (push) — kopia zapasowa i Twoje portfolio w jednym. Rekruter będzie oglądał właśnie to.\n"
         "Cykl, który będziesz powtarzał codziennie: git status (co się zmieniło) → git add . (zaznacz wszystko do zdjęcia) → git commit -m \"dzień N: temat\" (zrób zdjęcie z podpisem) → git push (wyślij na GitHub). "
         "Jednorazowo na początku: git init (zamień folder w repozytorium), git remote add origin adres (powiedz Gitowi, gdzie jest GitHub), git push -u origin main (pierwszy push z zapamiętaniem adresu).\n"
         "Opis commita pisz tak, żebyś za miesiąc wiedział, co tam jest: „dzień 7: słowniki i funkcja usun” zamiast „zmiany”.",
     "przyklad":
         "git init\ngit add .\ngit commit -m \"dzień 1: hello.py\"\n"
         "git remote add origin https://github.com/LukaszTM/nauka-python.git\n"
         "git branch -M main\ngit push -u origin main\n"
         "# i codziennie:\ngit add .\ngit commit -m \"dzień 2: zmienne\"\ngit push",
     "zadania": ["Zrób pierwszy commit w nauka-python i sprawdź git log --oneline.",
                 "Utwórz repozytorium na GitHubie (bez README) i wypchnij projekt — zobacz pliki w przeglądarce.",
                 "Zmień coś w hello.py, zrób drugi commit i push; odśwież GitHub — czy widać zmianę i dwa commity?"],
     "pytania": [("Jaka jest różnica między commit a push?", "Commit zapisuje zdjęcie lokalnie; push wysyła je na GitHub."),
                 ("Co robi git add .?", "Zaznacza wszystkie zmienione pliki do następnego commita."),
                 ("Po co git status?", "Żeby zobaczyć, co jest zmienione i co nie trafiło jeszcze do commita.")],
     "pulapki": ["„Please tell me who you are” → git config --global user.name i user.email.", "Commit bez git add jest pusty.", "Zaznaczenie „Add README” na GitHubie przy tworzeniu repo → konflikt przy pierwszym pushu."],
     "test": [
         {"p": "W jakiej kolejności wykonujesz codzienny cykl?", "o": ["push → commit → add", "add → commit → push", "commit → add → push", "init → push"],
          "odp": 1, "w": "Zaznacz (add), zrób zdjęcie (commit), wyślij (push)."},
         {"p": "Co robi git init?", "o": ["Wysyła pliki na GitHub", "Zamienia folder w repozytorium Git (tworzy ukryty .git)", "Instaluje Gita", "Usuwa historię"],
          "odp": 1, "w": "Robisz to raz na projekt."},
         {"p": "Który opis commita jest dobry?", "o": ["\"zmiany\"", "\"asdf\"", "\"dzień 4: litry.py — progi cenowe if/elif\"", "\"commit\""],
          "odp": 2, "w": "Opis ma mówić, co jest w środku."},
     ]},

    {"id": "nauka_z_asystentem", "tydzien": 0, "nazwa": "Jak uczyć się z asystentem AI, żeby to Ty umiał programować",
     "slowa": ["asystent", "claude", "prompt", "70/30", "15 minut", "zasad", "nie pisz za mnie", "claude.md"],
     "wyjasnienie":
         "Asystent (Claude Code, API albo tryb Offline) potrafi napisać program za Ciebie — i to jest największa pułapka nauki. Jeśli on pisze, Ty nie umiesz. "
         "Dlatego osiem zasad: (1) najpierw 15 minut sam, potem pytasz; (2) prosisz o podpowiedź, nie o rozwiązanie — „daj mi wskazówkę, nie poprawiaj”; "
         "(3) każdy fragment kodu od asystenta PRZEPISUJESZ ręcznie — palce uczą się składni; (4) zanim uruchomisz kod, tłumaczysz asystentowi, co robi; "
         "(5) dzień kończysz 3 pytaniami sprawdzającymi; (6) CLAUDE.md w projekcie przypomina asystentowi zasady; (7) większe zadanie najpierw planujesz (tryb planowania), potem kodujesz; "
         "(8) pytasz „dlaczego”, aż będzie oczywiste — nie idziesz dalej z niezrozumianym kodem.\n"
         "Zasada 70/30: 70% czasu piszesz kod sam, 30% rozmawiasz o tym, co napisałeś. Mentor pilnuje tego timerem sesji i licznikiem 15 minut walki.\n"
         "W tygodniach 1–3 asystent tylko podpowiada. Od tygodnia 4 może pisać fragmenty — ale Ty je tłumaczysz linijka po linijce. Od tygodnia 7: on pisze kod, Ty testy (i odwrotnie).",
     "przyklad":
         "ŹLE:   „Napisz mi kalkulator BMI.”\n"
         "DOBRZE: „Uczę się if/elif. Wytłumacz na 2 przykładach z gospodarstwa i daj 3 zadania. Nie podawaj rozwiązań.”\n"
         "DOBRZE: „Utknąłem. Oto @bmi.py i błąd: TypeError … Nie poprawiaj. Zadaj mi pytanie, które naprowadzi na przyczynę.”\n"
         "DOBRZE: „Zatrzymaj się. Zrobiłeś to za mnie. Cofnij i daj tylko pierwszy krok.”",
     "zadania": ["Wklej do asystenta prompt „Nowy temat” z tematem „zmienne” i sprawdź, czy dał zadania BEZ rozwiązań. Jeśli dał rozwiązania — napisz „zatrzymaj się”.",
                 "Przepisz ręcznie (nie kopiuj) 5-liniowy przykład z lekcji „Zmienne” i uruchom.",
                 "Zapisz w notatkach 8 zasad własnymi słowami, po jednym zdaniu."],
     "pytania": [("Ile minut sam, zanim zapytasz?", "Minimum 15."),
                 ("Co zrobić, gdy asystent napisał cały program?", "„Zatrzymaj się. Cofnij i daj tylko pierwszy krok.” Potem przepisać samemu."),
                 ("Na czym polega zasada 70/30?", "70% czasu piszesz kod sam, 30% rozmawiasz o nim z asystentem.")],
     "pulapki": ["Kopiuj-wklej kodu od asystenta = zero nauki. Przepisuj.", "Asystent może się mylić — jeśli coś nie działa, czytaj komunikat błędu, nie wierz na słowo."],
     "test": [
         {"p": "Co robisz, gdy utknąłeś po 3 minutach?", "o": ["Pytasz asystenta o rozwiązanie", "Walczysz dalej do 15 minut, potem prosisz o PYTANIE naprowadzające", "Kopiujesz kod z internetu", "Przechodzisz do następnego zadania"],
          "odp": 1, "w": "Frustracja to moment, w którym mózg się uczy."},
         {"p": "Co znaczy „przepisz, nie kopiuj”?", "o": ["Zmień nazwy zmiennych", "Wpisz kod ręcznie znak po znaku, bo palce zapamiętują składnię", "Przetłumacz na polski", "Nic nie znaczy"],
          "odp": 1, "w": "Pamięć mięśniowa + wymuszone czytanie każdej linii."},
         {"p": "Do czego służy CLAUDE.md?", "o": ["Do notatek", "Do zasad, które asystent czyta na starcie — np. „nie pisz rozwiązań za mnie”", "Do listy zadań", "Do haseł"],
          "odp": 1, "w": "W trybie Offline Mentor też go respektuje (nie pisze rozwiązań)."},
     ]},
]

# Mini-testy do lekcji z wiedza.TEMATY (3 pytania każda)
TESTY = {
    "zmienne": [
        {"p": "Jakiego typu jest wartość 612.5?", "o": ["int", "float", "str", "bool"], "odp": 1, "w": "Kropka dziesiętna = float."},
        {"p": "Co zwróci type(\"14\")?", "o": ["int", "float", "str", "bool"], "odp": 2, "w": "Cudzysłów = napis, nawet gdy w środku cyfry."},
        {"p": "Jak poprawnie skleić napis z liczbą?", "o": ["\"Waga: \" + 612", "\"Waga: \" + str(612)", "\"Waga: \" & 612", "\"Waga: \" . 612"], "odp": 1, "w": "str() zamienia liczbę na napis."},
    ],
    "input_print": [
        {"p": "Co zwraca input()?", "o": ["Liczbę", "Zawsze napis", "Zależy, co wpisano", "bool"], "odp": 1, "w": "Zawsze str — stąd int(input())."},
        {"p": "Co wypisze print(f\"{2 + 3} krów\")?", "o": ["{2 + 3} krów", "5 krów", "2 + 3 krów", "błąd"], "odp": 1, "w": "f-string oblicza wyrażenie w nawiasach."},
        {"p": "Co wypisze print(\"a\", \"b\", \"c\")?", "o": ["abc", "a b c", "a,b,c", "a\\nb\\nc"], "odp": 1, "w": "print rozdziela argumenty spacją."},
    ],
    "warunki": [
        {"p": "Które porównanie jest poprawne?", "o": ["if x = 5:", "if x == 5:", "if x => 5:", "if x equals 5:"], "odp": 1, "w": "== porównuje, = przypisuje."},
        {"p": "W łańcuchu if/elif/else wykona się…", "o": ["każdy prawdziwy blok", "tylko pierwszy prawdziwy blok", "wszystkie bloki", "ostatni blok"], "odp": 1, "w": "Kolejność warunków ma znaczenie."},
        {"p": "Co oznacza if waga > 500 and rasa == \"HF\":?", "o": ["Jeden z warunków", "Oba warunki naraz", "Żaden", "Błąd składni"], "odp": 1, "w": "and = oba; or = którykolwiek."},
    ],
    "petle": [
        {"p": "Ile razy wykona się for i in range(5)?", "o": ["4", "5", "6", "nieskończenie"], "odp": 1, "w": "0,1,2,3,4 — pięć obrotów."},
        {"p": "Co robi continue?", "o": ["Kończy pętlę", "Pomija resztę bieżącego obrotu i idzie do następnego", "Zatrzymuje program", "Cofa obrót"], "odp": 1, "w": "break kończy, continue przeskakuje."},
        {"p": "Kiedy while True jest bezpieczne?", "o": ["Nigdy", "Gdy w środku jest break przy jakimś warunku", "Zawsze", "Tylko w funkcjach"], "odp": 1, "w": "Bez break — pętla nieskończona."},
    ],
    "listy": [
        {"p": "Jaki indeks ma ostatni element listy o 4 elementach?", "o": ["4", "3", "-0", "1"], "odp": 1, "w": "Od 0: 0,1,2,3. Albo [-1]."},
        {"p": "Co zwraca lista.sort()?", "o": ["Posortowaną kopię", "None — sortuje w miejscu", "Pierwszy element", "Długość"], "odp": 1, "w": "sorted(lista) zwraca kopię."},
        {"p": "Jak sprawdzić, czy \"Mućka\" jest na liście stado?", "o": ["stado.has(\"Mućka\")", "\"Mućka\" in stado", "stado == \"Mućka\"", "stado.find(\"Mućka\") == True"], "odp": 1, "w": "Operator in."},
    ],
    "napisy": [
        {"p": "Co zwróci \"kot\"[::-1]?", "o": ["kot", "tok", "k", "t"], "odp": 1, "w": "Krok -1 = od tyłu."},
        {"p": "Czy tekst.upper() zmienia zmienną tekst?", "o": ["Tak", "Nie — zwraca nowy napis", "Tylko pierwszą literę", "Zależy od wersji"], "odp": 1, "w": "Napisy są niezmienne."},
        {"p": "Co zwróci \"a b c\".split()?", "o": ["\"abc\"", "[\"a\", \"b\", \"c\"]", "3", "(\"a\",\"b\",\"c\")"], "odp": 1, "w": "Lista słów."},
    ],
    "funkcje": [
        {"p": "Co zwraca funkcja bez return?", "o": ["0", "\"\"", "None", "błąd"], "odp": 2, "w": "Brak return = None."},
        {"p": "Gdzie żyje zmienna utworzona wewnątrz funkcji?", "o": ["Wszędzie", "Tylko w tej funkcji", "W całym pliku", "W module"], "odp": 1, "w": "Zakres lokalny."},
        {"p": "Czym jest docstring?", "o": ["Komentarzem po #", "Opisem w \"\"\" \"\"\" tuż pod def", "Nazwą funkcji", "Typem zwracanym"], "odp": 1, "w": "Czyta go help() i PyCharm."},
    ],
    "slowniki": [
        {"p": "Co zwróci d.get(\"byk\", 0), gdy klucza nie ma?", "o": ["KeyError", "0", "None", "\"byk\""], "odp": 1, "w": "get z wartością domyślną nie rzuca błędu."},
        {"p": "Jak przejść po parach klucz–wartość?", "o": ["for k, v in d:", "for k, v in d.items():", "for k in d.values():", "for d in d:"], "odp": 1, "w": "items() daje pary."},
        {"p": "Czego NIE można zrobić z krotką?", "o": ["Odczytać elementu", "Zmienić elementu po utworzeniu", "Przejść pętlą", "Zwrócić z funkcji"], "odp": 1, "w": "Krotka jest niezmienna."},
    ],
    "bledy": [
        {"p": "Jaki wyjątek rzuca float(\"abc\")?", "o": ["TypeError", "ValueError", "KeyError", "SyntaxError"], "odp": 1, "w": "Typ ok (napis), wartość zła."},
        {"p": "Dlaczego gołe except: jest złe?", "o": ["Jest wolne", "Ukrywa wszystkie błędy, także literówki w kodzie", "Nie działa w Pythonie 3", "Wymaga importu"], "odp": 1, "w": "Łap konkretny typ."},
        {"p": "Kiedy wykona się blok else po try?", "o": ["Zawsze", "Gdy w try NIE było błędu", "Gdy był błąd", "Nigdy"], "odp": 1, "w": "finally — zawsze; else — gdy sukces."},
    ],
    "moduly_std": [
        {"p": "Czy random.randint(1, 6) może zwrócić 6?", "o": ["Nie", "Tak, oba końce włącznie", "Tylko czasem", "Zwraca float"], "odp": 1, "w": "W odróżnieniu od range."},
        {"p": "Jak dodać 7 dni do daty d?", "o": ["d + 7", "d + datetime.timedelta(days=7)", "d.add(7)", "d + \"7 days\""], "odp": 1, "w": "timedelta reprezentuje odstęp czasu."},
        {"p": "Co zwraca random.sample(lista, 3)?", "o": ["Jeden element", "3 różne elementy jako listę", "Posortowaną listę", "3 elementy mogące się powtarzać"], "odp": 1, "w": "Bez powtórzeń; choice losuje jeden."},
    ],
    "pliki": [
        {"p": "Co robi open(\"a.txt\", \"w\")?", "o": ["Otwiera do odczytu", "Otwiera do zapisu i kasuje poprzednią zawartość", "Dopisuje na końcu", "Tworzy kopię"], "odp": 1, "w": "Tryb \"a\" dopisuje."},
        {"p": "Po co with open(...) as f:?", "o": ["Dla szybkości", "Zamyka plik automatycznie, nawet przy błędzie", "Dla czytelności", "Jest wymagane"], "odp": 1, "w": "Menedżer kontekstu."},
        {"p": "Skąd liczy się ścieżka względna \"stado.txt\"?", "o": ["Od pliku .py", "Od katalogu roboczego terminala", "Od Dokumentów", "Od C:\\"], "odp": 1, "w": "Dlatego uruchamiaj z folderu projektu."},
    ],
    "csv": [
        {"p": "Co daje csv.DictReader?", "o": ["Listy napisów", "Słowniki z nagłówkami jako kluczami", "Liczby", "Jeden napis"], "odp": 1, "w": "wiersz[\"waga\"]."},
        {"p": "Jakiego typu jest wiersz[\"waga\"] po DictReader?", "o": ["float", "int", "str", "zależy od pliku"], "odp": 2, "w": "CSV to tekst — trzeba float()."},
        {"p": "Po co newline=\"\" w open przy CSV?", "o": ["Dla UTF-8", "Żeby na Windows nie było pustych linii", "Dla szybkości", "Nie jest potrzebne"], "odp": 1, "w": "Dokumentacja csv tego wymaga."},
    ],
    "git": [
        {"p": "Co robi git checkout -b feature/csv?", "o": ["Usuwa gałąź", "Tworzy gałąź i przełącza na nią", "Scala z main", "Wysyła na GitHub"], "odp": 1, "w": "-b = nowa gałąź."},
        {"p": "Czym jest pull request?", "o": ["Pobraniem zmian", "Prośbą o scalenie gałęzi z możliwością recenzji", "Kopią repo", "Usunięciem gałęzi"], "odp": 1, "w": "Tak zespoły oglądają kod przed main."},
        {"p": "Które polecenie kasuje niezacommitowane zmiany w pliku bezpowrotnie?", "o": ["git stash", "git checkout -- plik", "git status", "git log"], "odp": 1, "w": "stash odkłada i przywraca."},
    ],
    "klasy": [
        {"p": "Co oznacza self w metodzie?", "o": ["Klasę", "Konkretny obiekt, na którym wywołano metodę", "Moduł", "Nic"], "odp": 1, "w": "self.waga to waga tej krowy."},
        {"p": "Kiedy wywołuje się __init__?", "o": ["Przy imporcie", "Przy tworzeniu obiektu", "Przy print", "Przy usuwaniu"], "odp": 1, "w": "Konstruktor."},
        {"p": "Jak utworzyć obiekt klasy Zwierze?", "o": ["new Zwierze()", "Zwierze(\"Krasula\", 612)", "Zwierze.create()", "class Zwierze()"], "odp": 1, "w": "Wywołanie klasy jak funkcji."},
    ],
    "moduly": [
        {"p": "Po co if __name__ == \"__main__\":?", "o": ["Dla szybkości", "Żeby kod startowy nie wykonywał się przy imporcie", "Dla PyCharm", "Jest wymagane"], "odp": 1, "w": "Import wykonuje tylko definicje."},
        {"p": "Jak zaimportować funkcję dodaj z zadania.py?", "o": ["import dodaj from zadania", "from zadania import dodaj", "include zadania.dodaj", "require(\"zadania\")"], "odp": 1, "w": "Składnia from … import …"},
        {"p": "Co to moduł?", "o": ["Folder", "Każdy plik .py, który można zaimportować", "Klasa", "Biblioteka z pip"], "odp": 1, "w": "Plik = moduł; folder z __init__.py = pakiet."},
    ],
    "venv": [
        {"p": "Po co venv?", "o": ["Szybszy Python", "Osobne biblioteki dla każdego projektu", "Większe bezpieczeństwo", "Wymaga go PyCharm"], "odp": 1, "w": "Bez konfliktów wersji."},
        {"p": "Jak odtworzyć środowisko na innym komputerze?", "o": ["Skopiować .venv", "pip install -r requirements.txt", "Zainstalować PyCharm", "git clone wystarczy"], "odp": 1, "w": "Dlatego .venv nie idzie do repo."},
        {"p": "Co powinno być w .gitignore?", "o": ["main.py", ".venv/ i __pycache__/", "README.md", "requirements.txt"], "odp": 1, "w": "Generowane i cudze — poza repo."},
    ],
    "requests": [
        {"p": "Co oznacza status 404?", "o": ["Sukces", "Nie znaleziono", "Brak internetu", "Błąd serwera"], "odp": 1, "w": "200 = OK, 500 = błąd serwera."},
        {"p": "Co zwraca odp.json()?", "o": ["Napis", "Struktury Pythona (dict/list) z JSON-a", "Plik", "HTML"], "odp": 1, "w": "Dalej czytasz jak słownik."},
        {"p": "Po co timeout w requests.get?", "o": ["Dla szybkości", "Żeby program nie wisiał w nieskończoność", "Dla bezpieczeństwa", "Nie jest potrzebny"], "odp": 1, "w": "Zawsze ustawiaj."},
    ],
    "debug": [
        {"p": "Co robi breakpoint?", "o": ["Usuwa linię", "Zatrzymuje program w tej linii", "Oznacza błąd", "Uruchamia test"], "odp": 1, "w": "Potem oglądasz zmienne."},
        {"p": "Od którego końca czytać traceback?", "o": ["Od góry", "Od dołu — ostatnia linia mówi CO", "Od środka", "Nie czytać"], "odp": 1, "w": "Wyżej — GDZIE."},
        {"p": "Co to błąd logiczny?", "o": ["SyntaxError", "Program działa, ale daje zły wynik", "Brak pliku", "Literówka w nazwie"], "odp": 1, "w": "Nie ma tracebacku — łapią go testy."},
    ],
    "readme": [
        {"p": "Co minimalnie ma README?", "o": ["Nazwę", "Co program robi i jak go uruchomić", "Cały kod", "Historię commitów"], "odp": 1, "w": "30 sekund rekrutera."},
        {"p": "Czym jest refaktoryzacja?", "o": ["Dodaniem funkcji", "Zmianą struktury kodu bez zmiany zachowania", "Naprawą błędu", "Usunięciem testów"], "odp": 1, "w": "Zachowanie identyczne."},
        {"p": "Po co docstring, skoro jest komentarz?", "o": ["Nie ma różnicy", "Docstring opisuje CO funkcja robi i czyta go help(); komentarz — DLACZEGO coś zrobiono", "Docstring jest szybszy", "Komentarze są zakazane"], "odp": 1, "w": "Oba mają miejsce."},
    ],
    "pytest": [
        {"p": "W jakich plikach pytest szuka testów?", "o": ["Wszystkich .py", "test_*.py i *_test.py", "main.py", "conftest.py"], "odp": 1, "w": "I funkcji def test_…"},
        {"p": "Co się dzieje przy assert 2 + 2 == 5?", "o": ["Przechodzi", "AssertionError — test czerwony", "Program kończy się", "Nic"], "odp": 1, "w": "Z pokazaniem obu wartości."},
        {"p": "Jak sprawdzić, że test naprawdę coś sprawdza?", "o": ["Uruchomić dwa razy", "Zepsuć kod i zobaczyć, czy test czerwienieje", "Dodać print", "Poprosić asystenta"], "odp": 1, "w": "Test, który nigdy nie był czerwony, jest podejrzany."},
    ],
    "parametrize_fixture": [
        {"p": "Po co parametrize?", "o": ["Dla szybkości", "Jeden test dla wielu zestawów danych", "Do raportów", "Do pomijania testów"], "odp": 1, "w": "Tabela przypadków zamiast kopii."},
        {"p": "Co dostaje test, który ma argument o nazwie fixture?", "o": ["None", "Świeży wynik tej fixture", "Błąd", "Listę"], "odp": 1, "w": "Nazwa argumentu = nazwa fixture."},
        {"p": "Co daje tmp_path?", "o": ["Losową liczbę", "Tymczasowy katalog na czas testu", "Ścieżkę projektu", "Internet"], "odp": 1, "w": "Testy nie dotykają prawdziwych danych."},
    ],
    "selenium": [
        {"p": "Który lokator jest najstabilniejszy?", "o": ["XPath po pełnej ścieżce", "id", "Tekst", "Pozycja"], "odp": 1, "w": "Unikalny, rzadko się zmienia."},
        {"p": "Co znaczy # w selektorze CSS?", "o": ["Klasę", "id", "Tag", "Komentarz"], "odp": 1, "w": "Kropka = klasa."},
        {"p": "Co robi driver.quit()?", "o": ["Odświeża stronę", "Zamyka przeglądarkę i zwalnia zasoby", "Robi zrzut", "Czeka"], "odp": 1, "w": "Zawsze na końcu."},
    ],
    "wait_pom": [
        {"p": "Dlaczego WebDriverWait zamiast time.sleep?", "o": ["sleep nie działa", "Wait czeka tylko tyle, ile trzeba, do spełnienia warunku", "Wait jest prostszy", "Bez różnicy"], "odp": 1, "w": "sleep zawsze pełny czas."},
        {"p": "Gdzie w POM leżą lokatory?", "o": ["W testach", "W klasie strony", "W conftest", "W README"], "odp": 1, "w": "Testy wołają metody."},
        {"p": "Co zmieniasz, gdy zmieni się id przycisku?", "o": ["Wszystkie testy", "Jeden lokator w klasie strony", "conftest", "Nic"], "odp": 1, "w": "To cała wartość POM."},
    ],
    "bug_raport": [
        {"p": "Jaki jest test dobrego bug raportu?", "o": ["Jest krótki", "Programista odtwarza błąd bez pytań", "Ma zrzut", "Ma priorytet"], "odp": 1, "w": "Kroki, oczekiwany, rzeczywisty, środowisko."},
        {"p": "Co zawiera przypadek testowy?", "o": ["Kod", "ID, warunki wstępne, kroki, oczekiwany wynik", "Zrzut", "Nazwisko"], "odp": 1, "w": "Przepis dla innego testera."},
        {"p": "Który tytuł buga jest dobry?", "o": ["\"nie działa\"", "\"błąd\"", "\"Przelew 0 zł zapisuje się bez komunikatu\"", "\"pomocy\""], "odp": 2, "w": "Co, gdzie, przy jakich danych."},
    ],
    "ci": [
        {"p": "Gdzie leży workflow GitHub Actions?", "o": ["tests/", ".github/workflows/", "README", ".venv/"], "odp": 1, "w": "Plik .yml."},
        {"p": "Co daje CI?", "o": ["Szybszy kod", "Automatyczne testy przy każdym pushu na czystej maszynie", "Lepszy wygląd", "Naprawę błędów"], "odp": 1, "w": "Działa nie tylko u Ciebie."},
        {"p": "Czego wymaga YAML?", "o": ["Tabulatorów", "Spacji we wcięciach", "Średników", "Nawiasów"], "odp": 1, "w": "Tabulator = błąd."},
    ],
    "sqlite": [
        {"p": "Czym jest SQLite?", "o": ["Serwerem", "Bazą w jednym pliku, wbudowaną w Pythona", "Biblioteką testów", "Frameworkiem WWW"], "odp": 1, "w": "import sqlite3."},
        {"p": "Jak przekazać wartość do zapytania?", "o": ["f-stringiem", "Przez ? i krotkę parametrów", "Sklejając napisy", "Przez print"], "odp": 1, "w": "Bezpiecznie, bez SQL injection."},
        {"p": "Bez czego dane nie zapiszą się w bazie?", "o": ["Bez print", "Bez con.commit()", "Bez close", "Bez SELECT"], "odp": 1, "w": "commit zatwierdza."},
    ],
    "flask": [
        {"p": "Jak połączyć adres / z funkcją?", "o": ["def main()", "@app.route(\"/\")", "app.home()", "flask.page(\"/\")"], "odp": 1, "w": "Dekorator route."},
        {"p": "Gdzie leżą szablony HTML?", "o": ["Obok app.py", "W folderze templates/", "W static/", "Gdziekolwiek"], "odp": 1, "w": "Flask szuka tam domyślnie."},
        {"p": "Po co walidacja po stronie serwera?", "o": ["Dla wyglądu", "Żeby złe dane nie trafiły do bazy, cokolwiek wpisze użytkownik", "Dla szybkości", "Nie trzeba"], "odp": 1, "w": "Tester wpisze wszystko."},
    ],
    "rekrutacja": [
        {"p": "Co zawiera wpis w sekcji Projekty w CV?", "o": ["Nazwę", "Co robi, technologie, liczba testów, link do GitHuba i CI", "Pół strony", "Zrzut"], "odp": 1, "w": "Każde słowo potwierdza kod."},
        {"p": "Struktura 2-minutowej opowieści o projekcie?", "o": ["Lista plików", "Problem → rozwiązanie → jak testuję → czego się nauczyłem", "Historia commitów", "Opis narzędzi"], "odp": 1, "w": "Rekruter chce usłyszeć, jak myślisz."},
        {"p": "Sygnał gotowości do aplikowania?", "o": ["12 tygodni minęło", "Naprawiasz test Selenium sam i tłumaczysz każdy plik koledze bez IT", "100 commitów", "Asystent powiedział ok"], "odp": 1, "w": "Samodzielność, nie kalendarz."},
    ],
}
