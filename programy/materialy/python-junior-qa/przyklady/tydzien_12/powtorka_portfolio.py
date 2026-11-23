LISTA = {
    "README z sekcją Jak testuję": True,
    "CI zielone z raportem HTML": True,
    "Zapytania SQL z parametrami ?": True,
    "Testy wartości brzegowych reguł": True,
    "Brak time.sleep w testach E2E": False,
    "Brak sekretów w repozytorium": True,
    "PLAN_TESTOW.md": False,
}
spelnione = [k for k, v in LISTA.items() if v]
do_poprawy = [k for k, v in LISTA.items() if not v]
print(f"Spełnione: {len(spelnione)}/{len(LISTA)} ({len(spelnione) / len(LISTA):.0%})")
for nr, k in enumerate(do_poprawy, 1):
    print(f"{nr}. Popraw: {k}")
