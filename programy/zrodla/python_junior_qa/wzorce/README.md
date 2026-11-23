# Nauka Pythona — od zera do Junior QA

Repozytorium z programami i projektami z kursu „Python od zera → Junior QA” (Mentor).

## Projekty

| projekt | co robi | technologie | link |
|---|---|---|---|
| kalkulator BMI | liczy BMI i kategorię z walidacją danych | Python | [bmi.py](bmi.py) |
| zgadnij liczbę | gra w zgadywanie z licznikiem prób | Python, random | [zgadnij.py](zgadnij.py) |
| menedżer zadań | lista zadań w konsoli, zapis do JSON | Python, json, moduły | [main.py](main.py) |
| raport cen | dane z API zapisane do CSV | Python, requests, csv | [raport_cen.py](raport_cen.py) |
| ewidencja magazynu | CSV z produktami, statystyki i wyszukiwanie | Python, csv | [magazyn_csv.py](magazyn_csv.py) |

## Jak uruchomić

```
git clone https://github.com/anna-nowak/nauka-python.git
cd nauka-python
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python bmi.py
```

## Jak testuję

Testy pytest w plikach `test_*.py`: `python -m pytest -v`.
