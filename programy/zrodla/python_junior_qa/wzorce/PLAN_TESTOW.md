# Plan testów — Magazyn

## Zakres
- produkty: dodawanie z walidacją, lista, filtr kategorii
- operacje przyjęcia i wydania z kontrolą stanu, historia
- interfejs webowy: lista, formularz, strona produktu

## Poza zakresem
- wydajność i bezpieczeństwo sieciowe (aplikacja lokalna)

## Ryzyka
- wydanie ponad stan albo blokada wydania całego stanu (granica)
- SQL injection w filtrze kategorii
- testy zmieniające prawdziwą bazę

## Poziomy i techniki
- jednostkowe/integracyjne: pytest z bazą w tmp_path, wartości brzegowe stanu (0, stan, stan + 1), klasy równoważności danych formularza
- E2E: 3 ścieżki w Selenium (POM) na serwerze testowym

## Co automatyzuję, co testuję ręcznie
- automatycznie: reguły, baza, strony (test_client), ścieżki krytyczne (Selenium)
- ręcznie: wygląd i czytelność komunikatów, sesja eksploracyjna formularza

## Kryteria zakończenia
- wszystkie testy zielone w CI, brak otwartych defektów o ważności wysokiej

## Znalezione defekty
- wydanie całego stanu było blokowane (warunek >= zamiast >) — naprawione, test regresji test_wydanie_calego_stanu
- cena z przecinkiem odrzucana w formularzu — naprawione (replace(",", "."))
- duplikat nazwy z inną wielkością liter przechodził — naprawione
