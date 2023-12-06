from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://accounts.google.com/signin/v2/challenge/pwd?continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=1&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&osid=1&passive=1209600&service=mail&ifkv=AXo7B7XEJ8_is-UCIlvAdszZc-6DvjQ5zPFdb12Q1Fln2aTjzHeReVJGF8M8B_BWu4ALbtj_XpfAdA&flowName=GlifWebSignIn&flowEntry=ServiceLogin&cid=1&navigationDirection=forward&TL=AGEVcSRwwTdea72ucQbvf3UCP8_Ry7U_8ZWLp5OS5hnZZAC__7b4rUpKO5v75lyZ")

# Preencher campos de login
username = driver.find_element("jsname","YPqjbf")
username.send_keys("cassio.matematica@gmail.com")
username = driver.find_element("class","VfPpkd-RLmnJb").click()


password = driver.find_element("jsname","YPqjbf")
password.send_keys("senha")
password = driver.find_element("class","VfPpkd-RLmnJb").click()

# Fazer login
login_button = driver.find_element("login_button")
login_button.click()

driver.quit()
