# Aplikacja internetowa we Flask: trasy, parametry, JSON i testy
Tydzień 10 · lekcja 32 z 48 · ≈ 50 min

**Po tej lekcji potrafisz:** czytasz i zlecasz małą aplikację Flask z funkcją create_app, trasą strony i trasą API zwracającą JSON, obsługujesz złe parametry kodem 400 i testujesz ją test_client bez uruchamiania serwera.

**Po co mi to?** Strona statyczna nie zapisze rezerwacji ani nie sprawdzi danych na serwerze. Flask to najprostszy krok od skryptu do aplikacji internetowej — i świetnie współpracuje z agentami.

## Czego potrzebujesz
- Środowisko kursu (Flask instaluje Mentor).
- Lekcje „Testy jako umowa” i „JavaScript na stronie”.

## 1 · Wyjaśnienie od podstaw
### Najmniejsza aplikacja
```
from flask import Flask, jsonify, request

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def start():
        return "<h1>Pod Lipą</h1>"

    @app.route("/api/cena")
    def cena():
        noce = request.args.get("noce", type=int)
        ...
        return jsonify({"koszt": 480.0})

    return app
```
- Trasa (route) łączy adres z funkcją: wejście na `/api/cena?noce=2&osoby=2` uruchamia funkcję cena.
- `request.args.get("noce", type=int)` czyta parametr z adresu; gdy nie jest liczbą — zwraca None.
- `jsonify` zwraca dane w JSON (dla JavaScriptu i innych programów).
- create_app (wzorzec „fabryki aplikacji” z dokumentacji Flaska) tworzy aplikację w funkcji — testy mogą zbudować świeżą aplikację, a konfiguracja (np. ścieżka bazy) przychodzi jako parametr.
### Kody odpowiedzi
| kod | znaczy | kiedy |
|---|---|---|
| 200 | OK | poprawne dane |
| 400 | złe żądanie | brak parametru, „abc” zamiast liczby, noce = 0 |
| 404 | nie ma takiej strony | zły adres |
| 500 | błąd serwera | wyjątek w Twoim kodzie — nie może się zdarzać dla złych danych od użytkownika |
Złe dane od użytkownika → 400 z komunikatem: `return jsonify({"blad": "noce musi być liczbą ≥ 1"}), 400`.
### Uruchomienie lokalnie
W terminalu Mentora: `flask --app app run --debug` → adres http://127.0.0.1:5000. Tryb debug przeładowuje kod po zmianie i pokazuje błędy w przeglądarce — TYLKO na Twoim komputerze. Dokumentacja Flaska: wbudowany serwer deweloperski nie nadaje się do produkcji, a debugger pozwala wykonać dowolny kod — nigdy nie włączaj go na serwerze publicznym.
### Testy bez serwera
```
def test_cena():
    klient = create_app().test_client()
    odp = klient.get("/api/cena?noce=2&osoby=2")
    assert odp.status_code == 200
    assert odp.get_json() == {"koszt": 480.0}
```
### Logika osobno
Funkcja licząca koszt mieszka w kalkulator_pobytu.py (już przetestowana). Trasa tylko: czyta parametry → woła funkcję → zamienia ValueError na 400 → zwraca JSON. Agent lubi wklejać logikę do trasy — prosisz o import.
### Gdzie to później działa
Aplikacja Python potrzebuje hostingu z Pythonem (np. usługi typu PaaS z darmowym lub tanim planem — warunki zmieniają się, sprawdzasz je przed decyzją). W kursie: lokalnie i w testach; publikacja w projekcie końcowym jest opcjonalna.

## 2 · Demonstracja — krok po kroku
**Aplikacja z agentem i test, który łapie 500**

```
from flask import Flask, jsonify, request
from kalkulator_pobytu import koszt_pobytu


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def start():
        return "<h1>Pod Lipą</h1><p>Kalkulator: /api/cena?noce=2&osoby=2</p>"

    @app.route("/api/cena")
    def cena():
        noce = request.args.get("noce", type=int)
        osoby = request.args.get("osoby", type=int)
        if noce is None or osoby is None:
            return jsonify({"blad": "podaj noce i osoby jako liczby"}), 400
        try:
            return jsonify({"koszt": koszt_pobytu(noce, osoby)})
        except ValueError as e:
            return jsonify({"blad": str(e)}), 400

    return app
```

1. Prośba: „app.py z create_app(): trasa / (HTML z nazwą Pod Lipą) i /api/cena?noce=&osoby= zwracająca JSON {"koszt": …} z funkcji koszt_pobytu z kalkulator_pobytu.py. Złe dane → 400 i {"blad": …}. Bez debug=True w kodzie. Testy w test_app.py.”
2. `flask --app app run --debug` → przeglądarka: http://127.0.0.1:5000/api/cena?noce=2&osoby=2 → {"koszt": 480}.
3. Adres z noce=0: strona błędu 500 i traceback ValueError — agent nie złapał wyjątku z koszt_pobytu.
4. Prośba: „ValueError z koszt_pobytu ma dawać 400 z komunikatem”. Test: klient.get("/api/cena?noce=0&osoby=2").status_code == 400 — zielono.
5. Ctrl + C zatrzymuje serwer. Commit app.py i test_app.py.

