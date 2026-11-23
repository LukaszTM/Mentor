# -*- coding: utf-8 -*-
"""Pozostałe części programu „Python od zera → Junior QA”: metadane, etapy, środowisko, diagnoza, ściąga, prompty, szablony, pojęcia, pytania rekrutacyjne."""

from wspolne import Q
import zrodla as Z

META = {
    "format": "mentor-program/1", "id": "python-junior-qa", "nazwa": "Python od zera → Junior QA",
    "podtytul": "13 tygodni · Python, Git, pytest, Selenium, SQL, Flask, CI i projekt portfolio",
    "opis": ("Po 13 tygodniach piszesz samodzielnie programy w Pythonie, projektujesz przypadki testowe technikami ISTQB (klasy równoważności, wartości brzegowe), "
             "piszesz testy w pytest i Selenium (Page Object Model), raporty błędów i pipeline CI w GitHub Actions, a na GitHubie masz projekt portfolio "
             "„Magazyn” (Python, SQLite, Flask) z testami na kilku poziomach — gotowy do pokazania na rozmowie Junior QA. Start od zera; zadania z kodem "
             "sprawdzają niezależne testy z paczki kursu (suma SHA-256); asystent AI jest pomocą, nie warunkiem."),
    "autor": "Mentor — kurs otwarty (fakty o narzędziach i rynku pracy sprawdzone u źródeł 23.11.2026)",
    "wersja": "3.0", "jezyk": "pl", "katalog_projektu": "nauka-python", "stanowisko": "Junior QA / tester oprogramowania (manualny i automatyzujący)",
    "czas_dziennie_min": 90, "dni_w_tygodniu": [0, 1, 2, 3, 4], "dzien_quizu": 5, "dzien_wolny": 6,
    "poziom": "od zera — bez wcześniejszej znajomości programowania, terminala i Gita",
    "system": "Windows 10 / 11 — Mentor.exe; Python i biblioteki kursu instaluje Mentor, Git for Windows instalujesz w tygodniu 0",
    "stan_prawny": "23 listopada 2026",
    "materialy": "materialy/python-junior-qa",
    "wymagania_wstepne": [
        "ok. 90 minut dziennie od poniedziałku do piątku i do 60 minut w sobotę (quiz, powtórka) przez 13 tygodni — razem ok. 100 godzin; każdy tydzień mieści się w 9 godzinach",
        "komputer z Windows 10/11 i internetem przy instalacji; Mentor instaluje Pythona i biblioteki kursu za Twoją zgodą, bez uprawnień administratora",
        "0 zł: Python, Git, GitHub (konto darmowe od tygodnia 0), PyCharm w wersji darmowej (opcjonalnie); asystent AI — tryb Offline Mentora albo darmowy czat; Claude Code (płatny) — opcjonalnie",
        "przeglądarka Microsoft Edge (wbudowana w Windows) albo Chrome od tygodnia 8; internet przy pierwszym uruchomieniu Selenium (pobranie sterownika)",
    ],
    "umiejetnosci_koncowe": [
        "pisać i czytać programy w Pythonie: typy, warunki, pętle, listy, słowniki, funkcje, wyjątki, pliki i CSV, klasy, moduły",
        "pracować jak w zespole: Git (gałęzie, pull request, cofanie zmian), GitHub, venv i requirements.txt, README",
        "projektować przypadki testowe technikami klas równoważności i wartości brzegowych; znać terminologię ISTQB (pomyłka, defekt, awaria, poziomy testów)",
        "pisać testy pytest (parametrize, fixtures, tmp_path, raises) i sprawdzać mutacją, że łapią błędy",
        "automatyzować testy przeglądarki w Selenium WebDriver z WebDriverWait i Page Object Model",
        "pisać przypadki testowe i raporty błędów odtwarzalne bez pytań; uruchamiać testy w GitHub Actions z raportem HTML",
        "używać SQL (SQLite) z zapytaniami parametryzowanymi i testować aplikację Flask na dwóch poziomach (test_client i E2E)",
        "przedstawić projekt portfolio na rozmowie Junior QA: CV, opowieść o projekcie, odpowiedzi techniczne",
    ],
    "zasady": [
        "Najpierw wyjaśnienie i demonstracja, potem ćwiczenie prowadzone, na końcu samodzielne — w tej kolejności.",
        "70% kodu piszesz sam; asystenta prosisz o wskazówkę, nie o rozwiązanie. Kod od AI przepisujesz ręcznie i tłumaczysz.",
        "Zaliczenie = zielony test Mentora + umiesz wyjaśnić, co i dlaczego działa.",
        "Logika w funkcjach z return, input()/print() tylko w bloku if __name__ == \"__main__\": — kod musi być testowalny.",
        "Testujesz granice i złe dane, nie tylko ścieżkę szczęśliwą.",
        "Sekrety (hasła, klucze) nigdy w kodzie ani w repozytorium; dane w kursie są fikcyjne.",
        "Każdą nazwę funkcji czy biblioteki z odpowiedzi AI sprawdzasz w dokumentacji albo uruchomieniem.",
    ],
    "firma": ("Świat ćwiczeń: fikcyjny sklep papierniczy „Papierowy Kot” — produkty (zeszyty, pisaki, papier, biuro), ceny, stany magazynowe, rabaty i dostawa. "
              "Na nim ćwiczysz od tygodnia 1, w tygodniu 8–9 testujesz jego lokalny sklep internetowy (z celowo wprowadzonymi defektami), a w tygodniach 10–12 budujesz "
              "dla niego aplikację „Magazyn” — swój projekt portfolio. Wszystkie dane są fikcyjne."),
    "srodowisko": {
        "python": ">=3.11,<3.14", "pakiety": ["pytest", "requests", "selenium", "flask"], "lock": "programy/zaleznosci/requirements.lock",
        "narzedzia_wymagane": [], "narzedzia_opcjonalne": {"git": 0, "claude": 0},
        "przegladarka": "edge", "przegladarka_od_tygodnia": 8,
        "sprawdzenia": [{"kind": "python_import", "module": "pytest"}, {"kind": "python_import", "module": "requests"}, {"kind": "python_import", "module": "selenium"},
                        {"kind": "python_import", "module": "flask"}, {"kind": "pytest_sample"}, {"kind": "local_api"}, {"kind": "selenium_browser", "optional": True}],
        "uwagi": ["Python 3.11–3.13 i biblioteki kursu (pytest, requests, selenium, flask) instaluje Mentor w osobnym środowisku .venv — za Twoją zgodą, bez uprawnień administratora.",
                  "Git for Windows instalujesz w tygodniu 0 (lekcja „Narzędzia”); Mentor pokazuje tylko, czy działa. Claude Code jest opcjonalny (płatny plan).",
                  "Przeglądarka Edge (wbudowana w Windows 10/11) albo Chrome potrzebna od tygodnia 8; sterownik pobiera Selenium Manager przy pierwszym uruchomieniu (internet)."],
    },
}

