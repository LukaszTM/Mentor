# -*- coding: utf-8 -*-
"""Etap 3, tygodnie 7–9: podstawy testowania (ISTQB/SJSI), pytest, parametrize i fixtures, Selenium WebDriver, czekanie i Page Object Model,
przypadki testowe i raporty błędów, GitHub Actions i pytest-html, powtórka etapu."""

from wspolne import B, C, L, T, bl, kod, li, tx, wy
import zrodla as Z

# =========================================================================== TYDZIEŃ 7
PODSTAWY = L(
    id="podstawy_testowania", nazwa="Podstawy testowania: pomyłka, defekt, awaria, poziomy testów, klasy równoważności i wartości brzegowe", tydzien=7,
    slowa=["testowanie", "ISTQB", "pomyłka", "defekt", "awaria", "test jednostkowy", "integracyjny", "systemowy", "akceptacyjny", "piramida testów",
           "klasy równoważności", "wartości brzegowe", "przypadek testowy", "regresja", "test negatywny"],
    cel="Po tej lekcji rozróżniasz pomyłkę, defekt i awarię (terminologia ISTQB/SJSI), znasz poziomy testów i piramidę testów oraz projektujesz przypadki testowe technikami podziału na klasy równoważności i analizy wartości brzegowych.",
    po_co="To słownictwo i te techniki padają na każdej rozmowie Junior QA i w egzaminie ISTQB Foundation; dzięki nim zamiast „klikam, aż coś się zepsuje” testujesz celowo i mało, a skutecznie.",
    wymagania=["Lekcje „Warunki” i „Funkcje”."],
    wyjasnienie=(
        "## Pomyłka → defekt → awaria\n"
        "Terminologia polskiej wersji sylabusa ISTQB (SJSI): **pomyłka** — działanie człowieka (programista źle zrozumiał „od 100 zł”); **defekt** — wada w kodzie (`>` zamiast `>=`); "
        "**awaria** — widoczny skutek podczas działania (klient z koszykiem za 100 zł płaci za dostawę). Tester obserwuje awarie i pomaga znaleźć defekty.\n"
        "## Po co testujemy\n"
        "Testy nie udowodnią braku defektów — zmniejszają ryzyko i dają informację o jakości. Wczesne testowanie (już wymagań) jest najtańsze.\n"
        "## Poziomy testów\n"
        "| poziom | co sprawdza | przykład w kursie |\n|---|---|---|\n"
        "| jednostkowe (modułowe) | pojedyncza funkcja/klasa | pytest: `koszt_dostawy(99.99)` |\n"
        "| integracyjne | współpraca części | funkcja + baza SQLite (tydz. 10) |\n"
        "| systemowe | cały system | Selenium w przeglądarce (tydz. 8) |\n"
        "| akceptacyjne | czy spełnia potrzeby użytkownika | scenariusz „klient składa zamówienie” |\n"
        "**Piramida testów**: dużo szybkich testów jednostkowych na dole, mniej integracyjnych, najmniej (wolnych, kruchych) testów E2E w przeglądarce na górze.\n"
        "## Podział na klasy równoważności\n"
        "Dzielisz dane wejściowe na grupy, które program powinien traktować tak samo, i z każdej bierzesz JEDEN reprezentant. Reguła „ilość w zamówieniu 1–50”: klasy: < 1 (niepoprawna), 1–50 (poprawna), > 50 (niepoprawna), nie-liczba (niepoprawna). 4 testy zamiast 100.\n"
        "## Analiza wartości brzegowych\n"
        "Defekty siedzą na granicach (`<` vs `<=`). Dla przedziału 1–50 testujesz granice i ich sąsiadów: **0, 1, 50, 51** (wariant dwupunktowy). Wariant trzypunktowy dodaje 2 i 49.\n"
        "## Testy pozytywne, negatywne, regresja\n"
        "Pozytywny — poprawne dane, oczekiwany sukces. Negatywny — złe dane, oczekiwany czytelny błąd (nie awaria!). **Regresja** — defekt, który wraca po zmianie; dlatego testy uruchamia się automatycznie przy każdej zmianie (CI, tydzień 9).\n"
        "## Przypadek testowy\n"
        "ID, tytuł, warunki wstępne, kroki, dane, **oczekiwany wynik**. Bez oczekiwanego wyniku to nie test, tylko wycieczka."),
    przyklad=kod("podstawy_testowania", (
        "def czy_ilosc_poprawna(ilosc):\n"
        "    \"\"\"Wymaganie: ilość w zamówieniu to liczba całkowita od 1 do 50.\"\"\"\n"
        "    return isinstance(ilosc, int) and 1 <= ilosc <= 50\n\n\n"
        "def czy_ilosc_z_defektem(ilosc):\n"
        "    return isinstance(ilosc, int) and 1 <= ilosc < 50\n\n\n"
        "PRZYPADKI = [(0, False), (1, True), (25, True), (50, True), (51, False), (-5, False), (\"10\", False)]\n"
        "for funkcja in (czy_ilosc_poprawna, czy_ilosc_z_defektem):\n"
        "    nieudane = [d for d, oczekiwane in PRZYPADKI if funkcja(d) != oczekiwane]\n"
        "    print(funkcja.__name__, \"— nieudane przypadki:\", nieudane)\n"), (
        "czy_ilosc_poprawna — nieudane przypadki: []\nczy_ilosc_z_defektem — nieudane przypadki: [50]\n")),
    demonstracja={"tytul": "7 przypadków z dwóch technik łapie defekt na granicy", "kroki": [
        "Wymaganie w docstringu: liczba całkowita 1–50.",
        "Klasy równoważności: < 1 (reprezentant -5), 1–50 (25), > 50 (51… albo 80), nie-liczba (\"10\" — napis).",
        "Wartości brzegowe (dwupunktowo): 0, 1, 50, 51.",
        "`PRZYPADKI` — pary (dane, oczekiwany wynik). Razem 7 przypadków.",
        "`czy_ilosc_z_defektem` ma `< 50` zamiast `<= 50` — typowa pomyłka programisty.",
        "Pętla sprawdza obie wersje: poprawna nie ma nieudanych przypadków, wadliwa pada TYLKO dla 50.",
        "Wniosek: bez testu wartości brzegowej 50 defekt przeszedłby niezauważony — 25 i 80 dają poprawne wyniki w obu wersjach."],
        "wynik": "Poprawna wersja: lista nieudanych pusta; wersja z defektem: [50]."},
    jak_uruchomic=["Zapisz jako techniki.py → ▶ Uruchom.", "Zmień defekt na `1 < ilosc <= 50` i przewidź, który przypadek padnie (1)."],
    cwiczenia=[
        C("prowadzone",
          "Wymaganie: „hasło ma od 8 do 20 znaków”. Na wzór demonstracji podaj długości do testów dwupunktowej analizy wartości brzegowych (4 liczby rosnąco po przecinku) oraz liczbę klas równoważności dla samej długości. Czas: 15 minut.",
          "Wartości brzegowe: 7, 8, 20, 21; klasy równoważności: 3 (za krótkie, poprawne, za długie).",
          ["Granice to 8 i 20.", "Do każdej granicy jej sąsiad po złej stronie.", "Ile grup traktowanych tak samo: poniżej, w zakresie, powyżej."],
          "Granice 8 i 20 plus sąsiedzi poza zakresem: 7, 8, 20, 21. Klasy: < 8, 8–20, > 20 → 3.",
          [tx("bv", "Wartości brzegowe", "7, 8, 20, 21"), li("kr", "Liczba klas równoważności", 3)]),
        C("samodzielne",
          "Zaklasyfikuj (pomyłka / defekt / awaria): (1) programista źle zrozumiał wymaganie „rabat od 200 zł” (działanie człowieka); (2) w kodzie jest `if razem > 200` zamiast `>=`; (3) klient z koszykiem 200 zł nie dostał rabatu. "
          "Dodatkowo (4): który poziom testów sprawdza pojedynczą funkcję rabat()? Opcje: jednostkowe / integracyjne / systemowe / akceptacyjne. Czas: 15 minut.",
          "(1) pomyłka; (2) defekt; (3) awaria; (4) jednostkowe.",
          ["Działanie człowieka.", "Wada w produkcie (kodzie, dokumencie).", "Widoczny skutek przy działaniu."],
          "(1) pomyłka — działanie człowieka; (2) defekt — wada w kodzie, skutek pomyłki; (3) awaria — widoczny skutek defektu; (4) testy jednostkowe (modułowe).",
          [wy("a", "(1) programista źle zrozumiał wymaganie", ["pomyłka", "defekt", "awaria"], "pomyłka"), wy("b", "(2) > zamiast >= w kodzie", ["pomyłka", "defekt", "awaria"], "defekt"),
           wy("c", "(3) klient bez rabatu", ["pomyłka", "defekt", "awaria"], "awaria"), wy("d", "(4) poziom dla rabat()", ["jednostkowe", "integracyjne", "systemowe", "akceptacyjne"], "jednostkowe")]),
    ],
    typowe_bledy=[
        B("„Przetestowałem 100 losowych wartości i jest OK”, a defekt na granicy przeszedł.", "Testy bez techniki — wszystkie wartości z jednej klasy.", "Czy testy obejmują granice i każdą klasę?", "Klasy równoważności + wartości brzegowe przed pisaniem testów."),
        B("Przypadek testowy „sprawdzić logowanie”.", "Brak danych i oczekiwanego wyniku.", "Czy obca osoba wie, co wpisać i co ma się stać?", "Kroki, dane (login/hasło) i oczekiwany wynik (komunikat, strona)."),
    ],
    pulapki=["Testowanie tylko ścieżki „szczęśliwej” — połowa defektów jest w obsłudze złych danych.", "Mylenie awarii z defektem w zgłoszeniu: opisujesz awarię (co widać), defekt wskazujesz tylko, gdy go znasz."],
    zadania=["Dla 3 reguł z kursu (dostawa, rabat, ilość) wypisz klasy równoważności i wartości brzegowe.", "Zapisz 5 przypadków testowych w tabeli (ID, dane, oczekiwany wynik).", "Wyjaśnij na głos różnicę pomyłka/defekt/awaria."],
    pytania=[["Czym różni się defekt od awarii?", "Defekt to wada w kodzie/produkcie, awaria to jej widoczny skutek podczas działania."],
             ["Jakie wartości testujesz dla zakresu 1–50 (dwupunktowo)?", "0, 1, 50, 51."], ["Co to piramida testów?", "Dużo testów jednostkowych, mniej integracyjnych, najmniej E2E."]],
    podsumowanie="Rozróżniasz pomyłkę, defekt i awarię, znasz poziomy testów i piramidę oraz projektujesz przypadki technikami klas równoważności i wartości brzegowych.",
    test=[T("W kodzie jest < zamiast <=. Ta wada w kodzie to:", ["awaria", "defekt", "pomyłka", "regresja"], 1, "Defekt — wada w produkcie; pomyłką było działanie programisty, a awarią będzie zły wynik u klienta."),
          T("Wartości brzegowe dla zakresu 10–20 (dwupunktowo):", ["10, 20", "9, 10, 20, 21", "0, 30", "15"], 1, "Granice i sąsiedzi."),
          T("Najwięcej testów w piramidzie to:", ["E2E w przeglądarce", "jednostkowe", "manualne", "akceptacyjne"], 1, "Szybkie i tanie."),
          T("Test negatywny sprawdza:", ["że program działa szybko", "reakcję na niepoprawne dane", "tylko ścieżkę szczęśliwą", "wygląd"], 1, "Czytelny błąd zamiast awarii."),
          T("Egzamin ISTQB CTFL 4.0:", ["40 pytań, próg 26, 60 minut", "100 pytań, ustny", "brak egzaminu", "10 pytań"], 0, "Według ISTQB.")],
    w_praktyce=["Przed pisaniem testów automatycznych: tabela klas i granic dla każdej reguły.", "W rozmowie rekrutacyjnej: pokaż technikę na przykładzie z własnego projektu."],
    zrodla=[Z.SJSI_CTFL_PL, Z.ISTQB_CTFL, Z.ISTQB_SLOWNIK],
)

