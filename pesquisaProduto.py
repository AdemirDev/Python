from selenium import webdriver

driver = webdriver.Chrome()

driver.get("URL_DO_SITE")

# Realizar pesquisa
search_box = driver.find_element_by_name("search")
search_box.send_keys("produto desejado")
search_box.submit()

# Adicionar ao carrinho
add_to_cart_button = driver.find_element_by_class_name("add-to-cart")
add_to_cart_button.click()

driver.quit()
