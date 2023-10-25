# usuario digita e numeros e o sistema verifica qual e o maior

numero_1 = float(input("Digite o Primeiro Numero: "))
numero_2 = float(input("Digite o Segundo Numero: "))
numero_3 = float(input("Digite o Terceiro Numero: "))



if (numero_1 > numero_2 and numero_1 > numero_3):
    print("O Primeiro Numero Digitado e o Maior!!")

elif (numero_2 > numero_1 and numero_2 > numero_3):
    print("O Segundo Valor Digitado e o Maior ")

else:
    print(" O Terceiro Valor Digitado e Maior")