ETAPY = [
    {"nr": 0, "nazwa": "Konfiguracja", "tygodnie": [0],
     "cel": "Środowisko kursu w Mentorze, Git i GitHub, katalog roboczy z CLAUDE.md, pierwszy program i pierwszy commit."},
    {"nr": 1, "nazwa": "Podstawy Pythona", "tygodnie": [1, 2, 3],
     "cel": "Piszesz bez pomocy program na 50–100 linii z funkcjami, pętlami, listami i słownikami, z obsługą błędów — i rozumiesz każdą linię."},
    {"nr": 2, "nazwa": "Projekt jak w zespole", "tygodnie": [4, 5, 6],
     "cel": "Pliki i CSV, Git w zespole (gałęzie, PR, cofanie), klasy i moduły, venv, API, debugowanie, README; czytasz cudzy kod."},
    {"nr": 3, "nazwa": "Testowanie: techniki, pytest, Selenium, CI", "tygodnie": [7, 8, 9],
     "cel": "Projektujesz przypadki testowe, piszesz testy pytest i Selenium (POM), raporty błędów i pipeline GitHub Actions z raportem HTML."},
    {"nr": 4, "nazwa": "Projekt portfolio i rekrutacja", "tygodnie": [10, 11, 12],
     "cel": "Aplikacja Magazyn (SQLite, Flask) z testami na kilku poziomach i CI, dokumentacja testów, CV i przygotowanie do rozmowy Junior QA."},
]

