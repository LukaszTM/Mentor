import random
from datetime import date, datetime, timedelta

random.seed(7)
produkty = ["zeszyt", "długopis", "klej", "gumka", "blok", "kredki"]
print("Do inwentaryzacji:", random.sample(produkty, 3))
print("Kostka:", random.randint(1, 6))

def termin(od, dni=7):
    return od + timedelta(days=dni)

start = date(2026, 11, 23)
print("Termin:", termin(start).strftime("%d.%m.%Y"))
wigilia = datetime.strptime("24.12.2026", "%d.%m.%Y").date()
print("Dni do Wigilii:", (wigilia - start).days)
