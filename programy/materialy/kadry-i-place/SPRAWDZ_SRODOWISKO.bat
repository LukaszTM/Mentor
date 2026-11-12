@echo off
chcp 65001 >nul
setlocal EnableDelayedExpansion
title Mentor - sprawdzenie srodowiska (nic nie zmienia)
echo ================================================================
echo  MENTOR - KADRY I PLACE: sprawdzenie srodowiska
echo  Ten skrypt tylko sprawdza i wypisuje. Niczego nie instaluje.
echo ================================================================
echo.
set "TU=%~dp0"
echo Folder paczki: "%TU%"
echo.
set BRAK=0
rem --- Windows
for /f "tokens=4-5 delims=. " %%i in ('ver') do set WER=%%i.%%j
echo [1] Windows: wersja %WER%  (wymagany Windows 10 lub 11)
rem --- Mentor.exe lub python
if exist "%TU%Mentor.exe" (
    echo [2] Mentor.exe: JEST
) else (
    if exist "%TU%mentor.py" (
        echo [2] Mentor.exe: brak, ale jest mentor.py - sprawdzam Pythona...
        where python >nul 2>nul
        if !errorlevel!==0 (
            for /f "tokens=2" %%v in ('python --version 2^>^&1') do echo     Python %%v  (wymagany 3.10 lub nowszy)
        ) else (
            echo     Python: NIE ZNALEZIONO. Pobierz oficjalnie: https://www.python.org/downloads/windows/  (wersja 3.12, zaznacz "Add python.exe to PATH")
            set BRAK=1
        )
    ) else (
        echo [2] Mentor.exe: BRAK - rozpakuj caly ZIP (nie uruchamiaj z wnetrza archiwum).
        set BRAK=1
    )
)
rem --- kurs
if exist "%TU%programy\kadry-i-place.json" (echo [3] Plik kursu programy\kadry-i-place.json: JEST) else (
    if exist "%TU%kurs_mentor.json" (echo [3] Plik kursu kurs_mentor.json: JEST ^(wgraj w Mentorze: Ustawienia - Wgraj program z pliku^)) else (echo [3] Plik kursu: BRAK & set BRAK=1))
rem --- materialy
set "MAT=%TU%programy\materialy\kadry-i-place"
if not exist "%MAT%\START_TUTAJ.md" set "MAT=%TU%"
if exist "%MAT%\cwiczenia" (echo [4] Materialy ^(cwiczenia, rozwiazania, pomoc^): JEST w "%MAT%") else (echo [4] Materialy: BRAK katalogu cwiczenia & set BRAK=1)
rem --- zapis w folderze
echo test > "%TU%_test_zapisu.tmp" 2>nul
if exist "%TU%_test_zapisu.tmp" (del "%TU%_test_zapisu.tmp" & echo [5] Zapis w folderze paczki: OK ^(Mentor zapisuje tu postepy: mentor_dane.json^)) else (
    echo [5] Zapis w folderze paczki: BRAK UPRAWNIEN - przenies folder np. do Dokumentow. & set BRAK=1)
rem --- miejsce na dysku
for /f "tokens=3" %%a in ('dir /-c "%TU%" ^| find "bajtów wolnych"') do set WOLNE=%%a
if not defined WOLNE for /f "tokens=3" %%a in ('dir /-c "%TU%" ^| find "bytes free"') do set WOLNE=%%a
if defined WOLNE (echo [6] Wolne miejsce na dysku: %WOLNE% bajtow ^(potrzeba ok. 100 MB^)) else (echo [6] Wolne miejsce: nie udalo sie odczytac - sprawdz w Eksploratorze ^(potrzeba ok. 100 MB^))
rem --- Dokumenty
if exist "%USERPROFILE%\Documents" (echo [7] Folder Dokumenty: "%USERPROFILE%\Documents" ^(tu INSTALACJA.bat zaproponuje katalog projektu^)) else (echo [7] Folder Dokumenty: nie znaleziono - katalog projektu wskazesz recznie w Mentorze)
rem --- internet (niewymagany)
echo [8] Internet: NIEWYMAGANY ^(kurs, Warsztat i Asystent offline dzialaja bez sieci^)
echo.
if %BRAK%==0 (
    echo WYNIK: srodowisko gotowe. Nastepny krok: URUCHOM_KURS.bat ^(albo Mentor.exe^), potem w Mentorze "Jak zaczac".
) else (
    echo WYNIK: czegos brakuje - patrz pozycje z napisem BRAK. Po poprawieniu uruchom ten skrypt ponownie.
)
echo.
pause
