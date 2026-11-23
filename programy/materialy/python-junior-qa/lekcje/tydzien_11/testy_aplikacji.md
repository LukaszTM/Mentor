# Testy aplikacji webowej: Flask test_client, testy E2E Selenium własnej aplikacji i CI
Tydzień 11 · lekcja 37 z 39 · ≈ 40 min

**Po tej lekcji potrafisz:** testujesz własną aplikację Flask na dwóch poziomach: szybkie testy z test_client (strony, formularze, kody odpowiedzi, baza tymczasowa) i kilka testów E2E w Selenium z Page Object Model na serwerze uruchomionym w fixturze — i łączysz je w CI.

**Po co mi to?** To jest serce projektu portfolio: aplikacja i jej testy na kilku poziomach, zielone w CI. Na rozmowie pokażesz piramidę testów na własnym kodzie.

## Czego potrzebujesz
- Lekcje „Flask”, „WebDriverWait i POM”, „GitHub Actions”.
- Aplikacja Magazyn z funkcją tworzącą aplikację (create_app) albo modułem app.py.

## 1 · Wyjaśnienie od podstaw
### Aplikacja do testów: fabryka z konfiguracją
Testy nie mogą psuć prawdziwej bazy. Wzorzec: `def create_app(sciezka_bazy="magazyn.db"):` tworzy aplikację dla podanej bazy. W testach: `create_app(tmp_path / "test.db")`.
### Poziom 1: test_client (szybko, bez przeglądarki)
```
@pytest.fixture
def klient(tmp_path):
    app = create_app(tmp_path / "test.db")
    return app.test_client()

def test_dodanie_produktu(klient):
    odp = klient.post("/dodaj", data={"nazwa": "Klej", "kategoria": "biuro", "cena": "3.40", "ilosc": "10"})
    assert odp.status_code == 302
    assert "Klej" in klient.get("/").get_data(as_text=True)
```
Sprawdzasz: kody (200/302/400/404), treść strony, komunikaty walidacji, stan bazy po operacji. Dziesiątki takich testów wykonują się w sekundę.
### Poziom 2: E2E w Selenium (mało, ścieżki krytyczne)
Fixture uruchamia serwer w wątku na wolnym porcie (`werkzeug.serving.make_server`), Selenium otwiera przeglądarkę w trybie headless, po teście wszystko zamyka. Page Objecty: `ListaPage`, `DodajPage`, `ProduktPage`. 3 testy: lista się wyświetla, dodanie produktu formularzem, historia produktu.
### CI
W tests.yml najpierw szybkie testy (`pytest tests/unit`), potem E2E (`pytest tests/e2e`) — przy czerwonych jednostkowych nie ma sensu czekać na przeglądarkę. ubuntu-latest ma Chrome; fixture wybiera `webdriver.Chrome` z `--headless=new`, gdy działa w CI (zmienna środowiskowa `CI=true`).
### Co pokazać rekruterowi
Liczby (np. 25 testów jednostkowych/integracyjnych, 3 E2E), zielone CI, raport HTML jako artefakt i sekcję „Jak testuję” w README.

## 2 · Demonstracja — krok po kroku
**Fixtury dla dwóch poziomów testów**

```
# tests/conftest.py (fragment) — serwer aplikacji w wątku dla testów E2E
import os
import threading

import pytest
from selenium import webdriver
from werkzeug.serving import make_server

from app import create_app


@pytest.fixture
def klient(tmp_path):
    return create_app(tmp_path / "test.db").test_client()


@pytest.fixture
def serwer(tmp_path):
    app = create_app(tmp_path / "e2e.db")
    srv = make_server("127.0.0.1", 0, app)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    yield f"http://127.0.0.1:{srv.server_port}"
    srv.shutdown()


@pytest.fixture
def driver():
    if os.environ.get("CI"):
        opcje = webdriver.ChromeOptions()
        opcje.add_argument("--headless=new")
        d = webdriver.Chrome(options=opcje)
    else:
        opcje = webdriver.EdgeOptions()
        opcje.add_argument("--headless=new")
        d = webdriver.Edge(options=opcje)
    yield d
    d.quit()

```

1. `klient(tmp_path)` — aplikacja na świeżej bazie w katalogu tymczasowym i jej test_client: testy jednostkowo-integracyjne bez sieci i przeglądarki.
2. `serwer(tmp_path)` — `make_server("127.0.0.1", 0, app)` z Werkzeug (instalowany razem z Flaskiem); port 0 = wolny port; wątek obsługuje żądania w tle.
3. `yield` adresu → test dostaje np. http://127.0.0.1:53187; po teście `shutdown()` zatrzymuje serwer.
4. `driver` — w CI (zmienna CI ustawiana przez GitHub Actions) Chrome headless, lokalnie Edge headless; po teście quit.
5. Test E2E prosi o oba: `def test_dodanie(serwer, driver): DodajPage(driver, serwer).open().dodaj("Klej", "biuro", "3.40", "10")` i sprawdza, że lista zawiera „Klej”.
6. Każdy test ma własną bazę — kolejność testów nie ma znaczenia.

