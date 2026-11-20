# -*- coding: utf-8 -*-
"""Etap 2, tygodnie 10–11: dane CSV/JSON, aplikacja Flask, baza SQLite; API i klucze, automatyzacje, powtórka."""

from wspolne import (TN, B, C, L, T, bl, kod, kw, li, tx, wy)
from etap2 import D, Z_CC_BEST

Z_CSV = ["Python — moduł csv (DictReader, delimiter) — oficjalna dokumentacja", "https://docs.python.org/3/library/csv.html", D]
Z_JSON = ["Python — moduł json (dump, load, ensure_ascii)", "https://docs.python.org/3/library/json.html", D]
Z_PATH = ["Python — pathlib (ścieżki niezależne od systemu)", "https://docs.python.org/3/library/pathlib.html", D]
Z_FLASK_QS = ["Flask — Quickstart (trasy, request.args, jsonify, tryb debug)", "https://flask.palletsprojects.com/en/stable/quickstart/", D]
Z_FLASK_FACT = ["Flask — Application Factories (create_app)", "https://flask.palletsprojects.com/en/stable/patterns/appfactories/", D]
Z_FLASK_TEST = ["Flask — Testing Flask Applications (test_client)", "https://flask.palletsprojects.com/en/stable/testing/", D]
Z_FLASK_DEPLOY = ["Flask — Deploying to Production (serwer deweloperski nie do produkcji)", "https://flask.palletsprojects.com/en/stable/deploying/", D]
Z_SQLITE = ["Python — sqlite3 (placeholders ?, ostrzeżenie o SQL injection)", "https://docs.python.org/3/library/sqlite3.html", D]
Z_OWASP_SQLI = ["OWASP — SQL Injection Prevention Cheat Sheet", "https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html", D]
Z_REQUESTS = ["Requests — Quickstart (params, timeout, raise_for_status)", "https://requests.readthedocs.io/en/latest/user/quickstart/", D]
Z_OS_ENV = ["Python — os.environ (zmienne środowiskowe)", "https://docs.python.org/3/library/os.html#os.environ", D]
Z_SETX = ["Microsoft Learn — setx (trwałe zmienne środowiskowe w Windows)", "https://learn.microsoft.com/windows-server/administration/windows-commands/setx", D]
Z_OWASP_SECRETS = ["OWASP — Secrets Management Cheat Sheet", "https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html", D]
Z_SCHTASKS = ["Microsoft Learn — schtasks create (Harmonogram zadań z wiersza poleceń)", "https://learn.microsoft.com/windows-server/administration/windows-commands/schtasks-create", D]
Z_SHUTIL = ["Python — shutil.move i operacje na plikach", "https://docs.python.org/3/library/shutil.html", D]


# =========================================================================== TYDZIEŃ 10
DANE = L(
    id="dane_csv_json", nazwa="Dane: CSV z arkusza i JSON — wczytaj, policz, zapisz", tydzien=10,
    slowa=["CSV", "JSON", "DictReader", "średnik", "przecinek dziesiętny", "kodowanie", "utf-8-sig", "raport"],
    cel="Po tej lekcji wczytujesz polski plik CSV z arkusza (średnik, przecinek dziesiętny, polskie znaki), liczysz z niego raport (sumy miesięczne, najczęstsza wartość) i zapisujesz wynik do JSON.",
    po_co="Klienci trzymają dane w arkuszach. „Zrób mi raport z tego pliku” to najczęstsze małe zlecenie — i najczęstsze źródło cichych błędów AI (zły separator, zła liczba).",
    wymagania=["Lekcje „Czytanie kodu 2” i „Debugowanie”.", "Plik dane/rezerwacje.csv z materiałów kursu."],
    wyjasnienie=(
        "## CSV po polsku\n"
        "CSV to tabela w pliku tekstowym: jedna linia = jeden wiersz. Polski Excel zapisuje CSV ze ŚREDNIKIEM jako separatorem (bo przecinek jest dziesiętny) i często z niewidocznym znacznikiem BOM na początku (kodowanie „UTF-8 z BOM”).\n"
        "```\ndata_przyjazdu;pokoj;noce;osoby;kwota\n2026-07-03;Lipowy;3;2;1080,00\n2026-07-10;Dębowy;7;4;3528,00\n```\n"
        "## Wczytanie bez pułapek\n"
        "```\nimport csv\nwith open(sciezka, encoding=\"utf-8-sig\", newline=\"\") as f:\n    wiersze = list(csv.DictReader(f, delimiter=\";\"))\n```\n"
        "- `utf-8-sig` usuwa BOM — bez tego pierwsza kolumna nazywa się „\\ufeffdata_przyjazdu” i KeyError murowany.\n"
        "- `delimiter=\";\"` — bez tego cały wiersz to jedna kolumna.\n"
        "- DictReader daje słowniki z NAPISAMI: `\"1080,00\"`. Liczby zamieniasz: `float(w[\"kwota\"].replace(\",\", \".\"))`, `int(w[\"noce\"])`.\n"
        "## Raport: grupowanie\n"
        "Suma na miesiąc: klucz to pierwsze 7 znaków daty (`\"2026-07\"`), słownik sum: `sumy[m] = sumy.get(m, 0) + kwota`. Najczęstsza wartość: `collections.Counter(pokoje).most_common(1)` — ale przy remisie zdecyduj regułę (np. alfabetycznie) i zapisz ją w specyfikacji.\n"
        "## JSON — format wymiany\n"
        "JSON wygląda jak słowniki i listy Pythona. `json.dump(dane, f, ensure_ascii=False, indent=2)` zapisuje czytelnie z polskimi znakami (bez ensure_ascii=False „Dębowy” zapisze się jako „D\\u0119bowy”). `json.load(f)` wczytuje.\n"
        "## Sprawdzenie raportu od agenta\n"
        "- Policz ręcznie jedną liczbę (np. lipiec) z 3–4 wierszy — zgadza się?\n"
        "- Sprawdź liczbę wczytanych wierszy (`len`) z liczbą wierszy w pliku minus nagłówek.\n"
        "- Sprawdź wiersz z polskimi znakami i największą kwotą.\n"
        "- Pusty wiersz na końcu pliku nie może wywracać programu.\n"
        "## Dane osobowe w plikach\n"
        "Plik klienta z imionami, telefonami i e-mailami to dane osobowe (RODO). Do agenta i czatu wysyłasz plik z danymi zastąpionymi przykładowymi albo tylko nagłówek i 3 zmyślone wiersze (tydzień 12)."),
    przyklad=kod("dane_csv_json:przyklad",
                 "import csv\nimport io\n\nplik = io.StringIO(\"\\ufeffdata_przyjazdu;pokoj;noce;kwota\\n2026-07-03;Lipowy;3;1080,00\\n2026-07-10;Dębowy;7;3528,00\\n2026-08-01;Lipowy;2;720,00\\n\")\n"
                 "wiersze = list(csv.DictReader(plik, delimiter=\";\"))\nprint(repr(list(wiersze[0].keys())[0]))     # niewidoczny BOM z Excela\n"
                 "wiersze = [{k.lstrip(\"\\ufeff\"): v for k, v in w.items()} for w in wiersze]   # przy open() zrobi to encoding=\"utf-8-sig\"\n"
                 "sumy = {}\nfor w in wiersze:\n    m = w[\"data_przyjazdu\"][:7]\n    sumy[m] = sumy.get(m, 0) + float(w[\"kwota\"].replace(\",\", \".\"))\nprint(sumy)\n",
                 "'\\ufeffdata_przyjazdu'\n{'2026-07': 4608.0, '2026-08': 720.0}\n"),
    demonstracja={"tytul": "Raport, który „działał”, ale liczył źle", "kroki": [
        "Prośba do agenta: „raport przychodu miesięcznego z dane/rezerwacje.csv”. Wynik uruchomienia: KeyError: 'data_przyjazdu'.",
        "print(wiersze[0].keys()) pokazuje '\\ufeffdata_przyjazdu' — BOM z Excela. Poprawka: encoding=\"utf-8-sig\".",
        "Drugie uruchomienie: lipiec = 4608.0 — sprawdzasz ręcznie dwa wiersze lipca: 1080 + 3528 = 4608 ✔. Ale łączna liczba wierszy: 40 zamiast 41 — agent pomija wiersze, w których kwota ma spację tysięcy („1 080,00”) przez `except ValueError: continue`.",
        "To cichy błąd (pulapka z tygodnia 2): poprawka parsowania (usuń spacje) i usunięcie „except: continue” — zamiast pomijać, raport ma zgłaszać zły wiersz z numerem.",
        "Zapis do raport.json z ensure_ascii=False — „Dębowy” czytelny."],
        "wynik": "Raport liczy wszystkie wiersze, poprawnie czyta polski CSV i głośno zgłasza złe wiersze zamiast je pomijać."},
    jak_uruchomic=["Skopiuj dane/rezerwacje.csv z materiałów do PRACA\\dane.", "Zadanie tygodnia → raport.py → „✔ Sprawdź wynik”."],
    cwiczenia=[
        C("prowadzone",
          "Przeczytaj przykład lekcji (dane jak z Excela: BOM, średnik, przecinek dziesiętny). (1) Jaki niewidoczny znak pokazuje pierwsza linia wyniku przed nazwą kolumny — wpisz jego zapis z repr (zaczyna się od \\u)? "
          "(2) Suma dla „2026-07”. (3) Liczba miesięcy w słowniku. Czas: 20 minut.",
          "(1) \\ufeff (BOM); (2) 4608,00; (3) 2.",
          ["repr pokazuje ukryte znaki w zapisie \\u….", "Lipiec: 1080 + 3528.", "Klucze słownika sum: lipiec i sierpień."],
          "Pierwsza kolumna ma na początku BOM \\ufeff — w prawdziwym pliku usuwa go encoding=\"utf-8-sig\". Lipiec 4608,00 zł, 2 miesiące.",
          [tx("bom", "(1) Niewidoczny znak", ["\\ufeff", "ufeff"]), kw("lipiec", "(2) Suma lipca", 4608), li("mies", "(3) Liczba miesięcy", 2)]),
        C("samodzielne",
          "Dopasuj objaw do przyczyny: (1) KeyError: 'data_przyjazdu' mimo że kolumna jest w pliku, (2) każdy wiersz ma jedną kolumnę z całym tekstem, (3) ValueError: could not convert string to float: '1080,00', (4) w JSON widać „D\\u0119bowy”. "
          "Przyczyny: BOM (utf-8-sig) / brak delimiter=\";\" / przecinek dziesiętny / brak ensure_ascii=False. Czas: 15 minut.",
          "(1) BOM; (2) brak delimiter; (3) przecinek dziesiętny; (4) brak ensure_ascii=False.",
          ["Niewidoczny znak na początku pliku.", "Domyślny separator csv to przecinek.", "float() rozumie tylko kropkę."],
          "(1) BOM → utf-8-sig, (2) delimiter=\";\", (3) replace(\",\", \".\"), (4) ensure_ascii=False.",
          [wy(f"o{i}", t, ["BOM (utf-8-sig)", "brak delimiter", "przecinek dziesiętny", "brak ensure_ascii=False"], w) for i, t, w in
           ((1, "(1) KeyError mimo kolumny", "BOM (utf-8-sig)"), (2, "(2) Jedna kolumna", "brak delimiter"), (3, "(3) float('1080,00')", "przecinek dziesiętny"), (4, "(4) \\u0119 w JSON", "brak ensure_ascii=False"))]),
    ],
    typowe_bledy=[
        B("„UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb9”.", "Plik zapisany w Windows-1250 (stary Excel „CSV (rozdzielany przecinkami)”).", "Otwórz w Notatniku → Zapisz jako → kodowanie.", "Zapisz plik jako „CSV UTF-8” w Excelu albo wczytaj encoding=\"cp1250\" (i zapisz to w specyfikacji)."),
        B("Raport ma mniej wierszy niż plik.", "Ciche pomijanie (except: continue) albo puste wiersze.", "len(wiersze) vs liczba linii.", "Zgłaszaj zły wiersz z numerem zamiast pomijać; puste wiersze pomijaj jawnie (if not any(w.values()))."),
        B("Kwoty 10 razy za duże/małe.", "Kropka jako separator tysięcy („1.080,00”).", "Przykładowa kwota przed i po konwersji.", "Usuń kropki i spacje tysięcy, potem przecinek → kropka."),
    ],
    pulapki=["Agent często zakłada amerykański CSV (przecinek, kropka). Zawsze pokaż mu nagłówek i 2–3 prawdziwe (zanonimizowane) wiersze.", "Nie wysyłaj do AI całego pliku klienta z danymi osobowymi."],
    zadania=["Zbuduj raport.py dla dane/rezerwacje.csv (zadanie tygodnia).", "Policz ręcznie jeden miesiąc i porównaj.", "Zapisz raport.json z ensure_ascii=False."],
    pytania=[["Dlaczego encoding=\"utf-8-sig\"?", "Usuwa BOM z plików z Excela — inaczej nazwa pierwszej kolumny ma niewidoczny znak."],
             ["Jak zamienić „1 080,00” na liczbę?", "Usunąć spacje (także twarde), przecinek zamienić na kropkę, float()."], ["Po co ensure_ascii=False?", "Żeby polskie znaki w JSON były czytelne."]],
    podsumowanie="Wczytujesz polski CSV (średnik, BOM, przecinek), liczysz raport z grupowaniem, zapisujesz JSON i sprawdzasz wyniki ręcznym rachunkiem.",
    test=[T("Separator w CSV z polskiego Excela to zwykle:", ["przecinek", "średnik", "tabulator", "spacja"], 1, "Przecinek jest dziesiętny."),
          T("KeyError dla pierwszej kolumny mimo poprawnej nazwy — przyczyna:", ["BOM — użyj utf-8-sig", "Za duży plik", "Brak internetu", "Zła wersja Pythona"], 0, "Niewidoczny znak."),
          T("Raport pomija błędne wiersze przez except: continue. To:", ["Dobra praktyka", "Cichy błąd — zgłaszaj wiersz z numerem", "Wymóg RODO", "Szybsze"], 1, "Ciche złe dane."),
          T("Polskie znaki w JSON czytelne dzięki:", ["indent=2", "ensure_ascii=False", "sort_keys", "encoding=ascii"], 1, "Bez escape \\u.")],
    w_praktyce=["Raport zawsze z liczbą wczytanych wierszy na końcu.", "Specyfikacja formatu pliku (separator, kodowanie, format liczb) przed kodem."],
    zrodla=[Z_CSV, Z_JSON, Z_PATH],
)

