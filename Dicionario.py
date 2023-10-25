contato = { 
"Nome": " Cassio",
"telefone": 123456,
"email": " ademir@ademir.com",

}
print(contato["Nome"])

contato["endereço"] = " Rua Teste  "

print(contato)

# verificando chaves em dicionarios

if 'endereeço' in contato:
    print(Achei)
else:
    print("Nao tem")


#percorrer dicionario para achar valor da chave nome

for Nome in contato.items():
    print(contato["Nome"])