PYTEST = L(
    id="pytest", nazwa="pytest: test_, assert, uruchamianie, pytest.raises i pytest.approx", tydzien=7,
    slowa=["pytest", "test", "assert", "test_", "pytest -v", "PASSED", "FAILED", "raises", "approx", "AAA", "Arrange", "Act", "Assert", "mutant"],
    cel="Po tej lekcji piszesz testy jednostkowe w pytest (pliki test_*.py, funkcje test_*, assert), czytasz wynik pytest -v, testujesz wyjątki pytest.raises i liczby zmiennoprzecinkowe pytest.approx oraz układasz test według schematu Arrange–Act–Assert.",
    po_co="pytest to standard testów w Pythonie. Rekruter zapyta „jak sprawdzisz, że funkcja działa?” — odpowiedzią jest test, który przechodzi na dobrym kodzie i pada na złym.",
    wymagania=["Lekcje „Funkcje”, „Obsługa błędów” i „Podstawy testowania”.", "pytest jest w środowisku kursu (pytest 9.2)."],
    wyjasnienie=(
        "## Pierwszy test\n"
        "```\n# test_ceny.py\nfrom ceny import brutto\n\ndef test_brutto_vat_23():\n    assert brutto(10) == 12.3\n```\n"
        "pytest sam znajduje pliki `test_*.py` i funkcje `test_*`. `assert warunek` — jeśli warunek jest fałszywy, test pada (FAILED), a pytest pokazuje obie wartości.\n"
        "## Uruchamianie\n"
        "Terminal Mentora w katalogu z plikami: `python -m pytest -v` (verbose — każdy test osobno), `-q` krótko, `-k brutto` tylko testy z „brutto” w nazwie, `-x` stop na pierwszym błędzie. W Mentorze zadania z testami sprawdza „✔ Sprawdź wynik”.\n"
        "## Schemat AAA\n"
        "**Arrange** — przygotuj dane, **Act** — wywołaj funkcję, **Assert** — sprawdź wynik. Jeden test = jedno zachowanie; nazwa mówi, co sprawdza: `test_dostawa_darmowa_od_100`.\n"
        "## Wyjątki: pytest.raises\n"
        "```\nimport pytest\n\ndef test_wydaj_wiecej_niz_stan():\n    with pytest.raises(ValueError):\n        wydaj(10, 20)\n```\n"
        "Test przechodzi tylko wtedy, gdy blok RZUCI ValueError. `pytest.raises(ValueError, match=\"brak towaru\")` sprawdza też treść komunikatu.\n"
        "## Liczby zmiennoprzecinkowe: pytest.approx\n"
        "`assert 0.1 + 0.2 == pytest.approx(0.3)` — porównanie z tolerancją. Kwoty po round() porównujesz zwykle, wyniki obliczeń — approx.\n"
        "## Dobry test łapie błąd\n"
        "Test, który przechodzi zawsze, jest bezwartościowy. Sprawdzian: celowo zepsuj funkcję (`>=` na `>`) — test musi paść. Taką zepsutą wersję nazywa się **mutantem**; weryfikatory Mentora uruchamiają Twoje testy na mutantach i zaliczają tylko testy, które je „zabijają”.\n"
        "## Wynik pytest\n"
        "`test_ceny.py::test_brutto_vat_23 PASSED`; przy FAILED pytest pokazuje linię assert z wartościami: `assert 12.299999 == 12.3`. Na dole podsumowanie: `3 passed, 1 failed in 0.05s`."),
    przyklad=kod("pytest", (
        "# test_magazyn_demo.py — uruchom: python -m pytest -v test_magazyn_demo.py\n"
        "import pytest\n\n\n"
        "def koszt_dostawy(razem):\n"
        "    if razem < 0:\n"
        "        raise ValueError(\"kwota nie może być ujemna\")\n"
        "    if razem >= 100:\n"
        "        return 0\n"
        "    return 9.99 if razem >= 50 else 14.99\n\n\n"
        "def test_dostawa_darmowa_od_100():\n"
        "    assert koszt_dostawy(100) == 0\n\n\n"
        "def test_dostawa_tuz_ponizej_progu():\n"
        "    assert koszt_dostawy(99.99) == 9.99\n\n\n"
        "def test_dostawa_mala_kwota():\n"
        "    wynik = koszt_dostawy(49.99)\n"
        "    assert wynik == 14.99\n\n\n"
        "def test_ujemna_kwota_to_blad():\n"
        "    with pytest.raises(ValueError, match=\"ujemna\"):\n"
        "        koszt_dostawy(-1)\n\n\n"
        "def test_suma_float():\n"
        "    assert 0.1 + 0.2 == pytest.approx(0.3)\n"), None),
    demonstracja={"tytul": "Pięć testów reguły dostawy", "kroki": [
        "Plik nazywa się `test_….py`, funkcje `test_…` — tylko takie pytest uruchamia. (W prawdziwym projekcie funkcja jest w osobnym module i importujesz ją: `from dostawa import koszt_dostawy`.)",
        "`test_dostawa_darmowa_od_100` — granica progu; `test_dostawa_tuz_ponizej_progu` — sąsiad granicy.",
        "`test_dostawa_mala_kwota` — AAA rozpisane: Act (wywołanie do zmiennej) i Assert.",
        "`pytest.raises(ValueError, match=\"ujemna\")` — przechodzi tylko, gdy funkcja rzuci ValueError z „ujemna” w treści.",
        "`pytest.approx` — 0.1 + 0.2 to 0.30000000000000004, a test przechodzi.",
        "Uruchom `python -m pytest -v test_magazyn_demo.py` → 5 passed.",
        "Mutacja: zmień w funkcji `razem >= 100` na `razem > 100` → pada dokładnie test granicy (1 failed). Przywróć."],
        "wynik": "5 passed; po mutacji `>=` → `>` — 1 failed (test_dostawa_darmowa_od_100) z komunikatem assert 9.99 == 0."},
    jak_uruchomic=["Zapisz jako test_magazyn_demo.py w PRACA.", "Terminal Mentora: `cd` do PRACA → `python -m pytest -v test_magazyn_demo.py`.",
                   "PyCharm: zielony trójkąt przy funkcji testu (interpreter środowiska kursu)."],
    cwiczenia=[
        C("prowadzone",
          "Na wzór demonstracji: dla `brutto(netto, vat=23)` (round 2) napisz w głowie 3 asserty i podaj oczekiwane wartości: (1) brutto(100), (2) brutto(10, 8), (3) brutto(0). (4) Jaki fragment kodu napiszesz, by sprawdzić, że `wydaj(5, 10)` rzuca ValueError (wpisz pierwszą linię bloku)? Czas: 15 minut.",
          "(1) 123.0; (2) 10.8; (3) 0.0; (4) with pytest.raises(ValueError):.",
          ["100 × 1.23.", "10 × 1.08.", "Wyjątek sprawdzasz menedżerem kontekstu pytest."],
          "`assert brutto(100) == 123.0`, `assert brutto(10, 8) == 10.8`, `assert brutto(0) == 0.0`; `with pytest.raises(ValueError):` + `wydaj(5, 10)` wcięte pod spodem.",
          [li("a", "(1) brutto(100)", 123.0), li("b", "(2) brutto(10, 8)", 10.8), li("c", "(3) brutto(0)", 0.0), tx("d", "(4) Pierwsza linia", "with pytest.raises(ValueError):")]),
        C("samodzielne",
          "Kolega napisał test: `def test_rabat(): wynik = rabat(250)` (bez assert). (1) Czy pytest uzna go za PASSED, gdy rabat() działa źle, ale nie rzuca wyjątku (tak/nie)? (2) Dla reguły „od 200 zł rabat 5%” (rabat zwraca procent) — który JEDEN assert złapie mutanta `> 200` zamiast `>= 200` (wpisz)? (3) Jak uruchomić tylko testy z „rabat” w nazwie (wpisz polecenie)? Czas: 15 minut.",
          "(1) tak; (2) assert rabat(200) == 5; (3) python -m pytest -k rabat.",
          ["Test bez assert sprawdza tylko, że nie było wyjątku.", "Mutant różni się zachowaniem dokładnie na granicy.", "Opcja wyboru po nazwie: -k."],
          "(1) tak — bez assert test niczego nie sprawdza; (2) `assert rabat(200) == 5` (mutant zwróci 0); (3) `python -m pytest -k rabat`.",
          [wy("a", "(1) PASSED mimo złego wyniku?", ["tak", "nie"], "tak"), tx("b", "(2) Assert", "assert rabat(200) == 5", bledy=[bl("assert rabat(250) == 5", "250 daje 5% w obu wersjach — mutant przeżyje; testuj granicę")]),
           tx("c", "(3) Polecenie", "python -m pytest -k rabat", zawiera=["pytest", "-k", "rabat"])]),
    ],
    typowe_bledy=[
        B("collected 0 items / no tests ran", "Plik nie zaczyna się od test_ albo funkcje nie zaczynają się od test_.", "Nazwy pliku i funkcji.", "test_nazwa.py i def test_cos():."),
        B("ModuleNotFoundError: No module named 'ceny' w teście", "pytest uruchomiony z innego katalogu niż moduł.", "`pwd` i `ls`.", "Uruchamiaj z katalogu projektu; testy obok modułu albo conftest.py w katalogu głównym."),
        B("assert 12.299999999999999 == 12.3 — FAILED", "Porównanie float bez zaokrąglenia/tolerancji.", "Wynik przed porównaniem.", "round() w funkcji albo pytest.approx w teście."),
    ],
    pulapki=["Testy zależne od kolejności (jeden zmienia dane, drugi na nich polega) — każdy test przygotowuje swoje dane.", "Test, który nigdy nie padł, może nic nie sprawdzać — zrób mutację."],
    zadania=["5 testów do funkcji z tygodnia 3 (pole, parzysta, maksimum, odwróć, silnia).", "Test wyjątku z pytest.raises.", "Mutacja: zepsuj funkcję i sprawdź, czy test pada."],
    pytania=[["Jak pytest znajduje testy?", "Pliki test_*.py, funkcje test_*."], ["Po co pytest.raises?", "Sprawdza, że kod rzuca oczekiwany wyjątek."], ["Czym jest mutant?", "Celowo zepsuta wersja kodu — dobry test ją wykrywa."]],
    podsumowanie="Piszesz testy pytest według AAA, testujesz wyjątki i liczby zmiennoprzecinkowe, uruchamiasz wybrane testy i sprawdzasz mutacją, że testy łapią błędy.",
    test=[T("Plik testów musi się nazywać:", ["testy.py", "test_cos.py", "cos.test", "TEST.py"], 1, "Wzorzec test_*.py."),
          T("Test bez assert:", ["zawsze FAILED", "PASSED, jeśli nie było wyjątku", "nie uruchomi się", "jest błędem składni"], 1, "Niczego nie sprawdza."),
          T("pytest.approx służy do:", ["napisów", "porównań liczb zmiennoprzecinkowych z tolerancją", "wyjątków", "plików"], 1, "0.1 + 0.2."),
          T("-k brutto uruchamia:", ["wszystkie testy", "testy z „brutto” w nazwie", "brutto.py", "nic"], 1, "Wybór po nazwie.")],
    w_praktyce=["Każdy defekt znaleziony ręcznie → test regresji w pytest.", "Nazwa testu = zdanie z wymagania: test_dostawa_darmowa_od_100."],
    zrodla=[Z.PYTEST_START, Z.PYTEST_ASSERT, Z.PYTEST_CHANGES],
)

