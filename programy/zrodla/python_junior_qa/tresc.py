# -*- coding: utf-8 -*-
"""
Treści programu nauki — plan 12 tygodni, quizy, prompty, odznaki.
Ten plik to "podręcznik" aplikacji. Możesz go edytować: dodać zadania,
pytania do quizu albo własne szablony promptów.
"""

# ---------------------------------------------------------------------------
# ETAPY
# ---------------------------------------------------------------------------
ETAPY = [
    {"nr": 0, "nazwa": "Konfiguracja", "tygodnie": [0],
     "cel": "Działający terminal, Python, Git, PyCharm i Claude Code. Pusty projekt nauka-python na GitHubie."},
    {"nr": 1, "nazwa": "Podstawy Pythona", "tygodnie": [1, 2, 3],
     "cel": "Piszesz bez pomocy program na 50–100 linii z funkcjami, pętlami i listami i rozumiesz każdą linię."},
    {"nr": 2, "nazwa": "Git, struktura projektu, prawdziwe programy", "tygodnie": [4, 5, 6],
     "cel": "Organizujesz kod w kilka plików, pracujesz na gałęziach Gita, używasz bibliotek. Czytasz cudzy kod."},
    {"nr": 3, "nazwa": "Testowanie — pytest, Selenium, automatyzacja QA", "tygodnie": [7, 8, 9],
     "cel": "Testy jednostkowe w pytest, testy przeglądarkowe w Selenium, pipeline testów na GitHubie."},
    {"nr": 4, "nazwa": "Projekt portfolio i rekrutacja", "tygodnie": [10, 11, 12],
     "cel": "Jeden dopracowany projekt, o którym opowiesz 10 minut, i CV potwierdzone kodem z GitHuba."},
]

