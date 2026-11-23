STRATEGIA = {
    "jednostkowe": ["koszt_dostawy", "rabat", "kod_pocztowy"],
    "integracyjne": ["GET /api/produkty", "zapis zamówienia"],
    "e2e": ["logowanie poprawne", "błędne hasło", "koszyk i suma", "zamówienie"],
    "reczne": ["wygląd na telefonie", "czytelność komunikatów"],
}
PRZYPADKI_KOD = ["00-950", "00950", "0-950", "00-95", "ab-cde", "", " 00-950 "]
for poziom, testy in STRATEGIA.items():
    print(f"{poziom:<13}{len(testy):>2}  {', '.join(testy)}")
razem = sum(len(t) for t in STRATEGIA.values())
print("Automatyczne:", razem - len(STRATEGIA["reczne"]), "z", razem)
print("Przypadki kodu pocztowego:", len(PRZYPADKI_KOD))
