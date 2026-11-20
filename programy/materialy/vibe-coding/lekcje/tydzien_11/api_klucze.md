# API i klucze: pobierasz dane z internetu i nie zdradzasz sekretów
Tydzień 11 · lekcja 34 z 48 · ≈ 50 min

**Po tej lekcji potrafisz:** wywołujesz API z Pythona (requests z timeoutem i obsługą błędów), trzymasz klucz w zmiennej środowiskowej zamiast w kodzie i reagujesz, gdy klucz wycieknie.

**Po co mi to?** Pogoda, kursy walut, mapy, SMS — aplikacje korzystają z cudzych usług przez API z kluczem. Klucz w kodzie na GitHubie to realne koszty i włamania; agent chętnie wpisuje klucz „na sztywno”.

## Czego potrzebujesz
- Biblioteka requests (instaluje Mentor).
- Lekcje „Aplikacja Flask” i „GitHub”.

## 1 · Wyjaśnienie od podstaw
### API w jednym zdaniu
API to adres, pod który program wysyła pytanie i dostaje odpowiedź w JSON. Przykład: `GET https://api.pogoda.example/v1/current?miasto=Radzyń&key=…` → `{"current": {"temp": 4.5}}` (usługa w kursie jest fikcyjna — prawdziwe API mają własną dokumentację).
### requests — wywołanie z bezpiecznikami
```
import requests
odp = requests.get(URL, params={"miasto": miasto}, headers={"X-API-Key": klucz}, timeout=10)
odp.raise_for_status()      # 4xx/5xx → wyjątek
dane = odp.json()
```
- `timeout=10` — bez niego program może czekać w nieskończoność (dokumentacja requests zaleca zawsze ustawiać timeout).
- `raise_for_status()` — błąd HTTP jako wyjątek, a nie „cicha” zła odpowiedź.
- Klucz w nagłówku (`headers`) albo w `params`, zależnie od dokumentacji usługi.
### Klucz poza kodem: zmienna środowiskowa
Kod czyta: `klucz = os.environ.get("POGODA_API_KEY")`; brak → czytelny błąd „Ustaw zmienną POGODA_API_KEY”. Ustawienie w Windows:
| gdzie | polecenie | jak długo |
|---|---|---|
| CMD (terminal Mentora) | `set POGODA_API_KEY=twoj_klucz` | do zamknięcia okna |
| PowerShell | `$env:POGODA_API_KEY="twoj_klucz"` | do zamknięcia okna |
| trwale | `setx POGODA_API_KEY "twoj_klucz"` | w NOWYCH oknach (bieżące nie widzi) |
Plik `.env` z liniami `NAZWA=wartość` to popularna wygoda (biblioteka python-dotenv) — ale wtedy `.env` MUSI być w .gitignore i w regułach deny agenta (tydzień 12).
### Gdy klucz wycieknie
- Unieważnij (revoke/rotate) klucz w panelu usługi NATYCHMIAST — usunięcie z kodu nie wystarczy (historia Gita, kopie, boty skanujące GitHub).
- Wygeneruj nowy, ustaw w zmiennej środowiskowej.
- Sprawdź rachunek/zużycie w panelu usługi.
- GitHub skanuje publiczne repozytoria pod kątem znanych formatów kluczy (secret scanning) i może zablokować push z kluczem — to siatka, nie strategia.
### Testy bez internetu
Funkcja przyjmuje opcjonalny parametr `klient` (funkcję wykonującą zapytanie). W testach podajesz fałszywego klienta zwracającego przygotowany JSON — test działa bez sieci i bez klucza, a Ty sprawdzasz też, czy funkcja przekazała klucz i obsłużyła błąd.

## 2 · Demonstracja — krok po kroku
**Agent wpisał klucz w kod — sprzątanie**

```
import os


def pobierz_temperature(miasto, klient=None):
    klucz = os.environ.get("POGODA_API_KEY")
    if not klucz:
        raise RuntimeError("Ustaw zmienną środowiskową POGODA_API_KEY")
    if klient is None:
        import requests
        def klient(url, params, headers):
            odp = requests.get(url, params=params, headers=headers, timeout=10)
            odp.raise_for_status()
            return odp.json()
    dane = klient("https://api.pogoda.example/v1/current", {"miasto": miasto}, {"X-API-Key": klucz})
    return float(dane["current"]["temp"])


os.environ["POGODA_API_KEY"] = "test-123"   # tylko na potrzeby przykładu!
print(pobierz_temperature("Radzyń", klient=lambda u, p, h: {"current": {"temp": 4.5}}))

```

1. Prośba „dodaj pobieranie pogody, klucz: abc…” — błąd już w prośbie: klucz trafił do rozmowy. Agent wpisał `API_KEY = "abc…"` w pogoda.py.
2. Zanim zrobisz commit: przegląd diffu (pytanie 4 — tajemnice) łapie klucz. Poprawka: os.environ.get + RuntimeError z instrukcją; `set POGODA_API_KEY=…` w terminalu.
3. Klucz był w rozmowie z agentem (serwery dostawcy) — dla bezpieczeństwa generujesz nowy w panelu usługi i stary unieważniasz.
4. Test z fałszywym klientem: sprawdza temperaturę, przekazanie klucza w nagłówku, RuntimeError bez zmiennej — bez internetu.
5. Zasada w AGENTS.md: „Klucze tylko ze zmiennych środowiskowych; nigdy w kodzie, testach ani README”.

✔ **Oczekiwany wynik:** Klucz poza kodem i historią Gita, unieważniony po kontakcie z rozmową, funkcja przetestowana bez sieci.

