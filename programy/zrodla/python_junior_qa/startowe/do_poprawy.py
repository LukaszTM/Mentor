"""Program z trzema błędami do znalezienia debuggerem. Nie zgaduj — odtwórz, zawęź, postaw hipotezę, sprawdź."""


def srednia_ceny(ceny):
    suma = 0
    for i in range(1, len(ceny)):
        suma += ceny[i]
    return suma / len(ceny)


def razem_koszyka(koszyk):
    suma = 0
    for cena, ilosc in koszyk:
        suma = cena * ilosc
    return suma


def kategoria_ceny(cena):
    if cena >= 10:
        return "średni"
    if cena >= 50:
        return "drogi"
    return "tani"


if __name__ == "__main__":
    print("Średnia (oczekiwane 4.0):", srednia_ceny([4.0, 2.0, 6.0]))
    print("Koszyk (oczekiwane 16.0):", razem_koszyka([(2.0, 3), (5.0, 2)]))
    print("Kategoria 75 zł (oczekiwane drogi):", kategoria_ceny(75))