# ---------------------------------------------------------------------------
# PLAN TYGODNI
# Każde zadanie: id, tytul, opis, pliki (do wykrywania w katalogu projektu), xp
# Zadania 1–4 = pon–czw, zadanie 5 = piątek (większe).
# ---------------------------------------------------------------------------
PROGRAM = [
    {
        "tydzien": 0, "etap": 0, "tytul": "Konfiguracja",
        "tematy": "Terminal, Python, Git, PyCharm, Claude Code, pierwszy commit",
        "rola_claude": "Przewodnik po narzędziach. Każdą komendę ma wytłumaczyć, zanim ją uruchomicie.",
        "zadania": [
            {"id": "t0z1", "tytul": "Zainstaluj Pythona, Gita, PyCharm i Claude Code",
             "opis": "python --version, git --version, claude --version, a potem claude doctor bez błędów. "
                     "Na Windows przy instalacji Pythona zaznacz „Add Python to PATH”.",
             "pliki": [], "xp": 10},
            {"id": "t0z2", "tytul": "Katalog nauka-python z plikiem CLAUDE.md",
             "opis": "Uruchom claude w katalogu, wpisz /init, a potem dopisz zasady nauki (zakładka Prompty → CLAUDE.md).",
             "pliki": ["CLAUDE.md"], "xp": 10},
            {"id": "t0z3", "tytul": "hello.py wypisuje Twoje imię i dzisiejszą datę",
             "opis": "Poproś Claude: „Wytłumacz mi, czym jest terminal, katalog roboczy i plik .py — jak dziesięciolatkowi. "
                     "Potem poprowadź mnie krok po kroku. Nie twórz pliku za mnie.”",
             "pliki": ["hello.py"], "xp": 10},
            {"id": "t0z4", "tytul": "Repozytorium nauka-python na GitHubie z pierwszym commitem",
             "opis": "„Poprowadź mnie przez git init, pierwszy commit i wypchnięcie na GitHub — tłumacz każdą komendę.”",
             "pliki": [".git"], "xp": 10},
            {"id": "t0z5", "tytul": "Piątek: zmienna, funkcja i pętla — własnymi słowami",
             "opis": "„Wytłumacz mi, co to jest zmienna, funkcja i pętla — bez kodu, na przykładach z gospodarstwa.” "
                     "Zapisz własnymi słowami w notatki.md.",
             "pliki": ["notatki.md"], "xp": 25},
        ],
    },
    {
        "tydzien": 1, "etap": 1, "tytul": "Zmienne, typy, warunki",
        "tematy": "Zmienne, typy (int, str, float, bool), print, input, operatory, if/elif/else, komentarze",
        "rola_claude": "Tylko podpowiada. Minimum 15 minut własnej walki, zanim zapytasz.",
        "zadania": [
            {"id": "t1z1", "tytul": "zmienne.py — 5 zmiennych różnych typów",
             "opis": "Wypisz każdą zmienną razem z jej type().", "pliki": ["zmienne.py"], "xp": 10},
            {"id": "t1z2", "tytul": "kalkulator.py — dwie liczby i działanie",
             "opis": "Program pyta o dwie liczby i działanie, wypisuje wynik. Dzielenie przez zero obsłużone if-em.",
             "pliki": ["kalkulator.py"], "xp": 10},
            {"id": "t1z3", "tytul": "wiek.py — rok urodzenia → wiek",
             "opis": "Liczy wiek i mówi, czy osoba jest pełnoletnia.", "pliki": ["wiek.py"], "xp": 10},
            {"id": "t1z4", "tytul": "litry.py — mleko na kilogramy i cenę skupu",
             "opis": "Trzy progi cenowe obsłużone przez if/elif/else.", "pliki": ["litry.py"], "xp": 10},
            {"id": "t1z5", "tytul": "Piątek: Kalkulator BMI",
             "opis": "Pyta o wzrost i wagę, wypisuje BMI i kategorię (niedowaga / norma / nadwaga). Obsługa błędnego wpisu.",
             "pliki": ["bmi.py", "kalkulator_bmi.py"], "xp": 25},
        ],
    },
    {
        "tydzien": 2, "etap": 1, "tytul": "Pętle i listy",
        "tematy": "Pętle for i while, listy, range, len, metody napisów, break/continue",
        "rola_claude": "Tylko podpowiada. Każdy fragment kodu od Claude przepisujesz ręcznie.",
        "zadania": [
            {"id": "t2z1", "tytul": "tabliczka.py — tabliczka mnożenia 1–10",
             "opis": "Pętlą for. Spróbuj też wersji z zagnieżdżoną pętlą.", "pliki": ["tabliczka.py"], "xp": 10},
            {"id": "t2z2", "tytul": "lista_zakupow.py — 5 produktów",
             "opis": "Dodaj, usuń, wypisz z numerami.", "pliki": ["lista_zakupow.py"], "xp": 10},
            {"id": "t2z3", "tytul": "suma.py — pętla while do wpisania 0",
             "opis": "Wypisz sumę, średnią i maksimum podanych liczb.", "pliki": ["suma.py"], "xp": 10},
            {"id": "t2z4", "tytul": "napisy.py — operacje na tekście",
             "opis": "Wielkimi literami, od tyłu, policz samogłoski.", "pliki": ["napisy.py"], "xp": 10},
            {"id": "t2z5", "tytul": "Piątek: Zgadnij liczbę",
             "opis": "Losowa liczba 1–100, podpowiedzi „za mało / za dużo”, licznik prób, lista najlepszych wyników.",
             "pliki": ["zgadnij.py", "zgadnij_liczbe.py", "gra.py"], "xp": 25},
        ],
    },
    {
        "tydzien": 3, "etap": 1, "tytul": "Funkcje, słowniki, błędy",
        "tematy": "Funkcje (argumenty, return), słowniki, krotki, moduły (random, datetime), try/except",
        "rola_claude": "Tylko podpowiada. Po tym tygodniu — checklista etapu 1.",
        "zadania": [
            {"id": "t3z1", "tytul": "funkcje.py — 5 funkcji z docstringami",
             "opis": "Pole prostokąta, czy parzysta, maksimum z listy, odwróć napis, silnia.",
             "pliki": ["funkcje.py"], "xp": 10},
            {"id": "t3z2", "tytul": "slownik.py — zwierzę → waga",
             "opis": "Dodaj, zmień, usuń, wypisz posortowane po wadze.", "pliki": ["slownik.py"], "xp": 10},
            {"id": "t3z3", "tytul": "bledy.py — try/except w pętli",
             "opis": "Pytaj o liczbę; zły wpis nie przerywa programu.", "pliki": ["bledy.py"], "xp": 10},
            {"id": "t3z4", "tytul": "losowanie.py — random i datetime",
             "opis": "Losuj 3 zwierzęta z listy do kontroli i wypisz datę kontroli za 7 dni.",
             "pliki": ["losowanie.py"], "xp": 10},
            {"id": "t3z5", "tytul": "Piątek: Menedżer zadań w konsoli",
             "opis": "Menu w pętli, każda operacja osobną funkcją, zadania w liście słowników.",
             "pliki": ["menedzer.py", "menedzer_zadan.py", "zadania.py"], "xp": 25},
        ],
    },
    {
        "tydzien": 4, "etap": 2, "tytul": "Git i pliki",
        "tematy": "Gałęzie, git log, git diff, cofanie zmian, pull request. Pliki: open, read, write, CSV",
        "rola_claude": "Może pisać fragmenty — ale zanim ich użyjesz, tłumaczysz mu je linijka po linijce.",
        "zadania": [
            {"id": "t4z1", "tytul": "Gałąź feature/csv i pull request",
             "opis": "Zmiany na gałęzi, git diff, git log, scalenie przez pull request na GitHubie.",
             "pliki": [], "xp": 10},
            {"id": "t4z2", "tytul": "zapis.py — zapis i odczyt stado.txt",
             "opis": "Drugi raz zrób to samo z with open i porównaj.", "pliki": ["zapis.py"], "xp": 10},
            {"id": "t4z3", "tytul": "csv_odczyt.py — moduł csv",
             "opis": "Wczytaj stado.csv (nr, imię, rasa, waga), policz średnią wagę.",
             "pliki": ["csv_odczyt.py"], "xp": 10},
            {"id": "t4z4", "tytul": "git stash i git checkout -- plik",
             "opis": "Celowo zepsuj plik, odzyskaj go dwoma sposobami, poproś Claude o wyjaśnienie różnicy.",
             "pliki": [], "xp": 10},
            {"id": "t4z5", "tytul": "Piątek: Dziennik stada w CSV",
             "opis": "Dodawanie zwierząt, statystyki (liczba, średnia, najcięższe), wyszukiwanie po rasie.",
             "pliki": ["dziennik_stada.py", "dziennik.py", "stado.py"], "xp": 25},
        ],
    },
    {
        "tydzien": 5, "etap": 2, "tytul": "Klasy, moduły, biblioteki",
        "tematy": "Klasy i obiekty, podział na moduły, venv, pip, requests",
        "rola_claude": "Tryb planowania przed większym zadaniem. Czytasz plan, dopiero potem kodujesz.",
        "zadania": [
            {"id": "t5z1", "tytul": "zwierze.py — klasa Zwierze",
             "opis": "Atrybuty, metoda opis(), 3 obiekty.", "pliki": ["zwierze.py"], "xp": 10},
            {"id": "t5z2", "tytul": "Menedżer zadań w 3 plikach",
             "opis": "main.py, zadania.py, plik.py — każdy z jasną odpowiedzialnością.",
             "pliki": ["main.py", "plik.py"], "xp": 10},
            {"id": "t5z3", "tytul": "venv, pip install requests, requirements.txt",
             "opis": "python -m venv .venv, aktywacja, .gitignore z wpisem .venv.",
             "pliki": ["requirements.txt", ".gitignore"], "xp": 10},
            {"id": "t5z4", "tytul": "api.py — dane z publicznego API",
             "opis": "Np. open-meteo.com. Wypisz 3 pola z odpowiedzi JSON.", "pliki": ["api.py"], "xp": 10},
            {"id": "t5z5", "tytul": "Piątek: Pogoda dla Radzynia",
             "opis": "Prognoza na 3 dni zapisana do CSV z datą, ostrzeżenie o przymrozku.",
             "pliki": ["pogoda.py"], "xp": 25},
        ],
    },
    {
        "tydzien": 6, "etap": 2, "tytul": "Czytanie kodu i refaktoryzacja",
        "tematy": "Czytanie cudzego kodu, debugger PyCharm, README, docstringi",
        "rola_claude": "Recenzent. Na koniec tygodnia ocenia Twoje repo „oczami rekrutera”.",
        "zadania": [
            {"id": "t6z1", "tytul": "Debugger: 80-liniowy program z 3 błędami",
             "opis": "Poproś Claude o program z ukrytymi błędami. Znajdź je breakpointami, krok po kroku.",
             "pliki": [], "xp": 10},
            {"id": "t6z2", "tytul": "Cudzy projekt z GitHuba opisany w notatki.md",
             "opis": "Mały projekt (np. kalkulator). Opisz, co robi każdy plik.", "pliki": ["notatki.md"], "xp": 10},
            {"id": "t6z3", "tytul": "Refaktoryzacja BMI i zgadywanki",
             "opis": "Funkcje, docstringi, poprawki po recenzji Claude.", "pliki": [], "xp": 10},
            {"id": "t6z4", "tytul": "README dla każdego z 6 projektów",
             "opis": "Co robi, jak uruchomić, zrzut ekranu z konsoli.", "pliki": ["README.md"], "xp": 10},
            {"id": "t6z5", "tytul": "Piątek: Porządek w GitHubie",
             "opis": "Jedno repo python-projekty z folderem na projekt i głównym README. Ocena „oczami rekrutera”.",
             "pliki": [], "xp": 25},
        ],
    },
    {
        "tydzien": 7, "etap": 3, "tytul": "pytest",
        "tematy": "Czym jest test; assert, nazewnictwo, fixtures, parametrize, pytest -v; piramida testów",
        "rola_claude": "Claude pisze kod, Ty piszesz testy — i odwrotnie. Celowe błędy do znalezienia.",
        "zadania": [
            {"id": "t7z1", "tytul": "test_funkcje.py — 5 testów",
             "opis": "pip install pytest; testy do funkcji z tygodnia 3; pytest -v.",
             "pliki": ["test_funkcje.py"], "xp": 10},
            {"id": "t7z2", "tytul": "parametrize — 6 przypadków BMI w jednym teście",
             "opis": "@pytest.mark.parametrize z listą (wzrost, waga, oczekiwana kategoria).",
             "pliki": ["test_bmi.py"], "xp": 10},
            {"id": "t7z3", "tytul": "Fixture z menedżerem zadań",
             "opis": "Fixture tworzy menedżer z 3 zadaniami; użyta w 4 testach.",
             "pliki": ["test_menedzer.py", "test_zadania.py", "conftest.py"], "xp": 10},
            {"id": "t7z4", "tytul": "Ukryty błąd w dzienniku stada",
             "opis": "„Wprowadź do @dziennik_stada.py jeden ukryty błąd. Nie mów jaki.” Znajdź go testem, napraw.",
             "pliki": [], "xp": 10},
            {"id": "t7z5", "tytul": "Piątek: 15+ testów z przypadkami brzegowymi",
             "opis": "Menedżer zadań i dziennik stada: pusta lista, zły typ, duplikat.",
             "pliki": ["test_dziennik.py", "test_stado.py"], "xp": 25},
        ],
    },
    {
        "tydzien": 8, "etap": 3, "tytul": "Selenium",
        "tematy": "WebDriver, lokatory (id, CSS, XPath), formularze, WebDriverWait, Page Object Model",
        "rola_claude": "Pyta o zgodę przed każdą komendą — widzisz, jak wygląda pip install selenium i pytest.",
        "zadania": [
            {"id": "t8z1", "tytul": "Pierwszy skrypt Selenium — saucedemo.com",
             "opis": "pip install selenium; otwórz stronę, zaloguj się, zrób zrzut ekranu.",
             "pliki": ["saucedemo.py", "selenium_start.py"], "xp": 10},
            {"id": "t8z2", "tytul": "Lokatory — 5 elementów trzema sposobami",
             "opis": "the-internet.herokuapp.com: id, CSS, XPath.", "pliki": ["lokatory.py"], "xp": 10},
            {"id": "t8z3", "tytul": "Formularz z WebDriverWait",
             "opis": "Wypełnij, wyślij, sprawdź komunikat. Bez time.sleep.", "pliki": ["formularz.py"], "xp": 10},
            {"id": "t8z4", "tytul": "Page Object Model — LoginPage",
             "opis": "Metody open(), login(), error_text() dla MeridianBank.",
             "pliki": ["login_page.py"], "xp": 10},
            {"id": "t8z5", "tytul": "Piątek: 5 testów end-to-end MeridianBank",
             "opis": "Logowanie, błędne hasło, przelew, saldo, wylogowanie — każdy w POM.",
             "pliki": ["test_meridianbank.py", "test_login.py"], "xp": 25},
        ],
    },
    {
        "tydzien": 9, "etap": 3, "tytul": "Proces QA i CI",
        "tematy": "Przypadki testowe, bug raporty, GitHub Actions, pytest-html",
        "rola_claude": "Ocenia bug raporty: czy programista zrozumie bez pytań.",
        "zadania": [
            {"id": "t9z1", "tytul": "10 przypadków testowych w tabeli",
             "opis": "ID, warunki wstępne, kroki, oczekiwany wynik — dla MeridianBank.",
             "pliki": ["przypadki_testowe.md"], "xp": 10},
            {"id": "t9z2", "tytul": "3 bug raporty z własnych znalezisk",
             "opis": "Tytuł, kroki, oczekiwany vs rzeczywisty, środowisko. Claude ocenia zrozumiałość.",
             "pliki": ["bug_raporty.md", "bugi.md"], "xp": 10},
            {"id": "t9z3", "tytul": "GitHub Actions — tests.yml",
             "opis": ".github/workflows/tests.yml uruchamia pytest przy każdym pushu. Zielony znacznik.",
             "pliki": ["tests.yml"], "xp": 10},
            {"id": "t9z4", "tytul": "pytest-html — raport jako artefakt CI",
             "opis": "pip install pytest-html; raport HTML dodany do workflow.", "pliki": [], "xp": 10},
            {"id": "t9z5", "tytul": "Piątek: Repozytorium meridianbank-tests",
             "opis": "POM, 15+ testów, raport HTML, odznaka CI w README.", "pliki": [], "xp": 25},
        ],
    },
    {
        "tydzien": 10, "etap": 4, "tytul": "Projekt: rdzeń",
        "tematy": "Planowanie zakresu, SQLite, moduły z testami",
        "rola_claude": "Partner do planowania (tryb planowania). Kod piszesz modułami, każdy z testami.",
        "zadania": [
            {"id": "t10z1", "tytul": "PLAN.md — zakres, struktura, kolejność",
             "opis": "W trybie planowania: ewidencja zwierząt, zdarzenia, zapis do SQLite.",
             "pliki": ["PLAN.md"], "xp": 10},
            {"id": "t10z2", "tytul": "baza.py — SQLite",
             "opis": "Tabele zwierzeta i zdarzenia; funkcje dodaj/pobierz/usuń.", "pliki": ["baza.py"], "xp": 10},
            {"id": "t10z3", "tytul": "stado.py — logika",
             "opis": "Rejestracja zwierzęcia, zdarzenie (szczepienie, wycielenie), lista zdarzeń po dacie.",
             "pliki": ["stado.py"], "xp": 10},
            {"id": "t10z4", "tytul": "Testy pytest z bazą tymczasową",
             "opis": "Fixture tworząca tymczasową bazę SQLite dla baza.py i stado.py.",
             "pliki": ["test_baza.py", "test_stado.py"], "xp": 10},
            {"id": "t10z5", "tytul": "Piątek: Działający rdzeń",
             "opis": "Konsolowe menu do obsługi stada, 20+ testów, CI zielone.", "pliki": [], "xp": 25},
        ],
    },
    {
        "tydzien": 11, "etap": 4, "tytul": "Projekt: interfejs webowy",
        "tematy": "Flask, formularze z walidacją, testy Selenium w CI",
        "rola_claude": "Pomaga przy Flasku, ale każdą stronę tłumaczysz mu, zanim ją dodasz.",
        "zadania": [
            {"id": "t11z1", "tytul": "Flask — strona główna z listą zwierząt",
             "opis": "pip install flask; dane z bazy SQLite.", "pliki": ["app.py"], "xp": 10},
            {"id": "t11z2", "tytul": "Formularz dodawania zwierzęcia z walidacją",
             "opis": "Puste pole, zła waga — komunikaty dla użytkownika.", "pliki": [], "xp": 10},
            {"id": "t11z3", "tytul": "Strona historii zdarzeń zwierzęcia",
             "opis": "Lista zdarzeń jednego zwierzęcia po dacie.", "pliki": [], "xp": 10},
            {"id": "t11z4", "tytul": "3 testy Selenium w POM w CI",
             "opis": "Lista, dodanie, historia — uruchamiane w GitHub Actions.",
             "pliki": ["test_web.py", "test_selenium.py"], "xp": 10},
            {"id": "t11z5", "tytul": "Piątek: Aplikacja jedną komendą",
             "opis": "python app.py; testy jednostkowe i Selenium zielone w GitHub Actions.", "pliki": [], "xp": 25},
        ],
    },
    {
        "tydzien": 12, "etap": 4, "tytul": "Projekt: dopracowanie i rekrutacja",
        "tematy": "README, plan testów, bug raporty, recenzja seniora, rozmowa rekrutacyjna, CV",
        "rola_claude": "Senior tester przed code review i rekruter na próbnej rozmowie.",
        "zadania": [
            {"id": "t12z1", "tytul": "README z zrzutami i sekcją „Jak testuję”",
             "opis": "Opis, zrzuty ekranu, instrukcja uruchomienia.", "pliki": ["README.md"], "xp": 10},
            {"id": "t12z2", "tytul": "PLAN_TESTOW.md + 3 bug raporty",
             "opis": "Zakres, przypadki, co zautomatyzowane, co manualne.", "pliki": ["PLAN_TESTOW.md"], "xp": 10},
            {"id": "t12z3", "tytul": "Recenzja jak senior tester",
             "opis": "„Oceń projekt jak senior tester przed code review.” Wdróż 3 najważniejsze uwagi.",
             "pliki": [], "xp": 10},
            {"id": "t12z4", "tytul": "Sesja rekrutacyjna: 15 pytań + nagranie",
             "opis": "Manual, pytest/Selenium, projekt. Nagraj 2-minutową opowieść o projekcie.",
             "pliki": [], "xp": 10},
            {"id": "t12z5", "tytul": "Piątek: CV z sekcją Projekty i 5 aplikacji",
             "opis": "Linki do GitHuba i CI. Pierwsze 5 aplikacji wysłane.", "pliki": [], "xp": 25},
        ],
    },
]

