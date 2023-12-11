from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


navegador = webdriver.Chrome()

navegador.get("https://www.anhanguera.com/inscricao?utm_source=google&utm_medium=cpc&utm_term=anhanguera&utm_content=sch-l1_aedu_aon_institucional-exata_perf_inhouse_gads_texto_texto_exata_inscrever_texto_cpa&utm_campaign=google_semadserver_sch-l1_aedu_aon_institucional-exata_perf_inhouse_conversao_valor-cpa_inscrever_cpa&gad_source=1&gclid=EAIaIQobChMIsLqgj7DlggMVzw2tBh1P8QWZEAAYASAAEgK_MfD_BwE&gclsrc=aw.ds")

time.sleep(3)



elemento = WebDriverWait(navegador, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="mainScroll"]/ul/li[3]/label'))
)
elemento.click()
time.sleep(3)

iframe = navegador.find_element(By.XPATH,'//*[@id="mainScroll"]/ul/li[3]/label')
navegador.switch_to.frame(iframe)

elemento.click()

