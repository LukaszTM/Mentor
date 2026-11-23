nazwa = "Zeszyt A5 w kratkę"
cena = 4.50
ilosc = 3
dostepny = True

razem = cena * ilosc
print(nazwa, type(nazwa))
print(cena, type(cena))
print(ilosc, type(ilosc))
print(dostepny, type(dostepny))
print(f"Do zapłaty: {razem:.2f} zł")
print("Paczki po 4 szt.:", 10 // 4, "reszta:", 10 % 4)
