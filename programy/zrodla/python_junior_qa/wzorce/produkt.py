class Produkt:
    """Produkt w magazynie: nazwa, cena (zł), ilość (szt.)."""

    def __init__(self, nazwa, cena, ilosc=0):
        if cena < 0:
            raise ValueError("cena nie może być ujemna")
        self.nazwa = nazwa
        self.cena = cena
        self.ilosc = ilosc

    def wartosc(self):
        return round(self.cena * self.ilosc, 2)

    def przyjmij(self, n):
        if n <= 0:
            raise ValueError("ilość musi być dodatnia")
        self.ilosc += n

    def wydaj(self, n):
        if n <= 0 or n > self.ilosc:
            raise ValueError(f"nie można wydać {n} szt. (stan: {self.ilosc})")
        self.ilosc -= n

    def __str__(self):
        return f"{self.nazwa} — {self.cena:.2f} zł, {self.ilosc} szt."


if __name__ == "__main__":
    for p in [Produkt("Zeszyt A5", 4.5, 120), Produkt("Klej w sztyfcie", 3.4, 50), Produkt("Kredki", 12.9, 40)]:
        print(p, "| wartość:", p.wartosc())
