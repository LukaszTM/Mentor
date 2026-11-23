"""Pięć elementów sklepu testowego, każdy trzema sposobami (ID / CSS / XPath)."""
from selenium.webdriver.common.by import By

LOKATORY = {
    "pole loginu": [(By.ID, "login"), (By.CSS_SELECTOR, "#login"), (By.XPATH, "//input[@id='login']")],
    "pole hasła": [(By.ID, "haslo"), (By.CSS_SELECTOR, "input[name=haslo]"), (By.XPATH, "//input[@id='haslo']")],
    "przycisk Zaloguj": [(By.NAME, "login"), (By.CSS_SELECTOR, "[data-test=zaloguj]"), (By.XPATH, "//button[text()='Zaloguj']")],
    "wyszukiwarka": [(By.ID, "szukaj"), (By.CSS_SELECTOR, "#szukaj"), (By.XPATH, "//input[@id='szukaj']")],
    "suma koszyka": [(By.ID, "koszyk"), (By.CSS_SELECTOR, "[data-test=suma]"), (By.XPATH, "//p[@data-test='suma']")],
}

if __name__ == "__main__":
    from selenium import webdriver
    driver = webdriver.Edge()
    try:
        driver.get("http://127.0.0.1:5001/logowanie")
        for nazwa, sposoby in list(LOKATORY.items())[:3]:
            for by, wartosc in sposoby:
                print(nazwa, by, wartosc, "→", len(driver.find_elements(by, wartosc)), "element(y)")
    finally:
        driver.quit()
