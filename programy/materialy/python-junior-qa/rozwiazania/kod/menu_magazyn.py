"""Magazyn — menu w konsoli (baza: zmienna środowiskowa MAGAZYN_DB albo magazyn.db)."""
import os
from datetime import date

import baza
import magazyn


def menu():
    con = baza.utworz_baze(os.environ.get("MAGAZYN_DB", "magazyn.db"))
    while True:
        w = input("1 dodaj produkt, 2 przyjęcie, 3 wydanie, 4 lista, 0 koniec: ").strip()
        try:
            if w == "1":
                pid = baza.dodaj_produkt(con, input("Nazwa: "), input("Kategoria: "), float(input("Cena: ").replace(",", ".")))
                print("Dodano produkt nr", pid)
            elif w in ("2", "3"):
                pid, n = int(input("Nr produktu: ")), int(input("Ilość: "))
                f = magazyn.przyjecie if w == "2" else magazyn.wydanie
                print("Stan po operacji:", f(con, pid, n, date.today().isoformat()))
            elif w == "4":
                for p in baza.pobierz_produkty(con):
                    print(f"{p['id']:>3}. {p['nazwa']:<25} {p['cena']:>8.2f} zł {p['ilosc']:>5} szt.")
            elif w == "0":
                break
            else:
                print("Nieznana opcja")
        except (ValueError, baza.sqlite3.IntegrityError) as e:
            print("Błąd:", e)


if __name__ == "__main__":
    menu()
