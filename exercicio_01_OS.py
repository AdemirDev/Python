import os
#Criar uma função que peça para o usuário digitar o caminho de uma pasta/diretorio e que liste os arquivos de desse diretorio utilizando a biblioteca os:

def listar_arquivos():
    caminho_diretorio = input("Informe o caminho do diretório")
    #Listar os arquivos do diretório passado

    arquivos = os.listdir(caminho_diretorio)

    print("Os Arquivos do diretório passado são:")

    for arquivo in arquivos:
        print(arquivo)
        
  
listar_arquivos ()


