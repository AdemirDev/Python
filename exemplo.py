from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Inicializar o navegador
driver = webdriver.Chrome()

# Abrir o Google
driver.get("https://www.google.com")

# Localizar a caixa de pesquisa
search_box = driver.find_element("name","q")

# Pesquisar pelo tempo em São Paulo
search_box.send_keys("tempo em São Paulo")
search_box.send_keys(Keys.RETURN)

# Aguardar a página carregar
time.sleep(5)  # Ajuste o tempo conforme necessário

# Localizar o elemento com a informação do tempo
weather_element = driver.find_element("id","wob_tm")

# Obter o texto com a temperatura
temperature = weather_element.text

# Mostrar a temperatura na saída
print("A temperatura em São Paulo é:", temperature, "°C")

# Mantenha o navegador aberto por mais alguns segundos para visualização
time.sleep(30)  # Ajuste o tempo conforme necessário

# Fechar o navegador
driver.quit()

