# FAQ — najczęstsze pytania

**„✔ Sprawdź wynik” mówi „Brak pliku …”.** Plik musi leżeć bezpośrednio w katalogu PRACA i mieć dokładnie tę nazwę (włącz widoczne rozszerzenia — `plik.py.txt` to nie `plik.py`).

**„W pliku brakuje funkcji …”.** Nazwy funkcji i parametrów są częścią specyfikacji — skopiuj je dosłownie z zadania.

**Testy „wiszą” albo kończą się po czasie.** W pliku jest `input()` poza blokiem `if __name__ == "__main__":` — test czeka na klawiaturę.

**„pytest nie jest dostępny w środowisku kursu”.** Środowisko → „⬇ Zainstaluj brakujące” → „✔ Sprawdź działanie”.

**Nie mam płatnego planu.** Każde zadanie z agentem ma plik `przyklady/odpowiedzi_agenta/<id>.md` — zapis pracy agenta z jednym błędem. Ta sama umiejętność: czytasz, sprawdzasz, poprawiasz.

**Testy Git (tydzień 6+) mówią „Nie znaleziono programu git”.** Zainstaluj Git for Windows (`winget install --id Git.Git -e --source winget`) i uruchom Mentora ponownie.

**Agent chce zmienić testy z WERYFIKATORY.** Odmów. Te testy są kopiowane przez Mentora z paczki i sprawdzane sumą SHA-256 — zmiana w Twoim folderze nic nie da, a zasada „nie zmieniaj testów” jest częścią kursu.

**Czy mogę używać innego agenta (Cursor, Copilot, Gemini…)?** Tak — specyfikacje, testy i przegląd działają tak samo. Lekcje pokazują Claude Code i Codex.