FLASK = L(
    id="aplikacja_flask", nazwa="Aplikacja internetowa we Flask: trasy, parametry, JSON i testy", tydzien=10,
    slowa=["Flask", "trasa", "route", "request.args", "jsonify", "create_app", "test_client", "debug", "serwer"],
    cel="Po tej lekcji czytasz i zlecasz małą aplikację Flask z funkcją create_app, trasą strony i trasą API zwracającą JSON, obsługujesz złe parametry kodem 400 i testujesz ją test_client bez uruchamiania serwera.",
    po_co="Strona statyczna nie zapisze rezerwacji ani nie sprawdzi danych na serwerze. Flask to najprostszy krok od skryptu do aplikacji internetowej — i świetnie współpracuje z agentami.",
    wymagania=["Środowisko kursu (Flask instaluje Mentor).", "Lekcje „Testy jako umowa” i „JavaScript na stronie”."],
    wyjasnienie=(
        "## Najmniejsza aplikacja\n"
        "```\nfrom flask import Flask, jsonify, request\n\ndef create_app():\n    app = Flask(__name__)\n\n    @app.route(\"/\")\n    def start():\n        return \"<h1>Pod Lipą</h1>\"\n\n    @app.route(\"/api/cena\")\n    def cena():\n        noce = request.args.get(\"noce\", type=int)\n        ...\n        return jsonify({\"koszt\": 480.0})\n\n    return app\n```\n"
        "- Trasa (route) łączy adres z funkcją: wejście na `/api/cena?noce=2&osoby=2` uruchamia funkcję cena.\n"
        "- `request.args.get(\"noce\", type=int)` czyta parametr z adresu; gdy nie jest liczbą — zwraca None.\n"
        "- `jsonify` zwraca dane w JSON (dla JavaScriptu i innych programów).\n"
        "- create_app (wzorzec „fabryki aplikacji” z dokumentacji Flaska) tworzy aplikację w funkcji — testy mogą zbudować świeżą aplikację, a konfiguracja (np. ścieżka bazy) przychodzi jako parametr.\n"
        "## Kody odpowiedzi\n"
        "| kod | znaczy | kiedy |\n"
        "|---|---|---|\n"
        "| 200 | OK | poprawne dane |\n"
        "| 400 | złe żądanie | brak parametru, „abc” zamiast liczby, noce = 0 |\n"
        "| 404 | nie ma takiej strony | zły adres |\n"
        "| 500 | błąd serwera | wyjątek w Twoim kodzie — nie może się zdarzać dla złych danych od użytkownika |\n"
        "Złe dane od użytkownika → 400 z komunikatem: `return jsonify({\"blad\": \"noce musi być liczbą ≥ 1\"}), 400`.\n"
        "## Uruchomienie lokalnie\n"
        "W terminalu Mentora: `flask --app app run --debug` → adres http://127.0.0.1:5000. Tryb debug przeładowuje kod po zmianie i pokazuje błędy w przeglądarce — TYLKO na Twoim komputerze. "
        "Dokumentacja Flaska: wbudowany serwer deweloperski nie nadaje się do produkcji, a debugger pozwala wykonać dowolny kod — nigdy nie włączaj go na serwerze publicznym.\n"
        "## Testy bez serwera\n"
        "```\ndef test_cena():\n    klient = create_app().test_client()\n    odp = klient.get(\"/api/cena?noce=2&osoby=2\")\n    assert odp.status_code == 200\n    assert odp.get_json() == {\"koszt\": 480.0}\n```\n"
        "## Logika osobno\n"
        "Funkcja licząca koszt mieszka w kalkulator_pobytu.py (już przetestowana). Trasa tylko: czyta parametry → woła funkcję → zamienia ValueError na 400 → zwraca JSON. Agent lubi wklejać logikę do trasy — prosisz o import.\n"
        "## Gdzie to później działa\n"
        "Aplikacja Python potrzebuje hostingu z Pythonem (np. usługi typu PaaS z darmowym lub tanim planem — warunki zmieniają się, sprawdzasz je przed decyzją). W kursie: lokalnie i w testach; publikacja w projekcie końcowym jest opcjonalna."),
    przyklad=("from flask import Flask, jsonify, request\nfrom kalkulator_pobytu import koszt_pobytu\n\n\ndef create_app():\n    app = Flask(__name__)\n\n"
              "    @app.route(\"/\")\n    def start():\n        return \"<h1>Pod Lipą</h1><p>Kalkulator: /api/cena?noce=2&osoby=2</p>\"\n\n"
              "    @app.route(\"/api/cena\")\n    def cena():\n        noce = request.args.get(\"noce\", type=int)\n        osoby = request.args.get(\"osoby\", type=int)\n"
              "        if noce is None or osoby is None:\n            return jsonify({\"blad\": \"podaj noce i osoby jako liczby\"}), 400\n"
              "        try:\n            return jsonify({\"koszt\": koszt_pobytu(noce, osoby)})\n        except ValueError as e:\n            return jsonify({\"blad\": str(e)}), 400\n\n    return app"),
    demonstracja={"tytul": "Aplikacja z agentem i test, który łapie 500", "kroki": [
        "Prośba: „app.py z create_app(): trasa / (HTML z nazwą Pod Lipą) i /api/cena?noce=&osoby= zwracająca JSON {\"koszt\": …} z funkcji koszt_pobytu z kalkulator_pobytu.py. Złe dane → 400 i {\"blad\": …}. Bez debug=True w kodzie. Testy w test_app.py.”",
        "`flask --app app run --debug` → przeglądarka: http://127.0.0.1:5000/api/cena?noce=2&osoby=2 → {\"koszt\": 480}.",
        "Adres z noce=0: strona błędu 500 i traceback ValueError — agent nie złapał wyjątku z koszt_pobytu.",
        "Prośba: „ValueError z koszt_pobytu ma dawać 400 z komunikatem”. Test: klient.get(\"/api/cena?noce=0&osoby=2\").status_code == 400 — zielono.",
        "Ctrl + C zatrzymuje serwer. Commit app.py i test_app.py."],
        "wynik": "Aplikacja odpowiada 200 dla dobrych danych i 400 z komunikatem dla złych; brak 500 dla błędów użytkownika, potwierdzony testem."},
    jak_uruchomic=["Terminal Mentora w PRACA: `flask --app app run --debug` → http://127.0.0.1:5000; Ctrl + C kończy.", "Testy: `python -m pytest -q test_app.py` albo „✔ Sprawdź wynik”."],
    cwiczenia=[
        C("prowadzone",
          "Jaki kod odpowiedzi powinna zwrócić aplikacja z przykładu dla: (1) /api/cena?noce=2&osoby=2, (2) /api/cena?noce=abc&osoby=2, (3) /api/cena?noce=0&osoby=2, (4) /api/cenaa?noce=2. Czas: 15 minut.",
          "(1) 200; (2) 400; (3) 400; (4) 404.",
          ["Poprawne dane — OK.", "type=int zwraca None dla „abc” → gałąź 400.", "Zły adres trasy — nie ma takiej strony."],
          "200, 400 (abc → None), 400 (ValueError z koszt_pobytu → 400), 404 (brak trasy /api/cenaa).",
          [li("k1", "(1)", 200), li("k2", "(2)", 400, bledy=[bl(500, "type=int zwraca None, a kod sprawdza None → 400, nie wyjątek")]), li("k3", "(3)", 400), li("k4", "(4)", 404)]),
        C("samodzielne",
          "Prawda czy fałsz? (1) `debug=True` można zostawić na serwerze publicznym, jeśli strona jest mała. (2) test_client pozwala testować trasy bez uruchamiania serwera. (3) Błąd 500 dla złych danych od użytkownika jest w porządku. "
          "(4) `request.args.get(\"noce\", type=int)` dla „abc” zwraca None. Czas: 15 minut.",
          "(1) fałsz; (2) prawda; (3) fałsz; (4) prawda.",
          ["Debugger pozwala wykonać kod na serwerze.", "test_client — z dokumentacji testowania.", "Złe dane → 400."],
          "Fałsz, prawda, fałsz, prawda.",
          [wy(f"p{i}", t, ["prawda", "fałsz"], w) for i, t, w in ((1, "(1) debug na serwerze", "fałsz"), (2, "(2) test_client", "prawda"), (3, "(3) 500 dla złych danych", "fałsz"), (4, "(4) type=int i „abc”", "prawda"))]),
    ],
    typowe_bledy=[
        B("„Error: Could not locate a Flask application”.", "Uruchomienie z innego folderu albo zła nazwa w --app.", "`dir app.py` w bieżącym folderze.", "`flask --app app run` w PRACA (app = nazwa pliku bez .py); w pliku funkcja create_app albo zmienna app."),
        B("„Address already in use” / port 5000 zajęty.", "Serwer działa w innym oknie.", "Czy inne okno terminala ma uruchomiony flask?", "Zatrzymaj Ctrl + C albo `flask --app app run --port 5001`."),
        B("Testy: „TypeError: 'NoneType' object is not subscriptable” na get_json().", "Trasa zwraca HTML albo tekst, nie JSON.", "odp.data w teście.", "Zwracaj jsonify(...) w trasach API."),
    ],
    pulapki=["Serwer deweloperski i tryb debug — tylko lokalnie. Agent czasem dopisuje `app.run(debug=True, host=\"0.0.0.0\")` — host 0.0.0.0 udostępnia aplikację w całej sieci lokalnej.",
             "Walidacja w JavaScript nie zwalnia z walidacji na serwerze — każdy może wywołać API ręcznie."],
    zadania=["Zbuduj app.py z create_app i testami (zadanie tygodnia).", "Sprawdź w przeglądarce kody 200/400/404.", "Commit + push."],
    pytania=[["Po co create_app?", "Testy i konfiguracja mogą tworzyć świeżą aplikację z parametrami, bez globalnego stanu."], ["Jaki kod dla złych danych użytkownika?", "400 z komunikatem w JSON."],
             ["Dlaczego debug=False na serwerze?", "Debugger pozwala wykonać dowolny kod — to dziura bezpieczeństwa."]],
    podsumowanie="Czytasz i zlecasz aplikację Flask z fabryką, trasami HTML i JSON, obsługą 400, testujesz ją test_client i wiesz, czego nie robić z trybem debug.",
    test=[T("`@app.route(\"/api/cena\")` oznacza:", ["Import", "Powiązanie adresu z funkcją", "Bazę danych", "Test"], 1, "Trasa."),
          T("Złe dane od użytkownika — kod odpowiedzi:", ["200", "400", "500", "302"], 1, "Błąd po stronie żądania."),
          T("Testowanie tras bez uruchamiania serwera:", ["app.test_client()", "flask run", "curl", "ping"], 0, "Dokumentacja Flaska."),
          T("Tryb debug Flaska na serwerze publicznym:", ["Zalecany", "Zabroniony — pozwala wykonać kod", "Obowiązkowy", "Bez znaczenia"], 1, "Tylko lokalnie.")],
    w_praktyce=["Logika w modułach, trasy tylko tłumaczą żądanie na wywołanie.", "Każda trasa API: test 200 i test 400."],
    zrodla=[Z_FLASK_QS, Z_FLASK_FACT, Z_FLASK_TEST, Z_FLASK_DEPLOY],
)

