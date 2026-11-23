# Rozwiązanie — ćwiczenie 1 (prowadzone) — WebDriverWait i Page Object Model

Najpierw własna próba. Podpowiedzi odkrywaj po kolei.

## Podpowiedź 1
Atrybut dla testów w nawiasach kwadratowych.

## Podpowiedź 2
Tekst odczytujesz, gdy element jest widoczny.

## Podpowiedź 3
open() w demonstracji zwraca…

## Rozwiązanie
(1) `SUMA = (By.CSS_SELECTOR, "[data-test=suma]")`; (2) `EC.visibility_of_element_located(self.SUMA)`; (3) `return self`.

## Oczekiwany wynik
(1) [data-test=suma]; (2) visibility_of_element_located; (3) self.

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co się zmieni, gdy zmienisz jedną daną (granicę, typ, plik)?
