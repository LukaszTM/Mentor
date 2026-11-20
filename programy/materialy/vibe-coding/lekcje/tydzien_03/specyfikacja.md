# Specyfikacja: „Gotowe, gdy…” — zamówienie, które da się sprawdzić
Tydzień 3 · lekcja 10 z 48 · ≈ 50 min

**Po tej lekcji potrafisz:** piszesz jednostronicową specyfikację (cel, wejście, wynik, przykłady, przypadki brzegowe, poza zakresem, gotowe gdy) — taką, z której agent zbuduje kod, a Ty test.

**Po co mi to?** Agent zrobi dokładnie to, co opiszesz — a czego nie opiszesz, wymyśli. Specyfikacja to Twoja najważniejsza praca w vibe codingu.

## Czego potrzebujesz
- Lekcja „Rozmowa z AI”.
- Edytor lub Notatnik (plik specyfikacja.md w PRACA).

## 1 · Wyjaśnienie od podstaw
### Po co spisywać, skoro można powiedzieć?
Rozmowa znika, plik zostaje. Specyfikację dasz agentowi dziś, przeczytasz za miesiąc przy poprawce i pokażesz klientowi przy odbiorze. Dokumentacja Claude Code (Best practices) radzi wprost: daj agentowi sposób na zweryfikowanie pracy — testy, przykłady, oczekiwane wyniki — i najpierw planuj, potem koduj.
### Siedem sekcji specyfikacji
| sekcja | co wpisujesz | przykład (walidacja e-maila) |
|---|---|---|
| Cel | jedno zdanie: co i dla kogo | funkcja sprawdzająca adres e-mail gościa w formularzu rezerwacji |
| Wejście | jakie dane, jakiego typu | napis (str) |
| Wynik | co zwraca / co robi | True albo False |
| Przykłady | 4–8 par wejście → wynik | "anna@pod-lipa.pl" → True; "anna@" → False |
| Przypadki brzegowe | puste, za długie, dziwne znaki, granice | "" → False; spacje na końcu → usuń i sprawdź |
| Poza zakresem | czego NIE robić | nie wysyłamy maili, nie sprawdzamy, czy skrzynka istnieje |
| Gotowe, gdy | jak sprawdzisz | przechodzą testy Mentora; przykłady dają dokładnie te wyniki |
### Przypadki brzegowe — gdzie mieszkają błędy
- Puste dane: pusta lista, pusty napis, 0.
- Granice: dokładnie 7 nocy, dokładnie 18 lat, ostatni dzień miesiąca.
- Złe typy i wartości: "abc" zamiast liczby, liczba ujemna.
- Polskie znaki i spacje: "Łódź ", "Żaneta".
- Duże dane: 10 000 wierszy zamiast 3.
### Poza zakresem — hamulec dla agenta
Agenci lubią „pomagać więcej”: dodają bibliotekę, przepisują sąsiedni plik, zmieniają nazwy. Sekcja „Poza zakresem” i lista plików, których nie wolno ruszać, to najprostsza ochrona.
### Gotowe, gdy — kryteria akceptacji
Kryterium musi dać odpowiedź tak/nie. „Działa szybko” — nie; „raport dla 10 000 wierszy powstaje w mniej niż 2 sekundy” — tak. „Ładny” — nie; „ma nagłówek h1, formularz z polami noce i osoby i działa na telefonie (meta viewport)” — tak.
### Format pliku: Markdown
Specyfikację piszesz w .md: `# Tytuł`, `## Sekcja`, listy `- `. Agenci czytają Markdown świetnie, GitHub pokazuje go ładnie.

## 2 · Demonstracja — krok po kroku
**Od mglistej prośby do specyfikacji w 15 minut**

```
# Specyfikacja: walidacja.py

## Cel
Funkcje sprawdzające e-mail i telefon gościa w formularzu rezerwacji „Pod Lipą”.

## Wejście
Napis (str).

## Wynik
czy_email(tekst) → True/False; czy_telefon(tekst) → True/False.

## Przykłady
- czy_email("anna@pod-lipa.pl") → True
- czy_email("anna@") → False
- czy_telefon("600 700 800") → True
- czy_telefon("+48 600-700-800") → True
- czy_telefon("12345") → False

## Przypadki brzegowe
- "" → False dla obu
- spacje na początku/końcu ignorujemy

## Poza zakresem
- nie sprawdzamy, czy skrzynka istnieje; bez bibliotek spoza Pythona

## Gotowe, gdy
- przechodzą testy Mentora (zadanie tygodnia 3)
```

1. Klientka „Pod Lipą” pisze: „Chciałabym, żeby formularz nie przyjmował złych telefonów”.
2. Cel: funkcja czy_telefon(tekst). Pytasz siebie: co to jest „dobry telefon”? Decyzja: polski numer, 9 cyfr, opcjonalnie +48 na początku, spacje i myślniki dozwolone.
3. Przykłady: "600700800" → True; "600 700 800" → True; "+48 600-700-800" → True; "48600700800" → False (bez plusa niejednoznaczne — decyzja!); "12345" → False; "" → False.
4. Poza zakresem: numery zagraniczne (zapisujesz jako pytanie do klientki), sprawdzanie, czy numer istnieje.
5. Gotowe, gdy: wszystkie przykłady dają wynik z listy; testy Mentora przechodzą. Każdy przykład to linia testu — spisałeś test, zanim powstał kod.

✔ **Oczekiwany wynik:** Specyfikacja z 6 przykładami, jedną świadomą decyzją (48 bez plusa = False) i jednym pytaniem do klientki — agent nie musi niczego zgadywać.

