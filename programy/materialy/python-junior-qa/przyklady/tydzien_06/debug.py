def srednia_ceny(ceny):
    suma = 0
    for i in range(1, len(ceny)):
        suma += ceny[i]
    return suma / len(ceny)


def srednia_ceny_poprawiona(ceny):
    if not ceny:
        return 0
    suma = 0
    for cena in ceny:
        suma += cena
    return suma / len(ceny)


ceny = [4.0, 2.0, 6.0]
print("Oczekiwane 4.0, otrzymane:", srednia_ceny(ceny))
for i in range(1, len(ceny)):
    print("DEBUG i =", i, "cena =", repr(ceny[i]))
print("Po poprawce:", srednia_ceny_poprawiona(ceny), srednia_ceny_poprawiona([]))
