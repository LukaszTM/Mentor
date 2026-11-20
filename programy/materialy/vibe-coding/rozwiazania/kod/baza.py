"""Goście „Pod Lipą” w SQLite — wyłącznie zapytania z parametrami."""
import sqlite3

SCHEMAT = """CREATE TABLE IF NOT EXISTS goscie (
    id INTEGER PRIMARY KEY,
    imie TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    noce INTEGER NOT NULL CHECK (noce >= 1)
)"""


def polacz(sciezka=":memory:"):
    con = sqlite3.connect(sciezka)
    con.row_factory = sqlite3.Row
    con.execute(SCHEMAT)
    return con


def dodaj_goscia(con, imie, email, noce):
    imie = (imie or "").strip()
    if not imie or noce < 1:
        raise ValueError("imię niepuste i noce ≥ 1")
    try:
        with con:
            cur = con.execute("INSERT INTO goscie (imie, email, noce) VALUES (?, ?, ?)", (imie, email, noce))
    except sqlite3.IntegrityError as e:
        raise ValueError(f"nie można dodać gościa: {e}") from None
    return cur.lastrowid


def znajdz_po_emailu(con, email):
    w = con.execute("SELECT id, imie, email, noce FROM goscie WHERE email = ?", (email,)).fetchone()
    return dict(w) if w else None


def lista_gosci(con):
    return [dict(w) for w in con.execute("SELECT id, imie, email, noce FROM goscie ORDER BY id")]
