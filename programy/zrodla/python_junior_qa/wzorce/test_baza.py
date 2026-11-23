import pytest

import baza
import magazyn


@pytest.fixture
def con(tmp_path):
    c = baza.utworz_baze(tmp_path / "test.db")
    yield c
    c.close()


@pytest.fixture
def klej(con):
    return baza.dodaj_produkt(con, "Klej w sztyfcie", "akcesoria", 3.4, 10)


def test_dodaj_i_pobierz(con):
    baza.dodaj_produkt(con, "Zeszyt A5", "zeszyty", 4.5)
    assert [p["nazwa"] for p in baza.pobierz_produkty(con)] == ["Zeszyt A5"]


def test_filtr_kategorii(con, klej):
    baza.dodaj_produkt(con, "Segregator A4", "biuro", 11.9)
    assert [p["nazwa"] for p in baza.pobierz_produkty(con, "biuro")] == ["Segregator A4"]


def test_sql_injection(con, klej):
    assert baza.pobierz_produkty(con, "x' OR '1'='1") == []


def test_zmien_ilosc_ponizej_zera(con, klej):
    with pytest.raises(ValueError):
        baza.zmien_ilosc(con, klej, -11)


def test_przyjecie(con, klej):
    assert magazyn.przyjecie(con, klej, 5, "2026-11-20") == 15


def test_wydanie_calego_stanu(con, klej):
    assert magazyn.wydanie(con, klej, 10, "2026-11-20") == 0


def test_wydanie_ponad_stan(con, klej):
    with pytest.raises(ValueError):
        magazyn.wydanie(con, klej, 11, "2026-11-20")


def test_historia_po_dacie(con, klej):
    magazyn.przyjecie(con, klej, 5, "2026-11-22")
    magazyn.wydanie(con, klej, 3, "2026-11-21")
    assert magazyn.historia(con, klej) == [("2026-11-21", "wydanie", 3), ("2026-11-22", "przyjecie", 5)]


def test_wartosc_magazynu(con, klej):
    assert magazyn.wartosc_magazynu(con) == pytest.approx(34.0)
