from selenium import webdriver

driver = webdriver.Chrome()

# Navegar por várias páginas
driver.get("https://www.google.com/")
# Realizar ações na página
# ...

# Navegar para outra página
driver.get("https://www.uol.com.br/")
# Realizar ações na página
# ...

# Capturar screenshots
driver.save_screenshot("screenshot.png")

driver.quit()

