# pages/login_page.py + tests/test_logowanie.py (w jednym pliku dla czytelności)
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

ADRES = "http://127.0.0.1:5001"


class LoginPage:
    LOGIN = (By.ID, "login")
    HASLO = (By.ID, "haslo")
    ZALOGUJ = (By.CSS_SELECTOR, "[data-test=zaloguj]")
    BLAD = (By.CSS_SELECTOR, "[data-test=blad]")
    POWITANIE = (By.CSS_SELECTOR, "[data-test=powitanie]")

    def __init__(self, driver):
        self.driver = driver
        self.czekaj = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(ADRES + "/logowanie")
        return self

    def login(self, login, haslo):
        self.czekaj.until(EC.visibility_of_element_located(self.LOGIN)).send_keys(login)
        self.driver.find_element(*self.HASLO).send_keys(haslo)
        self.driver.find_element(*self.ZALOGUJ).click()
        return self

    def error_text(self):
        return self.czekaj.until(EC.visibility_of_element_located(self.BLAD)).text

    def greeting(self):
        return self.czekaj.until(EC.visibility_of_element_located(self.POWITANIE)).text


@pytest.fixture
def driver():
    opcje = webdriver.EdgeOptions()
    opcje.add_argument("--headless=new")
    d = webdriver.Edge(options=opcje)
    yield d
    d.quit()


def test_logowanie_poprawne(driver):
    assert "tester" in LoginPage(driver).open().login("tester", "Test123!").greeting()


def test_bledne_haslo(driver):
    assert "Błędny login lub hasło" in LoginPage(driver).open().login("tester", "zle").error_text()
