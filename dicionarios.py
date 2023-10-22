"""Dicionários em Python são estruturas de dados que permitem armazenar pares
de chave-valor. Cada elemento em um dicionário consiste em uma chave única
e um valor associado a essa chave. Os dicionários são úteis para mapear
informações relacionadas e acessá-las de forma eficiente.
Aqui estão alguns conceitos básicos sobre dicionários em Python:
1.Criação de dicionários:
É possível criar dicionários usando chaves {} e especificando os pares
de chave-valor separados por vírgulas. Por exemplo:

# Criando um dicionário vazio

dicionario_vazio = {}

# Criando um dicionário com elementos
dicionario = {'chave1': valor1, 'chave2': valor2, 'chave3': valor3}

Acesso aos valores de um dicionário:
Os valores de um dicionário podem ser acessados usando a chave correspondente. Por exemplo:

# Acessando um valor específico
valor = dicionario['chave']

Adição e atualização de elementos:
É possível adicionar novos elementos a um dicionário ou atualizar os valores existentes usando a sintaxe dicionario[chave] = valor. Por exemplo:

# Adicionando um novo elemento
dicionario['nova_chave'] = novo_valor

# Atualizando um valor existente
dicionario['chave_existente'] = novo_valor

Remoção de elementos:
Os elementos de um dicionário podem ser removidos usando a palavra-chave del seguida pela chave. Por exemplo:

 Removendo um elemento específico
del dicionario['chave']

# Removendo todos os elementos do dicionário
dicionario.clear()

# Removendo o dicionário por completo
del dicionario

Verificação de existência de chave:
É possível verificar se uma chave existe em um dicionário usando o operador in. Por exemplo:

# Verificando a existência de uma chave
if 'chave' in dicionario:
# Faça algo

Percorrendo um dicionário:
É possível percorrer os elementos de um dicionário usando loops for. Por
padrão, o loop percorrerá as chaves, mas é possível obter os valores
correspondentes usando o método values() ou os pares chave-valor usando
o método items(). Por exemplo:

# Percorrendo as chaves do dicionário
for chave in dicionario:
valor = dicionario[chave]
# Faça algo com a chave e o valor

# Percorrendo os valores do dicionário
for valor in dicionario.values():
# Faça algo com o valor

# Percorrendo os pares chave-valor do dicionário
for chave, valor in dicionario.items():
# Faça algo com a chave e o valor

Esses são apenas alguns conceitos básicos sobre dicionários em Python. Eles
são uma estrutura poderosa e flexível para armazenar e manipular dados.
Você pode """