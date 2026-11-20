# Odzyskiwanie — gdy coś poszło nie tak

- **Agent popsuł plik, bez commita:** `git diff plik.py` (zobacz, co tracisz) → `git restore plik.py`. W Claude Code także Esc Esc / `/rewind`.
- **Zły commit:** `git revert HEAD` (nowy commit odwracający — bezpieczne).
- **Klucz API trafił do repozytorium:** unieważnij klucz w panelu usługi NATYCHMIAST, wygeneruj nowy, ustaw w zmiennej środowiskowej; usunięcie pliku nie usuwa go z historii.
- **Skrypt porządkujący przeniósł pliki:** log `.porzadki.log` w folderze mówi, skąd dokąd — przenieś z powrotem.
- **Zepsute środowisko Pythona:** Mentor → Środowisko → „Napraw środowisko”.
- **Zagubione materiały kursu:** Mój projekt → „📂 Skopiuj materiały kursu tutaj” (nie nadpisuje Twoich plików) albo rozpakuj ZIP kursu ponownie.
- **Postępy w Mentorze:** zapisane w `mentor_dane.json` w katalogu danych Mentora (`%LOCALAPPDATA%\Mentor\`; w trybie przenośnym — obok Mentor.exe) — skopiuj go jako kopię zapasową.
