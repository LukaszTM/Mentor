"""Raporty rezerwacji „Pod Lipą” — wersja poprawiona."""


def suma_przychodu(rezerwacje):
    suma = 0
    for r in rezerwacje:
        suma += r["kwota"]
    return suma


def srednia_dlugosc(rezerwacje):
    if not rezerwacje:
        return 0
    return round(sum(r["noce"] for r in rezerwacje) / len(rezerwacje), 1)


def top_pokoje(rezerwacje, n=3):
    sumy = {}
    for r in rezerwacje:
        sumy[r["pokoj"]] = sumy.get(r["pokoj"], 0) + r["noce"]
    return sorted(sumy.items(), key=lambda p: (-p[1], p[0]))[:n]
