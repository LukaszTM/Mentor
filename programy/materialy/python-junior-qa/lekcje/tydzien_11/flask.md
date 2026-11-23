# Flask: strony, szablony, formularze z walidacją i komunikaty
Tydzień 11 · lekcja 36 z 39 · ≈ 45 min

**Po tej lekcji potrafisz:** tworzysz aplikację Flask z trasami GET i POST, wyświetlasz dane z bazy w szablonie, przyjmujesz formularz (request.form), walidujesz dane po stronie serwera z czytelnymi komunikatami i przekierowujesz po zapisie (redirect).

**Po co mi to?** Interfejs webowy zamienia projekt z konsoli w aplikację, którą rekruter kliknie; a Ty — przetestujesz w przeglądarce Selenium, jak prawdziwy system.

## Czego potrzebujesz
- Lekcja „SQLite” i moduły projektu Magazyn (baza.py, magazyn.py).
- Flask jest w środowisku kursu (Flask 3.1).
- Podstawy HTML: znaczniki, formularz — wyjaśnione w lekcji.

## 1 · Wyjaśnienie od podstaw
### Minimalna aplikacja
```
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Magazyn</h1>"

if __name__ == "__main__":
    app.run(port=5000, debug=True)
```
`@app.route("/")` — pod adresem / (strona główna) Flask wywoła funkcję index i odeśle to, co zwróci. `python app.py` → http://127.0.0.1:5000. `debug=True` przeładowuje aplikację po zapisie pliku i pokazuje błędy — tylko lokalnie, nigdy na serwerze publicznym.
### Szablony (Jinja)
Pliki HTML w katalogu `templates/`. `render_template("index.html", produkty=lista)` przekazuje dane; w szablonie: `{{ p.nazwa }}` wstawia wartość (Flask automatycznie zabezpiecza znaki HTML), `{% for p in produkty %} … {% endfor %}` — pętla, `{% if blad %} … {% endif %}` — warunek.
### Formularz: GET pokazuje, POST zapisuje
```
@app.route("/dodaj", methods=["GET", "POST"])
def dodaj():
    if request.method == "POST":
        nazwa = request.form.get("nazwa", "").strip()
        ...
        return redirect(url_for("index"))
    return render_template("dodaj.html")
```
W HTML: `<form method="post"><input name="nazwa" id="nazwa"> <button data-test="zapisz">Zapisz</button></form>` — atrybut **name** to klucz w request.form; **id** i **data-test** przydadzą się w Selenium.
### Walidacja po stronie serwera
Atrybut `required` w HTML można obejść (Selenium, curl, DevTools) — reguły sprawdzasz zawsze w Pythonie: puste pole, cena nie-liczba albo ujemna, ilość niecałkowita. Przy błędzie: ten sam formularz z komunikatem i wpisanymi wartościami, kod **400**; przy sukcesie: zapis i `redirect` (wzorzec Post/Redirect/Get — odświeżenie strony nie doda produktu drugi raz).
### Trasy z parametrem
`@app.route("/produkt/<int:pid>")` → `def produkt(pid):` — strona jednego produktu z historią operacji; brak produktu → `abort(404)`.
### Porty
Sklep testowy z paczki działa na 5001, Twój Magazyn na 5000 — mogą działać jednocześnie. „Address already in use” = port zajęty przez inny proces.

## 2 · Demonstracja — krok po kroku
**Strona z listą i formularzem — sprawdzona bez przeglądarki**

