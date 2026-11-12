# Narzędzia: eZUS/PUE, Płatnik, e-Urząd Skarbowy, program kadrowy
Tydzień 0 · lekcja 3 z 46 · ≈ 50 min

**Po tej lekcji potrafisz:** wiesz, do czego służą eZUS, Płatnik, e-Urząd Skarbowy i program kadrowy, kto podpisuje PEL/UPL-1 i jak wygląda miesięczny obieg dokumentów.

**Po co mi to?** miesiąc kadrowca to stały obieg dokumentów między programem kadrowym, ZUS, urzędem skarbowym i PPK — kto go nie zna, spóźnia się z terminami, a spóźnienie kosztuje odsetki i mandaty.

## Czego potrzebujesz
- Warsztat: narzędzia „eZUS / Płatnik” i „e-Urząd: PIT” (symulatory — bez kont, bez instalacji; wyglądają i weryfikują jak prawdziwe systemy).
- Karta firmy FIRMA.md z zadania 1 (kto podpisuje dokumenty: prezes; kadry działają z pełnomocnictwa).
- Pojęcia: PEL (pełnomocnictwo w ZUS), UPL-1 (pełnomocnictwo do podpisywania deklaracji podatkowych), KEDU (plik z dokumentami ZUS eksportowany z programu kadrowego), UPP/UPO (urzędowe potwierdzenia odbioru).

## 1 · Wyjaśnienie od podstaw
### Cztery systemy, bez których nie da się pracować
| System | Do czego służy | Kto ma dostęp |
|---|---|---|
| eZUS (dawniej PUE ZUS) | portal ZUS: ubezpieczeni, e-ZLA pracowników, saldo składek, wnioski (Z-3, US-3 → A1, zaświadczenie o niezaleganiu), pisma z ZUS | pracownik kadr z pełnomocnictwem PEL podpisanym przez zarząd |
| Płatnik | program ZUS do dokumentów zgłoszeniowych (ZUA, ZZA, ZWUA, ZCNA) i rozliczeniowych (DRA, RCA, RSA, RPA); weryfikacja i wysyłka z certyfikatem kwalifikowanym | małe firmy mogą użyć ePłatnika w eZUS |
| e-Urząd Skarbowy / e-Deklaracje | PIT-4R, PIT-11, PIT-8AR, IFT składasz elektronicznie | osoba z pełnomocnictwem UPL-1 zgłoszonym do US |
| program kadrowo-płacowy (Symfonia, Optima, enova, Gratyfikant…) | generuje listy płac, dokumenty ZUS (eksport do Płatnika — plik KEDU) i PIT-11 | kadry i płace |
Program liczy, ale Ty odpowiadasz za błędy. Dlatego musisz rozumieć, co jest w środku każdego dokumentu.
Zaliczki PIT wpłacasz na mikrorachunek podatkowy firmy (NIP).
PIT-11 to tylko suma kartoteki przychodów. Kartotekę prowadzisz poprawnie przez cały rok.
### Pozostałe portale
- praca.gov.pl — powiadomienia o cudzoziemcach, PUP.
- e-PFRON2 — DEK, Wn-D.
- portal sprawozdawczy GUS.
- platforma PPK instytucji finansowej — zapisy, wpłaty (plik).
- e-Doręczenia — od 2025 obowiązkowe dla firm; tu przychodzą pisma urzędowe.
### Bezpieczeństwo dostępów
- Każda osoba ma oddzielne konto i własne uprawnienia.
- Prowadzisz rejestr pełnomocnictw.
- Gdy pracownik kadr odchodzi, odwołujesz jego pełnomocnictwa tego samego dnia.
### W tym kursie: Warsztat zamiast kont
Żadnego z tych systemów nie musisz zakładać ani instalować. Zakładka Warsztat w Mentorze ma ich symulatory.
| Narzędzie Warsztatu | Co odpowiada prawdziwemu systemowi |
|---|---|
| eZUS / Płatnik | rejestr ubezpieczonych, dokumenty zgłoszeniowe z weryfikacją jak w Płatniku, komplety DRA/RCA/RSA, skrzynka e-ZLA, rejestr z numerami UPP |
| e-Urząd: PIT | PIT-11 i PIT-4R z Twojej kartoteki, UPO |
| kalkulatory | lista płac, zasiłki, urlopy, czas pracy, potrącenia, delegacje |
| Przepisy | biblioteka przepisów offline |
Ekrany i komunikaty odpowiadają prawdziwym. Po kursie przesiadka na eZUS i Płatnika to kwestia logowania, nie nauki od nowa.

