# Przykład — Narzędzia: eZUS/PUE, Płatnik, e-Urząd Skarbowy, program kadrowy
Tydzień 0

**Miesięczny obieg dokumentów w firmie 62-osobowej — co, gdzie, do kiedy**

```
Miesięczny obieg w firmie 62-osobowej:
1. do 5. — zamknięcie ewidencji czasu pracy, e-ZLA z eZUS
2. do 8. — lista płac w programie, kontrola, przelewy na 10.
3. do 15. — eksport KEDU → Płatnik → weryfikacja → wysyłka DRA/RCA/RSA; przelew składek na NRS; plik PPK do instytucji
4. do 20. — zaliczka PIT na mikrorachunek; DEK-I-0 PFRON
5. do 25. — Wn-D (dofinansowanie niepełnosprawnych, jeśli dotyczy)
```

## Omówienie — co robi każdy krok i dlaczego
1. „do 5. — zamknięcie ewidencji czasu pracy, e-ZLA z eZUS”: bez zamkniętej ewidencji nie policzysz nadgodzin ani nocnych; e-ZLA (elektroniczne zwolnienia) pobierasz z eZUS — w Mentorze: Warsztat → eZUS / Płatnik → karta e-ZLA.
2. „do 8. — lista płac, kontrola, przelewy na 10.”: regulamin AGRO-MLEKO każe wypłacać do 10.; dwa dni rezerwy na kontrolę listy (bilans brutto = netto + obciążenia). Symulator: Warsztat → Lista płac.
3. „do 15. — KEDU → Płatnik → weryfikacja → wysyłka DRA/RCA/RSA; przelew na NRS; plik PPK”: spółka z o.o. rozlicza ZUS do 15. dnia następnego miesiąca; NRS to indywidualny numer rachunku składkowego firmy. Symulator: karta „Rozliczenie DRA/RCA/RSA” → Weryfikuj → Wyślij (dostajesz numer UPP, jak w prawdziwym Płatniku).
4. „do 20. — zaliczka PIT na mikrorachunek; DEK-I-0 PFRON”: zaliczki pracowników za miesiąc wypłaty wpłacasz do 20. następnego; DEK-I-0 to deklaracja wpłat na PFRON, gdy firma nie osiąga 6% zatrudnienia osób z niepełnosprawnością.
5. „do 25. — Wn-D”: wniosek o dofinansowanie wynagrodzeń pracowników niepełnosprawnych — tylko gdy firma z niego korzysta.
6. Kto podpisuje: dokumenty ZUS wysyła osoba z PEL (pełnomocnictwo złożone w ZUS przez prezesa), deklaracje PIT — osoba z UPL-1 (złożone w urzędzie skarbowym). Nowy pracownik kadr bez tych pełnomocnictw może przygotować dokumenty, ale nie może ich wysłać.

✔ Oczekiwany wynik: kalendarz miesiąca: 5. ewidencja → 8. lista → 10. wypłata → 15. ZUS + PPK → 20. PIT + PFRON → 25. Wn-D, z osobą odpowiedzialną przy każdym terminie.

## Jak to uruchomić
1. Warsztat → eZUS / Płatnik → karta „Ubezpieczeni”: zobacz 12 osób firmy (to rejestr, jaki widzi płatnik w eZUS).
2. Karta „Dokument zgłoszeniowy”: wybierz osobę, typ ZUA, kod 011000, datę → „Weryfikuj (jak Płatnik)” → zobacz komunikaty (błędy na czerwono blokują wysyłkę, ostrzeżenia nie).
3. Warsztat → e-Urząd: PIT → „Generuj PIT-11” dla dowolnej osoby → „Wyślij (symulacja, UPO)” → zobacz numer UPO.
4. Oczekiwany wynik: rozumiesz, że każdy dokument ma trzy stany: przygotowany → zweryfikowany → wysłany z potwierdzeniem (UPP/UPO), i że numer potwierdzenia archiwizujesz.
