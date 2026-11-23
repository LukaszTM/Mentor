# WebDriverWait i Page Object Model
Tydzień 8 · lekcja 31 z 39 · ≈ 50 min

**Po tej lekcji potrafisz:** czekasz na elementy WebDriverWait z expected_conditions zamiast time.sleep, budujesz Page Object (klasa strony z lokatorami i metodami akcji) i piszesz testy pytest, które używają fixtury przeglądarki i stron — czytelne jak scenariusz.

**Po co mi to?** Niestabilne (flaky) testy E2E to największy problem automatyzacji; czekanie na warunek i POM to odpowiedź, o którą zapyta każdy rekruter QA Automation.

## Czego potrzebujesz
- Lekcje „Selenium WebDriver”, „Klasy”, „parametrize i fixtures”.
- Sklep testowy uruchomiony (python app.py).

## 1 · Wyjaśnienie od podstaw
### Dlaczego czekać
Strona ładuje się asynchronicznie: element pojawia się po 0,3 s albo po 2 s. `find_element` od razu → NoSuchElementException. `time.sleep(3)` — za krótko na wolnym komputerze, za długo na szybkim.
### Czekanie jawne (explicit wait)
```
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

czekaj = WebDriverWait(driver, 10)
el = czekaj.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".promocja")))
```
Sprawdza warunek co 0,5 s, maksymalnie 10 s; zwraca element, gdy warunek spełniony, albo rzuca **TimeoutException**. Najczęstsze warunki:
| warunek | czeka, aż |
|---|---|
| `presence_of_element_located` | element jest w HTML |
| `visibility_of_element_located` | element jest widoczny |
| `element_to_be_clickable` | widoczny i aktywny |
| `text_to_be_present_in_element` | ma dany tekst |
| `url_contains` | adres zawiera fragment |
Czekanie domyślne (implicit, `driver.implicitly_wait(5)`) działa dla każdego find_element — dokumentacja Selenium odradza mieszanie go z jawnym. W kursie: tylko jawne.
### Page Object Model (POM)
Każda strona = klasa: lokatory w jednym miejscu, metody to działania użytkownika.
```
class LoginPage:
    LOGIN = (By.ID, "login")
    HASLO = (By.ID, "haslo")
    ZALOGUJ = (By.CSS_SELECTOR, "[data-test=zaloguj]")
    BLAD = (By.CSS_SELECTOR, "[data-test=blad]")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(ADRES + "/logowanie")
        return self

    def login(self, login, haslo):
        ...

    def error_text(self):
        ...
```
Test mówi **co** (`LoginPage(driver).open().login("tester", "zle")`), strona wie **jak**. Zmiana id pola = poprawka w jednym miejscu, nie w 30 testach. Asercje trzymasz w testach, nie w klasach stron.
### Fixture przeglądarki
W conftest.py: `@pytest.fixture def driver(): d = webdriver.Edge(); yield d; d.quit()` — każdy test dostaje świeżą przeglądarkę i zawsze ją zamyka. Tryb bez okna (headless, przydatny w CI): `opcje = webdriver.EdgeOptions(); opcje.add_argument("--headless=new")`.

## 2 · Demonstracja — krok po kroku
**LoginPage z czekaniem i dwa testy-scenariusze**

```
# pages/login_page.py + tests/test_logowanie.py (w jednym pliku dla czytelności)
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

ADRES = "http://127.0.0.1:5001"


class LoginPage:
    LOGIN = (By.ID, "login")
    HASLO = (By.ID, "haslo")
    ZALOGUJ = (By.CSS_SELECTOR, "[data-test=zaloguj]")
    BLAD = (By.CSS_SELECTOR, "[data-test=blad]")
    POWITANIE = (By.CSS_SELECTOR, "[data-test=powitanie]")

    def __init__(self, driver):
        self.driver = driver
        self.czekaj = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(ADRES + "/logowanie")
        return self

    def login(self, login, haslo):
        self.czekaj.until(EC.visibility_of_element_located(self.LOGIN)).send_keys(login)
        self.driver.find_element(*self.HASLO).send_keys(haslo)
        self.driver.find_element(*self.ZALOGUJ).click()
        return self

    def error_text(self):
        return self.czekaj.until(EC.visibility_of_element_located(self.BLAD)).text

    def greeting(self):
        return self.czekaj.until(EC.visibility_of_element_located(self.POWITANIE)).text


@pytest.fixture
def driver():
    opcje = webdriver.EdgeOptions()
    opcje.add_argument("--headless=new")
    d = webdriver.Edge(options=opcje)
    yield d
    d.quit()


def test_logowanie_poprawne(driver):
    assert "tester" in LoginPage(driver).open().login("tester", "Test123!").greeting()


def test_bledne_haslo(driver):
    assert "Błędny login lub hasło" in LoginPage(driver).open().login("tester", "zle").error_text()

```

1. Lokatory jako atrybuty klasy (krotki `(By…, "…")`) — jedno miejsce do zmiany.
2. `self.czekaj = WebDriverWait(driver, 10)` — jeden obiekt czekania na stronę.
3. `open()` zwraca `self` — dzięki temu można łączyć: `LoginPage(d).open().login(...)`.
4. `login()` czeka, aż pole loginu będzie widoczne, potem wpisuje dane i klika.
5. `find_element(*self.HASLO)` — gwiazdka rozpakowuje krotkę na dwa argumenty (By.ID, "haslo").
6. `error_text()` i `greeting()` czekają na komunikat — po kliknięciu strona się przeładowuje.
7. Fixture `driver` z headless i yield → quit zawsze, także po FAILED.
8. Testy czytają się jak zdanie; asercje są w testach, nie w klasie strony.
9. Uruchom: `python -m pytest -v` (sklep musi działać) → 2 passed.

