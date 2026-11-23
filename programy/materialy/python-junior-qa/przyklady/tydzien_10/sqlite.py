import sqlite3

con = sqlite3.connect(":memory:")
con.row_factory = sqlite3.Row
con.execute("""CREATE TABLE produkty (
    id INTEGER PRIMARY KEY, nazwa TEXT NOT NULL UNIQUE, kategoria TEXT NOT NULL,
    cena REAL NOT NULL CHECK (cena >= 0), ilosc INTEGER NOT NULL DEFAULT 0)""")
with con:
    con.executemany("INSERT INTO produkty (nazwa, kategoria, cena, ilosc) VALUES (?, ?, ?, ?)",
                    [("Zeszyt A5", "zeszyty", 4.5, 120), ("Segregator A4", "biuro", 11.9, 45), ("Zszywacz", "biuro", 19.9, 15)])
for w in con.execute("SELECT nazwa, cena FROM produkty WHERE kategoria = ? ORDER BY cena DESC", ("biuro",)):
    print(w["nazwa"], w["cena"])
with con:
    con.execute("UPDATE produkty SET ilosc = ilosc - ? WHERE nazwa = ?", (5, "Zszywacz"))
print("Zszywacz:", con.execute("SELECT ilosc FROM produkty WHERE nazwa = ?", ("Zszywacz",)).fetchone()["ilosc"])
try:
    with con:
        con.execute("INSERT INTO produkty (nazwa, kategoria, cena) VALUES (?, ?, ?)", ("Zeszyt A5", "zeszyty", 4.5))
except sqlite3.IntegrityError as e:
    print("Duplikat:", e)
zla = "x' OR '1'='1"
print("f-string:", len(con.execute(f"SELECT * FROM produkty WHERE nazwa = '{zla}'").fetchall()), "wierszy")
print("parametr ?:", len(con.execute("SELECT * FROM produkty WHERE nazwa = ?", (zla,)).fetchall()), "wierszy")
