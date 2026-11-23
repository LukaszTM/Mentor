# START TUTAJ — Python od zera → Junior QA (wersja demonstracyjna)

**Wersja kursu:** 3.0-demo · stan na: 23 listopada 2026 · format `mentor-program/1`
**Poziom:** od zera — bez wcześniejszej znajomości programowania, terminala i Gita.
**Czas:** 4 tygodni, ok. 90 minut dziennie (pn–pt) i do 60 minut w sobotę — razem ok. 29 godzin; żaden tydzień nie przekracza 9 godzin (czas policzony z treści lekcji i zadań).
**System:** Windows 10 / 11 — Mentor.exe; Python i biblioteki kursu instaluje Mentor, Git for Windows instalujesz w tygodniu 0.
**Potrzebujesz:** ok. 90 minut dziennie od poniedziałku do piątku i do 60 minut w sobotę (quiz, powtórka) przez 13 tygodni — razem ok. 100 godzin; każdy tydzień mieści się w 9 godzinach; komputer z Windows 10/11 i internetem przy instalacji; Mentor instaluje Pythona i biblioteki kursu za Twoją zgodą, bez uprawnień administratora; 0 zł: Python, Git, GitHub (konto darmowe od tygodnia 0), PyCharm w wersji darmowej (opcjonalnie); asystent AI — tryb Offline Mentora albo darmowy czat; Claude Code (płatny) — opcjonalnie; przeglądarka Microsoft Edge (wbudowana w Windows) albo Chrome od tygodnia 8; internet przy pierwszym uruchomieniu Selenium (pobranie sterownika).

> **Wersja demonstracyjna:** tygodnie 0–3 z 13 (konfiguracja i podstawy Pythona) — 16 lekcji i 20 zadań z niezależnymi testami. Pełny kurs (`Python-junior-qa-kurs.zip`) dodaje pliki i Git w zespole, klasy, API, techniki testowania ISTQB, pytest, Selenium z Page Object Model, raporty błędów, CI, SQLite, Flask i projekt portfolio. Postępy wersji demonstracyjnej są zapisywane osobno.

## Co będziesz umieć po kursie
- pisać i czytać programy w Pythonie: typy, warunki, pętle, listy, słowniki, funkcje, wyjątki, pliki i CSV, klasy, moduły
- pracować jak w zespole: Git (gałęzie, pull request, cofanie zmian), GitHub, venv i requirements.txt, README
- projektować przypadki testowe technikami klas równoważności i wartości brzegowych; znać terminologię ISTQB (pomyłka, defekt, awaria, poziomy testów)
- pisać testy pytest (parametrize, fixtures, tmp_path, raises) i sprawdzać mutacją, że łapią błędy
- automatyzować testy przeglądarki w Selenium WebDriver z WebDriverWait i Page Object Model
- pisać przypadki testowe i raporty błędów odtwarzalne bez pytań; uruchamiać testy w GitHub Actions z raportem HTML
- używać SQL (SQLite) z zapytaniami parametryzowanymi i testować aplikację Flask na dwóch poziomach (test_client i E2E)
- przedstawić projekt portfolio na rozmowie Junior QA: CV, opowieść o projekcie, odpowiedzi techniczne

## Pierwsze 30 minut
Kurs **nie jest wbudowany w Mentora** — to osobna paczka, którą wgrywasz sam(a), kiedy chcesz zacząć.
1. **Zainstaluj Mentora** (2.9.1 lub nowszy, paczka `Mentor-windows.zip`): rozpakuj do zwykłego folderu i uruchom `Mentor.exe`. Windows może zapytać o uruchomienie niepodpisanego programu: „Więcej informacji → Uruchom mimo to”.
2. **Wgraj kurs: Ustawienia → Program nauczania → „📦 Importuj kurs ZIP…”** → wybierz plik `Python-junior-qa-demo.zip` (nie musisz go rozpakowywać). Mentor pokaże podgląd — nazwę, wersję, liczbę lekcji, wymagania i listę skryptów, których **nie uruchamia** — a po Twojej zgodzie rozpakuje kurs do swojego katalogu danych i przełączy się na niego.
3. **Sprawdź:** Ustawienia → Program nauczania pokazuje „Python od zera → Junior QA (wersja demonstracyjna)”, a Plan — 4 tygodni. (Sam `kurs_mentor.json` przez „Importuj JSON…” nie wystarczy: bez paczki Mentor nie ma testów z `WERYFIKATORY/` i materiałów.)
4. **Mój projekt → „📁 Utwórz katalog roboczy kursu”** → **„📂 Skopiuj materiały kursu tutaj”** (dane, przykłady; nic nie nadpisuje).
5. **Środowisko → „Zainstaluj / Napraw”** — Python 3.11–3.13 i biblioteki kursu (pytest, requests, selenium, flask) w osobnym .venv, za Twoją zgodą, bez uprawnień administratora.
6. **Panel → Diagnoza** (10 pytań) → **Lekcje → „Start: jak uczyć się z tego kursu”** → **Plan → Tydzień 0**.

## Jak sprawdzane są zadania
- Pliki zadań tworzysz w katalogu PRACA (przycisk „📝 Utwórz plik ćwiczenia”). „✔ Sprawdź wynik” uruchamia **niezależne testy** z folderu `WERYFIKATORY/` tej paczki — Mentor sprawdza ich sumę SHA-256 (INTEGRITY.json) i uruchamia je w osobnym katalogu. Testy wywołują Twoje funkcje i programy na wielu danych, także błędnych, i mówią po polsku, czego brakuje.
- Część zadań sprawdza wyjście programu („wyjście zawiera…”); zadania z dokumentami — wymagane sekcje i treść; zadania rekrutacyjne — lista kryteriów do samooceny.
- Ćwiczenia w lekcjach mają pola „Twoje odpowiedzi” sprawdzane pole po polu.
- Zielony test to nie wszystko: wyjaśnij własnymi słowami, co i dlaczego działa.

## Bez płatnego konta
Cały kurs przejdziesz za 0 zł: Mentor, Python, Git, GitHub, PyCharm (funkcje darmowe). Asystent AI: tryb Offline w Mentorze albo darmowy czat; Claude Code (płatny plan) jest opcjonalny.

## Gdzie co jest
- `lekcje/` — lekcje (Markdown); `przyklady/tydzien_NN/` — programy z demonstracji; `cwiczenia/` i `rozwiazania/` — ćwiczenia z lekcji z podpowiedziami; `rozwiazania/kod/` — rozwiązania wzorcowe zadań (otwieraj po własnej próbie).
- `przyklady/*.py` — pliki startowe zadań (część celowo z błędami); `dane/produkty.csv` — dane fikcyjne.
- `pomoc/` — FAQ, typowe błędy, odzyskiwanie. `pytest.ini` — po skopiowaniu do PRACA `python -m pytest -q` uruchamia tylko Twoje testy.

## Aktualność i źródła
Fakty o narzędziach (Python, pytest, Selenium, Git, GitHub Actions, PyCharm), terminologia ISTQB/SJSI i dane rynku pracy sprawdzono 23.11.2026 — źródła z datą dostępu są przy każdej lekcji i w `ZRODLA.md`.

## Bezpieczeństwo i licencje
Paczka zawiera wyłącznie materiały kursu: dane fikcyjne (sklep „Papierowy Kot”), bez kluczy API, haseł, danych osobowych i programów firm trzecich.
