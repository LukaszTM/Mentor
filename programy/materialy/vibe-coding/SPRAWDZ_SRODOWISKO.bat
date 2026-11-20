@echo off
chcp 65001 >nul
echo === Sprawdzenie srodowiska kursu Vibe coding (niczego nie zmienia) ===
where python >nul 2>nul && (python --version) || echo [!] Python: brak w PATH - Mentor zainstaluje srodowisko kursu sam (zakladka Srodowisko).
where git >nul 2>nul && (git --version) || echo [i] Git: brak - potrzebny od tygodnia 6.
where claude >nul 2>nul && (claude --version) || echo [i] Claude Code: brak - instalacja w tygodniu 4 (opcjonalnie, albo Codex).
where codex >nul 2>nul && (codex --version) || echo [i] Codex: brak - instalacja w tygodniu 4 (opcjonalnie, albo Claude Code).
where node >nul 2>nul && (node --version) || echo [i] Node.js: brak - opcjonalny (test JavaScript w tygodniu 9).
echo.
pause
