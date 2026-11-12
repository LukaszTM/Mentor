# -*- coding: utf-8 -*-
"""Test Selenium z prawdziwą przeglądarką (headless): python selenium_test.py edge|chrome <sciezka_exe> <plik.html>
Wypisuje tytuł otwartej strony; każdy błąd (sterownik, wersja, brak przeglądarki) kończy się kodem != 0."""
import sys
from pathlib import Path

nazwa, exe, html = sys.argv[1], sys.argv[2], Path(sys.argv[3]).resolve()
from selenium import webdriver  # noqa: E402

if nazwa == "edge":
    opts = webdriver.EdgeOptions()
    opts.binary_location = exe
    opts.add_argument("--headless=new")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--no-sandbox")
    driver = webdriver.Edge(options=opts)
else:
    opts = webdriver.ChromeOptions()
    opts.binary_location = exe
    opts.add_argument("--headless=new")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=opts)
try:
    driver.set_page_load_timeout(30)
    driver.get(html.as_uri())
    tytul = driver.title
    naglowek = driver.find_element("tag name", "h1").text if driver.find_elements("tag name", "h1") else ""
    print(f"OK: {nazwa} otworzył {html.name} — tytuł „{tytul}”" + (f", nagłówek „{naglowek}”" if naglowek else ""))
finally:
    driver.quit()
