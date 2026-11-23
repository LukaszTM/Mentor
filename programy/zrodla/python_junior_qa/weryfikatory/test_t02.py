# Weryfikator tygodnia 2 — lista_zakupow.py, suma.py, napisy.py, zgadnij.py.


def test_lista_zakupow():
    dane = "1\nzeszyt\n1\nklej\n1\ngumka\n2\nklej\n3\n0\n"
    kod, out = uruchom("lista_zakupow.py", dane)
    bez_bledu(kod, out, dane)
    zawiera(out, "1. zeszyt", "2. gumka", dane="dodaj zeszyt, klej, gumka; usuń klej; wypisz")
    assert "3. " not in out.split("2. gumka")[-1][:40], "po usunięciu kleju lista ma mieć 2 pozycje"
    kod, out = uruchom("lista_zakupow.py", "2\nfarby\n0\n")
    bez_bledu(kod, out, "usuń nieistniejący")
    zawiera(out, "nie ma", dane="usunięcie produktu, którego nie ma na liście")
    kod, out = uruchom("lista_zakupow.py", "3\n0\n")
    zawiera(out, "pusta", dane="wypisanie pustej listy")
    kod, out = uruchom("lista_zakupow.py", "7\n0\n")
    bez_bledu(kod, out, "opcja 7")
    zawiera(out, "nieznana opcja", dane="opcja 7")


def test_suma():
    for dane, ocz in (("5\n3\n4\n0\n", ("12", "4.0", "5")), ("2.5\n-1\n0\n", ("1.5", "0.75", "2.5"))):
        kod, out = uruchom("suma.py", dane)
        bez_bledu(kod, out, dane)
        zawiera(out, *ocz, dane=dane)
    kod, out = uruchom("suma.py", "0\n")
    bez_bledu(kod, out, "0")
    zawiera(out, "nie podano", dane="od razu 0 (brak liczb)")


def test_napisy():
    kod, out = uruchom("napisy.py", "Ala ma kota i psa\n")
    bez_bledu(kod, out, "Ala ma kota i psa")
    for f in ("ALA MA KOTA I PSA", "asp i atok am alA", "17", "kota"):
        assert f in out, f"dla „Ala ma kota i psa” brakuje w wyjściu: {f}\n{out[-600:]}"
    assert "7" in out and "5" in out, "dla „Ala ma kota i psa”: 7 samogłosek i 5 słów"
    kod, out = uruchom("napisy.py", "  Zeszyt w kratkę  \n")
    bez_bledu(kod, out, "Zeszyt w kratkę")
    for f in ("ZESZYT W KRATKĘ", "ęktark w tyzseZ", "15", "Zeszyt"):
        assert f in out, f"dla „  Zeszyt w kratkę  ” (ze spacjami — strip!) brakuje w wyjściu: {f}\n{out[-600:]}"


def test_zgadnij():
    m = modul("zgadnij")
    ocen = funkcja(m, "ocen")
    ok(ocen(10, 50), "za mało", "ocen(10, 50)")
    ok(ocen(90, 50), "za dużo", "ocen(90, 50)")
    ok(ocen(50, 50), "trafione", "ocen(50, 50)")
    ok(ocen(1, 1), "trafione", "ocen(1, 1)")
    dane = "".join(f"{i}\n" for i in range(1, 101))
    kod, out = uruchom("zgadnij.py", dane)
    bez_bledu(kod, out, "kolejne liczby 1…100")
    zawiera(out, "trafione", "prób", dane="kolejne liczby 1…100 (gra kończy się trafieniem i liczbą prób)")
