# Rozwiązanie — ćwiczenie 2 (samodzielne) — Testy aplikacji webowej: Flask test_client, testy E2E Selenium własnej aplikacji i CI

Najpierw własna próba. Podpowiedzi odkrywaj po kolei.

## Podpowiedź 1
Serwer CI nie ma ekranu ani Edge.

## Podpowiedź 2
Każdy test potrzebuje świeżej bazy.

## Podpowiedź 3
Szybka informacja zwrotna najpierw.

## Rozwiązanie
(1) na ubuntu-latest: Chrome headless zamiast Edge z oknem; (2) `create_app(tmp_path / "test.db")` w fixturze; (3) test_client → E2E.

## Oczekiwany wynik
(1) przeglądarka bez trybu headless / Edge niedostępny na ubuntu; (2) baza w tmp_path przez create_app; (3) najpierw szybkie (test_client), potem E2E.

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co się zmieni, gdy zmienisz jedną daną (granicę, typ, plik)?
