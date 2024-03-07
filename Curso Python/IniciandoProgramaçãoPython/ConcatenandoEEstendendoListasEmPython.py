# Listas em Python 
# Tipo list - Mutável 
# Suporta vários valores de qualquer tipo
# Conhecimentos reutilizáveis - índices e fatiamento 
# Métodos úteis:
#   appends - Adiciona um item ao final 
#   insert - Adiciona um item no índice escolhido
#   pop - Remove do final ou do índice escolhido
#   del - apaga um índice 
#   clear - limpa a lista 
#   extend - estende a lista
#   +- - Concatena a lista 
# Create, Read, Update, Delete 
# Criar, ler, alterar, deletar = lista[i] (CRUD)

lista_a = [1,2,3]
lista_b = [4,5,6]
# Juntar essas duas listas numa outra lista (cancatenação)
lista_c = lista_a + lista_b
# Exibir lista C
print(lista_c) # Juntou lista_a + lista_b
# Estender uma lista 
lista_d = lista_a.extend(lista_b)
# Acessar a lista D
print(lista_d) # Resultado vai dar None, onde ele não me entrega o valor de volta, ou seja está mexendo no meu valor da lista A
