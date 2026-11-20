# raport_obroty.py — raport obrotów „Pod Lipą” (działa, ale wymaga refaktoryzacji)


def przychod(rezerwacje):
    s = 0
    for r in rezerwacje:
        if r["miesiac"] in (6, 7, 8, 12):
            if r["noce"] >= 7:
                s = s + r["noce"] * r["osoby"] * 150 * 0.9
            else:
                s = s + r["noce"] * r["osoby"] * 150
        else:
            if r["noce"] >= 7:
                s = s + r["noce"] * r["osoby"] * 110 * 0.9
            else:
                s = s + r["noce"] * r["osoby"] * 110
    return round(s, 2)


def raport_tekstowy(rezerwacje):
    m = {}
    for r in rezerwacje:
        if r["miesiac"] in (6, 7, 8, 12):
            if r["noce"] >= 7:
                k = r["noce"] * r["osoby"] * 150 * 0.9
            else:
                k = r["noce"] * r["osoby"] * 150
        else:
            if r["noce"] >= 7:
                k = r["noce"] * r["osoby"] * 110 * 0.9
            else:
                k = r["noce"] * r["osoby"] * 110
        m[r["miesiac"]] = m.get(r["miesiac"], 0) + k
    linie = []
    nazwy = ["Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec", "Lipiec", "Sierpień", "Wrzesień", "Październik", "Listopad", "Grudzień"]
    for mies in sorted(m):
        kw = f"{m[mies]:,.2f}".replace(",", " ").replace(".", ",")
        linie.append(nazwy[mies - 1] + ": " + kw + " zł")
    razem = 0
    for mies in m:
        razem = razem + m[mies]
    kw = f"{razem:,.2f}".replace(",", " ").replace(".", ",")
    linie.append("Razem: " + kw + " zł")
    return "\n".join(linie)
