import time

def wait_for_url(browser, url, timeout=40):
    start = time.time()
    while time.time() - start < timeout:
        try:
            browser.get(url)
            if browser.title:
                return True
        except Exception:
            time.sleep(1)
    return False

def test_home(browser):
    assert wait_for_url(browser, 'http://127.0.0.1:8081', timeout=40), 'App não respondeu em 40s'
    assert browser.title == "Dash"
    print("Teste da pagina inicial concluida com sucesso.")