# ---------------------------------------------------------------------------
# RYTM DNIA — fazy sesji (minuty) z promptem do każdej fazy
# ---------------------------------------------------------------------------
RYTM_DNIA = [
    {"nazwa": "Nowy temat", "minuty": 20, "ikona": "📖",
     "opis": "Uczysz się nowego tematu. Claude tłumaczy na przykładach i daje 3 zadania — bez rozwiązań.",
     "prompt": "Uczę się [temat]. Wytłumacz na 2 prostych przykładach z życia rolnika. "
               "Potem daj mi 3 zadania od łatwego do trudniejszego. Nie podawaj rozwiązań."},
    {"nazwa": "Kodowanie", "minuty": 50, "ikona": "⌨",
     "opis": "Rozwiązujesz zadania w PyCharm, uruchamiasz python plik.py, sam poprawiasz błędy. "
             "Claude pytasz dopiero po 15 minutach własnej walki.",
     "prompt": "Utknąłem na zadaniu [opis]. Oto mój kod @[plik.py] i błąd: [treść błędu]. "
               "Nie poprawiaj kodu. Zadaj mi pytanie, które naprowadzi mnie na przyczynę."},
    {"nazwa": "Recenzja", "minuty": 15, "ikona": "🔍",
     "opis": "Claude recenzuje Twój kod jak cierpliwy mentor — bez przepisywania.",
     "prompt": "Przejrzyj @[plik.py] jak cierpliwy mentor. Trzy rzeczy: co jest dobrze, co jest błędem, "
               "co można napisać czytelniej. Bez przepisywania. Na koniec zadaj mi pytanie, które naprowadzi mnie na poprawkę."},
    {"nazwa": "Commit i powtórka", "minuty": 5, "ikona": "✅",
     "opis": "git add . && git commit -m \"dzień N: [temat]\" && git push. Potem 3 pytania sprawdzające.",
     "prompt": "Zaproponuj treść commita dla dzisiejszych zmian. Potem zadaj mi 3 pytania sprawdzające z tego, co dziś robiłem — po jednym, oceniaj odpowiedzi."},
]

