#from cliente import Cliente
cadastro_cliente = {}

class Cadastro():

    def efetua_cadastro(self):
        self.nome= input(" Digite seu nome: ")
        self.endereco= input(" Digite seu endereço ")
        self.email = input ( " Digite seu email. ")
        self.senha= int(input("Digite uma senha de 4 números"))
 
    """def __init__(self, nome, endereco, email, senha):
        self.senha=senha
        super().__init__(nome,endereco, email)"""
       
        
    """ print("Bem vindo")
        print(cadastro_cliente[nome,endereco,email,senha])"""

    def verifica_Cadastro(self):
        print("Você já possui cadastro?")
        print("Digite 'S' para sim e 'N' para não")
        resposta= input("")
        if resposta == "S":
           from login import Login
           login1= Login()
           login1.efetua_login()
        
        if resposta == "N":
            cadastro = Cadastro()
            cadastro.efetua_cadastro()

       
            
      

