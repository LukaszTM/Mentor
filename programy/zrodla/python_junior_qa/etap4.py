# -*- coding: utf-8 -*-
"""Etap 4, tygodnie 10–12: projekt portfolio „Magazyn” — SQLite i plan projektu, Flask z formularzami i walidacją, testy aplikacji webowej
(test_client + Selenium), dokumentacja i rekrutacja, powtórka końcowa."""

from wspolne import B, C, L, T, bl, kod, li, tx, wy
import zrodla as Z

# =========================================================================== TYDZIEŃ 10
SQLITE = L(
    id="sqlite", nazwa="SQLite i plan projektu: tabele, CREATE/INSERT/SELECT/UPDATE/DELETE, zapytania z parametrami", tydzien=10,
    slowa=["SQLite", "baza danych", "SQL", "tabela", "CREATE TABLE", "INSERT", "SELECT", "WHERE", "ORDER BY", "UPDATE", "DELETE", "klucz główny", "sqlite3", "?", "SQL injection", "commit", "PLAN.md"],
    cel="Po tej lekcji planujesz zakres projektu w PLAN.md, tworzysz bazę SQLite z dwiema tabelami, wykonujesz zapytania CREATE, INSERT, SELECT (WHERE, ORDER BY), UPDATE i DELETE z modułu sqlite3 — zawsze z parametrami `?` — i testujesz kod bazy na bazie w pamięci albo w tmp_path.",
    po_co="Każda aplikacja trzyma dane w bazie, a tester sprawdza je zapytaniem SQL („czy zamówienie naprawdę się zapisało?”). Podstawy SQL są w większości ogłoszeń Junior QA.",
    wymagania=["Lekcje „Funkcje”, „Słowniki”, „Obsługa błędów”, „parametrize i fixtures”.", "sqlite3 jest w bibliotece standardowej Pythona — nic nie instalujesz."],
    wyjasnienie=(
        "## Plan projektu przed kodem (PLAN.md)\n"
        "Projekt portfolio to **Magazyn sklepu** „Papierowy Kot” (dane fikcyjne): produkty (nazwa, kategoria, cena, ilość) i operacje magazynowe (przyjęcie, wydanie, data). PLAN.md: cel w 2 zdaniach, zakres (co TAK, czego NIE), struktura plików, kolejność kroków (baza → logika → testy → web → testy E2E → README), ryzyka.\n"
        "## Baza, tabela, wiersz\n"
        "Baza SQLite to jeden plik (magazyn.db). Tabela jak arkusz: kolumny z typami, wiersze z danymi. **Klucz główny** (`id INTEGER PRIMARY KEY`) jednoznacznie identyfikuje wiersz — baza nadaje go sama.\n"
        "```\nCREATE TABLE IF NOT EXISTS produkty (\n    id INTEGER PRIMARY KEY,\n    nazwa TEXT NOT NULL UNIQUE,\n    kategoria TEXT NOT NULL,\n    cena REAL NOT NULL CHECK (cena >= 0),\n    ilosc INTEGER NOT NULL DEFAULT 0\n);\n```\n"
        "## Cztery podstawowe operacje (CRUD)\n"
        "| operacja | SQL |\n|---|---|\n"
        "| dodaj | `INSERT INTO produkty (nazwa, kategoria, cena) VALUES (?, ?, ?)` |\n"
        "| czytaj | `SELECT nazwa, cena FROM produkty WHERE kategoria = ? ORDER BY cena DESC` |\n"
        "| zmień | `UPDATE produkty SET ilosc = ilosc + ? WHERE id = ?` |\n"
        "| usuń | `DELETE FROM produkty WHERE id = ?` |\n"
        "## sqlite3 w Pythonie\n"
        "`con = sqlite3.connect(\"magazyn.db\")` (w testach `\":memory:\"` albo `tmp_path / \"test.db\"`), `con.execute(sql, (wartosci,))`, `con.commit()` — zapisuje zmiany; `cur.fetchall()` / `fetchone()` — wyniki. "
        "`con.row_factory = sqlite3.Row` — wiersze dostępne po nazwie kolumny jak słownik. Blok `with con:` sam robi commit (albo wycofanie przy błędzie).\n"
        "## Zawsze parametry `?` — nigdy f-string\n"
        "`f\"SELECT * FROM produkty WHERE nazwa = '{nazwa}'\"` dla nazwy `x' OR '1'='1` zwróci WSZYSTKIE wiersze — to **SQL injection** (OWASP: jedna z najgroźniejszych podatności). Z `?` sterownik bezpiecznie przekazuje wartość jako dane, nie jako kod SQL.\n"
        "## Testy bazy\n"
        "Fixture tworzy pustą bazę w tmp_path, wywołuje funkcję tworzącą tabele i oddaje połączenie; każdy test dostaje świeżą bazę. Testujesz: dodanie i odczyt, UNIQUE (duplikat → sqlite3.IntegrityError), wydanie więcej niż stan (ValueError z logiki), kolejność ORDER BY."),
    przyklad=kod("sqlite", (
        "import sqlite3\n\n"
        "con = sqlite3.connect(\":memory:\")\n"
        "con.row_factory = sqlite3.Row\n"
        "con.execute(\"\"\"CREATE TABLE produkty (\n"
        "    id INTEGER PRIMARY KEY, nazwa TEXT NOT NULL UNIQUE, kategoria TEXT NOT NULL,\n"
        "    cena REAL NOT NULL CHECK (cena >= 0), ilosc INTEGER NOT NULL DEFAULT 0)\"\"\")\n"
        "with con:\n"
        "    con.executemany(\"INSERT INTO produkty (nazwa, kategoria, cena, ilosc) VALUES (?, ?, ?, ?)\",\n"
        "                    [(\"Zeszyt A5\", \"zeszyty\", 4.5, 120), (\"Segregator A4\", \"biuro\", 11.9, 45), (\"Zszywacz\", \"biuro\", 19.9, 15)])\n"
        "for w in con.execute(\"SELECT nazwa, cena FROM produkty WHERE kategoria = ? ORDER BY cena DESC\", (\"biuro\",)):\n"
        "    print(w[\"nazwa\"], w[\"cena\"])\n"
        "with con:\n"
        "    con.execute(\"UPDATE produkty SET ilosc = ilosc - ? WHERE nazwa = ?\", (5, \"Zszywacz\"))\n"
        "print(\"Zszywacz:\", con.execute(\"SELECT ilosc FROM produkty WHERE nazwa = ?\", (\"Zszywacz\",)).fetchone()[\"ilosc\"])\n"
        "try:\n"
        "    with con:\n"
        "        con.execute(\"INSERT INTO produkty (nazwa, kategoria, cena) VALUES (?, ?, ?)\", (\"Zeszyt A5\", \"zeszyty\", 4.5))\n"
        "except sqlite3.IntegrityError as e:\n"
        "    print(\"Duplikat:\", e)\n"
        "zla = \"x' OR '1'='1\"\n"
        "print(\"f-string:\", len(con.execute(f\"SELECT * FROM produkty WHERE nazwa = '{zla}'\").fetchall()), \"wierszy\")\n"
        "print(\"parametr ?:\", len(con.execute(\"SELECT * FROM produkty WHERE nazwa = ?\", (zla,)).fetchall()), \"wierszy\")\n"), (
        "Zszywacz 19.9\nSegregator A4 11.9\nZszywacz: 10\nDuplikat: UNIQUE constraint failed: produkty.nazwa\nf-string: 3 wierszy\nparametr ?: 0 wierszy\n")),
    demonstracja={"tytul": "Magazyn w bazie: tabela, CRUD i lekcja o SQL injection", "kroki": [
        "`sqlite3.connect(\":memory:\")` — baza w pamięci (znika po zakończeniu) — idealna do przykładów i testów. W projekcie: `\"magazyn.db\"`.",
        "`row_factory = sqlite3.Row` — `w[\"nazwa\"]` zamiast `w[0]`.",
        "CREATE TABLE z ograniczeniami: NOT NULL, UNIQUE (nazwa nie może się powtórzyć), CHECK (cena ≥ 0), DEFAULT 0.",
        "`with con:` + `executemany` — trzy INSERT-y w jednej transakcji, commit automatycznie.",
        "SELECT z WHERE i ORDER BY cena DESC — produkty z kategorii biuro od najdroższego. Wartość kategorii przekazana jako parametr `?` w krotce `(\"biuro\",)` (przecinek = krotka jednoelementowa!).",
        "UPDATE `ilosc = ilosc - ?` — zmiana względem obecnej wartości; 15 − 5 = 10.",
        "Drugi „Zeszyt A5” → IntegrityError z UNIQUE — baza pilnuje reguły nawet, gdy kod zapomni.",
        "SQL injection: f-string zamienia dane w kod SQL i warunek `OR '1'='1'` zwraca wszystkie 3 wiersze; z `?` — 0 wierszy (szukana jest nazwa dosłownie)."],
        "wynik": "Dwa produkty biurowe od najdroższego, „Zszywacz: 10”, komunikat UNIQUE i porównanie 3 wierszy (f-string) vs 0 (parametr)."},
    jak_uruchomic=["Zapisz jako baza_demo.py → ▶ Uruchom.", "Podgląd pliku bazy (opcjonalnie): DB Browser for SQLite (sqlitebrowser.org) albo w terminalu Pythona `sqlite3.connect(\"magazyn.db\").execute(\"SELECT * FROM produkty\").fetchall()`."],
    cwiczenia=[
        C("prowadzone",
          "Tabela produkty z demonstracji (stan po UPDATE). Podaj wynik: (1) `SELECT COUNT(*) FROM produkty` , (2) `SELECT nazwa FROM produkty ORDER BY cena LIMIT 1`, (3) `SELECT SUM(ilosc) FROM produkty WHERE kategoria = 'biuro'`. Czas: 15 minut.",
          "(1) 3; (2) Zeszyt A5; (3) 55.",
          ["Duplikat nie został dodany.", "ORDER BY cena rośnie, LIMIT 1 — najtańszy.", "Biuro: segregator 45 + zszywacz 10."],
          "(1) 3 wiersze; (2) Zeszyt A5 (4.5); (3) 45 + 10 = 55.",
          [li("a", "(1) COUNT", 3, bledy=[bl(4, "drugi Zeszyt A5 odrzuciło UNIQUE — nie ma go w tabeli")]), tx("b", "(2) Najtańszy", "Zeszyt A5"), li("c", "(3) SUM biuro", 55, bledy=[bl(60, "zszywaczy jest już 10 (UPDATE −5)")])]),
        C("samodzielne",
          "Kolega napisał: `def znajdz(con, nazwa): return con.execute(f\"SELECT * FROM produkty WHERE nazwa = '{nazwa}'\").fetchall()`. (1) Czy to podatne na SQL injection (tak/nie)? (2) Wpisz poprawioną linię return. (3) Co zwróci poprawiona funkcja dla nazwy „Zeszyt A5' --”: wszystkie / pustą listę? (4) Jaki wyjątek rzuci INSERT z ceną -1 przy CHECK (cena >= 0) — wybierz. Czas: 15 minut.",
          "(1) tak; (2) return con.execute(\"SELECT * FROM produkty WHERE nazwa = ?\", (nazwa,)).fetchall(); (3) pustą listę; (4) sqlite3.IntegrityError.",
          ["Dane wklejone w tekst SQL stają się kodem.", "Znak zapytania i krotka z wartością.", "Ograniczenia tabeli zgłaszają IntegrityError."],
          "(1) tak; (2) `return con.execute(\"SELECT * FROM produkty WHERE nazwa = ?\", (nazwa,)).fetchall()`; (3) pustą listę — nie ma produktu o takiej dosłownej nazwie; (4) `sqlite3.IntegrityError: CHECK constraint failed`.",
          [wy("a", "(1) Podatne?", ["tak", "nie"], "tak"), tx("b", "(2) Poprawiona linia", "return con.execute(\"SELECT * FROM produkty WHERE nazwa = ?\", (nazwa,)).fetchall()", zawiera=["?", "(nazwa,)"]),
           wy("c", "(3) Wynik", ["wszystkie", "pustą listę"], "pustą listę"), wy("d", "(4) Wyjątek", ["ValueError", "sqlite3.IntegrityError", "TypeError", "KeyError"], "sqlite3.IntegrityError")]),
    ],
    typowe_bledy=[
        B("Dane „znikają” po zamknięciu programu", "Brak con.commit() (albo with con:).", "Czy po INSERT/UPDATE jest commit?", "`with con:` wokół zmian albo con.commit()."),
        B("sqlite3.OperationalError: no such table: produkty", "Tabela nie utworzona albo inny plik bazy (np. inny katalog roboczy).", "Ścieżka do pliku .db.", "CREATE TABLE IF NOT EXISTS przy starcie; ścieżka względem pliku programu."),
        B("sqlite3.ProgrammingError: Incorrect number of bindings supplied", "`(\"biuro\")` to napis, nie krotka.", "Czy po pojedynczej wartości jest przecinek?", "`(\"biuro\",)`."),
    ],
    pulapki=["f-string w SQL — SQL injection; zawsze `?`.", "Testy na prawdziwym magazyn.db — testy zmieniają dane; zawsze :memory: albo tmp_path."],
    zadania=["PLAN.md: cel, zakres TAK/NIE, struktura, kolejność, ryzyka.", "baza.py: utworz_baze, dodaj_produkt, pobierz_produkty, zmien_ilosc, usun_produkt — z parametrami ?.", "Testy bazy z fixturą tworzącą bazę w tmp_path."],
    pytania=[["Po co klucz główny?", "Jednoznacznie identyfikuje wiersz."], ["Jak bronisz się przed SQL injection?", "Zapytania parametryzowane (?), nigdy f-string z danymi."], ["Co robi with con:?", "Commit po bloku albo wycofanie zmian przy błędzie."]],
    podsumowanie="Planujesz projekt, tworzysz tabele z ograniczeniami, wykonujesz CRUD w sqlite3 z parametrami ?, rozumiesz SQL injection i testujesz bazę na danych tymczasowych.",
    test=[T("Zapytanie bezpieczne przed SQL injection:", ["f\"…WHERE id = {id}\"", "\"…WHERE id = ?\" z (id,)", "\"…WHERE id = \" + str(id)", "żadne"], 1, "Parametry."),
          T("SELECT … ORDER BY cena DESC zwraca:", ["od najtańszego", "od najdroższego", "losowo", "tylko najdroższy"], 1, "DESC = malejąco."),
          T("Zmiany po INSERT trafiają do pliku bazy po:", ["SELECT", "commit", "close bez commit", "print"], 1, "Transakcja."),
          T("Baza w testach jednostkowych:", ["produkcyjna magazyn.db", ":memory: albo tmp_path", "na serwerze", "w README"], 1, "Izolacja testów.")],
    w_praktyce=["Tester po akcji w aplikacji sprawdza SELECT-em, czy dane zapisały się poprawnie.", "W bug raporcie dotyczącym danych: zapytanie SQL i wynik."],
    zrodla=[Z.PY_SQLITE, Z.OWASP_SQLI, Z.OWASP_QP, Z.PYTEST_TMP],
)

