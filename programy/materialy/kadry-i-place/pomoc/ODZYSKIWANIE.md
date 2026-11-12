# Odzyskiwanie, reset, aktualizacja

## Kopia zapasowa i przywrócenie postępów
- Postępy: `mentor_dane.json` obok `Mentor.exe` (lub obok `mentor.py`). Skopiuj go w bezpieczne miejsce (np. raz w tygodniu).
- Przywrócenie: zamknij Mentora, wklej zapisany `mentor_dane.json`, uruchom ponownie.
- Twoje pliki (FIRMA.md, listy płac, pisma) są w katalogu projektu — to zwykłe pliki; kopiuj cały folder.

## Reset
- Jedno ćwiczenie: usuń plik z `cwiczenia/tydzien_NN/` i uruchom INSTALACJA.bat (lub Mój projekt → Skopiuj materiały) — skopiuje tylko brakujące.
- Postępy programu: Ustawienia → eksport postępów (kopia), potem usuń `mentor_dane.json` → Mentor startuje od zera (dla wszystkich programów!).
- Symulator ZUS: Warsztat → eZUS/Płatnik → „Wyczyść wszystkie zgłoszenia (zacznij od nowa)”; lista płac miesiąca: „Wyczyść listę miesiąca”.

## Aktualizacja kursu / Mentora
- Nowa wersja ZIP: rozpakuj do NOWEGO folderu, skopiuj do niego `mentor_dane.json` ze starego. Id zadań i lekcji są stałe — postępy pasują.
- Import nowej wersji kursu plikiem (Ustawienia → Wgraj program z pliku) nie usuwa postępów; stary plik kursu możesz usunąć z `programy/`.

## Odinstalowanie
- Mentor nie instaluje się w systemie: usuń folder paczki. Katalog projektu i kopia `mentor_dane.json` zostają, jeśli chcesz.

## Typowe problemy techniczne
- „Windows chronił komputer” przy Mentor.exe → „Więcej informacji” → „Uruchom mimo to” (plik bez podpisu certyfikatem).
- Antywirus blokuje exe → dodaj folder do wyjątków albo uruchom ze źródeł (`python mentor.py`, Python 3.12 z python.org).
- Okno za duże/za małe → Ustawienia → Czcionki/skala.
- Polskie znaki w ścieżce lub spacje — obsługiwane; nie uruchamiaj z wnętrza ZIP.
- Brak uprawnień do zapisu w folderze (np. Program Files) → przenieś folder do Dokumentów.
