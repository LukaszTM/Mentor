# Przypadki testowe i raporty błędów, które programista rozumie bez pytań
Tydzień 9 · lekcja 32 z 39 · ≈ 45 min

**Po tej lekcji potrafisz:** zapisujesz przypadki testowe w tabeli (ID, warunki wstępne, kroki, dane, oczekiwany wynik) i raporty błędów z tytułem, krokami odtworzenia, wynikiem oczekiwanym i rzeczywistym, środowiskiem, ważnością i dowodem.

**Po co mi to?** Raport błędu to najczęstszy produkt pracy testera. Dobry naprawia się szybko; zły wraca z pytaniem „nie mogę odtworzyć” i blokuje całe wydanie.

## Czego potrzebujesz
- Lekcja „Podstawy testowania”.
- Sklep testowy uruchomiony — ma kilka celowo wprowadzonych defektów do znalezienia.

## 1 · Wyjaśnienie od podstaw
### Przypadek testowy
| pole | przykład |
|---|---|
| ID | TC-05 |
| Tytuł | Zamówienie z kodem pocztowym w złym formacie jest odrzucone |
| Warunki wstępne | zalogowany jako tester, w koszyku 1 produkt |
| Kroki | 1. Koszyk → Zamów. 2. Wypełnij formularz, kod pocztowy „00000”. 3. Kliknij Zamawiam. |
| Dane | kod: 00000 |
| Oczekiwany wynik | komunikat „Kod pocztowy w formacie NN-NNN”, zamówienie nie zostaje złożone |
Zapisujesz go PRZED wykonaniem. Status po wykonaniu: zaliczony / niezaliczony / zablokowany.
### Raport błędu (zgłoszenie defektu)
1. **Tytuł**: gdzie + co nie działa + w jakich warunkach — „Koszyk: suma pomija produkty o ilości 10 i więcej”. Nie: „koszyk nie działa”.
2. **Środowisko**: wersja aplikacji, system, przeglądarka i wersja, adres.
3. **Warunki wstępne** i **kroki odtworzenia** — ponumerowane, z danymi. Ktoś obcy powtórzy je bez pytań.
4. **Wynik oczekiwany** (wg wymagań) i **rzeczywisty** (co dokładnie widać, z wartościami).
5. **Ważność** (severity — wpływ: krytyczna/wysoka/średnia/niska) i **priorytet** (pilność naprawy — ustala zespół).
6. **Dowód**: zrzut ekranu, nagranie, fragment logu, traceback.
7. Powtarzalność: „zawsze (5/5)” albo „sporadycznie (2/10)”.
### Jeden błąd = jedno zgłoszenie
Trzy problemy w jednym raporcie się gubią. Przed zgłoszeniem: odtwórz jeszcze raz, sprawdź, czy już nie zgłoszono, zawęź warunki (czy dotyczy tylko ilości ≥ 10?).
### Ton
Fakty, bez ocen („programista znowu zepsuł”). Raport czyta też klient i kierownik.
### Testowanie eksploracyjne
Gdy nie ma scenariuszy: sesja 30–60 minut z celem („formularz zamówienia: złe dane”), notatki na bieżąco, na końcu lista znalezisk i pomysłów na testy.

## 2 · Demonstracja — krok po kroku
**Od zauważonej awarii do raportu w 10 minut**

```
## BUG-03: Koszyk — suma nie uwzględnia ilości 10 i więcej sztuk
**Środowisko:** Sklep testowy 1.0 (lokalnie, http://127.0.0.1:5001), Windows 11, Edge 142
**Ważność:** wysoka (klient płaci złą kwotę) · **Powtarzalność:** zawsze (5/5)
**Warunki wstępne:** zalogowany użytkownik tester, pusty koszyk
**Kroki:**
1. Produkty → „Zeszyt A5 w kratkę” (4,50 zł) → ilość 10 → Dodaj do koszyka.
2. Otwórz Koszyk.
**Oczekiwany wynik:** pozycja 10 × 4,50 zł = 45,00 zł, suma koszyka 45,00 zł.
**Rzeczywisty wynik:** pozycja pokazuje 10 szt., ale suma koszyka to 4,50 zł.
**Dodatkowo:** dla ilości 9 suma jest poprawna (40,50 zł) — problem zaczyna się od 10 (wartość brzegowa).
**Dowód:** bug03_koszyk.png
```

