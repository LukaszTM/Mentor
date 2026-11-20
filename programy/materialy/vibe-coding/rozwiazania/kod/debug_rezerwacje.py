"""Import rezerwacji z linii tekstu — wersja poprawiona."""
from datetime import datetime


def parsuj_linie(linia):
    """'Anna;Lipowy;20.12.2026;23.12.2026' → słownik z datami (date)."""
    czesci = [c.strip() for c in linia.strip().split(";")]
    if len(czesci) != 4:
        raise ValueError(f"zła linia: {linia!r}")
    gosc, pokoj, od, do = czesci
    return {"gosc": gosc, "pokoj": pokoj, "od": datetime.strptime(od, "%d.%m.%Y").date(), "do": datetime.strptime(do, "%d.%m.%Y").date()}


def wczytaj_rezerwacje(linie, wynik=None):
    """Lista rezerwacji z linii tekstu; puste linie pomija."""
    if wynik is None:
        wynik = []
    for linia in linie:
        if linia.strip():
            wynik.append(parsuj_linie(linia))
    return wynik


def noce_razem(rezerwacje):
    """Suma nocy we wszystkich rezerwacjach."""
    return sum((r["do"] - r["od"]).days for r in rezerwacje)
