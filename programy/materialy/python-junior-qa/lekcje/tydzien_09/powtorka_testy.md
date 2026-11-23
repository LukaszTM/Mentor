# Powtórka etapu 3: strategia testów małego projektu
Tydzień 9 · lekcja 34 z 39 · ≈ 40 min

**Po tej lekcji potrafisz:** układasz strategię testów małego systemu: co testujesz jednostkowo, co integracyjnie, co E2E, a co ręcznie; dobierasz techniki do ryzyka i łączysz to w jeden przebieg CI.

**Po co mi to?** „Jak przetestowałbyś ten formularz / ten sklep?” — to najczęstsze pytanie otwarte na rozmowie Junior QA. Odpowiedź ma strukturę, a nie listę kliknięć.

## Czego potrzebujesz
- Lekcje tygodni 7–9.

## 1 · Wyjaśnienie od podstaw
### Strategia w 5 pytaniach
1. **Co jest najważniejsze / najbardziej ryzykowne?** (pieniądze, logowanie, dane osobowe) — tam najwięcej testów.
2. **Gdzie jest logika?** — reguły (rabat, dostawa, walidacja) testujesz jednostkowo, parametrize z klasami i granicami.
3. **Gdzie części się łączą?** — zapis do bazy/pliku, API → test integracyjny z danymi tymczasowymi.
4. **Jakie ścieżki użytkownika są krytyczne?** — 3–5 testów E2E w POM (logowanie, zamówienie, błędne hasło).
5. **Czego nie warto automatyzować?** — wygląd, jednorazowe sprawdzenia, eksploracja → testy ręczne.
### Mapa etapu 3
| umiejętność | dowód |
|---|---|
| techniki projektowania | tabela klas i granic dla reguły |
| pytest | testy z raises/approx, mutant wykryty |
| parametrize/fixtures | jeden test → wiele przypadków; dane w fixturze |
| Selenium + POM | testy E2E bez sleep, klasy stron |
| przypadki i raporty | tabela TC, raport odtwarzalny bez pytań |
| CI | zielony pipeline z raportem HTML |
### Przykład: sklep testowy
Jednostkowe: koszt dostawy, rabat, walidacja kodu pocztowego (20 przypadków parametrize). Integracyjne: API /api/produkty (status, pola, filtr). E2E: logowanie OK/błąd, dodanie do koszyka i suma, zamówienie. Ręczne: wygląd na telefonie, czytelność komunikatów. CI: jednostkowe przy każdym pushu, E2E przy PR do main.

## 2 · Demonstracja — krok po kroku
**Strategia testów sklepu jako struktura danych**

```
STRATEGIA = {
    "jednostkowe": ["koszt_dostawy", "rabat", "kod_pocztowy"],
    "integracyjne": ["GET /api/produkty", "zapis zamówienia"],
    "e2e": ["logowanie poprawne", "błędne hasło", "koszyk i suma", "zamówienie"],
    "reczne": ["wygląd na telefonie", "czytelność komunikatów"],
}
PRZYPADKI_KOD = ["00-950", "00950", "0-950", "00-95", "ab-cde", "", " 00-950 "]
for poziom, testy in STRATEGIA.items():
    print(f"{poziom:<13}{len(testy):>2}  {', '.join(testy)}")
razem = sum(len(t) for t in STRATEGIA.values())
print("Automatyczne:", razem - len(STRATEGIA["reczne"]), "z", razem)
print("Przypadki kodu pocztowego:", len(PRZYPADKI_KOD))

```

1. Słownik poziom → lista obszarów: od razu widać proporcje piramidy.
2. Jednostkowe: reguły z wymagań — każda rozpisana dalej na przypadki parametrize.
3. Integracyjne: miejsca styku (API, zapis).
4. E2E: tylko krytyczne ścieżki — 4, nie 40.
5. Ręczne: to, czego automatyzacja nie oceni dobrze.
6. Przypadki dla kodu pocztowego (format NN-NNN): poprawny, bez myślnika, za krótki człon, za krótki całość, litery, pusty, ze spacjami — klasy równoważności i granice formatu.
7. Zapis strategii w kodzie/tabeli łatwo pokazać na rozmowie i w PLAN_TESTOW.md (tydzień 12).

✔ **Oczekiwany wynik:** Tabelka 4 poziomów, „Automatyczne: 9 z 11” i „Przypadki kodu pocztowego: 7”.

## 3 · Jak to uruchomić
1. Zapisz jako strategia.py → ▶ Uruchom.
2. Przepisz strategię dla własnego projektu Magazyn (tydzień 10) do PLAN.md.

## W praktyce
- Plan testów projektu zaczyna się od listy ryzyk.
- Na rozmowie: narysuj piramidę i wstaw w nią testy swojego projektu.

