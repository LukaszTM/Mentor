# Rozliczenia miesięczne: DRA, RCA, RSA, RPA, terminy, NRS, zasada kasowa
Tydzień 8 · lekcja 32 z 45 · ≈ 30 min

**Po tej lekcji potrafisz:** składasz komplet DRA/RCA/RSA/RPA wg zasady kasowej, płacisz na NRS w terminie i kontrolujesz spójność z listą płac.

**Po co mi to?** do 15. każdego miesiąca spółka wysyła komplet DRA/RCA/RSA i płaci składki — spóźnienie to odsetki i utrata prawa do zasiłku z dobrowolnego chorobowego, a niezgodność RCA z listą płac wychodzi przy każdej kontroli ZUS.

## Czego potrzebujesz
- Warsztat → Lista płac → lista miesiąca (zapisana) — RCA powstaje z niej; Warsztat → eZUS / Płatnik → karta „Rozliczenie DRA/RCA/RSA” (Dodaj RSA, Pokaż komplet, Weryfikuj, Wyślij, identyfikator).
- Lekcje tygodnia 6 (kody RSA, zasiłki do odliczenia).
- Pojęcia: DRA (deklaracja zbiorcza), RCA (raport imienny — podstawy i składki każdej osoby), RSA (raport o przerwach i świadczeniach — za miesiąc, w którym była przerwa), RPA (przychód za inny rok), zasada kasowa (składki za miesiąc WYPŁATY), identyfikator 01 MM RRRR, NRS (numer rachunku składkowego), termin 15. (osoby prawne) / 20. (pozostali).

## 1 · Wyjaśnienie od podstaw
### Co miesiąc płatnik składa komplet
DRA (deklaracja zbiorcza: liczba ubezpieczonych, sumy składek wg funduszy, kwoty zasiłków wypłaconych przez płatnika do rozliczenia z ZUS, kwota do zapłaty, stopa wypadkowa), RCA (raport imienny: za każdego ubezpieczonego kod tytułu, wymiar etatu, podstawy i składki emerytalna/rentowa/chorobowa/wypadkowa, zdrowotna oraz — od 2022, informacyjnie — kwota wpłaty na PPK finansowanej przez płatnika), RSA (raport o przerwach i świadczeniach: kody przerw, okresy, dni, kwoty zasiłków wypłaconych przez płatnika), RPA (raport o przychodach dla celów emerytalnych — składasz TYLKO gdy wystąpiło: przychód należny za INNY rok kalendarzowy wypłacony w tym miesiącu (trzynastka, premia roczna, wyrównanie), składnik wypłacony OBOK wynagrodzenia chorobowego/zasiłku, od którego nie było składek, a stanowi podstawę do emerytury (dodatek stażowy w pełnej wysokości w czasie choroby), praca nauczycielska, praca w szczególnych warunkach przed 2009).
ZASADA KASOWA:
- w raportach za dany miesiąc wykazujesz przychody WYPŁACONE lub postawione do dyspozycji w tym miesiącu — wynagrodzenie za listopad wypłacone 10 grudnia → DRA/RCA za grudzień (12/2026)
- przy wypłacie do końca miesiąca → za ten miesiąc
- RSA — za miesiąc, którego dotyczy przerwa (nieobecność listopadowa w RSA 11/2026, choć pensja w grudniu) — stąd rozjazd okresów RCA/RSA jest normalny
Identyfikator dokumentu:
- 01 MM RRRR (pierwotny), 02–39 kolejne korekty
- za pracowników i zleceniobiorców — jeden komplet
- przy przekroczeniu 30-krotności — informacja ZUS i korekty
### Terminy złożenia i zapłaty
- do 5. dnia następnego miesiąca — jednostki budżetowe
- do 15. — płatnicy z osobowością prawną (sp. z o.o., S.A., spółdzielnie, fundacje)
- do 20. — pozostali (osoby fizyczne, spółki osobowe)
- dzień wolny → następny roboczy
Wpłata jednym przelewem na indywidualny NRS (numer rachunku składkowego — na zaświadczeniu ZUS; w tytule nic nie trzeba), ZUS rozdziela na fundusze proporcjonalnie, zaliczając najpierw najstarsze zaległości (uwaga: opóźnienie jednej wpłaty „przesuwa” kolejne).
- Odsetki za zwłokę — stawka jak od zaległości podatkowych (stopa na podatki.gov.pl), nie nalicza się, gdy ich kwota nie przekracza 1% minimalnego wynagrodzenia (48,06 zł w 2026)
- opłata dodatkowa do 100% nieopłaconych składek przy uporczywym niepłaceniu
- zaległości ZUS blokują zaświadczenie o niezaleganiu (przetargi, kredyty) i ulgi (ZUS może zawrzeć układ ratalny — wniosek RSR)
Płatnik zasiłków: wypłacone zasiłki (nie wynagrodzenie chorobowe!) odejmujesz w DRA od składek do zapłaty (gdy zasiłki > składki — ZUS zwraca na wniosek). Składki zdrowotne — do NRS tym samym przelewem (od 2018).
### Obowiązki wobec ubezpieczonego
roczna informacja IMIR (dawniej RMUA) do końca lutego za rok poprzedni (lub miesięczna na żądanie — w 7 dni?); w praktyce z programu. Dane na eZUS pracownika — weryfikuje sam.
Kontrola spójności przed wysyłką:
- liczba ubezpieczonych w DRA = liczba RCA
- sumy RCA = DRA
- podstawy RCA = lista płac (brutto − wyłączenia)
- RSA okresy = ewidencja nieobecności
- zdrowotna 9% od (podstawa − społeczne)
- zleceniobiorcy ze zbiegiem — podstawa społecznych 0, zdrowotna pełna
- kody RCA z informacją o etacie (np. 1/1, 1/2)
- wychowawczy — RCA 12 11 z podstawą 60% prognozowanego (5 652 zł w 2026, min. 75% minimalnej) finansowaną z budżetu (w DRA w osobnym bloku), składka zdrowotna od podstawy równej kwocie specjalnego zasiłku opiekuńczego (620 zł)
- PPK — poza ZUS
Korekta po terminie — lekcja o korektach. Przechowywanie dokumentów rozliczeniowych: 5 lat (kopie DRA/RCA/RSA i potwierdzenia).