DIAGNOZA = [
    Q("Plik ma ścieżkę C:\\Users\\Ania\\PRACA\\hello.py. W jakim folderze leży?", ["Users", "PRACA", "hello", "C:"], 1, "Ostatni element przed nazwą pliku.", "terminal"),
    Q("Co zwróci 7 // 2 w Pythonie?", ["3.5", "3", "4", "nie wiem"], 1, "Dzielenie całkowite.", "zmienne"),
    Q("x = input() — użytkownik wpisał 5. Typ x?", ["int", "str", "float", "nie wiem"], 1, "input() zawsze zwraca napis.", "input_print"),
    Q("Reguła „od 100 zł darmowa dostawa”. Które kwoty warto przetestować?", ["1 i 1000", "99.99 i 100", "tylko 50", "nie wiem"], 1, "Wartości brzegowe.", "warunki"),
    Q("Ile razy wykona się for i in range(3)?", ["2", "3", "4", "nie wiem"], 1, "0, 1, 2.", "petle"),
    Q("Pierwszy element listy l to:", ["l[1]", "l[0]", "l[-0]", "nie wiem"], 1, "Indeksy od 0.", "listy"),
    Q("Funkcja bez return zwraca:", ["0", "None", "błąd", "nie wiem"], 1, "Domyślnie None.", "funkcje"),
    Q("Co robi git commit?", ["wysyła na GitHub", "zapisuje zmiany w historii lokalnie", "usuwa pliki", "nie wiem"], 1, "push wysyła.", "git_start"),
    Q("Program „wisi” w pętli while. Najczęstsza przyczyna?", ["za wolny komputer", "nic w pętli nie zmienia warunku", "brak internetu", "nie wiem"], 1, "Pętla nieskończona.", "petle"),
    Q("Asystent AI podał funkcję, której nie ma w Pythonie. To:", ["nowa wersja Pythona", "halucynacja — trzeba sprawdzić w dokumentacji", "błąd Windows", "nie wiem"], 1, "Weryfikuj nazwy.", "nauka_z_asystentem"),
]

PYTANIA_DZIENNIKA = ["Co dziś zrobiłem(-am) i jaki był wynik?", "Co sprawdziłem(-am) testem albo uruchomieniem?", "Czego nie rozumiem — o co zapytam jutro?"]

RYTM_DNIA = [
    {"nazwa": "Powtórka", "minuty": 10, "ikona": "🔁", "opis": "Pytania z wczorajszej lekcji z pamięci — dopiero potem zajrzyj do notatek.",
     "prompt": "Zadaj mi 3 krótkie pytania z tematu [temat] z wczorajszej lekcji. Poczekaj na moje odpowiedzi i dopiero wtedy je oceń."},
    {"nazwa": "Nowy temat", "minuty": 30, "ikona": "📖", "opis": "Lekcja dnia: wyjaśnienie → demonstracja (uruchom i zmień jedną wartość) → ćwiczenie prowadzone z polami „Twoje odpowiedzi”.",
     "prompt": "Uczę się [temat] w Pythonie. Wytłumacz na 2 prostych przykładach ze sklepu i daj 3 zadania BEZ rozwiązań."},
    {"nazwa": "Zadanie", "minuty": 40, "ikona": "🛠", "opis": "Ćwiczenie samodzielne i zadanie z Planu: „📝 Utwórz plik ćwiczenia” → kod → „▶ Uruchom” → „✔ Sprawdź wynik”.",
     "prompt": "Mój kod: [kod]. Komunikat: [ostatnia linia tracebacku]. Nie podawaj poprawionego kodu — zadaj mi jedno pytanie, które pomoże znaleźć przyczynę."},
    {"nazwa": "Dziennik i commit", "minuty": 10, "ikona": "📝", "opis": "3 zdania: co zrobiłem, co sprawdziłem, czego nie rozumiem; git add, commit z opisem, push.",
     "prompt": "Oto mój opis commita: [opis]. Czy mówi, co i dlaczego zmieniłem? Zaproponuj lepszy, ale zostaw decyzję mnie."},
]

