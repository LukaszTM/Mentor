# Weryfikator tygodnia 1 — terminal i kalkulator_pobytu.py.


def test_terminal():
    for f in ("raporty", "dane", "notatki"):
        assert (WS / f).is_dir(), f"Brak folderu {f} w katalogu roboczym — utwórz go komendą mkdir {f}"
    p = plik("terminal.txt")
    surowe = p.read_bytes()
    t = surowe.decode("utf-8", errors="replace") + "\n" + surowe.decode("cp852", errors="replace")
    assert "<DIR>" in t, "terminal.txt nie zawiera „<DIR>” — zapisz wynik komendy: dir > terminal.txt (nie wpisuj listy ręcznie)"
    for f in ("raporty", "dane", "notatki"):
        assert f in t, f"terminal.txt: na liście z komendy dir brakuje folderu {f} — utwórz folder i zapisz listę ponownie"


def _k():
    return funkcja(modul("kalkulator_pobytu"), "koszt_pobytu")


def test_kalkulator_przyklady():
    f = _k()
    ok(f(2, 2), 480, "koszt_pobytu(2, 2)")
    ok(f(1, 1), 120, "koszt_pobytu(1, 1)")
    ok(f(6, 1), 720, "koszt_pobytu(6, 1) — 6 nocy, jeszcze bez rabatu")


def test_kalkulator_rabat_od_7_nocy():
    f = _k()
    ok(f(7, 1), 756.0, "koszt_pobytu(7, 1) — granica: od 7 nocy rabat 10%")
    ok(f(7, 2), 1512.0, "koszt_pobytu(7, 2)")
    ok(f(10, 3), 3240.0, "koszt_pobytu(10, 3)")


def test_kalkulator_inna_cena_i_grosze():
    f = _k()
    ok(f(2, 2, cena_za_osobe_noc=150), 600, "koszt_pobytu(2, 2, cena_za_osobe_noc=150)")
    ok(f(7, 1, cena_za_osobe_noc=99.99), 629.94, "koszt_pobytu(7, 1, cena_za_osobe_noc=99.99) — zaokrąglenie do groszy")
    w = f(7, 1, cena_za_osobe_noc=99.99)
    assert round(w, 2) == w, f"wynik {w!r} nie jest zaokrąglony do groszy — użyj round(koszt, 2)"


def test_kalkulator_zle_dane():
    f = _k()
    rzuca(f, 0, 2, opis="koszt_pobytu(0, 2) — zero nocy")
    rzuca(f, 2, 0, opis="koszt_pobytu(2, 0) — zero osób")
    rzuca(f, -3, 1, opis="koszt_pobytu(-3, 1) — ujemna liczba nocy")
