# Lista płac krok po kroku: od brutto do netto
Tydzień 5 · lekcja 17 z 46 · ≈ 65 min

**Po tej lekcji potrafisz:** liczysz listę płac od brutto do netto w poprawnej kolejności i z poprawnymi zaokrągleniami oraz umiesz ją skontrolować.

**Po co mi to?** lista płac to produkt, który co miesiąc trafia do 62 osób, ZUS i urzędu skarbowego — jedna zła kolejność kroków (np. KUP przed składkami) mnoży się przez wszystkich pracowników.

## Czego potrzebujesz
- Lekcja „Wskaźniki 2026” (składki, KUP, PIT-2) — tu składasz je w pełną listę.
- Warsztat → Lista płac: kalkulator z krokami, „Tryb ćwiczenia” (najpierw wpisujesz swoje netto) i lista miesiąca (zapis MD + CSV do 04-place/).
- Kartoteka osób (Warsztat → Firma ćwiczeniowa): zasadnicze, KUP, PIT-2, PPK każdej osoby.
- Pojęcia: przychód oskładkowany, podstawa zdrowotnej, podstawa opodatkowania, zaliczka, netto, bilans listy.

## 1 · Wyjaśnienie od podstaw
### Osiem kroków w stałej kolejności
| Krok | Co liczysz | Jak |
|---|---|---|
| 1 | przychód brutto | wszystkie składniki wypłacone w miesiącu: zasadnicze, nadgodziny, nocne, premie, świadczenia w naturze, wpłata pracodawcy na PPK (jako przychód) |
| 2 | podstawa i składki społeczne | podstawa = przychód bez wyłączeń z rozporządzenia składkowego; składki pracownika: emerytalna 9,76%, rentowa 1,5%, chorobowa 2,45% — każda zaokrąglona do grosza; limit 30-krotności dla emerytalnej i rentowej |
| 3 | podstawa i składka zdrowotna | podstawa = podstawa społecznych − składki społeczne pracownika + wynagrodzenie chorobowe; składka 9%, nie wyższa niż hipotetyczna zaliczka wg zasad z 2021 |
| 4 | podstawa opodatkowania | przychód − składki społeczne pracownika − KUP (250/300) + PPK pracodawcy (już w przychodzie) − przychody zwolnione; zaokrąglona do pełnych złotych |
| 5 | zaliczka | 12% (lub 32% po przekroczeniu 120 000 zł dochodu narastająco) − kwota zmniejszająca (300/150/100 wg PIT-2); zaokrąglenie do pełnych złotych |
| 6 | PPK pracownika | 2% (0,5–2%) od podstawy składek — potrącane z netto |
| 7 | potrącenia | komornik, dobrowolne |
| 8 | netto | brutto − społeczne − zdrowotna − zaliczka − PPK pracownika − potrącenia |
### Co jest wyłączone ze składek (rozporządzenie składkowe)
Odprawy. Nagrody jubileuszowe co 5 lat. Ekwiwalenty za pranie. Diety do limitu. ZFŚS z kryterium socjalnym. PPK pracodawcy.
Ograniczenie zdrowotnej do hipotetycznej zaliczki jest ważne przy niskich przychodach i uldze dla młodych.
Przychody zwolnione z PIT to m.in. ulga dla młodych i ZFŚS do 1 000 zł.
### Zaokrąglenia
| Co | Jak |
|---|---|
| składki | do 1 grosza, matematycznie |
| zdrowotna | do grosza |
| podstawa opodatkowania i zaliczka | do pełnego złotego: do 49 gr w dół, od 50 gr w górę |
### Trzy składniki specjalne
| Składnik | Składki społeczne | Zdrowotna | PIT |
|---|---|---|---|
| wynagrodzenie chorobowe | nie | tak | tak |
| zasiłek | nie | nie | zaliczka 12% bez KUP, z kwotą zmniejszającą, jeśli PIT-2 |
| świadczenie w naturze (auto) | tak — dodajesz do podstaw | tak | tak; nie wypłacasz |
### Kontrola listy
- Bilans: brutto = netto + wszystkie obciążenia pracownika.
- Porównanie z poprzednim miesiącem; odchylenia powyżej 10% wyjaśniasz.
- Zgodność z ewidencją czasu pracy.
- Progi narastająco: 120 000 dochodu, 85 528 ulga dla młodych, 282 600 składki.
- Zgodność oświadczeń z kartoteką.
### Termin wypłaty (art. 85)
Stały, z dołu, do 10. dnia następnego miesiąca. Gdy to dzień wolny — poprzedni dzień roboczy.
Co najmniej raz w miesiącu. Przelew na konto; gotówka tylko na wniosek.