PROMPTY = [
    {"nazwa": "Nowy temat", "kiedy": "Początek lekcji", "tresc": "Uczę się [temat] w Pythonie (tydzień [N] kursu). Wytłumacz na 2 prostych przykładach ze sklepu i daj 3 zadania BEZ rozwiązań."},
    {"nazwa": "Błąd w kodzie", "kiedy": "Program nie działa", "tresc": "Mój kod: [kod]. Komunikat: [ostatnia linia tracebacku]. Nie podawaj poprawionego kodu — zadaj mi jedno pytanie, które pomoże znaleźć przyczynę."},
    {"nazwa": "Wyjaśnij linia po linii", "kiedy": "Kod od AI albo z internetu", "tresc": "Wyjaśnij linia po linii, co robi ten kod i co się stanie, gdy zmienię [wartość]: [kod]"},
    {"nazwa": "Przegląd kodu", "kiedy": "Zadanie gotowe", "tresc": "Oceń mój kod jak doświadczony programista: 3 najważniejsze uwagi od najpoważniejszej (czytelność, przypadki brzegowe, testowalność). Nie poprawiaj kodu."},
    {"nazwa": "Przypadki testowe", "kiedy": "Przed pisaniem testów", "tresc": "Reguła: [opis]. Pomóż mi wypisać klasy równoważności i wartości brzegowe — najpierw zapytaj, co ja proponuję."},
    {"nazwa": "Ocena bug raportu", "kiedy": "Raport błędu gotowy", "tresc": "Oceń mój raport błędu: czy programista odtworzy błąd bez pytań? Czego brakuje (kroki, dane, środowisko, oczekiwany/rzeczywisty)? [raport]"},
    {"nazwa": "Rekruter Junior QA", "kiedy": "Tydzień 12", "tresc": "Jesteś rekruterem na stanowisko Junior QA. Zadaj mi po kolei 10 pytań technicznych i 3 miękkie; po każdej mojej odpowiedzi oceń ją krótko i podaj, czego zabrakło."},
    {"nazwa": "Recenzja seniora", "kiedy": "Tydzień 12", "tresc": "Oceń mój projekt jak senior tester przed code review: 5 najważniejszych uwag od najpoważniejszej (kod, testy, dokumentacja, bezpieczeństwo, CI). Nie poprawiaj kodu."},
]

CLAUDE_MD = ("# Zasady nauki — kurs „Python od zera → Junior QA”\n\n"
             "- Uczę się Pythona i testowania; tłumacz po polsku i prostymi słowami.\n"
             "- Nie podawaj gotowych rozwiązań zadań — najpierw pytanie naprowadzające, potem wskazówka, fragment, a pełne rozwiązanie tylko na prośbę, z omówieniem.\n"
             "- Każdy fragment kodu wyjaśnij linia po linii.\n"
             "- Przy błędzie pokaż, jak znaleźć przyczynę (traceback, print, debugger), zamiast tylko podać poprawkę.\n"
             "- Testów w katalogu WERYFIKATORY nie zmieniaj — to egzamin.\n"
             "- Nie proś o hasła, klucze API ani dane osobowe.\n")

SZABLONY = {
    "bug_raport": ("## BUG-NN: [miejsce]: [co nie działa] [w jakich warunkach]\n"
                   "**Środowisko:** wersja aplikacji, system, przeglądarka i wersja, adres\n"
                   "**Ważność:** krytyczna / wysoka / średnia / niska · **Powtarzalność:** zawsze (N/N) / sporadycznie\n"
                   "**Warunki wstępne:** …\n**Kroki:**\n1. …\n2. …\n**Oczekiwany wynik:** …\n**Rzeczywisty wynik:** …\n**Dowód:** zrzut / log\n"),
    "przypadek_testowy": "| ID | Tytuł | Warunki wstępne | Kroki | Dane | Oczekiwany wynik |\n|---|---|---|---|---|---|\n| TC-01 |  |  |  |  |  |\n",
    "plan_testow": ("# Plan testów — [projekt]\n\n## Zakres\n## Poza zakresem\n## Ryzyka\n## Poziomy i techniki\n## Co automatyzuję, co testuję ręcznie\n## Środowisko\n## Kryteria zakończenia\n"),
}

