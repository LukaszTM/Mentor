nazwa = "Długopis niebieski"
cena = 2.3
ilosc = 4
print("Produkt:", nazwa)
print("Cena", "Ilość", "Razem", sep=" | ")
print(cena, ilosc, cena * ilosc, sep=" | ")
print("Wczytuję", end="")
print("...", end="")
print(" gotowe")
print(f"{nazwa}: {ilosc} szt. × {cena:.2f} zł = {cena * ilosc:.2f} zł")