✔ **Oczekiwany wynik:** Aplikacja odpowiada 200 dla dobrych danych i 400 z komunikatem dla złych; brak 500 dla błędów użytkownika, potwierdzony testem.

## 3 · Jak to uruchomić
1. Terminal Mentora w PRACA: `flask --app app run --debug` → http://127.0.0.1:5000; Ctrl + C kończy.
2. Testy: `python -m pytest -q test_app.py` albo „✔ Sprawdź wynik”.

## W praktyce
- Logika w modułach, trasy tylko tłumaczą żądanie na wywołanie.
- Każda trasa API: test 200 i test 400.

## 4 · Ćwiczenie prowadzone
Jaki kod odpowiedzi powinna zwrócić aplikacja z przykładu dla: (1) /api/cena?noce=2&osoby=2, (2) /api/cena?noce=abc&osoby=2, (3) /api/cena?noce=0&osoby=2, (4) /api/cenaa?noce=2. Czas: 15 minut.

📄 `cwiczenia/tydzien_10/aplikacja_flask_1.md` · rozwiązanie: `rozwiazania/tydzien_10/aplikacja_flask_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Prawda czy fałsz? (1) `debug=True` można zostawić na serwerze publicznym, jeśli strona jest mała. (2) test_client pozwala testować trasy bez uruchamiania serwera. (3) Błąd 500 dla złych danych od użytkownika jest w porządku. (4) `request.args.get("noce", type=int)` dla „abc” zwraca None. Czas: 15 minut.

📄 `cwiczenia/tydzien_10/aplikacja_flask_2.md` · rozwiązanie: `rozwiazania/tydzien_10/aplikacja_flask_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **„Error: Could not locate a Flask application”.**
  - Przyczyna: Uruchomienie z innego folderu albo zła nazwa w --app.
  - Jak sprawdzić: `dir app.py` w bieżącym folderze.
  - Poprawka: `flask --app app run` w PRACA (app = nazwa pliku bez .py); w pliku funkcja create_app albo zmienna app.
- ✘ **„Address already in use” / port 5000 zajęty.**
  - Przyczyna: Serwer działa w innym oknie.
  - Jak sprawdzić: Czy inne okno terminala ma uruchomiony flask?
  - Poprawka: Zatrzymaj Ctrl + C albo `flask --app app run --port 5001`.
- ✘ **Testy: „TypeError: 'NoneType' object is not subscriptable” na get_json().**
  - Przyczyna: Trasa zwraca HTML albo tekst, nie JSON.
  - Jak sprawdzić: odp.data w teście.
  - Poprawka: Zwracaj jsonify(...) w trasach API.

## Pułapki
- Serwer deweloperski i tryb debug — tylko lokalnie. Agent czasem dopisuje `app.run(debug=True, host="0.0.0.0")` — host 0.0.0.0 udostępnia aplikację w całej sieci lokalnej.
- Walidacja w JavaScript nie zwalnia z walidacji na serwerze — każdy może wywołać API ręcznie.

## Dodatkowe zadania
1. Zbuduj app.py z create_app i testami (zadanie tygodnia).
2. Sprawdź w przeglądarce kody 200/400/404.
3. Commit + push.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Po co create_app?**
  - Testy i konfiguracja mogą tworzyć świeżą aplikację z parametrami, bez globalnego stanu.
- **Jaki kod dla złych danych użytkownika?**
  - 400 z komunikatem w JSON.
- **Dlaczego debug=False na serwerze?**
  - Debugger pozwala wykonać dowolny kod — to dziura bezpieczeństwa.

## Co potrafię teraz bez patrzenia na przykład?
Czytasz i zlecasz aplikację Flask z fabryką, trasami HTML i JSON, obsługą 400, testujesz ją test_client i wiesz, czego nie robić z trybem debug.

## Źródła (data dostępu w nawiasie)
Narzędzia, ceny i przepisy zmieniają się — przed użyciem w pracy otwórz źródło.
- Flask — Quickstart (trasy, request.args, jsonify, tryb debug) (dostęp 20.11.2026) — <https://flask.palletsprojects.com/en/stable/quickstart/>
- Flask — Application Factories (create_app) (dostęp 20.11.2026) — <https://flask.palletsprojects.com/en/stable/patterns/appfactories/>
- Flask — Testing Flask Applications (test_client) (dostęp 20.11.2026) — <https://flask.palletsprojects.com/en/stable/testing/>
- Flask — Deploying to Production (serwer deweloperski nie do produkcji) (dostęp 20.11.2026) — <https://flask.palletsprojects.com/en/stable/deploying/>

## Test (w Mentorze: Lekcje → Sprawdź się)
- `@app.route("/api/cena")` oznacza:
  - A) Import
  - B) Powiązanie adresu z funkcją
  - C) Bazę danych
  - D) Test
- Złe dane od użytkownika — kod odpowiedzi:
  - A) 200
  - B) 400
  - C) 500
  - D) 302
- Testowanie tras bez uruchamiania serwera:
  - A) app.test_client()
  - B) flask run
  - C) curl
  - D) ping
- Tryb debug Flaska na serwerze publicznym:
  - A) Zalecany
  - B) Zabroniony — pozwala wykonać kod
  - C) Obowiązkowy
  - D) Bez znaczenia

Odpowiedzi: B, B, A, B
