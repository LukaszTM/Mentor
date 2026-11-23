# Rozwiązanie — ćwiczenie 1 (prowadzone) — parametrize i fixtures: wiele przypadków w jednym teście, wspólne dane, tmp_path

Najpierw własna próba. Podpowiedzi odkrywaj po kolei.

## Podpowiedź 1
Dwie granice: 100 i 300.

## Podpowiedź 2
Dla każdej: tuż pod i na granicy.

## Podpowiedź 3
Każda para = osobny test.

## Rozwiązanie
(1) 4 pary; (2) 5; (3) 4 testy, np. test_rabat[99.99-0].

## Oczekiwany wynik
(1) 4 pary: (99.99, 0), (100, 5), (299.99, 5), (300, 10); (2) 5; (3) 4.

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co się zmieni, gdy zmienisz jedną daną (granicę, typ, plik)?
