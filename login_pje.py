from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time

navegador = webdriver.Firefox()

try:
    navegador.get("https://pje.trt2.jus.br/primeirograu/login.seam")
    time.sleep(1)

    caminho_arquivo = 'd:\\PapaCalc\\config.json'
    with open(caminho_arquivo) as f:
        config = json.load(f)

    username = config['username']
    password = config['password']

    # Preenche o usuário e senha na tela de login
    elemento_username = navegador.find_element(By.XPATH, '//*[@id="username"]')
    elemento_username.send_keys(username)

    elemento_password = navegador.find_element(By.XPATH, '//*[@id="password"]')
    elemento_password.send_keys(password)
    time.sleep(1)

    # Clica no botão para fazer login
    navegador.find_element(By.XPATH, '//*[@id="btnEntrar"]').click()
    time.sleep(1)

    # Clica no botão meu painel
    navegador.find_element(By.XPATH, '/html/body/pje-root/mat-sidenav-container/mat-sidenav-content/div/pje-menu-lateral/nav/pje-item-menu-lateral[2]/div/button/span[1]/i').click()
    time.sleep(1)

    # Clica no botão ET para abrir processo
    navegador.find_element(By.XPATH, '/html/body/pje-root/mat-sidenav-container/mat-sidenav-content/div/div/pje-gigs-meu-painel/mat-card[1]/pje-data-table/div[1]/table/tbody/tr[1]/td[1]/div[1]/pje-gigs-abrir-processo/button/span[1]/img').click()
    time.sleep(2)

    # Clica no menu para abrir a opção de baixar documento
    navegador.find_element(By.CSS_SELECTOR, '#botao-menu')
    time.sleep(3)
    navegador.click()


    # Clica em baixar documento
    navegador.find_element(By.XPATH, '/html/body/pje-root/mat-sidenav-container/mat-sidenav-content/div/div/pje-historico/div/pje-resumo-processo/mat-card/section[2]/pje-menu-processo/mat-card/ul/li[5]/pje-baixar-processo/li/button/span[1]/span').click()

except Exception as e:
    print(f"Ocorreu um erro: {e}")