✔ **Oczekiwany wynik:** Testy test_client wykonują się w ułamku sekundy; 3 testy E2E po kilka sekund; oba poziomy zielone lokalnie i w CI.

## 3 · Jak to uruchomić
1. Struktura: app.py (create_app), tests/conftest.py, tests/test_app.py (test_client), tests/test_e2e.py (Selenium), pages/ (Page Objecty).
2. Lokalnie: `python -m pytest -v tests` (Edge).
3. CI: w tests.yml dwa kroki — `pytest tests/test_app.py`, potem `pytest tests/test_e2e.py`.

## W praktyce
- W README sekcja „Jak testuję”: poziomy, liczba testów, jak uruchomić, link do CI.
- Każdy znaleziony defekt w aplikacji → test test_client odtwarzający go.

## 4 · Ćwiczenie prowadzone
Na wzór demonstracji dobierz fixturę (klient / serwer + driver): (1) test, że POST /dodaj z pustą nazwą daje 400; (2) test, że po kliknięciu „Zapisz” w przeglądarce produkt pojawia się na liście; (3) test, że GET /produkt/999 daje 404. Ile testów będzie wymagać przeglądarki? Czas: 10 minut.

📄 `cwiczenia/tydzien_11/testy_aplikacji_1.md` · rozwiązanie: `rozwiazania/tydzien_11/testy_aplikacji_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Testy E2E przechodzą lokalnie, ale w CI padają z `SessionNotCreatedException`. (1) Najbardziej prawdopodobna przyczyna (wybierz)? (2) Testy jednostkowe dodają produkty do prawdziwego magazyn.db i drugi przebieg pada na UNIQUE — co zmieniasz (wybierz)? (3) W jakiej kolejności uruchamiasz w CI poziomy testów (wybierz)? Czas: 15 minut.

📄 `cwiczenia/tydzien_11/testy_aplikacji_2.md` · rozwiązanie: `rozwiazania/tydzien_11/testy_aplikacji_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **Testy zmieniają prawdziwe dane**
  - Przyczyna: Aplikacja na stałe łączy się z magazyn.db.
  - Jak sprawdzić: Czy create_app przyjmuje ścieżkę bazy?
  - Poprawka: Fabryka aplikacji z parametrem i tmp_path w fixturze.
- ✘ **Test E2E czasem pada: element nie znaleziony**
  - Przyczyna: Brak czekania po przeładowaniu strony.
  - Jak sprawdzić: Zrzut ekranu przy błędzie.
  - Poprawka: WebDriverWait w metodach Page Objectów.

## Pułapki
- Dziesiątki testów E2E dla każdej walidacji — reguły testuj test_clientem.
- Serwer testowy na stałym porcie 5000 — kolizja z działającą aplikacją; port 0.

## Dodatkowe zadania
1. Testy test_client: lista, dodanie, walidacja (400), 404.
2. 3 testy Selenium w POM na serwerze z fixtury.
3. Oba poziomy w GitHub Actions — zielone.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Czym różni się test z test_client od testu Selenium?**
  - test_client wysyła żądania bez przeglądarki (szybko); Selenium klika w prawdziwej przeglądarce (wolniej, pełna ścieżka).
- **Po co create_app(ścieżka_bazy)?**
  - Żeby testy używały tymczasowej bazy.
- **Dlaczego najpierw szybkie testy w CI?**
  - Szybka informacja o błędzie; E2E nie ma sensu przy czerwonych jednostkowych.

## Co potrafię teraz bez patrzenia na przykład?
Testujesz własną aplikację na dwóch poziomach (test_client i Selenium z POM), izolujesz dane bazą tymczasową i uruchamiasz całość w CI.

## Źródła (data dostępu w nawiasie)
Wersje narzędzi i dane rynkowe zmieniają się — przed użyciem w pracy otwórz źródło.
- Flask — dokumentacja (3.1.x): Quickstart, szablony, testowanie (dostęp 23.11.2026) — <https://flask.palletsprojects.com/>
- Selenium — Page object models (test practices) (dostęp 23.11.2026) — <https://selenium.dev/documentation/test_practices/encouraged/page_object_models>
- GitHub Docs — Building and testing Python (actions/checkout@v6, actions/setup-python, pytest) (dostęp 23.11.2026) — <https://docs.github.com/en/actions/tutorials/build-and-test-code/python>
- pytest — How to use fixtures (dostęp 23.11.2026) — <https://docs.pytest.org/en/stable/how-to/fixtures.html>

## Test (w Mentorze: Lekcje → Sprawdź się)
- test_client Flask:
  - A) otwiera przeglądarkę
  - B) wysyła żądania do aplikacji bez serwera i przeglądarki
  - C) testuje CSS
  - D) instaluje Flask
- Serwer testowy na porcie 0 oznacza:
  - A) port 80
  - B) wolny port wybrany przez system
  - C) błąd
  - D) brak sieci
- Ile testów E2E w projekcie portfolio?
  - A) każda reguła
  - B) kilka krytycznych ścieżek
  - C) zero
  - D) 100+
- Testy E2E w CI na ubuntu-latest:
  - A) Edge z oknem
  - B) Chrome headless
  - C) tylko ręcznie
  - D) nie da się

Odpowiedzi: B, B, B, B
