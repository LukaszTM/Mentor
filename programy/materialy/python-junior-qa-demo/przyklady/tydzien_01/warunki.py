def koszt_dostawy(razem):
    if razem >= 100:
        return 0
    elif razem >= 50:
        return 9.99
    else:
        return 14.99


for kwota in [49.99, 50, 99.99, 100, 250]:
    print(kwota, "->", koszt_dostawy(kwota))
