# PLAN — Magazyn sklepu „Papierowy Kot”

## Cel
Aplikacja do ewidencji produktów i operacji magazynowych (przyjęcia, wydania) z historią, która zastępuje arkusz. Projekt portfolio pokazujący testowanie na kilku poziomach.

## Zakres
- produkty: dodawanie z walidacją, lista, filtr kategorii
- operacje: przyjęcie i wydanie z kontrolą stanu, historia po dacie
- interfejs: menu w konsoli, potem strona Flask

## Poza zakresem
- logowanie użytkowników i role
- faktury, płatności, wysyłka

## Struktura
- baza.py — SQLite (tabele produkty i operacje), zapytania z parametrami ?
- magazyn.py — logika operacji
- menu_magazyn.py, app.py — interfejsy
- test_baza.py, tests/ — testy

## Kolejność
1. baza.py i testy na bazie tymczasowej
2. magazyn.py i testy reguł (wartości brzegowe stanu)
3. menu w konsoli
4. Flask: lista, formularz, historia produktu
5. testy test_client i E2E Selenium, CI
6. README, PLAN_TESTOW.md

## Ryzyka
- zła kontrola stanu przy wydaniu (granica: wydanie całego stanu)
- SQL injection przy filtrze — tylko parametry ?
- testy na prawdziwej bazie — zawsze tmp_path
