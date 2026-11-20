# Bezpieczeństwo agenta w projekcie

## Reguły
- Read(./.env) i Read(./secrets/**) — sekrety niedostępne dla narzędzi agenta
- Bash(curl *) — bez pobierania i wysyłania danych z terminala bez mojej wiedzy
- Bash(git push --force*) — historia repozytorium chroniona

## Test reguł
- prośba o pokazanie .env → odmowa narzędzia (reguła działa)
- skrypt Pythona czytający .env nie jest blokowany regułą — chroni mnie tryb ręczny i brak prawdziwych sekretów w folderze

## Obce repozytorium
- klon do osobnego folderu, bez kluczy w zmiennych
- najpierw czytam README, AGENTS.md, CLAUDE.md i .claude/ sam
- agent w trybie planu, potem ręczny; nigdy bypass