CHECKLISTA = [
    {"po": "Po tygodniu 0", "punkty": ["Środowisko kursu zielone, git --version działa", "Repozytorium nauka-python na GitHubie z pierwszym commitem", "CLAUDE.md z zasadami nauki"]},
    {"po": "Po etapie 1 (tydzień 3)", "punkty": ["Piszę bez pomocy funkcję z warunkami i pętlą", "Rozróżniam return i print", "Czytam traceback i łapię konkretny wyjątek", "Program z menu: logika w funkcjach, input w bloku main"]},
    {"po": "Po etapie 2 (tydzień 6)", "punkty": ["Czytam CSV do listy słowników i liczę statystyki", "Gałąź → PR → merge bez pomocy", "Klasa z walidacją w metodach", "venv + requirements.txt + .gitignore", "README, które pozwala uruchomić projekt obcej osobie"]},
    {"po": "Po etapie 3 (tydzień 9)", "punkty": ["Tabela klas równoważności i wartości brzegowych dla reguły", "Testy pytest łapią mutanta", "Testy Selenium w POM bez time.sleep", "Raport błędu odtwarzalny bez pytań", "Zielone CI z raportem HTML"]},
    {"po": "Po kursie (tydzień 12)", "punkty": ["Projekt Magazyn z testami na dwóch poziomach i zielonym CI", "PLAN_TESTOW.md i raporty błędów", "CV z sekcją Projekty", "Opowieść o projekcie w 2 minuty", "5 aplikacji w dzienniku"]},
]

SCIAGA = [
    {"tytul": "Mentor — środowisko i ćwiczenia", "pozycje": [
        ["Środowisko → Sprawdź / Napraw", "Python 3.11–3.13 i biblioteki kursu w osobnym .venv"],
        ["📝 Utwórz plik ćwiczenia", "plik zadania w katalogu roboczym PRACA (z szablonem)"],
        ["▶ Uruchom", "uruchamia plik w środowisku kursu; dane dla input() w polu nad wynikiem"],
        ["✔ Sprawdź wynik", "niezależny test z paczki kursu (WERYFIKATORY) albo sprawdzenie wyjścia"],
        ["Mój projekt → Skopiuj materiały kursu", "dane/, przyklady/, projekty/sklep_testowy do PRACA"]]},
    {"tytul": "Terminal (PowerShell)", "pozycje": [["pwd / ls / cd nazwa / cd ..", "gdzie jestem / pliki / wejdź / wyjdź"], ["mkdir nazwa", "nowy katalog"],
                                                  ["python plik.py", "uruchom program"], ["python -m pytest -v", "uruchom testy"], ["Ctrl+C", "przerwij program"]]},
    {"tytul": "Git — codzienne komendy", "pozycje": [
        ["git status", "co się zmieniło"], ["git add plik / git add .", "do poczekalni"], ["git commit -m \"Dodaj …\"", "zapis w historii"], ["git push", "wyślij na GitHub"],
        ["git switch -c feature/x", "nowa gałąź"], ["git diff", "zmiany niezacommitowane"], ["git log --oneline --graph", "historia"],
        ["git restore plik", "cofnij niezapisane zmiany w pliku"], ["git stash / git stash pop", "odłóż / przywróć zmiany"], ["git revert <sha>", "odwróć wysłany commit"]]},
    {"tytul": "pytest", "pozycje": [["test_*.py, def test_*()", "pytest sam znajduje testy"], ["assert a == b", "sprawdzenie"], ["pytest.raises(ValueError)", "test wyjątku"],
                                    ["pytest.approx(0.3)", "porównanie float"], ["@pytest.mark.parametrize", "wiele przypadków"], ["@pytest.fixture / tmp_path", "dane testowe / katalog tymczasowy"],
                                    ["-v / -k nazwa / -x", "szczegóły / wybór / stop na błędzie"]]},
    {"tytul": "Selenium", "pozycje": [["webdriver.Edge() / .Chrome()", "przeglądarka (sterownik: Selenium Manager)"], ["driver.get(url)", "otwórz stronę"],
                                      ["find_element(By.ID, \"x\")", "jeden element (brak → NoSuchElementException)"], ["By.CSS_SELECTOR \"[data-test=x]\"", "stabilny lokator"],
                                      ["WebDriverWait(d, 10).until(EC.visibility_of_element_located(loc))", "czekanie na warunek"], ["driver.quit()", "zawsze na końcu"]]},
    {"tytul": "Testowanie — pojęcia ISTQB", "pozycje": [["pomyłka → defekt → awaria", "człowiek → wada w kodzie → widoczny skutek"],
                                                       ["klasy równoważności", "jeden reprezentant z każdej grupy danych"], ["wartości brzegowe", "granice i ich sąsiedzi: 0, 1, 50, 51"],
                                                       ["piramida testów", "dużo jednostkowych, mało E2E"], ["regresja", "defekt wracający po zmianie — chronią testy automatyczne w CI"]]},
]

