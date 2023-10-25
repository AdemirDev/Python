class Conta:
    def __init__(self, nome, conta, agencia,saldo):
        self.nome=nome
        self.conta=conta
        self.agencia= agencia
        self.saldo=saldo

    def pagamento(self, saldo, valor_aluguel):
       # conta= int(input("Digite o número de sua conta"))
       # agencia= int(input("Digite o número de sua agência"))

        if saldo >= valor_aluguel:
            print("Saldo Insuficiente")
            return False
        
            


