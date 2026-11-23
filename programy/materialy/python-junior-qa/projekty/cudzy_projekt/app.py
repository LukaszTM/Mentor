from datetime import date

import baza
import raport


def menu():
    wyp = baza.wczytaj()
    while True:
        w = input("1 wypożycz, 2 raport miesiąca, 0 koniec: ").strip()
        if w == "1":
            wyp.append({"sprzet": input("Sprzęt: ").strip(), "osoba": input("Kto: ").strip(), "data": date.today().strftime("%d.%m.%Y")})
            baza.zapisz(wyp)
        elif w == "2":
            dzis = date.today()
            for sprzet, n in sorted(raport.raport_miesieczny(wyp, dzis.year, dzis.month).items()):
                print(f"{sprzet}: {n}")
        elif w == "0":
            break


if __name__ == "__main__":
    menu()
