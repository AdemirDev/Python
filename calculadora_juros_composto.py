valor_investido_mensal= float(input("Digite o valor a ser Investido Mensalmente: \n"))
tempo_investimento = int(input("Digite quantos Meses o Valor ficará Investido: \n"))
taxa_anual=float(input("Digite Estimativa do valor da Taxa Anual de Rendimento: \n"))
contagem_mes=1
calcula_mes=0

while tempo_investimento >= contagem_mes:

    calcula_mes = (valor_investido_mensal* contagem_mes) * (((taxa_anual/12)/100)+1)
    print(f"Valor Total com o Rendimento: ", "Mês",{contagem_mes}, calcula_mes)
    calcula_mes = calcula_mes * contagem_mes
    contagem_mes+=1
    