```
from flask import Flask, redirect, render_template_string, request, url_for

app = Flask(__name__)
PRODUKTY = [{"nazwa": "Zeszyt A5", "cena": 4.5}]
STRONA = """<h1>Magazyn</h1>
{% if blad %}<p data-test="blad">{{ blad }}</p>{% endif %}
<ul>{% for p in produkty %}<li class="produkt">{{ p.nazwa }} — {{ '%.2f'|format(p.cena) }} zł</li>{% endfor %}</ul>
<form method="post"><input name="nazwa" value="{{ nazwa }}"><input name="cena"><button data-test="zapisz">Zapisz</button></form>"""


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nazwa = request.form.get("nazwa", "").strip()
        try:
            cena = float(request.form.get("cena", "").replace(",", "."))
        except ValueError:
            cena = None
        if not nazwa:
            blad = "Podaj nazwę produktu"
        elif cena is None or cena < 0:
            blad = "Cena musi być liczbą nieujemną"
        else:
            PRODUKTY.append({"nazwa": nazwa, "cena": cena})
            return redirect(url_for("index"))
        return render_template_string(STRONA, produkty=PRODUKTY, blad=blad, nazwa=nazwa), 400
    return render_template_string(STRONA, produkty=PRODUKTY, blad=None, nazwa="")


klient = app.test_client()
print(klient.get("/").status_code)
odp = klient.post("/", data={"nazwa": "Klej", "cena": "3,40"})
print(odp.status_code, odp.headers["Location"])
odp = klient.post("/", data={"nazwa": "", "cena": "5"})
print(odp.status_code, "Podaj nazwę produktu" in odp.get_data(as_text=True))
odp = klient.post("/", data={"nazwa": "<b>X</b>", "cena": "-1"})
print(odp.status_code, "&lt;b&gt;X&lt;/b&gt;" in odp.get_data(as_text=True))
print([p["nazwa"] for p in PRODUKTY])

```

1. `Flask(__name__)` — aplikacja; `PRODUKTY` — lista w pamięci (w projekcie: baza SQLite przez baza.py).
2. `render_template_string` — szablon w napisie, żeby przykład był jednym plikiem; w projekcie `render_template("index.html")` z katalogu templates/.
3. Szablon: `{% if blad %}` komunikat z data-test, pętla `{% for %}` po produktach, `'%.2f'|format` — 2 miejsca po przecinku, `value="{{ nazwa }}"` — wpisana nazwa wraca do pola po błędzie.
4. `methods=["GET", "POST"]` — GET pokazuje stronę, POST przyjmuje formularz.
5. Walidacja w Pythonie: pusta nazwa, cena nie-liczba (przecinek zamieniony na kropkę — polscy użytkownicy!), cena ujemna.
6. Sukces → `redirect(url_for("index"))` = kod 302 i nagłówek Location: /. Błąd → strona z komunikatem i kod 400.
7. `app.test_client()` — Flask wysyła żądania bez serwera i przeglądarki: tak piszesz szybkie testy aplikacji webowej (następna lekcja).
8. `<b>X</b>` w nazwie wraca jako `&lt;b&gt;X&lt;/b&gt;` — Jinja zabezpiecza HTML (ochrona przed XSS).

✔ **Oczekiwany wynik:** 200, „302 /”, „400 True” dwa razy i lista ['Zeszyt A5', 'Klej'] — klej dodany, dwa złe formularze odrzucone.

## 3 · Jak to uruchomić
1. Zapisz jako flask_demo.py → ▶ Uruchom (test_client działa bez przeglądarki).
2. Jako serwer: zamień 6 ostatnich linii na `app.run(port=5000, debug=True)` → `python flask_demo.py` → http://127.0.0.1:5000 → Ctrl+C kończy.

## W praktyce
- Testując formularz: puste pola, spacje, przecinek w liczbie, wartości ujemne, bardzo długi tekst, HTML w polu — i obejście walidacji przeglądarki.
- Każdy formularz = atrybuty id/data-test dla testów Selenium.

## 4 · Ćwiczenie prowadzone
Na wzór demonstracji: jakie kody odpowiedzi zwróci aplikacja dla POST: (1) nazwa „Gumka”, cena „1.50”; (2) nazwa „Gumka”, cena „abc”; (3) nazwa „  ”, cena „2”; (4) GET /? Czas: 10 minut.

