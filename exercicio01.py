#criar uma automação com pyautogui, pelo qual o programa abre o bloco de notas e digita ums msg e salva.

import pyautogui
import time

# abrir o bloco de notas

pyautogui.press('winleft')
programa ='Bloco'
pyautogui.write(programa)
pyautogui.press('enter')


time.sleep(2)


# escrever uma msg

pyautogui.typewrite("Tentando aprender Python, ainda....")

#salvando a msg automaticamente

pyautogui.hotkey('ctrl', 's')
nome_arquivo = 'aprendi.txt'
pyautogui.write(nome_arquivo)
pyautogui.press('enter')





