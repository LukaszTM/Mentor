# Rozwiązanie — ćwiczenie 1 (prowadzone) — Instalacja Claude Code w Windows i pierwsze uruchomienie

Najpierw własna próba. Podpowiedzi odkrywaj po kolei.

## Podpowiedź 1
PS na początku zachęty = PowerShell.

## Podpowiedź 2
Stare okno nie widzi nowego PATH.

## Podpowiedź 3
Polecenie diagnostyczne ma w nazwie „lekarza”.

## Rozwiązanie
PowerShell → install.ps1. „not recognized” tuż po instalacji to zwykle stare okno — otwórz nowe; jeśli dalej — dopisz %USERPROFILE%\.local\bin do PATH. Diagnostyka: claude doctor.

## Oczekiwany wynik
(1) ps1 (PowerShell); (2) najpierw nowe okno terminala (PATH), dopiero potem poprawka PATH z dokumentacji; (3) `claude doctor`.

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co się zmieni, gdy zmienisz jedną daną (granicę, typ, plik)?
