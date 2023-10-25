#crie uma classe pessoa que possui um atributo de classe para manter o numero de pessoas criadas. cada vez que vc insancia um objsto da classe pessoa, o contador deve ser incrementado

class Pessoa:

    total_pessoas =0

    def __init__(self, nome, idade): 
        self.nome = nome
        self.idade = idade
        Pessoa.total_pessoas += 1

    

    