## 2 · Demonstracja — kompletny przykład omówiony krok po kroku
**Brutto 7 200 zł (6 000 + 800 nadgodzin + 400 premii) z PPK — osiem kroków w stałej kolejności**

```
Brutto 7 200 zł (6 000 zasadnicze + 800 nadgodziny + 400 premia), KUP 250, PIT-2, PPK 2%/1,5%:
społeczne: 702,72 + 108,00 + 176,40 = 987,12 → podst. zdrow. 6 212,88 → zdrowotna 559,16
PPK pracodawcy 108,00 (przychód) → podstawa PIT = 7 200 + 108 − 987,12 − 250 = 6 070,88 → 6 071 → 12% = 728,52 − 300 = 428,52 → 429
PPK pracownika 144,00 → netto = 7 200 − 987,12 − 559,16 − 429 − 144 = 5 080,72 zł
```

1. „społeczne: 702,72 + 108,00 + 176,40 = 987,12”: podstawa składek = wszystkie składniki oskładkowane (7 200); emerytalna 9,76%, rentowa 1,5%, chorobowa 2,45% — każda osobno do grosza; gdyby pracownik przekroczył 282 600 zł narastająco, emerytalnej i rentowej nie byłoby od nadwyżki.
2. „podst. zdrow. 6 212,88 → zdrowotna 559,16”: 7 200 − 987,12; 9%. Wynagrodzenie chorobowe (gdyby było) wchodzi tu, choć nie ma składek społecznych.
3. „PPK pracodawcy 108,00 (przychód)”: 1,5% × 7 200 — pracodawca wpłaca do instytucji, pracownik nie dostaje gotówki, ale to jego przychód do PIT (bez ZUS). Dlatego podstawa PIT zaczyna się od 7 200 + 108.
4. „podstawa PIT = 7 308 − 987,12 − 250 = 6 070,88 → 6 071”: odejmujesz składki społeczne pracownika i KUP; zaokrąglasz do pełnych złotych (art. 63 Ordynacji).
5. „12% = 728,52 − 300 = 428,52 → 429”: stawka 12% (dochód narastająco poniżej 120 000), kwota zmniejszająca 300 (PIT-2), zaliczka do pełnego złotego.
6. „PPK pracownika 144,00”: 2% × 7 200 — schodzi z netto (po podatku).
7. „netto = 7 200 − 987,12 − 559,16 − 429 − 144 = 5 080,72”: odejmujesz tylko to, co pracownik rzeczywiście płaci; PPK pracodawcy nie odejmujesz (nie było wypłacone).
8. Bilans kontrolny: netto + społeczne + zdrowotna + zaliczka + PPK pracownika = 7 200 → 5 080,72 + 987,12 + 559,16 + 429 + 144 = 7 200,00 ✔. Koszt pracodawcy: 7 200 + składki pracodawcy (wypadkowa 1,2%) + 108 = 8 748,72.

✔ **Oczekiwany wynik:** netto 5 080,72 zł; zaliczka 429; bilans brutto = netto + obciążenia pracownika zgadza się co do grosza.

