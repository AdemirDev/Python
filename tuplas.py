#As tuplas são criadas utilizando parênteses ou, opcionalmente, sem parênteses, separando os elementos por vírgulas. Por exemplo:
minha_tupla = (1, 2, 3, 4, 5)
outra_tupla = 1, 2, 3 # também é uma tupla válida

#acessando eloementos da tupla

minha_tupla = (1, 2, 3, 4, 5)
primeiro_elemento = minha_tupla[0] # retorna 1
segundo_elemento = minha_tupla[1] # retorna 2

# tamanho da tupla

minha_lista = (1, 2, 3, 4, 5)
tamanho = len(minha_lista) # retorna 5

"""Desempacotamento de tuplas:
É possível atribuir os elementos de uma tupla a variáveis individuais em um processo
chamado desempacotamento. Por exemplo: """

minha_tupla = (1, 2, 3)
a, b, c = minha_tupla
print(a) # imprime 1
print(b) # imprime 2
print(c) # imprime 3

