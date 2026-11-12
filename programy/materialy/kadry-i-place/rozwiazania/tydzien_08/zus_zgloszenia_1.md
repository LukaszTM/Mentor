# Rozwiązanie — ćwiczenie 1 (prowadzone) — Dokumenty zgłoszeniowe ZUS: ZUA, ZZA, ZWUA, ZCNA, ZIUA, kody tytułu
Plik startowy: `cwiczenia/tydzien_08/zus_zgloszenia_1.md`

Zasada: najpierw własna próba. Podpowiedzi odkrywaj po kolei — rozwiązanie dopiero na końcu.

## Podpowiedź 1 — pytanie naprowadzające
Które z 5 osób w ogóle NIE podlegają zgłoszeniu w ZUS i jaki dokument zamiast tego?

## Podpowiedź 2 — gdzie szukać
Demonstracja, kroki 1–2; Ściąga → kody tytułu (01 10 pracownik, 04 11 zleceniobiorca) i szósty znak = niepełnosprawność (0–3).

## Podpowiedź 3 — częściowy przykład
Tabela — pierwszy wiersz: „Kowalczyk | ZUA | 01 10 0 0 | 2026-10-01 | do 2026-10-08 | UPP …”; Sobczak: 01 10 0 2; Pawlak: 04 11 0 0 + dobrowolne chorobowe; Król: 04 11 0 0; Michalska: RUD (bez ZUA).

## Pełne rozwiązanie
```
| Osoba | Dokument | Kod tytułu | Data powstania | Termin | Uwagi |
|---|---|---|---|---|---|
| Anna Kowalczyk | ZUA | 01 10 0 0 | 2026-10-01 | 2026-10-08 | wszystkie ubezpieczenia; UPP z Rejestru |
| Ewa Sobczak | ZUA | 01 10 0 2 | 2021-03-01 | 2021-03-08 | szósty znak 2 = lekki stopień niepełnosprawności; symulator ostrzega o terminie (data historyczna) |
| Agnieszka Pawlak | ZUA | 04 11 0 0 | 2026-02-01 | 2026-02-08 | jedyny tytuł → pełne składki; zaznacz „dobrowolne chorobowe” (od dnia wniosku, nie wstecz) |
| Robert Król | ZUA | 04 11 0 0 | 2024-06-01 | 2024-06-08 | pełne składki; PPK obsługujesz poza ZUS |
| Joanna Michalska | — (RUD) | — | umowa 2026-11-02 | 2026-11-09 | umowa o dzieło: brak tytułu; RUD przez eZUS w 7 dni od zawarcia, chyba że wykonawca jest pracownikiem zamawiającego |
Michał Dąbrowski (student) — poza ćwiczeniem: brak zgłoszenia (symulator: „nie zgłaszasz go wcale”).
```

## Oczekiwany wynik
4 ZUA przyjęte z UPP; Michalska — brak zgłoszenia (RUD w 7 dni od 2.11 → do 9.11.2026); Sobczak kod 011002; terminy: 7 dni od daty powstania obowiązku; symulator ostrzega „Zgłoszenie po terminie 7 dni” dla dat historycznych — w notatce zaznaczasz, że ćwiczysz wstecz.

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co by się zmieniło, gdyby zmienił się jeden fakt (etat, staż, data, kwota)?
