"""Cennik sezonowy i rabaty „Pod Lipą”."""

WYSOKI = (6, 7, 8, 12)


def sezon(miesiac):
    if miesiac not in range(1, 13):
        raise ValueError("miesiąc musi być liczbą 1–12")
    return "wysoki" if miesiac in WYSOKI else "niski"


def cena_nocy(miesiac):
    return 150 if sezon(miesiac) == "wysoki" else 110


def rabat(noce, osoby):
    if noce < 1 or osoby < 1:
        raise ValueError("noce i osoby muszą być co najmniej 1")
    r = 0
    if noce >= 7:
        r += 10
    if osoby >= 4:
        r += 5
    return min(r, 15)


def do_zaplaty(miesiac, noce, osoby):
    brutto = noce * osoby * cena_nocy(miesiac)
    return round(brutto * (100 - rabat(noce, osoby)) / 100, 2)
