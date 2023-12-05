from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

navegador = webdriver.Chrome()

navegador.get('http://google.com')

time.sleep(2)

elemento = navegador.find_element(By.ID,'APjFqb')
time.sleep(3)
elemento.send_keys("Guerra em Gaza")
time.sleep(3)
elemento.send_keys(Keys.RETURN)
time.sleep(3)