PARAM = L(
    id="parametrize_fixture", nazwa="parametrize i fixtures: wiele przypadków w jednym teście, wspólne dane, tmp_path", tydzien=7,
    slowa=["parametrize", "fixture", "conftest.py", "tmp_path", "yield", "dane testowe", "ids", "scope", "monkeypatch"],
    cel="Po tej lekcji uruchamiasz jeden test dla wielu danych (@pytest.mark.parametrize), przygotowujesz wspólne dane fixturą (także z yield i w conftest.py) i testujesz zapis do plików w katalogu tymczasowym tmp_path.",
    po_co="Tabela klas równoważności i wartości brzegowych zamienia się 1:1 w parametrize. Fixtury to podstawa każdego frameworka testów — także Selenium (przeglądarka jako fixture w tygodniu 8).",
    wymagania=["Lekcja „pytest”.", "Menedżer zadań i kalkulator BMI z wcześniejszych tygodni."],
    wyjasnienie=(
        "## parametrize — tabela przypadków\n"
        "```\nimport pytest\n\n@pytest.mark.parametrize(\"razem, oczekiwany\", [\n    (49.99, 14.99),\n    (50, 9.99),\n    (99.99, 9.99),\n    (100, 0),\n])\ndef test_koszt_dostawy(razem, oczekiwany):\n    assert koszt_dostawy(razem) == oczekiwany\n```\n"
        "Pierwszy argument — nazwy parametrów (przecinek w napisie), drugi — lista krotek. pytest uruchomi 4 osobne testy: `test_koszt_dostawy[49.99-14.99]` itd. Padnie tylko przypadek z defektem — reszta pokaże, że działa.\n"
        "## fixture — przygotowanie danych\n"
        "```\n@pytest.fixture\ndef menedzer():\n    lista = []\n    dodaj(lista, \"Zamówić papier\")\n    dodaj(lista, \"Policzyć zeszyty\")\n    return lista\n\ndef test_otwarte(menedzer):\n    assert len(otwarte(menedzer)) == 2\n```\n"
        "Test prosi o fixturę przez **nazwę parametru**. Każdy test dostaje **świeżą** kopię — testy nie psują sobie danych.\n"
        "## yield — sprzątanie\n"
        "W fixturze `yield wartosc` zamiast return: kod po yield wykona się po teście (zamknij plik, bazę, przeglądarkę).\n"
        "## conftest.py\n"
        "Fixtury w pliku conftest.py w katalogu testów są dostępne we wszystkich testach bez importu.\n"
        "## tmp_path — pliki w testach\n"
        "Wbudowana fixtura: osobny pusty katalog dla każdego testu. `plik = tmp_path / \"zadania.json\"` — test zapisuje i czyta, nie dotykając Twoich prawdziwych danych.\n"
        "## Inne wbudowane\n"
        "`monkeypatch` podmienia na czas testu np. funkcję input() albo zmienną środowiskową; `capsys` przechwytuje to, co wypisał print."),
    przyklad=kod("parametrize_fixture", (
        "# test_menedzer_demo.py — python -m pytest -v test_menedzer_demo.py\n"
        "import json\n"
        "import pytest\n\n\n"
        "def kategoria_bmi(bmi):\n"
        "    if bmi < 18.5:\n"
        "        return \"niedowaga\"\n"
        "    if bmi < 25:\n"
        "        return \"norma\"\n"
        "    if bmi < 30:\n"
        "        return \"nadwaga\"\n"
        "    return \"otyłość\"\n\n\n"
        "@pytest.mark.parametrize(\"bmi, oczekiwana\", [\n"
        "    (18.4, \"niedowaga\"), (18.5, \"norma\"), (24.9, \"norma\"),\n"
        "    (25, \"nadwaga\"), (29.9, \"nadwaga\"), (30, \"otyłość\"),\n"
        "])\n"
        "def test_kategoria_bmi(bmi, oczekiwana):\n"
        "    assert kategoria_bmi(bmi) == oczekiwana\n\n\n"
        "@pytest.fixture\n"
        "def zadania():\n"
        "    return [{\"tytul\": \"Zamówić papier\", \"zrobione\": False}, {\"tytul\": \"Policzyć zeszyty\", \"zrobione\": True}]\n\n\n"
        "def test_otwarte(zadania):\n"
        "    assert [z[\"tytul\"] for z in zadania if not z[\"zrobione\"]] == [\"Zamówić papier\"]\n\n\n"
        "def test_zapis_i_odczyt(zadania, tmp_path):\n"
        "    plik = tmp_path / \"zadania.json\"\n"
        "    plik.write_text(json.dumps(zadania, ensure_ascii=False), encoding=\"utf-8\")\n"
        "    assert json.loads(plik.read_text(encoding=\"utf-8\")) == zadania\n"), None),
    demonstracja={"tytul": "6 granic BMI, fixture z zadaniami i zapis w tmp_path", "kroki": [
        "`@pytest.mark.parametrize(\"bmi, oczekiwana\", [...])` — 6 par = 6 testów; dane to wartości brzegowe progów 18.5, 25 i 30.",
        "`pytest -v` pokaże `test_kategoria_bmi[18.4-niedowaga] PASSED` itd. — od razu widać, który przypadek pada.",
        "`@pytest.fixture def zadania()` — wspólne dane; zwraca nową listę dla KAŻDEGO testu.",
        "`test_otwarte(zadania)` — nazwa parametru = nazwa fixtury; pytest sam ją wywoła.",
        "`test_zapis_i_odczyt(zadania, tmp_path)` — dwie fixtury naraz; tmp_path to pusty katalog tymczasowy.",
        "Zapis JSON i odczyt — porównanie całych list słowników jednym assert.",
        "Uruchom: 8 passed. Zmień w kategoria_bmi `< 25` na `<= 25` — padnie dokładnie przypadek [25-nadwaga]."],
        "wynik": "8 passed (6 z parametrize + 2); po mutacji progu 25 — 1 failed z nazwą przypadku w nawiasie."},
    jak_uruchomic=["Zapisz jako test_menedzer_demo.py → terminal Mentora → `python -m pytest -v test_menedzer_demo.py`."],
    cwiczenia=[
        C("prowadzone",
          "Reguła rabatu: < 100 → 0, 100–299.99 → 5, ≥ 300 → 10. Na wzór demonstracji wypisz listę par dla parametrize (wartości brzegowe dwupunktowo). (1) Ile par? (2) Jaki oczekiwany rabat dla 299.99? (3) Ile testów pokaże pytest -v dla parametrize z tą listą? Czas: 15 minut.",
          "(1) 4 pary: (99.99, 0), (100, 5), (299.99, 5), (300, 10); (2) 5; (3) 4.",
          ["Dwie granice: 100 i 300.", "Dla każdej: tuż pod i na granicy.", "Każda para = osobny test."],
          "(1) 4 pary; (2) 5; (3) 4 testy, np. test_rabat[99.99-0].",
          [li("a", "(1) Liczba par", 4), li("b", "(2) Rabat dla 299.99", 5, bledy=[bl(10, "299.99 < 300 — jeszcze próg 5%")]), li("c", "(3) Liczba testów", 4)]),
        C("samodzielne",
          "Dwa testy używają tej samej listy produktów: test_a usuwa pierwszy produkt, test_b sprawdza, że lista ma 3 produkty. (1) Lista jako zmienna globalna w pliku testów — czy test_b może paść zależnie od kolejności (tak/nie)? (2) Jakim dekoratorem zrobisz z funkcji tworzącej listę fixturę (wpisz)? "
          "(3) Gdzie zapisze plik test zapisu, żeby nie zniszczyć Twoich danych — wybierz: katalog PRACA / tmp_path / pulpit. Czas: 15 minut.",
          "(1) tak; (2) @pytest.fixture; (3) tmp_path.",
          ["Globalna lista jest wspólna — zmiany zostają.", "Fixtura tworzy dane od nowa dla każdego testu.", "Wbudowana fixtura z katalogiem tymczasowym."],
          "(1) tak — test_a zmienia wspólną listę; (2) `@pytest.fixture`; (3) `tmp_path`.",
          [wy("a", "(1) Zależność od kolejności?", ["tak", "nie"], "tak"), tx("b", "(2) Dekorator", "@pytest.fixture"), wy("c", "(3) Gdzie zapis", ["katalog PRACA", "tmp_path", "pulpit"], "tmp_path")]),
    ],
    typowe_bledy=[
        B("fixture 'menedzer' not found", "Literówka w nazwie parametru albo fixtura w innym pliku bez conftest.py.", "Lista dostępnych: `python -m pytest --fixtures`.", "Ta sama nazwa; fixtury wspólne w conftest.py."),
        B("ValueError/TypeError w parametrize: wrong number of values", "Liczba nazw w napisie ≠ liczba elementów w krotkach.", "Porównaj \"a, b\" z (x, y).", "Ta sama liczba nazw i wartości w każdej krotce."),
        B("Test przechodzi pojedynczo, pada w całym zestawie", "Wspólne dane modyfikowane przez inne testy.", "Uruchom `-p no:randomly`/pojedynczo i porównaj.", "Dane w fixturze, nie w zmiennej globalnej."),
    ],
    pulapki=["parametrize z 50 przypadkami „na wszelki wypadek” — wybieraj technikami, nie losowo.", "Fixture, która łączy się z prawdziwą bazą lub siecią — w testach jednostkowych używaj danych w pamięci i tmp_path."],
    zadania=["parametrize: 6 przypadków BMI w jednym teście.", "Fixture z menedżerem zadań użyta w 4 testach.", "Test zapisu/odczytu z tmp_path."],
    pytania=[["Co robi parametrize?", "Uruchamia ten sam test dla wielu zestawów danych."], ["Jak test dostaje fixturę?", "Przez parametr o nazwie fixtury."], ["Po co tmp_path?", "Pusty katalog tymczasowy na pliki testu."]],
    podsumowanie="Zamieniasz tabelę przypadków w parametrize, przygotowujesz świeże dane fixturami (także w conftest.py) i testujesz pliki w tmp_path.",
    test=[T("Ile testów da parametrize z listą 5 krotek?", ["1", "5", "10", "zależy od assert"], 1, "Każda krotka osobno."),
          T("Fixture domyślnie tworzy dane:", ["raz na cały plik", "od nowa dla każdego testu", "nigdy", "tylko dla pierwszego testu"], 1, "scope=\"function\"."),
          T("Kod po yield w fixturze wykona się:", ["przed testem", "po teście", "nigdy", "dwa razy"], 1, "Sprzątanie."),
          T("Plik z fixturami wspólnymi dla wielu plików testów:", ["fixtures.py", "conftest.py", "setup.py", "__init__.py"], 1, "pytest wczytuje go automatycznie.")],
    w_praktyce=["Tabela z przypadkami testowymi (tydz. 9) i parametrize mają te same wiersze.", "Przeglądarka, baza testowa, zalogowany użytkownik — wszystko jako fixtury."],
    zrodla=[Z.PYTEST_PARAM, Z.PYTEST_FIX, Z.PYTEST_TMP],
)

