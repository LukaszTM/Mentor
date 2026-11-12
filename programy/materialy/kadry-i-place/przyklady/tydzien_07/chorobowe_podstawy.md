# Przykład — Wynagrodzenie chorobowe i zasiłek chorobowy: 33/14 dni, okres zasiłkowy, e-ZLA
Tydzień 7

**Operator 42 lata, 6 000 zł — trzy zwolnienia w 2026 r.: kto płaci, ile dni, który okres zasiłkowy**

```
Operator (42 lata), 6 000 zł, podstawa zasiłku 5 177,40 (6 000 − 13,71%), stawka dzienna 172,58.
Zwolnienia 2026: 10–19.03 (10 dni), 2–25.06 (24 dni; przerwa > 60 dni, ale dni liczą się do 33 w roku), 1–20.10 (20 dni).
Marzec: stawka dzienna 172,58 × 80% = 138,06; 10 dni × 138,06 = 1 380,60 (wynagrodzenie chorobowe; pula 23 dni).
Czerwiec: 23 dni chorobowe (23 × 138,06 = 3 175,38) + 1 dzień zasiłek (138,06) — od 25.06 zasiłek; przerwa marzec–czerwiec 74 dni → nowy okres zasiłkowy od 2.06 (dni: 24).
Październik: od 1. dnia zasiłek (pula 33 wyczerpana); przerwa od 25.06 do 1.10 = 97 dni → nowy okres zasiłkowy. Pensja za czerwiec: 6 000 − 6 000/30 × 24 = 1 200 + chorobowe + zasiłek.
```

## Omówienie — co robi każdy krok i dlaczego
1. „podstawa 5 177,40 (6 000 − 13,71%), stawka dzienna 172,58, 80% = 138,06”: podstawa wymiaru to przeciętne wynagrodzenie z 12 miesięcy po odliczeniu składek 13,71% (szczegóły w następnej lekcji); dzielisz przez 30 (zawsze 30, także w lutym), mnożysz przez 80% i zaokrąglasz do grosza — dopiero potem przez dni.
2. „Marzec 10–19.03: 10 dni × 138,06 = 1 380,60 — wynagrodzenie chorobowe; pula 23 dni”: pierwsze 33 dni niezdolności w roku kalendarzowym opłaca pracodawca (art. 92 §1); liczysz dni kalendarzowe (z weekendem); po marcu zostaje 23 dni.
3. „Czerwiec 2–25.06 (24 dni): 23 dni chorobowe (3 175,38) + 1 dzień zasiłek (138,06)”: 23 dni wyczerpują pulę 33; od 24. dnia czerwcowego zwolnienia (25.06) — zasiłek z ZUS (AGRO-MLEKO jako płatnik zasiłków wypłaca go i odlicza w DRA).
4. „przerwa marzec–czerwiec 74 dni → nowy okres zasiłkowy od 2.06”: okres zasiłkowy (182 dni) liczy się łącznie dla niezdolności bez przerwy ORAZ z przerwami ≤ 60 dni; 74 dni przerwy → licznik 182 startuje od nowa (dla tej samej i innej choroby). Pula 33 dni NIE startuje od nowa — ona zeruje się tylko 1 stycznia.
5. „Październik 1–20.10: od 1. dnia zasiłek (pula wyczerpana); przerwa 97 dni → nowy okres zasiłkowy”: wynagrodzenia chorobowego już nie ma do końca roku; zasiłek 80% × 20 dni; w RSA kod 313 (zasiłek) zamiast 331 (wynagrodzenie chorobowe).
6. „Pensja za czerwiec: 6 000 − 6 000/30 × 24 = 1 200 + chorobowe + zasiłek”: pensja za 6 przepracowanych dni (dzielnik 30), do tego 3 175,38 chorobowego (zdrowotna i PIT, bez społecznych) i 138,06 zasiłku (tylko PIT, bez KUP). e-ZLA: lekarz wystawia elektronicznie, płatnik widzi je w eZUS (w Mentorze: Warsztat → eZUS/Płatnik → e-ZLA → „Pobierz do RSA”).

✔ Oczekiwany wynik: marzec: 10 dni chorobowego; czerwiec: 23 chorobowego + 1 zasiłku; październik: 20 dni zasiłku; dwa nowe okresy zasiłkowe (2.06 i 1.10); pula 33 wyczerpana 24.06.

## Jak to uruchomić
1. Warsztat → Zasiłki i chorobowe → karta B: Od 2026-03-10, Do 2026-03-19, choroba → „Dodaj nieobecność”; potem 2026-06-02 – 2026-06-25; 2026-10-01 – 2026-10-20; Stawka dzienna 172,58 → wynik pokazuje podział dni i kwoty (138,06/dzień).
2. Zaznacz „pracownik 50+” → zobacz, jak zmienia się podział (14 dni).
3. Warsztat → eZUS / Płatnik → karta e-ZLA: zobacz zwolnienia osób z firmy (kody A/B/C/D/E, okresy) → „Pobierz do RSA” zapisuje je jako przerwy do raportu.
4. Oczekiwany wynik: Twój ręczny podział dni = podział z Warsztatu; w pliku cwiczenia/tydzien_07/chorobowe_podstawy_1.md tabela zwolnień z kolumnami: od–do | dni | chorobowe | zasiłek | % | okres zasiłkowy | kod RSA.
