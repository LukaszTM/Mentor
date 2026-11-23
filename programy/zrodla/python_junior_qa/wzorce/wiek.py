import datetime

rok_urodzenia = int(input("Rok urodzenia: "))
rok = datetime.date.today().year
wiek = rok - rok_urodzenia

if wiek < 0:
    print("To rok z przyszłości — sprawdź wpis")
elif wiek >= 18:
    print(f"Masz {wiek} lat — pełnoletni")
else:
    print(f"Masz {wiek} lat — niepełnoletni")
