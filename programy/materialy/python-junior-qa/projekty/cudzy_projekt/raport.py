def raport_miesieczny(wypozyczenia, rok, miesiac):
    """Słownik sprzęt → liczba wypożyczeń w danym miesiącu (data w formacie DD.MM.RRRR)."""
    wynik = {}
    for w in wypozyczenia:
        d, m, r = w["data"].split(".")
        if int(r) == rok and int(m) == miesiac:
            wynik[w["sprzet"]] = wynik.get(w["sprzet"], 0) + 1
    return wynik
