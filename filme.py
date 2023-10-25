class Filme:
    def __init__(self, nome, genero, classificação, duraçao):
        self.nome = input("Digite o nome do filme" ,nome)
        self.genero=input("Digite o genero do filme", genero)
        self.classificação= input("Digite a classificacao do filme" ,classificação)
        self.duração = input("Digite a duração do filme",duraçao)

class Serie(Filme):
     def __init__(self, nome, genero, classificação, duraçao,temporada):
         self.temporada=temporada
         super().__init__(nome, genero, classificação, duraçao)

class Documentario(Filme):
     def __init__(self, nome, genero, classificação, duraçao, tema):
         self.tema = tema
         super().__init__(nome,genero,classificação,duraçao)