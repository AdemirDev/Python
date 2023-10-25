#Criar uma classe Calculadora que possui metodos para adicionar, subtrair, multiplicar e dividir dois numeros

class Calculadora:

    #definindo os parametros da calculadora

    def __init__(self,num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    # criando os metodos da calculadora

    def somar(self, num_1, num_2):
        num_1 = float(input("Digite o Primeiro Numero: "))
        num_2 = float(input("Digite o Segundo Numero: "))
        return num_1+num_2
    
    def subtrair(self, num_1, num_2):
        num_1 = float(input("Digite o Primeiro Numero: "))
        num_2 = float(input("Digite o Segundo Numero: "))
        return num_1 - num_2
    
    def multiplicar(self, num_1, num_2):
        num_1 = float(input("Digite o Primeiro Numero: "))
        num_2 = float(input("Digite o Segundo Numero: "))
        return num_1 * num_2
    
    def dividir(self, num_1, num_2):
        num_1 = float(input("Digite o Primeiro Numero: "))
        num_2 = float(input("Digite o Segundo Numero: "))

        if num_2 == 0:
            num_1 = float(input("Digite o Primeiro Numero: "))
            num_2 = float(input("Digite o Segundo Numero: "))
            print(" Não é possivel divider por 0 ")
        else:
            return num_1 / num_2



        