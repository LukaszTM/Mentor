from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

ADRES = "http://127.0.0.1:5001"


class ProduktyPage:
    def __init__(self, driver):
        self.driver = driver
        self.czekaj = WebDriverWait(driver, 10)

    def dodaj(self, pid, ilosc=1):
        pole = self.czekaj.until(EC.visibility_of_element_located((By.ID, f"ilosc-{pid}")))
        pole.clear()
        pole.send_keys(str(ilosc))
        self.driver.find_element(By.ID, f"dodaj-{pid}").click()
        return KoszykPage(self.driver)

    def szukaj(self, fraza):
        self.czekaj.until(EC.visibility_of_element_located((By.ID, "szukaj"))).send_keys(fraza)
        self.driver.find_element(By.ID, "szukaj-btn").click()
        return len(self.driver.find_elements(By.CSS_SELECTOR, "#produkty .produkt"))


class KoszykPage:
    SUMA = (By.CSS_SELECTOR, "[data-test=suma]")

    def __init__(self, driver):
        self.driver = driver
        self.czekaj = WebDriverWait(driver, 10)

    def suma(self):
        return self.czekaj.until(EC.visibility_of_element_located(self.SUMA)).text

    def do_zamowienia(self):
        self.czekaj.until(EC.element_to_be_clickable((By.ID, "do-zamowienia"))).click()