# =========================================================================== TYDZIEŃ 8
SELENIUM = L(
    id="selenium", nazwa="Selenium WebDriver: przeglądarka, lokatory (ID, CSS, XPath), formularze", tydzien=8,
    slowa=["Selenium", "WebDriver", "Edge", "Chrome", "Selenium Manager", "lokator", "By.ID", "By.CSS_SELECTOR", "By.XPATH", "find_element", "send_keys", "click", "text", "screenshot", "quit"],
    cel="Po tej lekcji uruchamiasz przeglądarkę z Selenium (Selenium Manager sam dobiera sterownik), otwierasz stronę, znajdujesz elementy lokatorami ID, CSS i XPath, wypełniasz formularz, czytasz tekst, robisz zrzut ekranu i zamykasz przeglądarkę.",
    po_co="Testy E2E w przeglądarce to najczęściej wymieniana umiejętność w ogłoszeniach dla Junior QA Automation. Selenium jest standardem W3C WebDriver od lat.",
    wymagania=["Lekcje „Klasy” i „pytest”.", "Przeglądarka Microsoft Edge (wbudowana w Windows 10/11) albo Chrome.",
               "Sklep testowy z paczki (projekty/sklep_testowy) uruchomiony: `python app.py` → http://127.0.0.1:5001.",
               "Internet przy pierwszym uruchomieniu (Selenium Manager pobiera sterownik msedgedriver i zapisuje go w pamięci podręcznej)."],
    wyjasnienie=(
        "## Jak to działa\n"
        "Twój skrypt → biblioteka selenium → **sterownik** (msedgedriver/chromedriver) → przeglądarka. Od Selenium 4.6 **Selenium Manager** sam wykrywa wersję przeglądarki i pobiera pasujący sterownik (raz, potem bierze z pamięci podręcznej `~/.cache/selenium`) — nie pobierasz niczego ręcznie.\n"
        "## Pierwszy skrypt\n"
        "```\nfrom selenium import webdriver\nfrom selenium.webdriver.common.by import By\n\ndriver = webdriver.Edge()\ndriver.get(\"http://127.0.0.1:5001\")\nprint(driver.title)\ndriver.quit()\n```\n"
        "`driver.quit()` zamyka przeglądarkę i sterownik — zawsze, najlepiej w try/finally albo w fixturze z yield.\n"
        "## Lokatory — jak znaleźć element\n"
        "Prawy klik na elemencie → **Zbadaj** (DevTools) pokazuje HTML: `<input id=\"login\" name=\"login\" class=\"pole\">`.\n"
        "| lokator | przykład | kiedy |\n|---|---|---|\n"
        "| `By.ID` | `(By.ID, \"login\")` | najlepszy, jeśli id jest unikalne i stałe |\n"
        "| `By.CSS_SELECTOR` | `\"#login\"`, `\".komunikat\"`, `\"button[type=submit]\"`, `\"#koszyk .pozycja\"` | szybki, czytelny — domyślny wybór |\n"
        "| `By.XPATH` | `\"//button[text()='Zaloguj']\"` | gdy trzeba szukać po tekście albo „w górę” drzewa |\n"
        "| `By.NAME`, `By.LINK_TEXT` | `\"login\"`, `\"Koszyk\"` | formularze, linki |\n"
        "Unikaj kruchych lokatorów: długich ścieżek XPath od korzenia (`/html/body/div[2]/…`) i klas od wyglądu. Najlepsze są atrybuty dla testów, np. `data-test=\"zaloguj\"` → `[data-test=zaloguj]`.\n"
        "## Akcje\n"
        "`el = driver.find_element(By.ID, \"login\")` (brak → NoSuchElementException); `find_elements` — lista (pusta, gdy brak). `el.clear()`, `el.send_keys(\"tester\")`, `el.click()`, `el.text`, `el.get_attribute(\"value\")`, `el.is_displayed()`. "
        "`driver.save_screenshot(\"zrzut.png\")` — zrzut do raportu błędu.\n"
        "## Strony do ćwiczeń\n"
        "Kurs używa **lokalnego** sklepu testowego z paczki (działa offline, ma celowe defekty do znalezienia). Publiczne strony ćwiczeniowe (np. the-internet.herokuapp.com, saucedemo.com) są opcją dodatkową — mogą się zmienić lub zniknąć."),
    przyklad=kod("selenium", (
        "# selenium_start.py — wymaga działającego sklepu testowego (python app.py w projekty/sklep_testowy)\n"
        "from selenium import webdriver\n"
        "from selenium.webdriver.common.by import By\n\n"
        "ADRES = \"http://127.0.0.1:5001\"\n\n"
        "driver = webdriver.Edge()          # Chrome: webdriver.Chrome()\n"
        "try:\n"
        "    driver.get(ADRES + \"/logowanie\")\n"
        "    print(\"Tytuł:\", driver.title)\n"
        "    driver.find_element(By.ID, \"login\").send_keys(\"tester\")\n"
        "    driver.find_element(By.CSS_SELECTOR, \"input[name=haslo]\").send_keys(\"Test123!\")\n"
        "    driver.find_element(By.XPATH, \"//button[text()='Zaloguj']\").click()\n"
        "    powitanie = driver.find_element(By.CSS_SELECTOR, \"[data-test=powitanie]\").text\n"
        "    print(\"Po zalogowaniu:\", powitanie)\n"
        "    produkty = driver.find_elements(By.CSS_SELECTOR, \"#produkty .produkt\")\n"
        "    print(\"Produktów na stronie:\", len(produkty))\n"
        "    driver.save_screenshot(\"po_zalogowaniu.png\")\n"
        "finally:\n"
        "    driver.quit()\n"), None),
    demonstracja={"tytul": "Logowanie do sklepu testowego trzema rodzajami lokatorów", "kroki": [
        "Uruchom sklep: terminal Mentora → `cd` do projekty\\sklep_testowy → `python app.py` (zostaw okno otwarte). W drugim oknie uruchomisz skrypt.",
        "`webdriver.Edge()` — Selenium Manager sprawdza wersję Edge i pobiera msedgedriver (pierwszy raz kilka sekund, potem z pamięci podręcznej). Otwiera się okno przeglądarki z paskiem „sterowana przez oprogramowanie testowe”.",
        "`driver.get(...)` — otwiera stronę logowania; `driver.title` — tytuł z `<title>`.",
        "`By.ID, \"login\"` — pole loginu ma `id=\"login\"`; `send_keys` wpisuje tekst.",
        "`By.CSS_SELECTOR, \"input[name=haslo]\"` — pole hasła wskazane atrybutem name.",
        "`By.XPATH, \"//button[text()='Zaloguj']\"` — przycisk po tekście.",
        "`[data-test=powitanie]` — element z atrybutem przeznaczonym dla testów; `.text` zwraca widoczny tekst.",
        "`find_elements` — lista wszystkich `.produkt` w `#produkty`; `len` = liczba produktów.",
        "`save_screenshot` zapisuje PNG w katalogu roboczym; `finally: driver.quit()` zamyka przeglądarkę nawet przy błędzie."],
        "wynik": "Tytuł strony, „Po zalogowaniu: Witaj, tester!”, liczba produktów (20) i plik po_zalogowaniu.png."},
    jak_uruchomic=["Okno 1 (terminal Mentora): `cd` do materiałów kursu → `cd projekty\\sklep_testowy` → `python app.py`.",
                   "Okno 2: w PRACA `python selenium_start.py`. Pierwsze uruchomienie wymaga internetu (pobranie sterownika).",
                   "Bez Edge: zamień na `webdriver.Chrome()` (Selenium Manager pobierze Chrome for Testing, jeśli Chrome nie ma)."],
    cwiczenia=[
        C("prowadzone",
          "HTML: `<button id=\"dodaj-3\" class=\"btn btn-primary\" data-test=\"dodaj\">Dodaj do koszyka</button>`. Na wzór demonstracji wpisz lokatory: (1) po ID, (2) CSS po atrybucie data-test, (3) XPath po tekście. Czas: 15 minut.",
          "(1) dodaj-3; (2) [data-test=dodaj]; (3) //button[text()='Dodaj do koszyka'].",
          ["By.ID przyjmuje samą wartość id.", "CSS po atrybucie: [nazwa=wartość].", "XPath: //znacznik[text()='…']."],
          "(1) `(By.ID, \"dodaj-3\")`; (2) `(By.CSS_SELECTOR, \"[data-test=dodaj]\")` — ale uwaga: każdy przycisk „Dodaj” ma ten sam data-test, więc find_element weźmie pierwszy; (3) `(By.XPATH, \"//button[text()='Dodaj do koszyka']\")`.",
          [tx("a", "(1) ID", "dodaj-3"), tx("b", "(2) CSS", "[data-test=dodaj]", zawiera=["data-test", "dodaj"]), tx("c", "(3) XPath", "//button[text()='Dodaj do koszyka']", zawiera=["//button", "text()", "Dodaj do koszyka"])]),
        C("samodzielne",
          "Oceń lokatory (dobry / kruchy): (1) `/html/body/div[2]/div/form/input[1]`; (2) `#login`; (3) `.btn-primary` (na stronie są 4 takie przyciski); (4) `[data-test=koszyk-suma]`. Dodatkowo (5): `find_element` nie znalazł elementu — jaki wyjątek (wybierz)? Czas: 15 minut.",
          "(1) kruchy; (2) dobry; (3) kruchy; (4) dobry; (5) NoSuchElementException.",
          ["Ścieżka od korzenia psuje się przy każdej zmianie układu.", "Klasa od wyglądu nie jest unikalna.", "Atrybuty dla testów są stabilne."],
          "(1) kruchy; (2) dobry (unikalne id); (3) kruchy (nieunikalny, od wyglądu); (4) dobry; (5) NoSuchElementException.",
          [wy("a", "(1) /html/body/…", ["dobry", "kruchy"], "kruchy"), wy("b", "(2) #login", ["dobry", "kruchy"], "dobry"), wy("c", "(3) .btn-primary", ["dobry", "kruchy"], "kruchy"),
           wy("d", "(4) [data-test=koszyk-suma]", ["dobry", "kruchy"], "dobry"), wy("e", "(5) Wyjątek", ["TimeoutException", "NoSuchElementException", "ValueError", "KeyError"], "NoSuchElementException")]),
    ],
    typowe_bledy=[
        B("selenium.common.exceptions.NoSuchElementException: Unable to locate element", "Zły lokator albo element jeszcze się nie pojawił.", "DevTools → Ctrl+F w zakładce Elements → wpisz selektor CSS.", "Popraw lokator; dla elementów ładowanych później — WebDriverWait (następna lekcja)."),
        B("SessionNotCreatedException / Unable to obtain driver", "Brak przeglądarki albo brak internetu przy pierwszym pobraniu sterownika.", "Czy Edge/Chrome się otwiera? Czy jest internet?", "Uruchom z internetem raz (sterownik trafi do pamięci podręcznej) albo użyj innej przeglądarki."),
        B("ConnectionRefusedError / ERR_CONNECTION_REFUSED na stronie", "Sklep testowy nie jest uruchomiony.", "Otwórz http://127.0.0.1:5001 ręcznie.", "W osobnym oknie `python app.py` w projekty/sklep_testowy."),
    ],
    pulapki=["Brak driver.quit() — w tle zostają dziesiątki procesów przeglądarki.", "time.sleep(5) „na wszelki wypadek” — wolne i niepewne testy; czekaj na warunek (WebDriverWait)."],
    zadania=["Pierwszy skrypt: otwórz sklep testowy, zaloguj się, zrób zrzut ekranu.", "5 elementów strony znalezionych trzema rodzajami lokatorów.", "Formularz zamówienia: wypełnij i odczytaj komunikat."],
    pytania=[["Co robi Selenium Manager?", "Sam dobiera i pobiera sterownik (i w razie potrzeby przeglądarkę)."], ["Który lokator jest najlepszy?", "Unikalny i stały: id albo atrybut data-test."], ["Po co driver.quit()?", "Zamyka przeglądarkę i sterownik."]],
    podsumowanie="Uruchamiasz przeglądarkę z Selenium, znajdujesz elementy lokatorami ID/CSS/XPath, wypełniasz formularze, czytasz tekst, robisz zrzut ekranu i zawsze zamykasz przeglądarkę.",
    test=[T("Od której wersji Selenium sam pobiera sterowniki (Selenium Manager)?", ["3.0", "4.6", "5.0", "nigdy"], 1, "Wbudowany od 4.6."),
          T("find_elements, gdy nic nie pasuje, zwraca:", ["None", "pustą listę", "NoSuchElementException", "False"], 1, "Lista może być pusta."),
          T("Najbardziej kruchy lokator:", ["#login", "[data-test=zaloguj]", "/html/body/div[3]/form/input[2]", "input[name=login]"], 2, "Zależy od całego układu strony."),
          T("Tekst widoczny w elemencie:", ["el.value", "el.text", "el.html", "el.get()"], 1, "Właściwość text.")],
    w_praktyce=["Prośba do programistów: atrybuty data-test w kluczowych elementach — testy przestają się psuć przy zmianie wyglądu.", "Zrzut ekranu przy każdym nieudanym teście E2E."],
    zrodla=[Z.SEL_MANAGER, Z.SEL_WAITS, Z.SEL_POM],
)

