stany = {"zeszyt": 120, "klej": 110, "zszywki": 0}
stany["gumka"] = 150
stany["klej"] = 100
del stany["zszywki"]
print(stany)
print(stany.get("farby", 0), "klej" in stany, len(stany))
for nazwa, ilosc in sorted(stany.items(), key=lambda p: p[1]):
    print(f"{nazwa:<8}{ilosc:>5}")
print("Razem sztuk:", sum(stany.values()))
produkty = [{"nazwa": "zeszyt", "cena": 4.5}, {"nazwa": "klej", "cena": 3.4}]
najtanszy = min(produkty, key=lambda p: p["cena"])
print("Najtańszy:", najtanszy["nazwa"])
