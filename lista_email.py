from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import re
import time

# Configuração do Selenium
navegador = webdriver.Chrome()

# URL da página de contato
url_contato = "http://www.mcce.org.br/newsletter"
navegador.get(url_contato)

# Aguardar alguns segundos para garantir que a página foi carregada completamente
time.sleep(3)

# Extrair o HTML da página
html_pagina = navegador.page_source


# Utilizar expressões regulares para extrair nomes e e-mails
padrao_nome = r"maria"
padra_nome2= r"Deisy"
padrao_email = r"gmail.com"

nomes_encontrados = re.findall(padrao_nome, html_pagina)
nomes_encontrados2 = re.findall(padra_nome2, html_pagina)
emails_encontrados = re.findall(padrao_email, html_pagina)

# Exibir os resultados
print("Nomes encontrados:", nomes_encontrados)
print("E-mails encontrados:", emails_encontrados)