## 2 · Demonstracja — kompletny przykład omówiony krok po kroku
**Komplet 01 12 2026 AGRO-MLEKO: wypłata za listopad 10.12 — kto trafia do RCA, co do RSA, ile do zapłaty**

```
AGRO-MLEKO (sp. z o.o. → do 15.), wypłata za listopad 10.12.2026, 62 pracowników + 6 zleceniobiorców (3 ze zbiegiem — tylko zdrowotna, 1 student — poza ZUS), 1 osoba na wychowawczym (12 11), 1 na macierzyńskim (zasiłek od płatnika — RSA 327, kwota w DRA do odliczenia), nadgodziny listopadowe i trzynastka za 2025 wypłacona w grudniu (RPA — przychód za inny rok dla 62 osób).
Komplet 01 12 2026: DRA + 68 RCA (62 × 01 10, 5 × 04 11, 1 × 12 11; student bez raportu) + RSA (chorobowe 331, zasiłki 313/312, macierzyński 327, bezpłatny 111 — za okresy GRUDNIOWE) + RPA (trzynastka). Wysyłka i przelew na NRS do 15.01.2027 (do zapłaty = składki − zasiłki wypłacone). Zasiłki za listopad wypłacone 10.12 — rozliczane w DRA 12/2026.
```

1. „wypłata za listopad 10.12.2026 → komplet 01 12 2026, wysyłka i przelew do 15.01.2027”: zasada kasowa — składki rozliczasz w miesiącu WYPŁATY (grudzień), nie za miesiąc pracy; spółka z o.o. ma termin 15. dnia następnego miesiąca (15.01.2027 — piątek).
2. „DRA + 68 RCA (62 × 01 10, 5 × 04 11, 1 × 12 11; student bez raportu)”: każda osoba z podstawą składek ma RCA z kodem tytułu; osoba na wychowawczym — RCA z kodem 12 11 (składki finansowane z budżetu); student na zleceniu — w ogóle poza kompletem; 3 zleceniobiorców ze zbiegiem — RCA tylko ze zdrowotną.
3. „RSA (chorobowe 331, zasiłki 313/312, macierzyński 327, bezpłatny 111)”: dwie reguły — ŚWIADCZENIA (331, 313, 312, 327…) wykazujesz w komplecie za miesiąc, w którym je WYPŁACONO (10.12 → komplet 12/2026), z faktycznym okresem (np. 16–30.11); PRZERWY bez świadczeń (111 urlop bezpłatny, 151, 152) — w komplecie za miesiąc, w którym przerwa WYSTĄPIŁA (bezpłatny z grudnia → 12/2026, z listopada → 11/2026). Symulator ostrzega przy okresie z innego miesiąca — dla świadczeń to normalne.
4. „RPA (trzynastka za 2025 wypłacona w grudniu)”: przychód za inny rok kalendarzowy niż rok wypłaty wykazujesz dodatkowo w RPA (dla celów emerytalnych) — składki normalnie w RCA.
5. „do zapłaty = składki − zasiłki wypłacone”: płatnik zasiłków odejmuje w DRA zasiłki (313/312/327…), NIE wynagrodzenie chorobowe (331) — to koszt pracodawcy; przelew jedną kwotą na NRS firmy.
6. Kontrola przed wysyłką: liczba RCA = liczba ubezpieczonych w DRA; suma podstaw w RCA = suma w DRA; podstawy w RCA = lista płac (przychód oskładkowany); zasiłki w RSA = zasiłki na liście; zachowaj UPP.

