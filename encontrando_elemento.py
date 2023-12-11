#importar biblioteca selenium
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Instanciar um navegador ( Chrome, neste exemplo)

navegador = webdriver.Chrome()

#Navegar para uma URL

navegador.get("https://www.google.com.br/")

try: # Encapsula um código que pode gerar
    time.sleep(2)# aguarda 2 segundos

    #Econtrar um elemento pelo ID
    elemento = navegador.find_element(By.ID,"APjFqb")
   
   #Digita um texto no campo selecionado
    elemento.send_keys("Greve de Metro em São Paulo")

    # Simula a tecla enter
    elemento.send_keys(Keys.RETURN)

    time.sleep(2)# aguarda 2 segundos

except :
    print("Erro")  

finally:
    #Fecha o navegador

    navegador.close()


    