# =========================================================================== TYDZIEŃ 11
FLASK = L(
    id="flask", nazwa="Flask: strony, szablony, formularze z walidacją i komunikaty", tydzien=11,
    slowa=["Flask", "trasa", "route", "@app.route", "GET", "POST", "render_template", "Jinja", "request.form", "redirect", "url_for", "walidacja", "flash", "debug", "port"],
    cel="Po tej lekcji tworzysz aplikację Flask z trasami GET i POST, wyświetlasz dane z bazy w szablonie, przyjmujesz formularz (request.form), walidujesz dane po stronie serwera z czytelnymi komunikatami i przekierowujesz po zapisie (redirect).",
    po_co="Interfejs webowy zamienia projekt z konsoli w aplikację, którą rekruter kliknie; a Ty — przetestujesz w przeglądarce Selenium, jak prawdziwy system.",
    wymagania=["Lekcja „SQLite” i moduły projektu Magazyn (baza.py, magazyn.py).", "Flask jest w środowisku kursu (Flask 3.1).", "Podstawy HTML: znaczniki, formularz — wyjaśnione w lekcji."],
    wyjasnienie=(
        "## Minimalna aplikacja\n"
        "```\nfrom flask import Flask\napp = Flask(__name__)\n\n@app.route(\"/\")\ndef index():\n    return \"<h1>Magazyn</h1>\"\n\nif __name__ == \"__main__\":\n    app.run(port=5000, debug=True)\n```\n"
        "`@app.route(\"/\")` — pod adresem / (strona główna) Flask wywoła funkcję index i odeśle to, co zwróci. `python app.py` → http://127.0.0.1:5000. `debug=True` przeładowuje aplikację po zapisie pliku i pokazuje błędy — tylko lokalnie, nigdy na serwerze publicznym.\n"
        "## Szablony (Jinja)\n"
        "Pliki HTML w katalogu `templates/`. `render_template(\"index.html\", produkty=lista)` przekazuje dane; w szablonie: `{{ p.nazwa }}` wstawia wartość (Flask automatycznie zabezpiecza znaki HTML), `{% for p in produkty %} … {% endfor %}` — pętla, `{% if blad %} … {% endif %}` — warunek.\n"
        "## Formularz: GET pokazuje, POST zapisuje\n"
        "```\n@app.route(\"/dodaj\", methods=[\"GET\", \"POST\"])\ndef dodaj():\n    if request.method == \"POST\":\n        nazwa = request.form.get(\"nazwa\", \"\").strip()\n        ...\n        return redirect(url_for(\"index\"))\n    return render_template(\"dodaj.html\")\n```\n"
        "W HTML: `<form method=\"post\"><input name=\"nazwa\" id=\"nazwa\"> <button data-test=\"zapisz\">Zapisz</button></form>` — atrybut **name** to klucz w request.form; **id** i **data-test** przydadzą się w Selenium.\n"
        "## Walidacja po stronie serwera\n"
        "Atrybut `required` w HTML można obejść (Selenium, curl, DevTools) — reguły sprawdzasz zawsze w Pythonie: puste pole, cena nie-liczba albo ujemna, ilość niecałkowita. Przy błędzie: ten sam formularz z komunikatem i wpisanymi wartościami, kod **400**; przy sukcesie: zapis i `redirect` (wzorzec Post/Redirect/Get — odświeżenie strony nie doda produktu drugi raz).\n"
        "## Trasy z parametrem\n"
        "`@app.route(\"/produkt/<int:pid>\")` → `def produkt(pid):` — strona jednego produktu z historią operacji; brak produktu → `abort(404)`.\n"
        "## Porty\n"
        "Sklep testowy z paczki działa na 5001, Twój Magazyn na 5000 — mogą działać jednocześnie. „Address already in use” = port zajęty przez inny proces."),
    przyklad=kod("flask", (
        "from flask import Flask, redirect, render_template_string, request, url_for\n\n"
        "app = Flask(__name__)\n"
        "PRODUKTY = [{\"nazwa\": \"Zeszyt A5\", \"cena\": 4.5}]\n"
        "STRONA = \"\"\"<h1>Magazyn</h1>\n"
        "{% if blad %}<p data-test=\"blad\">{{ blad }}</p>{% endif %}\n"
        "<ul>{% for p in produkty %}<li class=\"produkt\">{{ p.nazwa }} — {{ '%.2f'|format(p.cena) }} zł</li>{% endfor %}</ul>\n"
        "<form method=\"post\"><input name=\"nazwa\" value=\"{{ nazwa }}\"><input name=\"cena\"><button data-test=\"zapisz\">Zapisz</button></form>\"\"\"\n\n\n"
        "@app.route(\"/\", methods=[\"GET\", \"POST\"])\n"
        "def index():\n"
        "    if request.method == \"POST\":\n"
        "        nazwa = request.form.get(\"nazwa\", \"\").strip()\n"
        "        try:\n"
        "            cena = float(request.form.get(\"cena\", \"\").replace(\",\", \".\"))\n"
        "        except ValueError:\n"
        "            cena = None\n"
        "        if not nazwa:\n"
        "            blad = \"Podaj nazwę produktu\"\n"
        "        elif cena is None or cena < 0:\n"
        "            blad = \"Cena musi być liczbą nieujemną\"\n"
        "        else:\n"
        "            PRODUKTY.append({\"nazwa\": nazwa, \"cena\": cena})\n"
        "            return redirect(url_for(\"index\"))\n"
        "        return render_template_string(STRONA, produkty=PRODUKTY, blad=blad, nazwa=nazwa), 400\n"
        "    return render_template_string(STRONA, produkty=PRODUKTY, blad=None, nazwa=\"\")\n\n\n"
        "klient = app.test_client()\n"
        "print(klient.get(\"/\").status_code)\n"
        "odp = klient.post(\"/\", data={\"nazwa\": \"Klej\", \"cena\": \"3,40\"})\n"
        "print(odp.status_code, odp.headers[\"Location\"])\n"
        "odp = klient.post(\"/\", data={\"nazwa\": \"\", \"cena\": \"5\"})\n"
        "print(odp.status_code, \"Podaj nazwę produktu\" in odp.get_data(as_text=True))\n"
        "odp = klient.post(\"/\", data={\"nazwa\": \"<b>X</b>\", \"cena\": \"-1\"})\n"
        "print(odp.status_code, \"&lt;b&gt;X&lt;/b&gt;\" in odp.get_data(as_text=True))\n"
        "print([p[\"nazwa\"] for p in PRODUKTY])\n"), "200\n302 /\n400 True\n400 True\n['Zeszyt A5', 'Klej']\n"),
    demonstracja={"tytul": "Strona z listą i formularzem — sprawdzona bez przeglądarki", "kroki": [
        "`Flask(__name__)` — aplikacja; `PRODUKTY` — lista w pamięci (w projekcie: baza SQLite przez baza.py).",
        "`render_template_string` — szablon w napisie, żeby przykład był jednym plikiem; w projekcie `render_template(\"index.html\")` z katalogu templates/.",
        "Szablon: `{% if blad %}` komunikat z data-test, pętla `{% for %}` po produktach, `'%.2f'|format` — 2 miejsca po przecinku, `value=\"{{ nazwa }}\"` — wpisana nazwa wraca do pola po błędzie.",
        "`methods=[\"GET\", \"POST\"]` — GET pokazuje stronę, POST przyjmuje formularz.",
        "Walidacja w Pythonie: pusta nazwa, cena nie-liczba (przecinek zamieniony na kropkę — polscy użytkownicy!), cena ujemna.",
        "Sukces → `redirect(url_for(\"index\"))` = kod 302 i nagłówek Location: /. Błąd → strona z komunikatem i kod 400.",
        "`app.test_client()` — Flask wysyła żądania bez serwera i przeglądarki: tak piszesz szybkie testy aplikacji webowej (następna lekcja).",
        "`<b>X</b>` w nazwie wraca jako `&lt;b&gt;X&lt;/b&gt;` — Jinja zabezpiecza HTML (ochrona przed XSS)."],
        "wynik": "200, „302 /”, „400 True” dwa razy i lista ['Zeszyt A5', 'Klej'] — klej dodany, dwa złe formularze odrzucone."},
    jak_uruchomic=["Zapisz jako flask_demo.py → ▶ Uruchom (test_client działa bez przeglądarki).",
                   "Jako serwer: zamień 6 ostatnich linii na `app.run(port=5000, debug=True)` → `python flask_demo.py` → http://127.0.0.1:5000 → Ctrl+C kończy."],
    cwiczenia=[
        C("prowadzone",
          "Na wzór demonstracji: jakie kody odpowiedzi zwróci aplikacja dla POST: (1) nazwa „Gumka”, cena „1.50”; (2) nazwa „Gumka”, cena „abc”; (3) nazwa „  ”, cena „2”; (4) GET /? Czas: 10 minut.",
          "(1) 302; (2) 400; (3) 400; (4) 200.",
          ["Sukces kończy się przekierowaniem.", "float(\"abc\") → ValueError → komunikat.", "strip() z samych spacji daje pusty napis."],
          "(1) 302 — zapis i redirect; (2) 400 — cena nie-liczba; (3) 400 — po strip() nazwa pusta; (4) 200.",
          [li("a", "(1) poprawne dane", 302, bledy=[bl(200, "po zapisie aplikacja PRZEKIEROWUJE (Post/Redirect/Get) — 302")]), li("b", "(2) cena abc", 400), li("c", "(3) nazwa ze spacji", 400), li("d", "(4) GET", 200)]),
        C("samodzielne",
          "Formularz ma `<input name=\"ilosc\" type=\"number\" min=\"1\" required>`. (1) Czy to wystarczy, żeby serwer nie przyjął ilości 0 (tak/nie)? (2) Jak tester to sprawdzi bez przeglądarki — wybierz: test_client.post z ilosc=0 / zmiana CSS. (3) Jaki kod odpowiedzi powinien dostać przy ilości 0, a jaki przy błędzie w kodzie serwera (dwa kody po przecinku)? Czas: 15 minut.",
          "(1) nie; (2) test_client.post z ilosc=0; (3) 400, 500.",
          ["Atrybuty HTML sprawdza przeglądarka, nie serwer.", "Żądanie można wysłać z pominięciem formularza.", "Złe dane klienta to 4xx, błąd serwera to 5xx."],
          "(1) nie — required/min działa tylko w przeglądarce, serwer musi walidować sam; (2) `test_client.post(\"/dodaj\", data={\"ilosc\": \"0\"})`; (3) 400 dla złych danych, 500 oznacza defekt serwera.",
          [wy("a", "(1) HTML wystarczy?", ["tak", "nie"], "nie"), wy("b", "(2) Jak sprawdzić", ["test_client.post z ilosc=0", "zmiana CSS"], "test_client.post z ilosc=0"), tx("c", "(3) Kody", "400, 500")]),
    ],
    typowe_bledy=[
        B("jinja2.exceptions.TemplateNotFound: index.html", "Szablon nie leży w katalogu templates/ obok app.py.", "Struktura katalogów.", "templates/index.html w katalogu aplikacji."),
        B("405 Method Not Allowed po wysłaniu formularza", "Trasa bez methods=[\"GET\", \"POST\"].", "Dekorator @app.route.", "Dodaj methods=[\"GET\", \"POST\"]."),
        B("OSError: [Errno 98/10048] Address already in use", "Port zajęty (druga kopia aplikacji albo inny program).", "Czy aplikacja działa w innym oknie?", "Zamknij poprzednią (Ctrl+C) albo użyj innego portu."),
        B("KeyError / BadRequest: The browser sent a request that this server could not understand", "request.form[\"pole\"] dla pola, którego nie ma w formularzu.", "Nazwy name w HTML.", "request.form.get(\"pole\", \"\") i zgodne atrybuty name."),
    ],
    pulapki=["Walidacja tylko w HTML/JavaScript — serwer musi sprawdzać sam.", "debug=True na serwerze dostępnym z internetu — konsola debugera pozwala wykonać kod."],
    zadania=["Strona główna z listą produktów z bazy.", "Formularz dodawania produktu z walidacją i komunikatami.", "Strona produktu z historią operacji; 404 dla nieistniejącego."],
    pytania=[["Po co redirect po zapisie formularza?", "Odświeżenie strony nie wyśle formularza drugi raz (Post/Redirect/Get)."], ["Dlaczego walidacja w Pythonie, skoro jest required?", "Atrybuty HTML da się obejść; serwer jest ostatnią linią obrony."], ["Gdzie Flask szuka szablonów?", "W katalogu templates/ obok aplikacji."]],
    podsumowanie="Budujesz aplikację Flask z trasami, szablonami, formularzem z walidacją po stronie serwera, przekierowaniem po zapisie i stroną z parametrem.",
    test=[T("Kod odpowiedzi po udanym zapisie z redirect:", ["200", "302", "400", "500"], 1, "Przekierowanie."),
          T("Wartość pola formularza o name=\"cena\":", ["request.args[\"cena\"]", "request.form.get(\"cena\")", "form.cena", "request.cena"], 1, "Dane POST w request.form."),
          T("Jinja przy {{ nazwa }} z <script>:", ["wykona skrypt", "zabezpieczy znaki HTML", "usunie nazwę", "rzuci błąd"], 1, "Autoescaping chroni przed XSS."),
          T("Atrybut required w HTML:", ["chroni serwer", "działa tylko w przeglądarce", "jest zbędny", "zastępuje testy"], 1, "Serwer waliduje sam.")],
    w_praktyce=["Testując formularz: puste pola, spacje, przecinek w liczbie, wartości ujemne, bardzo długi tekst, HTML w polu — i obejście walidacji przeglądarki.", "Każdy formularz = atrybuty id/data-test dla testów Selenium."],
    zrodla=[Z.FLASK, Z.OWASP_SQLI],
)

