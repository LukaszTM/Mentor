from selenium import webdriver
from selenium.webdriver.common.by import By

ADRES = "http://127.0.0.1:5001"

driver = webdriver.Edge()
try:
    driver.get(ADRES + "/logowanie")
    print("Tytuł:", driver.title)
    driver.find_element(By.ID, "login").send_keys("tester")
    driver.find_element(By.CSS_SELECTOR, "input[name=haslo]").send_keys("Test123!")
    driver.find_element(By.XPATH, "//button[text()='Zaloguj']").click()
    print("Po zalogowaniu:", driver.find_element(By.CSS_SELECTOR, "[data-test=powitanie]").text)
    driver.save_screenshot("po_zalogowaniu.png")
finally:
    driver.quit()
