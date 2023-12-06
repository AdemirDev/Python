#criar uma automação com pyautogui, pelo qual o programa abre o bloco de notas e digita ums msg e salva.

import pyautogui
import time

# abrir o bloco de notas

pyautogui.press('winleft')
programa ='Bloco'
pyautogui.write(programa)
pyautogui.press('enter')


time.sleep(1)


# escrever uma msg

pyautogui.typewrite("Devagar e sempre!!!....")

pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')


pyautogui.press('winleft')
programa ='Bloco'
pyautogui.write(programa)
pyautogui.press('enter')

pyautogui.hotkey('ctrl', 'v')

time.sleep(1)

pyautogui.hotkey('ctrl', 's')

time.sleep(2)

pyautogui.hotkey('ctrl', 's')
nome_arquivo = 'teste2.txt'
pyautogui.write(nome_arquivo)
pyautogui.press('enter')


