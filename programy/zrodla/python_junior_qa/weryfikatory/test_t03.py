# Weryfikator tygodnia 3 — funkcje.py, stany.py, bledy.py, losowanie.py, menedzer.py.
import ast as _ast
import datetime as _dt


def test_funkcje():
    m = modul("funkcje")
    pole, parz, maks, odw, sil = (funkcja(m, n) for n in ("pole_prostokata", "czy_parzysta", "maksimum", "odwroc", "silnia"))
    ok(pole(3, 4), 12, "pole_prostokata(3, 4)")
    ok(pole(2.5, 2), 5.0, "pole_prostokata(2.5, 2)")
    ok(parz(4), True, "czy_parzysta(4)")
    ok(parz(7), False, "czy_parzysta(7)")
    ok(parz(0), True, "czy_parzysta(0)")
    ok(maks([3, 9, 2]), 9, "maksimum([3, 9, 2])")
    ok(maks([-5, -2, -9]), -2, "maksimum([-5, -2, -9])")
    ok(maks([7]), 7, "maksimum([7])")
    rzuca(maks, [], opis="maksimum([])")
    ok(odw("kot"), "tok", "odwroc(\"kot\")")
    ok(odw(""), "", "odwroc(\"\")")
    ok(sil(0), 1, "silnia(0)")
    ok(sil(5), 120, "silnia(5)")
    rzuca(sil, -1, opis="silnia(-1)")
    for n in ("pole_prostokata", "czy_parzysta", "maksimum", "odwroc", "silnia"):
        assert (getattr(m, n).__doc__ or "").strip(), f"funkcja {n} nie ma docstringu"
    for w in _ast.walk(drzewo("funkcje.py")):
        if isinstance(w, _ast.FunctionDef) and w.name == "maksimum":
            uzyte = {getattr(c.func, "id", "") for c in _ast.walk(w) if isinstance(c, _ast.Call)}
            assert not uzyte & {"max", "sorted"}, "maksimum: napisz pętlę — bez wbudowanych max() i sorted()"


def test_stany():
    m = modul("stany")
    dodaj, usun, pos, razem = (funkcja(m, n) for n in ("dodaj", "usun", "posortowane", "razem"))
    s = {}
    dodaj(s, "zeszyt", 120)
    dodaj(s, "klej", 30)
    dodaj(s, "zeszyt", 10)
    ok(s, {"zeszyt": 130, "klej": 30}, "stany po dodaj(zeszyt 120), dodaj(klej 30), dodaj(zeszyt 10)")
    rzuca(dodaj, s, "gumka", 0, opis="dodaj(…, 0)")
    rzuca(dodaj, s, "gumka", -5, opis="dodaj(…, -5)")
    dodaj(s, "gumka", 30)
    ok(pos(s), [("gumka", 30), ("klej", 30), ("zeszyt", 130)], "posortowane — rosnąco po ilości, przy remisie po nazwie")
    ok(razem(s), 190, "razem")
    usun(s, "klej")
    assert "klej" not in s, "usun(s, \"klej\") — klej nadal jest w słowniku"
    rzuca(usun, s, "farby", opis="usun(s, \"farby\") — brak produktu")
    ok(razem({}), 0, "razem({})")


def test_bledy():
    m = modul("bledy")
    f = funkcja(m, "na_liczbe")
    ok(f("4.5"), 4.5, "na_liczbe(\"4.5\")")
    ok(f("4,5"), 4.5, "na_liczbe(\"4,5\")")
    ok(f("  3 "), 3.0, "na_liczbe(\"  3 \")")
    for zle in ("abc", "", "4,5,6"):
        rzuca(f, zle, opis=f"na_liczbe({zle!r})")
    kod, out = uruchom("bledy.py", "abc\n9\n2\n")
    bez_bledu(kod, out, "abc, 9, 2")
    zawiera(out, "nie liczba", "4.5", dane="abc → ponowne pytanie, potem 9 i 2")
    kod, out = uruchom("bledy.py", "8\n0\n")
    bez_bledu(kod, out, "8 i 0")
    zawiera(out, "zero", dane="8 / 0")


def test_losowanie():
    m = modul("losowanie")
    los, termin = funkcja(m, "do_inwentaryzacji"), funkcja(m, "termin")
    prod = ["zeszyt", "długopis", "klej", "gumka", "blok", "kredki"]
    w = los(prod)
    assert isinstance(w, list) and len(w) == 3, f"do_inwentaryzacji(produkty) ma zwrócić listę 3 produktów, zwróciła {w!r}"
    assert len(set(w)) == 3 and set(w) <= set(prod), f"wylosowane produkty mają być różne i z listy: {w!r}"
    ok(len(los(prod, 5)), 5, "len(do_inwentaryzacji(produkty, 5))")
    assert los(prod, 3, seed=7) == los(prod, 3, seed=7), "ten sam seed ma dawać ten sam wynik"
    rzuca(los, prod, 10, opis="do_inwentaryzacji(6 produktów, 10)")
    ok(prod, ["zeszyt", "długopis", "klej", "gumka", "blok", "kredki"], "lista wejściowa po losowaniu (nie zmieniaj jej)")
    ok(termin(_dt.date(2026, 1, 28)), _dt.date(2026, 2, 4), "termin(28.01.2026)")
    ok(termin(_dt.date(2026, 12, 28), 7), _dt.date(2027, 1, 4), "termin(28.12.2026, 7)")
    ok(termin(_dt.date(2026, 1, 28), 30), _dt.date(2026, 2, 27), "termin(28.01.2026, 30)")


def test_menedzer():
    m = modul("menedzer")
    dodaj, oznacz, usun, otwarte = (funkcja(m, n) for n in ("dodaj", "oznacz", "usun", "otwarte"))
    z = []
    dodaj(z, "Zamówić papier")
    dodaj(z, "  Policzyć zeszyty ")
    dodaj(z, "Wysłać paczkę")
    ok(otwarte(z), ["Zamówić papier", "Policzyć zeszyty", "Wysłać paczkę"], "otwarte po 3 × dodaj (spacje usunięte)")
    rzuca(dodaj, z, "   ", opis="dodaj(z, \"   \")")
    oznacz(z, 2)
    ok(otwarte(z), ["Zamówić papier", "Wysłać paczkę"], "otwarte po oznacz(z, 2)")
    for zly in (0, 4, -1):
        rzuca(oznacz, z, zly, opis=f"oznacz(z, {zly})")
    ok(usun(z, 1), "Zamówić papier", "usun(z, 1) zwraca tytuł")
    ok(len(z), 2, "liczba zadań po usunięciu")
    ok(otwarte(z), ["Wysłać paczkę"], "otwarte po usunięciu")
    rzuca(usun, z, 3, opis="usun(z, 3) przy 2 zadaniach")
    kod, out = uruchom("menedzer.py", "1\nZamówić papier\n3\n0\n")
    bez_bledu(kod, out, "menu: dodaj, lista, koniec")
    zawiera(out, "Zamówić papier", dane="menu: 1 dodaj → 3 lista → 0")
