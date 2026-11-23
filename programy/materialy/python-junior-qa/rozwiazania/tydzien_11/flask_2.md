# Rozwiązanie — ćwiczenie 2 (samodzielne) — Flask: strony, szablony, formularze z walidacją i komunikaty

Najpierw własna próba. Podpowiedzi odkrywaj po kolei.

## Podpowiedź 1
Atrybuty HTML sprawdza przeglądarka, nie serwer.

## Podpowiedź 2
Żądanie można wysłać z pominięciem formularza.

## Podpowiedź 3
Złe dane klienta to 4xx, błąd serwera to 5xx.

## Rozwiązanie
(1) nie — required/min działa tylko w przeglądarce, serwer musi walidować sam; (2) `test_client.post("/dodaj", data={"ilosc": "0"})`; (3) 400 dla złych danych, 500 oznacza defekt serwera.

## Oczekiwany wynik
(1) nie; (2) test_client.post z ilosc=0; (3) 400, 500.

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co się zmieni, gdy zmienisz jedną daną (granicę, typ, plik)?