BAZA = L(
    id="baza_sqlite", nazwa="Baza danych SQLite: tabela, zapis, wyszukiwanie — bez SQL injection", tydzien=10,
    slowa=["SQLite", "SQL", "tabela", "INSERT", "SELECT", "placeholder", "SQL injection", "commit"],
    cel="Po tej lekcji tworzysz tabelę SQLite, zapisujesz i wyszukujesz dane z Pythona zapytaniami z parametrami (?), rozumiesz SQL injection i rozpoznajesz niebezpieczny kod od agenta.",
    po_co="Lista gości w pliku przestaje wystarczać, gdy aplikacja ma zapisywać rezerwacje. SQLite jest wbudowany w Pythona — a SQL injection to jedna z najstarszych i wciąż częstych dziur w kodzie, także generowanym przez AI.",
    wymagania=["Lekcja „Aplikacja Flask”.", "Moduł sqlite3 (wbudowany w Pythona — nic nie instalujesz)."],
    wyjasnienie=(
        "## Baza = plik z tabelami\n"
        "SQLite trzyma całą bazę w jednym pliku (np. pod_lipa.db). Tabela ma kolumny i wiersze — jak arkusz, ale z typami i regułami. Język zapytań to SQL.\n"
        "```\nCREATE TABLE IF NOT EXISTS goscie (\n  id INTEGER PRIMARY KEY,\n  imie TEXT NOT NULL,\n  email TEXT NOT NULL UNIQUE,\n  noce INTEGER NOT NULL CHECK (noce >= 1)\n)\n```\n"
        "## Python + sqlite3\n"
        "```\nimport sqlite3\ncon = sqlite3.connect(\"pod_lipa.db\")\ncon.execute(CREATE_GOSCIE)\nwith con:   # zatwierdza (commit) albo wycofuje przy błędzie\n    cur = con.execute(\"INSERT INTO goscie (imie, email, noce) VALUES (?, ?, ?)\", (imie, email, noce))\nnowe_id = cur.lastrowid\nwiersz = con.execute(\"SELECT id, imie, email, noce FROM goscie WHERE email = ?\", (email,)).fetchone()\n```\n"
        "## SQL injection — dlaczego znaki ? są obowiązkowe\n"
        "Niebezpieczne (agent czasem tak pisze):\n"
        "`con.execute(f\"SELECT * FROM goscie WHERE email = '{email}'\")`\n"
        "Jeśli ktoś wpisze w formularzu e-mail `x' OR '1'='1`, zapytanie staje się `… WHERE email = 'x' OR '1'='1'` — zwraca WSZYSTKICH gości. Inne wpisy mogą usunąć dane. "
        "Dokumentacja sqlite3 mówi wprost: używaj placeholderów zamiast formatowania napisów. OWASP: zapytania parametryzowane to główna obrona.\n"
        "| zapis | bezpieczny? |\n"
        "|---|---|\n"
        "| `execute(\"… WHERE email = ?\", (email,))` | tak |\n"
        "| `execute(f\"… WHERE email = '{email}'\")` | NIE |\n"
        "| `execute(\"… WHERE email = '%s'\" % email)` | NIE |\n"
        "| `execute(\"… WHERE email = '\" + email + \"'\")` | NIE |\n"
        "Uwaga na krotkę jednoelementową: `(email,)` — z przecinkiem.\n"
        "## Reguły w bazie\n"
        "NOT NULL, UNIQUE i CHECK pilnują danych nawet, gdy kod się pomyli: drugi gość z tym samym e-mailem → sqlite3.IntegrityError. Twój kod zamienia go na czytelny komunikat (albo ValueError).\n"
        "## Testy z bazą\n"
        "W testach baza w pamięci: `sqlite3.connect(\":memory:\")` — szybka, znika po teście, nie miesza danych. Dlatego funkcje przyjmują połączenie (`con`) jako parametr."),
    przyklad=kod("baza_sqlite:przyklad",
                 "import sqlite3\n\ncon = sqlite3.connect(\":memory:\")\ncon.execute(\"CREATE TABLE goscie (id INTEGER PRIMARY KEY, imie TEXT, email TEXT UNIQUE)\")\n"
                 "with con:\n    con.execute(\"INSERT INTO goscie (imie, email) VALUES (?, ?)\", (\"Anna\", \"anna@pod-lipa.pl\"))\n    con.execute(\"INSERT INTO goscie (imie, email) VALUES (?, ?)\", (\"Piotr\", \"piotr@pod-lipa.pl\"))\n\n"
                 "zly = \"x' OR '1'='1\"\nprint(con.execute(\"SELECT COUNT(*) FROM goscie WHERE email = ?\", (zly,)).fetchone()[0])\n"
                 "print(con.execute(f\"SELECT COUNT(*) FROM goscie WHERE email = '{zly}'\").fetchone()[0])\n",
                 "0\n2\n"),
    demonstracja={"tytul": "Atak na wyszukiwarkę gości i jego zablokowanie", "kroki": [
        "Agent napisał znajdz_po_emailu z f-stringiem. Test normalny: anna@pod-lipa.pl → Anna. Działa.",
        "Wpisujesz e-mail `x' OR '1'='1` → funkcja zwraca pierwszego gościa z bazy, choć taki e-mail nie istnieje. W wersji „lista wyników” — wszystkich.",
        "Przykład lekcji pokazuje to liczbowo: zapytanie z ? zwraca 0, z f-stringiem — 2.",
        "Prośba: „wszystkie zapytania wyłącznie z placeholderami ?, żadnego formatowania SQL”. Test: zapis gościa z e-mailem `x' OR '1'='1` zapisuje dokładnie ten napis, a wyszukiwanie innego e-maila zwraca None.",
        "Dopisujesz zasadę do AGENTS.md: „SQL tylko z parametrami ?”."],
        "wynik": "Wyszukiwarka odporna na SQL injection, potwierdzona testem z „podejrzanym” e-mailem; zasada utrwalona w instrukcjach agenta."},
    jak_uruchomic=["Zadanie tygodnia „baza.py” → testy użyją bazy :memory: → „✔ Sprawdź wynik”."],
    cwiczenia=[
        C("prowadzone",
          "Co wypisze przykład lekcji (dwie liczby)? Która linia jest podatna na SQL injection: pierwsza (z ?) czy druga (z f-stringiem)? Jak zapiszesz krotkę z jednym parametrem email? Czas: 15 minut.",
          "0 i 2; podatna druga (f-string); krotka (email,).",
          ["Z ? cały napis jest porównywany jako e-mail — takiego nie ma.", "W f-stringu napis staje się częścią SQL: OR '1'='1' jest zawsze prawdą.", "Krotka jednoelementowa ma przecinek."],
          "0 (bezpiecznie), 2 (atak zwrócił wszystkich); podatna wersja z f-stringiem; (email,).",
          [li("a", "Pierwsza liczba", 0), li("b", "Druga liczba", 2), wy("podatna", "Podatna linia", ["pierwsza (z ?)", "druga (z f-stringiem)"], "druga (z f-stringiem)"), tx("krotka", "Krotka z jednym parametrem", ["(email,)"])]),
        C("samodzielne",
          "Które zapisy są bezpieczne? (1) `execute(\"DELETE FROM goscie WHERE id = ?\", (gid,))` (2) `execute(\"DELETE FROM goscie WHERE id = \" + str(gid))` (3) `execute(\"SELECT * FROM goscie WHERE imie = '%s'\" % imie)` (4) `execute(\"SELECT * FROM goscie WHERE imie = ?\", (imie,))`. "
          "Podaj numery bezpiecznych rosnąco. Jaki wyjątek rzuci sqlite3 przy drugim gościu z tym samym e-mailem (UNIQUE)? Czas: 15 minut.",
          "Bezpieczne: 1 i 4 → „14”; IntegrityError.",
          ["Bezpieczne mają ? i krotkę parametrów.", "Sklejanie i % to formatowanie napisu SQL.", "Naruszenie reguły UNIQUE — błąd integralności."],
          "1 i 4 (parametry). Duplikat UNIQUE → sqlite3.IntegrityError.",
          [tx("bezp", "Numery bezpiecznych", ["14"]), tx("wyj", "Wyjątek przy duplikacie", ["IntegrityError", "sqlite3.IntegrityError"])]),
    ],
    typowe_bledy=[
        B("„sqlite3.ProgrammingError: Incorrect number of bindings supplied”.", "`(email)` zamiast `(email,)` — napis traktowany jak sekwencja znaków.", "Liczba ? vs elementy krotki.", "Krotka z przecinkiem: (email,)."),
        B("Dane „znikają” po zamknięciu programu.", "Brak commit (zapis bez with con: ani con.commit()).", "Czy INSERT jest w bloku with con:?", "with con: wokół zapisów."),
        B("„sqlite3.OperationalError: no such table: goscie”.", "Tabela nie utworzona w tej bazie (inna ścieżka pliku, :memory: w innym połączeniu).", "Ścieżka pliku bazy, kolejność wywołań.", "CREATE TABLE IF NOT EXISTS przy połączeniu (funkcja polacz)."),
    ],
    pulapki=["Plik bazy z danymi gości nie trafia do Gita (.gitignore: *.db) — to dane osobowe.", "Agent „naprawia” IntegrityError przez usunięcie UNIQUE z tabeli — to osłabienie reguły, nie poprawka."],
    zadania=["Zbuduj baza.py z polacz, dodaj_goscia, znajdz_po_emailu, lista_gosci (zadanie tygodnia).", "Dopisz *.db do .gitignore.", "Zasada „SQL tylko z ?” w AGENTS.md."],
    pytania=[["Czym jest SQL injection?", "Wstrzyknięciem fragmentu SQL przez dane użytkownika wklejone do zapytania jako tekst."], ["Jak się przed nim bronisz?", "Zapytania parametryzowane (?) zamiast formatowania napisów."],
             ["Po co baza :memory: w testach?", "Szybka, izolowana baza znikająca po teście."]],
    podsumowanie="Tworzysz tabelę z regułami, zapisujesz i wyszukujesz zapytaniami z ?, rozpoznajesz SQL injection w kodzie agenta i testujesz na bazie w pamięci.",
    test=[T("Bezpieczne zapytanie w sqlite3:", ["f\"… = '{x}'\"", "\"… = ?\", (x,)", "\"… = '\" + x + \"'\"", "\"… = '%s'\" % x"], 1, "Parametry."),
          T("`x' OR '1'='1` w podatnym wyszukiwaniu po e-mailu:", ["Nic nie zwraca", "Zwraca wszystkich gości", "Usuwa bazę zawsze", "Błąd składni zawsze"], 1, "Warunek zawsze prawdziwy."),
          T("Reguła blokująca dwa takie same e-maile:", ["NOT NULL", "UNIQUE", "CHECK", "PRIMARY"], 1, "IntegrityError."),
          T("Plik bazy z danymi gości w Gicie:", ["Commitujesz", "Dodajesz *.db do .gitignore", "Wysyłasz na Pages", "Wklejasz do README"], 1, "Dane osobowe.")],
    w_praktyce=["Każde zapytanie SQL od agenta — szukasz f\" i + w execute.", "Funkcje bazy przyjmują połączenie jako parametr."],
    zrodla=[Z_SQLITE, Z_OWASP_SQLI, ["Veracode — GenAI Code Security Report (30.07.2025)", "https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/", D]],
)


