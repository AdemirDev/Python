"""Exercício logar no e-mail 
utilizando Selenium"""

#Importa as bibliotecas
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Instancia um navegador
options = webdriver.ChromeOptions()
options.add_argument('--disable-web-security')
navegador = webdriver.Chrome(options=options)

#Digita e busca a URL
navegador.get("http://gmail.com")
time.sleep(2)

#Encontrar um elemento pela classe
elemento = navegador.find_element(By.ID,"identifierId")
elemento.send_keys("cassio.matematica@gmail.com")
time.sleep(2)
elemento.send_keys(Keys.RETURN)
elemento = navegador.find_element(By.CLASS_NAME,"VfPpkd-vQzf8d")
time.sleep(2)
elemento.send_keys(Keys.RETURN)


