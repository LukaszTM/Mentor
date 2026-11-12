# Rozwiązanie — ćwiczenie 1 (prowadzone) — Korekty ZUS: po błędzie, po 30-krotności, po kontroli; nadpłaty i zwroty
Plik startowy: `cwiczenia/tydzien_08/zus_korekty_1.md`

Zasada: najpierw własna próba. Podpowiedzi odkrywaj po kolei — rozwiązanie dopiero na końcu.

## Podpowiedź 1 — pytanie naprowadzające
Od kiedy student przestaje być zwolniony ze składek — od daty oświadczenia czy od faktycznej utraty statusu?

## Podpowiedź 2 — gdzie szukać
Demonstracja, kroki 2–3; Warsztat → Przepisy → „Odsetki, przedawnienie, korekty” (korekta w 7 dni od stwierdzenia, odsetki od dnia po terminie).

## Podpowiedź 3 — częściowy przykład
Szkic: ZUA 16.09; 02 10 2026 (wypłata 10.10 — podstawa ~1 000 za 16–30.09) i 02 11 2026 (2 000); składki: zleceniobiorca 13,71%, zleceniodawca 9,76 + 6,5 + 1,2 = 17,46% (FP: 2 000 < 4 806 → bez), zdrowotna 9%…

## Pełne rozwiązanie
```
1. Zgłoszenie: ZUA 04 11 00 z datą 16.09.2026 (dzień po skreśleniu) — w 7 dni od powzięcia informacji (do 27.11), ale obowiązek istniał od 16.09; dobrowolne chorobowe — tylko od dnia wniosku, nie wstecz.
2. Komplety korygujące: 02 10 2026 — RCA Dąbrowskiego za wypłatę 10.10 (wynagrodzenie za 16–30.09 ≈ 1 000 zł; jeśli umowa płatna za cały wrzesień 2 000 — składki od części przypadającej po 15.09 nie da się wydzielić bez ewidencji godzin → przyjmij proporcję z ewidencji) + DRA; 02 11 2026 — RCA za wypłatę 10.11 (2 000) + DRA. Komplet 12/2026 (wypłata 10.12) — już pierwotny z Dąbrowskim.
3. Składki do dopłaty (podstawa 3 000): zleceniobiorca 13,71% = 411,30 — firma musi je zapłacić do ZUS; potrącić z jego wynagrodzenia może tylko za zgodą (brak przepisu uprawniającego do jednostronnego potrącenia składek za okresy wsteczne); zleceniodawca: emerytalna 292,80 + rentowa 195,00 + wypadkowa 36,00 = 523,80 (FP/FGŚP: 2 000 < 4 806 → nie); zdrowotna 9% × 2 588,70 = 232,98 (część ubezpieczonego — j.w. za zgodą).
4. Odsetki: od sumy kompletu 10/2026 za okres 16.11.2026 → dzień zapłaty; 11/2026 od 16.12; stopa 14,5% rocznie; jeśli łącznie < 48,06 zł — ZUS nie pobiera.
5. PIT: ulga dla młodych nie zależy od składek → zaliczka nadal 0; w PIT-11 za 2026 wykażesz składki społeczne i zdrowotne pobrane (jeśli potrącone).
6. PPK: od 16.09 obowiązkowe składki ER → „osoba zatrudniona”; umowa o prowadzenie po 3 miesiącach (do 10.01.2027), chyba że złoży rezygnację.
7. Do akt: oświadczenie o utracie statusu z datą wpływu; procedura: sprawdzanie statusu studenta w lutym i październiku.
```

## Oczekiwany wynik
ZUA 04 11 00 od 16.09.2026 (jedyny tytuł → pełne składki; chorobowe dobrowolne od wniosku); komplety 02 10 2026 (RCA za wrzesień: podstawa 16–30.09 ≈ 1 000) i 02 11 2026 (RCA za październik: 2 000); niedopłata: zleceniobiorca 13,71% × 3 000 = 411,30 (można potrącić z bieżącej wypłaty tylko za zgodą — inaczej płaci firma), zleceniodawca 17,46% × 3 000 = 523,80; zdrowotna 9% × (3 000 − 411,30) = 232,98; odsetki od sum za każdy komplet od 16.11 / 16.12 do dnia zapłaty; PIT: ulga dla młodych nadal — zaliczka 0; PPK: od 16.09 Dąbrowski jest „osobą zatrudnioną” → umowa o prowadzenie po 3 miesiącach (do 10.01.2027).

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co by się zmieniło, gdyby zmienił się jeden fakt (etat, staż, data, kwota)?