# =========================================================================== TYDZIEŃ 11
API = L(
    id="api_klucze", nazwa="API i klucze: pobierasz dane z internetu i nie zdradzasz sekretów", tydzien=11,
    slowa=["API", "klucz API", "zmienna środowiskowa", "requests", "timeout", ".env", "sekret", "os.environ"],
    cel="Po tej lekcji wywołujesz API z Pythona (requests z timeoutem i obsługą błędów), trzymasz klucz w zmiennej środowiskowej zamiast w kodzie i reagujesz, gdy klucz wycieknie.",
    po_co="Pogoda, kursy walut, mapy, SMS — aplikacje korzystają z cudzych usług przez API z kluczem. Klucz w kodzie na GitHubie to realne koszty i włamania; agent chętnie wpisuje klucz „na sztywno”.",
    wymagania=["Biblioteka requests (instaluje Mentor).", "Lekcje „Aplikacja Flask” i „GitHub”."],
    wyjasnienie=(
        "## API w jednym zdaniu\n"
        "API to adres, pod który program wysyła pytanie i dostaje odpowiedź w JSON. Przykład: `GET https://api.pogoda.example/v1/current?miasto=Radzyń&key=…` → `{\"current\": {\"temp\": 4.5}}` (usługa w kursie jest fikcyjna — prawdziwe API mają własną dokumentację).\n"
        "## requests — wywołanie z bezpiecznikami\n"
        "```\nimport requests\nodp = requests.get(URL, params={\"miasto\": miasto}, headers={\"X-API-Key\": klucz}, timeout=10)\nodp.raise_for_status()      # 4xx/5xx → wyjątek\ndane = odp.json()\n```\n"
        "- `timeout=10` — bez niego program może czekać w nieskończoność (dokumentacja requests zaleca zawsze ustawiać timeout).\n"
        "- `raise_for_status()` — błąd HTTP jako wyjątek, a nie „cicha” zła odpowiedź.\n"
        "- Klucz w nagłówku (`headers`) albo w `params`, zależnie od dokumentacji usługi.\n"
        "## Klucz poza kodem: zmienna środowiskowa\n"
        "Kod czyta: `klucz = os.environ.get(\"POGODA_API_KEY\")`; brak → czytelny błąd „Ustaw zmienną POGODA_API_KEY”. Ustawienie w Windows:\n"
        "| gdzie | polecenie | jak długo |\n"
        "|---|---|---|\n"
        "| CMD (terminal Mentora) | `set POGODA_API_KEY=twoj_klucz` | do zamknięcia okna |\n"
        "| PowerShell | `$env:POGODA_API_KEY=\"twoj_klucz\"` | do zamknięcia okna |\n"
        "| trwale | `setx POGODA_API_KEY \"twoj_klucz\"` | w NOWYCH oknach (bieżące nie widzi) |\n"
        "Plik `.env` z liniami `NAZWA=wartość` to popularna wygoda (biblioteka python-dotenv) — ale wtedy `.env` MUSI być w .gitignore i w regułach deny agenta (tydzień 12).\n"
        "## Gdy klucz wycieknie\n"
        "- Unieważnij (revoke/rotate) klucz w panelu usługi NATYCHMIAST — usunięcie z kodu nie wystarczy (historia Gita, kopie, boty skanujące GitHub).\n"
        "- Wygeneruj nowy, ustaw w zmiennej środowiskowej.\n"
        "- Sprawdź rachunek/zużycie w panelu usługi.\n"
        "- GitHub skanuje publiczne repozytoria pod kątem znanych formatów kluczy (secret scanning) i może zablokować push z kluczem — to siatka, nie strategia.\n"
        "## Testy bez internetu\n"
        "Funkcja przyjmuje opcjonalny parametr `klient` (funkcję wykonującą zapytanie). W testach podajesz fałszywego klienta zwracającego przygotowany JSON — test działa bez sieci i bez klucza, a Ty sprawdzasz też, czy funkcja przekazała klucz i obsłużyła błąd."),
    przyklad=kod("api_klucze:przyklad",
                 "import os\n\n\ndef pobierz_temperature(miasto, klient=None):\n    klucz = os.environ.get(\"POGODA_API_KEY\")\n    if not klucz:\n        raise RuntimeError(\"Ustaw zmienną środowiskową POGODA_API_KEY\")\n"
                 "    if klient is None:\n        import requests\n        def klient(url, params, headers):\n            odp = requests.get(url, params=params, headers=headers, timeout=10)\n            odp.raise_for_status()\n            return odp.json()\n"
                 "    dane = klient(\"https://api.pogoda.example/v1/current\", {\"miasto\": miasto}, {\"X-API-Key\": klucz})\n    return float(dane[\"current\"][\"temp\"])\n\n\n"
                 "os.environ[\"POGODA_API_KEY\"] = \"test-123\"   # tylko na potrzeby przykładu!\nprint(pobierz_temperature(\"Radzyń\", klient=lambda u, p, h: {\"current\": {\"temp\": 4.5}}))\n",
                 "4.5\n"),
    demonstracja={"tytul": "Agent wpisał klucz w kod — sprzątanie", "kroki": [
        "Prośba „dodaj pobieranie pogody, klucz: abc…” — błąd już w prośbie: klucz trafił do rozmowy. Agent wpisał `API_KEY = \"abc…\"` w pogoda.py.",
        "Zanim zrobisz commit: przegląd diffu (pytanie 4 — tajemnice) łapie klucz. Poprawka: os.environ.get + RuntimeError z instrukcją; `set POGODA_API_KEY=…` w terminalu.",
        "Klucz był w rozmowie z agentem (serwery dostawcy) — dla bezpieczeństwa generujesz nowy w panelu usługi i stary unieważniasz.",
        "Test z fałszywym klientem: sprawdza temperaturę, przekazanie klucza w nagłówku, RuntimeError bez zmiennej — bez internetu.",
        "Zasada w AGENTS.md: „Klucze tylko ze zmiennych środowiskowych; nigdy w kodzie, testach ani README”."],
        "wynik": "Klucz poza kodem i historią Gita, unieważniony po kontakcie z rozmową, funkcja przetestowana bez sieci."},
    jak_uruchomic=["CMD: `set POGODA_API_KEY=…` → `python pogoda.py` w tym samym oknie.", "Zadanie tygodnia → „✔ Sprawdź wynik” (testy z fałszywym klientem, bez internetu i bez klucza)."],
    cwiczenia=[
        C("prowadzone",
          "W terminalu Mentora wpisujesz `setx POGODA_API_KEY \"k123\"`, a potem w TYM SAMYM oknie `python pogoda.py` → RuntimeError „Ustaw zmienną…”. (1) Dlaczego? Wybierz: setx działa w nowych oknach / setx nie działa w Windows. "
          "(2) Jakie polecenie CMD ustawi zmienną w bieżącym oknie? (3) Jaką wartość domyślną ma timeout w requests, jeśli go nie podasz: brak (czeka bez końca) czy 30 s? Czas: 15 minut.",
          "(1) setx działa w nowych oknach; (2) set POGODA_API_KEY=k123; (3) brak — bez timeout żądanie może czekać bez końca.",
          ["setx zapisuje trwale dla przyszłych okien.", "Bieżące okno: polecenie set.", "Dokumentacja requests zaleca zawsze podawać timeout."],
          "setx działa dopiero w nowych oknach; w bieżącym: set POGODA_API_KEY=k123; requests bez timeout czeka bez limitu.",
          [wy("setx", "(1) Dlaczego?", ["setx działa w nowych oknach", "setx nie działa w Windows"], "setx działa w nowych oknach"),
           tx("set", "(2) Polecenie CMD", ["set POGODA_API_KEY=k123"], zawiera=["setPOGODA_API_KEY"]), wy("timeout", "(3) Domyślny timeout", ["brak (czeka bez końca)", "30 s"], "brak (czeka bez końca)")]),
        C("samodzielne",
          "Klucz API trafił do publicznego repozytorium 2 dni temu; usunąłeś go nowym commitem. Uporządkuj działania: A) unieważnij klucz w panelu usługi, B) wygeneruj nowy i ustaw w zmiennej środowiskowej, C) sprawdź zużycie/rachunek w panelu, D) dopisz zasadę do AGENTS.md. Kolejność liter. "
          "Czy usunięcie pliku w nowym commicie usunęło klucz z historii (tak/nie)? Czas: 15 minut.",
          "ABCD; nie.",
          ["Najpierw zatrzymaj szkody.", "Potem przywróć działanie aplikacji.", "Na końcu sprawdzenie skutków i zapobieganie."],
          "Unieważnij → nowy klucz → sprawdź zużycie → zasada = ABCD. Historia Gita nadal zawiera klucz.",
          [tx("kol", "Kolejność", ["ABCD"]), wy("hist", "Usunięty z historii?", TN, "nie")]),
    ],
    typowe_bledy=[
        B("„requests.exceptions.ConnectTimeout” albo program wisi.", "Brak sieci, usługa nie odpowiada, brak timeout.", "Czy timeout jest ustawiony?", "timeout=10 i obsługa wyjątku z czytelnym komunikatem („usługa pogody nie odpowiada”)."),
        B("„401 Unauthorized” / „403 Forbidden”.", "Zły/nieaktywny klucz albo zły sposób przekazania (nagłówek vs parametr).", "Dokumentacja usługi: jak przekazać klucz.", "Sprawdź zmienną (echo %POGODA_API_KEY% — tylko u siebie!), sposób przekazania, aktywację klucza."),
        B("GitHub odrzuca push: „Push cannot contain secrets”.", "Ochrona przed wypchnięciem sekretu (push protection).", "Który plik i linia?", "Usuń klucz z commita (zanim trafi do historii), unieważnij go, ustaw w zmiennej."),
    ],
    pulapki=["Nie wklejaj kluczy do rozmowy z agentem ani czatem. Jeśli wkleiłeś — traktuj klucz jako ujawniony.", "Klucz w JavaScript na stronie publicznej jest jawny dla każdego gościa (F12) — klucze do płatnych usług tylko po stronie serwera."],
    zadania=["Zbuduj pogoda.py z kluczem ze zmiennej i testem z fałszywym klientem (zadanie tygodnia).", "Dopisz .env do .gitignore (jeśli jeszcze nie ma).", "Zasada o kluczach w AGENTS.md."],
    pytania=[["Gdzie trzymasz klucz API?", "W zmiennej środowiskowej (lub w .env poza Gitem), nigdy w kodzie."], ["Co robisz po wycieku klucza?", "Unieważniam go, generuję nowy, sprawdzam zużycie, dopisuję zasadę."],
             ["Po co timeout w requests?", "Żeby program nie czekał bez końca na odpowiedź."]],
    podsumowanie="Wywołujesz API z timeoutem i obsługą błędów, trzymasz klucz w zmiennej środowiskowej, testujesz bez sieci i wiesz, co robić po wycieku.",
    test=[T("Klucz API w kodzie na GitHubie:", ["W porządku w repo prywatnym na zawsze", "Ryzyko — unieważnij i przenieś do zmiennej środowiskowej", "Wymóg API", "Przyspiesza"], 1, "Historia i kopie."),
          T("`set NAZWA=wartość` w CMD działa:", ["Na zawsze", "Do zamknięcia okna", "Tylko w PowerShell", "Po restarcie"], 1, "Trwale — setx w nowych oknach."),
          T("Dlaczego testy API z fałszywym klientem?", ["Bo są ładniejsze", "Działają bez sieci i klucza, sprawdzają obsługę danych i błędów", "Bo API jest płatne zawsze", "Nie ma powodu"], 1, "Izolacja."),
          T("`odp.raise_for_status()` robi:", ["Nic", "Zamienia odpowiedź 4xx/5xx w wyjątek", "Ponawia zapytanie", "Usuwa klucz"], 1, "Brak cichych błędów.")],
    w_praktyce=["Każdy klucz: zmienna środowiskowa + .gitignore + reguła deny agenta.", "Raz w miesiącu przegląd aktywnych kluczy w panelach usług."],
    zrodla=[Z_REQUESTS, Z_OS_ENV, Z_SETX, Z_OWASP_SECRETS],
)

