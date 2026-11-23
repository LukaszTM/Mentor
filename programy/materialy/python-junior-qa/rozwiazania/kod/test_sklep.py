"""Testy E2E sklepu testowego (uruchomiony: python app.py w projekty/sklep_testowy)."""
from pages.koszyk_page import ProduktyPage  # noqa: F401
from pages.login_page import LoginPage


def zaloguj(driver):
    return LoginPage(driver).open().login("tester", "Test123!")


def test_logowanie_poprawne(driver):
    assert "tester" in zaloguj(driver).greeting()


def test_bledne_haslo(driver):
    assert "Błędny login lub hasło" in LoginPage(driver).open().login("tester", "zle").error_text()


def test_puste_pola(driver):
    assert "Błędny login" in LoginPage(driver).open().login("", "").error_text()


def test_koszyk_jedna_sztuka(driver):
    zaloguj(driver)
    assert "4,50" in ProduktyPage(driver).dodaj(1).suma()


def test_koszyk_dziesiec_sztuk(driver):
    zaloguj(driver)
    assert "45,00" in ProduktyPage(driver).dodaj(1, 10).suma()


def test_wyszukiwarka_bez_wielkosci_liter(driver):
    zaloguj(driver)
    assert ProduktyPage(driver).szukaj("długopis") == 2


def test_wyszukiwarka_brak_wynikow(driver):
    zaloguj(driver)
    assert ProduktyPage(driver).szukaj("rower") == 0


def test_login_wielka_litera(driver):
    assert "tester" in LoginPage(driver).open().login("Tester", "Test123!").greeting()
