@echo off
chcp 65001 >nul
set CEL=%USERPROFILE%\Documents\Mentor\vibe-coding\PRACA
echo Kopiuje materialy kursu do: %CEL%  (istniejace pliki NIE beda nadpisane)
if not exist "%CEL%" mkdir "%CEL%"
robocopy "%~dp0." "%CEL%" /E /XC /XN /XO /XF *.bat /XD testy /NFL /NDL /NJH /NJS >nul
echo Gotowe. Otworz Mentora: Moj projekt -> wskaz ten katalog.
pause
