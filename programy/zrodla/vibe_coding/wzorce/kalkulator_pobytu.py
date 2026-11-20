"""Kalkulator ceny pobytu w gospodarstwie „Pod Lipą”."""


def koszt_pobytu(noce, osoby, cena_za_osobe_noc=120):
    """Koszt pobytu: noce × osoby × cena; od 7 nocy rabat 10%; wynik w groszach."""
    if noce < 1 or osoby < 1:
        raise ValueError("noce i osoby muszą być co najmniej 1")
    koszt = noce * osoby * cena_za_osobe_noc
    if noce >= 7:
        koszt = koszt * 0.9
    return round(koszt, 2)


if __name__ == "__main__":
    print(koszt_pobytu(2, 2))
    print(koszt_pobytu(7, 1))
