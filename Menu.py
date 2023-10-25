


def somar( num_1= float (input("Digite o primeiro numero ")),num_2= float (input("Digite o segundo numero "))):    
    
    return print("O Valor da Soma é:"  , (num_1 + num_2))

def subtrair(num_1= float (input("Digite o primeiro numero ")),num_2= float (input("Digite o segundo numero "))):
    return print(num1-num2)

def multiplicar(num_1= float (input("Digite o primeiro numero ")),num_2= float (input("Digite o segundo numero "))):
    return print(num1*num2)

def dividir(num_1= float (input("Digite o primeiro numero ")),num_2= float (input("Digite o segundo numero "))):
    return print(num1/num2)


def menu():
    
    opcao=0
    
    while True:
        #print("Escolha uma opçao: \n")
        print("Opção 1: Somar")
        print("Opção 2: Subtrair")
        print("Opcap 3: Multiplicar")
        print("Opcao 4: Dividir")
        print("Opcao 5: Sair ")

        opcao=input("Escolha uma Opçao: ")

        if opcao== "5":
            print("Saindo da Calculadora")
        

        elif opcao == "1":
            somar() 
        

        elif opcao == "2":
            subtrair()
        

        elif opcao == "3":
            multiplicar()
            

        elif  opcao == "4":
            dividir()          

        


