print("#############################################")

numero = int(input(" Digite um Numero: \n"))

numero_par = (numero // 2)

if (numero % 2 == 0):
        print("Este numero e PAR  \n")
else:
        print(" Este numero e IMPAR \n")

print(f"Dentro do Intervalo 1 a {numero} exitem {numero_par} numeros pares e {numero-numero_par} numeros Impares \n")        