def pole_prostokata(a, b):
    """Zwraca pole prostokąta o bokach a i b."""
    return a * b


def czy_parzysta(n):
    """True, gdy liczba całkowita n jest parzysta."""
    return n % 2 == 0


def maksimum(lista):
    """Największy element listy (bez max()); pusta lista → ValueError."""
    if not lista:
        raise ValueError("lista jest pusta")
    najwieksza = lista[0]
    for x in lista:
        if x > najwieksza:
            najwieksza = x
    return najwieksza


def odwroc(napis):
    """Zwraca napis od tyłu."""
    return napis[::-1]


def silnia(n):
    """n! dla n ≥ 0; liczba ujemna → ValueError."""
    if n < 0:
        raise ValueError("silnia liczby ujemnej nie istnieje")
    wynik = 1
    for i in range(2, n + 1):
        wynik *= i
    return wynik


if __name__ == "__main__":
    print(pole_prostokata(3, 4), czy_parzysta(7), maksimum([3, 9, 2]), odwroc("kot"), silnia(5))
