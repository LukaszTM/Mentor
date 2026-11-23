import pytest

from magazyn_csv import dodaj, statystyki, szukaj, wczytaj, zapisz

CSV = ("id,nazwa,kategoria,cena,ilosc\n"
       "1,Zeszyt A5,zeszyty,4.50,120\n"
       "3,Długopis,pisaki,2.30,300\n"
       "17,Zszywki,biuro,3.90,0\n")


@pytest.fixture
def produkty(tmp_path):
    p = tmp_path / "produkty.csv"
    p.write_text(CSV, encoding="utf-8")
    return wczytaj(p)


def test_wczytaj_typy(produkty):
    assert isinstance(produkty[0]["cena"], float) and isinstance(produkty[0]["ilosc"], int)


def test_wczytaj_liczba(produkty):
    assert len(produkty) == 3


def test_statystyki_liczba(produkty):
    assert statystyki(produkty)["liczba"] == 3


def test_statystyki_srednia(produkty):
    assert statystyki(produkty)["srednia_cena"] == pytest.approx(3.57)


def test_statystyki_najdrozszy(produkty):
    assert statystyki(produkty)["najdrozszy"] == "Zeszyt A5"


def test_statystyki_wartosc_z_iloscia(produkty):
    assert statystyki(produkty)["wartosc"] == pytest.approx(1230.0)


def test_statystyki_pusta_lista():
    assert statystyki([]) == {"liczba": 0, "srednia_cena": 0, "najdrozszy": None, "wartosc": 0}


def test_dodaj_nadaje_id(produkty):
    assert dodaj(produkty, "Klej", "akcesoria", 3.4, 10)["id"] == 18


def test_dodaj_cena_zero_dozwolona(produkty):
    assert dodaj(produkty, "Gratis", "akcesoria", 0, 1)["cena"] == 0


def test_dodaj_duplikat_inna_wielkosc(produkty):
    with pytest.raises(ValueError):
        dodaj(produkty, "zeszyt a5", "zeszyty", 1, 1)


def test_dodaj_cena_ujemna(produkty):
    with pytest.raises(ValueError):
        dodaj(produkty, "Nowy", "biuro", -0.01, 1)


def test_dodaj_ilosc_ujemna(produkty):
    with pytest.raises(ValueError):
        dodaj(produkty, "Nowy", "biuro", 1, -1)


def test_dodaj_pusta_nazwa(produkty):
    with pytest.raises(ValueError):
        dodaj(produkty, "   ", "biuro", 1, 1)


def test_szukaj_bez_wielkosci_liter(produkty):
    assert [p["nazwa"] for p in szukaj(produkty, "ZESZYT")] == ["Zeszyt A5"]


def test_szukaj_po_kategorii(produkty):
    assert [p["nazwa"] for p in szukaj(produkty, "biuro")] == ["Zszywki"]


def test_szukaj_brak(produkty):
    assert szukaj(produkty, "farby") == []


def test_zapisz_i_wczytaj(produkty, tmp_path):
    cel = tmp_path / "kopia.csv"
    zapisz(produkty, cel)
    assert wczytaj(cel) == produkty
