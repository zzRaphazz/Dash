import pytest
import time
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="module")

def browser():
   chrome_options = Options()
   chrome_options.add_argument('--headless')
   chrome_options.add_argument('--disable-gpu')
   chrome_options.add_argument('--no-sandbox')
   chrome_options.add_argument('--disable-dev-shm-usage')
   chrome_options.binary_location = '/usr/bin/chromium'

   service = Service('/usr/bin/chromedriver')
   driver = webdriver.Chrome(service=service, options=chrome_options)
   
   yield driver
   
   driver.quit()
