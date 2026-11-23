# Odzyskiwanie — gdy coś poszło nie tak

- **Zepsuty plik, bez commita:** `git diff plik.py` (zobacz, co tracisz) → `git restore plik.py`.
- **Zły commit:** `git revert HEAD` (nowy commit odwracający — bezpieczne).
- **Klucz API trafił do repozytorium:** unieważnij klucz w panelu usługi NATYCHMIAST, wygeneruj nowy, ustaw w zmiennej środowiskowej; usunięcie pliku nie usuwa go z historii.
- **Testy zapisały coś do Twoich danych:** w testach zawsze `tmp_path`; dane odtworzysz z `dane/produkty.csv` paczki.
- **Zepsute środowisko Pythona:** Mentor → Środowisko → „Napraw środowisko”.
- **Zagubione materiały kursu:** Mój projekt → „📂 Skopiuj materiały kursu tutaj” (nie nadpisuje Twoich plików) albo rozpakuj ZIP kursu ponownie.
- **Postępy w Mentorze:** zapisane w `mentor_dane.json` w katalogu danych Mentora (`%LOCALAPPDATA%\Mentor\`; w trybie przenośnym — obok Mentor.exe) — skopiuj go jako kopię zapasową.
