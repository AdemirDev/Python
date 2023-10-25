# definindo uma funçao

#paramento e o nome da variavel
#argumento e o valor da variavel

def saudacao(nome, sobrenome):
    print(f"minha saudaçao......{nome} {sobrenome}")

#chamando a funcao saudacao
saudacao("Ademir", "Junior")


def custo_mercadoria_vendida(estoque_inicial, estoque_final, compras):
    cmv= estoque_final+compras - estoque_inicial
    print(" O estoque atual é de : " , cmv)

    def valor_compras_periodo(estoque_inicial, estoque_final):
        valor_compras_periodo = estoque_final-estoque_inicial
        print("O valor compras: ", valor_compras_periodo)


    
    