# START TUTAJ — Vibe coding od podstaw

**Wersja kursu:** 1.1 · stan na: 20 listopada 2026 · format `mentor-program/1`
**Poziom:** od zera — bez wcześniejszej znajomości plików, terminala, programowania i narzędzi AI.
**Czas:** 16 tygodni, ok. 80 minut dziennie (pn–pt) i do 90 minut w sobotę — razem ok. 118 godzin; żaden tydzień nie przekracza 9 godzin (czas policzony z treści lekcji i zadań).
**System:** Windows 10 (1809+) / 11 — Mentor.exe; Claude Code i Codex instalowane w tygodniu 4.
**Potrzebujesz:** ok. 80 minut dziennie od poniedziałku do piątku i do 90 minut w sobotę (quiz, powtórka) przez 16 tygodni — razem ok. 120 godzin; każdy tydzień mieści się w 9 godzinach; komputer z Windows 10/11 i internetem; Mentor instaluje Pythona i biblioteki kursu za Twoją zgodą; tygodnie 0–3: 0 zł (darmowy czat AI wystarczy); od tygodnia 4: jeden plan z agentem (Claude Pro albo ChatGPT Plus, ok. 20 USD + VAT miesięcznie) albo ścieżka bez konta; konto GitHub (darmowe) od tygodnia 6.

## Co będziesz umieć po kursie
- poruszać się po plikach i terminalu Windows, czytać prosty kod Pythona i komunikaty błędów
- pisać specyfikacje z przykładami i kryteriami „Gotowe, gdy” oraz testy pytest, które łapią błędy
- bezpiecznie pracować z Claude Code i Codex: tryby uprawnień, AGENTS.md/CLAUDE.md, małe kroki, kontekst i koszty
- prowadzić projekt w Git i GitHub: commity, gałęzie, pull requesty, przegląd zmian agenta, CI w GitHub Actions
- budować stronę (HTML/CSS/JS, GitHub Pages), raporty z CSV/JSON, aplikację Flask z bazą SQLite i integracje z API
- rozpoznawać i naprawiać typowe dziury w kodzie od AI (XSS, SQL injection, sekrety, zależności) i zabezpieczać agenta przed prompt injection
- znać podstawy prawa: prawa do kodu z AI, licencje, RODO, AI Act; zamieniać mail klienta w wymagania i wycenę
- wydać projekt końcowy 1.0.0 z testami, CI, README i portfolio gotowym dla rekrutera lub klienta

## Pierwsze 30 minut
Kurs **nie jest wbudowany w Mentora** — to osobna paczka, którą wgrywasz sam(a), kiedy chcesz zacząć.
1. **Zainstaluj Mentora** (2.9.0 lub nowszy, paczka `Mentor-windows.zip`): rozpakuj do zwykłego folderu i uruchom `Mentor.exe`. Windows może zapytać o uruchomienie niepodpisanego programu: „Więcej informacji → Uruchom mimo to”.
2. **Wgraj kurs: Ustawienia → Program nauczania → „📦 Importuj kurs ZIP…”** → wybierz plik `Vibe-coding-kurs.zip` (nie musisz go rozpakowywać). Mentor najpierw pokaże podgląd — nazwę, wersję, liczbę lekcji, wymagania i listę skryptów, których **nie uruchamia** — a po Twojej zgodzie rozpakuje kurs do swojego katalogu danych i przełączy się na niego.
3. **Sprawdź:** Ustawienia → Program nauczania pokazuje „Vibe coding od podstaw”, a Plan — 16 tygodni. (Plik `kurs_mentor.json` sam, przez „Importuj JSON…”, nie wystarczy: bez paczki Mentor nie ma testów z `WERYFIKATORY/` i materiałów.)
4. **Mój projekt → „📁 Utwórz katalog roboczy kursu”** (Dokumenty\Mentor\vibe-coding\PRACA) → **„📂 Skopiuj materiały kursu tutaj”** (nic nie nadpisuje).
5. **Środowisko → „⬇ Zainstaluj brakujące”** — Python i biblioteki kursu (pytest, flask, requests) w osobnym .venv, za Twoją zgodą.
6. **Panel → Diagnoza** (10 pytań) → **Lekcje → „Jak uczyć się z tego kursu”** → **Plan → Tydzień 0**.

## Jak sprawdzane są zadania
- Pliki zadań tworzysz w katalogu PRACA (przycisk „📝 Utwórz plik ćwiczenia”). „✔ Sprawdź wynik” uruchamia **niezależne testy** z folderu `WERYFIKATORY/` tej paczki — Mentor sprawdza ich sumę SHA-256 (INTEGRITY.json), kopiuje do osobnego katalogu tylko do odczytu i dopiero wtedy uruchamia. Agent AI nie może ich zmienić.
- Zadania opisowe (plany, przeglądy, wyceny) mają listę kryteriów do samooceny.
- Ćwiczenia w lekcjach mają pola „Twoje odpowiedzi” sprawdzane pole po polu; w Warsztacie są **Karty przeglądu** — sytuacje z pracy z agentem.

## Bez płatnego konta
Tygodnie 0–3 kosztują 0 zł. Od tygodnia 4 zadania z agentem mają ścieżkę bez konta: `przyklady/odpowiedzi_agenta/<zadanie>.md` — zapis pracy agenta z jednym celowo wstawionym błędem do znalezienia testem i poprawienia.

## Gdzie co jest
- `lekcje/` — 48 lekcji (Markdown); `cwiczenia/` i `rozwiazania/` — ćwiczenia z lekcji z podpowiedziami; `rozwiazania/kod/` — rozwiązania wzorcowe zadań (otwieraj po własnej próbie).
- `przyklady/` — pliki startowe zadań (część celowo z błędami), `przyklady/odpowiedzi_agenta/` — ścieżka bez konta; `dane/rezerwacje.csv` — dane fikcyjne.
- `pomoc/` — materiały do zadań (tracebacki, diff do przeglądu, obce repozytorium, brief klientki), FAQ, typowe błędy, odzyskiwanie.
- `pytest.ini` — po skopiowaniu do PRACA sprawia, że `python -m pytest -q` uruchamia tylko Twoje testy (pomija foldery materiałów).

## Aktualność
Fakty o narzędziach (Claude Code, Codex), cenach planów i prawie (AI Act, RODO, prawo autorskie) sprawdzono 19–20.11.2026 — źródła z datą dostępu są przy każdej lekcji i w `ZRODLA.md`. Kalendarz aktualizacji (Ściąga w Mentorze) mówi, kiedy sprawdzić ceny, wersje narzędzi i terminy.

## Bezpieczeństwo i licencje
Paczka zawiera wyłącznie materiały kursu: dane fikcyjne, bez kluczy API, haseł i programów firm trzecich. Adresy i klucze w przykładach (np. `smsapi_live_…`, `api.pogoda.example`) są zmyślone na potrzeby ćwiczeń.
