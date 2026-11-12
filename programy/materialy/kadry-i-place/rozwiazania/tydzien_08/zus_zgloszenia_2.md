# Rozwiązanie — ćwiczenie 2 (samodzielne) — Dokumenty zgłoszeniowe ZUS: ZUA, ZZA, ZWUA, ZCNA, ZIUA, kody tytułu
Plik startowy: `cwiczenia/tydzien_08/zus_zgloszenia_2.md`

Zasada: najpierw własna próba. Podpowiedzi odkrywaj po kolei — rozwiązanie dopiero na końcu.

## Podpowiedź 1 — pytanie naprowadzające
Czy zmiana kodu tytułu to ZIUA, czy ZWUA + ZUA? (ZIUA zmienia dane identyfikacyjne — PESEL, nazwisko — nie kod.)

## Podpowiedź 2 — gdzie szukać
Warsztat → Przepisy → „Tytuły do ubezpieczeń, zbiegi, zgłoszenia” (art. 9 ust. 1, art. 36 ust. 14); demonstracja krok 4 (ZWUA = dzień po ustaniu, ale przy korekcie kodu — data pierwotna).

## Podpowiedź 3 — częściowy przykład
Szkic: (a) ZWUA 1.06.2024 (korekta) + ZUA 0411 1.06.2024; (b) ZWUA 1.09.2026 + ZZA 0411 1.09.2026; (c) społeczne IX–XI: 3 × 479,85 = 1 439,55 (pracownik), 3 × 611 (pracodawca) …

## Pełne rozwiązanie
```
(a) Błędny kod tytułu od początku: ZWUA z kodem 01 10 00 i datą 1.06.2024 (wyrejestrowanie „od początku” — w Płatniku jako korekta zgłoszenia) oraz ZUA z prawidłowym kodem 04 11 00 od 1.06.2024 (w 7 dni od wykrycia). Kwoty składek za 06/2024–08/2026 nie zmieniają się (zleceniobiorca z jedynym tytułem ma te same stopy), ale RCA za każdy miesiąc musi mieć kod 04 11 → komplety korygujące za 27 miesięcy (lekcja „Korekty ZUS”); ZUS może też sam przeksięgować po wyjaśnieniu — zapytaj przez eZUS.
(b) Od 1.09.2026 zbieg tytułów (art. 9 ust. 1 i 1a ustawy systemowej): etat z podstawą 5 500 ≥ minimalne 4 806 → ze zlecenia obowiązkowo tylko zdrowotna, społeczne dobrowolne. Dokumenty: tytuł trwa, zmienia się tylko schemat ubezpieczeń → ZWUA z kodem przyczyny 600 („inna przyczyna”) z datą 1.09.2026 i ZZA 04 11 00 od 1.09.2026. Oświadczenie Króla o etacie do akt; ponowne sprawdzenie, gdyby etat ustał.
(c) IX–XI 2026: składki społeczne nienależne → nadpłata: pracownika 13,71% × 3 500 × 3 = 1 439,55 (do zwrotu — stanowi jego przychód w miesiącu zwrotu, PIT 12%, zdrowotna 9%), pracodawcy (9,76 + 6,5 + 1,2)% × 10 500 = 1 832,88 (zaliczenie na przyszłe składki lub wniosek RZS-P). Zdrowotna niedopłata: 9% × 3 500 = 315,00 zamiast 271,81 → +43,19 × 3 = 129,57 (do dopłaty, część ubezpieczonego potrąca się z jego zwrotu za zgodą). Komplet korygujący 02 09 2026, 02 10 2026, 02 11 2026 (DRA + RCA Króla z ZZA-schematem). PPK: zleceniobiorca bez obowiązkowych składek ER wypada z PPK od 1.09 — wpłaty IX–XI do zwrotu.
```

## Oczekiwany wynik
(a) ZWUA z datą 1.06.2024 w trybie korekty (wyrejestrowanie błędnego kodu) + ZUA 04 11 00 od 1.06.2024 — składki były pełne, więc kwoty się nie zmieniają, ale RCA za wszystkie miesiące wymagają korekty kodu (30 miesięcy!); (b) od 1.09.2026 zbieg: etat ≥ minimalne → ze zlecenia tylko zdrowotna → ZWUA (04 11) z datą 1.09.2026 + ZZA 04 11 00 od 1.09.2026; (c) nadpłata: społeczne za IX–XI 2026 nienależne: pracownik 13,71% × 3 500 × 3 = 1 439,55 (zwrot; przychód, PIT), pracodawca (9,76 + 6,5 + 1,2)% × 10 500 = 1 832,88 (zaliczenie); zdrowotna wzrośnie (od 3 500 zamiast 3 020,15: +43,19/mies.); korekta RCA 09–11/2026 z identyfikatorem 02 i DRA.

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co by się zmieniło, gdyby zmienił się jeden fakt (etat, staż, data, kwota)?
