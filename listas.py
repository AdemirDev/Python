"""" Resumindo:
Listas são um coleção dados, que podem ser do mesmo tipo ou de tipo diferentes e
mutável, ou seja, pode ser alterada."""


#criando lista manualmente

minha_lista = [1,2,3,4]

#acessando elementos da lista

minha_lista = [1, 2, 3, 4, 5]
primeiro_elemento = minha_lista[0] # retorna 1
segundo_elemento = minha_lista[1] # retorna 2

#modificando elementos da lista

minha_lista = [1, 2, 3, 4, 5]
minha_lista[2] = 10 # modifica o terceiro elemento para 10

#tamanho da lista

minha_lista = [1, 2, 3, 4, 5]
tamanho = len(minha_lista) # retorna 5

#removendo elementos da lista

minha_lista = [1, 2, 3, 4, 5]
del minha_lista[2] # remove o terceiro elemento (índice 2) da lista
minha_lista.remove(4) # remove o número 4 da lista

#percorrendo uma lista com loop for

minha_lista = [1, 2, 3, 4, 5]
for elemento in minha_lista:
    print(elemento) # imprime cada elemento da lista em uma linha separada

#adicona um elemento ao final da lista

minha_lista = [1, 2, 3]
minha_lista.append(4)
print(minha_lista) # Saída: [1, 2, 3, 4] 

#lista.insert(indice, elemento) - Insere um elemento em uma posição específica da lista

lista = [1, 2, 3]
lista.insert(1, 10)
print(lista) # Saída: [1, 10, 2, 3]


#lista.remove(elemento)

lista = [1, 2, 3, 2]
lista.remove(2)
print(lista) # Saída: [1, 3, 2]

#lista.pop(indice) - Remove e retorna o elemento de uma posição específica da lista:

lista = [1, 2, 3]
elemento = lista.pop(1)
print(elemento) # Saída: 2
print(lista) # Saída: [1, 3]


#lista.index(elemento) - Retorna o índice da primeira ocorrência de um elemento na lista:

lista = [1, 2, 3, 2]
indice = lista.index(2)
print(indice) # Saída: 1

#elemento in lista - Verifica se um elemento está presente na lista:

lista = [1, 2, 3]
existe = 2 in lista
print(existe) # Saída: True

#lista.count(elemento) - Conta o número de ocorrências de um elemento na lista:

lista = [1, 2, 3, 2]
ocorrencias = lista.count(2)
print(ocorrencias) # Saída: 2

#lista.sort() - Ordena os elementos da lista em ordem crescente:

lista = [3, 1, 4, 2]
lista.sort()
print(lista) # Saída: [1, 2, 3, 4]

#lista.reverse() - Inverte a ordem dos elementos da lista:

lista = [1, 2, 3, 4]
lista.reverse()
print(lista) # Saída: [4, 3, 2, 1]