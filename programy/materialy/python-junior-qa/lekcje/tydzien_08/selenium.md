# Selenium WebDriver: przeglądarka, lokatory (ID, CSS, XPath), formularze
Tydzień 8 · lekcja 30 z 39 · ≈ 50 min

**Po tej lekcji potrafisz:** uruchamiasz przeglądarkę z Selenium (Selenium Manager sam dobiera sterownik), otwierasz stronę, znajdujesz elementy lokatorami ID, CSS i XPath, wypełniasz formularz, czytasz tekst, robisz zrzut ekranu i zamykasz przeglądarkę.

**Po co mi to?** Testy E2E w przeglądarce to najczęściej wymieniana umiejętność w ogłoszeniach dla Junior QA Automation. Selenium jest standardem W3C WebDriver od lat.

## Czego potrzebujesz
- Lekcje „Klasy” i „pytest”.
- Przeglądarka Microsoft Edge (wbudowana w Windows 10/11) albo Chrome.
- Sklep testowy z paczki (projekty/sklep_testowy) uruchomiony: `python app.py` → http://127.0.0.1:5001.
- Internet przy pierwszym uruchomieniu (Selenium Manager pobiera sterownik msedgedriver i zapisuje go w pamięci podręcznej).

## 1 · Wyjaśnienie od podstaw
### Jak to działa
Twój skrypt → biblioteka selenium → **sterownik** (msedgedriver/chromedriver) → przeglądarka. Od Selenium 4.6 **Selenium Manager** sam wykrywa wersję przeglądarki i pobiera pasujący sterownik (raz, potem bierze z pamięci podręcznej `~/.cache/selenium`) — nie pobierasz niczego ręcznie.
### Pierwszy skrypt
```
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("http://127.0.0.1:5001")
print(driver.title)
driver.quit()
```
`driver.quit()` zamyka przeglądarkę i sterownik — zawsze, najlepiej w try/finally albo w fixturze z yield.
### Lokatory — jak znaleźć element
Prawy klik na elemencie → **Zbadaj** (DevTools) pokazuje HTML: `<input id="login" name="login" class="pole">`.
| lokator | przykład | kiedy |
|---|---|---|
| `By.ID` | `(By.ID, "login")` | najlepszy, jeśli id jest unikalne i stałe |
| `By.CSS_SELECTOR` | `"#login"`, `".komunikat"`, `"button[type=submit]"`, `"#koszyk .pozycja"` | szybki, czytelny — domyślny wybór |
| `By.XPATH` | `"//button[text()='Zaloguj']"` | gdy trzeba szukać po tekście albo „w górę” drzewa |
| `By.NAME`, `By.LINK_TEXT` | `"login"`, `"Koszyk"` | formularze, linki |
Unikaj kruchych lokatorów: długich ścieżek XPath od korzenia (`/html/body/div[2]/…`) i klas od wyglądu. Najlepsze są atrybuty dla testów, np. `data-test="zaloguj"` → `[data-test=zaloguj]`.
### Akcje
`el = driver.find_element(By.ID, "login")` (brak → NoSuchElementException); `find_elements` — lista (pusta, gdy brak). `el.clear()`, `el.send_keys("tester")`, `el.click()`, `el.text`, `el.get_attribute("value")`, `el.is_displayed()`. `driver.save_screenshot("zrzut.png")` — zrzut do raportu błędu.
### Strony do ćwiczeń
Kurs używa **lokalnego** sklepu testowego z paczki (działa offline, ma celowe defekty do znalezienia). Publiczne strony ćwiczeniowe (np. the-internet.herokuapp.com, saucedemo.com) są opcją dodatkową — mogą się zmienić lub zniknąć.

## 2 · Demonstracja — krok po kroku
**Logowanie do sklepu testowego trzema rodzajami lokatorów**

```
# selenium_start.py — wymaga działającego sklepu testowego (python app.py w projekty/sklep_testowy)
from selenium import webdriver
from selenium.webdriver.common.by import By

ADRES = "http://127.0.0.1:5001"

driver = webdriver.Edge()          # Chrome: webdriver.Chrome()
try:
    driver.get(ADRES + "/logowanie")
    print("Tytuł:", driver.title)
    driver.find_element(By.ID, "login").send_keys("tester")
    driver.find_element(By.CSS_SELECTOR, "input[name=haslo]").send_keys("Test123!")
    driver.find_element(By.XPATH, "//button[text()='Zaloguj']").click()
    powitanie = driver.find_element(By.CSS_SELECTOR, "[data-test=powitanie]").text
    print("Po zalogowaniu:", powitanie)
    produkty = driver.find_elements(By.CSS_SELECTOR, "#produkty .produkt")
    print("Produktów na stronie:", len(produkty))
    driver.save_screenshot("po_zalogowaniu.png")
finally:
    driver.quit()

```

1. Uruchom sklep: terminal Mentora → `cd` do projekty\sklep_testowy → `python app.py` (zostaw okno otwarte). W drugim oknie uruchomisz skrypt.
2. `webdriver.Edge()` — Selenium Manager sprawdza wersję Edge i pobiera msedgedriver (pierwszy raz kilka sekund, potem z pamięci podręcznej). Otwiera się okno przeglądarki z paskiem „sterowana przez oprogramowanie testowe”.
3. `driver.get(...)` — otwiera stronę logowania; `driver.title` — tytuł z `<title>`.
4. `By.ID, "login"` — pole loginu ma `id="login"`; `send_keys` wpisuje tekst.
5. `By.CSS_SELECTOR, "input[name=haslo]"` — pole hasła wskazane atrybutem name.
6. `By.XPATH, "//button[text()='Zaloguj']"` — przycisk po tekście.
7. `[data-test=powitanie]` — element z atrybutem przeznaczonym dla testów; `.text` zwraca widoczny tekst.
8. `find_elements` — lista wszystkich `.produkt` w `#produkty`; `len` = liczba produktów.
9. `save_screenshot` zapisuje PNG w katalogu roboczym; `finally: driver.quit()` zamyka przeglądarkę nawet przy błędzie.