## 3 · Jak to uruchomić
1. CMD: `set POGODA_API_KEY=…` → `python pogoda.py` w tym samym oknie.
2. Zadanie tygodnia → „✔ Sprawdź wynik” (testy z fałszywym klientem, bez internetu i bez klucza).

## W praktyce
- Każdy klucz: zmienna środowiskowa + .gitignore + reguła deny agenta.
- Raz w miesiącu przegląd aktywnych kluczy w panelach usług.

## 4 · Ćwiczenie prowadzone
W terminalu Mentora wpisujesz `setx POGODA_API_KEY "k123"`, a potem w TYM SAMYM oknie `python pogoda.py` → RuntimeError „Ustaw zmienną…”. (1) Dlaczego? Wybierz: setx działa w nowych oknach / setx nie działa w Windows. (2) Jakie polecenie CMD ustawi zmienną w bieżącym oknie? (3) Jaką wartość domyślną ma timeout w requests, jeśli go nie podasz: brak (czeka bez końca) czy 30 s? Czas: 15 minut.

📄 `cwiczenia/tydzien_11/api_klucze_1.md` · rozwiązanie: `rozwiazania/tydzien_11/api_klucze_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Klucz API trafił do publicznego repozytorium 2 dni temu; usunąłeś go nowym commitem. Uporządkuj działania: A) unieważnij klucz w panelu usługi, B) wygeneruj nowy i ustaw w zmiennej środowiskowej, C) sprawdź zużycie/rachunek w panelu, D) dopisz zasadę do AGENTS.md. Kolejność liter. Czy usunięcie pliku w nowym commicie usunęło klucz z historii (tak/nie)? Czas: 15 minut.

📄 `cwiczenia/tydzien_11/api_klucze_2.md` · rozwiązanie: `rozwiazania/tydzien_11/api_klucze_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **„requests.exceptions.ConnectTimeout” albo program wisi.**
  - Przyczyna: Brak sieci, usługa nie odpowiada, brak timeout.
  - Jak sprawdzić: Czy timeout jest ustawiony?
  - Poprawka: timeout=10 i obsługa wyjątku z czytelnym komunikatem („usługa pogody nie odpowiada”).
- ✘ **„401 Unauthorized” / „403 Forbidden”.**
  - Przyczyna: Zły/nieaktywny klucz albo zły sposób przekazania (nagłówek vs parametr).
  - Jak sprawdzić: Dokumentacja usługi: jak przekazać klucz.
  - Poprawka: Sprawdź zmienną (echo %POGODA_API_KEY% — tylko u siebie!), sposób przekazania, aktywację klucza.
- ✘ **GitHub odrzuca push: „Push cannot contain secrets”.**
  - Przyczyna: Ochrona przed wypchnięciem sekretu (push protection).
  - Jak sprawdzić: Który plik i linia?
  - Poprawka: Usuń klucz z commita (zanim trafi do historii), unieważnij go, ustaw w zmiennej.

## Pułapki
- Nie wklejaj kluczy do rozmowy z agentem ani czatem. Jeśli wkleiłeś — traktuj klucz jako ujawniony.
- Klucz w JavaScript na stronie publicznej jest jawny dla każdego gościa (F12) — klucze do płatnych usług tylko po stronie serwera.

## Dodatkowe zadania
1. Zbuduj pogoda.py z kluczem ze zmiennej i testem z fałszywym klientem (zadanie tygodnia).
2. Dopisz .env do .gitignore (jeśli jeszcze nie ma).
3. Zasada o kluczach w AGENTS.md.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Gdzie trzymasz klucz API?**
  - W zmiennej środowiskowej (lub w .env poza Gitem), nigdy w kodzie.
- **Co robisz po wycieku klucza?**
  - Unieważniam go, generuję nowy, sprawdzam zużycie, dopisuję zasadę.
- **Po co timeout w requests?**
  - Żeby program nie czekał bez końca na odpowiedź.

## Co potrafię teraz bez patrzenia na przykład?
Wywołujesz API z timeoutem i obsługą błędów, trzymasz klucz w zmiennej środowiskowej, testujesz bez sieci i wiesz, co robić po wycieku.

## Źródła (data dostępu w nawiasie)
Narzędzia, ceny i przepisy zmieniają się — przed użyciem w pracy otwórz źródło.
- Requests — Quickstart (params, timeout, raise_for_status) (dostęp 20.11.2026) — <https://requests.readthedocs.io/en/latest/user/quickstart/>
- Python — os.environ (zmienne środowiskowe) (dostęp 20.11.2026) — <https://docs.python.org/3/library/os.html#os.environ>
- Microsoft Learn — setx (trwałe zmienne środowiskowe w Windows) (dostęp 20.11.2026) — <https://learn.microsoft.com/windows-server/administration/windows-commands/setx>
- OWASP — Secrets Management Cheat Sheet (dostęp 20.11.2026) — <https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Klucz API w kodzie na GitHubie:
  - A) W porządku w repo prywatnym na zawsze
  - B) Ryzyko — unieważnij i przenieś do zmiennej środowiskowej
  - C) Wymóg API
  - D) Przyspiesza
- `set NAZWA=wartość` w CMD działa:
  - A) Na zawsze
  - B) Do zamknięcia okna
  - C) Tylko w PowerShell
  - D) Po restarcie
- Dlaczego testy API z fałszywym klientem?
  - A) Bo są ładniejsze
  - B) Działają bez sieci i klucza, sprawdzają obsługę danych i błędów
  - C) Bo API jest płatne zawsze
  - D) Nie ma powodu
- `odp.raise_for_status()` robi:
  - A) Nic
  - B) Zamienia odpowiedź 4xx/5xx w wyjątek
  - C) Ponawia zapytanie
  - D) Usuwa klucz

Odpowiedzi: B, B, B, B
