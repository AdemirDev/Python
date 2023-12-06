import os

#exemplo 1: obter o diretorio de trabalho atual

"""diretorio_atual = os.getcwd()
print(f"O diretorio atual é : {diretorio_atual}")

#listar os arquivos de um diretorio

diretorio = "A:\Prof. Cassio de Albuquerque\Python III\Ademir Jr"

arquivos = os.listdir(diretorio)

print(f"os arquivo do diretorio sao:")

for arquivo in arquivos:
    if (arquivo == "banco_de_dados"):
     print(arquivos)
else:
    print("arquivo nao encontrado")

    #criar um diretorio

novo_diretorio = "A:\\Prof. Cassio de Albuquerque\\Python III\\Ademir Jr\\aaaaa"

os.mkdir(novo_diretorio)"""

#executar comando no sistema

contador = 0

while contador <10:
    os.system("echo Ola, Mundo")
    contador +=1