LINKI = [["Python — Poradnik (po polsku)", "https://docs.python.org/pl/3/tutorial/"], ["Pro Git (po polsku)", "https://git-scm.com/book/pl/v2"],
         ["pytest — dokumentacja", "https://docs.pytest.org/en/stable/getting-started.html"], ["Selenium — dokumentacja", "https://selenium.dev/documentation/selenium_manager"],
         ["ISTQB CTFL 4.0", "https://istqb.org/certifications/certified-tester-foundation-level-ctfl-v4-0"], ["Słownik ISTQB (PL)", "https://glossary.istqb.org/"],
         ["Flask — dokumentacja", "https://flask.palletsprojects.com/"], ["GitHub Actions — Python", "https://docs.github.com/en/actions/tutorials/build-and-test-code/python"],
         ["OWASP — SQL Injection Prevention", "https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html"]]

POJECIA = {
    "zmienna": "Zmienna to pudełko z etykietą na wartość: cena = 4.50. Znak = przypisuje (wkłada do pudełka), nie porównuje.",
    "funkcja": "Funkcja to przepis z nazwą: dostaje parametry, zwraca wynik przez return. Testy wywołują funkcje i sprawdzają, co zwracają.",
    "pętla": "Pętla powtarza czynność: for — dla każdego elementu kolekcji, while — dopóki warunek jest prawdziwy (coś musi go zmienić).",
    "lista": "Lista to uporządkowany ciąg elementów w [ ]; indeksy od 0, -1 to ostatni.",
    "słownik": "Słownik to pary klucz: wartość w { }; d.get(k, 0) czyta bezpiecznie.",
    "wyjątek": "Wyjątek to błąd w czasie działania (ValueError, KeyError…); łapiesz go try/except, zgłaszasz raise.",
    "traceback": "Traceback to raport błędu Pythona: ostatnia linia — typ i opis, wyżej — plik i numer linii.",
    "klasa": "Klasa to wzór obiektów: dane (atrybuty self.x) i operacje (metody); obiekt to konkretny egzemplarz.",
    "moduł": "Moduł to plik .py, który importujesz: import zadania / from zadania import dodaj.",
    "venv": "Środowisko wirtualne — osobny Python z pakietami jednego projektu; zależności zapisujesz w requirements.txt.",
    "git": "Git zapisuje historię zmian w commitach; gałęzie oddzielają pracę, pull request służy do recenzji i scalenia.",
    "api": "API to okienko programu dla innych programów: żądanie HTTP (GET, POST) → odpowiedź z kodem (200, 404, 500) i danymi (JSON).",
    "test": "Test to automatyczne sprawdzenie: dane → wywołanie → assert oczekiwanego wyniku. Dobry test pada na zepsutym kodzie.",
    "pytest": "pytest uruchamia funkcje test_* z plików test_*.py; parametrize daje wiele przypadków, fixture — wspólne dane.",
    "defekt": "Defekt to wada w kodzie lub dokumencie; awaria to jej widoczny skutek; pomyłka — działanie człowieka, które ją spowodowało.",
    "wartości brzegowe": "Technika testowania: sprawdzasz granice przedziałów i ich sąsiadów (dla 1–50: 0, 1, 50, 51), bo tam najczęściej siedzą defekty.",
    "klasy równoważności": "Technika testowania: dzielisz dane na grupy traktowane tak samo i bierzesz po jednym reprezentancie z każdej.",
    "selenium": "Selenium WebDriver steruje przeglądarką z kodu: otwiera strony, szuka elementów lokatorami, klika i wpisuje.",
    "page object": "Page Object Model: klasa strony z lokatorami i metodami akcji; testy wołają metody, asercje są w testach.",
    "ci": "Ciągła integracja: przy każdym pushu serwer instaluje środowisko i uruchamia testy (GitHub Actions).",
    "sql injection": "Atak, w którym dane użytkownika stają się kodem SQL; obrona — zapytania parametryzowane (?).",
    "bug raport": "Raport błędu: tytuł (gdzie + co + warunek), środowisko, kroki, oczekiwany i rzeczywisty wynik, ważność, dowód.",
}

