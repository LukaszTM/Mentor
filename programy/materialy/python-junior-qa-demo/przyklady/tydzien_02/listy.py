koszyk = ["zeszyt", "długopis", "klej"]
ceny = [4.5, 2.3, 3.4]
koszyk.append("gumka")
ceny.append(1.5)
print(koszyk[0], koszyk[-1], len(koszyk))
print(koszyk[1:3])
koszyk.remove("klej")
print(koszyk, "klej" in koszyk)
print("Suma:", sum(ceny), "max:", max(ceny), "min:", min(ceny))
print(sorted(ceny), sorted(ceny, reverse=True)[0])
print(f"Średnia: {sum(ceny) / len(ceny):.2f}")
