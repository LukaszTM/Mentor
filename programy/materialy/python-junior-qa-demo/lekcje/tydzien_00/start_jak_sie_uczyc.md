# Start: jak uczyć się z tego kursu (przeczytaj najpierw)
Tydzień 0 · lekcja 1 z 16 · ≈ 40 min

**Po tej lekcji potrafisz:** wiesz, co umiesz po 13 tygodniach, ile czasu to zajmie, jak wygląda dzień nauki i jak Mentor sprawdza zadania — i ustawiasz swój plan.

**Po co mi to?** Kurs to 13 tygodni po ok. 7,5 godziny. Bez planu i jasnych zasad większość osób odpada w 3. tygodniu — z planem i małymi krokami dochodzi do końca.

## Czego potrzebujesz
- Mentor uruchomiony (Mentor.exe) i ten kurs wgrany (Ustawienia → Program nauczania → „📦 Importuj kurs ZIP…”).
- Kartka albo plik notatki.md na zapiski.

## 1 · Wyjaśnienie od podstaw
### Co umiesz po kursie
- Piszesz samodzielnie programy w Pythonie na 100–300 linii: zmienne, warunki, pętle, funkcje, listy i słowniki, pliki CSV, klasy, moduły.
- Testujesz: projektujesz przypadki testowe (klasy równoważności, wartości brzegowe), piszesz testy w pytest, testy przeglądarki w Selenium (Page Object Model), raporty błędów, które programista rozumie bez pytań.
- Pracujesz jak w zespole: Git (gałęzie, pull request), GitHub, automatyczne testy w GitHub Actions.
- Masz na GitHubie projekt portfolio — aplikację „Magazyn” (Python, SQLite, Flask) z testami jednostkowymi, testami Selenium i CI — i umiesz o nim opowiedzieć na rozmowie Junior QA.
### Ile to trwa
13 tygodni (tydzień 0–12), 5 dni w tygodniu po ok. 90 minut + sobota na quiz i powtórkę. Razem ok. 100 godzin. Każdy tydzień mieści się w 9 godzinach — Mentor pokazuje czas lekcji i zadań.
### Jak wygląda jedna lekcja
Zawsze ta sama kolejność: **po co** → **wyjaśnienie od podstaw** → **demonstracja** (gotowy program omówiony linia po linii) → **jak uruchomić** → **ćwiczenie prowadzone** (prawie jak demonstracja) → **ćwiczenie samodzielne** (musisz podjąć decyzję) → **typowe błędy** → **pytania i test**. Każde ćwiczenie ma 3 poziomy podpowiedzi: pytanie naprowadzające → wskazanie fragmentu → częściowe rozwiązanie. Pełne rozwiązanie jest osobno, do samosprawdzenia.
### Jak Mentor sprawdza zadania
- Zadanie z kodem sprawdza **niezależny test z paczki kursu** (folder WERYFIKATORY, zabezpieczony sumą SHA-256). Test uruchamia Twoje funkcje na wielu danych — także błędnych — i mówi po polsku, czego brakuje.
- Zadanie z dokumentem (np. bug raport) sprawdza test struktury (czy są wymagane sekcje i treść), a jakość oceniasz według listy „Gotowe, gdy”.
- Zielony wynik to nie wszystko: po zadaniu wyjaśnij na głos (albo w notatki.md), **co i dlaczego działa**. To jest prawdziwe zaliczenie.
### Zasada 70/30 z asystentem AI
70% kodu piszesz sam, 30% może pochodzić z podpowiedzi. Asystent (Offline w Mentorze, API albo Claude Code) jest nauczycielem: najpierw pytasz o wskazówkę, potem o fragment, na końcu o pełne rozwiązanie — z omówieniem. Każdy fragment od AI przepisujesz ręcznie i umiesz go wytłumaczyć.
### Diagnoza na start
Plan → „Diagnoza” to 10 krótkich pytań. Wynik nie blokuje nauki — pokazuje, które lekcje warto przeczytać uważniej.
### Uczciwie o rynku pracy
W I kwartale 2026 oferty juniorskie stanowiły ok. 5% ogłoszeń w portalu justjoin.it, a odsetek kandydatów z doświadczeniem rósł. Kurs daje solidne podstawy i projekt portfolio, ale pierwszej pracy nie gwarantuje — w tygodniu 12 dostajesz plan szukania (CV, portfolio, rozmowa) zamiast obietnic.

## 2 · Demonstracja — krok po kroku
**Plan nauki policzony w 4 linijkach Pythona**

```
tygodnie = 13
dni_w_tygodniu = 5
minut_dziennie = 90
godziny = tygodnie * dni_w_tygodniu * minut_dziennie / 60
print("Godzin nauki w dni robocze:", godziny)

```

1. `tygodnie = 13` — zmienna (pudełko z etykietą) przechowuje liczbę tygodni. Zmienisz na 10 — wynik się zmieni.
2. `dni_w_tygodniu = 5` i `minut_dziennie = 90` — dwa kolejne pudełka. Nazwy mówią, co jest w środku.
3. `godziny = tygodnie * dni_w_tygodniu * minut_dziennie / 60` — mnożysz i dzielisz przez 60 (minuty → godziny). Gwiazdka `*` to mnożenie, `/` dzielenie.
4. `print(...)` wypisuje tekst i wynik. Wynik 97.5 ma kropkę, bo dzielenie `/` w Pythonie zawsze daje liczbę z przecinkiem (float).
5. Nie musisz jeszcze rozumieć składni — w tygodniu 1 przerobisz to dokładnie. Teraz zobacz tylko, że program to lista poleceń wykonywanych od góry.

