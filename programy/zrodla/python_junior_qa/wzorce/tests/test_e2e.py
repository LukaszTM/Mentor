"""Testy E2E aplikacji Magazyn (serwer i przeglądarka z fixtur w conftest.py)."""
from pages.magazyn_pages import DodajPage, ListaPage, ProduktPage


def test_pusta_lista(serwer, driver):
    assert ListaPage(driver, serwer).open().nazwy() == []


def test_dodanie_formularzem(serwer, driver):
    assert "Klej w sztyfcie" in DodajPage(driver, serwer).open().dodaj("Klej w sztyfcie", "akcesoria", "3,40", "10").nazwy()


def test_przyjecie_i_historia(serwer, driver):
    DodajPage(driver, serwer).open().dodaj("Zszywacz", "biuro", "19.90", "0")
    assert ProduktPage(driver, serwer).open(1).operacja("przyjecie", 15).stan() == "15"
