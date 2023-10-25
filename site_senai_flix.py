from filmes_series import Filme, Serie, Documentario
from cliente import Cliente
from login import Login
from conta import Conta
from cadastro import Cadastro

print("#################################")
print("     Bem vindo a SenaiFlix       ")
print("#################################")


#Chama a classe login e seu método para efetuar login

clientes = {}

while True:
    print(" Escolha uma opção: ")
    print(" Opção 1. Alugar um Filme ")
    print(" Opção 2. Alugar uma série ")
    print(" Opção 3. Alugar um Documentário ")
    print(" Opção 4. Sair. ")

    opcao = input("")

    if opcao == "4":
        break

    if opcao == "1":
        cadastro = Cadastro()
        cadastro_cliente = cadastro.verifica_Cadastro()
        
        login = Login()
        cliente_logado= login.efetua_login(cadastro_cliente['email'], cadastro_cliente['senha'])

        if cliente_logado:
            valor_aluguel_filme= 10
            if cliente_logado.conta.pagamento(valor_aluguel_filme):
                print("Filme Alugado com sucesso.")
            else:
                print("Não foi possível efetuar a locação.")

    #if opcao == "2":
      




   
            



