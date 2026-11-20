"""Cennik gospodarstwa „Pod Lipą” (dane fikcyjne).

Specyfikacja:
- cena_pokoju(pokoj, miesiac) → cena za noc (zł) za pokój:
    Lipowy 180 (sezon wysoki) / 140 (niski), Dębowy 160 / 120, Klonowy 200 / 150.
    Sezon wysoki: czerwiec, lipiec, sierpień, grudzień (6, 7, 8, 12); pozostałe miesiące 1–12 — niski.
    Nieznany pokój albo miesiąc spoza 1–12 → ValueError.
- oplata_klimatyczna(dorosli, noce, dzieci=0) → 2,50 zł za dorosłego za noc; dzieci nie płacą.
    dorosli < 1, noce < 1 albo dzieci < 0 → ValueError. Wynik zaokrąglony do groszy.
"""

CENY = {"Lipowy": (180, 140), "Dębowy": (160, 120), "Klonowy": (200, 150)}
SEZON_WYSOKI = (6, 7, 8, 12)
STAWKA_KLIMATYCZNA = 2.5


def cena_pokoju(pokoj, miesiac):
    if pokoj not in CENY:
        raise ValueError(f"nieznany pokój: {pokoj}")
    if miesiac not in range(1, 13):
        raise ValueError("miesiąc musi być liczbą 1–12")
    wysoka, niska = CENY[pokoj]
    return wysoka if miesiac in SEZON_WYSOKI else niska


def oplata_klimatyczna(dorosli, noce, dzieci=0):
    if dorosli < 1 or noce < 1 or dzieci < 0:
        raise ValueError("dorośli i noce ≥ 1, dzieci ≥ 0")
    return round(dorosli * noce * STAWKA_KLIMATYCZNA, 2)
