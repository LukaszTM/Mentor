zdanie = "  Ala ma kota i psa  "
czyste = zdanie.strip()
print(czyste.upper())
print(czyste[::-1])
print(len(czyste), "znaków")
slowa = czyste.split()
print(len(slowa), "słów:", ", ".join(slowa))
samogloski = 0
for znak in czyste.lower():
    if znak in "aąeęioóuy":
        samogloski += 1
print("Samogłoski:", samogloski)
najdluzsze = max(slowa, key=len)
print("Najdłuższe:", najdluzsze)
print("4,50 zł".replace(",", "."), "Długopis".lower().startswith("dług"))