TESTY_APLIKACJI = L(
    id="testy_aplikacji", nazwa="Testy aplikacji webowej: Flask test_client, testy E2E Selenium własnej aplikacji i CI", tydzien=11,
    slowa=["test_client", "testy integracyjne", "testy E2E", "fixture app", "serwer testowy", "wątek", "baza testowa", "headless", "CI", "regresja"],
    cel="Po tej lekcji testujesz własną aplikację Flask na dwóch poziomach: szybkie testy z test_client (strony, formularze, kody odpowiedzi, baza tymczasowa) i kilka testów E2E w Selenium z Page Object Model na serwerze uruchomionym w fixturze — i łączysz je w CI.",
    po_co="To jest serce projektu portfolio: aplikacja i jej testy na kilku poziomach, zielone w CI. Na rozmowie pokażesz piramidę testów na własnym kodzie.",
    wymagania=["Lekcje „Flask”, „WebDriverWait i POM”, „GitHub Actions”.", "Aplikacja Magazyn z funkcją tworzącą aplikację (create_app) albo modułem app.py."],
    wyjasnienie=(
        "## Aplikacja do testów: fabryka z konfiguracją\n"
        "Testy nie mogą psuć prawdziwej bazy. Wzorzec: `def create_app(sciezka_bazy=\"magazyn.db\"):` tworzy aplikację dla podanej bazy. W testach: `create_app(tmp_path / \"test.db\")`.\n"
        "## Poziom 1: test_client (szybko, bez przeglądarki)\n"
        "```\n@pytest.fixture\ndef klient(tmp_path):\n    app = create_app(tmp_path / \"test.db\")\n    return app.test_client()\n\ndef test_dodanie_produktu(klient):\n    odp = klient.post(\"/dodaj\", data={\"nazwa\": \"Klej\", \"kategoria\": \"biuro\", \"cena\": \"3.40\", \"ilosc\": \"10\"})\n    assert odp.status_code == 302\n    assert \"Klej\" in klient.get(\"/\").get_data(as_text=True)\n```\n"
        "Sprawdzasz: kody (200/302/400/404), treść strony, komunikaty walidacji, stan bazy po operacji. Dziesiątki takich testów wykonują się w sekundę.\n"
        "## Poziom 2: E2E w Selenium (mało, ścieżki krytyczne)\n"
        "Fixture uruchamia serwer w wątku na wolnym porcie (`werkzeug.serving.make_server`), Selenium otwiera przeglądarkę w trybie headless, po teście wszystko zamyka. Page Objecty: `ListaPage`, `DodajPage`, `ProduktPage`. 3 testy: lista się wyświetla, dodanie produktu formularzem, historia produktu.\n"
        "## CI\n"
        "W tests.yml najpierw szybkie testy (`pytest tests/unit`), potem E2E (`pytest tests/e2e`) — przy czerwonych jednostkowych nie ma sensu czekać na przeglądarkę. ubuntu-latest ma Chrome; fixture wybiera `webdriver.Chrome` z `--headless=new`, gdy działa w CI (zmienna środowiskowa `CI=true`).\n"
        "## Co pokazać rekruterowi\n"
        "Liczby (np. 25 testów jednostkowych/integracyjnych, 3 E2E), zielone CI, raport HTML jako artefakt i sekcję „Jak testuję” w README."),
    przyklad=kod("testy_aplikacji", (
        "# tests/conftest.py (fragment) — serwer aplikacji w wątku dla testów E2E\n"
        "import os\n"
        "import threading\n\n"
        "import pytest\n"
        "from selenium import webdriver\n"
        "from werkzeug.serving import make_server\n\n"
        "from app import create_app\n\n\n"
        "@pytest.fixture\n"
        "def klient(tmp_path):\n"
        "    return create_app(tmp_path / \"test.db\").test_client()\n\n\n"
        "@pytest.fixture\n"
        "def serwer(tmp_path):\n"
        "    app = create_app(tmp_path / \"e2e.db\")\n"
        "    srv = make_server(\"127.0.0.1\", 0, app)\n"
        "    threading.Thread(target=srv.serve_forever, daemon=True).start()\n"
        "    yield f\"http://127.0.0.1:{srv.server_port}\"\n"
        "    srv.shutdown()\n\n\n"
        "@pytest.fixture\n"
        "def driver():\n"
        "    if os.environ.get(\"CI\"):\n"
        "        opcje = webdriver.ChromeOptions()\n"
        "        opcje.add_argument(\"--headless=new\")\n"
        "        d = webdriver.Chrome(options=opcje)\n"
        "    else:\n"
        "        opcje = webdriver.EdgeOptions()\n"
        "        opcje.add_argument(\"--headless=new\")\n"
        "        d = webdriver.Edge(options=opcje)\n"
        "    yield d\n"
        "    d.quit()\n"), None),
    demonstracja={"tytul": "Fixtury dla dwóch poziomów testów", "kroki": [
        "`klient(tmp_path)` — aplikacja na świeżej bazie w katalogu tymczasowym i jej test_client: testy jednostkowo-integracyjne bez sieci i przeglądarki.",
        "`serwer(tmp_path)` — `make_server(\"127.0.0.1\", 0, app)` z Werkzeug (instalowany razem z Flaskiem); port 0 = wolny port; wątek obsługuje żądania w tle.",
        "`yield` adresu → test dostaje np. http://127.0.0.1:53187; po teście `shutdown()` zatrzymuje serwer.",
        "`driver` — w CI (zmienna CI ustawiana przez GitHub Actions) Chrome headless, lokalnie Edge headless; po teście quit.",
        "Test E2E prosi o oba: `def test_dodanie(serwer, driver): DodajPage(driver, serwer).open().dodaj(\"Klej\", \"biuro\", \"3.40\", \"10\")` i sprawdza, że lista zawiera „Klej”.",
        "Każdy test ma własną bazę — kolejność testów nie ma znaczenia."],
        "wynik": "Testy test_client wykonują się w ułamku sekundy; 3 testy E2E po kilka sekund; oba poziomy zielone lokalnie i w CI."},
    jak_uruchomic=["Struktura: app.py (create_app), tests/conftest.py, tests/test_app.py (test_client), tests/test_e2e.py (Selenium), pages/ (Page Objecty).",
                   "Lokalnie: `python -m pytest -v tests` (Edge).", "CI: w tests.yml dwa kroki — `pytest tests/test_app.py`, potem `pytest tests/test_e2e.py`."],
    cwiczenia=[
        C("prowadzone",
          "Na wzór demonstracji dobierz fixturę (klient / serwer + driver): (1) test, że POST /dodaj z pustą nazwą daje 400; (2) test, że po kliknięciu „Zapisz” w przeglądarce produkt pojawia się na liście; (3) test, że GET /produkt/999 daje 404. Ile testów będzie wymagać przeglądarki? Czas: 10 minut.",
          "(1) klient; (2) serwer + driver; (3) klient; przeglądarki wymaga 1 test.",
          ["Kody odpowiedzi i treść strony sprawdzi test_client.", "Kliknięcie w przeglądarce wymaga Selenium.", "Przeglądarka tylko dla ścieżki użytkownika."],
          "(1) klient; (2) serwer + driver; (3) klient; tylko 1 test wymaga przeglądarki — reszta jest szybka.",
          [wy("a", "(1) 400 dla pustej nazwy", ["klient", "serwer + driver"], "klient"), wy("b", "(2) kliknięcie Zapisz", ["klient", "serwer + driver"], "serwer + driver"),
           wy("c", "(3) 404", ["klient", "serwer + driver"], "klient"), li("d", "Testy z przeglądarką", 1)]),
        C("samodzielne",
          "Testy E2E przechodzą lokalnie, ale w CI padają z `SessionNotCreatedException`. (1) Najbardziej prawdopodobna przyczyna (wybierz)? (2) Testy jednostkowe dodają produkty do prawdziwego magazyn.db i drugi przebieg pada na UNIQUE — co zmieniasz (wybierz)? (3) W jakiej kolejności uruchamiasz w CI poziomy testów (wybierz)? Czas: 15 minut.",
          "(1) przeglądarka bez trybu headless / Edge niedostępny na ubuntu; (2) baza w tmp_path przez create_app; (3) najpierw szybkie (test_client), potem E2E.",
          ["Serwer CI nie ma ekranu ani Edge.", "Każdy test potrzebuje świeżej bazy.", "Szybka informacja zwrotna najpierw."],
          "(1) na ubuntu-latest: Chrome headless zamiast Edge z oknem; (2) `create_app(tmp_path / \"test.db\")` w fixturze; (3) test_client → E2E.",
          [wy("a", "(1) Przyczyna", ["za mało testów", "przeglądarka bez trybu headless / Edge niedostępny na ubuntu", "zły README"], "przeglądarka bez trybu headless / Edge niedostępny na ubuntu"),
           wy("b", "(2) Zmiana", ["usuwam UNIQUE", "baza w tmp_path przez create_app", "kasuję magazyn.db ręcznie"], "baza w tmp_path przez create_app"),
           wy("c", "(3) Kolejność", ["najpierw E2E, potem szybkie", "najpierw szybkie (test_client), potem E2E"], "najpierw szybkie (test_client), potem E2E")]),
    ],
    typowe_bledy=[
        B("Testy zmieniają prawdziwe dane", "Aplikacja na stałe łączy się z magazyn.db.", "Czy create_app przyjmuje ścieżkę bazy?", "Fabryka aplikacji z parametrem i tmp_path w fixturze."),
        B("Test E2E czasem pada: element nie znaleziony", "Brak czekania po przeładowaniu strony.", "Zrzut ekranu przy błędzie.", "WebDriverWait w metodach Page Objectów."),
    ],
    pulapki=["Dziesiątki testów E2E dla każdej walidacji — reguły testuj test_clientem.", "Serwer testowy na stałym porcie 5000 — kolizja z działającą aplikacją; port 0."],
    zadania=["Testy test_client: lista, dodanie, walidacja (400), 404.", "3 testy Selenium w POM na serwerze z fixtury.", "Oba poziomy w GitHub Actions — zielone."],
    pytania=[["Czym różni się test z test_client od testu Selenium?", "test_client wysyła żądania bez przeglądarki (szybko); Selenium klika w prawdziwej przeglądarce (wolniej, pełna ścieżka)."],
             ["Po co create_app(ścieżka_bazy)?", "Żeby testy używały tymczasowej bazy."], ["Dlaczego najpierw szybkie testy w CI?", "Szybka informacja o błędzie; E2E nie ma sensu przy czerwonych jednostkowych."]],
    podsumowanie="Testujesz własną aplikację na dwóch poziomach (test_client i Selenium z POM), izolujesz dane bazą tymczasową i uruchamiasz całość w CI.",
    test=[T("test_client Flask:", ["otwiera przeglądarkę", "wysyła żądania do aplikacji bez serwera i przeglądarki", "testuje CSS", "instaluje Flask"], 1, "Szybkie testy webowe."),
          T("Serwer testowy na porcie 0 oznacza:", ["port 80", "wolny port wybrany przez system", "błąd", "brak sieci"], 1, "Unikasz kolizji."),
          T("Ile testów E2E w projekcie portfolio?", ["każda reguła", "kilka krytycznych ścieżek", "zero", "100+"], 1, "Piramida."),
          T("Testy E2E w CI na ubuntu-latest:", ["Edge z oknem", "Chrome headless", "tylko ręcznie", "nie da się"], 1, "Brak ekranu.")],
    w_praktyce=["W README sekcja „Jak testuję”: poziomy, liczba testów, jak uruchomić, link do CI.", "Każdy znaleziony defekt w aplikacji → test test_client odtwarzający go."],
    zrodla=[Z.FLASK, Z.SEL_POM, Z.GH_ACTIONS_PY, Z.PYTEST_FIX],
)