AUTOMATY = L(
    id="automatyzacje", nazwa="Automatyzacje: skrypt porządkujący pliki z trybem próby i harmonogram", tydzien=11,
    slowa=["automatyzacja", "pathlib", "shutil", "tryb próby", "dry-run", "harmonogram", "schtasks", "log"],
    cel="Po tej lekcji zlecasz i sprawdzasz skrypt, który porządkuje pliki (z obowiązkowym trybem próby, bez nadpisywania), oraz uruchamiasz go automatycznie Harmonogramem zadań Windows.",
    po_co="„Codziennie przenoszę faktury i zdjęcia do folderów” — klienci płacą za oszczędzony czas. Skrypt działający na prawdziwych plikach musi być bezpieczny, bo pomyłka niszczy dane.",
    wymagania=["Lekcje „Pliki, foldery…” i „Terminal”.", "Folder testowy z kopiami plików (NIE prawdziwe dokumenty przy pierwszych próbach)."],
    wyjasnienie=(
        "## Zasady bezpiecznej automatyzacji plików\n"
        "| zasada | jak w kodzie |\n"
        "|---|---|\n"
        "| najpierw tryb próby | `uporzadkuj(katalog, wykonaj=False)` tylko zwraca plan „plik → cel”, nic nie zmienia |\n"
        "| nigdy nie nadpisuj | gdy cel istnieje: `faktura_1.pdf`, `faktura_2.pdf`… |\n"
        "| nie usuwaj | przenoś; kasowanie zostaw człowiekowi |\n"
        "| działaj tylko w podanym katalogu | bez rekurencji w górę, bez ścieżek absolutnych z danych |\n"
        "| zapisuj, co zrobiłeś | log: data, plik, skąd, dokąd |\n"
        "| najpierw na kopii | folder testowy przed prawdziwym |\n"
        "## pathlib i shutil\n"
        "`from pathlib import Path`: `Path(katalog).iterdir()` — zawartość folderu, `p.suffix.lower()` — rozszerzenie (`.JPG` → `.jpg`), `p.is_file()`, `cel.exists()`, `(katalog / \"zdjecia\").mkdir(exist_ok=True)`. "
        "`shutil.move(str(p), str(cel))` przenosi. Path działa tak samo w Windows i Linuksie.\n"
        "## Reguły porządkowania (zadanie tygodnia)\n"
        "| rozszerzenia | folder |\n"
        "|---|---|\n"
        "| .jpg .jpeg .png .heic | zdjecia |\n"
        "| .pdf .doc .docx | dokumenty |\n"
        "| .csv .xlsx .xls | dane |\n"
        "| pozostałe pliki | inne |\n"
        "Foldery i pliki ukryte (zaczynające się od kropki) pomijasz. Plik bez rozszerzenia → inne.\n"
        "## Harmonogram zadań Windows\n"
        "Graficznie: Start → „Harmonogram zadań” → Utwórz zadanie podstawowe → codziennie 20:00 → Uruchom program: pełna ścieżka do python.exe środowiska kursu, argument: pełna ścieżka do skryptu. "
        "Z wiersza poleceń: `schtasks /create /sc daily /tn \"PodLipa_porzadki\" /tr \"\\\"C:\\…\\python.exe\\\" \\\"C:\\…\\porzadki.py\\\" --wykonaj\" /st 20:00`. "
        "Sprawdzenie: `schtasks /query /tn \"PodLipa_porzadki\"`, usunięcie: `schtasks /delete /tn \"PodLipa_porzadki\"`.\n"
        "Skrypt uruchamiany z harmonogramu nie ma okna — dlatego log w pliku jest jedynym śladem jego pracy.\n"
        "## Agent a pliki poza projektem\n"
        "Agent pracuje w katalogu projektu; skrypt, który napisał, uruchamiasz TY na wskazanym folderze. Nie dawaj agentowi dostępu do całego dysku „żeby sam poprzenosił”."),
    przyklad=kod("automatyzacje:przyklad",
                 "from pathlib import Path\n\nREGULY = {\".jpg\": \"zdjecia\", \".png\": \"zdjecia\", \".pdf\": \"dokumenty\", \".csv\": \"dane\"}\n\n"
                 "def cel_dla(nazwa):\n    return REGULY.get(Path(nazwa).suffix.lower(), \"inne\")\n\n"
                 "for n in [\"Lipa.JPG\", \"faktura.pdf\", \"notatka\", \"goscie.csv\", \"plan.txt\"]:\n    print(n, \"->\", cel_dla(n))\n",
                 "Lipa.JPG -> zdjecia\nfaktura.pdf -> dokumenty\nnotatka -> inne\ngoscie.csv -> dane\nplan.txt -> inne\n"),
    demonstracja={"tytul": "Tryb próby ratuje 200 zdjęć", "kroki": [
        "Agent napisał porzadki.py. Tworzysz folder testowy z 6 kopiami plików, w tym zdjecia/lipa.jpg i drugi lipa.jpg w korzeniu.",
        "Tryb próby: plan pokazuje „lipa.jpg → zdjecia/lipa.jpg” — konflikt nazw! Kod agenta użyłby shutil.move, który w tej sytuacji nadpisałby istniejący plik.",
        "Prośba: „gdy cel istnieje, dodaj _1, _2… przed rozszerzeniem; dodaj test na konflikt”. Plan: „lipa.jpg → zdjecia/lipa_1.jpg”.",
        "Uruchomienie z --wykonaj na kopii: pliki przeniesione, log zawiera 6 linii. Porównujesz liczbę plików przed i po — zgodna.",
        "Dopiero teraz harmonogram na prawdziwy folder — z logiem."],
        "wynik": "Skrypt bez nadpisywania i bez usuwania, sprawdzony trybem próby i na kopii, uruchamiany codziennie z logiem."},
    jak_uruchomic=["`python porzadki.py C:\\sciezka\\folder_testowy` (tryb próby), potem z `--wykonaj`.", "Harmonogram zadań → Utwórz zadanie podstawowe albo `schtasks /create …`."],
    cwiczenia=[
        C("prowadzone",
          "Co wypisze przykład lekcji? Wpisz cel (folder) dla: (1) Lipa.JPG, (2) notatka (bez rozszerzenia), (3) plan.txt. Dlaczego Lipa.JPG trafia do zdjęć mimo wielkich liter? Czas: 15 minut.",
          "(1) zdjecia; (2) inne; (3) inne; .lower() zamienia .JPG na .jpg.",
          ["suffix to rozszerzenie z kropką.", "Brak rozszerzenia → pusty suffix → domyślnie inne.", "Reguły mają małe litery."],
          "zdjecia (dzięki .lower()), inne (brak rozszerzenia), inne (.txt nie ma reguły).",
          [tx("c1", "(1) Lipa.JPG", ["zdjecia"]), tx("c2", "(2) notatka", ["inne"]), tx("c3", "(3) plan.txt", ["inne"])]),
        C("samodzielne",
          "W folderze jest już `dokumenty/faktura.pdf` oraz `dokumenty/faktura_1.pdf`. Porządkujesz nowy `faktura.pdf`. Jaką nazwę dostanie według zasady „nie nadpisuj”? "
          "Drugie: jakie polecenie pokaże, czy zadanie harmonogramu „PodLipa_porzadki” istnieje (pierwsze dwa słowa polecenia)? Czas: 15 minut.",
          "faktura_2.pdf; schtasks /query.",
          ["_1 jest zajęty.", "Kolejny wolny numer.", "Zapytanie o zadanie — parametr /query."],
          "faktura_2.pdf (pierwszy wolny numer); schtasks /query /tn \"PodLipa_porzadki\".",
          [tx("nazwa", "Nowa nazwa", ["faktura_2.pdf"], bledy=[bl("faktura_1.pdf", "faktura_1.pdf już istnieje — szukasz pierwszego wolnego numeru")]), tx("q", "Polecenie (dwa słowa)", ["schtasks /query"])]),
    ],
    typowe_bledy=[
        B("Pliki zniknęły / zostały nadpisane.", "shutil.move do istniejącej nazwy, brak trybu próby.", "Kosz, kopia zapasowa, log.", "Zasada „nie nadpisuj” + test konfliktu + zawsze najpierw tryb próby na kopii."),
        B("Zadanie harmonogramu „działa”, ale nic się nie dzieje.", "Względne ścieżki albo inny Python (bez bibliotek) w harmonogramie.", "Historia zadania w Harmonogramie, plik logu.", "Pełne ścieżki do python.exe środowiska kursu i do skryptu; katalog roboczy jako argument."),
        B("„PermissionError: [WinError 32] The process cannot access the file”.", "Plik otwarty w innym programie (np. Excel) albo synchronizowany przez OneDrive.", "Czy plik jest otwarty?", "Pomiń plik z wpisem w logu zamiast przerywać całość; uruchamiaj, gdy pliki nie są używane."),
    ],
    pulapki=["Skrypt z „rekursywnym” przeszukiwaniem (`rglob`) na folderze Dokumenty może przenieść pliki z podfolderów programów — działaj tylko na jednym poziomie, chyba że specyfikacja mówi inaczej.",
             "Automatyczne usuwanie plików zostawiasz człowiekowi; skrypt najwyżej przenosi do folderu „do_usuniecia”."],
    zadania=["Zbuduj porzadki.py z trybem próby i bez nadpisywania (zadanie tygodnia).", "Przetestuj na kopii plików.", "Opcjonalnie: zadanie w Harmonogramie z logiem."],
    pytania=[["Po co tryb próby?", "Żeby zobaczyć plan zmian bez dotykania plików i wyłapać konflikty."], ["Co robisz, gdy plik o tej nazwie już jest w celu?", "Dodaję numer _1, _2… — nigdy nie nadpisuję."],
             ["Dlaczego log jest obowiązkowy przy harmonogramie?", "Skrypt działa bez okna — log to jedyny ślad, co zrobił."]],
    podsumowanie="Zlecasz i sprawdzasz bezpieczną automatyzację plików: tryb próby, brak nadpisywania i usuwania, log, test na kopii i uruchamianie z Harmonogramu zadań.",
    test=[T("Pierwsze uruchomienie skryptu porządkującego:", ["Od razu na prawdziwych plikach", "Tryb próby na kopii", "Jako administrator", "Bez logu"], 1, "Bezpieczeństwo danych."),
          T("`Path(\"Foto.PNG\").suffix.lower()` to:", ["\"PNG\"", "\".png\"", "\"Foto\"", "\"png\""], 1, "Z kropką, małymi literami."),
          T("Skrypt ma usuwać duplikaty automatycznie. Zasada kursu:", ["Tak, od razu", "Przenieś do folderu do decyzji człowieka", "Usuń i nie loguj", "Usuń cały folder"], 1, "Kasowanie zostawiasz człowiekowi."),
          T("Polecenie tworzące zadanie w Harmonogramie z wiersza poleceń:", ["schtasks /create", "cron add", "at now", "task new"], 0, "Windows.")],
    w_praktyce=["Każdy skrypt na plikach klienta: tryb próby jako domyślny.", "Log w pliku z datą przy każdej automatyzacji."],
    zrodla=[Z_PATH, Z_SHUTIL, Z_SCHTASKS],
)

