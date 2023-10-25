# crie uma classe tarefe que representa uma tarefa a ser realizada. a classe deve ter atributos com nome da tarefa, data vencimento, e status (pendende, em adamento e concluida
# implemente medotos para marcar a tarefa como concluida

class Tarefa:

    def __init__(self,nome_tarefa, data_vencimento, status):
        self.nome_tarefa = nome_tarefa
        self.data_vencimento = data_vencimento
        self.status = status

    def verificar_status(self,status):

        if status == 1:
            print("Pendente")
        elif status ==2:
            print("Em Andamento")
        elif status==3:
            print("Concluido")
        else:
            print("Opção invalida")


    def verificar_venciment0(self):
        data_tarefa = input(" Digite a data da tarefa")
        #if self.status == 1 and self.data_vencimento > data_tarefa
           # return f"a tarefa '{self.nome_tarefa}' esta atrasada."
        

