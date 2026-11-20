"""Dostępność pokoi „Pod Lipą”."""
from datetime import date

POKOJE = ["Lipowy", "Dębowy", "Klonowy"]


def _d(t):
    return t if isinstance(t, date) else date.fromisoformat(t)


def noce(od, do):
    n = (_d(do) - _d(od)).days
    if n < 1:
        raise ValueError("data wyjazdu musi być po dacie przyjazdu")
    return n


def koliduje(a, b):
    if a["pokoj"] != b["pokoj"]:
        return False
    return _d(a["od"]) < _d(b["do"]) and _d(b["od"]) < _d(a["do"])


def czy_wolny(rezerwacje, pokoj, od, do):
    nowa = {"pokoj": pokoj, "od": od, "do": do}
    return not any(koliduje(r, nowa) for r in rezerwacje)


def wolne_pokoje(rezerwacje, od, do):
    return [p for p in POKOJE if czy_wolny(rezerwacje, p, od, do)]
