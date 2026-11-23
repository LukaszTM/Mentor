# Powtórka końcowa: przegląd projektu jak senior tester i plan dalszej nauki
Tydzień 12 · lekcja 39 z 39 · ≈ 35 min

**Po tej lekcji potrafisz:** przeglądasz własny projekt listą kontrolną seniora (kod, testy, dokumentacja, bezpieczeństwo, CI), wdrażasz najważniejsze poprawki i układasz plan nauki na 3 miesiące po kursie.

**Po co mi to?** Projekt, który przeszedł Twoją własną surową recenzję, broni się na rozmowie. Plan po kursie sprawia, że nauka nie kończy się w tygodniu 12.

## Czego potrzebujesz
- Projekt Magazyn i repozytorium testów sklepu.
- Wszystkie etapy kursu.

## 1 · Wyjaśnienie od podstaw
### Lista kontrolna seniora
**Kod**: funkcje krótkie z docstringami, nazwy, brak duplikacji, brak magicznych liczb, input/print tylko w interfejsie, zapytania SQL z `?`.
**Testy**: piramida (dużo test_client/jednostkowych, kilka E2E), wartości brzegowe reguł, przypadki negatywne, testy niezależne (tmp_path), brak sleep, nazwy jak zdania, każdy test zawodzi na mutancie.
**Dokumentacja**: README (opis, uruchomienie, przykład, „Jak testuję”), PLAN_TESTOW.md (zakres, poziomy, ryzyka, co ręcznie), raporty błędów.
**Bezpieczeństwo**: brak sekretów i .env w repo, debug=False poza komputerem, walidacja serwera, autoescaping szablonów.
**CI**: zielone, raport HTML jako artefakt, odznaka w README.
### Recenzja z asystentem
Prompt: „Oceń mój projekt jak senior tester przed code review. Wypisz 5 najważniejszych uwag, od najpoważniejszej. Nie poprawiaj kodu.” — potem sam(a) decydujesz, które 3 wdrażasz, i opisujesz je w RECENZJA.md (uwaga → decyzja → commit).
### Co dalej (3 miesiące)
1. **Testy API** (requests + pytest, ewentualnie Postman) — bardzo częste w ogłoszeniach. 2. **SQL** — JOIN, GROUP BY. 3. **ISTQB CTFL 4.0** — polska wersja sylabusa i egzaminy przykładowe SJSI. 4. Alternatywa dla Selenium: Playwright — pojawia się coraz częściej w ogłoszeniach; Twoje POM i czekanie przenoszą się 1:1. 5. Angielski techniczny — dokumentacja narzędzi jest po angielsku.
### Mapa całego kursu
Etap 1: Python (podstawy) → Etap 2: projekt jak w zespole (Git, moduły, venv, API) → Etap 3: testowanie (techniki, pytest, Selenium, raporty, CI) → Etap 4: projekt portfolio i rekrutacja.

## 2 · Demonstracja — krok po kroku
**Lista kontrolna jako słownik — i plan poprawek**

```
LISTA = {
    "README z sekcją Jak testuję": True,
    "CI zielone z raportem HTML": True,
    "Zapytania SQL z parametrami ?": True,
    "Testy wartości brzegowych reguł": True,
    "Brak time.sleep w testach E2E": False,
    "Brak sekretów w repozytorium": True,
    "PLAN_TESTOW.md": False,
}
spelnione = [k for k, v in LISTA.items() if v]
do_poprawy = [k for k, v in LISTA.items() if not v]
print(f"Spełnione: {len(spelnione)}/{len(LISTA)} ({len(spelnione) / len(LISTA):.0%})")
for nr, k in enumerate(do_poprawy, 1):
    print(f"{nr}. Popraw: {k}")

```

1. Słownik: punkt listy → czy spełniony (bool).
2. Listy składane wybierają spełnione i do poprawy.
3. `:.0%` — format procentowy bez miejsc po przecinku (5/7 = 71%).
4. `enumerate(…, 1)` numeruje poprawki od 1 — gotowa lista do RECENZJA.md.
5. Każdy punkt „do poprawy” = osobny mały commit z opisem („Zastąp time.sleep czekaniem na listę produktów”).

✔ **Oczekiwany wynik:** „Spełnione: 5/7 (71%)” i dwie numerowane poprawki.

## 3 · Jak to uruchomić
1. Zapisz jako przeglad.py → ▶ Uruchom; uzupełnij listę o swoje punkty.
2. Poprawki: osobne commity, potem push i sprawdzenie CI.

## W praktyce
- Co kwartał: przegląd portfolio listą seniora.
- Każda nowa umiejętność = mały projekt na GitHubie z README i testami.

