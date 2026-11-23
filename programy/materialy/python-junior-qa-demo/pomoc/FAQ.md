# FAQ — najczęstsze pytania

**„✔ Sprawdź wynik” mówi „Brak pliku …”.** Plik musi leżeć bezpośrednio w katalogu PRACA i mieć dokładnie tę nazwę (włącz widoczne rozszerzenia — `plik.py.txt` to nie `plik.py`).

**„W pliku brakuje funkcji …”.** Nazwy funkcji i parametrów są częścią specyfikacji — skopiuj je dosłownie z zadania.

**Testy „wiszą” albo kończą się po czasie.** W pliku jest `input()` poza blokiem `if __name__ == "__main__":` — test czeka na klawiaturę.

**„pytest nie jest dostępny w środowisku kursu”.** Środowisko → „⬇ Zainstaluj brakujące” → „✔ Sprawdź działanie”.

**Nie mam płatnego planu AI.** Nie jest potrzebny — Asystent Offline w Mentorze, lekcje i podpowiedzi wystarczą.

**Selenium: „Unable to obtain driver”.** Pierwsze uruchomienie wymaga internetu (Selenium Manager pobiera sterownik Edge/Chrome); potem działa z pamięci podręcznej.

**Sklep testowy nie odpowiada (ERR_CONNECTION_REFUSED).** W osobnym oknie terminala Mentora: `cd projekty\sklep_testowy` → `python app.py`.

**Testy Git mówią „Nie znaleziono programu git”.** Zainstaluj Git for Windows (git-scm.com albo `winget install --id Git.Git -e`) i uruchom Mentora ponownie.

**Asystent proponuje zmienić testy z WERYFIKATORY.** Odmów. Te testy są kopiowane przez Mentora z paczki i sprawdzane sumą SHA-256 — zmiana w Twoim folderze nic nie da, a zasada „nie zmieniaj testów” jest częścią kursu.

**Czy mogę pisać w PyCharm albo VS Code?** Tak — pliki zapisuj w katalogu PRACA i wskaż interpreter środowiska kursu (ścieżka w Mentorze → Środowisko).
