# Conhecimentos reutilizáveis - índices e fatiamento 
# Métodos úteis:
#   appends - Adiciona um item ao final 
#   insert - Adiciona um item no índice escolhido 
#   pop - Remove do final ou do índice escolhido
#   del - apaga um índice 
#   clear - limpa a lista 
#   extend - estende listas 
#   +- - concatena listas 
# Create Read Update Delete
# Criar, ler, alterar, apagar = lista[i] (CRUD)

#          0   1   2   3
listas = [10, 20, 30, 40]
# Adicionar elemento na lista
listas.append("Gabriel")
# Puxar o último elemento da lista com variável, para fora da lista
nome = listas.pop()
# Acessar lista
print(listas, nome)
# Adicionar mais um elemento na lista
listas.append(75)
# Acessar lista
print(listas)
# Apagar um elemento da lista 
del listas[3]
# Acessar lista com a modificação (del) na lista
print(listas)
# Insirir um elemento no final da lista 
listas.insert(4, 90)
# Insirir um elemento no início da lista 
listas.insert(0, 90)
# Acessar lista 
print(listas) # Assim a lista possui mais elementos
# Limpar a lista 
listas.clear()
# Acessar lista
print(listas) # Assim a lista fica vazia 
# NUNCA MEXER NA LISTA LÁ EM CIMA



