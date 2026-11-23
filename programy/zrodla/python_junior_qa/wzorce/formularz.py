from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

ADRES = "http://127.0.0.1:5001"

driver = webdriver.Edge()
czekaj = WebDriverWait(driver, 10)
try:
    driver.get(ADRES + "/logowanie")
    czekaj.until(EC.visibility_of_element_located((By.ID, "login"))).send_keys("tester")
    driver.find_element(By.ID, "haslo").send_keys("Test123!")
    driver.find_element(By.CSS_SELECTOR, "[data-test=zaloguj]").click()
    czekaj.until(EC.element_to_be_clickable((By.ID, "dodaj-1"))).click()
    czekaj.until(EC.element_to_be_clickable((By.ID, "do-zamowienia"))).click()
    czekaj.until(EC.visibility_of_element_located((By.ID, "imie"))).send_keys("Anna Nowak")
    driver.find_element(By.ID, "email").send_keys("anna@example.com")
    driver.find_element(By.ID, "kod_pocztowy").send_keys("00-950")
    driver.find_element(By.CSS_SELECTOR, "[data-test=zamawiam]").click()
    print(czekaj.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test=komunikat]"))).text)
finally:
    driver.quit()