# ---------------------------------------------------------------------------
# SZABLONY PROMPTÓW
# ---------------------------------------------------------------------------
PROMPTY = [
    {"nazwa": "Nowy temat", "kiedy": "Początek dnia (pon–czw)",
     "tresc": "Uczę się [temat]. Wytłumacz na 2 przykładach z życia, potem daj 3 zadania rosnącej trudności. Nie podawaj rozwiązań."},
    {"nazwa": "Utknąłem", "kiedy": "Po 15 minutach samodzielnej walki",
     "tresc": "Utknąłem na zadaniu [opis]. Oto mój kod @[plik.py] i błąd: [treść]. Nie poprawiaj kodu. Zadaj mi pytanie, które naprowadzi mnie na przyczynę."},
    {"nazwa": "Recenzja", "kiedy": "Koniec dnia, po napisaniu kodu",
     "tresc": "Przejrzyj @[plik.py] jak cierpliwy mentor. Trzy rzeczy: co jest dobrze, co jest błędem, co można napisać czytelniej. Bez przepisywania."},
    {"nazwa": "Sprawdzenie zrozumienia", "kiedy": "Zanim uruchomisz kod, którego nie jesteś pewien",
     "tresc": "Myślę, że ten kod robi [opis]. Sprawdź, czy dobrze rozumiem, i wskaż luki."},
    {"nazwa": "Quiz tygodnia", "kiedy": "Sobota",
     "tresc": "Zrób mi 10-pytaniowy quiz z [temat]. Pytaj po jednym, oceniaj odpowiedź i wyjaśniaj, jeśli się pomylę."},
    {"nazwa": "Plan projektu (tryb planowania)", "kiedy": "Przed większym zadaniem — Shift+Tab aż zobaczysz „plan”",
     "tresc": "Chcę zbudować [projekt]. Zaproponuj strukturę plików i kolejność kroków. Ja zdecyduję, co robimy pierwsze."},
    {"nazwa": "Zatrzymaj się", "kiedy": "Gdy Claude robi za dużo",
     "tresc": "Zatrzymaj się. Zrobiłeś to za mnie. Cofnij zmiany i daj mi tylko pierwszy krok."},
    {"nazwa": "Ja tłumaczę Twój kod (etap 2+)", "kiedy": "Po otrzymaniu fragmentu kodu od Claude",
     "tresc": "Napisałeś tę funkcję. Teraz ja Ci wytłumaczę, co robi, linijka po linijce, a Ty popraw mnie, jeśli się pomylę. Zaczynam: [Twoje wyjaśnienie]"},
    {"nazwa": "Claude pisze kod, ja piszę testy (etap 3)", "kiedy": "Tydzień 7+",
     "tresc": "Napisz funkcję [opis funkcji]. Nie pokazuj mi jej kodu. Ja napiszę testy, a potem porównamy, co przeoczyłem."},
    {"nazwa": "Ukryty błąd", "kiedy": "Tydzień 7+",
     "tresc": "Wprowadź do @[plik.py] jeden ukryty błąd. Nie mów jaki. Ja mam go znaleźć testami."},
    {"nazwa": "Ocena bug raportu", "kiedy": "Tydzień 9+",
     "tresc": "Oto mój bug raport:\n[treść raportu]\nOceń jak programista, który ma go naprawić: czy zrozumiesz bez dodatkowych pytań? Czego brakuje?"},
    {"nazwa": "Oczami rekrutera", "kiedy": "Tydzień 6 i 12",
     "tresc": "Oceń moje repozytorium oczami rekrutera na Junior QA. Co zobaczy w pierwszych 30 sekundach? Co go zniechęci? Podaj 3 konkretne poprawki."},
    {"nazwa": "Senior tester przed code review", "kiedy": "Tydzień 12",
     "tresc": "Zrób mi recenzję projektu jak senior tester przed code review. Wskaż 3 najważniejsze uwagi w kolejności od najpoważniejszej."},
    {"nazwa": "Próbna rozmowa rekrutacyjna", "kiedy": "Tygodnie 11–12, 20 min dziennie",
     "tresc": "Odpytaj mnie jak rekruter na Junior QA — 5 pytań o testowanie manualne, 5 o pytest/Selenium, 5 o mój projekt. Po każdej odpowiedzi oceń i podpowiedz, co dodać. Pytaj po jednym."},
    {"nazwa": "Zadanie rekrutacyjne", "kiedy": "Tydzień 12",
     "tresc": "Daj mi typowe zadanie rekrutacyjne na Junior QA Automation i oceń moje rozwiązanie bez podpowiadania w trakcie."},
]

CLAUDE_MD = """# Zasady pracy
- Jestem początkującym programistą, uczę się Pythona pod rolę Junior QA.
- Nie pisz rozwiązań zadań za mnie. Dawaj wskazówki i pytania naprowadzające.
- Zanim zaproponujesz kod, zapytaj, czy chcę go zobaczyć.
- Tłumacz po polsku, prostym językiem, z przykładami.
- Gdy poprawiasz mój kod, pokaż różnicę i wyjaśnij dlaczego.
"""

