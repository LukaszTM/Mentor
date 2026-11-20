# Bezpieczeństwo kodu od AI: XSS, wstrzyknięcia, sekrety, zależności
Tydzień 12 · lekcja 37 z 48 · ≈ 50 min

**Po tej lekcji potrafisz:** rozpoznajesz w kodzie od AI 6 najczęstszych dziur (XSS, SQL injection, sekret w kodzie, debug na serwerze, niesprawdzone dane, podejrzana zależność) i każesz je naprawić z testem potwierdzającym.

**Po co mi to?** Raport Veracode (2025): 45% próbek kodu z ponad 100 modeli miało luki z listy OWASP, a przy XSS modele zawodziły w 86% przypadków. Kod „działa” — i jest dziurawy. To Twoja odpowiedzialność wobec klienta.

## Czego potrzebujesz
- Lekcje „Aplikacja Flask”, „Baza SQLite”, „API i klucze”.
- Plik przyklady/podatna_aplikacja.py (zadanie tygodnia).

## 1 · Wyjaśnienie od podstaw
### Sześć dziur, które łapiesz w każdym przeglądzie
| dziura | jak wygląda u agenta | poprawka | test |
|---|---|---|---|
| XSS (wstrzyknięcie skryptu do strony) | `return f"<p>Witaj {imie}</p>"` z danymi z formularza | `escape(imie)` (markupsafe) albo szablon Jinja z autoescape | `<script>` w odpowiedzi jako `&lt;script&gt;` |
| SQL injection | f-string w execute | parametry `?` | `x' OR '1'='1` nic nie znajduje |
| sekret w kodzie | `SECRET_KEY = "dev123"`, klucze API | zmienna środowiskowa, brak = błąd startu | grep sekretów w repo |
| debug na serwerze | `app.run(debug=True, host="0.0.0.0")` | debug tylko lokalnie | brak debug=True w kodzie produkcyjnym |
| niesprawdzone dane | brak walidacji typów, zakresów, długości | walidacja na serwerze + 400 | testy złych danych |
| podejrzana zależność | `pip install` nieznanej paczki | sprawdzenie na pypi.org, wersja w requirements | przegląd requirements w diffie |
### XSS po ludzku
Jeśli strona wstawia tekst od użytkownika jako HTML, ktoś wpisze w polu imienia `<script>…</script>` — i skrypt wykona się w przeglądarce każdego, kto obejrzy stronę (kradzież sesji, fałszywe formularze). Dokumentacja Flaska: szablony Jinja domyślnie zamieniają `<` na `&lt;` (autoescape) — ale HTML sklejany f-stringiem w Pythonie albo `innerHTML` w JS omija tę ochronę. Tak właśnie piszą agenci, gdy prosisz o „szybką stronę”.
### SECRET_KEY we Flasku
Flask używa SECRET_KEY do podpisywania ciasteczek sesji. Znany klucz = możliwość podrobienia sesji (np. „jestem administratorem”). W kodzie: `app.config["SECRET_KEY"] = os.environ["FLASK_SECRET_KEY"]`; wygenerowanie losowego: `python -c "import secrets; print(secrets.token_hex(32))"`.
### Łańcuch dostaw: slopsquatting
Badanie zaprezentowane na USENIX Security 2025: w 19,7% z 2,23 mln próbek kodu z 16 modeli pojawiła się co najmniej jedna nieistniejąca paczka (205 474 unikalne zmyślone nazwy; modele otwarte 21,7%, komercyjne 5,2%), a 43% zmyśleń powtarzało się w 10 na 10 prób. Przestępcy rejestrują takie nazwy ze złośliwym kodem — „slopsquatting”. Zasada: każda nowa zależność → pypi.org (czy istnieje, od kiedy, kto wydaje, ile pobrań, repozytorium źródłowe) → dopiero potem instalacja i wpis do requirements.
### Proś o bezpieczeństwo wprost
Do specyfikacji i AGENTS.md: „Dane od użytkownika zawsze walidowane na serwerze; HTML tylko przez szablony z autoescape albo escape(); SQL tylko z ?; sekrety tylko ze zmiennych środowiskowych; bez nowych zależności bez pytania”. Potem i tak sprawdzasz — testem i przeglądem.

## 2 · Demonstracja — krok po kroku
**Cztery dziury w 30 liniach — przegląd podatnej aplikacji**

```
from markupsafe import escape

imie = "<script>alert('hej')</script>"
print(f"<p>Witaj {imie}</p>")
print(f"<p>Witaj {escape(imie)}</p>")

```

1. Otwierasz przyklady/podatna_aplikacja.py (kod jak od agenta: „szybka strona powitania i wyszukiwarka gości”).
2. Trasa /powitanie zwraca f"<h1>Witaj {imie}</h1>" — XSS. Sprawdzasz: /powitanie?imie=<b>Ania</b> → pogrubione „Ania” w przeglądarce = HTML wykonany.
3. Trasa /szukaj: execute(f"… WHERE email = '{email}'") — SQL injection. `x' OR '1'='1` → lista wszystkich gości.
4. Na górze: app.config["SECRET_KEY"] = "tajne123" — sekret w kodzie. Na dole: app.run(debug=True) — debug.
5. Prośba do agenta z listą 4 dziur i wymogiem testu na każdą. Po poprawkach: escape w powitaniu, ? w zapytaniu, klucz z FLASK_SECRET_KEY (brak → RuntimeError), debug usunięty. Testy z zadania — zielone.

