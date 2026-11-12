# Przykład — Dokumenty zgłoszeniowe ZUS: ZUA, ZZA, ZWUA, ZCNA, ZIUA, kody tytułu
Tydzień 8

**Pracownik z rentą i umiarkowanym stopniem, zatrudniony 16.11.2026 — ZUA, ZCNA, ZWUA i premia po ustaniu**

```
Pracownik zatrudniony 16.11.2026 (umowa podpisana 10.11, praca od 16.11), ma rentę, umiarkowany stopień: ZUA do 23.11 z kodem 01 10 2 2, data powstania obowiązku 16.11.2026 (wszystkie ubezpieczenia), NFZ lubelski. Żona bez pracy: ZCNA do 7 dni od oświadczenia (kod 01 — małżonek). Umowa kończy się 31.03.2027 (upływ czasu): ZWUA do 7.04.2027, data 1.04.2027, kod 100, tryb: upływ czasu — art. 30 §1 pkt 4 KP. Premia roczna wypłacona 15.05.2027 → RCA 05/2027 z kodem 30 00.
```

## Omówienie — co robi każdy krok i dlaczego
1. „umowa podpisana 10.11, praca od 16.11 → ZUA do 23.11 z kodem 01 10 2 2, data 16.11.2026”: obowiązek ubezpieczeń powstaje z dniem nawiązania stosunku pracy = rozpoczęcia pracy (16.11), nie podpisania umowy; termin 7 dni (art. 36 ust. 4 ustawy systemowej); kod: 01 10 (pracownik) + 2 (renta) + 2 (umiarkowany stopień).
2. „wszystkie ubezpieczenia, NFZ lubelski”: ZUA = emerytalne, rentowe, chorobowe, wypadkowe (obowiązkowe) + zdrowotne; oddział NFZ wg miejsca zamieszkania; pola „dobrowolne” zostają puste (pracownik ma chorobowe obowiązkowe — symulator to przypomni ostrzeżeniem).
3. „Żona bez pracy: ZCNA do 7 dni od oświadczenia (kod 01 — małżonek)”: członka rodziny bez własnego tytułu zgłaszasz do zdrowotnego na wniosek pracownika; kody pokrewieństwa 01 małżonek, 11 dziecko własne; ZCNA składasz do osoby już zgłoszonej (symulator sprawdza).
4. „Umowa kończy się 31.03.2027: ZWUA do 7.04.2027, data 1.04.2027, kod 100, tryb: upływ czasu — art. 30 §1 pkt 4 KP”: data wyrejestrowania = dzień następny po ustaniu tytułu; kod przyczyny 100 (ustanie tytułu); dla pracownika obowiązkowo tryb rozwiązania i podstawa prawna (od 2022) — symulator blokuje ZWUA bez trybu.
5. „Premia roczna wypłacona 15.05.2027 → RCA 05/2027 z kodem 30 00”: przychód wypłacony po ustaniu zatrudnienia podlega składkom wg zasady kasowej — w RCA za miesiąc wypłaty z kodem 30 00 (osoba, której tytuł ustał), bez ponownego ZUA.

✔ Oczekiwany wynik: ZUA 01 10 2 2 (16.11, do 23.11) → ZCNA (małżonek, kod 01) → ZWUA (1.04.2027, kod 100, tryb 7 — upływ czasu, art. 30 §1 pkt 4) → RCA 30 00 za maj 2027.

## Jak to uruchomić
1. Warsztat → eZUS / Płatnik → „Wyczyść wszystkie zgłoszenia (zacznij od nowa)” (jeśli ćwiczyłeś wcześniej) → Dokument zgłoszeniowy: Osoba Anna Kowalczyk, ZUA, kod 011000, data 2026-10-01 → „Weryfikuj (jak Płatnik)” → brak błędów → „Wyślij do ZUS (symulacja)” → UPP w Rejestrze.
2. Powtórz ZUA dla tej samej osoby → błąd: „Osoba jest już zgłoszona z tym tytułem — najpierw ZWUA (lub ZUA w trybie korekty)”.
3. ZWUA: data 2027-01-01, kod 100, tryb 7 → Weryfikuj → Wyślij. Potem ZCNA dla innej osoby: PESEL członka (symulator sprawdza sumę kontrolną), pokrewieństwo 11.
4. Oczekiwany wynik: Rejestr pokazuje dokumenty ze statusem „przyjęty” i numerami UPP; karta „Ubezpieczeni” — aktualny stan każdej osoby.