## 4 · Ćwiczenie prowadzone
Przypisz poziom testu (jednostkowe / integracyjne / E2E / ręczne): (1) funkcja kod_pocztowy_poprawny("00-950"); (2) zapis zamówienia do bazy SQLite i odczyt; (3) klient loguje się i składa zamówienie w przeglądarce; (4) czy przyciski są czytelne na telefonie. Czas: 10 minut.

📄 `cwiczenia/tydzien_09/powtorka_testy_1.md` · rozwiązanie: `rozwiazania/tydzien_09/powtorka_testy_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Zespół ma 200 testów E2E (2 godziny w CI) i 10 jednostkowych; testy często padają losowo. (1) Jak nazywa się ten antywzorzec (wybierz)? (2) Co zmieniasz najpierw (wybierz)? (3) Ile minimum przypadków dla walidacji „ilość 1–50, liczba całkowita” według klas i granic (dwupunktowo + nie-liczba)? Czas: 15 minut.

📄 `cwiczenia/tydzien_09/powtorka_testy_2.md` · rozwiązanie: `rozwiazania/tydzien_09/powtorka_testy_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **Odpowiedź na rozmowie: lista 30 kliknięć bez struktury.**
  - Przyczyna: Brak strategii.
  - Jak sprawdzić: Czy mówisz o ryzyku, poziomach i technikach?
  - Poprawka: 5 pytań strategii: ryzyko → logika → integracja → ścieżki krytyczne → ręczne.
- ✘ **Wszystko automatyzowane E2E.**
  - Przyczyna: „Bo to wygląda najlepiej”.
  - Jak sprawdzić: Ile trwa CI, ile testów jest flaky?
  - Poprawka: Piramida: reguły jednostkowo, E2E tylko krytyczne.

## Pułapki
- Pokrycie kodu 100% ≠ brak defektów — testy mogą nie mieć sensownych asercji.
- Brak testów ręcznych „bo mamy automaty” — eksploracja znajduje to, czego nie przewidział nikt.

## Dodatkowe zadania
1. Strategia testów sklepu testowego w 5 punktach.
2. Repozytorium testów sklepu: POM, 15+ testów, raport HTML, odznaka CI.
3. Powtórz lekcje z czerwonymi quizami etapu 3.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Jak przetestowałbyś formularz zamówienia?**
  - Ryzyko → reguły jednostkowo (klasy/granice) → integracja API/zapis → E2E ścieżki krytyczne → ręcznie wygląd i komunikaty.
- **Co to odwrócona piramida?**
  - Dużo E2E, mało jednostkowych — wolne, kruche testy.
- **Czego nie automatyzujesz?**
  - Wyglądu, jednorazowych sprawdzeń, eksploracji.

## Co potrafię teraz bez patrzenia na przykład?
Układasz strategię testów: ryzyko, poziomy, techniki, proporcje piramidy i podział na automatyczne i ręczne — w formie, którą pokażesz na rozmowie.

## Źródła (data dostępu w nawiasie)
Wersje narzędzi i dane rynkowe zmieniają się — przed użyciem w pracy otwórz źródło.
- ISTQB — Certified Tester Foundation Level (CTFL) v4.0 (sylabus v4.0.1, egzamin 40 pytań, próg 26, 60 min) (dostęp 23.11.2026) — <https://istqb.org/certifications/certified-tester-foundation-level-ctfl-v4-0>
- SJSI — Egzamin przykładowy CTFL 4.0, wersja polska (terminologia: pomyłka, defekt, awaria, klasy równoważności, wartości brzegowe) (dostęp 23.11.2026) — <https://testerzy.pl/pliki/certyfikacja/egzamin-przykladowy-ctfl-ver-4-0-pytania-pl.pdf/podglad>
- Selenium — Page object models (test practices) (dostęp 23.11.2026) — <https://selenium.dev/documentation/test_practices/encouraged/page_object_models>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Najwięcej testów automatycznych powinno być:
  - A) E2E
  - B) jednostkowych
  - C) ręcznych
  - D) wydajnościowych
- Ryzyko w strategii testów to:
  - A) koszt licencji
  - B) prawdopodobieństwo i skutek problemu
  - C) liczba testerów
  - D) kolor UI
- Wygląd na telefonie testujesz najlepiej:
  - A) pytest
  - B) ręcznie (eksploracyjnie)
  - C) SQL
  - D) nie testujesz
- Testy E2E w strategii obejmują:
  - A) każdą regułę
  - B) krytyczne ścieżki użytkownika
  - C) tylko logowanie
  - D) nic

Odpowiedzi: B, B, B, B