WAIT_POM = L(
    id="wait_pom", nazwa="WebDriverWait i Page Object Model", tydzien=8,
    slowa=["WebDriverWait", "expected_conditions", "EC", "visibility_of_element_located", "element_to_be_clickable", "TimeoutException", "implicit wait",
           "Page Object Model", "POM", "LoginPage", "fixture przeglądarki", "flaky"],
    cel="Po tej lekcji czekasz na elementy WebDriverWait z expected_conditions zamiast time.sleep, budujesz Page Object (klasa strony z lokatorami i metodami akcji) i piszesz testy pytest, które używają fixtury przeglądarki i stron — czytelne jak scenariusz.",
    po_co="Niestabilne (flaky) testy E2E to największy problem automatyzacji; czekanie na warunek i POM to odpowiedź, o którą zapyta każdy rekruter QA Automation.",
    wymagania=["Lekcje „Selenium WebDriver”, „Klasy”, „parametrize i fixtures”.", "Sklep testowy uruchomiony (python app.py)."],
    wyjasnienie=(
        "## Dlaczego czekać\n"
        "Strona ładuje się asynchronicznie: element pojawia się po 0,3 s albo po 2 s. `find_element` od razu → NoSuchElementException. `time.sleep(3)` — za krótko na wolnym komputerze, za długo na szybkim.\n"
        "## Czekanie jawne (explicit wait)\n"
        "```\nfrom selenium.webdriver.support.ui import WebDriverWait\nfrom selenium.webdriver.support import expected_conditions as EC\n\nczekaj = WebDriverWait(driver, 10)\nel = czekaj.until(EC.visibility_of_element_located((By.CSS_SELECTOR, \".promocja\")))\n```\n"
        "Sprawdza warunek co 0,5 s, maksymalnie 10 s; zwraca element, gdy warunek spełniony, albo rzuca **TimeoutException**. Najczęstsze warunki:\n"
        "| warunek | czeka, aż |\n|---|---|\n"
        "| `presence_of_element_located` | element jest w HTML |\n| `visibility_of_element_located` | element jest widoczny |\n"
        "| `element_to_be_clickable` | widoczny i aktywny |\n| `text_to_be_present_in_element` | ma dany tekst |\n| `url_contains` | adres zawiera fragment |\n"
        "Czekanie domyślne (implicit, `driver.implicitly_wait(5)`) działa dla każdego find_element — dokumentacja Selenium odradza mieszanie go z jawnym. W kursie: tylko jawne.\n"
        "## Page Object Model (POM)\n"
        "Każda strona = klasa: lokatory w jednym miejscu, metody to działania użytkownika.\n"
        "```\nclass LoginPage:\n    LOGIN = (By.ID, \"login\")\n    HASLO = (By.ID, \"haslo\")\n    ZALOGUJ = (By.CSS_SELECTOR, \"[data-test=zaloguj]\")\n    BLAD = (By.CSS_SELECTOR, \"[data-test=blad]\")\n\n    def __init__(self, driver):\n        self.driver = driver\n\n    def open(self):\n        self.driver.get(ADRES + \"/logowanie\")\n        return self\n\n    def login(self, login, haslo):\n        ...\n\n    def error_text(self):\n        ...\n```\n"
        "Test mówi **co** (`LoginPage(driver).open().login(\"tester\", \"zle\")`), strona wie **jak**. Zmiana id pola = poprawka w jednym miejscu, nie w 30 testach. Asercje trzymasz w testach, nie w klasach stron.\n"
        "## Fixture przeglądarki\n"
        "W conftest.py: `@pytest.fixture def driver(): d = webdriver.Edge(); yield d; d.quit()` — każdy test dostaje świeżą przeglądarkę i zawsze ją zamyka. Tryb bez okna (headless, przydatny w CI): `opcje = webdriver.EdgeOptions(); opcje.add_argument(\"--headless=new\")`."),
    przyklad=kod("wait_pom", (
        "# pages/login_page.py + tests/test_logowanie.py (w jednym pliku dla czytelności)\n"
        "import pytest\n"
        "from selenium import webdriver\n"
        "from selenium.webdriver.common.by import By\n"
        "from selenium.webdriver.support import expected_conditions as EC\n"
        "from selenium.webdriver.support.ui import WebDriverWait\n\n"
        "ADRES = \"http://127.0.0.1:5001\"\n\n\n"
        "class LoginPage:\n"
        "    LOGIN = (By.ID, \"login\")\n"
        "    HASLO = (By.ID, \"haslo\")\n"
        "    ZALOGUJ = (By.CSS_SELECTOR, \"[data-test=zaloguj]\")\n"
        "    BLAD = (By.CSS_SELECTOR, \"[data-test=blad]\")\n"
        "    POWITANIE = (By.CSS_SELECTOR, \"[data-test=powitanie]\")\n\n"
        "    def __init__(self, driver):\n"
        "        self.driver = driver\n"
        "        self.czekaj = WebDriverWait(driver, 10)\n\n"
        "    def open(self):\n"
        "        self.driver.get(ADRES + \"/logowanie\")\n"
        "        return self\n\n"
        "    def login(self, login, haslo):\n"
        "        self.czekaj.until(EC.visibility_of_element_located(self.LOGIN)).send_keys(login)\n"
        "        self.driver.find_element(*self.HASLO).send_keys(haslo)\n"
        "        self.driver.find_element(*self.ZALOGUJ).click()\n"
        "        return self\n\n"
        "    def error_text(self):\n"
        "        return self.czekaj.until(EC.visibility_of_element_located(self.BLAD)).text\n\n"
        "    def greeting(self):\n"
        "        return self.czekaj.until(EC.visibility_of_element_located(self.POWITANIE)).text\n\n\n"
        "@pytest.fixture\n"
        "def driver():\n"
        "    opcje = webdriver.EdgeOptions()\n"
        "    opcje.add_argument(\"--headless=new\")\n"
        "    d = webdriver.Edge(options=opcje)\n"
        "    yield d\n"
        "    d.quit()\n\n\n"
        "def test_logowanie_poprawne(driver):\n"
        "    assert \"tester\" in LoginPage(driver).open().login(\"tester\", \"Test123!\").greeting()\n\n\n"
        "def test_bledne_haslo(driver):\n"
        "    assert \"Błędny login lub hasło\" in LoginPage(driver).open().login(\"tester\", \"zle\").error_text()\n"), None),
    demonstracja={"tytul": "LoginPage z czekaniem i dwa testy-scenariusze", "kroki": [
        "Lokatory jako atrybuty klasy (krotki `(By…, \"…\")`) — jedno miejsce do zmiany.",
        "`self.czekaj = WebDriverWait(driver, 10)` — jeden obiekt czekania na stronę.",
        "`open()` zwraca `self` — dzięki temu można łączyć: `LoginPage(d).open().login(...)`.",
        "`login()` czeka, aż pole loginu będzie widoczne, potem wpisuje dane i klika.",
        "`find_element(*self.HASLO)` — gwiazdka rozpakowuje krotkę na dwa argumenty (By.ID, \"haslo\").",
        "`error_text()` i `greeting()` czekają na komunikat — po kliknięciu strona się przeładowuje.",
        "Fixture `driver` z headless i yield → quit zawsze, także po FAILED.",
        "Testy czytają się jak zdanie; asercje są w testach, nie w klasie strony.",
        "Uruchom: `python -m pytest -v` (sklep musi działać) → 2 passed."],
        "wynik": "2 passed: logowanie poprawne (powitanie zawiera „tester”) i błędne hasło (komunikat „Błędny login lub hasło”)."},
    jak_uruchomic=["Struktura w PRACA: `pages/__init__.py` (pusty), `pages/login_page.py`, `tests/test_logowanie.py`, `conftest.py` z fixturą driver.",
                   "Okno 1: sklep testowy `python app.py`; okno 2 w PRACA: `python -m pytest -v`.",
                   "Chcesz widzieć przeglądarkę? Usuń linię z `--headless=new`."],
    cwiczenia=[
        C("prowadzone",
          "Na wzór LoginPage zaprojektuj CartPage koszyka. Wpisz: (1) lokator CSS sumy koszyka z atrybutem data-test=\"suma\"; (2) warunek EC, na który czekasz przed odczytem tekstu sumy; (3) co zwraca metoda add(…) w stylu demonstracji, żeby dało się łączyć wywołania. Czas: 15 minut.",
          "(1) [data-test=suma]; (2) visibility_of_element_located; (3) self.",
          ["Atrybut dla testów w nawiasach kwadratowych.", "Tekst odczytujesz, gdy element jest widoczny.", "open() w demonstracji zwraca…"],
          "(1) `SUMA = (By.CSS_SELECTOR, \"[data-test=suma]\")`; (2) `EC.visibility_of_element_located(self.SUMA)`; (3) `return self`.",
          [tx("a", "(1) Lokator", "[data-test=suma]", zawiera=["data-test", "suma"]), wy("b", "(2) Warunek", ["presence_of_element_located", "visibility_of_element_located", "url_contains", "time.sleep"], "visibility_of_element_located"),
           tx("c", "(3) Zwraca", "self")]),
        C("samodzielne",
          "Test czasem pada (flaky): `driver.find_element(By.ID, \"promocja\")` zaraz po get(); promocja pokazuje się po ok. 1,5 s. Wybierz: (1) najlepsza poprawka: time.sleep(5) / WebDriverWait(driver, 10).until(EC.visibility_of_element_located(...)) / implicitly_wait(60); (2) jaki wyjątek, jeśli promocja nie pojawi się w 10 s; "
          "(3) gdzie umieścisz asercję „promocja zawiera −10%”: w metodzie klasy strony / w teście. Czas: 15 minut.",
          "(1) WebDriverWait…; (2) TimeoutException; (3) w teście.",
          ["Czekasz na warunek, nie na zegar.", "until rzuca wyjątek po przekroczeniu czasu.", "Klasa strony wie JAK, test sprawdza CO."],
          "(1) `WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, \"promocja\")))`; (2) TimeoutException; (3) w teście — strona zwraca tekst, test go sprawdza.",
          [wy("a", "(1) Poprawka", ["time.sleep(5)", "WebDriverWait(driver, 10).until(EC.visibility_of_element_located(...))", "implicitly_wait(60)"], "WebDriverWait(driver, 10).until(EC.visibility_of_element_located(...))"),
           wy("b", "(2) Wyjątek", ["NoSuchElementException", "TimeoutException", "ValueError"], "TimeoutException"), wy("c", "(3) Asercja", ["w metodzie klasy strony", "w teście"], "w teście")]),
    ],
    typowe_bledy=[
        B("selenium.common.exceptions.TimeoutException: Message:", "Warunek nie spełnił się w czasie: zły lokator albo element naprawdę się nie pojawił (bug?).", "Zrzut ekranu w momencie błędu; sprawdź lokator w DevTools.", "Popraw lokator; jeśli element powinien być — zgłoś defekt."),
        B("ElementClickInterceptedException", "Inny element (baner, okno) zasłania przycisk.", "Zrzut ekranu.", "Zamknij baner w kroku testu albo czekaj element_to_be_clickable."),
        B("StaleElementReferenceException", "Strona się przeładowała, a używasz starego elementu.", "Czy po kliknięciu była nawigacja?", "Znajdź element ponownie po przeładowaniu (metoda strony za każdym razem szuka od nowa)."),
    ],
    pulapki=["Asercje w Page Objectach — klasa przestaje być wielokrotnego użytku.", "Testy E2E zależne od siebie (test 2 korzysta z koszyka testu 1) — każdy test zaczyna od czystego stanu."],
    zadania=["Formularz zamówienia z WebDriverWait — bez time.sleep.", "Page Object LoginPage z metodami open(), login(), error_text().", "5 testów E2E sklepu w POM z fixturą driver."],
    pytania=[["Dlaczego nie time.sleep?", "Za krótki albo za długi; czekanie na warunek jest szybsze i pewniejsze."], ["Co zawiera Page Object?", "Lokatory i metody akcji jednej strony — bez asercji."], ["Co rzuca WebDriverWait po przekroczeniu czasu?", "TimeoutException."]],
    podsumowanie="Czekasz na warunki WebDriverWait, budujesz Page Objecty i piszesz stabilne testy E2E z fixturą przeglądarki, czytelne jak scenariusz.",
    test=[T("WebDriverWait(driver, 10).until(...) sprawdza warunek:", ["raz po 10 s", "co ok. 0,5 s do 10 s", "w nieskończoność", "tylko raz"], 1, "Polling do limitu."),
          T("W POM asercje umieszczasz:", ["w klasach stron", "w testach", "w conftest.py", "nigdzie"], 1, "Strona = jak, test = co."),
          T("Element przykryty banerem przy click():", ["NoSuchElementException", "ElementClickInterceptedException", "TimeoutException", "ValueError"], 1, "Coś przechwyciło kliknięcie."),
          T("Fixture driver z yield gwarantuje:", ["szybszy test", "zamknięcie przeglądarki po teście", "brak błędów", "tryb headless"], 1, "Kod po yield = sprzątanie.")],
    w_praktyce=["Każdy nowy ekran aplikacji = nowa klasa strony.", "Test flaky w CI: najpierw zrzut i lokator, potem warunek czekania — nigdy sleep."],
    zrodla=[Z.SEL_WAITS, Z.SEL_API_WAIT, Z.SEL_POM, Z.PYTEST_FIX],
)

