import pyautogui
import time


#função para desenhar esterela

def desenha_estrela(x,y, tamanho):
    pyautogui.click(x,y) #clica no ponto incial do paint


    #calcuoar os pontos da estrela

    pontas = 5
    angulo = 360
    raio_externo = tamanho
    raio_interno = tamanho/2

    for i in range (pontas*2):
        if i % 2 !=0:
            pyautogui.dragRel(raio_interno,0, duration=1)
            #desenha a linha interna
        else:
            pyautogui.dragRel(raio_externo,0, duration=1)
            #desenha a linha externa

            pyautogui.moveRel(0,0)

    #aguardar alguns segundos

    time.sleep(5)

    #corrdenadas do ponto inicial e tamanho da estrela

    x_inicial, y_inicial = 100,100
    tamanho_estrela = 50

    desenha_estrela(10,5,5)


                

