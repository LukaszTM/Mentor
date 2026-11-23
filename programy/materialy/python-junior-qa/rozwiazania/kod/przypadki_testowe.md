# Przypadki testowe — sklep testowy „Papierowy Kot”

| ID | Tytuł | Warunki wstępne | Kroki | Dane | Oczekiwany wynik |
|---|---|---|---|---|---|
| TC-01 | Logowanie poprawne | sklep uruchomiony | 1. /logowanie 2. wpisz dane 3. Zaloguj | tester / Test123! | strona Produkty, powitanie „Witaj, tester!” |
| TC-02 | Błędne hasło | — | 1. /logowanie 2. wpisz dane 3. Zaloguj | tester / zle | komunikat „Błędny login lub hasło”, brak zalogowania |
| TC-03 | Puste pola logowania | — | 1. /logowanie 2. Zaloguj bez danych | puste | komunikat błędu, brak zalogowania |
| TC-04 | Login z wielką literą | — | 1. /logowanie 2. wpisz dane 3. Zaloguj | Tester / Test123! | zalogowanie (login niewrażliwy na wielkość liter) |
| TC-05 | Wyszukiwarka bez wielkości liter | zalogowany | 1. Szukaj 2. wpisz frazę | „długopis” | 2 wyniki: długopis niebieski i czarny |
| TC-06 | Suma koszyka dla 10 sztuk | zalogowany, pusty koszyk | 1. Zeszyt A5 ilość 10 2. Dodaj 3. Koszyk | 10 × 4,50 zł | suma 45,00 zł |
| TC-07 | Produkt bez stanu | zalogowany | 1. Zszywki 1000 szt. (0 szt.) 2. Dodaj | ilość 1 | komunikat o braku towaru, produkt nie trafia do koszyka |
| TC-08 | Kod rabatowy jednorazowo | koszyk 45,00 zł | 1. kod KOT10 2. Zastosuj 3. ponownie KOT10 | KOT10 × 2 | suma 40,50 zł po obu próbach, drugi raz komunikat odrzucenia |
| TC-09 | Kod pocztowy bez myślnika | koszyk niepusty | 1. Zamówienie 2. wypełnij 3. Zamawiam | kod 00000 | komunikat „Kod pocztowy w formacie NN-NNN”, zamówienie nie złożone |
| TC-10 | Zamówienie poprawne | koszyk niepusty | 1. Zamówienie 2. wypełnij 3. Zamawiam | Anna Nowak, anna@example.com, 00-950 | komunikat „Dziękujemy! Zamówienie nr … przyjęte”, koszyk pusty |
| TC-11 | E-mail bez @ | koszyk niepusty | 1. Zamówienie 2. wypełnij 3. Zamawiam | anna.example.com | komunikat „Podaj poprawny e-mail”, zamówienie odrzucone |