## 3 · Jak to uruchomić
1. Warsztat → Lista płac → Osoba „— własne dane —”, Zasadnicze 6000, Nadgodziny/premie 1200, PPK 2 / 1,5, KUP 250, PIT-2 300 → pole „Tryb ćwiczenia — moje netto”: wpisz swoje 5 080,72 → „Sprawdź”.
2. Jeśli się zgadza — zobaczysz ✔ i kroki; jeśli nie — Mentor podpowie, jakiej kwocie równa się różnica (np. „różnica równa się: PPK pracodawcy”).
3. „Dodaj do listy miesiąca” → powtórz dla kolejnych osób → „Pokaż listę miesiąca” → „Zapisz listę (MD + CSV)” → plik 04-place/lista_plac_2026-11.md w katalogu projektu.
4. Oczekiwany wynik: tabela listy z wierszem RAZEM; suma zaliczek = kwota do US do 20. następnego miesiąca.

## W praktyce — jak to robisz w firmie
1. Zbierz składniki z ewidencji i kartoteki (zasadnicze, nadgodziny, nocne, premie, benefity, chorobowe/zasiłki).
2. Policz: 3 składki osobno → zdrowotna → podstawa PIT (zaokrąglona) → zaliczka − PIT-2 → PPK → potrącenia.
3. Zrób bilans (brutto = netto + obciążenia) i porównaj z poprzednim miesiącem.
4. Zatwierdź do 8., przelew do 10., paski dla pracowników.

## 4 · Ćwiczenie prowadzone
Policz na kartce listę za listopad 2026 dla Ewy Sobczak (5 200 zł zasadnicze, nadgodziny 573,75 — z lekcji o nadgodzinach, KUP 250, PIT-2, PPK 2%/1,5%) w ośmiu krokach jak w demonstracji; sprawdź w Trybie ćwiczenia i dodaj do listy miesiąca. Plik: cwiczenia/tydzien_05/lista_plac_krok_1.md. Czas: 20 minut.

📄 Plik startowy: `cwiczenia/tydzien_05/lista_plac_krok_1.md` · rozwiązanie: `rozwiazania/tydzien_05/lista_plac_krok_1.md`
✔ Poprawny wynik wygląda tak: brutto 5 773,75; społeczne 563,52 + 86,61 + 141,46 = 791,59; zdrowotna 448,39; PPK pracodawcy 86,61; podstawa PIT 4 819; zaliczka 278; PPK pracownika 115,48; netto 4 140,29 zł (bilans: 4 140,29 + 791,59 + 448,39 + 278 + 115,48 = 5 773,75).

## 5 · Ćwiczenie samodzielne
Na liście za listopad Marek Zieliński (5 400) chorował 10 dni (wynagrodzenie chorobowe 1 334,60 — policzysz je w tygodniu 7; teraz przyjmij tę kwotę). Zdecyduj, które kroki rachunku zmienia wynagrodzenie chorobowe (składki społeczne? zdrowotna? PIT? FP?), policz pensję za przepracowaną część i netto. Plik: cwiczenia/tydzien_05/lista_plac_krok_2.md. Czas: 20 minut.

📄 Plik startowy: `cwiczenia/tydzien_05/lista_plac_krok_2.md` · rozwiązanie: `rozwiazania/tydzien_05/lista_plac_krok_2.md`
✔ Poprawny wynik wygląda tak: pensja za część miesiąca 5 400 − 5 400/30 × 10 = 3 600; składki społeczne tylko od 3 600 (351,36 + 54,00 + 88,20 = 493,56); zdrowotna od 3 600 − 493,56 + 1 334,60 = 4 441,04 → 399,69; PIT: przychód 3 600 + 1 334,60 + 54,00 (PPK) − 493,56 − 250 = 4 245,04 → 4 245 → 509,40 − 300 → 209; PPK pracownika 72,00 (od 3 600); netto 3 600 + 1 334,60 − 493,56 − 399,69 − 209 − 72 = 3 760,35; FP/FGŚP należne (pensja umowna 5 400 ≥ minimalne).