## 4 · Ćwiczenie prowadzone
Recenzja dała 5 uwag: (A) hasło do bazy w kodzie, (B) time.sleep(3) w testach E2E, (C) brak docstringów w 4 funkcjach, (D) literówka w README, (E) brak testu dla wydania równego stanowi. Na wzór listy seniora ułóż 3 najważniejsze do wdrożenia od najpoważniejszej (litery po przecinku). Czas: 10 minut.

📄 `cwiczenia/tydzien_12/powtorka_portfolio_1.md` · rozwiązanie: `rozwiazania/tydzien_12/powtorka_portfolio_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Plan po kursie: masz 5 godzin tygodniowo przez 3 miesiące. (1) Ile to godzin razem (12 tygodni)? (2) Który temat wybierasz na pierwszy miesiąc, jeśli 3 z 5 ogłoszeń, które cię interesują, wymagają testów API — wybierz: Playwright / testy API / ISTQB. (3) Czy certyfikat ISTQB zastępuje projekt w CV (tak/nie)? Czas: 10 minut.

📄 `cwiczenia/tydzien_12/powtorka_portfolio_2.md` · rozwiązanie: `rozwiazania/tydzien_12/powtorka_portfolio_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **Wdrożenie wszystkich 20 uwag naraz w jednym commicie.**
  - Przyczyna: Brak priorytetów.
  - Jak sprawdzić: Które uwagi dotyczą bezpieczeństwa i poprawności?
  - Poprawka: 3 najważniejsze, każda osobnym commitem, CI po każdym.
- ✘ **Projekt „skończony”, a CI czerwone od tygodnia.**
  - Przyczyna: Brak sprawdzenia po ostatnich zmianach.
  - Jak sprawdzić: Zakładka Actions.
  - Poprawka: Napraw przed wysłaniem CV — rekruter widzi czerwony znaczek.

## Pułapki
- Ślepe wdrażanie wszystkich uwag AI — część bywa nietrafiona; decyzja i uzasadnienie są Twoje.
- Nauka 5 nowych narzędzi naraz po kursie — jedno na miesiąc, z projektem.

## Dodatkowe zadania
1. Recenzja projektu jak senior tester; 3 poprawki w osobnych commitach; RECENZJA.md.
2. Plan nauki na 3 miesiące w notatki.md.
3. Ostatni przegląd repozytoriów przed wysłaniem CV.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Co sprawdza lista kontrolna seniora?**
  - Kod, testy, dokumentację, bezpieczeństwo i CI.
- **Jak wybierasz poprawki z recenzji?**
  - Najpierw bezpieczeństwo i poprawność, potem stabilność testów, na końcu kosmetyka.
- **Co po kursie najczęściej wymagają ogłoszenia QA?**
  - Testy API, SQL, narzędzia automatyzacji (Selenium/Playwright).

## Co potrafię teraz bez patrzenia na przykład?
Recenzujesz własny projekt listą seniora, wdrażasz najważniejsze poprawki z uzasadnieniem i masz plan nauki na 3 miesiące.

## Źródła (data dostępu w nawiasie)
Wersje narzędzi i dane rynkowe zmieniają się — przed użyciem w pracy otwórz źródło.
- ISTQB — Certified Tester Foundation Level (CTFL) v4.0 (sylabus v4.0.1, egzamin 40 pytań, próg 26, 60 min) (dostęp 23.11.2026) — <https://istqb.org/certifications/certified-tester-foundation-level-ctfl-v4-0>
- SJSI — Egzamin przykładowy CTFL 4.0, wersja polska (terminologia: pomyłka, defekt, awaria, klasy równoważności, wartości brzegowe) (dostęp 23.11.2026) — <https://testerzy.pl/pliki/certyfikacja/egzamin-przykladowy-ctfl-ver-4-0-pytania-pl.pdf/podglad>
- OWASP — SQL Injection Prevention Cheat Sheet (zapytania parametryzowane) (dostęp 23.11.2026) — <https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html>
- GitHub Docs — Building and testing Python (actions/checkout@v6, actions/setup-python, pytest) (dostęp 23.11.2026) — <https://docs.github.com/en/actions/tutorials/build-and-test-code/python>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Najpilniejsza uwaga z recenzji:
  - A) literówka w README
  - B) hasło w kodzie
  - C) brak emoji
  - D) kolor przycisku
- Uwagi z recenzji wdrażasz:
  - A) wszystkie w jednym commicie
  - B) najważniejsze, osobnymi commitami
  - C) żadnej
  - D) tylko kosmetyczne
- Certyfikat ISTQB CTFL:
  - A) zastępuje projekt
  - B) wzmacnia CV obok projektu
  - C) jest wymagany prawnie
  - D) jest tylko po angielsku
- format(5/7, ".0%") daje:
  - A) 0.71
  - B) 71%
  - C) 5/7
  - D) 71.4%

Odpowiedzi: B, B, B, B