# =========================================================================== TYDZIEŃ 12
REKRUTACJA = L(
    id="rekrutacja", nazwa="CV, opowieść o projekcie i rozmowa rekrutacyjna Junior QA", tydzien=12,
    slowa=["CV", "portfolio", "rekrutacja", "rozmowa", "Junior QA", "opowieść o projekcie", "STAR", "pytania techniczne", "zadanie rekrutacyjne", "LinkedIn", "widełki", "jawność wynagrodzeń", "ISTQB"],
    cel="Po tej lekcji masz jednostronicowe CV z sekcją Projekty na górze, 2-minutową opowieść o projekcie (problem → rozwiązanie → jak testuję → czego się nauczyłem), odpowiedzi na typowe pytania techniczne i miękkie (metoda STAR) oraz plan wysyłania aplikacji.",
    po_co="Rynek juniorski jest trudny (w I kwartale 2026 oferty juniorskie to ok. 5% ogłoszeń w justjoin.it) — wygrywa kandydat, który pokazuje działający projekt z testami i umie o nim mówić konkretnie.",
    wymagania=["Projekt Magazyn na GitHubie z README, testami i zielonym CI.", "Repozytorium testów sklepu testowego (tydzień 9).", "Lekcje etapu 3 (słownictwo testowania)."],
    wyjasnienie=(
        "## CV na 1 stronę (PDF)\n"
        "1. Nagłówek: imię i nazwisko, miasto (opcjonalnie), e-mail, link do GitHuba i LinkedIn. Bez zdjęcia z wakacji, PESEL-u, daty urodzenia.\n"
        "2. **Projekty — na górze** (przed doświadczeniem, jeśli zmieniasz branżę): nazwa + link, 1 zdanie co robi, technologie, liczby: „Magazyn — Python, SQLite, Flask; 28 testów pytest, 3 testy E2E Selenium (POM), CI GitHub Actions”.\n"
        "3. Umiejętności: Python, pytest, Selenium WebDriver, Git/GitHub, GitHub Actions, SQL (podstawy), projektowanie przypadków testowych (klasy równoważności, wartości brzegowe), raporty błędów, API (requests).\n"
        "4. Doświadczenie: także spoza IT — opisuj **kompetencje przydatne w QA**: dokładność, procedury, kontrola jakości, kontakt z klientem.\n"
        "5. Klauzula zgody na przetwarzanie danych — gdy wymaga jej ogłoszenie.\n"
        "## Opowieść o projekcie (2 minuty)\n"
        "**Problem** (jedno zdanie) → **rozwiązanie** (co robi aplikacja, technologie) → **jak testuję** (poziomy, techniki, CI, przykład znalezionego defektu) → **czego się nauczyłem** (konkretnie). Nagraj się telefonem, odsłuchaj, skróć o 30%.\n"
        "## Pytania techniczne — przykłady\n"
        "Różnica defekt/awaria; klasy równoważności i wartości brzegowe na przykładzie; piramida testów; jak przetestujesz formularz logowania; co zawiera bug raport; czym jest regresja; różnica WebDriverWait i sleep; co to Page Object; co robi fixture; jak działa CI; co to SQL injection; GET vs POST; kody 200/400/404/500.\n"
        "## Pytania miękkie — metoda STAR\n"
        "**S**ytuacja → **Z**adanie (Task) → **D**ziałanie (Action) → **R**ezultat. „Opowiedz o trudnym problemie” → konkretna historia z projektu (np. testy flaky w CI i jak je ustabilizowałeś).\n"
        "## Zadanie rekrutacyjne\n"
        "Częste: przetestuj stronę/formularz i opisz defekty, napisz kilka testów automatycznych, przeczytaj kod i znajdź błąd. Pisz przypadki z oczekiwanym wynikiem i raporty jak w tygodniu 9; dołącz README „jak uruchomić”.\n"
        "## Widełki wynagrodzeń\n"
        "Od 24 grudnia 2025 r. pracodawca w Polsce musi przekazać kandydatowi informację o wynagrodzeniu (lub jego przedziale) — w ogłoszeniu albo przed rozmową. Orientacyjnie raport Bulldogjob (dane z początku 2025) podaje dla juniora testera manualnego ok. 6 900 zł brutto miesięcznie na umowie o pracę; sprawdzaj aktualne raporty, bo kwoty się zmieniają.\n"
        "## Plan szukania\n"
        "5 dopasowanych aplikacji tygodniowo (nie 50 jednakowych), dziennik aplikacji (data, firma, stanowisko, link, status), po każdej rozmowie — notatka z pytań, których nie znałeś. ISTQB Foundation (CTFL 4.0: 40 pytań, próg 26, 60 minut) wzmacnia CV, ale nie zastępuje projektu."),
    przyklad=("PROJEKTY\n"
              "Magazyn sklepu — aplikacja webowa do ewidencji produktów i operacji magazynowych      github.com/anna-nowak/magazyn\n"
              "• Python, SQLite, Flask; walidacja formularzy po stronie serwera, zapytania parametryzowane (ochrona przed SQL injection)\n"
              "• 28 testów pytest (parametrize, fixtures, baza tymczasowa) + 3 testy E2E Selenium w Page Object Model\n"
              "• CI w GitHub Actions z raportem HTML; plan testów i 3 raporty błędów w repozytorium\n\n"
              "Testy sklepu internetowego (projekt szkoleniowy)                                         github.com/anna-nowak/sklep-testy\n"
              "• 15 testów E2E (Selenium, POM, WebDriverWait), 10 przypadków testowych, 3 zgłoszone defekty z krokami odtworzenia\n\n"
              "Opowieść (fragment): „Zbudowałam aplikację magazynową, żeby przećwiczyć testowanie na wszystkich poziomach. "
              "Reguły — jak blokada wydania ponad stan — testuję jednostkowo z wartościami brzegowymi; zapis do bazy integracyjnie na bazie tymczasowej; "
              "trzy najważniejsze ścieżki w Selenium. Test brzegowy złapał, że wydanie dokładnie całego stanu było blokowane — warunek > zamiast >=.”"),
    demonstracja={"tytul": "Sekcja Projekty, która broni się sama", "kroki": [
        "Nazwa projektu + link — rekruter kliknie; repozytorium musi mieć README i zielone CI.",
        "Jedno zdanie, co robi — bez żargonu.",
        "Technologie wymienione z nazwy — w ogłoszeniach szuka się ich słowami kluczowymi (Python, pytest, Selenium, SQL, CI).",
        "Liczby: ile testów, jakie poziomy — konkret zamiast „znam pytest”.",
        "Słownictwo testera: Page Object Model, wartości brzegowe, raporty błędów — pokazujesz, że rozumiesz zawód, nie tylko kod.",
        "Opowieść kończy się prawdziwym przykładem defektu znalezionego testem — najmocniejszy moment rozmowy."],
        "wynik": "Sekcja Projekty na 6 linii i 30-sekundowy fragment opowieści z konkretnym defektem."},
    jak_uruchomic=["CV: edytor tekstu → eksport do PDF; nazwa pliku Imie_Nazwisko_CV_Junior_QA.pdf.", "Nagranie opowieści: telefon, 2 minuty, odsłuchaj i skróć.",
                   "Próbna rozmowa: Asystent (API albo Claude Code) z promptem „Rekruter Junior QA” z zakładki Prompty; Offline — lista pytań w Ściądze."],
    cwiczenia=[
        C("prowadzone",
          "Ułóż opowieść o projekcie w kolejności (numery po przecinku): 1 „Testuję reguły jednostkowo z wartościami brzegowymi, a 3 ścieżki w Selenium; CI uruchamia wszystko przy pushu”, 2 „Sklep potrzebował ewidencji stanów zamiast arkusza”, "
          "3 „Nauczyłam się projektować testy przed kodem i stabilizować testy E2E”, 4 „Zbudowałam aplikację Flask z bazą SQLite”. Czas: 10 minut.",
          "2, 4, 1, 3 — problem → rozwiązanie → jak testuję → czego się nauczyłam.",
          ["Zaczynasz od problemu.", "Potem co zbudowałaś.", "Testowanie przed nauką."],
          "2 (problem), 4 (rozwiązanie), 1 (jak testuję), 3 (czego się nauczyłam).",
          [tx("k", "Kolejność", "2, 4, 1, 3")]),
        C("samodzielne",
          "Oceń wpisy w CV (zostaw / popraw): (1) „Znajomość Pythona — średnio-zaawansowana”; (2) „Magazyn — Flask, SQLite; 28 testów pytest, 3 E2E Selenium POM, CI — link”; (3) „Hobby: gry komputerowe” w miejscu sekcji Projekty; (4) PESEL i data urodzenia w nagłówku. "
          "Dodatkowo (5): pytanie „Opowiedz o trudnym problemie” — jaką metodą budujesz odpowiedź (wpisz skrót)? Czas: 15 minut.",
          "(1) popraw — zamień ogólnik na konkret (projekt, liczby); (2) zostaw; (3) popraw — projekty ważniejsze niż hobby; (4) popraw — usuń; (5) STAR.",
          ["Ogólniki bez dowodu nic nie mówią.", "Dane osobowe ponad potrzebę — usuń.", "Sytuacja → zadanie → działanie → rezultat."],
          "(1) popraw — „Python: projekt Magazyn (link), 28 testów” zamiast samooceny; (2) zostaw; (3) popraw — Projekty na górze, hobby opcjonalnie na dole; (4) popraw — usuń (niepotrzebne dane osobowe); (5) STAR.",
          [wy("a", "(1) samoocena Pythona", ["zostaw", "popraw"], "popraw"), wy("b", "(2) wpis Magazyn z liczbami", ["zostaw", "popraw"], "zostaw"), wy("c", "(3) hobby zamiast projektów", ["zostaw", "popraw"], "popraw"),
           wy("d", "(4) PESEL i data urodzenia", ["zostaw", "popraw"], "popraw"), tx("e", "(5) Metoda", "STAR")]),
    ],
    typowe_bledy=[
        B("Brak odpowiedzi na 50 wysłanych CV.", "Jednakowe CV bez projektów i słów kluczowych z ogłoszenia.", "Porównaj CV z 3 ogłoszeniami — ile słów kluczowych się pokrywa?", "Projekty na górze, technologie z ogłoszenia, 5 dopasowanych aplikacji tygodniowo."),
        B("Na rozmowie: „nie wiem” i cisza.", "Brak struktury odpowiedzi.", "Czy znasz pytania z listy w Ściądze?", "Powiedz, jak byś to sprawdził(a): „Nie używałam X, ale zrobiłabym to tak…” + przykład z projektu."),
    ],
    pulapki=["Link do GitHuba z pustymi repozytoriami albo czerwonym CI — sprawdź przed wysłaniem.", "Kopiowanie opisów projektów z internetu — rekruter zapyta o szczegóły."],
    zadania=["CV 1 strona z sekcją Projekty i linkami.", "Nagranie 2-minutowej opowieści o projekcie.", "Sesja 15 pytań technicznych i 3 miękkich; 5 aplikacji w dzienniku."],
    pytania=[["Jak zbudować opowieść o projekcie?", "Problem → rozwiązanie → jak testuję → czego się nauczyłem."], ["Co to metoda STAR?", "Sytuacja, zadanie, działanie, rezultat."], ["Czego nie wpisujesz do CV?", "PESEL, data urodzenia, niepotrzebne dane osobowe."]],
    podsumowanie="Masz CV z projektami i liczbami, opowieść o projekcie w 2 minuty, odpowiedzi na pytania techniczne i miękkie oraz plan wysyłania aplikacji z dziennikiem.",
    test=[T("Struktura 2-minutowej opowieści o projekcie?", ["Lista plików", "Problem → rozwiązanie → jak testuję → czego się nauczyłem", "Historia commitów", "Lista technologii"], 1, "Od problemu do wniosków."),
          T("Sekcja Projekty w CV osoby zmieniającej branżę:", ["na końcu", "na górze", "niepotrzebna", "w osobnym pliku"], 1, "Najmocniejszy dowód."),
          T("Od 24.12.2025 pracodawca w Polsce musi:", ["zatrudnić juniora", "przekazać kandydatowi informację o wynagrodzeniu", "wymagać ISTQB", "płacić za rekrutację"], 1, "Jawność wynagrodzeń."),
          T("Na pytanie, na które nie znasz odpowiedzi:", ["milczysz", "zmyślasz", "mówisz, jak byś to sprawdził(a)", "kończysz rozmowę"], 2, "Pokazujesz sposób myślenia.")],
    w_praktyce=["Dziennik aplikacji: data, firma, stanowisko, link, status, następny krok.", "Po każdej rozmowie: 3 pytania, których nie znałeś → lekcja do powtórki."],
    zrodla=[Z.RYNEK_JJ, Z.RYNEK_BDJ, Z.ISTQB_CTFL, Z.GH_README],
)

