# Podstawy testowania: pomyłka, defekt, awaria, poziomy testów, klasy równoważności i wartości brzegowe
Tydzień 7 · lekcja 27 z 39 · ≈ 50 min

**Po tej lekcji potrafisz:** rozróżniasz pomyłkę, defekt i awarię (terminologia ISTQB/SJSI), znasz poziomy testów i piramidę testów oraz projektujesz przypadki testowe technikami podziału na klasy równoważności i analizy wartości brzegowych.

**Po co mi to?** To słownictwo i te techniki padają na każdej rozmowie Junior QA i w egzaminie ISTQB Foundation; dzięki nim zamiast „klikam, aż coś się zepsuje” testujesz celowo i mało, a skutecznie.

## Czego potrzebujesz
- Lekcje „Warunki” i „Funkcje”.

## 1 · Wyjaśnienie od podstaw
### Pomyłka → defekt → awaria
Terminologia polskiej wersji sylabusa ISTQB (SJSI): **pomyłka** — działanie człowieka (programista źle zrozumiał „od 100 zł”); **defekt** — wada w kodzie (`>` zamiast `>=`); **awaria** — widoczny skutek podczas działania (klient z koszykiem za 100 zł płaci za dostawę). Tester obserwuje awarie i pomaga znaleźć defekty.
### Po co testujemy
Testy nie udowodnią braku defektów — zmniejszają ryzyko i dają informację o jakości. Wczesne testowanie (już wymagań) jest najtańsze.
### Poziomy testów
| poziom | co sprawdza | przykład w kursie |
|---|---|---|
| jednostkowe (modułowe) | pojedyncza funkcja/klasa | pytest: `koszt_dostawy(99.99)` |
| integracyjne | współpraca części | funkcja + baza SQLite (tydz. 10) |
| systemowe | cały system | Selenium w przeglądarce (tydz. 8) |
| akceptacyjne | czy spełnia potrzeby użytkownika | scenariusz „klient składa zamówienie” |
**Piramida testów**: dużo szybkich testów jednostkowych na dole, mniej integracyjnych, najmniej (wolnych, kruchych) testów E2E w przeglądarce na górze.
### Podział na klasy równoważności
Dzielisz dane wejściowe na grupy, które program powinien traktować tak samo, i z każdej bierzesz JEDEN reprezentant. Reguła „ilość w zamówieniu 1–50”: klasy: < 1 (niepoprawna), 1–50 (poprawna), > 50 (niepoprawna), nie-liczba (niepoprawna). 4 testy zamiast 100.
### Analiza wartości brzegowych
Defekty siedzą na granicach (`<` vs `<=`). Dla przedziału 1–50 testujesz granice i ich sąsiadów: **0, 1, 50, 51** (wariant dwupunktowy). Wariant trzypunktowy dodaje 2 i 49.
### Testy pozytywne, negatywne, regresja
Pozytywny — poprawne dane, oczekiwany sukces. Negatywny — złe dane, oczekiwany czytelny błąd (nie awaria!). **Regresja** — defekt, który wraca po zmianie; dlatego testy uruchamia się automatycznie przy każdej zmianie (CI, tydzień 9).
### Przypadek testowy
ID, tytuł, warunki wstępne, kroki, dane, **oczekiwany wynik**. Bez oczekiwanego wyniku to nie test, tylko wycieczka.

## 2 · Demonstracja — krok po kroku
**7 przypadków z dwóch technik łapie defekt na granicy**

```
def czy_ilosc_poprawna(ilosc):
    """Wymaganie: ilość w zamówieniu to liczba całkowita od 1 do 50."""
    return isinstance(ilosc, int) and 1 <= ilosc <= 50


def czy_ilosc_z_defektem(ilosc):
    return isinstance(ilosc, int) and 1 <= ilosc < 50


PRZYPADKI = [(0, False), (1, True), (25, True), (50, True), (51, False), (-5, False), ("10", False)]
for funkcja in (czy_ilosc_poprawna, czy_ilosc_z_defektem):
    nieudane = [d for d, oczekiwane in PRZYPADKI if funkcja(d) != oczekiwane]
    print(funkcja.__name__, "— nieudane przypadki:", nieudane)

```

1. Wymaganie w docstringu: liczba całkowita 1–50.
2. Klasy równoważności: < 1 (reprezentant -5), 1–50 (25), > 50 (51… albo 80), nie-liczba ("10" — napis).
3. Wartości brzegowe (dwupunktowo): 0, 1, 50, 51.
4. `PRZYPADKI` — pary (dane, oczekiwany wynik). Razem 7 przypadków.
5. `czy_ilosc_z_defektem` ma `< 50` zamiast `<= 50` — typowa pomyłka programisty.
6. Pętla sprawdza obie wersje: poprawna nie ma nieudanych przypadków, wadliwa pada TYLKO dla 50.
7. Wniosek: bez testu wartości brzegowej 50 defekt przeszedłby niezauważony — 25 i 80 dają poprawne wyniki w obu wersjach.

✔ **Oczekiwany wynik:** Poprawna wersja: lista nieudanych pusta; wersja z defektem: [50].

## 3 · Jak to uruchomić
1. Zapisz jako techniki.py → ▶ Uruchom.
2. Zmień defekt na `1 < ilosc <= 50` i przewidź, który przypadek padnie (1).

