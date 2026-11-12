@echo off
chcp 65001 >nul
setlocal EnableDelayedExpansion
title Mentor - instalacja materialow kursu (z potwierdzeniem)
set "TU=%~dp0"
set "MAT=%TU%programy\materialy\kadry-i-place"
if not exist "%MAT%\START_TUTAJ.md" set "MAT=%TU%"
set "CEL=%USERPROFILE%\Documents\kadry-praktyka"
echo ================================================================
echo  MENTOR - KADRY I PLACE: instalacja materialow kursu
echo ================================================================
echo.
echo Ten skrypt NIE instaluje zadnych programow (Mentor dziala bez instalacji).
echo Zrobi tylko jedno: skopiuje materialy kursu do Twojego katalogu projektu.
echo.
echo   Zrodlo:  "%MAT%"
echo   Cel:     "%CEL%"
echo.
echo Istniejace pliki o tej samej nazwie NIE zostana nadpisane (Twoja praca jest bezpieczna).
echo Mozesz tez zrobic to samo w Mentorze: Moj projekt - "Skopiuj materialy kursu tutaj".
echo.
set /p ODP="Kontynuowac? [T/N] "
if /i not "%ODP%"=="T" (echo Przerwano - nic nie zmieniono. & pause & exit /b 0)
set /p INNY="Inny katalog docelowy? Wpisz sciezke albo ENTER, zeby uzyc domyslnego: "
if not "%INNY%"=="" set "CEL=%INNY%"
if not exist "%CEL%" (
    mkdir "%CEL%" 2>nul
    if not exist "%CEL%" (echo BLAD: nie mozna utworzyc "%CEL%" - brak uprawnien lub zla sciezka. & pause & exit /b 1)
)
set N=0
for %%D in (lekcje przyklady cwiczenia rozwiazania pomoc projekty testy) do (
    if exist "%MAT%\%%D" (
        xcopy "%MAT%\%%D" "%CEL%\%%D\" /E /I /Q /Y /D >nul 2>nul
        rem /D kopiuje tylko nowsze; dodatkowo nie nadpisujemy zmienionych przez ucznia: robocopy z /XO /XN /XC
        robocopy "%MAT%\%%D" "%CEL%\%%D" /E /XO /XN /XC /NFL /NDL /NJH /NJS /NC /NS /NP >nul 2>nul
        set /a N+=1
    )
)
if exist "%MAT%\START_TUTAJ.md" if not exist "%CEL%\START_TUTAJ.md" copy "%MAT%\START_TUTAJ.md" "%CEL%\" >nul
if not exist "%CEL%\dziennik.md" (
    echo # Dziennik nauki - kadry i place> "%CEL%\dziennik.md"
    echo.>> "%CEL%\dziennik.md"
    echo Dzien 1: >> "%CEL%\dziennik.md"
)
echo.
echo Gotowe. Skopiowano %N% katalogow do "%CEL%".
echo W Mentorze: Ustawienia (lub Moj projekt) - "Wybierz katalog..." - wskaz ten folder.
echo Wycofanie: usun folder "%CEL%" (paczka zostaje nietknieta). Reset jednego cwiczenia: skasuj jego plik i uruchom ten skrypt ponownie.
echo.
pause