BUG_RAPORT_SZABLON = """# Bug raport: [krótki tytuł — co nie działa]

**ID:** BUG-[numer]
**Data:** [data]
**Priorytet:** [niski / średni / wysoki / krytyczny]
**Środowisko:** [system, przeglądarka, wersja aplikacji]

## Kroki do odtworzenia
1. [krok 1]
2. [krok 2]
3. [krok 3]

## Oczekiwany wynik
[co powinno się stać]

## Rzeczywisty wynik
[co się stało]

## Załączniki
[zrzut ekranu, log, nagranie]
"""

# ---------------------------------------------------------------------------
# ŚCIĄGA CLAUDE CODE
# ---------------------------------------------------------------------------
SCIAGA = [
    ("claude", "Uruchamia sesję w bieżącym katalogu"),
    ("claude -c", "Wraca do ostatniej rozmowy w tym katalogu"),
    ("claude -r", "Wybiera wcześniejszą rozmowę do wznowienia"),
    ("/init", "Tworzy plik CLAUDE.md dla projektu"),
    ("/help", "Lista wszystkich komend"),
    ("/clear", "Czyści rozmowę — nowy temat, czysta głowa"),
    ("/compact", "Streszcza długą rozmowę, żeby Claude nie gubił kontekstu"),
    ("/rewind", "Cofa zmiany w plikach do wcześniejszego punktu"),
    ("/exit  (lub Ctrl+D ×2)", "Kończy sesję"),
    ("Shift+Tab", "Przełącza tryb uprawnień: pytaj o zgodę / auto / planowanie"),
    ("@plik.py", "Wskazuje plik, który Claude ma przeczytać"),
    ("Esc", "Przerywa Claude w trakcie odpowiedzi"),
    ("↑", "Historia wpisanych poleceń"),
    ("claude doctor", "Sprawdza, czy instalacja jest poprawna"),
]

SCIAGA_GIT = [
    ("git status", "Co jest zmienione, a co nie trafiło jeszcze do commita"),
    ("git add .", "Dodaje wszystkie zmiany do następnego commita"),
    ("git commit -m \"opis\"", "Zapisuje migawkę zmian lokalnie"),
    ("git push", "Wysyła commity na GitHub"),
    ("git log --oneline", "Historia commitów w skrócie"),
    ("git diff", "Różnice w plikach, których jeszcze nie dodałeś"),
    ("git checkout -b nazwa", "Tworzy nową gałąź i przełącza na nią"),
    ("git stash", "Odkłada zmiany na bok; git stash pop je przywraca"),
    ("git checkout -- plik", "Cofa niezacommitowane zmiany w pliku"),
]

# ---------------------------------------------------------------------------
# CHECKLISTA POSTĘPÓW (odhaczasz tylko to, co robisz bez pomocy Claude)
# ---------------------------------------------------------------------------
CHECKLISTA = [
    {"po": "Po tygodniu 0", "punkty": [
        "Otwieram terminal, przechodzę do katalogu i uruchamiam claude",
        "Uruchamiam plik .py z terminala",
        "Robię commit i push na GitHub"]},
    {"po": "Po etapie 1 (tydzień 3)", "punkty": [
        "Piszę program z if, pętlą for, listą i dwiema funkcjami bez zaglądania do notatek",
        "Czytam komunikat błędu Pythona i wiem, w której linii szukać",
        "Wyjaśniam różnicę między listą a słownikiem na przykładzie"]},
    {"po": "Po etapie 2 (tydzień 6)", "punkty": [
        "Tworzę gałąź, wprowadzam zmiany, otwieram pull request",
        "Instaluję bibliotekę przez pip w venv i używam jej",
        "Czytam 100-liniowy cudzy plik i opisuję, co robi",
        "Każdy mój projekt na GitHubie ma README"]},
    {"po": "Po etapie 3 (tydzień 9)", "punkty": [
        "Piszę test pytest z parametrize i fixture",
        "Piszę test Selenium z Page Object Model i WebDriverWait",
        "Piszę bug raport, który programista zrozumie bez pytań",
        "Moje testy uruchamiają się automatycznie w GitHub Actions"]},
    {"po": "Po etapie 4 (tydzień 12)", "punkty": [
        "Opowiadam o projekcie gospodarstwa w 2 minuty bez notatek",
        "Naprawiam niedziałający test Selenium sam",
        "CV ma sekcję Projekty z linkami do GitHuba i CI",
        "Wysłałem pierwsze 5 aplikacji na Junior QA"]},
]

