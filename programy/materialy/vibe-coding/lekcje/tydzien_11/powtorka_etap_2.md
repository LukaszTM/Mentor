# Powtórka etapu 2: aplikacja „wolne pokoje” — strona, API, dane
Tydzień 11 · lekcja 36 z 48 · ≈ 45 min

**Po tej lekcji potrafisz:** łączysz moduły z etapów 1–2 w działającą funkcję aplikacji: trasa /api/wolne korzysta z kalendarz.py, obsługuje złe daty kodem 400 i jest przetestowana — i oceniasz gotowość do etapu jakości.

**Po co mi to?** Prawdziwe zlecenia to łączenie kawałków. Integracja ujawnia błędy, których nie widać w pojedynczych modułach (formaty dat, nazwy pól, kody błędów).

## Czego potrzebujesz
- Wszystkie lekcje tygodni 8–11.
- kalendarz.py (tydzień 7) i app.py (tydzień 10) w PRACA.

## 1 · Wyjaśnienie od podstaw
### Lista kontrolna etapu 2
| umiejętność | sprawdzian |
|---|---|
| testy | piszesz testy ze specyfikacji, łapiesz mutanty |
| debugowanie | 5 kroków, minimalny przykład, test regresji |
| refaktoryzacja | pod osłoną testów, bez zmiany zachowania |
| strona | lang, viewport, label, alt; JS z walidacją; Pages |
| dane | polski CSV, JSON, raport sprawdzony ręcznie |
| Flask | create_app, 200/400/404, test_client |
| baza | SQL z ?, reguły tabeli, :memory: w testach |
| API i klucze | timeout, raise_for_status, zmienna środowiskowa |
| automatyzacje | tryb próby, bez nadpisywania, log |
### Mini-projekt: /api/wolne
Specyfikacja (dopisz do app.py, nie psując /api/cena):
- `GET /api/wolne?od=2026-12-21&do=2026-12-22` → 200 i `{"od": "2026-12-21", "do": "2026-12-22", "wolne": ["Dębowy", "Klonowy"]}`.
- Rezerwacje: `create_app(rezerwacje=None)` — lista przekazana przy tworzeniu aplikacji (testy podają własną); domyślnie pusta lista.
- Brak parametru, zła data ("2026-13-01", "jutro"), do ≤ od → 400 i `{"blad": "…"}`.
- Logika wyłącznie z kalendarz.wolne_pokoje — bez kopiowania kodu do trasy.
### Na co patrzeć przy integracji
- Format danych na granicy modułów: daty jako napisy RRRR-MM-DD w API, `date` w środku kalendarza.
- Wyjątki z niższych warstw (ValueError z noce/fromisoformat) zamieniane na 400 w jednym miejscu.
- Stare testy (/api/cena) dalej zielone — integracja nie może psuć tego, co działało.
### Co dalej
Etap 3: bezpieczeństwo kodu i agenta, prawo, przegląd, dokumentacja, CI, praca z klientem i projekt końcowy — rozbudowa właśnie tej aplikacji.

## 2 · Demonstracja — krok po kroku
**Integracja ujawnia błąd granicy modułów**

```
@app.route("/api/wolne")
def wolne():
    od, do = request.args.get("od"), request.args.get("do")
    try:
        noce(od, do)                         # walidacja dat i kolejności
        pokoje = wolne_pokoje(rezerwacje, od, do)
    except (TypeError, ValueError):
        return jsonify({"blad": "podaj od i do jako RRRR-MM-DD, do po od"}), 400
    return jsonify({"od": od, "do": do, "wolne": pokoje})
```

1. Agent dodał /api/wolne. Test z dobrymi datami — zielony.
2. Test bez parametru `do`: 500 TypeError — noce(od, None) wywołało fromisoformat(None), a trasa łapała tylko ValueError.
3. Poprawka: łapanie (TypeError, ValueError) w trasie — jeden punkt zamiany błędów na 400.
4. Test daty „2026-13-01” → 400 ✔. Test /api/cena — nadal zielony ✔.
5. Commit „Dodaj /api/wolne z walidacją dat (400)”, push.

✔ **Oczekiwany wynik:** Nowa trasa korzysta z gotowego modułu, wszystkie złe dane dają 400, stare funkcje działają — sprawdzone testami.

## 3 · Jak to uruchomić
1. Zadanie tygodnia „/api/wolne” → „✔ Sprawdź wynik” (testy użyją create_app(rezerwacje=[…])).

