# Listas em Python
# Tipo list - Mutável 
# Suporta vários valores de qualquer tipo
# COnhecimentos reutilizáveis - indices e fatiamento
# Métodos úteis:
#   appends, insert, pop, del, clear, extden, +
# Create Read Update Delete 
# Criar, ler, alterar, apagar = lista[i] (CRUD)

lista = [10, 20, 30, 40]
# Jogar o valor de uma lista dentro de uma variável
numero = lista[2]
# Acessar por indice
print(lista[2])
# Acessar o valor da lista, adiconado numa variável 
print(numero)
# Alterar valor da lista 
lista[2] = 50
# Apagar um valor da lista (del)
del lista[3]
# Acessar a lista com o valor deletado
print(lista)
# Adicionar coisas na lista 
lista.append(60)
# Acessara lista 
print(lista)
# Remover o ultimo elemento da lista 
lista.pop()
# Adicionar coisas na lista 
lista.append(50)
# Acessar lista
print(lista)
# Variável que vai me informar qual elemento da lista remvido (pulado) LEMBRANDO "REMOVIDO" POIS NÃO FOI USADO DEL
ultimo_valor = lista.pop()
# Acessar lista
print(lista, "Removido", ultimo_valor)
# Pular indice 3 
lista.pop(3)

# URGENTE!!! NÃO MEXER EM LISTAS GRANDES COM O POP