# ---------------------------------------------------------------------------
# QUIZY — klucz: numer tygodnia. odp = indeks poprawnej odpowiedzi.
# ---------------------------------------------------------------------------
QUIZ = {
    0: [
        {"p": "Co robi komenda python --version?",
         "o": ["Uruchamia ostatni program", "Pokazuje zainstalowaną wersję Pythona", "Instaluje Pythona", "Tworzy nowy plik .py"],
         "odp": 1, "w": "To test, czy Python jest zainstalowany i widoczny w PATH."},
        {"p": "Do czego służy plik CLAUDE.md w katalogu projektu?",
         "o": ["Przechowuje hasła", "Zawiera zasady i kontekst projektu, które Claude Code czyta na starcie", "Jest kodem programu", "To lista commitów"],
         "odp": 1, "w": "Claude Code czyta CLAUDE.md automatycznie — to tam wpisujesz „nie pisz rozwiązań za mnie”."},
        {"p": "Jak uruchomić plik hello.py z terminala?",
         "o": ["run hello.py", "python hello.py", "start hello", "claude hello.py"],
         "odp": 1, "w": "Interpreter Pythona dostaje nazwę pliku jako argument."},
        {"p": "Co robi git commit?",
         "o": ["Wysyła zmiany na GitHub", "Zapisuje migawkę zmian w lokalnym repozytorium", "Usuwa zmiany", "Tworzy gałąź"],
         "odp": 1, "w": "Commit jest lokalny. Dopiero git push wysyła go na GitHub."},
        {"p": "Który skrót przełącza tryb uprawnień w Claude Code (pytaj / auto / plan)?",
         "o": ["Ctrl+C", "Shift+Tab", "Esc", "Alt+P"],
         "odp": 1, "w": "Na czas nauki trzymaj tryb, w którym Claude pyta o zgodę przed każdą zmianą."},
    ],
    1: [
        {"p": "Co zwróci type(3.5)?",
         "o": ["int", "str", "float", "bool"], "odp": 2, "w": "Liczby z kropką dziesiętną to float."},
        {"p": "x = input(\"Podaj wiek: \") — jakiego typu jest x?",
         "o": ["int", "str", "float", "zależy, co wpisze użytkownik"],
         "odp": 1, "w": "input() ZAWSZE zwraca napis. Żeby liczyć, trzeba zrobić int(x)."},
        {"p": "Co wypisze print(7 // 2)?",
         "o": ["3.5", "3", "4", "1"], "odp": 1, "w": "// to dzielenie całkowite — obcina część po przecinku."},
        {"p": "Co wypisze print(7 % 3)?",
         "o": ["2", "1", "2.33", "0"], "odp": 1, "w": "% to reszta z dzielenia. 7 = 2·3 + 1."},
        {"p": "Jak sprawdzić, czy a jest równe b?",
         "o": ["a = b", "a == b", "a => b", "a equals b"],
         "odp": 1, "w": "Pojedynczy = to przypisanie. Porównanie to ==."},
    ],
    2: [
        {"p": "Co wypisze: for i in range(3): print(i)?",
         "o": ["1 2 3", "0 1 2", "0 1 2 3", "3"], "odp": 1, "w": "range(3) daje 0, 1, 2 — zaczyna od zera, kończy PRZED 3."},
        {"p": "Co zwróci len([1, 2, 3, 4])?",
         "o": ["3", "4", "5", "błąd"], "odp": 1, "w": "len() liczy elementy listy."},
        {"p": "Co robi break w pętli?",
         "o": ["Pomija jeden obrót pętli", "Kończy całą pętlę natychmiast", "Zatrzymuje program", "Cofa się o jeden obrót"],
         "odp": 1, "w": "break wychodzi z pętli; continue tylko przeskakuje do następnego obrotu."},
        {"p": "Co zwróci \"abc\".upper()?",
         "o": ["abc", "ABC", "Abc", "cba"], "odp": 1, "w": "upper() zamienia wszystkie litery na wielkie."},
        {"p": "Jak dodać element na koniec listy lista?",
         "o": ["lista.add(x)", "lista.append(x)", "lista.push(x)", "lista + x"],
         "odp": 1, "w": "append() dodaje na koniec. insert(i, x) wstawia w wybrane miejsce."},
    ],
    3: [
        {"p": "Co zwraca funkcja, która nie ma instrukcji return?",
         "o": ["0", "pusty napis", "None", "błąd"], "odp": 2, "w": "Brak return = funkcja zwraca None."},
        {"p": "d = {\"krowa\": 600}; co zwróci d[\"krowa\"]?",
         "o": ["\"krowa\"", "600", "0", "błąd"], "odp": 1, "w": "Słownik: klucz → wartość. Klucz „krowa” wskazuje na 600."},
        {"p": "Czym krotka (tuple) różni się od listy?",
         "o": ["Niczym", "Krotki nie można zmieniać po utworzeniu", "Krotka jest szybsza do sortowania", "Krotka może mieć tylko liczby"],
         "odp": 1, "w": "Krotka jest niezmienna (immutable) — przydatna na dane, które nie powinny się zmienić."},
        {"p": "Kiedy wykona się blok except?",
         "o": ["Zawsze po try", "Gdy w bloku try wystąpi błąd", "Gdy try zakończy się poprawnie", "Nigdy, to tylko komentarz"],
         "odp": 1, "w": "try próbuje, except łapie błąd. Dzięki temu program nie wywala się na złym wpisie."},
        {"p": "Co robi random.choice(lista)?",
         "o": ["Sortuje listę", "Zwraca losowy element z listy", "Miesza listę", "Usuwa losowy element"],
         "odp": 1, "w": "random.choice losuje jeden element. random.sample(lista, 3) losuje trzy bez powtórzeń."},
    ],
    4: [
        {"p": "Co robi git checkout -b feature/csv?",
         "o": ["Usuwa gałąź", "Tworzy nową gałąź i przełącza na nią", "Scala gałąź z main", "Wysyła gałąź na GitHub"],
         "odp": 1, "w": "-b tworzy gałąź. Samo git checkout nazwa tylko przełącza na istniejącą."},
        {"p": "Jaka jest główna zaleta with open(\"plik.txt\") as f:?",
         "o": ["Działa szybciej", "Plik zamyka się automatycznie, nawet przy błędzie", "Tworzy kopię pliku", "Pozwala pisać i czytać naraz"],
         "odp": 1, "w": "with to menedżer kontekstu — zamyka plik za Ciebie."},
        {"p": "Co pokazuje git diff?",
         "o": ["Listę commitów", "Różnice w plikach, których jeszcze nie dodałeś do commita", "Listę gałęzi", "Adres repozytorium"],
         "odp": 1, "w": "git diff = co zmieniłeś od ostatniego commita (w plikach nie dodanych przez git add)."},
        {"p": "Czym jest pull request?",
         "o": ["Pobraniem zmian z GitHuba", "Prośbą o scalenie zmian z gałęzi do innej gałęzi, z możliwością recenzji", "Usunięciem gałęzi", "Kopią repozytorium"],
         "odp": 1, "w": "PR to miejsce, gdzie zespół ogląda zmiany, zanim trafią do main."},
        {"p": "Co zwraca csv.reader przy iteracji?",
         "o": ["Cały plik jako jeden napis", "Każdy wiersz jako listę pól", "Słownik", "Liczbę wierszy"],
         "odp": 1, "w": "csv.reader daje listy; csv.DictReader daje słowniki z nagłówkami jako kluczami."},
    ],
    5: [
        {"p": "Czym jest metoda __init__ w klasie?",
         "o": ["Metodą usuwającą obiekt", "Konstruktorem wywoływanym przy tworzeniu obiektu", "Metodą do drukowania", "Importem modułu"],
         "odp": 1, "w": "__init__ ustawia początkowe atrybuty obiektu (self.imie = imie)."},
        {"p": "Po co tworzyć środowisko wirtualne (venv)?",
         "o": ["Żeby program działał szybciej", "Żeby biblioteki projektu były odizolowane od reszty systemu", "Żeby Python był bezpieczniejszy", "Nie ma to znaczenia"],
         "odp": 1, "w": "Każdy projekt ma własne wersje bibliotek — bez konfliktów między projektami."},
        {"p": "Do czego służy requirements.txt?",
         "o": ["To lista zadań", "To lista bibliotek projektu; pip install -r requirements.txt je instaluje", "To konfiguracja Gita", "To plik testów"],
         "odp": 1, "w": "Ktoś inny (lub CI) odtwarza Twoje środowisko jedną komendą."},
        {"p": "Co zwraca requests.get(url).json()?",
         "o": ["Napis HTML", "Dane z odpowiedzi zamienione na słownik/listę Pythona", "Plik na dysku", "Kod statusu"],
         "odp": 1, "w": ".json() parsuje JSON na struktury Pythona — potem odczytujesz pola jak ze słownika."},
        {"p": "Dlaczego .venv powinno być w .gitignore?",
         "o": ["Bo zawiera hasła", "Bo to setki plików bibliotek, które każdy może zainstalować sam z requirements.txt", "Bo Git nie obsługuje folderów", "Nie powinno — trzeba je commitować"],
         "odp": 1, "w": "Repo ma zawierać Twój kod, nie cudze biblioteki."},
    ],
    6: [
        {"p": "Co robi breakpoint w debuggerze PyCharm?",
         "o": ["Usuwa linię", "Zatrzymuje program w tej linii, żebyś obejrzał zmienne", "Zaznacza błąd", "Uruchamia testy"],
         "odp": 1, "w": "Zatrzymany program = widzisz wartości zmiennych i idziesz krok po kroku."},
        {"p": "Czym jest docstring?",
         "o": ["Komentarzem po #", "Opisem funkcji w potrójnych cudzysłowach tuż po def", "Nazwą pliku", "Typem danych"],
         "odp": 1, "w": "Docstring czyta też help(funkcja) i PyCharm w podpowiedziach."},
        {"p": "Co minimalnie powinno zawierać README projektu?",
         "o": ["Tylko nazwę", "Co program robi i jak go uruchomić", "Cały kod", "Listę commitów"],
         "odp": 1, "w": "Rekruter czyta README w 30 sekund. Jeśli nie wie, co to robi — zamyka kartę."},
        {"p": "Co robi /compact w Claude Code?",
         "o": ["Zmniejsza czcionkę", "Streszcza długą rozmowę, żeby Claude nie gubił kontekstu", "Usuwa pliki", "Kompresuje repo"],
         "odp": 1, "w": "/compact streszcza, /clear zaczyna od zera."},
        {"p": "Czym jest refaktoryzacja?",
         "o": ["Dodaniem nowych funkcji", "Zmianą struktury kodu bez zmiany jego zachowania", "Naprawą błędów", "Usunięciem testów"],
         "odp": 1, "w": "Program robi to samo, ale kod jest czytelniejszy. Testy pilnują, że nic się nie zepsuło."},
    ],
    7: [
        {"p": "W jakich plikach pytest automatycznie szuka testów?",
         "o": ["Wszystkich .py", "Zaczynających się od test_ lub kończących na _test.py", "Tylko w conftest.py", "W main.py"],
         "odp": 1, "w": "Konwencja nazw: test_funkcje.py, a w środku funkcje def test_...()."},
        {"p": "Co się stanie przy assert 2 + 2 == 5 w teście?",
         "o": ["Test przejdzie", "Test nie przejdzie — AssertionError", "Program się wyłączy", "Nic"],
         "odp": 1, "w": "assert sprawdza warunek; fałsz = test czerwony."},
        {"p": "Do czego służy @pytest.mark.parametrize?",
         "o": ["Do pomijania testów", "Do uruchomienia jednego testu dla wielu zestawów danych", "Do mierzenia czasu", "Do raportów HTML"],
         "odp": 1, "w": "Jeden test, 6 przypadków BMI — zamiast 6 kopii tej samej funkcji."},
        {"p": "Czym jest fixture?",
         "o": ["Błędem w teście", "Funkcją przygotowującą dane lub obiekty dla testów", "Raportem", "Wtyczką do PyCharm"],
         "odp": 1, "w": "Fixture tworzy np. menedżer z 3 zadaniami, a testy dostają go jako argument."},
        {"p": "Co robi flaga -v w pytest -v?",
         "o": ["Wersja pytest", "Tryb szczegółowy — pokazuje nazwę każdego testu i wynik", "Uruchamia tylko jeden test", "Wyłącza kolory"],
         "odp": 1, "w": "verbose = widzisz każdy test osobno zamiast samych kropek."},
    ],
    8: [
        {"p": "Który lokator jest zwykle najstabilniejszy?",
         "o": ["XPath po pełnej ścieżce", "id", "Tekst przycisku", "Pozycja na ekranie"],
         "odp": 1, "w": "id jest unikalne i rzadko się zmienia. XPath po pełnej ścieżce psuje się przy każdej zmianie układu."},
        {"p": "Dlaczego WebDriverWait zamiast time.sleep(5)?",
         "o": ["Bo sleep nie działa w Selenium", "Bo Wait czeka tylko tyle, ile trzeba, aż warunek się spełni", "Bo Wait jest prostszy", "Nie ma różnicy"],
         "odp": 1, "w": "sleep zawsze czeka 5 s (za długo lub za krótko). Wait kończy, gdy element się pojawi."},
        {"p": "Na czym polega Page Object Model?",
         "o": ["Jeden plik na wszystkie testy", "Każda strona to klasa z lokatorami i akcjami; testy używają tych metod", "Model danych w bazie", "Wzorzec w PyCharm"],
         "odp": 1, "w": "Zmiana lokatora = poprawka w jednym miejscu, nie w 15 testach."},
        {"p": "driver.find_element(By.CSS_SELECTOR, \"#login\") szuka…",
         "o": ["Elementu z klasą login", "Elementu z id = login", "Przycisku z tekstem login", "Wszystkich linków"],
         "odp": 1, "w": "W CSS # oznacza id, kropka oznacza klasę."},
        {"p": "Czym jest test end-to-end?",
         "o": ["Testem jednej funkcji", "Testem całego przepływu jak robi to użytkownik — od logowania do wyniku", "Testem wydajności", "Testem kodu CSS"],
         "odp": 1, "w": "E2E = przeglądarka, klikanie, cały scenariusz. Wolne, ale najbliższe prawdzie."},
    ],
    9: [
        {"p": "Co musi zawierać dobry bug raport?",
         "o": ["Tylko opis problemu", "Kroki odtworzenia, oczekiwany vs rzeczywisty wynik, środowisko", "Rozwiązanie błędu", "Nazwisko programisty"],
         "odp": 1, "w": "Test: czy programista odtworzy błąd bez pytania Cię o cokolwiek."},
        {"p": "Gdzie leży plik workflow GitHub Actions?",
         "o": [".github/workflows/", "tests/", "W README", ".venv/"],
         "odp": 0, "w": "Np. .github/workflows/tests.yml."},
        {"p": "Co daje CI (ciągła integracja) w projekcie?",
         "o": ["Automatyczne uruchamianie testów przy każdym pushu", "Szybsze pisanie kodu", "Lepszą czcionkę", "Automatyczne naprawianie błędów"],
         "odp": 0, "w": "Zielona odznaka w README = testy przechodzą na czystej maszynie, nie tylko u Ciebie."},
        {"p": "Do czego służy pytest-html?",
         "o": ["Do testowania HTML", "Do generowania raportu HTML z wyników testów", "Do Selenium", "Do CSS"],
         "odp": 1, "w": "pytest --html=raport.html — raport, który możesz pokazać na rozmowie."},
        {"p": "Co zawiera przypadek testowy?",
         "o": ["Tylko nazwę", "ID, warunki wstępne, kroki, oczekiwany wynik", "Kod testu", "Zrzut ekranu"],
         "odp": 1, "w": "Przypadek testowy to przepis, który inny tester wykona bez Ciebie."},
    ],
    10: [
        {"p": "Czym jest SQLite?",
         "o": ["Serwerem bazy danych", "Bazą danych w jednym pliku, wbudowaną w Pythona (moduł sqlite3)", "Biblioteką do testów", "Frameworkiem webowym"],
         "odp": 1, "w": "Bez instalacji, bez serwera — idealne na projekt portfolio."},
        {"p": "Co daje fixture tmp_path w pytest?",
         "o": ["Losową liczbę", "Tymczasowy katalog, w którym możesz stworzyć bazę testową", "Dostęp do internetu", "Zrzut ekranu"],
         "odp": 1, "w": "Testy nie dotykają Twojej prawdziwej bazy — każdy dostaje czystą."},
        {"p": "Po co pisać PLAN.md przed kodowaniem?",
         "o": ["Bo tak każe Git", "Żeby ustalić zakres i kolejność kroków, zanim utoniesz w szczegółach", "Żeby mieć więcej plików", "Nie ma po co"],
         "odp": 1, "w": "Plan w trybie planowania = Ty decydujesz, co pierwsze; Claude nie wyprzedza."},
    ],
    11: [
        {"p": "Jak we Flasku zdefiniować stronę główną?",
         "o": ["@app.route(\"/\")", "def main():", "flask.page(\"/\")", "app.home()"],
         "odp": 0, "w": "Dekorator @app.route łączy adres URL z funkcją, która zwraca stronę."},
        {"p": "Po co walidować formularz po stronie serwera?",
         "o": ["Żeby strona była ładniejsza", "Żeby złe dane (puste pole, waga -5) nie trafiły do bazy", "Żeby było szybciej", "Nie trzeba, przeglądarka to robi"],
         "odp": 1, "w": "Użytkownik (i tester!) wpisze wszystko. Serwer musi to odrzucić i powiedzieć dlaczego."},
        {"p": "Co robi python app.py w projekcie Flask?",
         "o": ["Uruchamia testy", "Uruchamia lokalny serwer WWW z aplikacją", "Tworzy bazę", "Wysyła na GitHub"],
         "odp": 1, "w": "Potem otwierasz http://127.0.0.1:5000 w przeglądarce."},
    ],
    12: [
        {"p": "Co powinien zawierać wpis w sekcji Projekty w CV?",
         "o": ["Tylko nazwę projektu", "Co robi, technologie, liczba testów, link do GitHuba i CI", "Opis na pół strony", "Zrzut ekranu"],
         "odp": 1, "w": "Każde słowo w CV potwierdza kod, który rekruter może kliknąć."},
        {"p": "Jak zbudować 2-minutową opowieść o projekcie?",
         "o": ["Wymienić wszystkie pliki", "Problem → rozwiązanie → technologie → czego się nauczyłem", "Przeczytać README", "Opowiedzieć o Claude Code"],
         "odp": 1, "w": "Rekruter chce usłyszeć, jak myślisz, nie ile plików masz."},
        {"p": "Jaki jest sygnał, że jesteś gotowy aplikować?",
         "o": ["Minęło 12 tygodni", "Naprawiasz błąd w teście Selenium sam i tłumaczysz każdy plik koledze bez IT", "Masz 100 commitów", "Claude powiedział, że jest ok"],
         "odp": 1, "w": "Samodzielność, nie kalendarz."},
    ],
}