# =========================================================================== TYDZIEŃ 9
BUG = L(
    id="bug_raport", nazwa="Przypadki testowe i raporty błędów, które programista rozumie bez pytań", tydzien=9,
    slowa=["przypadek testowy", "test case", "scenariusz", "bug raport", "zgłoszenie defektu", "kroki odtworzenia", "oczekiwany wynik", "rzeczywisty wynik",
           "priorytet", "ważność", "severity", "środowisko", "Jira", "zrzut ekranu", "testowanie eksploracyjne"],
    cel="Po tej lekcji zapisujesz przypadki testowe w tabeli (ID, warunki wstępne, kroki, dane, oczekiwany wynik) i raporty błędów z tytułem, krokami odtworzenia, wynikiem oczekiwanym i rzeczywistym, środowiskiem, ważnością i dowodem.",
    po_co="Raport błędu to najczęstszy produkt pracy testera. Dobry naprawia się szybko; zły wraca z pytaniem „nie mogę odtworzyć” i blokuje całe wydanie.",
    wymagania=["Lekcja „Podstawy testowania”.", "Sklep testowy uruchomiony — ma kilka celowo wprowadzonych defektów do znalezienia."],
    wyjasnienie=(
        "## Przypadek testowy\n"
        "| pole | przykład |\n|---|---|\n"
        "| ID | TC-05 |\n| Tytuł | Zamówienie z kodem pocztowym w złym formacie jest odrzucone |\n| Warunki wstępne | zalogowany jako tester, w koszyku 1 produkt |\n"
        "| Kroki | 1. Koszyk → Zamów. 2. Wypełnij formularz, kod pocztowy „00000”. 3. Kliknij Zamawiam. |\n| Dane | kod: 00000 |\n| Oczekiwany wynik | komunikat „Kod pocztowy w formacie NN-NNN”, zamówienie nie zostaje złożone |\n"
        "Zapisujesz go PRZED wykonaniem. Status po wykonaniu: zaliczony / niezaliczony / zablokowany.\n"
        "## Raport błędu (zgłoszenie defektu)\n"
        "1. **Tytuł**: gdzie + co nie działa + w jakich warunkach — „Koszyk: suma pomija produkty o ilości 10 i więcej”. Nie: „koszyk nie działa”.\n"
        "2. **Środowisko**: wersja aplikacji, system, przeglądarka i wersja, adres.\n"
        "3. **Warunki wstępne** i **kroki odtworzenia** — ponumerowane, z danymi. Ktoś obcy powtórzy je bez pytań.\n"
        "4. **Wynik oczekiwany** (wg wymagań) i **rzeczywisty** (co dokładnie widać, z wartościami).\n"
        "5. **Ważność** (severity — wpływ: krytyczna/wysoka/średnia/niska) i **priorytet** (pilność naprawy — ustala zespół).\n"
        "6. **Dowód**: zrzut ekranu, nagranie, fragment logu, traceback.\n"
        "7. Powtarzalność: „zawsze (5/5)” albo „sporadycznie (2/10)”.\n"
        "## Jeden błąd = jedno zgłoszenie\n"
        "Trzy problemy w jednym raporcie się gubią. Przed zgłoszeniem: odtwórz jeszcze raz, sprawdź, czy już nie zgłoszono, zawęź warunki (czy dotyczy tylko ilości ≥ 10?).\n"
        "## Ton\n"
        "Fakty, bez ocen („programista znowu zepsuł”). Raport czyta też klient i kierownik.\n"
        "## Testowanie eksploracyjne\n"
        "Gdy nie ma scenariuszy: sesja 30–60 minut z celem („formularz zamówienia: złe dane”), notatki na bieżąco, na końcu lista znalezisk i pomysłów na testy."),
    przyklad=("## BUG-03: Koszyk — suma nie uwzględnia ilości 10 i więcej sztuk\n"
              "**Środowisko:** Sklep testowy 1.0 (lokalnie, http://127.0.0.1:5001), Windows 11, Edge 142\n"
              "**Ważność:** wysoka (klient płaci złą kwotę) · **Powtarzalność:** zawsze (5/5)\n"
              "**Warunki wstępne:** zalogowany użytkownik tester, pusty koszyk\n"
              "**Kroki:**\n"
              "1. Produkty → „Zeszyt A5 w kratkę” (4,50 zł) → ilość 10 → Dodaj do koszyka.\n"
              "2. Otwórz Koszyk.\n"
              "**Oczekiwany wynik:** pozycja 10 × 4,50 zł = 45,00 zł, suma koszyka 45,00 zł.\n"
              "**Rzeczywisty wynik:** pozycja pokazuje 10 szt., ale suma koszyka to 4,50 zł.\n"
              "**Dodatkowo:** dla ilości 9 suma jest poprawna (40,50 zł) — problem zaczyna się od 10 (wartość brzegowa).\n"
              "**Dowód:** bug03_koszyk.png"),
    demonstracja={"tytul": "Od zauważonej awarii do raportu w 10 minut", "kroki": [
        "Zauważasz: suma koszyka dziwnie niska. Nie zgłaszasz od razu — najpierw odtwarzasz: pusty koszyk, jeden produkt, ilość 10 → suma 4,50 zł. Powtarzasz 5 razy — zawsze.",
        "Zawężasz: ilość 9 → poprawnie, 10 → źle, 25 → źle. Granica 10 — to informacja dla programisty, gdzie szukać.",
        "Tytuł: miejsce (Koszyk) + co (suma nie uwzględnia ilości) + warunek (10 i więcej).",
        "Środowisko z wersją przeglądarki (edge://version).",
        "Kroki ponumerowane, z nazwą produktu i ceną — każdy może je powtórzyć.",
        "Oczekiwany vs rzeczywisty — z konkretnymi kwotami.",
        "Ważność wysoka: złe pieniądze. Priorytet ustali zespół.",
        "Dowód: driver.save_screenshot albo Win+Shift+S; nazwa pliku z numerem zgłoszenia."],
        "wynik": "Raport BUG-03, który programista odtwarza za pierwszym razem, z granicą (10 sztuk) wskazującą miejsce defektu."},
    jak_uruchomic=["Sklep testowy: `python app.py` → http://127.0.0.1:5001 → login tester / Test123!.",
                   "Raporty zapisuj w bug_raporty.md (Markdown) w PRACA — tak jak w szablonie Mentora (zakładka Szablony)."],
    cwiczenia=[
        C("prowadzone",
          "Popraw tytuł raportu „logowanie nie działa” na wzór demonstracji. Fakty: przy loginie z wielką literą („Tester”) i poprawnym haśle pojawia się „Błędny login lub hasło”; z „tester” działa. Wybierz najlepszy tytuł i podaj wynik oczekiwany (wybierz). Czas: 10 minut.",
          "Tytuł: „Logowanie: login z wielką literą („Tester”) odrzucany mimo poprawnego hasła”; oczekiwany: zależy od wymagań — jeśli login ma być niewrażliwy na wielkość liter, użytkownik zostaje zalogowany.",
          ["Tytuł: gdzie + co + w jakich warunkach.", "Fakty z obserwacji, bez ocen.", "Oczekiwany wynik wynika z wymagań — jeśli ich nie ma, zapytaj."],
          "Najlepszy: „Logowanie: login z wielką literą odrzucany mimo poprawnego hasła”. Oczekiwany — według wymagań; jeśli login ma być niewrażliwy na wielkość liter: zalogowanie. Jeśli wymagania tego nie mówią — w raporcie dopisujesz pytanie do analityka.",
          [wy("t", "Tytuł", ["logowanie nie działa", "Logowanie: login z wielką literą odrzucany mimo poprawnego hasła", "BŁĄD!!! pilne", "tester nie może się zalogować czasami"], "Logowanie: login z wielką literą odrzucany mimo poprawnego hasła"),
           wy("o", "Oczekiwany wynik", ["komunikat błędu", "zalogowanie (jeśli login ma być niewrażliwy na wielkość liter)", "zamknięcie strony"], "zalogowanie (jeśli login ma być niewrażliwy na wielkość liter)")]),
        C("samodzielne",
          "Oceń ważność (krytyczna / wysoka / średnia / niska): (1) po kliknięciu „Zamawiam” serwer zwraca 500 dla każdego zamówienia; (2) literówka „Koszuk” w menu; (3) kod pocztowy „00000” jest akceptowany; (4) suma koszyka zła dla ilości ≥ 10. Dodatkowo (5): czy 3 znalezione problemy wpisujesz w jedno zgłoszenie (tak/nie)? Czas: 15 minut.",
          "(1) krytyczna; (2) niska; (3) średnia; (4) wysoka; (5) nie.",
          ["Czy da się w ogóle użyć systemu?", "Czy chodzi o pieniądze klienta?", "Kosmetyka nie blokuje pracy."],
          "(1) krytyczna — nikt nie złoży zamówienia; (2) niska — kosmetyka; (3) średnia — złe dane w zamówieniach, obejście możliwe; (4) wysoka — złe kwoty; (5) nie — jedno zgłoszenie na jeden defekt.",
          [wy("a", "(1) 500 przy każdym zamówieniu", ["krytyczna", "wysoka", "średnia", "niska"], "krytyczna"), wy("b", "(2) literówka w menu", ["krytyczna", "wysoka", "średnia", "niska"], "niska"),
           wy("c", "(3) kod 00000 akceptowany", ["krytyczna", "wysoka", "średnia", "niska"], "średnia"), wy("d", "(4) zła suma koszyka", ["krytyczna", "wysoka", "średnia", "niska"], "wysoka"),
           wy("e", "(5) Jedno zgłoszenie na 3 problemy?", ["tak", "nie"], "nie")]),
    ],
    typowe_bledy=[
        B("Zgłoszenie wraca z „Cannot reproduce”", "Brak danych, środowiska albo kroków wstępnych.", "Czy obca osoba wykona kroki bez pytań?", "Dopisz dane, wersje, warunki wstępne; nagraj ekran."),
        B("Spór o ważność", "Ocena wpływu z perspektywy „mnie to irytuje”.", "Jaki jest wpływ na użytkownika i biznes?", "Opisz skutki faktami (np. „klient płaci 4,50 zamiast 45 zł”)."),
    ],
    pulapki=["Raport z opinią zamiast faktów („ten formularz jest beznadziejny”).", "Zrzut ekranu bez zaznaczenia miejsca problemu — zaznacz ramką."],
    zadania=["10 przypadków testowych sklepu testowego w tabeli Markdown.", "3 raporty błędów z defektów znalezionych w sklepie testowym.", "Sesja eksploracyjna 30 minut z notatkami."],
    pytania=[["Co musi mieć raport błędu?", "Tytuł, środowisko, kroki, oczekiwany i rzeczywisty wynik, ważność, dowód."], ["Ważność a priorytet?", "Ważność = wpływ; priorytet = pilność naprawy (ustala zespół)."], ["Dlaczego jeden błąd = jedno zgłoszenie?", "Każdy defekt ma własny cykl naprawy i weryfikacji."]],
    podsumowanie="Zapisujesz przypadki testowe z oczekiwanym wynikiem i raporty błędów, które da się odtworzyć bez pytań, z rzetelną oceną ważności i dowodem.",
    test=[T("Najlepszy tytuł zgłoszenia:", ["Nie działa", "Koszyk: suma pomija produkty o ilości ≥ 10", "BUG!!!", "Problem z aplikacją"], 1, "Gdzie + co + warunek."),
          T("Ważność (severity) opisuje:", ["kolejność naprawy", "wpływ defektu", "kto zgłosił", "datę"], 1, "Priorytet to pilność."),
          T("Przypadek testowy bez oczekiwanego wyniku:", ["jest kompletny", "nie pozwala ocenić, czy test przeszedł", "jest szybszy", "jest negatywny"], 1, "Brak kryterium."),
          T("Przed zgłoszeniem błędu najpierw:", ["zgłaszasz, ile się da", "odtwarzasz i zawężasz warunki", "naprawiasz sam kod", "czekasz tydzień"], 1, "Powtarzalność i granice.")],
    w_praktyce=["Szablon zgłoszenia w zespole (Jira/GitHub Issues) — wypełniaj wszystkie pola.", "Po naprawie: retest kroków z raportu + test regresji automatyczny."],
    zrodla=[Z.SJSI_CTFL_PL, Z.ISTQB_SLOWNIK, Z.ISTQB_CTFL],
)

