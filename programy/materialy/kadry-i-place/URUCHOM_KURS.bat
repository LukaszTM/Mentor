@echo off
chcp 65001 >nul
title Mentor - Kadry i place
set "TU=%~dp0"
cd /d "%TU%"
if exist "%TU%Mentor.exe" (
    start "" "%TU%Mentor.exe"
    exit /b 0
)
if exist "%TU%mentor.py" (
    where python >nul 2>nul
    if errorlevel 1 (
        echo Nie znaleziono Mentor.exe ani Pythona. Rozpakuj caly ZIP albo zainstaluj Pythona 3.12 z https://www.python.org/downloads/windows/
        pause
        exit /b 1
    )
    python "%TU%mentor.py"
    exit /b %errorlevel%
)
echo Nie znaleziono Mentor.exe w folderze "%TU%". Rozpakuj caly ZIP do jednego folderu.
pause
exit /b 1
