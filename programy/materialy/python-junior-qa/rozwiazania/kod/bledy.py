def na_liczbe(tekst):
    """Zamienia napis na float (przyjmuje przecinek); zły napis → ValueError."""
    return float(tekst.strip().replace(",", "."))


def wczytaj_liczbe(komunikat):
    while True:
        try:
            return na_liczbe(input(komunikat))
        except ValueError:
            print("To nie liczba — spróbuj jeszcze raz")


if __name__ == "__main__":
    a = wczytaj_liczbe("Pierwsza liczba: ")
    b = wczytaj_liczbe("Druga liczba: ")
    try:
        print("a / b =", a / b)
    except ZeroDivisionError:
        print("Nie dzielimy przez zero")
