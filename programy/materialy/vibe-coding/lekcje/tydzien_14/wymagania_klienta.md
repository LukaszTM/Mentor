# Praca z klientem: od maila do wymagań, wyceny i odbioru
Tydzień 14 · lekcja 43 z 48 · ≈ 50 min

**Po tej lekcji potrafisz:** zamieniasz nieprecyzyjny mail klienta w historyjki użytkownika z kryteriami akceptacji, listę pytań i zakres „poza projektem”, przygotowujesz wycenę z buforem i plan odbioru.

**Po co mi to?** Najczęstsza przyczyna konfliktów z klientem to niejasny zakres, nie zły kod. Agent przyspiesza pisanie kodu — ale nie zrozumie za Ciebie, czego klient naprawdę potrzebuje.

## Czego potrzebujesz
- Lekcja „Specyfikacja” (tydzień 3).
- Plik pomoc/brief_klienta.md z materiałów (zadanie tygodnia).

## 1 · Wyjaśnienie od podstaw
### Historyjka użytkownika
Format: „Jako [kto] chcę [co], aby [po co]”. Pod nią kryteria akceptacji — sprawdzalne zdania tak/nie. Przykład:
„Jako gość chcę zobaczyć wolne pokoje w wybranych datach, aby zarezerwować pobyt bez dzwonienia.”
- Dla dat 21–22.12 przy rezerwacji Lipowego 20–23.12 lista nie zawiera Lipowego.
- Data wyjazdu przed datą przyjazdu → komunikat po polsku, brak listy.
- Strona działa na telefonie o szerokości 375 px.
### Od maila do wymagań — 5 kroków
| krok | wynik |
|---|---|
| 1. Wypisz potrzeby z maila (rzeczowniki i czasowniki) | lista „co ma umieć” |
| 2. Każdą zamień na historyjkę z 2–4 kryteriami | wymagania.md |
| 3. Zaznacz niejasności | lista pytań do klienta |
| 4. Ustal, czego NIE robisz | sekcja „Poza zakresem” |
| 5. Priorytety: musi / powinno / może (MoSCoW) | kolejność pracy |
Agent pomaga: „Na podstawie maila zaproponuj historyjki i 10 pytań o niejasności; nie zakładaj odpowiedzi”. Ty weryfikujesz i rozmawiasz z klientem.
### Wycena
- Rozbij pracę na zadania (historyjki + testy + README + wdrożenie + poprawki po odbiorze).
- Szacuj godziny dla każdego, dodaj bufor 30–50% na nieznane (pierwsze projekty prawie zawsze się przeciągają).
- Dolicz koszty: plan AI w czasie projektu, hosting, domena (płaci klient — zapisz to).
- Wycena ryczałtowa = zakres musi być zamknięty; zmiany zakresu → osobna wycena (zapis w umowie).
### Forma rozliczenia (Polska, w skrócie)
Drobne zlecenia możesz rozliczać w działalności nierejestrowanej do 225% minimalnego wynagrodzenia na kwartał (2026: 10 813,50 zł); po przekroczeniu 7 dni na wpis do CEIDG. Inne formy: umowa o dzieło/zlecenie, własna działalność. Prawa autorskie i powierzenie danych — w umowie. To nie porada podatkowa — sprawdź aktualne przepisy lub zapytaj księgowego.
### Odbiór
Odbiór = przejście kryteriów akceptacji przy kliencie (lista z historyjek), nie „czy się podoba”. Po odbiorze: README, dostęp do repozytorium, instrukcja dla klienta, okres poprawek (np. 14 dni), co dalej z utrzymaniem (aktualizacje, koszty).

## 2 · Demonstracja — krok po kroku
**Mail → wymagania → wycena w 45 minut**

```
Fragment maila klientki:
„Chciałabym, żeby goście mogli sami sprawdzić, czy jest wolny pokój, i żeby nie dzwonili o ceny. Fajnie, jakby było też zdjęcia i może płatność online? I żeby działało na telefonie.”

Z tego: US-1 wolne pokoje (musi), US-2 kalkulator ceny (musi), US-3 galeria (powinno), US-4 telefon (musi — jako kryterium dla wszystkich), płatność online → poza zakresem v1 (osobna wycena: operator płatności, regulamin, RODO). Pytania: ile pokoi, sezonowość cen, kto aktualizuje rezerwacje, czy zbieramy dane gości.
```

1. Czytasz pomoc/brief_klienta.md. Wypisujesz 7 potrzeb, w tym 2 ukryte („nie chcę przepisywać rezerwacji z zeszytu” = import danych).
2. Agent (nowa sesja, tryb planu): proponuje 8 historyjek i 12 pytań. Odrzucasz 2 historyjki (logowanie gości, newsletter — nikt o nie nie prosił), 4 pytania łączysz.
3. Poza zakresem: płatności online, aplikacja mobilna, integracja z portalami rezerwacyjnymi.
4. Wycena: 6 historyjek × średnio 4 h + testy 6 h + README i wdrożenie 4 h + poprawki 4 h = 38 h; bufor 40% → 53 h. Koszty narzędzi i hostingu — osobna pozycja.
5. Wysyłasz klientce wymagania i pytania PRZED wyceną końcową; wycenę po odpowiedziach.

