@echo off
chcp 65001 >nul
echo === Sprawdzenie srodowiska kursu Python Junior QA (niczego nie zmienia) ===
where python >nul 2>nul && (python --version) || echo [!] Python: brak w PATH - Mentor zainstaluje srodowisko kursu sam (zakladka Srodowisko).
where git >nul 2>nul && (git --version) || echo [!] Git: brak - potrzebny od tygodnia 0 (git-scm.com, lekcja Narzedzia).
where claude >nul 2>nul && (claude --version) || echo [i] Claude Code: brak - opcjonalny.
if exist "%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe" (echo Edge: jest) else (echo [i] Edge: nie znaleziono - Selenium od tygodnia 8 moze uzyc Chrome.)
echo.
pause
