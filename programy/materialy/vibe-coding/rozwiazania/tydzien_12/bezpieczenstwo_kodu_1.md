# Rozwiązanie — ćwiczenie 1 (prowadzone) — Bezpieczeństwo kodu od AI: XSS, wstrzyknięcia, sekrety, zależności

Najpierw własna próba. Podpowiedzi odkrywaj po kolei.

## Podpowiedź 1
escape zamienia znaki specjalne HTML na encje.

## Podpowiedź 2
< staje się &lt;.

## Podpowiedź 3
Przeglądarka pokaże &lt; jako znak, nie wykona skryptu.

## Rozwiązanie
escape daje &lt;script&gt;… — tekst, nie znacznik. Bezpieczna jest linia 2.

## Oczekiwany wynik
Pierwszy znak w wersji z escape: & (z &lt;); bezpieczna linia 2.

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co się zmieni, gdy zmienisz jedną daną (granicę, typ, plik)?
