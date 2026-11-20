# Weryfikator tygodnia 4 — instalacja agenta i powitanie.py.


def test_instalacja():
    p = plik("instalacja.txt")
    surowe = p.read_bytes()
    for kod in ("utf-8", "utf-16", "cp1250"):
        try:
            t = surowe.decode(kod)
            if re.search(r"\d+\.\d+", t):
                break
        except UnicodeDecodeError:
            continue
    else:
        t = surowe.decode("utf-8", errors="replace")
    t = t.replace("\x00", "")
    assert re.search(r"\b\d+\.\d+\.\d+\s*\(Claude Code\)", t) or re.search(r"codex(-cli)?\s+v?\d+\.\d+\.\d+", t, re.I), \
        "instalacja.txt nie zawiera wyniku claude --version („X.Y.Z (Claude Code)”) ani codex --version („codex-cli X.Y.Z”) — zapisz go komendą: claude --version > instalacja.txt"


def _p():
    return funkcja(modul("powitanie"), "powitanie")


def test_powitanie_godziny():
    f = _p()
    for g, w in ((9, "Dzień dobry, Anna!"), (5, "Dzień dobry, Anna!"), (17, "Dzień dobry, Anna!"), (18, "Dobry wieczór, Anna!"),
                 (23, "Dobry wieczór, Anna!"), (0, "Dobry wieczór, Anna!"), (4, "Dobry wieczór, Anna!")):
        ok(f("Anna", g), w, f"powitanie('Anna', {g})")


def test_powitanie_imie():
    f = _p()
    ok(f("anna", 9), "Dzień dobry, Anna!", "powitanie('anna', 9) — wielka pierwsza litera")
    ok(f("  Ewa ", 20), "Dobry wieczór, Ewa!", "powitanie('  Ewa ', 20) — bez spacji na brzegach")
    ok(f("maria-józefa", 10), "Dzień dobry, Maria-józefa!", "powitanie('maria-józefa', 10) — reszta imienia bez zmian")
    ok(f("ANNA", 10), "Dzień dobry, ANNA!", "powitanie('ANNA', 10) — reszta imienia bez zmian (nie capitalize)")


def test_powitanie_zle_dane():
    f = _p()
    rzuca(f, "", 9, opis="powitanie('', 9)")
    rzuca(f, "   ", 9, opis="powitanie('   ', 9)")
    rzuca(f, "Anna", 24, opis="powitanie('Anna', 24)")
    rzuca(f, "Anna", -1, opis="powitanie('Anna', -1)")