✔ **Oczekiwany wynik:** Tytuł strony, „Po zalogowaniu: Witaj, tester!”, liczba produktów (20) i plik po_zalogowaniu.png.

## 3 · Jak to uruchomić
1. Okno 1 (terminal Mentora): `cd` do materiałów kursu → `cd projekty\sklep_testowy` → `python app.py`.
2. Okno 2: w PRACA `python selenium_start.py`. Pierwsze uruchomienie wymaga internetu (pobranie sterownika).
3. Bez Edge: zamień na `webdriver.Chrome()` (Selenium Manager pobierze Chrome for Testing, jeśli Chrome nie ma).

## W praktyce
- Prośba do programistów: atrybuty data-test w kluczowych elementach — testy przestają się psuć przy zmianie wyglądu.
- Zrzut ekranu przy każdym nieudanym teście E2E.

## 4 · Ćwiczenie prowadzone
HTML: `<button id="dodaj-3" class="btn btn-primary" data-test="dodaj">Dodaj do koszyka</button>`. Na wzór demonstracji wpisz lokatory: (1) po ID, (2) CSS po atrybucie data-test, (3) XPath po tekście. Czas: 15 minut.

📄 `cwiczenia/tydzien_08/selenium_1.md` · rozwiązanie: `rozwiazania/tydzien_08/selenium_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Oceń lokatory (dobry / kruchy): (1) `/html/body/div[2]/div/form/input[1]`; (2) `#login`; (3) `.btn-primary` (na stronie są 4 takie przyciski); (4) `[data-test=koszyk-suma]`. Dodatkowo (5): `find_element` nie znalazł elementu — jaki wyjątek (wybierz)? Czas: 15 minut.

📄 `cwiczenia/tydzien_08/selenium_2.md` · rozwiązanie: `rozwiazania/tydzien_08/selenium_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **selenium.common.exceptions.NoSuchElementException: Unable to locate element**
  - Przyczyna: Zły lokator albo element jeszcze się nie pojawił.
  - Jak sprawdzić: DevTools → Ctrl+F w zakładce Elements → wpisz selektor CSS.
  - Poprawka: Popraw lokator; dla elementów ładowanych później — WebDriverWait (następna lekcja).
- ✘ **SessionNotCreatedException / Unable to obtain driver**
  - Przyczyna: Brak przeglądarki albo brak internetu przy pierwszym pobraniu sterownika.
  - Jak sprawdzić: Czy Edge/Chrome się otwiera? Czy jest internet?
  - Poprawka: Uruchom z internetem raz (sterownik trafi do pamięci podręcznej) albo użyj innej przeglądarki.
- ✘ **ConnectionRefusedError / ERR_CONNECTION_REFUSED na stronie**
  - Przyczyna: Sklep testowy nie jest uruchomiony.
  - Jak sprawdzić: Otwórz http://127.0.0.1:5001 ręcznie.
  - Poprawka: W osobnym oknie `python app.py` w projekty/sklep_testowy.

## Pułapki
- Brak driver.quit() — w tle zostają dziesiątki procesów przeglądarki.
- time.sleep(5) „na wszelki wypadek” — wolne i niepewne testy; czekaj na warunek (WebDriverWait).

## Dodatkowe zadania
1. Pierwszy skrypt: otwórz sklep testowy, zaloguj się, zrób zrzut ekranu.
2. 5 elementów strony znalezionych trzema rodzajami lokatorów.
3. Formularz zamówienia: wypełnij i odczytaj komunikat.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Co robi Selenium Manager?**
  - Sam dobiera i pobiera sterownik (i w razie potrzeby przeglądarkę).
- **Który lokator jest najlepszy?**
  - Unikalny i stały: id albo atrybut data-test.
- **Po co driver.quit()?**
  - Zamyka przeglądarkę i sterownik.

## Co potrafię teraz bez patrzenia na przykład?
Uruchamiasz przeglądarkę z Selenium, znajdujesz elementy lokatorami ID/CSS/XPath, wypełniasz formularze, czytasz tekst, robisz zrzut ekranu i zawsze zamykasz przeglądarkę.

## Źródła (data dostępu w nawiasie)
Wersje narzędzi i dane rynkowe zmieniają się — przed użyciem w pracy otwórz źródło.
- Selenium — Selenium Manager (sterowniki i przeglądarki automatycznie, od 4.6; cache, SE_OFFLINE) (dostęp 23.11.2026) — <https://selenium.dev/documentation/selenium_manager>
- Selenium (Python) — Waits: explicit i implicit (dostęp 23.11.2026) — <https://selenium-python.readthedocs.io/waits.html>
- Selenium — Page object models (test practices) (dostęp 23.11.2026) — <https://selenium.dev/documentation/test_practices/encouraged/page_object_models>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Od której wersji Selenium sam pobiera sterowniki (Selenium Manager)?
  - A) 3.0
  - B) 4.6
  - C) 5.0
  - D) nigdy
- find_elements, gdy nic nie pasuje, zwraca:
  - A) None
  - B) pustą listę
  - C) NoSuchElementException
  - D) False
- Najbardziej kruchy lokator:
  - A) #login
  - B) [data-test=zaloguj]
  - C) /html/body/div[3]/form/input[2]
  - D) input[name=login]
- Tekst widoczny w elemencie:
  - A) el.value
  - B) el.text
  - C) el.html
  - D) el.get()

Odpowiedzi: B, B, C, B
