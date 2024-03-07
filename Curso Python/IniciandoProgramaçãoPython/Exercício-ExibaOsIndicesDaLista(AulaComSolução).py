# Exercício 
# Exiba os índices da lista

lista = ["Maria", "Helena", "Luiz"]
# Adicionar mais um elemento na lista
lista.append("João")
# Gerar índices com o range
indices = range(len(lista)) # Pegar o tamanho da lista
 # Acessar os índices 
print(indices)
# Acessar os elementos com os índices, para isso iremos usar um laço for
for indice in indices :
    print(indice, lista[indice])