✔ **Oczekiwany wynik:** 2 passed: logowanie poprawne (powitanie zawiera „tester”) i błędne hasło (komunikat „Błędny login lub hasło”).

## 3 · Jak to uruchomić
1. Struktura w PRACA: `pages/__init__.py` (pusty), `pages/login_page.py`, `tests/test_logowanie.py`, `conftest.py` z fixturą driver.
2. Okno 1: sklep testowy `python app.py`; okno 2 w PRACA: `python -m pytest -v`.
3. Chcesz widzieć przeglądarkę? Usuń linię z `--headless=new`.

## W praktyce
- Każdy nowy ekran aplikacji = nowa klasa strony.
- Test flaky w CI: najpierw zrzut i lokator, potem warunek czekania — nigdy sleep.

## 4 · Ćwiczenie prowadzone
Na wzór LoginPage zaprojektuj CartPage koszyka. Wpisz: (1) lokator CSS sumy koszyka z atrybutem data-test="suma"; (2) warunek EC, na który czekasz przed odczytem tekstu sumy; (3) co zwraca metoda add(…) w stylu demonstracji, żeby dało się łączyć wywołania. Czas: 15 minut.

📄 `cwiczenia/tydzien_08/wait_pom_1.md` · rozwiązanie: `rozwiazania/tydzien_08/wait_pom_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Test czasem pada (flaky): `driver.find_element(By.ID, "promocja")` zaraz po get(); promocja pokazuje się po ok. 1,5 s. Wybierz: (1) najlepsza poprawka: time.sleep(5) / WebDriverWait(driver, 10).until(EC.visibility_of_element_located(...)) / implicitly_wait(60); (2) jaki wyjątek, jeśli promocja nie pojawi się w 10 s; (3) gdzie umieścisz asercję „promocja zawiera −10%”: w metodzie klasy strony / w teście. Czas: 15 minut.

📄 `cwiczenia/tydzien_08/wait_pom_2.md` · rozwiązanie: `rozwiazania/tydzien_08/wait_pom_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **selenium.common.exceptions.TimeoutException: Message:**
  - Przyczyna: Warunek nie spełnił się w czasie: zły lokator albo element naprawdę się nie pojawił (bug?).
  - Jak sprawdzić: Zrzut ekranu w momencie błędu; sprawdź lokator w DevTools.
  - Poprawka: Popraw lokator; jeśli element powinien być — zgłoś defekt.
- ✘ **ElementClickInterceptedException**
  - Przyczyna: Inny element (baner, okno) zasłania przycisk.
  - Jak sprawdzić: Zrzut ekranu.
  - Poprawka: Zamknij baner w kroku testu albo czekaj element_to_be_clickable.
- ✘ **StaleElementReferenceException**
  - Przyczyna: Strona się przeładowała, a używasz starego elementu.
  - Jak sprawdzić: Czy po kliknięciu była nawigacja?
  - Poprawka: Znajdź element ponownie po przeładowaniu (metoda strony za każdym razem szuka od nowa).

## Pułapki
- Asercje w Page Objectach — klasa przestaje być wielokrotnego użytku.
- Testy E2E zależne od siebie (test 2 korzysta z koszyka testu 1) — każdy test zaczyna od czystego stanu.

## Dodatkowe zadania
1. Formularz zamówienia z WebDriverWait — bez time.sleep.
2. Page Object LoginPage z metodami open(), login(), error_text().
3. 5 testów E2E sklepu w POM z fixturą driver.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Dlaczego nie time.sleep?**
  - Za krótki albo za długi; czekanie na warunek jest szybsze i pewniejsze.
- **Co zawiera Page Object?**
  - Lokatory i metody akcji jednej strony — bez asercji.
- **Co rzuca WebDriverWait po przekroczeniu czasu?**
  - TimeoutException.

## Co potrafię teraz bez patrzenia na przykład?
Czekasz na warunki WebDriverWait, budujesz Page Objecty i piszesz stabilne testy E2E z fixturą przeglądarki, czytelne jak scenariusz.

## Źródła (data dostępu w nawiasie)
Wersje narzędzi i dane rynkowe zmieniają się — przed użyciem w pracy otwórz źródło.
- Selenium (Python) — Waits: explicit i implicit (dostęp 23.11.2026) — <https://selenium-python.readthedocs.io/waits.html>
- Selenium Python API — selenium.webdriver.support.wait (WebDriverWait) (dostęp 23.11.2026) — <https://www.selenium.dev/selenium/docs/api/py/selenium_webdriver_support/selenium.webdriver.support.wait.html>
- Selenium — Page object models (test practices) (dostęp 23.11.2026) — <https://selenium.dev/documentation/test_practices/encouraged/page_object_models>
- pytest — How to use fixtures (dostęp 23.11.2026) — <https://docs.pytest.org/en/stable/how-to/fixtures.html>

## Test (w Mentorze: Lekcje → Sprawdź się)
- WebDriverWait(driver, 10).until(...) sprawdza warunek:
  - A) raz po 10 s
  - B) co ok. 0,5 s do 10 s
  - C) w nieskończoność
  - D) tylko raz
- W POM asercje umieszczasz:
  - A) w klasach stron
  - B) w testach
  - C) w conftest.py
  - D) nigdzie
- Element przykryty banerem przy click():
  - A) NoSuchElementException
  - B) ElementClickInterceptedException
  - C) TimeoutException
  - D) ValueError
- Fixture driver z yield gwarantuje:
  - A) szybszy test
  - B) zamknięcie przeglądarki po teście
  - C) brak błędów
  - D) tryb headless

Odpowiedzi: B, B, B, B
