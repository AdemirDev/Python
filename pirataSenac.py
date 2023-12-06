from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Inicializar o navegador
driver = webdriver.Chrome()

# Abrir o Google
driver.get("https://www.ead.senac.br/")

driver.get("https://www.ead.senac.br/cursos-tecnicos/tecnico-em-meio-ambiente/")

# Localizar a caixa de pesquisa
link = driver.find_element("ng-click","activeMessage()").click()






# Aguardar a página carregar
time.sleep(5)  # Ajuste o tempo conforme necessário





# Mantenha o navegador aberto por mais alguns segundos para visualização
time.sleep(30)  # Ajuste o tempo conforme necessário

# Fechar o navegador
driver.quit()