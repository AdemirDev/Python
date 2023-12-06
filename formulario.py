from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Inicializar o navegador
driver = webdriver.Chrome()

# Abrir o site com o formulário
driver.get("URL_DO_FORMULÁRIO")

# Preencher campos de texto
nome_input = driver.find_element_by_name("nome")
nome_input.send_keys(Keys("Nome do Aluno"))

# Selecionar opções em um seletor
seletor = driver.find_element_by_name("seletor")
seletor.send_keys("Opção desejada")

# Marcar caixas de seleção
checkbox = driver.find_element_by_name("checkbox")
checkbox.click()

# Enviar o formulário
botao_enviar = driver.find_element_by_name("enviar")
botao_enviar.click()

# Fechar o navegador
driver.quit()