✔ **Oczekiwany wynik:** Na ekranie: „Godzin nauki w dni robocze: 97.5” — plus soboty na quiz i powtórkę daje ok. 100 godzin.

## 3 · Jak to uruchomić
1. Mentor → Lekcje → ta lekcja: przeczytaj w kolejności sekcji.
2. Plan → Diagnoza: odpowiedz na 10 pytań (ok. 10 minut).
3. Demonstrację uruchomisz po lekcji „Terminal”: wklej kod do pliku plan.py i kliknij ▶ Uruchom w pasku ćwiczenia.

## W praktyce
- Codziennie: lekcja dnia → zadanie → 3 zdania w notatki.md (co zrobiłem, co było trudne, pytanie na jutro).
- Sobota: quiz tygodnia i powtórka tematów z czerwonymi wynikami.

## 4 · Ćwiczenie prowadzone
Policz jak w demonstracji, ale dla planu „wolniejszego”: 13 tygodni, 4 dni w tygodniu, 60 minut dziennie. (1) Ile minut tygodniowo? (2) Ile godzin razem? Czas: 10 minut.

📄 `cwiczenia/tydzien_00/start_jak_sie_uczyc_1.md` · rozwiązanie: `rozwiazania/tydzien_00/start_jak_sie_uczyc_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Zdecyduj, co robisz w każdej sytuacji: (1) nie rozumiesz komunikatu błędu po 10 minutach prób; (2) asystent podał gotowe rozwiązanie całego zadania; (3) test Mentora jest zielony, ale nie umiesz wyjaśnić, dlaczego kod działa; (4) opuściłeś(-aś) tydzień nauki. Opcje: poproś asystenta o wskazówkę (nie rozwiązanie) / przepisz ręcznie, linia po linii z wyjaśnieniem / wróć do lekcji i wyjaśnij w notatki.md / wróć do planu bez nadrabiania wszystkiego naraz. Czas: 10 minut.

📄 `cwiczenia/tydzien_00/start_jak_sie_uczyc_2.md` · rozwiązanie: `rozwiazania/tydzien_00/start_jak_sie_uczyc_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **„Zrobię cały tydzień w sobotę”.**
  - Przyczyna: Nauka zrywami — po 6 godzinach naraz pamięć i motywacja spadają.
  - Jak sprawdzić: Spójrz na Statystyki w Mentorze: ile dni z nauką w tygodniu?
  - Poprawka: Krótko, ale codziennie: 60–90 minut dziennie, sobota na quiz.
- ✘ **Zadanie zielone, a na quizie pustka.**
  - Przyczyna: Kod skopiowany bez zrozumienia.
  - Jak sprawdzić: Spróbuj wyjaśnić na głos każdą linię.
  - Poprawka: Przepisz kod ręcznie, zmień jedną wartość i przewidź wynik, zanim uruchomisz.

## Pułapki
- Porównywanie się z innymi („ktoś zrobił kurs w miesiąc”) — liczy się, czy umiesz wyjaśnić swój kod.
- Kupowanie płatnych narzędzi na start — kurs przechodzisz za 0 zł (Mentor, Python, Git, GitHub i PyCharm w wersji darmowej).

## Dodatkowe zadania
1. Zrób Diagnozę w Planie.
2. Wpisz do kalendarza 5 stałych godzin nauki w tygodniu.
3. Załóż notatki.md i zapisz w 3 zdaniach, po co robisz ten kurs.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Ile godzin trwa kurs?**
  - Ok. 100 godzin: 13 tygodni po ok. 7,5 h.
- **Kiedy zadanie jest naprawdę zaliczone?**
  - Gdy test Mentora jest zielony I umiesz wyjaśnić, co i dlaczego działa.
- **Co robisz, gdy asystent poda gotowe rozwiązanie?**
  - Przepisujesz ręcznie linia po linii i tłumaczysz każdą linię.

## Co potrafię teraz bez patrzenia na przykład?
Znasz cel kursu, rytm dnia (90 minut, 5 dni), kolejność pracy z lekcją, sposób sprawdzania zadań i zasadę 70/30 z asystentem.

## Źródła (data dostępu w nawiasie)
Wersje narzędzi i dane rynkowe zmieniają się — przed użyciem w pracy otwórz źródło.
- ISTQB — Certified Tester Foundation Level (CTFL) v4.0 (sylabus v4.0.1, egzamin 40 pytań, próg 26, 60 min) (dostęp 23.11.2026) — <https://istqb.org/certifications/certified-tester-foundation-level-ctfl-v4-0>
- Antyweb — barometr justjoin.it i rocketjobs.pl za I kw. 2026: oferty juniorskie 5% ogłoszeń (10.04.2026) (dostęp 23.11.2026) — <https://antyweb.pl/rynek-pracy-it-juniorzy>
- Python — Poradnik (oficjalna dokumentacja, wersja polska) (dostęp 23.11.2026) — <https://docs.python.org/pl/3/tutorial/>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Ile mniej więcej trwa kurs?
  - A) 10 godzin
  - B) ok. 100 godzin
  - C) 500 godzin
  - D) tyle, ile chcesz — bez planu
- Co sprawdza zadanie z kodem?
  - A) tylko czy plik istnieje
  - B) niezależny test z paczki kursu
  - C) liczba linii
  - D) nic — odhaczasz sam
- Zasada 70/30 oznacza:
  - A) 70% czasu oglądasz filmy
  - B) 70% kodu piszesz sam
  - C) 70% zadań robi AI
  - D) 70% na quizie wystarczy
- Diagnoza na start:
  - A) blokuje dostęp do lekcji
  - B) pokazuje, co warto powtórzyć
  - C) jest płatna
  - D) zastępuje kurs

Odpowiedzi: B, B, B, B
