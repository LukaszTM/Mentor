"""Logika magazynu: przyjęcia i wydania z kontrolą stanu oraz historia operacji."""
import baza


def _ilosc_poprawna(ilosc):
    if not isinstance(ilosc, int) or ilosc <= 0:
        raise ValueError("ilość musi być dodatnią liczbą całkowitą")


def przyjecie(con, pid, ilosc, data):
    """Przyjmuje towar; zwraca nowy stan."""
    _ilosc_poprawna(ilosc)
    nowy = baza.zmien_ilosc(con, pid, ilosc)
    baza.dodaj_operacje(con, pid, "przyjecie", ilosc, data)
    return nowy


def wydanie(con, pid, ilosc, data):
    """Wydaje towar (najwyżej cały stan); zwraca nowy stan."""
    p = baza.pobierz_produkt(con, pid)
    if p is None:
        raise ValueError(f"nie ma produktu o id {pid}")
    stan = p["ilosc"]
    if ilosc <= 0 or ilosc > stan or not isinstance(ilosc, int):
        raise ValueError(f"nie można wydać {ilosc} szt. (stan: {stan})")
    nowy = baza.zmien_ilosc(con, pid, -ilosc)
    baza.dodaj_operacje(con, pid, "wydanie", ilosc, data)
    return nowy


def historia(con, pid):
    """Lista (data, typ, ilość) operacji produktu rosnąco po dacie."""
    w = con.execute("SELECT data, typ, ilosc FROM operacje WHERE produkt_id = ? ORDER BY data, id", (pid,)).fetchall()
    return [(r["data"], r["typ"], r["ilosc"]) for r in w]


def wartosc_magazynu(con):
    return round(sum(p["cena"] * p["ilosc"] for p in baza.pobierz_produkty(con)), 2)
