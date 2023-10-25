class Veiculo:
    def __init__(self,nome,marca,modelo,potencia,combustivel, n_passageiros):
        self.nome = nome
        self.marca = marca
        self.modelo = modelo 
        self.potencia = potencia
        self.combustivel = combustivel
        self.n_passageiros = n_passageiros
        

        
#herança da classe veiculo
class Automovel(Veiculo):

    def __init__(self,nome,marca,modelo,potencia,combustivel, n_passageiros,cor):
        self.cor=cor
        super().__init__(nome,marca,modelo,potencia,combustivel, n_passageiros)

    def acelerar():
        print(" O carro acelerou")

class Moto(Automovel,Veiculo):
    print("Ifood")


class Pessoa:
    def __init__(self,nome,sobrenome,endereço):
        self.nome=nome
        self.sobrenome = sobrenome
        self.endereço = endereço

#herança da classe Pessoa
class Aluno(Pessoa):
    def __init__(self, matricula,curso,nome,sobrenome,endereço):
        self.matricula=matricula
        self.curso = curso
        super().__init__(nome, sobrenome, endereço)
   
