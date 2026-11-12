# Rozwiązanie — ćwiczenie 1 (prowadzone) — Narzędzia: eZUS/PUE, Płatnik, e-Urząd Skarbowy, program kadrowy
Plik startowy: `cwiczenia/tydzien_00/narzedzia_kadrowca_1.md`

Zasada: najpierw własna próba. Podpowiedzi odkrywaj po kolei — rozwiązanie dopiero na końcu.

## Podpowiedź 1 — pytanie naprowadzające
Kto w spółce z o.o. jest „pracodawcą” uprawnionym do udzielania pełnomocnictw? (Zarząd — tu prezes.)

## Podpowiedź 2 — gdzie szukać
W lekcji sekcja o PEL/UPL-1; w Warsztat → Firma ćwiczeniowa: struktura firmy i kto podpisuje.

## Podpowiedź 3 — częściowy przykład
Wiersz wzorcowy: „eZUS | podgląd ubezpieczonych, e-ZLA, saldo, wysyłka ePłatnikiem | specjalista kadr | PEL (ZUS-PEL) | prezes zarządu”.

## Pełne rozwiązanie
```
| System | Do czego | Kto w firmie | Pełnomocnictwo | Podpisuje |
|---|---|---|---|---|
| eZUS | ubezpieczeni, e-ZLA, saldo składek, Z-3, ePłatnik | specjalista ds. kadr i płac | PEL złożony w ZUS | prezes zarządu |
| Płatnik | ZUA/ZWUA, DRA/RCA/RSA, weryfikacja, wysyłka z certyfikatem | specjalista ds. kadr i płac | PEL + certyfikat kwalifikowany na osobę | prezes (PEL); certyfikat kupuje firma |
| e-Urząd Skarbowy | PIT-4R, PIT-11, UPO, mikrorachunek | główna księgowa / kadry | UPL-1 złożone w US | prezes zarządu |
| PPK (PFR TFI) | pliki wpłat, rejestracja uczestników, rezygnacje | kadry | upoważnienie wewnętrzne + konto administratora w portalu instytucji | prezes |
| praca.gov.pl | powiadomienia o cudzoziemcach, oświadczenia | kadry | profil zaufany + pełnomocnictwo firmy w portalu | prezes |
| program kadrowy | kartoteki, listy płac, eksport KEDU | kadry, księgowa | uprawnienia w programie (role) | administrator |
```

## Oczekiwany wynik
6 wierszy; przy eZUS i Płatniku — PEL podpisany przez prezesa; przy e-Urzędzie — UPL-1 podpisany przez prezesa, złożony w US; przy PPK — upoważnienie wewnętrzne + dostęp do portalu instytucji; praca.gov.pl — profil zaufany pracownika kadr + pełnomocnictwo firmy.

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co by się zmieniło, gdyby zmienił się jeden fakt (etat, staż, data, kwota)?
