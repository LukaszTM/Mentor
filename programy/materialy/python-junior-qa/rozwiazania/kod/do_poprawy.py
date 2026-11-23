"""Program z trzema błędami do znalezienia debuggerem (wersja poprawiona)."""


def srednia_ceny(ceny):
    if not ceny:
        return 0
    suma = 0
    for cena in ceny:
        suma += cena
    return suma / len(ceny)


def razem_koszyka(koszyk):
    suma = 0
    for cena, ilosc in koszyk:
        suma += cena * ilosc
    return suma


def kategoria_ceny(cena):
    if cena >= 50:
        return "drogi"
    if cena >= 10:
        return "średni"
    return "tani"


if __name__ == "__main__":
    print(srednia_ceny([4.0, 2.0, 6.0]), razem_koszyka([(2.0, 3), (5.0, 2)]), kategoria_ceny(75))
