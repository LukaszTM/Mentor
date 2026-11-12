# Rozwiązanie — ćwiczenie 1 (prowadzone) — Kalendarz kadrowo-płacowy: miesięczny, roczny, cykliczny
Plik startowy: `cwiczenia/tydzien_09/kalendarz_roczny_1.md`

Zasada: najpierw własna próba. Podpowiedzi odkrywaj po kolei — rozwiązanie dopiero na końcu.

## Podpowiedź 1 — pytanie naprowadzające
Termin wypłaty w dzień wolny przesuwasz do przodu czy do tyłu? A termin ZUS/PIT?

## Podpowiedź 2 — gdzie szukać
Demonstracja, kroki 1 i 4; art. 85 §3 KP (wypłata — dzień poprzedni) vs art. 12 §5 Ordynacji (deklaracje/składki — dzień następny).

## Podpowiedź 3 — częściowy przykład
Szkic: wypłata 8.01; PPK do 11.01; ZUS 15.01 (pt); PIT/IWA 31.01 (nd) → 1.02; powrót z urlopu — lista: stanowisko, RSA, FP…

## Pełne rozwiązanie
```
| Termin | Zdarzenie | Podstawa | Właściciel | Co robisz |
|---|---|---|---|---|
| 8.01.2027 (pt) | wypłata za grudzień — 10.01 to niedziela → dzień roboczy POPRZEDNI | art. 85 §3 KP, regulamin | kadry + księgowa | lista zatwierdzona 6.01, przelewy 7.01, paski, potrącenia komornicze |
| 11.01 (pon) | umowa o prowadzenie PPK Anny Kowalczyk (90 dni minęło 29.12; termin „do 10. dnia następnego miesiąca” — 10.01 niedziela → 11.01) | art. 16 ustawy o PPK | kadry | zawarcie w portalu instytucji; wpłaty od pierwszej wypłaty po zawarciu (10.02.2027) |
| 12.01 (wt) | powrót z urlopu rodzicielskiego | art. 183² KP; art. 104a ustawy o promocji zatrudnienia | kadry | dopuszczenie na dotychczasowe stanowisko; aktualizacja kartoteki; zwolnienie z FP/FGŚP 36 mies. (do 11.01.2030); ewentualny wniosek o obniżony etat (art. 186⁷) |
| 15.01 (pt) | komplet 01 12 2026 (wypłata 10.12), przelew na NRS, plik i przelew PPK za grudzień | art. 47 ustawy systemowej; art. 28 ustawy o PPK | kadry | Weryfikuj → Wyślij → UPP; księgowa: przelew 14.01 |
| 20.01 (śr) | zaliczki PIT za grudzień (wypłata 10.12) na mikrorachunek; DEK-I-0 za grudzień | art. 38 PIT; art. 49 ustawy o rehabilitacji | księgowa / kadry | suma zaliczek z listy 12/2026 |
| 25.01 (pon) | Wn-D (jeśli SOD) | art. 26c | kadry | wniosek w SODiR |
| do 31.01 (nd → 1.02) | PIT-4R, PIT-8AR, PIT-11 do US (e-Deklaracje, UPL-1); ZUS IWA za 2026 | art. 38, 39, 42 PIT; art. 31 ustawy wypadkowej | księgowa + kadry | uzgodnienie zaliczek z przelewami; IWA: liczba ubezpieczonych, wypadki, zatrudnieni w warunkach zagrożenia |
| styczeń | aktualizacja wskaźników 2027 (minimalne 4 950, limit 30-krotności, odpis ZFŚS, współczynnik 20,92) | obwieszczenia/rozporządzenia | kadry | parametry w programie, aneksy dla pensji < 4 950, nowe kwoty wolne |
```

## Oczekiwany wynik
11.01 (pon) wypłata — regulamin: 10. w niedzielę → dzień roboczy WCZEŚNIEJ, czyli 8.01 (piątek)! (wynagrodzenie, gdy termin wypada w dzień wolny, wypłaca się dnia poprzedniego — art. 85 §3); 12.01 powrót z rodzicielskiego — dopuszczenie na dotychczasowym stanowisku, ZUS: koniec RSA 319, zwolnienie z FP/FGŚP przez 36 mies.; umowa o prowadzenie PPK Kowalczyk do 11.01 (termin „do 10. dnia” wypada w niedzielę → następny dzień roboczy, art. 115 KC); 15.01 (pt) komplet 01 12 2026 + składki + PPK; do 31.01 (nd → 1.02): PIT-4R, PIT-8AR, PIT-11 do US; IWA; 31.01 zgłoszenie ZUS IWA za 2026 (jeśli firma ma obowiązek — ≥ 10 ubezpieczonych i wpis do REGON: tak).

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co by się zmieniło, gdyby zmienił się jeden fakt (etat, staż, data, kwota)?
