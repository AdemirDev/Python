import random

print("********************SORTEIO ANIMADO ************************** \n")
numero_sorteado = random.randint(1,100)
#print(numero_sorteado)

tentativas =1
while(True):

    palpite = int(input("Digite um Numero (entre 1 e 100) para Tentar Adivinhar: \n"))

    if (palpite < numero_sorteado):
            print("Voce Errou!! Digite um numero Maior \n")
        
    elif (palpite > numero_sorteado):
            print("Voce Errou!!! Digite um numero Menor \n")
        
    else:
            print(f"Parabens, vc Acertou em {tentativas} tentavivas !!!!  \n ")
            break

    tentativas += 1

