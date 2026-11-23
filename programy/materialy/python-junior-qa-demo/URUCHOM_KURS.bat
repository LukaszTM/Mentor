@echo off
chcp 65001 >nul
if exist "%~dp0..\Mentor.exe" (start "" "%~dp0..\Mentor.exe" & goto :eof)
if exist "%~dp0Mentor.exe" (start "" "%~dp0Mentor.exe" & goto :eof)
echo Nie znaleziono Mentor.exe obok paczki. Uruchom Mentora i wgraj kurs: Ustawienia - Program nauczania - Importuj kurs ZIP - plik ZIP kursu.
pause