# ---------------------------------------------------------------------------
# WSKAZÓWKI DNIA
# ---------------------------------------------------------------------------
WSKAZOWKI = [
    "Zasada 70/30: 70% czasu piszesz kod własnoręcznie, 30% rozmawiasz z Claude o tym, co napisałeś.",
    "Minimum 15 minut własnej walki z zadaniem, zanim poprosisz o pomoc. Frustracja to moment, w którym mózg się uczy.",
    "Proś o podpowiedź, nie o rozwiązanie: „daj mi wskazówkę, co jest nie tak — nie poprawiaj”.",
    "Każdy fragment kodu od Claude przepisujesz ręcznie. Nie kopiuj — pisz. Palce zapamiętują składnię.",
    "Zanim uruchomisz kod, wytłumacz Claude, co robi. Jeśli nie umiesz — jeszcze go nie rozumiesz.",
    "Pytaj „dlaczego”, aż odpowiedź będzie oczywista. Nie idź dalej z niezrozumianym kodem.",
    "Commit jest dowodem, że zadanie zrobione. Mały commit codziennie > wielki raz w tygodniu.",
    "Komunikat błędu czytaj od dołu: ostatnia linia mówi CO, linie wyżej mówią GDZIE.",
    "Niedziela jest wolna celowo. Mózg utrwala w przerwie — seria nie przerywa się w niedzielę.",
    "Tryb planowania (Shift+Tab) przed większym zadaniem: czytasz plan, pytasz o niejasne kroki, dopiero potem kodujesz.",
    "Gdy Claude zrobi za dużo: „Zatrzymaj się. Cofnij zmiany i daj mi tylko pierwszy krok.”",
    "Kończ dzień 3 pytaniami sprawdzającymi. To, co powtórzysz tego samego dnia, zostaje na tygodnie.",
    "Twoje 15 lat prowadzenia gospodarstwa to przewaga: żaden inny junior nie zna dziedziny projektu tak jak Ty.",
    "Tester myśli: „co się stanie, gdy użytkownik wpisze coś głupiego?”. Ćwicz to już przy kalkulatorze.",
    "Nazwa zmiennej ma mówić, co trzyma: waga_kg zamiast w. Czytelny kod to pierwsza rzecz, którą widzi rekruter.",
    "Jeśli po etapie zostają puste pola w checkliście — dodaj tydzień. Tempo nie jest celem, umiejętność jest.",
    "Zły dzień też się liczy. 20 minut i jeden commit podtrzymują nawyk; nawyk podtrzymuje wszystko inne.",
    "print() to Twój pierwszy debugger. Wypisz zmienną przed i po linii, której nie rozumiesz.",
]

