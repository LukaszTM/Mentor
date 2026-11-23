# Rozwiązanie — ćwiczenie 2 (samodzielne) — parametrize i fixtures: wiele przypadków w jednym teście, wspólne dane, tmp_path

Najpierw własna próba. Podpowiedzi odkrywaj po kolei.

## Podpowiedź 1
Globalna lista jest wspólna — zmiany zostają.

## Podpowiedź 2
Fixtura tworzy dane od nowa dla każdego testu.

## Podpowiedź 3
Wbudowana fixtura z katalogiem tymczasowym.

## Rozwiązanie
(1) tak — test_a zmienia wspólną listę; (2) `@pytest.fixture`; (3) `tmp_path`.

## Oczekiwany wynik
(1) tak; (2) @pytest.fixture; (3) tmp_path.

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co się zmieni, gdy zmienisz jedną daną (granicę, typ, plik)?