## W praktyce
- Przed pisaniem testów automatycznych: tabela klas i granic dla każdej reguły.
- W rozmowie rekrutacyjnej: pokaż technikę na przykładzie z własnego projektu.

## 4 · Ćwiczenie prowadzone
Wymaganie: „hasło ma od 8 do 20 znaków”. Na wzór demonstracji podaj długości do testów dwupunktowej analizy wartości brzegowych (4 liczby rosnąco po przecinku) oraz liczbę klas równoważności dla samej długości. Czas: 15 minut.

📄 `cwiczenia/tydzien_07/podstawy_testowania_1.md` · rozwiązanie: `rozwiazania/tydzien_07/podstawy_testowania_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Zaklasyfikuj (pomyłka / defekt / awaria): (1) programista źle zrozumiał wymaganie „rabat od 200 zł” (działanie człowieka); (2) w kodzie jest `if razem > 200` zamiast `>=`; (3) klient z koszykiem 200 zł nie dostał rabatu. Dodatkowo (4): który poziom testów sprawdza pojedynczą funkcję rabat()? Opcje: jednostkowe / integracyjne / systemowe / akceptacyjne. Czas: 15 minut.

📄 `cwiczenia/tydzien_07/podstawy_testowania_2.md` · rozwiązanie: `rozwiazania/tydzien_07/podstawy_testowania_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **„Przetestowałem 100 losowych wartości i jest OK”, a defekt na granicy przeszedł.**
  - Przyczyna: Testy bez techniki — wszystkie wartości z jednej klasy.
  - Jak sprawdzić: Czy testy obejmują granice i każdą klasę?
  - Poprawka: Klasy równoważności + wartości brzegowe przed pisaniem testów.
- ✘ **Przypadek testowy „sprawdzić logowanie”.**
  - Przyczyna: Brak danych i oczekiwanego wyniku.
  - Jak sprawdzić: Czy obca osoba wie, co wpisać i co ma się stać?
  - Poprawka: Kroki, dane (login/hasło) i oczekiwany wynik (komunikat, strona).

## Pułapki
- Testowanie tylko ścieżki „szczęśliwej” — połowa defektów jest w obsłudze złych danych.
- Mylenie awarii z defektem w zgłoszeniu: opisujesz awarię (co widać), defekt wskazujesz tylko, gdy go znasz.

## Dodatkowe zadania
1. Dla 3 reguł z kursu (dostawa, rabat, ilość) wypisz klasy równoważności i wartości brzegowe.
2. Zapisz 5 przypadków testowych w tabeli (ID, dane, oczekiwany wynik).
3. Wyjaśnij na głos różnicę pomyłka/defekt/awaria.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Czym różni się defekt od awarii?**
  - Defekt to wada w kodzie/produkcie, awaria to jej widoczny skutek podczas działania.
- **Jakie wartości testujesz dla zakresu 1–50 (dwupunktowo)?**
  - 0, 1, 50, 51.
- **Co to piramida testów?**
  - Dużo testów jednostkowych, mniej integracyjnych, najmniej E2E.

## Co potrafię teraz bez patrzenia na przykład?
Rozróżniasz pomyłkę, defekt i awarię, znasz poziomy testów i piramidę oraz projektujesz przypadki technikami klas równoważności i wartości brzegowych.

## Źródła (data dostępu w nawiasie)
Wersje narzędzi i dane rynkowe zmieniają się — przed użyciem w pracy otwórz źródło.
- SJSI — Egzamin przykładowy CTFL 4.0, wersja polska (terminologia: pomyłka, defekt, awaria, klasy równoważności, wartości brzegowe) (dostęp 23.11.2026) — <https://testerzy.pl/pliki/certyfikacja/egzamin-przykladowy-ctfl-ver-4-0-pytania-pl.pdf/podglad>
- ISTQB — Certified Tester Foundation Level (CTFL) v4.0 (sylabus v4.0.1, egzamin 40 pytań, próg 26, 60 min) (dostęp 23.11.2026) — <https://istqb.org/certifications/certified-tester-foundation-level-ctfl-v4-0>
- ISTQB Glossary — słownik terminów testowania (dostępny w języku polskim) (dostęp 23.11.2026) — <https://glossary.istqb.org/>

## Test (w Mentorze: Lekcje → Sprawdź się)
- W kodzie jest < zamiast <=. Ta wada w kodzie to:
  - A) awaria
  - B) defekt
  - C) pomyłka
  - D) regresja
- Wartości brzegowe dla zakresu 10–20 (dwupunktowo):
  - A) 10, 20
  - B) 9, 10, 20, 21
  - C) 0, 30
  - D) 15
- Najwięcej testów w piramidzie to:
  - A) E2E w przeglądarce
  - B) jednostkowe
  - C) manualne
  - D) akceptacyjne
- Test negatywny sprawdza:
  - A) że program działa szybko
  - B) reakcję na niepoprawne dane
  - C) tylko ścieżkę szczęśliwą
  - D) wygląd
- Egzamin ISTQB CTFL 4.0:
  - A) 40 pytań, próg 26, 60 minut
  - B) 100 pytań, ustny
  - C) brak egzaminu
  - D) 10 pytań

Odpowiedzi: B, B, B, B, A
