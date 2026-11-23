nazwa = "Zeszyt A5 w kratkę"
cena = 4.50
ilosc = 120
dostepny = True
kategoria = "zeszyty"

print(nazwa, type(nazwa))
print(cena, type(cena))
print(ilosc, type(ilosc))
print(dostepny, type(dostepny))
print(kategoria, type(kategoria))
print(f"Wartość na stanie: {cena * ilosc:.2f} zł")
