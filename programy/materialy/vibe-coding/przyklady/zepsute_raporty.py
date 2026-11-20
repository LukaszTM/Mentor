# zepsute_raporty.py — raporty rezerwacji „Pod Lipą” (kod od AI z błędami)

def suma_przychodu(rezerwacje):
    """Suma pól 'kwota'."""
    suma = 0
    for r in rezerwacje:
        suma =+ r["kwota"]
    return suma


def srednia_dlugosc(rezerwacje):
    """Średnia liczba nocy, zaokrąglona do 1 miejsca; pusta lista → 0."""
    if not rezerwacje:
        return 0
    return round(sum(r["noce"] for r in rezerwacje) // len(rezerwacje), 1)


def top_pokoje(rezerwacje, n=3):
    """Lista (pokoj, suma_nocy) — najwięcej nocy pierwsze, remis alfabetycznie; najwyżej n pozycji."""
    sumy = {}
    for r in rezerwacje:
        sumy[r["pokoj"]] = sumy.get(r["pokoj"], 0) + r["noce"]
    return sorted(sumy.items(), key=lambda p: (p[1], p[0]))[:n]
