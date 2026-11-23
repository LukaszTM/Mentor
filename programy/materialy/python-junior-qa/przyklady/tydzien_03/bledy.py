def wydaj(stan, ilosc):
    """Zwraca nowy stan po wydaniu towaru; zła ilość → ValueError."""
    if ilosc <= 0:
        raise ValueError("ilość musi być dodatnia")
    if ilosc > stan:
        raise ValueError(f"brak towaru: na stanie {stan}")
    return stan - ilosc


for wpis in ["5", "dwa", "0", "200"]:
    try:
        ilosc = int(wpis)
        nowy = wydaj(120, ilosc)
    except ValueError as e:
        print(f"{wpis!r}: błąd — {e}")
    else:
        print(f"{wpis!r}: wydano, zostało {nowy}")
    finally:
        print("---")
