# criar uma classe aluno com atributos nome idade e notas
#incrementar metodos para calcular media das notas e vefica se o aluno foi aprovado com media igual ou superior a 6

class Aluno:

    def __init__(self, nome, idade, notas):
        self.nome = nome
        self.idade = idade
        self.notas = notas
        


    def calcular_media_notas(self):
        return sum(self.notas) / len(self.notas)
    
    def verificar_aprovaçao(self):
        media = self.calcular_media_notas()
        if media >= 6:
            return f" {self.nome} "
    
    




