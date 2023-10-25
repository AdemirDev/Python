import random

numero_aleatorio = random.randint(1,100)
tentativas =0

while True
tentativas = int (input("Adivinhe o numero ( entre 1 e 100): "))
tentativas += 1

if tentativas = numero_aleatorio:
    print(f"Parabens! Voce acertou em {tentativas} tentativas. ")
break
elif tentativa < numero_aleatorio:
    print ("Tente um numero maior ")
else:
    print("Tente um numero menor. ")





