# CV, opowieść o projekcie i rozmowa rekrutacyjna Junior QA
Tydzień 12 · lekcja 38 z 39 · ≈ 45 min

**Po tej lekcji potrafisz:** masz jednostronicowe CV z sekcją Projekty na górze, 2-minutową opowieść o projekcie (problem → rozwiązanie → jak testuję → czego się nauczyłem), odpowiedzi na typowe pytania techniczne i miękkie (metoda STAR) oraz plan wysyłania aplikacji.

**Po co mi to?** Rynek juniorski jest trudny (w I kwartale 2026 oferty juniorskie to ok. 5% ogłoszeń w justjoin.it) — wygrywa kandydat, który pokazuje działający projekt z testami i umie o nim mówić konkretnie.

## Czego potrzebujesz
- Projekt Magazyn na GitHubie z README, testami i zielonym CI.
- Repozytorium testów sklepu testowego (tydzień 9).
- Lekcje etapu 3 (słownictwo testowania).

## 1 · Wyjaśnienie od podstaw
### CV na 1 stronę (PDF)
1. Nagłówek: imię i nazwisko, miasto (opcjonalnie), e-mail, link do GitHuba i LinkedIn. Bez zdjęcia z wakacji, PESEL-u, daty urodzenia.
2. **Projekty — na górze** (przed doświadczeniem, jeśli zmieniasz branżę): nazwa + link, 1 zdanie co robi, technologie, liczby: „Magazyn — Python, SQLite, Flask; 28 testów pytest, 3 testy E2E Selenium (POM), CI GitHub Actions”.
3. Umiejętności: Python, pytest, Selenium WebDriver, Git/GitHub, GitHub Actions, SQL (podstawy), projektowanie przypadków testowych (klasy równoważności, wartości brzegowe), raporty błędów, API (requests).
4. Doświadczenie: także spoza IT — opisuj **kompetencje przydatne w QA**: dokładność, procedury, kontrola jakości, kontakt z klientem.
5. Klauzula zgody na przetwarzanie danych — gdy wymaga jej ogłoszenie.
### Opowieść o projekcie (2 minuty)
**Problem** (jedno zdanie) → **rozwiązanie** (co robi aplikacja, technologie) → **jak testuję** (poziomy, techniki, CI, przykład znalezionego defektu) → **czego się nauczyłem** (konkretnie). Nagraj się telefonem, odsłuchaj, skróć o 30%.
### Pytania techniczne — przykłady
Różnica defekt/awaria; klasy równoważności i wartości brzegowe na przykładzie; piramida testów; jak przetestujesz formularz logowania; co zawiera bug raport; czym jest regresja; różnica WebDriverWait i sleep; co to Page Object; co robi fixture; jak działa CI; co to SQL injection; GET vs POST; kody 200/400/404/500.
### Pytania miękkie — metoda STAR
**S**ytuacja → **Z**adanie (Task) → **D**ziałanie (Action) → **R**ezultat. „Opowiedz o trudnym problemie” → konkretna historia z projektu (np. testy flaky w CI i jak je ustabilizowałeś).
### Zadanie rekrutacyjne
Częste: przetestuj stronę/formularz i opisz defekty, napisz kilka testów automatycznych, przeczytaj kod i znajdź błąd. Pisz przypadki z oczekiwanym wynikiem i raporty jak w tygodniu 9; dołącz README „jak uruchomić”.
### Widełki wynagrodzeń
Od 24 grudnia 2025 r. pracodawca w Polsce musi przekazać kandydatowi informację o wynagrodzeniu (lub jego przedziale) — w ogłoszeniu albo przed rozmową. Orientacyjnie raport Bulldogjob (dane z początku 2025) podaje dla juniora testera manualnego ok. 6 900 zł brutto miesięcznie na umowie o pracę; sprawdzaj aktualne raporty, bo kwoty się zmieniają.
### Plan szukania
5 dopasowanych aplikacji tygodniowo (nie 50 jednakowych), dziennik aplikacji (data, firma, stanowisko, link, status), po każdej rozmowie — notatka z pytań, których nie znałeś. ISTQB Foundation (CTFL 4.0: 40 pytań, próg 26, 60 minut) wzmacnia CV, ale nie zastępuje projektu.

