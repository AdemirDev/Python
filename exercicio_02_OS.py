# Crie uma função que cria um diretório e pergunte ao usuário qual será o nome

import os
def criar_diretorio():
    nome_diretorio = input("Informe um nome para diretorio:")
    novo_diretorio = os.path.join(os.getcwd(), nome_diretorio)

    #Criando um novo diretório

    os.mkdir(novo_diretorio)

    print(f"Diretório '{nome_diretorio}'criado com sucesso!\n")

criar_diretorio()
