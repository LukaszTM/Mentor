import csv

POLA = ["id", "nazwa", "kategoria", "cena", "ilosc"]


def wczytaj(sciezka):
    """Produkty z CSV (id, ilosc → int; cena → float)."""
    with open(sciezka, encoding="utf-8", newline="") as f:
        wiersze = list(csv.DictReader(f))
    return [{"id": int(w["id"]), "nazwa": w["nazwa"], "kategoria": w["kategoria"], "cena": float(w["cena"]), "ilosc": int(w["ilosc"])} for w in wiersze]


def zapisz(produkty, sciezka):
    with open(sciezka, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=POLA)
        w.writeheader()
        w.writerows(produkty)


def dodaj(produkty, nazwa, kategoria, cena, ilosc):
    """Dodaje produkt z walidacją: niepusta, unikalna nazwa (bez wielkości liter), cena ≥ 0, ilość całkowita ≥ 0."""
    nazwa = nazwa.strip()
    if not nazwa:
        raise ValueError("nazwa nie może być pusta")
    if any(p["nazwa"].lower() == nazwa.lower() for p in produkty):
        raise ValueError(f"produkt {nazwa} już istnieje")
    if cena < 0:
        raise ValueError("cena nie może być ujemna")
    if not isinstance(ilosc, int) or ilosc < 0:
        raise ValueError("ilość musi być liczbą całkowitą ≥ 0")
    nowy = {"id": max((p["id"] for p in produkty), default=0) + 1, "nazwa": nazwa, "kategoria": kategoria, "cena": float(cena), "ilosc": ilosc}
    produkty.append(nowy)
    return nowy


def statystyki(produkty):
    if not produkty:
        return {"liczba": 0, "srednia_cena": 0, "najdrozszy": None, "wartosc": 0}
    return {"liczba": len(produkty),
            "srednia_cena": round(sum(p["cena"] for p in produkty) / len(produkty), 2),
            "najdrozszy": max(produkty, key=lambda p: p["cena"])["nazwa"],
            "wartosc": round(sum(p["cena"] * p["ilosc"] for p in produkty), 2)}


def szukaj(produkty, fraza):
    """Produkty, których nazwa albo kategoria zawiera frazę (bez wielkości liter)."""
    f = fraza.strip().lower()
    return [p for p in produkty if f in p["nazwa"].lower() or f in p["kategoria"].lower()]


if __name__ == "__main__":
    p = wczytaj("dane/produkty.csv")
    print(statystyki(p))
    for x in szukaj(p, input("Szukaj: ")):
        print(x["id"], x["nazwa"], x["cena"])
