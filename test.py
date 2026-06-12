import shutil
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def test_paginas():
    chrome_path = (
        shutil.which("chromium-browser")
        or shutil.which("chromium")
        or "/usr/bin/chromium-browser"
    )

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    if chrome_path:
        chrome_options.binary_location = chrome_path

    service = Service(executable_path="/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        url = "http://127.0.0.1:8080"

        driver.get(url)
        time.sleep(2)
        assert "Dash" in driver.title
        assert "pagina inicial" in driver.page_source

        driver.get(url + "/formulario")
        time.sleep(2)
        assert "Dash" in driver.title
        assert "For" in driver.page_source

        driver.get(url + "/graficos")
        time.sleep(2)
        assert "Dash" in driver.title
        assert "Gráficos" in driver.page_source
    finally:
        driver.quit()