✔ **Oczekiwany wynik:** komplet 01 12 2026: DRA + 68 RCA + RSA + RPA, wysłany i opłacony do 15.01.2027; do zapłaty = składki − zasiłki (bez wynagrodzenia chorobowego).

## 3 · Jak to uruchomić
1. Warsztat → Lista płac: dla miesiąca 2026-11 dodaj do listy co najmniej 4 osoby (w tym Zielińskiego z wynagrodzeniem chorobowym 1 201,14 i zasiłkiem 800,76) → „Zapisz listę”.
2. Warsztat → eZUS / Płatnik → Rozliczenie DRA/RCA/RSA: miesiąc 2026-12 (wypłata 10.12!), identyfikator 01 → „Dodaj RSA”: Zieliński 331 16–24.11 kwota 1 201,14; 313 25–30.11 kwota 800,76 → „Pokaż komplet” → sumy DRA → „Weryfikuj” → „Wyślij (symulacja)” → UPP; „Zapisz do projektu” → 05-zus-us/komplet_2026-12.md.
3. Zwróć uwagę na ostrzeżenie o przerwie z innego miesiąca (listopad w komplecie grudniowym) — to zamierzone: wypłata była w grudniu.
4. Oczekiwany wynik: DRA z liczbą ubezpieczonych = liczba wierszy listy, składki = suma z listy, zasiłki odjęte = 800,76 (nie 2 001,90).

## W praktyce — jak to robisz w firmie
1. Po wypłacie wygeneruj komplet z programu (KEDU) → Płatnik → weryfikacja.
2. RCA = podstawy z listy płac; RSA = przerwy z ewidencji za ten miesiąc; RPA, gdy przychód za inny rok.
3. Sprawdź: liczba RCA = DRA, sumy = DRA, zasiłki odjęte (tylko płatnik zasiłków).
4. Wyślij i zapłać na NRS do 15. (osoby prawne) / 20.; zachowaj UPP.

## 4 · Ćwiczenie prowadzone
Zbuduj komplet za 12/2026 (wypłata listopadowa 10.12) dla 8 osób z zadania tygodnia jak w demonstracji: lista płac → RCA; przerwy: Zieliński (331 + 313 jak wyżej), Sobczak opieka 312 16–20.11 kwota 598,30, Nowak urlop bezpłatny 111 2–3.12 (przerwa grudniowa), Michalska — poza kompletem. Policz ręcznie sumę do zapłaty i porównaj z DRA w symulatorze. Plik: cwiczenia/tydzien_08/zus_rozliczenia_1.md. Czas: 25 minut.

📄 Plik startowy: `cwiczenia/tydzien_08/zus_rozliczenia_1.md` · rozwiązanie: `rozwiazania/tydzien_08/zus_rozliczenia_1.md`
✔ Poprawny wynik wygląda tak: RCA: 8 wierszy (Dąbrowski-student i Michalska-dzieło poza); RSA: 331 (kwota informacyjnie, nie odliczana), 313 800,76, 312 598,30, 111 2–3.12 (bez kwoty); DRA: do zapłaty = suma składek społecznych (prac. + pracod.) + zdrowotnych + FP + FGŚP − (800,76 + 598,30); identyfikator 01 12 2026; termin 15.01.2027.

## 5 · Ćwiczenie samodzielne
W styczniu 2027 AGRO-MLEKO wypłaca (10.01) pensje za grudzień oraz 15.01 trzynastkę za 2026 r. dla 62 osób; ponadto 20.01 Ewa Sobczak dostaje zaległe nadgodziny za listopad 2026 (lista dodatkowa). Zdecyduj: (a) w którym komplecie i z jakim identyfikatorem rozliczasz każdą wypłatę, (b) czy potrzebujesz RPA i za kogo, (c) ile wynosi termin i co się dzieje, gdy 15.02.2027 wypada w poniedziałek, a przelew wyszedł 16.02 (kwota składek 180 000 zł, stopa odsetek 14,5%). Plik: cwiczenia/tydzien_08/zus_rozliczenia_2.md. Czas: 15 minut.

