import csv
import io

DANE = """id,nazwa,kategoria,cena,ilosc
1,Zeszyt A5 w kratkę,zeszyty,4.50,120
3,Długopis niebieski,pisaki,2.30,300
9,"Papier ksero A4, 500 ark.",papier,24.99,35
17,Zszywki 1000 szt.,biuro,3.90,0
"""
wiersze = list(csv.DictReader(io.StringIO(DANE)))
print("Produktów:", len(wiersze), "| pierwszy:", wiersze[0]["nazwa"])
ceny = [float(w["cena"]) for w in wiersze]
print(f"Średnia cena: {sum(ceny) / len(ceny):.2f}")
najdrozszy = max(wiersze, key=lambda w: float(w["cena"]))
print("Najdroższy:", najdrozszy["nazwa"])
brak = [w["nazwa"] for w in wiersze if int(w["ilosc"]) == 0]
print("Brak na stanie:", brak)
wartosc = sum(float(w["cena"]) * int(w["ilosc"]) for w in wiersze)
print(f"Wartość magazynu: {wartosc:.2f} zł")
wyjscie = io.StringIO()
pisarz = csv.DictWriter(wyjscie, fieldnames=["nazwa", "wartosc"], lineterminator="\n")
pisarz.writeheader()
pisarz.writerow({"nazwa": "Zeszyt A5 w kratkę", "wartosc": 540.0})
print(wyjscie.getvalue(), end="")
