# Rozwiązanie — ćwiczenie 2 (samodzielne) — Bezpieczeństwo agenta: prompt injection, uprawnienia, sekrety, obce repozytoria

Najpierw własna próba. Podpowiedzi odkrywaj po kolei.

## Podpowiedź 1
Read deny obejmuje Edit i Write tej ścieżki.

## Podpowiedź 2
Dowolne podprocesy — poza zasięgiem reguł; potrzebny sandbox.

## Podpowiedź 3
.claudeignore nie ma efektu — zastępują go reguły Read deny.

## Rozwiązanie
Prawda, fałsz, prawda, fałsz.

## Oczekiwany wynik
(1) prawda; (2) fałsz; (3) prawda; (4) fałsz.

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co się zmieni, gdy zmienisz jedną daną (granicę, typ, plik)?
