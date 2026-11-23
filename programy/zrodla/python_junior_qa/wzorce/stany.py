def dodaj(stany, nazwa, ilosc):
    """Dodaje ilość produktu (nowy albo istniejący); ilość ≤ 0 → ValueError."""
    if ilosc <= 0:
        raise ValueError("ilość musi być dodatnia")
    stany[nazwa] = stany.get(nazwa, 0) + ilosc


def usun(stany, nazwa):
    """Usuwa produkt; brak produktu → ValueError."""
    if nazwa not in stany:
        raise ValueError(f"nie ma produktu {nazwa}")
    del stany[nazwa]


def posortowane(stany):
    """Lista par (nazwa, ilość) rosnąco po ilości, przy remisie alfabetycznie."""
    return sorted(stany.items(), key=lambda p: (p[1], p[0]))


def razem(stany):
    """Suma sztuk wszystkich produktów."""
    return sum(stany.values())


if __name__ == "__main__":
    s = {}
    dodaj(s, "zeszyt", 120)
    dodaj(s, "klej", 30)
    for nazwa, ilosc in posortowane(s):
        print(f"{nazwa:<10}{ilosc:>5}")
    print("Razem:", razem(s))
