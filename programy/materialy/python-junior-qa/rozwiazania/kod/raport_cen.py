import csv
from datetime import date

from api import pobierz_produkty


def zapisz_raport(produkty, sciezka, data):
    """Raport CSV (data, nazwa, kategoria, cena) malejąco po cenie; zwraca liczbę wierszy."""
    wiersze = sorted(produkty, key=lambda p: p["cena"], reverse=True)
    with open(sciezka, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["data", "nazwa", "kategoria", "cena"])
        for p in wiersze:
            w.writerow([data, p["nazwa"], p["kategoria"], p["cena"]])
    return len(wiersze)


def ostrzezenia(produkty, prog=10):
    """Nazwy produktów z ilością poniżej progu, alfabetycznie."""
    return sorted(p["nazwa"] for p in produkty if p["ilosc"] < prog)


if __name__ == "__main__":
    try:
        produkty = pobierz_produkty("http://127.0.0.1:5001/api/produkty")
    except RuntimeError as e:
        print("Błąd:", e)
    else:
        n = zapisz_raport(produkty, "raport_cen.csv", date.today().isoformat())
        print(f"Zapisano {n} produktów do raport_cen.csv")
        print("Kończy się:", ostrzezenia(produkty))
