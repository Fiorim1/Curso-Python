# Listas em Python
# Tipo list - Mutável 
# Suporta vários valores de qualquer tipo
# Conhecimento reutilizáveis - íncides e fatiamento
# Métodos úteis: append, insert, pop, del, clear, extend, +

#              01234 (indices positivos)
#             -54321 (indices negativos)

# Cadeia de caracter
string = "ABCDE" # 5 caracteres (len)
# Criar um pacote de nomes de pessoas
# Usar uma list (array)
#         0     1       2       3    4
lista = [123, True, "Gabriel", 1.2, []] 
#        -5    -4      -3      -2   -1
# print(lista, type(lista))
#print(bool(lista)) (Se a letra estiver vazia ela é False)
print(lista)
# Acessar elemto por indice
print(lista[2].upper(), type(lista[2]))
# Alterar valores da lista
lista[-3] = "Fiorim"
# Imprimir o valor mudado
print(lista[2])
# Imprimir a lista inteira com a lateração já inclusa
print(lista)