CI = L(
    id="ci", nazwa="GitHub Actions i pytest-html: testy uruchamiane przy każdym pushu", tydzien=9,
    slowa=["CI", "ciągła integracja", "GitHub Actions", "workflow", "YAML", "tests.yml", "runs-on", "steps", "actions/checkout", "actions/setup-python",
           "pytest-html", "artefakt", "upload-artifact", "odznaka", "badge", "headless"],
    cel="Po tej lekcji tworzysz workflow GitHub Actions (.github/workflows/tests.yml), który przy każdym pushu instaluje zależności i uruchamia pytest, dodajesz raport HTML (pytest-html) jako artefakt i odznakę statusu w README.",
    po_co="Zielony znaczek CI przy projekcie mówi rekruterowi: testy naprawdę działają, a nie tylko „u mnie”. W firmach żaden pull request nie jest scalany bez zielonego CI.",
    wymagania=["Repozytorium na GitHubie z testami pytest i requirements.txt.", "Lekcje „venv” i „pytest”.", "GitHub Actions jest darmowe dla repozytoriów publicznych."],
    wyjasnienie=(
        "## Ciągła integracja (CI)\n"
        "Po każdym pushu serwer pobiera kod, instaluje środowisko od zera i uruchamia testy. Wynik widać przy commicie i w pull requeście (✔ albo ✘). To automatyczny test regresji.\n"
        "## Workflow = plik YAML\n"
        "Plik `.github/workflows/tests.yml` w repozytorium. YAML: wcięcia **spacjami** (nie Tab), `klucz: wartość`, listy z `-`.\n"
        "```\nname: Testy\non: [push, pull_request]\njobs:\n  testy:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v6\n      - uses: actions/setup-python@v5\n        with:\n          python-version: \"3.12\"\n      - run: python -m pip install -r requirements.txt\n      - run: python -m pytest -v\n```\n"
        "`on` — kiedy uruchomić; `runs-on` — system maszyny; `uses` — gotowa akcja (checkout pobiera kod, setup-python instaluje Pythona); `run` — polecenie. Wersje akcji podane jak w dokumentacji GitHub.\n"
        "## Raport HTML: pytest-html\n"
        "Dopisz `pytest-html` do requirements.txt i zmień polecenie: `python -m pytest -v --html=raport.html --self-contained-html`. Raport zapisz jako **artefakt** (do pobrania z zakładki Actions):\n"
        "```\n      - uses: actions/upload-artifact@v4\n        if: always()\n        with:\n          name: raport-testow\n          path: raport.html\n```\n"
        "`if: always()` — raport trafia na GitHub także wtedy, gdy testy padły (wtedy jest najbardziej potrzebny).\n"
        "## Selenium w CI\n"
        "Maszyny ubuntu-latest mają przeglądarkę Chrome; w CI uruchamiasz ją bez okna (`--headless=new`). Sklep testowy/aplikację startujesz w kroku przed testami (np. `python app.py &` i chwila na start) albo w fixturze.\n"
        "## Odznaka w README\n"
        "`![Testy](https://github.com/TWOJA-NAZWA/REPO/actions/workflows/tests.yml/badge.svg)` — zielona/czerwona plakietka na górze README.\n"
        "## Czytanie wyniku\n"
        "Actions → przebieg → zadanie „testy” → rozwiń krok z ✘ — zobaczysz ten sam wynik pytest co lokalnie."),
    przyklad=("# .github/workflows/tests.yml\n"
              "name: Testy\n"
              "on: [push, pull_request]\n"
              "jobs:\n"
              "  testy:\n"
              "    runs-on: ubuntu-latest\n"
              "    steps:\n"
              "      - uses: actions/checkout@v6\n"
              "      - uses: actions/setup-python@v5\n"
              "        with:\n"
              "          python-version: \"3.12\"\n"
              "      - name: Zależności\n"
              "        run: python -m pip install -r requirements.txt\n"
              "      - name: Testy z raportem\n"
              "        run: python -m pytest -v --html=raport.html --self-contained-html\n"
              "      - name: Raport jako artefakt\n"
              "        if: always()\n"
              "        uses: actions/upload-artifact@v4\n"
              "        with:\n"
              "          name: raport-testow\n"
              "          path: raport.html"),
    demonstracja={"tytul": "Pierwszy zielony pipeline", "kroki": [
        "Utwórz katalogi `.github\\workflows` w repozytorium (kropka na początku nazwy!) i plik tests.yml z ramki.",
        "`name` — nazwa widoczna w zakładce Actions; `on: [push, pull_request]` — przy każdym pushu i PR.",
        "`runs-on: ubuntu-latest` — darmowa maszyna z Linuksem; Twój kod Pythona działa tam tak samo.",
        "`actions/checkout@v6` — pobiera Twoje repozytorium; `actions/setup-python@v5` z `python-version` — instaluje Pythona.",
        "`pip install -r requirements.txt` — dlatego requirements.txt musi zawierać wszystko (pytest, pytest-html…).",
        "`pytest … --html=raport.html --self-contained-html` — jeden plik HTML z wynikami.",
        "`upload-artifact` z `if: always()` — raport do pobrania nawet przy czerwonym wyniku.",
        "commit + push → GitHub → Actions: żółta kropka (trwa) → zielony ✔ po ok. minucie. Zepsuj test, push → czerwony ✘ i e-mail o nieudanym przebiegu."],
        "wynik": "Zakładka Actions z zielonym przebiegiem i artefaktem raport-testow; odznaka „Testy passing” w README."},
    jak_uruchomic=["W repozytorium: `mkdir .github\\workflows` → plik tests.yml → `git add .github` → commit → push.",
                   "GitHub → zakładka Actions → przebieg → Summary → Artifacts → raport-testow."],
    cwiczenia=[
        C("prowadzone",
          "Na wzór demonstracji uzupełnij brakujące elementy workflow: (1) nazwa akcji pobierającej kod (z wersją jak w lekcji), (2) klucz określający system maszyny, (3) warunek, żeby raport trafił na GitHub także przy czerwonych testach. Czas: 10 minut.",
          "(1) actions/checkout@v6; (2) runs-on; (3) if: always().",
          ["Akcja „checkout”.", "Na czym „biegnie” zadanie.", "Krok, który ma się wykonać zawsze."],
          "(1) `actions/checkout@v6`; (2) `runs-on: ubuntu-latest`; (3) `if: always()`.",
          [tx("a", "(1) Akcja", "actions/checkout@v6"), tx("b", "(2) Klucz", "runs-on"), tx("c", "(3) Warunek", "if: always()", zawiera=["always"])]),
        C("samodzielne",
          "CI jest czerwone, lokalnie wszystko zielone. Log: `ModuleNotFoundError: No module named 'requests'`. (1) Najbardziej prawdopodobna przyczyna (wybierz)? (2) Co robisz (wybierz)? (3) Gdyby log mówił `yaml: line 9: found character that cannot start any token` — co jest źle (wybierz)? Czas: 15 minut.",
          "(1) requests nie ma w requirements.txt; (2) dopisz requests do requirements.txt i push; (3) Tab zamiast spacji (albo zła składnia) w YAML.",
          ["CI instaluje TYLKO to, co jest w requirements.txt.", "Lokalnie pakiet masz „od dawna”.", "YAML nie akceptuje tabulatorów we wcięciach."],
          "(1) brak requests w requirements.txt — lokalnie był zainstalowany ręcznie; (2) dopisz (albo `pip freeze` w .venv projektu) i push; (3) znak Tab we wcięciu linii 9 — YAML wymaga spacji.",
          [wy("a", "(1) Przyczyna", ["GitHub nie obsługuje Pythona", "requests nie ma w requirements.txt", "za wolny internet", "zły login"], "requests nie ma w requirements.txt"),
           wy("b", "(2) Co robisz", ["usuwasz CI", "dopisujesz requests do requirements.txt i push", "wyłączasz testy"], "dopisujesz requests do requirements.txt i push"),
           wy("c", "(3) Błąd YAML", ["Tab zamiast spacji we wcięciu", "za długi plik", "brak internetu"], "Tab zamiast spacji we wcięciu")]),
    ],
    typowe_bledy=[
        B("Zakładka Actions pusta po pushu", "Plik w złym miejscu (np. github/workflows bez kropki) albo rozszerzenie .yml.txt.", "Ścieżka na GitHubie: .github/workflows/tests.yml.", "Przenieś plik do .github/workflows/ z rozszerzeniem .yml."),
        B("ERROR: file or directory not found: tests/", "Polecenie pytest wskazuje katalog, którego nie ma w repozytorium.", "Struktura repo na GitHubie.", "Popraw ścieżkę albo uruchamiaj samo `python -m pytest`."),
        B("Selenium w CI: SessionNotCreatedException / brak ekranu", "Przeglądarka bez trybu headless na serwerze bez ekranu.", "Opcje przeglądarki w fixturze.", "`--headless=new`; w CI Chrome (`webdriver.Chrome(options=...)`)."),
    ],
    pulapki=["Sekrety (hasła, klucze) w pliku workflow — tylko w Settings → Secrets and variables → Actions.", "Wersje akcji „@main” zamiast konkretnej — zmiana po stronie autora może zepsuć Twój pipeline."],
    zadania=["tests.yml uruchamiający pytest przy pushu — zielony znaczek.", "pytest-html i raport jako artefakt.", "Odznaka CI w README repozytorium testów."],
    pytania=[["Co robi CI?", "Przy każdej zmianie instaluje środowisko od zera i uruchamia testy."], ["Dlaczego if: always() przy raporcie?", "Żeby raport był dostępny także przy czerwonych testach."], ["Gdzie trzymasz sekrety dla Actions?", "W Settings → Secrets and variables → Actions, nie w pliku."]],
    podsumowanie="Tworzysz workflow GitHub Actions z pytest, raportem HTML jako artefaktem i odznaką w README; czytasz logi i naprawiasz typowe przyczyny czerwonego CI.",
    test=[T("Plik workflow umieszczasz w:", [".github/workflows/", "workflows/", "github/", ".git/workflows/"], 0, "Z kropką na początku."),
          T("CI czerwone, lokalnie zielone — częsta przyczyna:", ["zbyt szybki komputer", "brak pakietu w requirements.txt", "kolor motywu", "nazwa gałęzi"], 1, "CI instaluje od zera."),
          T("Wcięcia w YAML:", ["Tab", "spacje", "dowolne", "nawiasy"], 1, "Tab = błąd składni."),
          T("Raport pytest-html tworzy opcja:", ["--report", "--html=raport.html", "-v", "--junit"], 1, "Plugin pytest-html.")],
    w_praktyce=["Każdy PR: zielone CI przed recenzją.", "Czerwone CI na main = wszyscy przerywają i naprawiają (zasada zespołu)."],
    zrodla=[Z.GH_ACTIONS_PY, Z.GH_README, Z.PYTEST_START],
)

