import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="module")

def browser():

# 1. Cria as opções de configuração do Chrome
    chrome_options = Options()

# 2. Ativa o modo sem navegador (Headless)
    chrome_options.add_argument("--headless")

# 3. Configurações extras para evitar erros comuns em modo headless
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

# 4. Inicia o driver com as configurações sem navegador
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), 
        options=chrome_options)

    yield driver

    driver.quit()
