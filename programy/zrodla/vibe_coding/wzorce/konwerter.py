"""Konwersja i formatowanie kwot."""


def parsuj_kwote(tekst):
    t = (tekst or "").strip().lower()
    if t.endswith("zł"):
        t = t[:-2]
    t = t.replace(" ", "").replace(" ", "").replace(",", ".")
    if not t or t.count(".") > 1:
        raise ValueError(f"nie rozumiem kwoty: {tekst!r}")
    try:
        return float(t)
    except ValueError:
        raise ValueError(f"nie rozumiem kwoty: {tekst!r}") from None


def zl_na_eur(kwota, kurs):
    if kwota < 0 or kurs <= 0:
        raise ValueError("kwota ≥ 0 i kurs > 0")
    return round(kwota / kurs, 2)


def formatuj_zl(kwota):
    return f"{kwota:,.2f}".replace(",", " ").replace(".", ",") + " zł"