1. Zauważasz: suma koszyka dziwnie niska. Nie zgłaszasz od razu — najpierw odtwarzasz: pusty koszyk, jeden produkt, ilość 10 → suma 4,50 zł. Powtarzasz 5 razy — zawsze.
2. Zawężasz: ilość 9 → poprawnie, 10 → źle, 25 → źle. Granica 10 — to informacja dla programisty, gdzie szukać.
3. Tytuł: miejsce (Koszyk) + co (suma nie uwzględnia ilości) + warunek (10 i więcej).
4. Środowisko z wersją przeglądarki (edge://version).
5. Kroki ponumerowane, z nazwą produktu i ceną — każdy może je powtórzyć.
6. Oczekiwany vs rzeczywisty — z konkretnymi kwotami.
7. Ważność wysoka: złe pieniądze. Priorytet ustali zespół.
8. Dowód: driver.save_screenshot albo Win+Shift+S; nazwa pliku z numerem zgłoszenia.

✔ **Oczekiwany wynik:** Raport BUG-03, który programista odtwarza za pierwszym razem, z granicą (10 sztuk) wskazującą miejsce defektu.

## 3 · Jak to uruchomić
1. Sklep testowy: `python app.py` → http://127.0.0.1:5001 → login tester / Test123!.
2. Raporty zapisuj w bug_raporty.md (Markdown) w PRACA — tak jak w szablonie Mentora (zakładka Szablony).

## W praktyce
- Szablon zgłoszenia w zespole (Jira/GitHub Issues) — wypełniaj wszystkie pola.
- Po naprawie: retest kroków z raportu + test regresji automatyczny.

## 4 · Ćwiczenie prowadzone
Popraw tytuł raportu „logowanie nie działa” na wzór demonstracji. Fakty: przy loginie z wielką literą („Tester”) i poprawnym haśle pojawia się „Błędny login lub hasło”; z „tester” działa. Wybierz najlepszy tytuł i podaj wynik oczekiwany (wybierz). Czas: 10 minut.

📄 `cwiczenia/tydzien_09/bug_raport_1.md` · rozwiązanie: `rozwiazania/tydzien_09/bug_raport_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Oceń ważność (krytyczna / wysoka / średnia / niska): (1) po kliknięciu „Zamawiam” serwer zwraca 500 dla każdego zamówienia; (2) literówka „Koszuk” w menu; (3) kod pocztowy „00000” jest akceptowany; (4) suma koszyka zła dla ilości ≥ 10. Dodatkowo (5): czy 3 znalezione problemy wpisujesz w jedno zgłoszenie (tak/nie)? Czas: 15 minut.

📄 `cwiczenia/tydzien_09/bug_raport_2.md` · rozwiązanie: `rozwiazania/tydzien_09/bug_raport_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **Zgłoszenie wraca z „Cannot reproduce”**
  - Przyczyna: Brak danych, środowiska albo kroków wstępnych.
  - Jak sprawdzić: Czy obca osoba wykona kroki bez pytań?
  - Poprawka: Dopisz dane, wersje, warunki wstępne; nagraj ekran.
- ✘ **Spór o ważność**
  - Przyczyna: Ocena wpływu z perspektywy „mnie to irytuje”.
  - Jak sprawdzić: Jaki jest wpływ na użytkownika i biznes?
  - Poprawka: Opisz skutki faktami (np. „klient płaci 4,50 zamiast 45 zł”).

## Pułapki
- Raport z opinią zamiast faktów („ten formularz jest beznadziejny”).
- Zrzut ekranu bez zaznaczenia miejsca problemu — zaznacz ramką.

## Dodatkowe zadania
1. 10 przypadków testowych sklepu testowego w tabeli Markdown.
2. 3 raporty błędów z defektów znalezionych w sklepie testowym.
3. Sesja eksploracyjna 30 minut z notatkami.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Co musi mieć raport błędu?**
  - Tytuł, środowisko, kroki, oczekiwany i rzeczywisty wynik, ważność, dowód.
- **Ważność a priorytet?**
  - Ważność = wpływ; priorytet = pilność naprawy (ustala zespół).
- **Dlaczego jeden błąd = jedno zgłoszenie?**
  - Każdy defekt ma własny cykl naprawy i weryfikacji.

## Co potrafię teraz bez patrzenia na przykład?
Zapisujesz przypadki testowe z oczekiwanym wynikiem i raporty błędów, które da się odtworzyć bez pytań, z rzetelną oceną ważności i dowodem.

## Źródła (data dostępu w nawiasie)
Wersje narzędzi i dane rynkowe zmieniają się — przed użyciem w pracy otwórz źródło.
- SJSI — Egzamin przykładowy CTFL 4.0, wersja polska (terminologia: pomyłka, defekt, awaria, klasy równoważności, wartości brzegowe) (dostęp 23.11.2026) — <https://testerzy.pl/pliki/certyfikacja/egzamin-przykladowy-ctfl-ver-4-0-pytania-pl.pdf/podglad>
- ISTQB Glossary — słownik terminów testowania (dostępny w języku polskim) (dostęp 23.11.2026) — <https://glossary.istqb.org/>
- ISTQB — Certified Tester Foundation Level (CTFL) v4.0 (sylabus v4.0.1, egzamin 40 pytań, próg 26, 60 min) (dostęp 23.11.2026) — <https://istqb.org/certifications/certified-tester-foundation-level-ctfl-v4-0>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Najlepszy tytuł zgłoszenia:
  - A) Nie działa
  - B) Koszyk: suma pomija produkty o ilości ≥ 10
  - C) BUG!!!
  - D) Problem z aplikacją
- Ważność (severity) opisuje:
  - A) kolejność naprawy
  - B) wpływ defektu
  - C) kto zgłosił
  - D) datę
- Przypadek testowy bez oczekiwanego wyniku:
  - A) jest kompletny
  - B) nie pozwala ocenić, czy test przeszedł
  - C) jest szybszy
  - D) jest negatywny
- Przed zgłoszeniem błędu najpierw:
  - A) zgłaszasz, ile się da
  - B) odtwarzasz i zawężasz warunki
  - C) naprawiasz sam kod
  - D) czekasz tydzień

Odpowiedzi: B, B, B, B
