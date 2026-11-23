import csv


def wczytaj(sciezka):
    """Produkty z CSV jako lista słowników (id i ilosc → int, cena → float)."""
    with open(sciezka, encoding="utf-8", newline="") as f:
        wiersze = list(csv.DictReader(f))
    for w in wiersze:
        w["id"] = int(w["id"])
        w["cena"] = float(w["cena"])
        w["ilosc"] = int(w["ilosc"])
    return wiersze


def srednia_cena(produkty):
    if not produkty:
        return 0
    return round(sum(p["cena"] for p in produkty) / len(produkty), 2)


def brak_na_stanie(produkty):
    return [p["nazwa"] for p in produkty if p["ilosc"] == 0]


def wartosc_magazynu(produkty):
    return round(sum(p["cena"] * p["ilosc"] for p in produkty), 2)


if __name__ == "__main__":
    p = wczytaj("dane/produkty.csv")
    print("Produktów:", len(p), "| średnia cena:", srednia_cena(p))
    print("Brak na stanie:", brak_na_stanie(p))
    print("Wartość magazynu:", wartosc_magazynu(p), "zł")