POWTORKA4 = L(
    id="powtorka_portfolio", nazwa="Powtórka końcowa: przegląd projektu jak senior tester i plan dalszej nauki", tydzien=12,
    slowa=["powtórka", "przegląd", "senior", "code review", "checklista", "portfolio", "plan nauki", "API testing", "ISTQB", "co dalej"],
    cel="Po tej lekcji przeglądasz własny projekt listą kontrolną seniora (kod, testy, dokumentacja, bezpieczeństwo, CI), wdrażasz najważniejsze poprawki i układasz plan nauki na 3 miesiące po kursie.",
    po_co="Projekt, który przeszedł Twoją własną surową recenzję, broni się na rozmowie. Plan po kursie sprawia, że nauka nie kończy się w tygodniu 12.",
    wymagania=["Projekt Magazyn i repozytorium testów sklepu.", "Wszystkie etapy kursu."],
    wyjasnienie=(
        "## Lista kontrolna seniora\n"
        "**Kod**: funkcje krótkie z docstringami, nazwy, brak duplikacji, brak magicznych liczb, input/print tylko w interfejsie, zapytania SQL z `?`.\n"
        "**Testy**: piramida (dużo test_client/jednostkowych, kilka E2E), wartości brzegowe reguł, przypadki negatywne, testy niezależne (tmp_path), brak sleep, nazwy jak zdania, każdy test zawodzi na mutancie.\n"
        "**Dokumentacja**: README (opis, uruchomienie, przykład, „Jak testuję”), PLAN_TESTOW.md (zakres, poziomy, ryzyka, co ręcznie), raporty błędów.\n"
        "**Bezpieczeństwo**: brak sekretów i .env w repo, debug=False poza komputerem, walidacja serwera, autoescaping szablonów.\n"
        "**CI**: zielone, raport HTML jako artefakt, odznaka w README.\n"
        "## Recenzja z asystentem\n"
        "Prompt: „Oceń mój projekt jak senior tester przed code review. Wypisz 5 najważniejszych uwag, od najpoważniejszej. Nie poprawiaj kodu.” — potem sam(a) decydujesz, które 3 wdrażasz, i opisujesz je w RECENZJA.md (uwaga → decyzja → commit).\n"
        "## Co dalej (3 miesiące)\n"
        "1. **Testy API** (requests + pytest, ewentualnie Postman) — bardzo częste w ogłoszeniach. 2. **SQL** — JOIN, GROUP BY. 3. **ISTQB CTFL 4.0** — polska wersja sylabusa i egzaminy przykładowe SJSI. "
        "4. Alternatywa dla Selenium: Playwright — pojawia się coraz częściej w ogłoszeniach; Twoje POM i czekanie przenoszą się 1:1. 5. Angielski techniczny — dokumentacja narzędzi jest po angielsku.\n"
        "## Mapa całego kursu\n"
        "Etap 1: Python (podstawy) → Etap 2: projekt jak w zespole (Git, moduły, venv, API) → Etap 3: testowanie (techniki, pytest, Selenium, raporty, CI) → Etap 4: projekt portfolio i rekrutacja."),
    przyklad=kod("powtorka_portfolio", (
        "LISTA = {\n"
        "    \"README z sekcją Jak testuję\": True,\n"
        "    \"CI zielone z raportem HTML\": True,\n"
        "    \"Zapytania SQL z parametrami ?\": True,\n"
        "    \"Testy wartości brzegowych reguł\": True,\n"
        "    \"Brak time.sleep w testach E2E\": False,\n"
        "    \"Brak sekretów w repozytorium\": True,\n"
        "    \"PLAN_TESTOW.md\": False,\n"
        "}\n"
        "spelnione = [k for k, v in LISTA.items() if v]\n"
        "do_poprawy = [k for k, v in LISTA.items() if not v]\n"
        "print(f\"Spełnione: {len(spelnione)}/{len(LISTA)} ({len(spelnione) / len(LISTA):.0%})\")\n"
        "for nr, k in enumerate(do_poprawy, 1):\n"
        "    print(f\"{nr}. Popraw: {k}\")\n"), "Spełnione: 5/7 (71%)\n1. Popraw: Brak time.sleep w testach E2E\n2. Popraw: PLAN_TESTOW.md\n"),
    demonstracja={"tytul": "Lista kontrolna jako słownik — i plan poprawek", "kroki": [
        "Słownik: punkt listy → czy spełniony (bool).",
        "Listy składane wybierają spełnione i do poprawy.",
        "`:.0%` — format procentowy bez miejsc po przecinku (5/7 = 71%).",
        "`enumerate(…, 1)` numeruje poprawki od 1 — gotowa lista do RECENZJA.md.",
        "Każdy punkt „do poprawy” = osobny mały commit z opisem („Zastąp time.sleep czekaniem na listę produktów”)."],
        "wynik": "„Spełnione: 5/7 (71%)” i dwie numerowane poprawki."},
    jak_uruchomic=["Zapisz jako przeglad.py → ▶ Uruchom; uzupełnij listę o swoje punkty.", "Poprawki: osobne commity, potem push i sprawdzenie CI."],
    cwiczenia=[
        C("prowadzone",
          "Recenzja dała 5 uwag: (A) hasło do bazy w kodzie, (B) time.sleep(3) w testach E2E, (C) brak docstringów w 4 funkcjach, (D) literówka w README, (E) brak testu dla wydania równego stanowi. Na wzór listy seniora ułóż 3 najważniejsze do wdrożenia od najpoważniejszej (litery po przecinku). Czas: 10 minut.",
          "A, E, B — bezpieczeństwo, brak testu granicy reguły, niestabilne testy.",
          ["Bezpieczeństwo pierwsze.", "Brak testu granicy = defekt może przejść.", "sleep = testy flaky."],
          "A (sekret w kodzie), E (wartość brzegowa reguły), B (flaky). C i D są ważne, ale mniej pilne.",
          [tx("k", "Trzy najważniejsze", "A, E, B")]),
        C("samodzielne",
          "Plan po kursie: masz 5 godzin tygodniowo przez 3 miesiące. (1) Ile to godzin razem (12 tygodni)? (2) Który temat wybierasz na pierwszy miesiąc, jeśli 3 z 5 ogłoszeń, które cię interesują, wymagają testów API — wybierz: Playwright / testy API / ISTQB. (3) Czy certyfikat ISTQB zastępuje projekt w CV (tak/nie)? Czas: 10 minut.",
          "(1) 60; (2) testy API; (3) nie.",
          ["5 × 12.", "Wybierasz według ogłoszeń, które chcesz zdobyć.", "Certyfikat potwierdza wiedzę, projekt — umiejętność."],
          "(1) 60 godzin; (2) testy API — najczęściej wymagane w Twoich ogłoszeniach; (3) nie — wzmacnia CV, ale nie zastępuje projektu.",
          [li("a", "(1) Godzin razem", 60), wy("b", "(2) Pierwszy miesiąc", ["Playwright", "testy API", "ISTQB"], "testy API"), wy("c", "(3) ISTQB zastępuje projekt?", ["tak", "nie"], "nie")]),
    ],
    typowe_bledy=[
        B("Wdrożenie wszystkich 20 uwag naraz w jednym commicie.", "Brak priorytetów.", "Które uwagi dotyczą bezpieczeństwa i poprawności?", "3 najważniejsze, każda osobnym commitem, CI po każdym."),
        B("Projekt „skończony”, a CI czerwone od tygodnia.", "Brak sprawdzenia po ostatnich zmianach.", "Zakładka Actions.", "Napraw przed wysłaniem CV — rekruter widzi czerwony znaczek."),
    ],
    pulapki=["Ślepe wdrażanie wszystkich uwag AI — część bywa nietrafiona; decyzja i uzasadnienie są Twoje.", "Nauka 5 nowych narzędzi naraz po kursie — jedno na miesiąc, z projektem."],
    zadania=["Recenzja projektu jak senior tester; 3 poprawki w osobnych commitach; RECENZJA.md.", "Plan nauki na 3 miesiące w notatki.md.", "Ostatni przegląd repozytoriów przed wysłaniem CV."],
    pytania=[["Co sprawdza lista kontrolna seniora?", "Kod, testy, dokumentację, bezpieczeństwo i CI."], ["Jak wybierasz poprawki z recenzji?", "Najpierw bezpieczeństwo i poprawność, potem stabilność testów, na końcu kosmetyka."], ["Co po kursie najczęściej wymagają ogłoszenia QA?", "Testy API, SQL, narzędzia automatyzacji (Selenium/Playwright)."]],
    podsumowanie="Recenzujesz własny projekt listą seniora, wdrażasz najważniejsze poprawki z uzasadnieniem i masz plan nauki na 3 miesiące.",
    test=[T("Najpilniejsza uwaga z recenzji:", ["literówka w README", "hasło w kodzie", "brak emoji", "kolor przycisku"], 1, "Bezpieczeństwo."),
          T("Uwagi z recenzji wdrażasz:", ["wszystkie w jednym commicie", "najważniejsze, osobnymi commitami", "żadnej", "tylko kosmetyczne"], 1, "Mała zmiana = łatwa do sprawdzenia."),
          T("Certyfikat ISTQB CTFL:", ["zastępuje projekt", "wzmacnia CV obok projektu", "jest wymagany prawnie", "jest tylko po angielsku"], 1, "Polska wersja: SJSI."),
          T("format(5/7, \".0%\") daje:", ["0.71", "71%", "5/7", "71.4%"], 1, "Procent bez miejsc po przecinku.")],
    w_praktyce=["Co kwartał: przegląd portfolio listą seniora.", "Każda nowa umiejętność = mały projekt na GitHubie z README i testami."],
    zrodla=[Z.ISTQB_CTFL, Z.SJSI_CTFL_PL, Z.OWASP_SQLI, Z.GH_ACTIONS_PY],
)
