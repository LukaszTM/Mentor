# Biblioteka requests i API: GET, kody HTTP, JSON
Tydzień 5 · lekcja 23 z 39 · ≈ 45 min

**Po tej lekcji potrafisz:** pobierasz dane z API biblioteką requests (GET z parametrami i timeout), sprawdzasz kod odpowiedzi HTTP, czytasz JSON jako słowniki i listy oraz obsługujesz brak połączenia — także na lokalnym serwerze bez internetu.

**Po co mi to?** Testy API to codzienność testera: wysyłasz żądanie, sprawdzasz status, pola i czas odpowiedzi. requests to najpopularniejsza biblioteka HTTP w Pythonie.

## Czego potrzebujesz
- Lekcje „Słowniki”, „Obsługa błędów”, „venv” (requests jest w środowisku kursu).
- Sklep testowy z paczki (projekty/sklep_testowy) — lokalne API bez internetu.

## 1 · Wyjaśnienie od podstaw
### API w jednym zdaniu
API to „okienko” programu dla innych programów: wysyłasz **żądanie** (request) pod adres (endpoint), dostajesz **odpowiedź** (response) — zwykle JSON.
### HTTP: metoda i kod odpowiedzi
GET — pobierz, POST — wyślij/utwórz, PUT/PATCH — zmień, DELETE — usuń. Kod odpowiedzi:
| kod | znaczenie |
|---|---|
| 200 OK | sukces |
| 201 Created | utworzono (po POST) |
| 400 Bad Request | złe dane od klienta |
| 401 / 403 | brak logowania / brak uprawnień |
| 404 Not Found | nie ma takiego zasobu |
| 500 Internal Server Error | błąd serwera — zawsze bug do zgłoszenia |
### requests
```
import requests
odp = requests.get("http://127.0.0.1:5001/api/produkty", params={"kategoria": "biuro"}, timeout=10)
odp.status_code   # 200
dane = odp.json()  # lista słowników
```
`params` dokleja do adresu `?kategoria=biuro`. **Zawsze `timeout`** — bez niego program może czekać w nieskończoność. `odp.raise_for_status()` rzuca wyjątek dla kodów 4xx/5xx.
### Błędy sieci
Brak internetu / serwer wyłączony → `requests.exceptions.ConnectionError`; za długo → `Timeout`. Obie dziedziczą po `requests.exceptions.RequestException` — łapiesz ją i wypisujesz zrozumiały komunikat.
### Lokalne API zamiast internetu
Sklep testowy z paczki kursu uruchomisz poleceniem `python app.py` w projekty/sklep_testowy — API działa pod `http://127.0.0.1:5001/api/produkty`. Publiczne API z internetu (np. open-meteo.com — prognozy pogody bez klucza) to opcja dodatkowa.
### Co sprawdza tester API
Kod odpowiedzi, typ treści (JSON), obecność i typy pól, wartości graniczne parametrów, zachowanie przy złym parametrze (400, nie 500) i czas odpowiedzi.

## 2 · Demonstracja — krok po kroku
**Mini-API na Twoim komputerze i klient requests**

```
import json
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

import requests

PRODUKTY = [{"id": 1, "nazwa": "Zeszyt A5", "cena": 4.5, "kategoria": "zeszyty"},
            {"id": 14, "nazwa": "Segregator A4", "cena": 11.9, "kategoria": "biuro"}]


class Api(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/api/produkty"):
            tresc, kod = json.dumps(PRODUKTY).encode(), 200
        else:
            tresc, kod = b'{"blad": "nie ma"}', 404
        self.send_response(kod)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(tresc)

    def log_message(self, *args):
        pass


serwer = HTTPServer(("127.0.0.1", 0), Api)
threading.Thread(target=serwer.serve_forever, daemon=True).start()
adres = f"http://127.0.0.1:{serwer.server_port}"

odp = requests.get(adres + "/api/produkty", timeout=5)
print(odp.status_code, odp.headers["Content-Type"])
for p in odp.json():
    print(p["id"], p["nazwa"], p["cena"])
print("Brak zasobu:", requests.get(adres + "/api/koszyk", timeout=5).status_code)
serwer.shutdown()
serwer.server_close()
try:
    requests.get(adres + "/api/produkty", timeout=3)
except requests.exceptions.RequestException:
    print("Serwer niedostępny — sprawdź, czy działa i czy adres jest dobry")

```

1. Górna część to mały serwer HTTP z biblioteki standardowej — tylko po to, żeby przykład działał bez internetu i bez sklepu testowego. Nie musisz go umieć pisać.
2. `do_GET` — dla adresu /api/produkty odsyła listę produktów jako JSON z kodem 200, dla innych — 404.
3. `HTTPServer(("127.0.0.1", 0), Api)` — port 0 = system wybiera wolny port; wątek (thread) uruchamia serwer w tle.
4. `requests.get(adres + "/api/produkty", timeout=5)` — żądanie GET z limitem 5 sekund.
5. `odp.status_code` → 200, nagłówek Content-Type → application/json.
6. `odp.json()` zamienia JSON na listę słowników — dalej zwykły Python: pętla i klucze.
7. Nieistniejący zasób → 404 (to nie wyjątek w requests — kod sprawdzasz sam).
8. Po `serwer.shutdown()` i `server_close()` serwer nie odpowiada: requests rzuca ConnectionError (albo Timeout) — oba łapie `RequestException`, a użytkownik dostaje czytelny komunikat. Tak samo zachowa się program bez internetu.