## W praktyce
- Integracja = testy na granicy modułów.
- Jeden punkt tłumaczenia wyjątków na kody HTTP.

## 4 · Ćwiczenie prowadzone
Dla rezerwacji [Lipowy 20–23.12, Klonowy 22–27.12] podaj liczbę wolnych pokoi z odpowiedzi /api/wolne dla: (1) od=2026-12-21&do=2026-12-22, (2) od=2026-12-23&do=2026-12-25, (3) od=2026-12-25&do=2026-12-24 — tu podaj kod odpowiedzi. Czas: 15 minut.

📄 `cwiczenia/tydzien_11/powtorka_etap_2_1.md` · rozwiązanie: `rozwiazania/tydzien_11/powtorka_etap_2_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Samoocena: ile pozycji z listy kontrolnej etapu 2 (9) oceniasz na „umiem” z dowodem? Wpisz liczbę (każda odpowiedź 0–9 jest poprawna jako samoocena — zapisz ją też w dzienniku). Pytanie kontrolne: jaki kod HTTP zwróci dobrze napisana trasa, gdy wyjątek z niższej warstwy wynika ze złych danych użytkownika? Czas: 15 minut.

📄 `cwiczenia/tydzien_11/powtorka_etap_2_2.md` · rozwiązanie: `rozwiazania/tydzien_11/powtorka_etap_2_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **500 przy braku parametru.**
  - Przyczyna: Łapany tylko ValueError, a None daje TypeError.
  - Jak sprawdzić: Test bez parametru.
  - Poprawka: Łap (TypeError, ValueError) albo sprawdź None jawnie.
- ✘ **Testy /api/cena czerwone po dodaniu /api/wolne.**
  - Przyczyna: Zmieniona sygnatura create_app albo importy.
  - Jak sprawdzić: Diff app.py.
  - Poprawka: create_app(rezerwacje=None) z wartością domyślną — stare wywołania create_app() działają.

## Pułapki
- Nie kopiuj logiki kalendarza do trasy — dwie kopie rozjadą się przy pierwszej zmianie.
- Lista rezerwacji jako argument domyślny create_app(rezerwacje=[]) — pułapka mutowalnej wartości domyślnej; użyj None.

## Dodatkowe zadania
1. Dodaj /api/wolne z testami (zadanie tygodnia).
2. Samoocena etapu 2.
3. Quiz tygodnia 11.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Gdzie zamieniasz wyjątki ze złych danych na 400?**
  - W jednym miejscu — w trasie, która przyjmuje dane od użytkownika.
- **Po co rezerwacje jako parametr create_app?**
  - Żeby testy mogły podać własne dane bez globalnego stanu.
- **Co sprawdzasz po integracji oprócz nowej trasy?**
  - Że stare testy (np. /api/cena) dalej przechodzą.

## Co potrafię teraz bez patrzenia na przykład?
Połączyłeś kalendarz z aplikacją Flask w trasie z walidacją i testami, sprawdziłeś, że nic się nie zepsuło, i oceniłeś gotowość do etapu jakości.

## Źródła (data dostępu w nawiasie)
Narzędzia, ceny i przepisy zmieniają się — przed użyciem w pracy otwórz źródło.
- Flask — Quickstart (trasy, request.args, jsonify, tryb debug) (dostęp 20.11.2026) — <https://flask.palletsprojects.com/en/stable/quickstart/>
- Flask — Testing Flask Applications (test_client) (dostęp 20.11.2026) — <https://flask.palletsprojects.com/en/stable/testing/>
- Claude Code — Best practices (test-driven, weryfikacja) (dostęp 19.11.2026) — <https://code.claude.com/docs/en/best-practices>

## Test (w Mentorze: Lekcje → Sprawdź się)
- /api/wolne bez parametru „do” powinno zwrócić:
  - A) 200
  - B) 400
  - C) 500
  - D) 404
- create_app(rezerwacje=None) zamiast rezerwacje=[] chroni przed:
  - A) SQL injection
  - B) Mutowalną wartością domyślną
  - C) XSS
  - D) Limitem tokenów
- Po dodaniu nowej trasy sprawdzasz:
  - A) Tylko nową trasę
  - B) Nową trasę i wszystkie stare testy
  - C) Nic
  - D) Tylko wygląd

Odpowiedzi: B, B, B