## 2 · Demonstracja — kompletny przykład omówiony krok po kroku
**Miesięczny obieg dokumentów w firmie 62-osobowej — co, gdzie, do kiedy**

```
Miesięczny obieg w firmie 62-osobowej:
1. do 5. — zamknięcie ewidencji czasu pracy, e-ZLA z eZUS
2. do 8. — lista płac w programie, kontrola, przelewy na 10.
3. do 15. — eksport KEDU → Płatnik → weryfikacja → wysyłka DRA/RCA/RSA; przelew składek na NRS; plik PPK do instytucji
4. do 20. — zaliczka PIT na mikrorachunek; DEK-I-0 PFRON
5. do 25. — Wn-D (dofinansowanie niepełnosprawnych, jeśli dotyczy)
```

1. „do 5. — zamknięcie ewidencji czasu pracy, e-ZLA z eZUS”: bez zamkniętej ewidencji nie policzysz nadgodzin ani nocnych; e-ZLA (elektroniczne zwolnienia) pobierasz z eZUS — w Mentorze: Warsztat → eZUS / Płatnik → karta e-ZLA.
2. „do 8. — lista płac, kontrola, przelewy na 10.”: regulamin AGRO-MLEKO każe wypłacać do 10.; dwa dni rezerwy na kontrolę listy (bilans brutto = netto + obciążenia). Symulator: Warsztat → Lista płac.
3. „do 15. — KEDU → Płatnik → weryfikacja → wysyłka DRA/RCA/RSA; przelew na NRS; plik PPK”: spółka z o.o. rozlicza ZUS do 15. dnia następnego miesiąca; NRS to indywidualny numer rachunku składkowego firmy. Symulator: karta „Rozliczenie DRA/RCA/RSA” → Weryfikuj → Wyślij (dostajesz numer UPP, jak w prawdziwym Płatniku).
4. „do 20. — zaliczka PIT na mikrorachunek; DEK-I-0 PFRON”: zaliczki pracowników za miesiąc wypłaty wpłacasz do 20. następnego; DEK-I-0 to deklaracja wpłat na PFRON, gdy firma nie osiąga 6% zatrudnienia osób z niepełnosprawnością.
5. „do 25. — Wn-D”: wniosek o dofinansowanie wynagrodzeń pracowników niepełnosprawnych — tylko gdy firma z niego korzysta.
6. Kto podpisuje: dokumenty ZUS wysyła osoba z PEL (pełnomocnictwo złożone w ZUS przez prezesa), deklaracje PIT — osoba z UPL-1 (złożone w urzędzie skarbowym). Nowy pracownik kadr bez tych pełnomocnictw może przygotować dokumenty, ale nie może ich wysłać.

✔ **Oczekiwany wynik:** kalendarz miesiąca: 5. ewidencja → 8. lista → 10. wypłata → 15. ZUS + PPK → 20. PIT + PFRON → 25. Wn-D, z osobą odpowiedzialną przy każdym terminie.

