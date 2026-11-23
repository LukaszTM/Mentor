"""Warstwa danych projektu Magazyn — SQLite, zapytania wyłącznie z parametrami ?."""
import sqlite3


def utworz_baze(sciezka="magazyn.db"):
    """Połączenie z bazą (wiersze jak słowniki) i tabele, jeśli ich nie ma."""
    con = sqlite3.connect(sciezka)
    con.row_factory = sqlite3.Row
    with con:
        con.execute("""CREATE TABLE IF NOT EXISTS produkty (
            id INTEGER PRIMARY KEY, nazwa TEXT NOT NULL UNIQUE, kategoria TEXT NOT NULL,
            cena REAL NOT NULL CHECK (cena >= 0), ilosc INTEGER NOT NULL DEFAULT 0 CHECK (ilosc >= 0))""")
        con.execute("""CREATE TABLE IF NOT EXISTS operacje (
            id INTEGER PRIMARY KEY, produkt_id INTEGER NOT NULL REFERENCES produkty(id),
            typ TEXT NOT NULL CHECK (typ IN ('przyjecie', 'wydanie')), ilosc INTEGER NOT NULL, data TEXT NOT NULL)""")
    return con


def dodaj_produkt(con, nazwa, kategoria, cena, ilosc=0):
    """Dodaje produkt i zwraca jego id; duplikat nazwy → sqlite3.IntegrityError."""
    with con:
        cur = con.execute("INSERT INTO produkty (nazwa, kategoria, cena, ilosc) VALUES (?, ?, ?, ?)", (nazwa.strip(), kategoria.strip(), cena, ilosc))
    return cur.lastrowid


def pobierz_produkty(con, kategoria=None):
    """Lista produktów (słowniki) alfabetycznie; opcjonalnie z jednej kategorii."""
    if kategoria is None:
        wiersze = con.execute("SELECT * FROM produkty ORDER BY nazwa").fetchall()
    else:
        wiersze = con.execute("SELECT * FROM produkty WHERE kategoria = ? ORDER BY nazwa", (kategoria,)).fetchall()
    return [dict(w) for w in wiersze]


def pobierz_produkt(con, pid):
    w = con.execute("SELECT * FROM produkty WHERE id = ?", (pid,)).fetchone()
    return dict(w) if w else None


def zmien_ilosc(con, pid, delta):
    """Zmienia stan o delta i zwraca nowy stan; brak produktu albo stan < 0 → ValueError."""
    p = pobierz_produkt(con, pid)
    if p is None:
        raise ValueError(f"nie ma produktu o id {pid}")
    nowa = p["ilosc"] + delta
    if nowa < 0:
        raise ValueError(f"stan nie może być ujemny (jest {p['ilosc']})")
    with con:
        con.execute("UPDATE produkty SET ilosc = ? WHERE id = ?", (nowa, pid))
    return nowa


def usun_produkt(con, pid):
    with con:
        if con.execute("DELETE FROM produkty WHERE id = ?", (pid,)).rowcount == 0:
            raise ValueError(f"nie ma produktu o id {pid}")


def dodaj_operacje(con, pid, typ, ilosc, data):
    with con:
        con.execute("INSERT INTO operacje (produkt_id, typ, ilosc, data) VALUES (?, ?, ?, ?)", (pid, typ, ilosc, data))
