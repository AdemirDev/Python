# verificar se o usuario tem obrigaçao de votar ou e facultativo

idade = int(input("Digite sua idade: "))

if (idade >= 16 and idade < 18):
    print("Voto Facultativo")

elif (idade >=18 and idade < 66):
    print("Voto Obrigatorio")

elif (idade > 65):
    print(" Voto Facultativo (idoso)")

else:
    print("Voto nao Permitido")  