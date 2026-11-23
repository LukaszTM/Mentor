# Rozwiązanie — ćwiczenie 2 (samodzielne) — WebDriverWait i Page Object Model

Najpierw własna próba. Podpowiedzi odkrywaj po kolei.

## Podpowiedź 1
Czekasz na warunek, nie na zegar.

## Podpowiedź 2
until rzuca wyjątek po przekroczeniu czasu.

## Podpowiedź 3
Klasa strony wie JAK, test sprawdza CO.

## Rozwiązanie
(1) `WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "promocja")))`; (2) TimeoutException; (3) w teście — strona zwraca tekst, test go sprawdza.

## Oczekiwany wynik
(1) WebDriverWait…; (2) TimeoutException; (3) w teście.

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co się zmieni, gdy zmienisz jedną daną (granicę, typ, plik)?