## 3 · Jak to uruchomić
1. Warsztat → eZUS / Płatnik → karta „Ubezpieczeni”: zobacz 12 osób firmy (to rejestr, jaki widzi płatnik w eZUS).
2. Karta „Dokument zgłoszeniowy”: wybierz osobę, typ ZUA, kod 011000, datę → „Weryfikuj (jak Płatnik)” → zobacz komunikaty (błędy na czerwono blokują wysyłkę, ostrzeżenia nie).
3. Warsztat → e-Urząd: PIT → „Generuj PIT-11” dla dowolnej osoby → „Wyślij (symulacja, UPO)” → zobacz numer UPO.
4. Oczekiwany wynik: rozumiesz, że każdy dokument ma trzy stany: przygotowany → zweryfikowany → wysłany z potwierdzeniem (UPP/UPO), i że numer potwierdzenia archiwizujesz.

## W praktyce — jak to robisz w firmie
1. Rozpisz kalendarz miesiąca: 5. ewidencja, 8. lista, 10. wypłata, 15. ZUS/PPK, 20. PIT/PFRON, 25. Wn-D — z właścicielem każdego terminu.
2. Ustal, kto w firmie ma PEL (ZUS) i UPL-1 (US) i kto je podpisuje; wpisz do dostepy.md.
3. Przejdź w symulatorze eZUS/Płatnik pełną ścieżkę dokumentu: przygotuj → weryfikuj → wyślij → UPP w Rejestrze.
4. Wygeneruj w e-Urząd: PIT jeden PIT-11 i zapisz go do projektu — zobacz, które pola rozumiesz.

## 4 · Ćwiczenie prowadzone
Zbuduj plik dostepy.md: tabela „System → do czego → kto ma dostęp w AGRO-MLEKO → jakie pełnomocnictwo → kto je podpisuje”. Wiersze: eZUS, Płatnik, e-Urząd Skarbowy, PPK (instytucja PFR TFI), praca.gov.pl, program kadrowy. Wzór pierwszego wiersza jest w cwiczenia/tydzien_00/narzedzia_kadrowca_1.md. Czas: 20 minut.

📄 Plik startowy: `cwiczenia/tydzien_00/narzedzia_kadrowca_1.md` · rozwiązanie: `rozwiazania/tydzien_00/narzedzia_kadrowca_1.md`
✔ Poprawny wynik wygląda tak: 6 wierszy; przy eZUS i Płatniku — PEL podpisany przez prezesa; przy e-Urzędzie — UPL-1 podpisany przez prezesa, złożony w US; przy PPK — upoważnienie wewnętrzne + dostęp do portalu instytucji; praca.gov.pl — profil zaufany pracownika kadr + pełnomocnictwo firmy.

## 5 · Ćwiczenie samodzielne
15 grudnia 2026 wypada we wtorek, 15 listopada 2026 — w niedzielę, 20 grudnia 2026 — w niedzielę. Zdecyduj dla każdego z tych terminów (ZUS za październik, ZUS za listopad, PIT za listopad), do którego dnia AGRO-MLEKO musi wysłać dokumenty i zapłacić, i uzasadnij regułą przesunięcia. Zapisz w cwiczenia/tydzien_00/narzedzia_kadrowca_2.md. Czas: 10 minut.

📄 Plik startowy: `cwiczenia/tydzien_00/narzedzia_kadrowca_2.md` · rozwiązanie: `rozwiazania/tydzien_00/narzedzia_kadrowca_2.md`
✔ Poprawny wynik wygląda tak: ZUS za X: do 16.11.2026 (poniedziałek — termin przypadający w dzień wolny przesuwa się na następny dzień roboczy, art. 12 §5 Ordynacji / art. 31 ustawy systemowej); ZUS za XI: do 15.12.2026 (wtorek, bez przesunięcia); PIT za XI: do 21.12.2026 (poniedziałek).

