# Rozwiązanie — ćwiczenie 2 (samodzielne) — Bezpieczeństwo kodu od AI: XSS, wstrzyknięcia, sekrety, zależności

Najpierw własna próba. Podpowiedzi odkrywaj po kolei.

## Podpowiedź 1
Tekst od użytkownika w HTML bez escape.

## Podpowiedź 2
Sklejanie SQL.

## Podpowiedź 3
Nazwa podobna do znanej biblioteki.

## Rozwiązanie
XSS, SQL injection, sekret, podejrzana zależność (sprawdź na pypi.org — prawdziwa nazwa to requests).

## Oczekiwany wynik
(1) XSS; (2) SQL injection; (3) sekret w kodzie; (4) podejrzana zależność (literówka „requestz” — możliwy typosquatting/slopsquatting).

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co się zmieni, gdy zmienisz jedną daną (granicę, typ, plik)?