POWTORKA_2 = L(
    id="powtorka_etap_2", nazwa="Powtórka etapu 2: aplikacja „wolne pokoje” — strona, API, dane", tydzien=11,
    slowa=["powtórka", "integracja", "API", "kalendarz", "Flask", "etap 2", "mini-projekt"],
    cel="Po tej lekcji łączysz moduły z etapów 1–2 w działającą funkcję aplikacji: trasa /api/wolne korzysta z kalendarz.py, obsługuje złe daty kodem 400 i jest przetestowana — i oceniasz gotowość do etapu jakości.",
    po_co="Prawdziwe zlecenia to łączenie kawałków. Integracja ujawnia błędy, których nie widać w pojedynczych modułach (formaty dat, nazwy pól, kody błędów).",
    wymagania=["Wszystkie lekcje tygodni 8–11.", "kalendarz.py (tydzień 7) i app.py (tydzień 10) w PRACA."],
    wyjasnienie=(
        "## Lista kontrolna etapu 2\n"
        "| umiejętność | sprawdzian |\n"
        "|---|---|\n"
        "| testy | piszesz testy ze specyfikacji, łapiesz mutanty |\n"
        "| debugowanie | 5 kroków, minimalny przykład, test regresji |\n"
        "| refaktoryzacja | pod osłoną testów, bez zmiany zachowania |\n"
        "| strona | lang, viewport, label, alt; JS z walidacją; Pages |\n"
        "| dane | polski CSV, JSON, raport sprawdzony ręcznie |\n"
        "| Flask | create_app, 200/400/404, test_client |\n"
        "| baza | SQL z ?, reguły tabeli, :memory: w testach |\n"
        "| API i klucze | timeout, raise_for_status, zmienna środowiskowa |\n"
        "| automatyzacje | tryb próby, bez nadpisywania, log |\n"
        "## Mini-projekt: /api/wolne\n"
        "Specyfikacja (dopisz do app.py, nie psując /api/cena):\n"
        "- `GET /api/wolne?od=2026-12-21&do=2026-12-22` → 200 i `{\"od\": \"2026-12-21\", \"do\": \"2026-12-22\", \"wolne\": [\"Dębowy\", \"Klonowy\"]}`.\n"
        "- Rezerwacje: `create_app(rezerwacje=None)` — lista przekazana przy tworzeniu aplikacji (testy podają własną); domyślnie pusta lista.\n"
        "- Brak parametru, zła data (\"2026-13-01\", \"jutro\"), do ≤ od → 400 i `{\"blad\": \"…\"}`.\n"
        "- Logika wyłącznie z kalendarz.wolne_pokoje — bez kopiowania kodu do trasy.\n"
        "## Na co patrzeć przy integracji\n"
        "- Format danych na granicy modułów: daty jako napisy RRRR-MM-DD w API, `date` w środku kalendarza.\n"
        "- Wyjątki z niższych warstw (ValueError z noce/fromisoformat) zamieniane na 400 w jednym miejscu.\n"
        "- Stare testy (/api/cena) dalej zielone — integracja nie może psuć tego, co działało.\n"
        "## Co dalej\n"
        "Etap 3: bezpieczeństwo kodu i agenta, prawo, przegląd, dokumentacja, CI, praca z klientem i projekt końcowy — rozbudowa właśnie tej aplikacji."),
    przyklad=("@app.route(\"/api/wolne\")\ndef wolne():\n    od, do = request.args.get(\"od\"), request.args.get(\"do\")\n    try:\n        noce(od, do)                         # walidacja dat i kolejności\n"
              "        pokoje = wolne_pokoje(rezerwacje, od, do)\n    except (TypeError, ValueError):\n        return jsonify({\"blad\": \"podaj od i do jako RRRR-MM-DD, do po od\"}), 400\n"
              "    return jsonify({\"od\": od, \"do\": do, \"wolne\": pokoje})"),
    demonstracja={"tytul": "Integracja ujawnia błąd granicy modułów", "kroki": [
        "Agent dodał /api/wolne. Test z dobrymi datami — zielony.",
        "Test bez parametru `do`: 500 TypeError — noce(od, None) wywołało fromisoformat(None), a trasa łapała tylko ValueError.",
        "Poprawka: łapanie (TypeError, ValueError) w trasie — jeden punkt zamiany błędów na 400.",
        "Test daty „2026-13-01” → 400 ✔. Test /api/cena — nadal zielony ✔.",
        "Commit „Dodaj /api/wolne z walidacją dat (400)”, push."],
        "wynik": "Nowa trasa korzysta z gotowego modułu, wszystkie złe dane dają 400, stare funkcje działają — sprawdzone testami."},
    jak_uruchomic=["Zadanie tygodnia „/api/wolne” → „✔ Sprawdź wynik” (testy użyją create_app(rezerwacje=[…]))."],
    cwiczenia=[
        C("prowadzone",
          "Dla rezerwacji [Lipowy 20–23.12, Klonowy 22–27.12] podaj liczbę wolnych pokoi z odpowiedzi /api/wolne dla: (1) od=2026-12-21&do=2026-12-22, (2) od=2026-12-23&do=2026-12-25, (3) od=2026-12-25&do=2026-12-24 — tu podaj kod odpowiedzi. Czas: 15 minut.",
          "(1) 2 (Dębowy, Klonowy); (2) 2 (Lipowy, Dębowy — Klonowy zajęty do 27); (3) kod 400.",
          ["21–22: Lipowy zajęty, Klonowy od 22 — wolny w nocy 21/22.", "23–25: Lipowy wolny od 23, Klonowy zajęty.", "do przed od — złe dane."],
          "(1) Dębowy i Klonowy = 2; (2) Lipowy i Dębowy = 2; (3) do przed od → 400.",
          [li("w1", "(1) Wolne pokoje", 2), li("w2", "(2) Wolne pokoje", 2), li("k3", "(3) Kod odpowiedzi", 400)]),
        C("samodzielne",
          "Samoocena: ile pozycji z listy kontrolnej etapu 2 (9) oceniasz na „umiem” z dowodem? Wpisz liczbę (każda odpowiedź 0–9 jest poprawna jako samoocena — zapisz ją też w dzienniku). "
          "Pytanie kontrolne: jaki kod HTTP zwróci dobrze napisana trasa, gdy wyjątek z niższej warstwy wynika ze złych danych użytkownika? Czas: 15 minut.",
          "Samoocena 0–9; kod 400.",
          ["Licz tylko pozycje z dowodem (test, commit, plik).", "Złe dane użytkownika to nie błąd serwera.", "Lekcja Flask: tabela kodów."],
          "Samoocena dowolna z dowodami; złe dane użytkownika → 400.",
          [li("ile", "Pozycje „umiem” (0–9)", 9, tol=9), li("kod", "Kod dla złych danych", 400, bledy=[bl(500, "500 oznacza błąd serwera — złe dane użytkownika zamieniasz na 400")])]),
    ],
    typowe_bledy=[
        B("500 przy braku parametru.", "Łapany tylko ValueError, a None daje TypeError.", "Test bez parametru.", "Łap (TypeError, ValueError) albo sprawdź None jawnie."),
        B("Testy /api/cena czerwone po dodaniu /api/wolne.", "Zmieniona sygnatura create_app albo importy.", "Diff app.py.", "create_app(rezerwacje=None) z wartością domyślną — stare wywołania create_app() działają."),
    ],
    pulapki=["Nie kopiuj logiki kalendarza do trasy — dwie kopie rozjadą się przy pierwszej zmianie.", "Lista rezerwacji jako argument domyślny create_app(rezerwacje=[]) — pułapka mutowalnej wartości domyślnej; użyj None."],
    zadania=["Dodaj /api/wolne z testami (zadanie tygodnia).", "Samoocena etapu 2.", "Quiz tygodnia 11."],
    pytania=[["Gdzie zamieniasz wyjątki ze złych danych na 400?", "W jednym miejscu — w trasie, która przyjmuje dane od użytkownika."], ["Po co rezerwacje jako parametr create_app?", "Żeby testy mogły podać własne dane bez globalnego stanu."],
             ["Co sprawdzasz po integracji oprócz nowej trasy?", "Że stare testy (np. /api/cena) dalej przechodzą."]],
    podsumowanie="Połączyłeś kalendarz z aplikacją Flask w trasie z walidacją i testami, sprawdziłeś, że nic się nie zepsuło, i oceniłeś gotowość do etapu jakości.",
    test=[T("/api/wolne bez parametru „do” powinno zwrócić:", ["200", "400", "500", "404"], 1, "Złe dane."),
          T("create_app(rezerwacje=None) zamiast rezerwacje=[] chroni przed:", ["SQL injection", "Mutowalną wartością domyślną", "XSS", "Limitem tokenów"], 1, "Lekcja o debugowaniu."),
          T("Po dodaniu nowej trasy sprawdzasz:", ["Tylko nową trasę", "Nową trasę i wszystkie stare testy", "Nic", "Tylko wygląd"], 1, "Regresja.")],
    w_praktyce=["Integracja = testy na granicy modułów.", "Jeden punkt tłumaczenia wyjątków na kody HTTP."],
    zrodla=[Z_FLASK_QS, Z_FLASK_TEST, Z_CC_BEST],
)
