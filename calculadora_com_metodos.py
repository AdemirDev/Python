from exercicio01 import Calculadora

calculadora = Calculadora(0,0)

print("************** Calculadora Python *************** \n")

print("Escolha a Operação Desejada: \n")
print("Opção 1: Somar")
print("Opção 2: Subtrair")
print("Opção 3: Multiplicar")
print("Opção 4: Dividir")
print("Opção 5: Sair")

opcao = int(input())
num_1=0
num_2 =0

if opcao ==1:
    print(f"O Resultado da Soma é: " ,calculadora.somar(num_1,num_2))
elif opcao ==2:
   print(f"O Resultado da Subtração é: " ,calculadora.subtrair(num_1,num_2))
elif opcao == 3:
    print(f"O Resultado da Multiplicação é: " ,calculadora.multiplicar(num_1,num_2))
elif opcao ==4:
    print(f"O Resultado da Divisão é: " ,calculadora.dividir(num_1,num_2))
elif opcao == 5:
    print("Saindo da Calculadora....")
else:
    print("Opção Inválida!!!!")

    
    
