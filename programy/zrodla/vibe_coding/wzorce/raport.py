"""Raport z pliku rezerwacji (CSV z polskiego arkusza)."""
import csv
import json
from collections import Counter


def _liczba(tekst):
    return float(tekst.replace(" ", "").replace(" ", "").replace(",", "."))


def wczytaj(sciezka):
    """Lista rezerwacji; puste wiersze pomija, zły wiersz → ValueError z numerem wiersza."""
    wynik = []
    with open(sciezka, encoding="utf-8-sig", newline="") as f:
        for nr, w in enumerate(csv.DictReader(f, delimiter=";"), start=2):
            if not any((v or "").strip() for v in w.values()):
                continue
            try:
                wynik.append({"data_przyjazdu": w["data_przyjazdu"].strip(), "pokoj": w["pokoj"].strip(), "noce": int(w["noce"]),
                              "osoby": int(w["osoby"]), "kwota": _liczba(w["kwota"])})
            except (KeyError, ValueError, AttributeError) as e:
                raise ValueError(f"wiersz {nr}: {e}") from None
    return wynik


def przychod_miesieczny(rezerwacje):
    """{'RRRR-MM': suma} zaokrąglone do groszy."""
    sumy = {}
    for r in rezerwacje:
        m = r["data_przyjazdu"][:7]
        sumy[m] = sumy.get(m, 0) + r["kwota"]
    return {m: round(s, 2) for m, s in sumy.items()}


def najczestszy_pokoj(rezerwacje):
    """Pokój z największą liczbą rezerwacji; remis — alfabetycznie pierwszy; brak — None."""
    if not rezerwacje:
        return None
    licz = Counter(r["pokoj"] for r in rezerwacje)
    return sorted(licz.items(), key=lambda p: (-p[1], p[0]))[0][0]


def zapisz_json(dane, sciezka):
    with open(sciezka, "w", encoding="utf-8") as f:
        json.dump(dane, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    rez = wczytaj("dane/rezerwacje.csv")
    print(len(rez), przychod_miesieczny(rez), najczestszy_pokoj(rez))