✔ **Oczekiwany wynik:** Każda z 4 dziur nazwana, naprawiona i potwierdzona testem; zasady bezpieczeństwa dopisane do AGENTS.md.

## 3 · Jak to uruchomić
1. Zadanie tygodnia „podatna_aplikacja.py” → przegląd z tabelą 6 dziur → poprawki → „✔ Sprawdź wynik”.

## W praktyce
- Każdy przegląd: tabela 6 dziur.
- Każda nowa paczka: pypi.org przed instalacją.

## 4 · Ćwiczenie prowadzone
Co wypisze przykład lekcji? Druga linia zaczyna się od `<p>Witaj ` — jaki jest pierwszy znak PO tym fragmencie w wersji z escape: `<` czy `&`? Która linia jest bezpieczna do wstawienia na stronę (1 czy 2)? Czas: 15 minut.

📄 `cwiczenia/tydzien_12/bezpieczenstwo_kodu_1.md` · rozwiązanie: `rozwiazania/tydzien_12/bezpieczenstwo_kodu_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Dopasuj dziurę: (1) `return f"<li>{komentarz}</li>"`, (2) `execute("… WHERE pokoj = '" + pokoj + "'")`, (3) `STRIPE_KEY = "sk_live_…"` w pliku, (4) `pip install requestz` zaproponowane przez agenta. Opcje: XSS, SQL injection, sekret w kodzie, podejrzana zależność. Czas: 15 minut.

📄 `cwiczenia/tydzien_12/bezpieczenstwo_kodu_2.md` · rozwiązanie: `rozwiazania/tydzien_12/bezpieczenstwo_kodu_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **Po „naprawie” XSS strona pokazuje &amp;lt; zamiast <.**
  - Przyczyna: Podwójne escapowanie (escape + szablon z autoescape).
  - Jak sprawdzić: Gdzie tekst jest escapowany?
  - Poprawka: Escapuj w jednym miejscu: szablon z autoescape albo escape() przy sklejaniu, nie oba.
- ✘ **Aplikacja nie startuje: KeyError 'FLASK_SECRET_KEY'.**
  - Przyczyna: Zmienna nie ustawiona w tym oknie.
  - Jak sprawdzić: echo %FLASK_SECRET_KEY% (CMD).
  - Poprawka: set FLASK_SECRET_KEY=… (lokalnie) — i czytelny RuntimeError zamiast KeyError.

## Pułapki
- „Dodaj walidację w JavaScript” nie zabezpiecza serwera — atakujący wyśle żądanie z pominięciem strony.
- Agent proszony o „naprawę bezpieczeństwa” bywa nadgorliwy: dodaje biblioteki i konfiguracje. Wymagaj minimalnych zmian i testu na każdą dziurę.

## Dodatkowe zadania
1. Napraw podatna_aplikacja.py z testami (zadanie tygodnia).
2. Dopisz zasady bezpieczeństwa do AGENTS.md.
3. Przejrzyj requirements.txt projektu: każda paczka sprawdzona na pypi.org.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Co to jest XSS?**
  - Wstrzyknięcie skryptu przez dane użytkownika wstawione do strony jako HTML.
- **Jak chronisz SECRET_KEY?**
  - Trzymam go w zmiennej środowiskowej, generuję losowo, nigdy w kodzie.
- **Co robisz z nową zależnością od agenta?**
  - Sprawdzam na pypi.org, czy istnieje i jest wiarygodna — dopiero potem instaluję.

## Co potrafię teraz bez patrzenia na przykład?
Rozpoznajesz i naprawiasz 6 typowych dziur w kodzie od AI z testem na każdą, rozumiesz slopsquatting i wpisujesz wymogi bezpieczeństwa do specyfikacji.

## Źródła (data dostępu w nawiasie)
Narzędzia, ceny i przepisy zmieniają się — przed użyciem w pracy otwórz źródło.
- Veracode — GenAI Code Security Report (30.07.2025): 45% próbek z lukami, XSS 86% (dostęp 19.11.2026) — <https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/>
- OWASP Top 10 — najważniejsze ryzyka aplikacji webowych (dostęp 20.11.2026) — <https://owasp.org/www-project-top-ten/>
- OWASP — Cross Site Scripting Prevention Cheat Sheet (dostęp 20.11.2026) — <https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html>
- Flask — Security Considerations (XSS, autoescape, SECRET_KEY) (dostęp 20.11.2026) — <https://flask.palletsprojects.com/en/stable/web-security/>
- Cloud Security Alliance — slopsquatting (badanie USENIX Security 2025: 19,7% próbek ze zmyśloną paczką) (dostęp 19.11.2026) — <https://labs.cloudsecurityalliance.org/research/csa-research-note-slopsquatting-ai-supply-chain-20260419/>

## Test (w Mentorze: Lekcje → Sprawdź się)
- `return f"<p>{imie}</p>"` z danymi z formularza to ryzyko:
  - A) SQL injection
  - B) XSS
  - C) Wyciek klucza
  - D) Brak
- Według raportu Veracode 2025 odsetek próbek kodu z lukami:
  - A) 5%
  - B) 45%
  - C) 86%
  - D) 100%
- Slopsquatting to:
  - A) Szybkie kodowanie
  - B) Rejestrowanie paczek o nazwach zmyślanych przez AI
  - C) Błąd Gita
  - D) Typ testu
- SECRET_KEY Flaska:
  - A) W kodzie dla wygody
  - B) Ze zmiennej środowiskowej, losowy
  - C) Pusty
  - D) W README

Odpowiedzi: B, B, B, B