📄 Plik startowy: `cwiczenia/tydzien_08/zus_rozliczenia_2.md` · rozwiązanie: `rozwiazania/tydzien_08/zus_rozliczenia_2.md`
✔ Poprawny wynik wygląda tak: (a) wszystkie trzy wypłaty są w styczniu → jeden komplet 01 01 2027 (zasada kasowa; lista dodatkowa nie tworzy osobnego kompletu — sumujesz podstawy w RCA tej osoby); (b) RPA dla 62 osób za trzynastkę (przychód za 2026 wypłacony w 2027) oraz dla Sobczak — nadgodziny za listopad 2026 wypłacone w 2027 to także przychód za inny rok; (c) termin 15.02.2027 (poniedziałek — bez przesunięcia); 1 dzień zwłoki: 180 000 × 14,5% / 365 ≈ 71,51 zł → odsetki ≥ 1% minimalnego (48,06 zł) → ZUS je pobiera (poniżej tego progu — nie); dodatkowo zaległość wyższa niż 1% minimalnego wynagrodzenia (48,06 zł) wstrzymuje wypłatę zasiłków osobom z dobrowolnym chorobowym (zleceniobiorcy) do czasu spłaty.

## 6 · Typowe błędy i naprawa
- ✘ **Symulator: „RCA …: osoba nie figuruje w rejestrze ubezpieczonych (brak ZUA/ZZA)”.**
  - Prawdopodobna przyczyna: Osoba na liście płac bez przyjętego zgłoszenia.
  - Jak sprawdzić: Karta „Ubezpieczeni” — status osoby.
  - Poprawka: Najpierw ZUA (z datą rozpoczęcia pracy), potem komplet.
- ✘ **Symulator: „RCA …: składka emerytalna … ≠ 9,76% × podstawa”.**
  - Prawdopodobna przyczyna: Ręcznie wpisana składka lub podstawa z innego miesiąca.
  - Jak sprawdzić: Porównaj RCA z listą płac (Warsztat → Lista płac → Pokaż listę).
  - Poprawka: RCA zawsze z listy; nie przepisuj ręcznie.
- ✘ **Symulator: „RSA 331: przerwa z innego miesiąca niż raport” (ostrzeżenie) — i komplet wysłany za niewłaściwy miesiąc.**
  - Prawdopodobna przyczyna: RSA za miesiąc wypłaty zamiast za miesiąc przerwy (lub odwrotnie).
  - Jak sprawdzić: Kiedy była przerwa, kiedy wypłata świadczenia?
  - Poprawka: RSA z okresem przerwy; w komplecie za miesiąc wypłaty świadczenia; przerwy bez świadczeń (111, 151) — za miesiąc przerwy.

## Pułapki
- RSA „za miesiąc wypłaty” — nie, RSA za miesiąc, w którym była przerwa.
- Wynagrodzenie chorobowe odejmowane w DRA jak zasiłek — nie, tylko zasiłki.

## Dodatkowe zadania
1. Zbuduj komplet DRA/RCA/RSA dla 8 osób z zadania tygodnia 8 i sprawdź sumy.
2. Ustal, które sytuacje z listy wymagają RPA.
3. Policz odsetki za 10 dni zwłoki od 50 000 zł składek (stopa z podatki.gov.pl) i sprawdź próg 1% minimalnej.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Za który miesiąc składasz RCA z pensją listopadową wypłaconą 10 grudnia?**
  - Za grudzień (zasada kasowa — miesiąc wypłaty).
- **Kiedy składasz RPA?**
  - Gdy w miesiącu wypłacono przychód należny za inny rok, składnik obok chorobowego/zasiłku bez składek, lub przy pracy nauczycielskiej/w szczególnych warunkach.
- **Do kiedy spółka z o.o. opłaca składki?**
  - Do 15. dnia następnego miesiąca (osoby fizyczne — do 20., budżet — do 5.).

## Co potrafię teraz zrobić bez patrzenia na przykład?
Złożyć komplet DRA/RCA/RSA(/RPA) wg zasady kasowej, odjąć w DRA tylko zasiłki, skontrolować zgodność z listą płac i zapłacić na NRS w terminie z wiedzą, co kosztuje spóźnienie.

## Test (w Mentorze: Lekcje → Sprawdź się)
- Dokument z danymi o przerwach w opłacaniu składek i wypłaconych zasiłkach:
  - A) ZUS DRA
  - B) ZUS RCA
  - C) ZUS RSA
  - D) ZUS RPA
- Termin rozliczenia składek dla osoby fizycznej zatrudniającej pracowników:
  - A) Do 5.
  - B) Do 10.
  - C) Do 15.
  - D) Do 20.
- Trzynastka za 2025 wypłacona w marcu 2026 — w raportach za 03/2026 wykazujesz ją:
  - A) Tylko w RCA
  - B) W RCA i RPA (przychód za inny rok)
  - C) Tylko w RPA
  - D) W RSA

Odpowiedzi: C, D, B