BLEDY = {
    "SyntaxError": {"co": "Błąd składni: brakujący nawias, cudzysłów albo dwukropek po if/for/def. Sprawdź wskazaną linię i tę przed nią.", "pytanie": "Przeczytaj ostatnią linię tracebacku i linię wskazaną w File … line N — co jest tam inaczej, niż zakładasz?"},
    "IndentationError": {"co": "Złe wcięcie: po linii z dwukropkiem blok musi być wcięty 4 spacjami; nie mieszaj Tab ze spacjami.", "pytanie": "Przeczytaj ostatnią linię tracebacku i linię wskazaną w File … line N — co jest tam inaczej, niż zakładasz?"},
    "NameError": {"co": "Nazwa nieznana: literówka, wielkość liter albo zmienna/moduł użyte przed utworzeniem/importem.", "pytanie": "Przeczytaj ostatnią linię tracebacku i linię wskazaną w File … line N — co jest tam inaczej, niż zakładasz?"},
    "TypeError": {"co": "Zły typ: np. \"a\" + 1, brak argumentu funkcji albo metoda bez self.", "pytanie": "Przeczytaj ostatnią linię tracebacku i linię wskazaną w File … line N — co jest tam inaczej, niż zakładasz?"},
    "ValueError": {"co": "Zła wartość: int(\"abc\"), float(\"4,5\") albo Twój raise przy złych danych.", "pytanie": "Przeczytaj ostatnią linię tracebacku i linię wskazaną w File … line N — co jest tam inaczej, niż zakładasz?"},
    "ZeroDivisionError": {"co": "Dzielenie przez zero", "pytanie": "sprawdź mianownik (pusta lista?) przed dzieleniem."},
    "IndexError": {"co": "Indeks poza listą", "pytanie": "ostatni element to lista[-1] albo lista[len(lista) - 1]."},
    "KeyError": {"co": "Brak klucza w słowniku", "pytanie": "użyj d.get(klucz) albo sprawdź `in`."},
    "AttributeError": {"co": "Obiekt nie ma takiej metody/atrybutu", "pytanie": "sprawdź typ (print(type(x))) i pisownię."},
    "FileNotFoundError": {"co": "Plik nie istnieje w katalogu roboczym", "pytanie": "sprawdź os.getcwd() i nazwę z rozszerzeniem."},
    "ModuleNotFoundError": {"co": "Moduł niezainstalowany w tym Pythonie albo plik w innym katalogu", "pytanie": "uruchamiaj w środowisku kursu (▶ w Mentorze)."},
    "NoSuchElementException": {"co": "Selenium nie znalazł elementu", "pytanie": "popraw lokator (DevTools) albo czekaj WebDriverWait."},
    "TimeoutException": {"co": "Warunek WebDriverWait nie spełnił się w czasie", "pytanie": "zły lokator albo element się nie pojawił (defekt?)."},
}

