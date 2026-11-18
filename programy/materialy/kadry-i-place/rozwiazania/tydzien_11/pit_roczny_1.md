# Rozwiązanie — ćwiczenie 1 (prowadzone) — Rozliczenie roczne płatnika: PIT-4R, PIT-8AR, PIT-11, IFT-1R, korekty
Plik startowy: `cwiczenia/tydzien_11/pit_roczny_1.md`

Zasada: najpierw własna próba. Podpowiedzi odkrywaj po kolei — rozwiązanie dopiero na końcu.

## Podpowiedź 1 — pytanie naprowadzające
Ile wypłat Kowalczyk dostała W ROKU 2026 (daty!), a ile miesięcy przepracowała?

## Podpowiedź 2 — gdzie szukać
Demonstracja, krok 1 (zasada kasowa); Warsztat → Lista płac: osoba Kowalczyk, listy za 2026-10 i 2026-11 (pole „Wypłata w miesiącu”: 2026-11 i 2026-12) → dodaj do list → e-Urząd: PIT → Generuj.

## Podpowiedź 3 — częściowy przykład
Szkic: 2 wypłaty × 6 000 = 12 000; KUP 500; społeczne 1 645,20; zaliczki 2 × 291 = 582; lista za grudzień (wypłata 8.01.2027) to już rok 2027 — z PPK pracodawcy w przychodzie…

## Pełne rozwiązanie
```
PIT-11 za 2026 (Anna Kowalczyk):
- Przychód ze stosunku pracy: 2 wypłaty (10.11, 10.12) × 6 000 = 12 000,00 (wpłat PPK w 2026 r. jeszcze nie było)
- Koszty uzyskania: 2 × 250 = 500,00
- Dochód (poz. 31): 12 000 − 500 = 11 500,00 — w PIT-11 dochód to przychód minus koszty; składki społeczne są osobno, w poz. 95, i podatnik odliczy je w zeznaniu (w liście płac do progu 120 000 zł liczysz dochód po składkach: 12 000 − 500 − 1 645,20 = 9 854,80)
- Zaliczka pobrana: 2 × 291 = 582,00 (podstawa 6 000 − 822,60 − 250 = 4 927 → 12% − 300 = 291)
- Składki na ubezpieczenia społeczne podlegające odliczeniu: 1 645,20
- Składka zdrowotna (2 × 465,97 = 931,94) — część G, poz. 122: wykazujesz ją informacyjnie (od 2022 r. bez odliczenia od podatku).
Pensja za grudzień (wypłata 8.01.2027) → PIT-11 za 2027. W 2027 r. dojdzie PPK: wpłata pracodawcy 90 zł miesięcznie zwiększa przychód ze stosunku pracy (zaliczka 302 zamiast 291), wpłat pracownika (120 zł) nie wykazujesz — nie obniżają podatku. Terminy: do US (e-Deklaracje, UPL-1) do 31.01.2027 (niedziela → 1.02.2027); pracownikowi do 28.02.2027 (niedziela → 1.03.2027). Warsztat → e-Urząd: PIT daje te same kwoty, jeśli w kartotece są listy za 2026-10 i 2026-11 (wypłaty w 2026-11 i 2026-12) z PPK 0 / 0.
```

## Oczekiwany wynik
w 2026 r. wypłacono 2 pensje (10.11 i 10.12): przychód 2 × 6 000 = 12 000 (bez PPK — pierwsze wpłaty w 2027); KUP 2 × 250 = 500; dochód w PIT-11 (poz. 31) = przychód − koszty = 11 500; składki społeczne 2 × 822,60 = 1 645,20 wykazujesz osobno (poz. 95) — do progu 120 000 zł w liście płac liczy się dochód po składkach: 9 854,80; zaliczki 2 × 291 = 582; zdrowotna 2 × 465,97 = 931,94 (część G, poz. 122 — informacyjnie); pensja grudniowa (wypłata 8.01.2027) → PIT-11 za 2027, w którym przychód powiększą wpłaty pracodawcy na PPK (90 zł miesięcznie).

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co by się zmieniło, gdyby zmienił się jeden fakt (etat, staż, data, kwota)?
