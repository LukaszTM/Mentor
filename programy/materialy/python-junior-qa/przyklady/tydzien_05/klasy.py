class Produkt:
    def __init__(self, nazwa, cena, ilosc=0):
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


zeszyt = Produkt("Zeszyt A5", 4.5, 120)
klej = Produkt("Klej w sztyfcie", 3.4)
klej.przyjmij(50)
zeszyt.wydaj(20)
for p in [zeszyt, klej]:
    print(p, "| wartość:", p.wartosc())
try:
    klej.wydaj(80)
except ValueError as e:
    print("Błąd:", e)
