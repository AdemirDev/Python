import pyautogui
import time

#Aguardar alguns segudos antes de iniciar

time.sleep(5)

"""#Obtenha e imprima as dimensoes da tela

largura, altura = pyautogui.size()
print (f"A largura da tela e: {largura}\n. A altura da tela: {altura}.")

#mover o mouse para coordenadas (x,y) e clique

pyautogui.move(200,200, duration =3)
pyautogui.click()

#digite algo usando o teclado virtual

pyautogui.typewrite("Hello, word!")

#obter e imrpimir a posição atual do mouse

while True:

    x,y = pyautogui.position()
    print(f" Aposição atual do mouse e {x} and {y}.")

#exibir um alerta


pyautogui.alert("este e um alerta!")"""


### abrir programas como o paint

pyautogui.press('winleft')
programa ='Paint'
pyautogui.write(programa)
pyautogui.press('enter')

#aguardar aberturar do programa
time.sleep(2)

#mover cursos para area de desenho

x =600
y =500
pyautogui.move(x,y)

#criar um desenho simples

pyautogui.dragTo(600,600, duration = 1, button ='left')#desenha uma linha simples

pyautogui.dragTo(300,300, duration =1, button ='right') #desenha uma linha simples

#fecha o programa






