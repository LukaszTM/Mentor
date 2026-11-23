# Rozwiązanie — ćwiczenie 1 (prowadzone) — pytest: test_, assert, uruchamianie, pytest.raises i pytest.approx

Najpierw własna próba. Podpowiedzi odkrywaj po kolei.

## Podpowiedź 1
100 × 1.23.

## Podpowiedź 2
10 × 1.08.

## Podpowiedź 3
Wyjątek sprawdzasz menedżerem kontekstu pytest.

## Rozwiązanie
`assert brutto(100) == 123.0`, `assert brutto(10, 8) == 10.8`, `assert brutto(0) == 0.0`; `with pytest.raises(ValueError):` + `wydaj(5, 10)` wcięte pod spodem.

## Oczekiwany wynik
(1) 123.0; (2) 10.8; (3) 0.0; (4) with pytest.raises(ValueError):.

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co się zmieni, gdy zmienisz jedną daną (granicę, typ, plik)?