MOTYWACJA_POWROT = [
    "Dobrze, że jesteś. Każdy powrót liczy się bardziej niż przerwa.",
    "Nie nadrabiaj wszystkiego naraz. Jedno zadanie, jeden commit — i seria rusza od nowa.",
    "Przerwa nie kasuje tego, co umiesz. Sprawdź to w quizie — będziesz zaskoczony, ile zostało.",
    "Zacznij od najmniejszej rzeczy: otwórz PyCharm, uruchom wczorajszy plik. Reszta przyjdzie sama.",
]

# ---------------------------------------------------------------------------
# ODZNAKI — warunek dostaje słownik statystyk (patrz mentor.py: statystyki())
# ---------------------------------------------------------------------------
ODZNAKI = [
    {"id": "start", "ikona": "🚀", "nazwa": "Start", "opis": "Pierwsza zapisana sesja nauki",
     "warunek": lambda s: s["dni_nauki"] >= 1},
    {"id": "hello", "ikona": "👋", "nazwa": "Hello, world", "opis": "Ukończony tydzień 0",
     "warunek": lambda s: s["tygodnie_ukonczone"] >= 1},
    {"id": "seria5", "ikona": "🔥", "nazwa": "Rozgrzewka", "opis": "Seria 5 dni nauki",
     "warunek": lambda s: s["najdluzsza_seria"] >= 5},
    {"id": "seria15", "ikona": "🔥🔥", "nazwa": "Nawyk", "opis": "Seria 15 dni nauki",
     "warunek": lambda s: s["najdluzsza_seria"] >= 15},
    {"id": "seria30", "ikona": "🏆", "nazwa": "Żelazna dyscyplina", "opis": "Seria 30 dni nauki",
     "warunek": lambda s: s["najdluzsza_seria"] >= 30},
    {"id": "etap1", "ikona": "🐍", "nazwa": "Python w palcach", "opis": "Ukończony etap 1 (tygodnie 1–3)",
     "warunek": lambda s: s["etapy_ukonczone"] >= 2},
    {"id": "etap2", "ikona": "🌿", "nazwa": "Gałęzie i moduły", "opis": "Ukończony etap 2 (tygodnie 4–6)",
     "warunek": lambda s: s["etapy_ukonczone"] >= 3},
    {"id": "etap3", "ikona": "🧪", "nazwa": "Tester", "opis": "Ukończony etap 3 (tygodnie 7–9)",
     "warunek": lambda s: s["etapy_ukonczone"] >= 4},
    {"id": "etap4", "ikona": "🎓", "nazwa": "Gotowy na rozmowę", "opis": "Ukończony cały program",
     "warunek": lambda s: s["etapy_ukonczone"] >= 5},
    {"id": "quiz100", "ikona": "💯", "nazwa": "Bezbłędnie", "opis": "Quiz tygodnia na 100%",
     "warunek": lambda s: s["quizy_100"] >= 1},
    {"id": "quiz5", "ikona": "🧠", "nazwa": "Powtarzacz", "opis": "5 zaliczonych quizów",
     "warunek": lambda s: s["quizy_zaliczone"] >= 5},
    {"id": "xp100", "ikona": "⭐", "nazwa": "100 XP", "opis": "Zdobyte 100 punktów doświadczenia",
     "warunek": lambda s: s["xp"] >= 100},
    {"id": "xp500", "ikona": "🌟", "nazwa": "500 XP", "opis": "Zdobyte 500 punktów doświadczenia",
     "warunek": lambda s: s["xp"] >= 500},
    {"id": "dziennik10", "ikona": "📓", "nazwa": "Kronikarz", "opis": "10 wpisów w dzienniku nauki",
     "warunek": lambda s: s["wpisy_dziennika"] >= 10},
    {"id": "sesje20", "ikona": "⏱", "nazwa": "20 sesji", "opis": "20 dni z zapisaną sesją nauki",
     "warunek": lambda s: s["dni_nauki"] >= 20},
    {"id": "godziny50", "ikona": "⏳", "nazwa": "50 godzin", "opis": "50 godzin nauki łącznie",
     "warunek": lambda s: s["minuty"] >= 50 * 60},
]