PYTANIA_REKRUTACYJNE = [
    ("Czym różni się defekt od awarii?", "Defekt to wada w kodzie/produkcie, awaria to jej widoczny skutek podczas działania; pomyłka to działanie człowieka, które wprowadziło defekt."),
    ("Jak dobierzesz przypadki testowe dla pola „ilość 1–50”?", "Klasy równoważności (<1, 1–50, >50, nie-liczba) i wartości brzegowe 0, 1, 50, 51."),
    ("Czym jest piramida testów?", "Dużo szybkich testów jednostkowych, mniej integracyjnych, najmniej E2E."),
    ("Jak przetestujesz formularz logowania?", "Poprawne dane, złe hasło, pusty login/hasło, wielkość liter, spacje, długie dane, blokada po próbach, komunikaty, bezpieczeństwo (SQL injection, hasło w adresie), E2E dla ścieżki krytycznej."),
    ("Co zawiera dobry raport błędu?", "Tytuł gdzie+co+warunek, środowisko, kroki, dane, oczekiwany i rzeczywisty wynik, ważność, powtarzalność, dowód."),
    ("Ważność a priorytet?", "Ważność = wpływ defektu; priorytet = pilność naprawy, ustala zespół."),
    ("Czym jest test regresji?", "Sprawdzenie, że zmiana nie zepsuła tego, co działało; najlepiej automatycznie w CI."),
    ("Dlaczego WebDriverWait, a nie time.sleep?", "Czeka na konkretny warunek — szybciej i stabilniej; sleep jest za krótki albo za długi."),
    ("Co to Page Object Model?", "Klasa strony z lokatorami i metodami akcji; testy czytelne, zmiana lokatora w jednym miejscu."),
    ("Do czego służy fixture w pytest?", "Przygotowuje dane/zasoby dla testu (i sprząta po yield); każdy test dostaje świeże dane."),
    ("Co robi parametrize?", "Uruchamia ten sam test dla wielu zestawów danych — jak tabela przypadków."),
    ("Jak działa CI w Twoim projekcie?", "GitHub Actions przy pushu instaluje requirements.txt i uruchamia pytest, raport HTML jako artefakt, odznaka w README."),
    ("Co to SQL injection i jak się bronić?", "Dane wklejone w zapytanie stają się kodem SQL; zapytania parametryzowane (?)."),
    ("GET a POST? Kody 200/400/404/500?", "GET pobiera, POST wysyła; 200 OK, 400 złe dane, 404 brak zasobu, 500 błąd serwera."),
    ("Różnica między return a print w funkcji?", "return oddaje wartość do dalszego użycia i testów, print tylko wyświetla."),
    ("Jak sprawdzisz, że Twój test coś testuje?", "Celowo psuję kod (mutacja) — dobry test musi paść."),
]

TEMATY_WPISU = ["Zmienne i typy", "Warunki i wartości brzegowe", "Pętle", "Listy", "Napisy", "Funkcje i return", "Słowniki", "Wyjątki", "random i datetime",
                "Pliki i CSV", "Git: gałęzie i PR", "Klasy", "Moduły", "venv", "API i requests", "Debugowanie", "README", "Techniki testowania",
                "pytest", "parametrize i fixtures", "Selenium", "Page Object Model", "Raporty błędów", "CI", "SQLite", "Flask", "Testy aplikacji", "Rekrutacja"]

WSKAZOWKI = [
    "Uruchamiaj kod co kilka linii — błąd szybciej znaleziony to błąd łatwiejszy.",
    "Zanim uruchomisz, przewidź wynik. Różnica między przewidywaniem a wynikiem to najcenniejsza lekcja.",
    "Ostatnia linia tracebacku mówi, CO; linia File … line N mówi, GDZIE.",
    "Nazwa testu jak zdanie z wymagania: test_dostawa_darmowa_od_100.",
    "Mały commit z dobrym opisem po każdym działającym kroku.",
    "Wartości brzegowe przed losowymi: 0, 1, granica, granica + 1.",
    "Gdy utkniesz na 20 minut — wskazówka 1 w ćwiczeniu, potem asystent z promptem „Błąd w kodzie”.",
]

MOTYWACJA_POWROT = ["Dobrze, że wracasz. Zacznij od powtórki ostatniej lekcji — 15 minut wystarczy, żeby wejść w rytm.",
                    "Przerwa to nie porażka. Mentor pokazuje, gdzie skończyłeś(-aś); jedna lekcja dziś to krok do przodu.",
                    "Nie nadrabiaj wszystkiego naraz — wróć do planu tydzień po tygodniu."]

ZRODLA_DODATKOWE = [Z.PY_315, Z.PYTEST_CHANGES, Z.ISTQB_CTFL, Z.SJSI_CTFL_PL, Z.RYNEK_JJ, Z.RYNEK_BDJ]