## 6 · Typowe błędy i naprawa
- ✘ **Tryb ćwiczenia: „Różnica równa się kwocie: PPK pracodawcy 1.5%”.**
  - Prawdopodobna przyczyna: Odjęto wpłatę pracodawcy od netto (nie jest wypłacana) albo nie dodano jej do podstawy PIT.
  - Jak sprawdzić: Czy w podstawie PIT jest brutto + 1,5%? Czy w netto odjęto tylko 2%?
  - Poprawka: Podstawa PIT z PPK pracodawcy; netto minus PPK pracownika.
- ✘ **Tryb ćwiczenia: różnica kilku złotych bez wskazania kroku.**
  - Prawdopodobna przyczyna: Brak zaokrągleń podstawy PIT i zaliczki do pełnych złotych lub KUP odjęty przed składkami.
  - Jak sprawdzić: Sprawdź kolejność: brutto → składki → zdrowotna → (brutto + PPK pracod. − składki − KUP) zaokr. → zaliczka zaokr.
  - Poprawka: Powtórz rachunek w tej kolejności; porównaj krok po kroku z „Policz”.
- ✘ **Suma zaliczek na liście ≠ kwota przelana do US.**
  - Prawdopodobna przyczyna: Zaliczki od zasiłków (12%, bez KUP) liczone poza listą albo lista dodatkowa (wyrównanie) pominięta.
  - Jak sprawdzić: „Pokaż listę miesiąca” → wiersz RAZEM → porównaj z przelewem.
  - Poprawka: Każda wypłata w miesiącu (także dodatkowa) trafia na listę; zaliczka do US = suma wszystkich.

## Pułapki
- Zaokrąglanie 13,71% jedną kwotą — składki osobno.
- KUP odejmujesz także od wynagrodzenia chorobowego (tak — to przychód ze stosunku pracy), ale nie od zasiłku.

## Dodatkowe zadania
1. Policz ręcznie 4 806 zł w 4 wariantach (bez PPK / z PPK / bez PIT-2 / ulga dla młodych) — zadanie 1 tygodnia 4.
2. Zbuduj w Warsztacie listę miesiąca dla 8 pracowników z FIRMA.md (każdy wiersz najpierw na kartce, potem „Sprawdź”) i zapisz MD + CSV.
3. Sprawdź, co się dzieje ze składką zdrowotną pracownika 1/2 etatu 2 500 zł bez PIT-2 — i przy 1 200 zł (1/4 etatu) z PIT-2; wyjaśnij różnicę.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Od jakiej podstawy liczysz składkę zdrowotną?**
  - Od podstawy składek społecznych pomniejszonej o składki społeczne pracownika (13,71%).
- **Czy wpłata pracodawcy na PPK obniża netto?**
  - Pośrednio — jest przychodem do PIT (zaliczka rośnie), ale nie potrąca się jej z wynagrodzenia.
- **Do czego zaokrąglasz podstawę opodatkowania?**
  - Do pełnych złotych (49 gr w dół, 50 gr w górę).

## Co potrafię teraz zrobić bez patrzenia na przykład?
Policzyć listę płac z nadgodzinami, PPK i wynagrodzeniem chorobowym w stałej kolejności ośmiu kroków, zrobić bilans i zapisać listę miesiąca z Warsztatu.

## Test (w Mentorze: Lekcje → Sprawdź się)
- Ile wynosi netto przy 4 806 zł brutto, KUP 250, PIT-2, bez PPK (2026)?
  - A) 3 505,85
  - B) 3 605,85
  - C) 3 773,85
  - D) 3 305,85
- Które składki nalicza się od wynagrodzenia chorobowego?
  - A) Społeczne i zdrowotną
  - B) Tylko zdrowotną
  - C) Żadnych
  - D) Tylko społeczne
- Kwotę zmniejszającą (300 zł) odejmujesz od:
  - A) Podstawy opodatkowania
  - B) Obliczonej zaliczki (12% podstawy)
  - C) Przychodu
  - D) Składki zdrowotnej

Odpowiedzi: B, B, B
