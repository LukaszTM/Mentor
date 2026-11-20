# Rozwiązanie — ćwiczenie 2 (samodzielne) — Terminal bez strachu: CMD i PowerShell

Najpierw własna próba. Podpowiedzi odkrywaj po kolei.

## Podpowiedź 1
Zachęta z literami PS na początku oznacza PowerShell, bez nich — CMD.

## Podpowiedź 2
`irm` to polecenie PowerShell.

## Podpowiedź 3
Dokumentacja: „'irm' is not recognized” = jesteś w CMD.

## Rozwiązanie
Okno to CMD (brak PS). Właściwa: wersja z curl i install.cmd. Komenda PowerShell w CMD daje błąd „'irm' is not recognized…”, a komenda CMD w PowerShell — „The token '&&' is not a valid statement separator”.

## Oczekiwany wynik
Zachęta bez PS = CMD → komenda z curl … install.cmd. Gdybyś wkleił `irm …` w CMD, zobaczysz „'irm' is not recognized as an internal or external command”.

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co się zmieni, gdy zmienisz jedną daną (granicę, typ, plik)?