## 2 · Demonstracja — krok po kroku
**Sekcja Projekty, która broni się sama**

```
PROJEKTY
Magazyn sklepu — aplikacja webowa do ewidencji produktów i operacji magazynowych      github.com/anna-nowak/magazyn
• Python, SQLite, Flask; walidacja formularzy po stronie serwera, zapytania parametryzowane (ochrona przed SQL injection)
• 28 testów pytest (parametrize, fixtures, baza tymczasowa) + 3 testy E2E Selenium w Page Object Model
• CI w GitHub Actions z raportem HTML; plan testów i 3 raporty błędów w repozytorium

Testy sklepu internetowego (projekt szkoleniowy)                                         github.com/anna-nowak/sklep-testy
• 15 testów E2E (Selenium, POM, WebDriverWait), 10 przypadków testowych, 3 zgłoszone defekty z krokami odtworzenia

Opowieść (fragment): „Zbudowałam aplikację magazynową, żeby przećwiczyć testowanie na wszystkich poziomach. Reguły — jak blokada wydania ponad stan — testuję jednostkowo z wartościami brzegowymi; zapis do bazy integracyjnie na bazie tymczasowej; trzy najważniejsze ścieżki w Selenium. Test brzegowy złapał, że wydanie dokładnie całego stanu było blokowane — warunek > zamiast >=.”
```

1. Nazwa projektu + link — rekruter kliknie; repozytorium musi mieć README i zielone CI.
2. Jedno zdanie, co robi — bez żargonu.
3. Technologie wymienione z nazwy — w ogłoszeniach szuka się ich słowami kluczowymi (Python, pytest, Selenium, SQL, CI).
4. Liczby: ile testów, jakie poziomy — konkret zamiast „znam pytest”.
5. Słownictwo testera: Page Object Model, wartości brzegowe, raporty błędów — pokazujesz, że rozumiesz zawód, nie tylko kod.
6. Opowieść kończy się prawdziwym przykładem defektu znalezionego testem — najmocniejszy moment rozmowy.

✔ **Oczekiwany wynik:** Sekcja Projekty na 6 linii i 30-sekundowy fragment opowieści z konkretnym defektem.

## 3 · Jak to uruchomić
1. CV: edytor tekstu → eksport do PDF; nazwa pliku Imie_Nazwisko_CV_Junior_QA.pdf.
2. Nagranie opowieści: telefon, 2 minuty, odsłuchaj i skróć.
3. Próbna rozmowa: Asystent (API albo Claude Code) z promptem „Rekruter Junior QA” z zakładki Prompty; Offline — lista pytań w Ściądze.

## W praktyce
- Dziennik aplikacji: data, firma, stanowisko, link, status, następny krok.
- Po każdej rozmowie: 3 pytania, których nie znałeś → lekcja do powtórki.

## 4 · Ćwiczenie prowadzone
Ułóż opowieść o projekcie w kolejności (numery po przecinku): 1 „Testuję reguły jednostkowo z wartościami brzegowymi, a 3 ścieżki w Selenium; CI uruchamia wszystko przy pushu”, 2 „Sklep potrzebował ewidencji stanów zamiast arkusza”, 3 „Nauczyłam się projektować testy przed kodem i stabilizować testy E2E”, 4 „Zbudowałam aplikację Flask z bazą SQLite”. Czas: 10 minut.

