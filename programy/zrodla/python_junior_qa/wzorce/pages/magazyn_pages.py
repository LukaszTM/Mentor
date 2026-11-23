from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ListaPage:
    def __init__(self, driver, adres):
        self.driver, self.adres = driver, adres
        self.czekaj = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.adres + "/")
        return self

    def nazwy(self):
        self.czekaj.until(EC.presence_of_element_located((By.ID, "produkty")))
        return [e.text.split("\n")[0] for e in self.driver.find_elements(By.CSS_SELECTOR, "#produkty .produkt td:first-child")]


class DodajPage:
    def __init__(self, driver, adres):
        self.driver, self.adres = driver, adres
        self.czekaj = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.adres + "/dodaj")
        return self

    def dodaj(self, nazwa, kategoria, cena, ilosc):
        self.czekaj.until(EC.visibility_of_element_located((By.ID, "nazwa"))).send_keys(nazwa)
        self.driver.find_element(By.ID, "kategoria").send_keys(kategoria)
        self.driver.find_element(By.ID, "cena").send_keys(cena)
        pole = self.driver.find_element(By.ID, "ilosc")
        pole.clear()
        pole.send_keys(ilosc)
        self.driver.find_element(By.CSS_SELECTOR, "[data-test=zapisz]").click()
        return ListaPage(self.driver, self.adres)


class ProduktPage:
    def __init__(self, driver, adres):
        self.driver, self.adres = driver, adres
        self.czekaj = WebDriverWait(driver, 10)

    def open(self, pid):
        self.driver.get(f"{self.adres}/produkt/{pid}")
        return self

    def operacja(self, typ, ilosc):
        self.czekaj.until(EC.visibility_of_element_located((By.ID, "ilosc"))).send_keys(str(ilosc))
        self.driver.find_element(By.CSS_SELECTOR, f"#typ option[value={typ}]").click()
        self.driver.find_element(By.CSS_SELECTOR, "[data-test=wykonaj]").click()
        return self

    def stan(self):
        return self.czekaj.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test=stan]"))).text
