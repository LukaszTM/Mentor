import random
from datetime import date, timedelta


def do_inwentaryzacji(produkty, n=3, seed=None):
    """n różnych produktów do kontroli; seed daje powtarzalny wynik; n > liczba produktów → ValueError."""
    if n > len(produkty):
        raise ValueError("za mało produktów do wylosowania")
    los = random.Random(seed)
    return los.sample(produkty, n)


def termin(od, dni=7):
    """Data kontroli: od + dni."""
    return od + timedelta(days=dni)


if __name__ == "__main__":
    produkty = ["zeszyt", "długopis", "klej", "gumka", "blok", "kredki"]
    print("Do inwentaryzacji:", do_inwentaryzacji(produkty))
    print("Termin kontroli:", termin(date.today()).strftime("%d.%m.%Y"))