✔ **Oczekiwany wynik:** 200 application/json, dwa produkty, „Brak zasobu: 404” i komunikat „Serwer niedostępny — …”.

## 3 · Jak to uruchomić
1. Zapisz jako api_demo.py → ▶ Uruchom (działa offline).
2. Sklep testowy: terminal Mentora → `cd projekty\sklep_testowy` (w materiałach kursu) → `python app.py` → w przeglądarce http://127.0.0.1:5001/api/produkty.

## W praktyce
- Test API: status, Content-Type, pola i typy, przypadek negatywny, czas odpowiedzi.
- W bug raporcie API: metoda, pełny adres z parametrami, treść żądania, kod i treść odpowiedzi.

## 4 · Ćwiczenie prowadzone
Dopasuj kod odpowiedzi: (1) GET /api/produkty — lista OK; (2) POST nowego zamówienia — utworzone; (3) GET /api/produkty/999 — brak produktu; (4) serwer rzucił wyjątek przy dzieleniu przez zero; (5) POST z ilością „abc” — serwer odrzucił dane. Opcje: 200, 201, 400, 404, 500. Czas: 10 minut.

📄 `cwiczenia/tydzien_05/requests_1.md` · rozwiązanie: `rozwiazania/tydzien_05/requests_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Testujesz API sklepu: GET /api/produkty?kategoria=xyz (nieistniejąca kategoria) zwraca 500 i stronę z tracebackiem. (1) Czy to błąd do zgłoszenia (tak/nie)? (2) Jaki kod byłby właściwy — wybierz: 200 z pustą listą / 404 / 500. (3) Czego zabrakło w kodzie klienta, który przy wyłączonym serwerze „zawiesił się” na 2 minuty (wpisz nazwę argumentu)? Czas: 15 minut.

📄 `cwiczenia/tydzien_05/requests_2.md` · rozwiązanie: `rozwiazania/tydzien_05/requests_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **requests.exceptions.ConnectionError: … Failed to establish a new connection**
  - Przyczyna: Serwer nie działa / brak internetu / zły port.
  - Jak sprawdzić: Otwórz adres w przeglądarce.
  - Poprawka: Uruchom serwer (python app.py) albo sprawdź adres; łap RequestException.
- ✘ **requests.exceptions.JSONDecodeError: Expecting value**
  - Przyczyna: Odpowiedź nie jest JSON-em (np. strona błędu HTML).
  - Jak sprawdzić: `print(odp.status_code, odp.text[:200])`.
  - Poprawka: Sprawdź status przed .json().
- ✘ **KeyError: 'temperature' przy czytaniu JSON**
  - Przyczyna: Inna struktura odpowiedzi niż zakładasz.
  - Jak sprawdzić: `print(json.dumps(dane, indent=2)[:500])`.
  - Poprawka: Dopasuj klucze do prawdziwej odpowiedzi; używaj .get().

## Pułapki
- Brak timeout — program może czekać bez końca.
- Klucze API w kodzie — tylko w zmiennych środowiskowych/.env (poza repo).

## Dodatkowe zadania
1. Pobierz produkty z lokalnego API sklepu i wypisz 3 pola.
2. Obsłuż wyłączony serwer czytelnym komunikatem.
3. Zapisz wybrane dane z API do CSV z datą.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Co oznacza 404, a co 500?**
  - 404 — brak zasobu; 500 — błąd serwera.
- **Po co timeout?**
  - Żeby program nie czekał w nieskończoność.
- **Co zwraca odp.json()?**
  - Dane JSON zamienione na słowniki/listy Pythona.

## Co potrafię teraz bez patrzenia na przykład?
Wysyłasz żądania GET z parametrami i timeout, rozumiesz kody HTTP, czytasz JSON i obsługujesz błędy sieci — także na lokalnym serwerze.

## Źródła (data dostępu w nawiasie)
Wersje narzędzi i dane rynkowe zmieniają się — przed użyciem w pracy otwórz źródło.
- Python — json: JSON encoder and decoder (dostęp 23.11.2026) — <https://docs.python.org/3/library/json.html>
- Flask — dokumentacja (3.1.x): Quickstart, szablony, testowanie (dostęp 23.11.2026) — <https://flask.palletsprojects.com/>
- Python — Poradnik: Błędy i wyjątki (dostęp 23.11.2026) — <https://docs.python.org/pl/3/tutorial/errors.html>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Kod 201 oznacza:
  - A) OK
  - B) Created
  - C) Not Found
  - D) Server Error
- requests.get(url) bez timeout:
  - A) kończy się po 1 s
  - B) może czekać bez końca
  - C) nie działa
  - D) zawsze 200
- Serwer zwraca 500 przy złym parametrze. To:
  - A) poprawne
  - B) błąd serwera do zgłoszenia
  - C) błąd klienta
  - D) brak internetu
- Wyjątek łapiący błędy sieci w requests:
  - A) ValueError
  - B) requests.exceptions.RequestException
  - C) KeyError
  - D) OSError tylko

Odpowiedzi: B, B, B, B
