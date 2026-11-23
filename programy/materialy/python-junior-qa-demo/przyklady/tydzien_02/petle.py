ceny = [4.5, 2.3, 0, 7.5, 24.99]
suma = 0
ile_drogich = 0
for cena in ceny:
    if cena == 0:
        continue
    suma += cena
    if cena > 5:
        ile_drogich += 1
print(f"Suma: {suma:.2f}, droższe niż 5 zł: {ile_drogich}")

for n in range(1, 4):
    print(n, "x 7 =", n * 7)

stan = 10
while stan > 0:
    stan -= 4
    print("Zostało:", stan)
