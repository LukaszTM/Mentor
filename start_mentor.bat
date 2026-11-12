@echo off
chcp 65001 >nul
cd /d "%~dp0"
where pythonw >nul 2>nul
if %errorlevel%==0 (
    start "" pythonw mentor.py
) else (
    where python >nul 2>nul
    if %errorlevel%==0 (
        python mentor.py
    ) else (
        echo Nie znaleziono Pythona. Zainstaluj go z https://www.python.org/downloads/
        echo i zaznacz "Add Python to PATH" podczas instalacji.
        pause
    )
)