📄 `cwiczenia/tydzien_11/flask_1.md` · rozwiązanie: `rozwiazania/tydzien_11/flask_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Formularz ma `<input name="ilosc" type="number" min="1" required>`. (1) Czy to wystarczy, żeby serwer nie przyjął ilości 0 (tak/nie)? (2) Jak tester to sprawdzi bez przeglądarki — wybierz: test_client.post z ilosc=0 / zmiana CSS. (3) Jaki kod odpowiedzi powinien dostać przy ilości 0, a jaki przy błędzie w kodzie serwera (dwa kody po przecinku)? Czas: 15 minut.

📄 `cwiczenia/tydzien_11/flask_2.md` · rozwiązanie: `rozwiazania/tydzien_11/flask_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **jinja2.exceptions.TemplateNotFound: index.html**
  - Przyczyna: Szablon nie leży w katalogu templates/ obok app.py.
  - Jak sprawdzić: Struktura katalogów.
  - Poprawka: templates/index.html w katalogu aplikacji.
- ✘ **405 Method Not Allowed po wysłaniu formularza**
  - Przyczyna: Trasa bez methods=["GET", "POST"].
  - Jak sprawdzić: Dekorator @app.route.
  - Poprawka: Dodaj methods=["GET", "POST"].
- ✘ **OSError: [Errno 98/10048] Address already in use**
  - Przyczyna: Port zajęty (druga kopia aplikacji albo inny program).
  - Jak sprawdzić: Czy aplikacja działa w innym oknie?
  - Poprawka: Zamknij poprzednią (Ctrl+C) albo użyj innego portu.
- ✘ **KeyError / BadRequest: The browser sent a request that this server could not understand**
  - Przyczyna: request.form["pole"] dla pola, którego nie ma w formularzu.
  - Jak sprawdzić: Nazwy name w HTML.
  - Poprawka: request.form.get("pole", "") i zgodne atrybuty name.

## Pułapki
- Walidacja tylko w HTML/JavaScript — serwer musi sprawdzać sam.
- debug=True na serwerze dostępnym z internetu — konsola debugera pozwala wykonać kod.

## Dodatkowe zadania
1. Strona główna z listą produktów z bazy.
2. Formularz dodawania produktu z walidacją i komunikatami.
3. Strona produktu z historią operacji; 404 dla nieistniejącego.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Po co redirect po zapisie formularza?**
  - Odświeżenie strony nie wyśle formularza drugi raz (Post/Redirect/Get).
- **Dlaczego walidacja w Pythonie, skoro jest required?**
  - Atrybuty HTML da się obejść; serwer jest ostatnią linią obrony.
- **Gdzie Flask szuka szablonów?**
  - W katalogu templates/ obok aplikacji.

## Co potrafię teraz bez patrzenia na przykład?
Budujesz aplikację Flask z trasami, szablonami, formularzem z walidacją po stronie serwera, przekierowaniem po zapisie i stroną z parametrem.

## Źródła (data dostępu w nawiasie)
Wersje narzędzi i dane rynkowe zmieniają się — przed użyciem w pracy otwórz źródło.
- Flask — dokumentacja (3.1.x): Quickstart, szablony, testowanie (dostęp 23.11.2026) — <https://flask.palletsprojects.com/>
- OWASP — SQL Injection Prevention Cheat Sheet (zapytania parametryzowane) (dostęp 23.11.2026) — <https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Kod odpowiedzi po udanym zapisie z redirect:
  - A) 200
  - B) 302
  - C) 400
  - D) 500
- Wartość pola formularza o name="cena":
  - A) request.args["cena"]
  - B) request.form.get("cena")
  - C) form.cena
  - D) request.cena
- Jinja przy {{ nazwa }} z <script>:
  - A) wykona skrypt
  - B) zabezpieczy znaki HTML
  - C) usunie nazwę
  - D) rzuci błąd
- Atrybut required w HTML:
  - A) chroni serwer
  - B) działa tylko w przeglądarce
  - C) jest zbędny
  - D) zastępuje testy

Odpowiedzi: B, B, B, B
