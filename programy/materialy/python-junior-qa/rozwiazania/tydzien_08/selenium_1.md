# Rozwiązanie — ćwiczenie 1 (prowadzone) — Selenium WebDriver: przeglądarka, lokatory (ID, CSS, XPath), formularze

Najpierw własna próba. Podpowiedzi odkrywaj po kolei.

## Podpowiedź 1
By.ID przyjmuje samą wartość id.

## Podpowiedź 2
CSS po atrybucie: [nazwa=wartość].

## Podpowiedź 3
XPath: //znacznik[text()='…'].

## Rozwiązanie
(1) `(By.ID, "dodaj-3")`; (2) `(By.CSS_SELECTOR, "[data-test=dodaj]")` — ale uwaga: każdy przycisk „Dodaj” ma ten sam data-test, więc find_element weźmie pierwszy; (3) `(By.XPATH, "//button[text()='Dodaj do koszyka']")`.

## Oczekiwany wynik
(1) dodaj-3; (2) [data-test=dodaj]; (3) //button[text()='Dodaj do koszyka'].

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co się zmieni, gdy zmienisz jedną daną (granicę, typ, plik)?