POWTORKA3 = L(
    id="powtorka_testy", nazwa="Powtórka etapu 3: strategia testów małego projektu", tydzien=9,
    slowa=["powtórka", "etap 3", "strategia testów", "plan testów", "pokrycie", "ryzyko", "automatyzacja", "manualne", "regresja", "piramida"],
    cel="Po tej lekcji układasz strategię testów małego systemu: co testujesz jednostkowo, co integracyjnie, co E2E, a co ręcznie; dobierasz techniki do ryzyka i łączysz to w jeden przebieg CI.",
    po_co="„Jak przetestowałbyś ten formularz / ten sklep?” — to najczęstsze pytanie otwarte na rozmowie Junior QA. Odpowiedź ma strukturę, a nie listę kliknięć.",
    wymagania=["Lekcje tygodni 7–9."],
    wyjasnienie=(
        "## Strategia w 5 pytaniach\n"
        "1. **Co jest najważniejsze / najbardziej ryzykowne?** (pieniądze, logowanie, dane osobowe) — tam najwięcej testów.\n"
        "2. **Gdzie jest logika?** — reguły (rabat, dostawa, walidacja) testujesz jednostkowo, parametrize z klasami i granicami.\n"
        "3. **Gdzie części się łączą?** — zapis do bazy/pliku, API → test integracyjny z danymi tymczasowymi.\n"
        "4. **Jakie ścieżki użytkownika są krytyczne?** — 3–5 testów E2E w POM (logowanie, zamówienie, błędne hasło).\n"
        "5. **Czego nie warto automatyzować?** — wygląd, jednorazowe sprawdzenia, eksploracja → testy ręczne.\n"
        "## Mapa etapu 3\n"
        "| umiejętność | dowód |\n|---|---|\n"
        "| techniki projektowania | tabela klas i granic dla reguły |\n| pytest | testy z raises/approx, mutant wykryty |\n| parametrize/fixtures | jeden test → wiele przypadków; dane w fixturze |\n"
        "| Selenium + POM | testy E2E bez sleep, klasy stron |\n| przypadki i raporty | tabela TC, raport odtwarzalny bez pytań |\n| CI | zielony pipeline z raportem HTML |\n"
        "## Przykład: sklep testowy\n"
        "Jednostkowe: koszt dostawy, rabat, walidacja kodu pocztowego (20 przypadków parametrize). Integracyjne: API /api/produkty (status, pola, filtr). E2E: logowanie OK/błąd, dodanie do koszyka i suma, zamówienie. Ręczne: wygląd na telefonie, czytelność komunikatów. CI: jednostkowe przy każdym pushu, E2E przy PR do main."),
    przyklad=kod("powtorka_testy", (
        "STRATEGIA = {\n"
        "    \"jednostkowe\": [\"koszt_dostawy\", \"rabat\", \"kod_pocztowy\"],\n"
        "    \"integracyjne\": [\"GET /api/produkty\", \"zapis zamówienia\"],\n"
        "    \"e2e\": [\"logowanie poprawne\", \"błędne hasło\", \"koszyk i suma\", \"zamówienie\"],\n"
        "    \"reczne\": [\"wygląd na telefonie\", \"czytelność komunikatów\"],\n"
        "}\n"
        "PRZYPADKI_KOD = [\"00-950\", \"00950\", \"0-950\", \"00-95\", \"ab-cde\", \"\", \" 00-950 \"]\n"
        "for poziom, testy in STRATEGIA.items():\n"
        "    print(f\"{poziom:<13}{len(testy):>2}  {', '.join(testy)}\")\n"
        "razem = sum(len(t) for t in STRATEGIA.values())\n"
        "print(\"Automatyczne:\", razem - len(STRATEGIA[\"reczne\"]), \"z\", razem)\n"
        "print(\"Przypadki kodu pocztowego:\", len(PRZYPADKI_KOD))\n"), (
        "jednostkowe   3  koszt_dostawy, rabat, kod_pocztowy\nintegracyjne  2  GET /api/produkty, zapis zamówienia\n"
        "e2e           4  logowanie poprawne, błędne hasło, koszyk i suma, zamówienie\nreczne        2  wygląd na telefonie, czytelność komunikatów\nAutomatyczne: 9 z 11\nPrzypadki kodu pocztowego: 7\n")),
    demonstracja={"tytul": "Strategia testów sklepu jako struktura danych", "kroki": [
        "Słownik poziom → lista obszarów: od razu widać proporcje piramidy.",
        "Jednostkowe: reguły z wymagań — każda rozpisana dalej na przypadki parametrize.",
        "Integracyjne: miejsca styku (API, zapis).",
        "E2E: tylko krytyczne ścieżki — 4, nie 40.",
        "Ręczne: to, czego automatyzacja nie oceni dobrze.",
        "Przypadki dla kodu pocztowego (format NN-NNN): poprawny, bez myślnika, za krótki człon, za krótki całość, litery, pusty, ze spacjami — klasy równoważności i granice formatu.",
        "Zapis strategii w kodzie/tabeli łatwo pokazać na rozmowie i w PLAN_TESTOW.md (tydzień 12)."],
        "wynik": "Tabelka 4 poziomów, „Automatyczne: 9 z 11” i „Przypadki kodu pocztowego: 7”."},
    jak_uruchomic=["Zapisz jako strategia.py → ▶ Uruchom.", "Przepisz strategię dla własnego projektu Magazyn (tydzień 10) do PLAN.md."],
    cwiczenia=[
        C("prowadzone",
          "Przypisz poziom testu (jednostkowe / integracyjne / E2E / ręczne): (1) funkcja kod_pocztowy_poprawny(\"00-950\"); (2) zapis zamówienia do bazy SQLite i odczyt; (3) klient loguje się i składa zamówienie w przeglądarce; (4) czy przyciski są czytelne na telefonie. Czas: 10 minut.",
          "(1) jednostkowe; (2) integracyjne; (3) E2E; (4) ręczne.",
          ["Jedna funkcja w izolacji.", "Dwie części razem (kod + baza).", "Cały system oczami użytkownika."],
          "(1) jednostkowe; (2) integracyjne; (3) E2E; (4) ręczne (ocena wyglądu).",
          [wy("a", "(1) funkcja kodu", ["jednostkowe", "integracyjne", "E2E", "ręczne"], "jednostkowe"), wy("b", "(2) zapis do bazy", ["jednostkowe", "integracyjne", "E2E", "ręczne"], "integracyjne"),
           wy("c", "(3) zamówienie w przeglądarce", ["jednostkowe", "integracyjne", "E2E", "ręczne"], "E2E"), wy("d", "(4) czytelność na telefonie", ["jednostkowe", "integracyjne", "E2E", "ręczne"], "ręczne")]),
        C("samodzielne",
          "Zespół ma 200 testów E2E (2 godziny w CI) i 10 jednostkowych; testy często padają losowo. (1) Jak nazywa się ten antywzorzec (wybierz)? (2) Co zmieniasz najpierw (wybierz)? (3) Ile minimum przypadków dla walidacji „ilość 1–50, liczba całkowita” według klas i granic (dwupunktowo + nie-liczba)? Czas: 15 minut.",
          "(1) odwrócona piramida (rożek lodów); (2) przenieś sprawdzanie reguł do testów jednostkowych; (3) 5 (0, 1, 50, 51, nie-liczba).",
          ["Proporcje odwrotne niż w piramidzie.", "Reguły biznesowe nie potrzebują przeglądarki.", "Granice 1 i 50 z sąsiadami + jedna klasa „nie-liczba”."],
          "(1) odwrócona piramida (tzw. rożek lodów); (2) reguły → testy jednostkowe, E2E tylko krytyczne ścieżki; (3) 0, 1, 50, 51 i np. \"abc\" → 5.",
          [wy("a", "(1) Antywzorzec", ["piramida testów", "odwrócona piramida (rożek lodów)", "TDD", "regresja"], "odwrócona piramida (rożek lodów)"),
           wy("b", "(2) Najpierw", ["dodać kolejne 100 E2E", "przenieść sprawdzanie reguł do testów jednostkowych", "wyłączyć CI"], "przenieść sprawdzanie reguł do testów jednostkowych"), li("c", "(3) Minimum przypadków", 5)]),
    ],
    typowe_bledy=[
        B("Odpowiedź na rozmowie: lista 30 kliknięć bez struktury.", "Brak strategii.", "Czy mówisz o ryzyku, poziomach i technikach?", "5 pytań strategii: ryzyko → logika → integracja → ścieżki krytyczne → ręczne."),
        B("Wszystko automatyzowane E2E.", "„Bo to wygląda najlepiej”.", "Ile trwa CI, ile testów jest flaky?", "Piramida: reguły jednostkowo, E2E tylko krytyczne."),
    ],
    pulapki=["Pokrycie kodu 100% ≠ brak defektów — testy mogą nie mieć sensownych asercji.", "Brak testów ręcznych „bo mamy automaty” — eksploracja znajduje to, czego nie przewidział nikt."],
    zadania=["Strategia testów sklepu testowego w 5 punktach.", "Repozytorium testów sklepu: POM, 15+ testów, raport HTML, odznaka CI.", "Powtórz lekcje z czerwonymi quizami etapu 3."],
    pytania=[["Jak przetestowałbyś formularz zamówienia?", "Ryzyko → reguły jednostkowo (klasy/granice) → integracja API/zapis → E2E ścieżki krytyczne → ręcznie wygląd i komunikaty."],
             ["Co to odwrócona piramida?", "Dużo E2E, mało jednostkowych — wolne, kruche testy."], ["Czego nie automatyzujesz?", "Wyglądu, jednorazowych sprawdzeń, eksploracji."]],
    podsumowanie="Układasz strategię testów: ryzyko, poziomy, techniki, proporcje piramidy i podział na automatyczne i ręczne — w formie, którą pokażesz na rozmowie.",
    test=[T("Najwięcej testów automatycznych powinno być:", ["E2E", "jednostkowych", "ręcznych", "wydajnościowych"], 1, "Piramida."),
          T("Ryzyko w strategii testów to:", ["koszt licencji", "prawdopodobieństwo i skutek problemu", "liczba testerów", "kolor UI"], 1, "Tam więcej testów."),
          T("Wygląd na telefonie testujesz najlepiej:", ["pytest", "ręcznie (eksploracyjnie)", "SQL", "nie testujesz"], 1, "Ocena człowieka."),
          T("Testy E2E w strategii obejmują:", ["każdą regułę", "krytyczne ścieżki użytkownika", "tylko logowanie", "nic"], 1, "Mało, ale ważne.")],
    w_praktyce=["Plan testów projektu zaczyna się od listy ryzyk.", "Na rozmowie: narysuj piramidę i wstaw w nią testy swojego projektu."],
    zrodla=[Z.ISTQB_CTFL, Z.SJSI_CTFL_PL, Z.SEL_POM],
)
