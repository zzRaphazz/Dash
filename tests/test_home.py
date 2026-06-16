import time

def test_home(browser):
    browser.get('http://127.0.0.1:8081')

    time.sleep(50)

    assert browser.title == "Dash"
    
    print("Teste da pagina inicial concluida com sucesso.")
