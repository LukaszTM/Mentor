# Pod Lipą — mini system rezerwacji

## Opis
Projekt szkoleniowy (dane fikcyjne) dla agroturystyki „Pod Lipą”: kalkulator ceny, kalendarz pokoi i API rezerwacji we Flask.

## Funkcje
- API rezerwacji z walidacją (201/400/409)
- lista rezerwacji bez danych kontaktowych
- wolne pokoje w wybranych datach

## Wymagania
- Windows 10/11, Python 3.12, Git

## Instalacja
```
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Uruchomienie
```
set FLASK_SECRET_KEY=wygeneruj_losowa_wartosc
flask --app system run
```
Otwórz http://127.0.0.1:5000

## Testy
```
python -m pytest -q
```

## Konfiguracja
- FLASK_SECRET_KEY — losowa wartość: python -c "import secrets; print(secrets.token_hex(32))"
- POGODA_API_KEY — klucz do API pogody (tylko pogoda.py)

## Ograniczenia
- baza w pamięci w testach; brak logowania właścicielki; brak płatności online

## Jak powstał
Kod powstał z pomocą agentów AI na podstawie moich specyfikacji; każdą zmianę przejrzałem i przetestowałem.

## Licencja
MIT — zobacz plik LICENSE.
