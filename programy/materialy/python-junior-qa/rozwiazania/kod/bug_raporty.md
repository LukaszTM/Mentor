# Raporty błędów — sklep testowy

## BUG-01: Koszyk: suma nie uwzględnia ilości 10 i więcej sztuk
**Środowisko:** sklep testowy (http://127.0.0.1:5001), Windows 11, Edge 142
**Ważność:** wysoka · **Powtarzalność:** zawsze (5/5)
**Kroki:**
1. Zaloguj się jako tester.
2. Zeszyt A5 w kratkę → ilość 10 → Dodaj do koszyka.
3. Otwórz koszyk.
**Oczekiwany wynik:** suma 45,00 zł (10 × 4,50 zł).
**Rzeczywisty wynik:** suma 4,50 zł; dla ilości 9 suma poprawna (40,50 zł).

## BUG-02: Zamówienie: kod pocztowy 00000 bez myślnika jest akceptowany
**Środowisko:** jak w BUG-01
**Ważność:** średnia · **Powtarzalność:** zawsze
**Kroki:**
1. Dodaj produkt do koszyka i przejdź do zamówienia.
2. Wypełnij imię, e-mail i kod pocztowy 00000.
3. Kliknij Zamawiam.
**Oczekiwany wynik:** komunikat „Kod pocztowy w formacie NN-NNN”.
**Rzeczywisty wynik:** zamówienie przyjęte.

## BUG-03: Wyszukiwarka: fraza małymi literami nie znajduje produktów z wielkiej litery
**Środowisko:** jak w BUG-01
**Ważność:** średnia · **Powtarzalność:** zawsze
**Kroki:**
1. Zaloguj się, w polu Szukaj wpisz „długopis”.
2. Kliknij Szukaj.
**Oczekiwany wynik:** 2 wyniki (wyszukiwarka nie zależy od wielkości liter).
**Rzeczywisty wynik:** „Znaleziono: 0”; dla „Długopis” — 2 wyniki.