📄 `cwiczenia/tydzien_12/rekrutacja_1.md` · rozwiązanie: `rozwiazania/tydzien_12/rekrutacja_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Oceń wpisy w CV (zostaw / popraw): (1) „Znajomość Pythona — średnio-zaawansowana”; (2) „Magazyn — Flask, SQLite; 28 testów pytest, 3 E2E Selenium POM, CI — link”; (3) „Hobby: gry komputerowe” w miejscu sekcji Projekty; (4) PESEL i data urodzenia w nagłówku. Dodatkowo (5): pytanie „Opowiedz o trudnym problemie” — jaką metodą budujesz odpowiedź (wpisz skrót)? Czas: 15 minut.

📄 `cwiczenia/tydzien_12/rekrutacja_2.md` · rozwiązanie: `rozwiazania/tydzien_12/rekrutacja_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **Brak odpowiedzi na 50 wysłanych CV.**
  - Przyczyna: Jednakowe CV bez projektów i słów kluczowych z ogłoszenia.
  - Jak sprawdzić: Porównaj CV z 3 ogłoszeniami — ile słów kluczowych się pokrywa?
  - Poprawka: Projekty na górze, technologie z ogłoszenia, 5 dopasowanych aplikacji tygodniowo.
- ✘ **Na rozmowie: „nie wiem” i cisza.**
  - Przyczyna: Brak struktury odpowiedzi.
  - Jak sprawdzić: Czy znasz pytania z listy w Ściądze?
  - Poprawka: Powiedz, jak byś to sprawdził(a): „Nie używałam X, ale zrobiłabym to tak…” + przykład z projektu.

## Pułapki
- Link do GitHuba z pustymi repozytoriami albo czerwonym CI — sprawdź przed wysłaniem.
- Kopiowanie opisów projektów z internetu — rekruter zapyta o szczegóły.

## Dodatkowe zadania
1. CV 1 strona z sekcją Projekty i linkami.
2. Nagranie 2-minutowej opowieści o projekcie.
3. Sesja 15 pytań technicznych i 3 miękkich; 5 aplikacji w dzienniku.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Jak zbudować opowieść o projekcie?**
  - Problem → rozwiązanie → jak testuję → czego się nauczyłem.
- **Co to metoda STAR?**
  - Sytuacja, zadanie, działanie, rezultat.
- **Czego nie wpisujesz do CV?**
  - PESEL, data urodzenia, niepotrzebne dane osobowe.

## Co potrafię teraz bez patrzenia na przykład?
Masz CV z projektami i liczbami, opowieść o projekcie w 2 minuty, odpowiedzi na pytania techniczne i miękkie oraz plan wysyłania aplikacji z dziennikiem.

## Źródła (data dostępu w nawiasie)
Wersje narzędzi i dane rynkowe zmieniają się — przed użyciem w pracy otwórz źródło.
- Antyweb — barometr justjoin.it i rocketjobs.pl za I kw. 2026: oferty juniorskie 5% ogłoszeń (10.04.2026) (dostęp 23.11.2026) — <https://antyweb.pl/rynek-pracy-it-juniorzy>
- Bulldogjob — IT Community Report 2025: wynagrodzenia testerów manualnych (junior UoP 6 900 zł brutto) (dostęp 23.11.2026) — <https://bulldogjob.com/it-report/salaries/tester>
- ISTQB — Certified Tester Foundation Level (CTFL) v4.0 (sylabus v4.0.1, egzamin 40 pytań, próg 26, 60 min) (dostęp 23.11.2026) — <https://istqb.org/certifications/certified-tester-foundation-level-ctfl-v4-0>
- GitHub Docs — About READMEs (dostęp 23.11.2026) — <https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Struktura 2-minutowej opowieści o projekcie?
  - A) Lista plików
  - B) Problem → rozwiązanie → jak testuję → czego się nauczyłem
  - C) Historia commitów
  - D) Lista technologii
- Sekcja Projekty w CV osoby zmieniającej branżę:
  - A) na końcu
  - B) na górze
  - C) niepotrzebna
  - D) w osobnym pliku
- Od 24.12.2025 pracodawca w Polsce musi:
  - A) zatrudnić juniora
  - B) przekazać kandydatowi informację o wynagrodzeniu
  - C) wymagać ISTQB
  - D) płacić za rekrutację
- Na pytanie, na które nie znasz odpowiedzi:
  - A) milczysz
  - B) zmyślasz
  - C) mówisz, jak byś to sprawdził(a)
  - D) kończysz rozmowę

Odpowiedzi: B, B, B, C