## 6 · Typowe błędy i naprawa
- ✘ **Symulator eZUS/Płatnik: „Kod tytułu „0110” nie istnieje (4 cyfry tytułu + emerytura/renta + niepełnosprawność)”.**
  - Prawdopodobna przyczyna: Wpisano 4 znaki zamiast 6 — kod tytułu ma zawsze 6 znaków (01 10 + 0 + 0).
  - Jak sprawdzić: Policz znaki w polu „Kod tytułu”.
  - Poprawka: Wpisz 011000 (pracownik bez emerytury/renty, bez niepełnosprawności).
- ✘ **Zaliczka PIT wpłacona 20. na „konto urzędu skarbowego”.**
  - Prawdopodobna przyczyna: Od 2020 r. wpłaty idą na mikrorachunek podatkowy firmy (generowany z NIP), nie na rachunek urzędu.
  - Jak sprawdzić: Czy numer rachunku zawiera NIP firmy? Generator: podatki.gov.pl (bez logowania).
  - Poprawka: Wygeneruj mikrorachunek z NIP i zapisz go w FIRMA.md.
- ✘ **Dokument ZUS „przygotowany”, ale ZUS go nie widzi.**
  - Prawdopodobna przyczyna: Przygotowanie ≠ wysłanie — brak kroku „Wyślij” albo brak PEL/certyfikatu u osoby wysyłającej.
  - Jak sprawdzić: Czy masz numer UPP dla tego dokumentu? (W symulatorze: karta Rejestr.)
  - Poprawka: Weryfikuj → Wyślij → zapisz UPP; w prawdziwej firmie upewnij się, że PEL jest złożony.

## Pułapki
- Jedno hasło do Płatnika dla całego działu — po odejściu pracownika nikt go nie zmienia.
- Program kadrowy „liczy sam” — ale źle wprowadzony kod tytułu lub oświadczenie daje błędne DRA/PIT przez cały rok.

## Dodatkowe zadania
1. Przejdź w symulatorze eZUS/Płatnik pełną ścieżkę jednego dokumentu: przygotuj ZUA dla Anny Kowalczyk, zweryfikuj, wyślij, znajdź UPP w Rejestrze.
2. Wygeneruj w e-Urząd: PIT PIT-11 dla Haliny Mazur i zapisz go do projektu; zapisz w dzienniku, które pola rozumiesz, a których nie.
3. Wypisz, jakie pełnomocnictwa (PEL, UPL-1) musiałby mieć nowy pracownik kadr i kto je podpisuje.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Kto wysyła DRA, gdy firma zatrudnia 62 osoby?**
  - Płatnik (pracodawca) — przez program Płatnik z certyfikatem lub ePłatnik; w praktyce kadry z pełnomocnictwem PEL.
- **Czym różni się UPL-1 od PEL?**
  - UPL-1 — pełnomocnictwo do podpisywania e-deklaracji podatkowych (US); PEL — pełnomocnictwo do ZUS.
- **Co to jest KEDU?**
  - Plik z dokumentami ZUS (format XML) eksportowany z programu kadrowego do Płatnika.

## Co potrafię teraz zrobić bez patrzenia na przykład?
Rozpisać miesiąc kadrowca z terminami 5/8/10/15/20/25, wskazać, kto i na jakiej podstawie (PEL, UPL-1) wysyła dokumenty, i przesunąć termin, gdy wypada w dzień wolny.

## Test (w Mentorze: Lekcje → Sprawdź się)
- Jakim dokumentem zarząd upoważnia kadrową do działania w ZUS przez eZUS?
  - A) UPL-1
  - B) PEL
  - C) ZUS ZUA
  - D) ZUS PEL-K
- Gdzie wpłacasz zaliczki na PIT od wynagrodzeń?
  - A) Na rachunek ZUS (NRS)
  - B) Na mikrorachunek podatkowy firmy (NIP)
  - C) Na konto pracownika
  - D) Na rachunek PFR
- Kto składa raporty miesięczne RCA/RSA?
  - A) Pracownik przez eZUS
  - B) Płatnik składek (pracodawca)
  - C) Urząd skarbowy
  - D) Instytucja PPK

Odpowiedzi: B, B, B
