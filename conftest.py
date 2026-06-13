import shutil
import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="module")
def browser():
#    chrome_path = (
#        shutil.which("chromium-browser")
#        or shutil.which("chromium")
#        or "/usr/bin/chromium-browser"
#    )
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
#    
#    chrome_options.add_argument("--disable-dev-shm-usage")
#    if chrome_path:
#        chrome_options.binary_location = chrome_path
#
    service = Service(executable_path="/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()
