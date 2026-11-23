VAT = 0.23
PROG_DARMOWEJ_DOSTAWY = 100
KOSZT_DOSTAWY = 14.99


def brutto(netto):
    """Zwraca cenę brutto zaokrągloną do groszy."""
    return round(netto * (1 + VAT), 2)


def do_zaplaty(ceny_netto):
    """Suma brutto koszyka plus dostawa (darmowa od PROG_DARMOWEJ_DOSTAWY zł).

    ceny_netto: lista cen netto; pusta lista → 0.
    """
    if not ceny_netto:
        return 0
    suma = round(sum(brutto(c) for c in ceny_netto), 2)
    dostawa = 0 if suma >= PROG_DARMOWEJ_DOSTAWY else KOSZT_DOSTAWY
    return round(suma + dostawa, 2)


print(do_zaplaty([10, 20]), do_zaplaty([50, 40]), do_zaplaty([]))
print(do_zaplaty.__doc__.splitlines()[0])