✔ **Oczekiwany wynik:** Wymagania z kryteriami, lista pytań, jasny „poza zakresem” i wycena z buforem — klientka wie, co dostanie i za ile.

## 3 · Jak to uruchomić
1. Zadanie tygodnia „wymagania.md” → „✔ Sprawdź wynik” (struktura historyjek).

## W praktyce
- Każde zlecenie: wymagania.md potwierdzone przez klienta przed kodem.
- Dziennik godzin — podstawa kolejnych wycen.

## 4 · Ćwiczenie prowadzone
Wycena: 5 historyjek po 4 h, testy 6 h, README i wdrożenie 4 h, poprawki 4 h. (1) Suma godzin bez bufora, (2) z buforem 40% (zaokrąglij w górę do pełnej godziny), (3) wartość przy stawce 80 zł/h (zł). Czas: 15 minut.

📄 `cwiczenia/tydzien_14/wymagania_klienta_1.md` · rozwiązanie: `rozwiazania/tydzien_14/wymagania_klienta_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Które kryteria akceptacji są poprawne (sprawdzalne)? (1) „Kalkulator jest intuicyjny”, (2) „Dla 7 nocy i 2 osób w lipcu kalkulator pokazuje kwotę z rabatem 10%”, (3) „Strona ładuje się szybko”, (4) „Formularz z pustą datą pokazuje komunikat po polsku i nie wysyła danych”. Podaj liczbę poprawnych. Do której sekcji trafia „płatność online” w wersji 1? Czas: 15 minut.

📄 `cwiczenia/tydzien_14/wymagania_klienta_2.md` · rozwiązanie: `rozwiazania/tydzien_14/wymagania_klienta_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **Klient przy odbiorze: „myślałam, że będzie też…”.**
  - Przyczyna: Zakres nie spisany, brak „Poza zakresem”.
  - Jak sprawdzić: Czy klient potwierdził wymagania na piśmie?
  - Poprawka: Wymagania z sekcją Poza zakresem wysłane i potwierdzone przed pracą; zmiany = nowa wycena.
- ✘ **Projekt trwa 2× dłużej niż wycena.**
  - Przyczyna: Brak bufora, nieuwzględnione testy/README/poprawki.
  - Jak sprawdzić: Porównaj wycenę z rzeczywistym czasem (dziennik).
  - Poprawka: Bufor 30–50%, osobne pozycje na testy, dokumentację i poprawki.

## Pułapki
- „Agent zrobi to w godzinę” nie jest podstawą wyceny — czas zabierają rozmowy, testy, poprawki i odbiór.
- Nie obiecuj „bezpieczeństwa” ani „zgodności z RODO” bez sprawdzenia — obiecuj konkretne środki (lista z tygodnia 12).

## Dodatkowe zadania
1. Napisz wymagania.md z briefu klientki (zadanie tygodnia).
2. Przygotuj wycena.md z buforem.
3. Zapisz 5 pytań do klientki.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Jaki jest format historyjki użytkownika?**
  - Jako [kto] chcę [co], aby [po co] + sprawdzalne kryteria akceptacji.
- **Po co sekcja „Poza zakresem”?**
  - Żeby klient i Ty mieli tę samą wizję i żeby zmiany zakresu były osobno wyceniane.
- **Czym jest odbiór?**
  - Sprawdzeniem kryteriów akceptacji przy kliencie, nie oceną „czy się podoba”.

## Co potrafię teraz bez patrzenia na przykład?
Zamieniasz mail klienta w historyjki z kryteriami, pytania i zakres, wyceniasz z buforem i planujesz odbiór oraz formę rozliczenia.

## Źródła (data dostępu w nawiasie)
Narzędzia, ceny i przepisy zmieniają się — przed użyciem w pracy otwórz źródło.
- Atlassian — User stories: przykłady i szablon (tłumaczenie robocze) (dostęp 20.11.2026) — <https://www.atlassian.com/agile/project-management/user-stories>
- Atlassian — Acceptance criteria (dostęp 20.11.2026) — <https://www.atlassian.com/work-management/project-management/acceptance-criteria>
- Działalność nierejestrowana 2026: limit 10 813,50 zł (money.pl) (dostęp 20.11.2026) — <https://direct.money.pl/artykuly/porady/dzialalnosc-nierejestrowana-2026-limit-10-813,50-zl,-po-przekroczeniu-7-dni-na-ceidg>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Poprawne kryterium akceptacji:
  - A) Strona jest ładna
  - B) Dla dat 21–22.12 lista nie zawiera zajętego Lipowego
  - C) Działa szybko
  - D) Klient zadowolony
- Bufor w wycenie pierwszych projektów:
  - A) 0%
  - B) 30–50%
  - C) 200%
  - D) Nie stosuje się
- Klient prosi w trakcie o płatności online. Ruch:
  - A) Robię za darmo
  - B) Osobna wycena — zmiana zakresu
  - C) Odmawiam bez rozmowy
  - D) Ukrywam w kosztach
- Limit działalności nierejestrowanej 2026:
  - A) 10 813,50 zł na kwartał
  - B) 10 813,50 zł na rok
  - C) Brak limitu
  - D) 3 000 zł na miesiąc

Odpowiedzi: B, B, B, A
