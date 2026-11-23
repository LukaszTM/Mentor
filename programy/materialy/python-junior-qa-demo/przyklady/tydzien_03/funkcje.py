def brutto(netto, vat=23):
    """Zwraca cenę brutto (2 miejsca po przecinku) z ceny netto i stawki VAT w %."""
    return round(netto * (1 + vat / 100), 2)


def czy_parzysta(n):
    """True, gdy n jest parzyste."""
    return n % 2 == 0


def wypisz_brutto(netto):
    print("Brutto:", brutto(netto))


if __name__ == "__main__":
    print(brutto(10), brutto(10, 8), brutto(netto=100, vat=5))
    print(czy_parzysta(4), czy_parzysta(7))
    wynik = wypisz_brutto(20)
    print("Funkcja bez return zwraca:", wynik)
