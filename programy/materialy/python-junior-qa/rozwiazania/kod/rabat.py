kwota = float(input("Kwota zamówienia (zł): "))

if kwota < 0:
    print("Kwota nie może być ujemna")
else:
    if kwota >= 300:
        rabat = 10
    elif kwota >= 100:
        rabat = 5
    else:
        rabat = 0
    do_zaplaty = kwota * (100 - rabat) / 100
    print(f"Rabat: {rabat}%")
    print(f"Do zapłaty: {do_zaplaty:.2f} zł")
