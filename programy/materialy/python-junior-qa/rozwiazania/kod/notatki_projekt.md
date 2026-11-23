# Cudzy projekt — notatki

## README.md
Opisuje aplikację do ewidencji wypożyczeń sprzętu w klubie i podaje, jak ją uruchomić poleceniem python app.py.

## app.py
Punkt wejścia: menu w pętli w bloku main, wywołuje funkcje z baza.py i raport.py, sam nie liczy niczego.

## baza.py
Warstwa danych: funkcje zapisz i wczytaj zapisują listę wypożyczeń do pliku JSON i odczytują ją przy starcie.

## raport.py
Funkcja raport_miesieczny liczy wypożyczenia w danym miesiącu i zwraca słownik sprzęt → liczba wypożyczeń.

## Pytania
- Co się stanie, gdy plik JSON jest uszkodzony — czy program to obsługuje?
- Dlaczego daty są zapisywane jako tekst, a nie w formacie ISO?
