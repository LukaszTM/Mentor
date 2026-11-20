# Weryfikator tygodnia 2 — napraw_mnie.py i lista_gosci.py.


def test_napraw_srednia():
    f = funkcja(modul("napraw_mnie"), "srednia_ocen")
    ok(f([5, 4, 5]), 4.67, "srednia_ocen([5, 4, 5])")
    ok(f([3]), 3, "srednia_ocen([3])")
    ok(f([]), 0, "srednia_ocen([]) — pusta lista (bez dzielenia przez zero)")


def test_napraw_najlepsza():
    f = funkcja(modul("napraw_mnie"), "najlepsza")
    ok(f([3, 5, 4]), 5, "najlepsza([3, 5, 4])")
    ok(f([2]), 2, "najlepsza([2])")
    assert f([]) is None, "najlepsza([]) powinna zwrócić None"


def test_napraw_noclegi():
    f = funkcja(modul("napraw_mnie"), "liczba_noclegow")
    ok(f([{"noce": 2}, {"noce": 3}]), 5, "liczba_noclegow([{'noce': 2}, {'noce': 3}])")
    ok(f([{"noce": 1}, {"noce": 1}, {"noce": 4}]), 6, "liczba_noclegow — trzy rezerwacje")
    ok(f([]), 0, "liczba_noclegow([])")


def _lg():
    m = modul("lista_gosci")
    return funkcja(m, "dodaj_goscia"), funkcja(m, "liczba_gosci"), funkcja(m, "raport")


def test_lista_dodawanie():
    dodaj, liczba, _ = _lg()
    l = []
    w = dodaj(l, "Anna", 2)
    assert w is l, "dodaj_goscia powinna zwrócić tę samą listę (return lista)"
    assert l == [{"imie": "Anna", "noce": 2}], f"po dodaj_goscia([], 'Anna', 2) lista to {l!r}, oczekiwano [{{'imie': 'Anna', 'noce': 2}}]"
    dodaj(l, "  Piotr ", 3)
    assert l[1] == {"imie": "Piotr", "noce": 3}, f"imię powinno być bez spacji na brzegach: otrzymano {l[1]!r}"
    ok(liczba(l), 2, "liczba_gosci po dodaniu 2 gości")
    ok(liczba([]), 0, "liczba_gosci([])")


def test_lista_walidacja():
    dodaj, _, _ = _lg()
    rzuca(dodaj, [], "", 2, opis="dodaj_goscia z pustym imieniem")
    rzuca(dodaj, [], "   ", 2, opis="dodaj_goscia z imieniem z samych spacji")
    rzuca(dodaj, [], "Ewa", 0, opis="dodaj_goscia z 0 nocy")


def test_lista_raport_odmiana():
    _, _, raport = _lg()
    l = [{"imie": i, "noce": n} for i, n in (("Anna", 1), ("Piotr", 3), ("Ola", 5), ("Ewa", 12), ("Jan", 22), ("Iza", 25), ("Tomek", 4))]
    linie = [x.strip() for x in raport(l).strip().splitlines()]
    oczek = ["Anna: 1 noc", "Piotr: 3 noce", "Ola: 5 nocy", "Ewa: 12 nocy", "Jan: 22 noce", "Iza: 25 nocy", "Tomek: 4 noce"]
    assert linie == oczek, f"raport: oczekiwano linii {oczek}, otrzymano {linie}"


def test_lista_raport_pusty():
    _, _, raport = _lg()
    ok(raport([]).strip(), "Brak gości", "raport([])")
