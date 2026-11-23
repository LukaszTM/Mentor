# Odzyskiwanie zmian w Gicie

## git restore
Używam, gdy zepsułam plik i nie zrobiłam jeszcze commita. Polecenie git restore csv_odczyt.py przywraca plik do stanu z ostatniego commita, a moje niezapisane zmiany przepadają, więc najpierw patrzę w git diff.

## git stash
Używam, gdy muszę na chwilę przełączyć gałąź, a zmiany nie są gotowe do commita. git stash odkłada je na półkę i czyści katalog, a git stash pop przywraca je z powrotem na bieżącej gałęzi.

## git revert
Używam, gdy zły commit jest już wysłany na GitHub i inni mogli go pobrać. git revert z identyfikatorem commita tworzy nowy commit odwracający zmiany, nie przepisuje historii i jest bezpieczny dla zespołu.