## 3 · Jak to uruchomić
1. Utwórz specyfikacja.md w PRACA (zadanie tygodnia — „📝 Utwórz plik ćwiczenia” wstawi szablon sekcji).
2. „✔ Sprawdź wynik” sprawdzi, czy są wszystkie sekcje i co najmniej 4 przykłady.

## W praktyce
- Każde zlecenie dla agenta = plik specyfikacji w repozytorium.
- Decyzje zapisuj w specyfikacji, nie w głowie.

## 4 · Ćwiczenie prowadzone
Specyfikacja funkcji cena_sniadan(osoby, noce): 35 zł za osobę za dzień; dzieci nie są liczone osobno. Uzupełnij wyniki przykładów: (1) cena_sniadan(2, 3), (2) cena_sniadan(1, 1), (3) cena_sniadan(4, 7). Do której sekcji wpiszesz „osoby = 0 → ValueError”? Czas: 15 minut.

📄 `cwiczenia/tydzien_03/specyfikacja_1.md` · rozwiązanie: `rozwiazania/tydzien_03/specyfikacja_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Które kryteria „Gotowe, gdy” są sprawdzalne (tak/nie)? (1) „Strona ładnie wygląda” (2) „Raport dla 10 000 wierszy powstaje w < 2 s” (3) „Kod jest dobry” (4) „Funkcja dla (7, 1) zwraca 756.0” (5) „Formularz ma pola noce i osoby”. Ile jest sprawdzalnych? Czas: 15 minut.

📄 `cwiczenia/tydzien_03/specyfikacja_2.md` · rozwiązanie: `rozwiazania/tydzien_03/specyfikacja_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **Agent zrobił „coś innego”, niż chciałeś.**
  - Przyczyna: Specyfikacja bez przykładów — model zinterpretował słowa po swojemu.
  - Jak sprawdzić: Ile przykładów wejście → wynik ma specyfikacja?
  - Poprawka: Minimum 4 przykłady, w tym 2 brzegowe.
- ✘ **Agent dodał bibliotekę i przerobił 5 plików.**
  - Przyczyna: Brak sekcji „Poza zakresem”.
  - Jak sprawdzić: Czy napisałeś, czego nie ruszać?
  - Poprawka: Dopisz listę plików i rzeczy zakazanych; w Claude Code użyj trybu planu (tydzień 5).
- ✘ **Klient przy odbiorze: „miało być inaczej”.**
  - Przyczyna: Decyzje podjęte po cichu zamiast zapisane i potwierdzone.
  - Jak sprawdzić: Czy decyzje są w specyfikacji?
  - Poprawka: Sekcja „Decyzje i pytania do klienta” — wysyłasz ją przed budową.

## Pułapki
- Specyfikacja nie musi być długa — jedna strona wystarczy. Długie specyfikacje agent czyta gorzej i drożej.
- Nie wpisuj w specyfikację rozwiązania („użyj wyrażeń regularnych”), jeśli nie masz powodu — opisuj CO, a nie JAK.

## Dodatkowe zadania
1. Napisz specyfikację dla funkcji czy_telefon z demonstracji (zadanie tygodnia).
2. Dla jednej codziennej rzeczy (np. lista zakupów) wypisz 5 przypadków brzegowych.
3. Przerób 2 niesprawdzalne kryteria z ćwiczenia na sprawdzalne.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Jakie sekcje ma specyfikacja?**
  - Cel, wejście, wynik, przykłady, przypadki brzegowe, poza zakresem, gotowe gdy.
- **Czym jest kryterium akceptacji?**
  - Warunkiem z odpowiedzią tak/nie, który mówi, kiedy praca jest skończona.
- **Dlaczego przykłady w specyfikacji to „testy przed kodem”?**
  - Bo każdy przykład wejście → wynik można od razu zamienić na test.

## Co potrafię teraz bez patrzenia na przykład?
Piszesz specyfikację z 7 sekcji, wymyślasz przypadki brzegowe, ograniczasz agenta sekcją „Poza zakresem” i formułujesz sprawdzalne kryteria „Gotowe, gdy”.

## Źródła (data dostępu w nawiasie)
Narzędzia, ceny i przepisy zmieniają się — przed użyciem w pracy otwórz źródło.
- Claude Code — Best practices (oficjalna dokumentacja) (dostęp 19.11.2026) — <https://code.claude.com/docs/en/best-practices>
- Anthropic — Be clear, direct, and detailed (dokumentacja Claude) (dostęp 19.11.2026) — <https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/be-clear-and-direct>
- Atlassian — Acceptance criteria: definicja i przykłady (tłumaczenie robocze) (dostęp 19.11.2026) — <https://www.atlassian.com/work-management/project-management/acceptance-criteria>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Które kryterium jest sprawdzalne?
  - A) Kod jest czytelny
  - B) Funkcja dla "" zwraca False
  - C) Program jest nowoczesny
  - D) Strona jest ładna
- Po co sekcja „Poza zakresem”?
  - A) Żeby było dłużej
  - B) Żeby agent nie robił rzeczy, o które nie prosiłeś
  - C) Dla prawnika
  - D) Nie ma sensu
- Który przykład jest przypadkiem brzegowym dla „rabat od 7 nocy”?
  - A) 3 noce
  - B) Dokładnie 7 nocy
  - C) 100 nocy
  - D) Każdy
- W jakim formacie piszemy specyfikację?
  - A) Markdown (.md)
  - B) .exe
  - C) .zip
  - D) Zdjęcie kartki

Odpowiedzi: B, B, B, A
