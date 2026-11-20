# debug_rezerwacje.py — import rezerwacji z linii tekstu (kod od AI, 3 błędy)
from datetime import datetime


def parsuj_linie(linia):
    """'Anna;Lipowy;20.12.2026;23.12.2026' → słownik z datami (date)."""
    czesci = [c.strip() for c in linia.strip().split(";")]
    if len(czesci) != 4:
        raise ValueError(f"zła linia: {linia!r}")
    gosc, pokoj, od, do = czesci
    return {"gosc": gosc, "pokoj": pokoj, "od": datetime.strptime(od, "%m.%d.%Y").date(), "do": datetime.strptime(do, "%m.%d.%Y").date()}


def wczytaj_rezerwacje(linie, wynik=[]):
    """Lista rezerwacji z linii tekstu; puste linie pomija."""
    for linia in linie:
        if linia.strip():
            wynik.append(parsuj_linie(linia))
    return wynik


def noce_razem(rezerwacje):
    """Suma nocy we wszystkich rezerwacjach."""
    return sum((r["do"] - r["od"]).days + 1 for r in rezerwacje)
