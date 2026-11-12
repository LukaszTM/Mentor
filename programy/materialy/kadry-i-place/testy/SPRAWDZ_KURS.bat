@echo off
chcp 65001 >nul
set "TU=%~dp0.."
echo Sprawdzanie paczki kursu w "%TU%"
set B=0
for %%F in (START_TUTAJ.md manifest.json kurs_mentor.json) do (if exist "%TU%\%%F" (echo [OK] %%F) else (echo [BRAK] %%F & set B=1))
for %%D in (lekcje przyklady cwiczenia rozwiazania pomoc projekty testy) do (if exist "%TU%\%%D" (echo [OK] %%D\) else (echo [BRAK] %%D\ & set B=1))
for /f %%n in ('dir /b /s "%TU%\cwiczenia\*.md" 2^>nul ^| find /c ".md"') do echo Plikow cwiczen: %%n (oczekiwane: 90)
for /f %%n in ('dir /b /s "%TU%\rozwiazania\*.md" 2^>nul ^| find /c ".md"') do echo Plikow rozwiazan: %%n (oczekiwane: 90)
where python >nul 2>nul && (python "%TU%\testy\sprawdz_kurs.py") || echo (Python niedostepny - pominieto sprawdzenie sum kontrolnych; to nie jest wymagane do nauki)
if %B%==0 (echo WYNIK: struktura paczki kompletna.) else (echo WYNIK: brakuje plikow - rozpakuj ZIP ponownie.)
pause
