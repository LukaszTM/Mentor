"""Raport obrotów „Pod Lipą” — po refaktoryzacji (te same wyniki)."""

SEZON_WYSOKI = (6, 7, 8, 12)
CENA_WYSOKA = 150
CENA_NISKA = 110
RABAT_DLUGI = 0.9
PROG_RABATU = 7
MIESIACE = ["Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec", "Lipiec", "Sierpień", "Wrzesień", "Październik", "Listopad", "Grudzień"]


def cena_nocy(miesiac):
    """Cena za osobę za noc zależna od sezonu."""
    return CENA_WYSOKA if miesiac in SEZON_WYSOKI else CENA_NISKA


def koszt(rezerwacja):
    """Koszt jednej rezerwacji z rabatem za długi pobyt."""
    k = rezerwacja["noce"] * rezerwacja["osoby"] * cena_nocy(rezerwacja["miesiac"])
    return k * RABAT_DLUGI if rezerwacja["noce"] >= PROG_RABATU else k


def przychod(rezerwacje):
    """Suma kosztów wszystkich rezerwacji, zaokrąglona do groszy."""
    return round(sum(koszt(r) for r in rezerwacje), 2)


def sumy_miesieczne(rezerwacje):
    """Słownik: numer miesiąca → suma kosztów."""
    sumy = {}
    for r in rezerwacje:
        sumy[r["miesiac"]] = sumy.get(r["miesiac"], 0) + koszt(r)
    return sumy


def zl(kwota):
    """Kwota w formacie „1 234,56 zł”."""
    return f"{kwota:,.2f}".replace(",", " ").replace(".", ",") + " zł"


def raport_tekstowy(rezerwacje):
    """Linie „Miesiąc: kwota” w kolejności miesięcy i linia „Razem”."""
    sumy = sumy_miesieczne(rezerwacje)
    linie = [f"{MIESIACE[m - 1]}: {zl(sumy[m])}" for m in sorted(sumy)]
    linie.append(f"Razem: {zl(sum(sumy.values()))}")
    return "\n".join(linie)
