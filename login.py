
class Login():
    """def __init__(self, email, senha):
        self.email=email
        self.senha=senha"""
    
    def efetua_login(self, email, senha):
        from cadastro import Cadastro
        cadastro = Cadastro()

        self.email= input("Digite seu email")
        self.senha= input("Digite usa senha")

        if ( self.email == cadastro.email):
                if(self.senha == cadastro.senha):
                    print("Login Efetuado com Sucesso")
                else:
                    print("E-mail ou Senha Invalidos.")