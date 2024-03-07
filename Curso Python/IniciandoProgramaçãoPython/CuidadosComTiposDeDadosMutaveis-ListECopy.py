# cuidados com dados mutáveis
# = - copiando o valor (imutáveis)
# = - aponta para o mesmo valor na memória (mutável)

nome = "Gabriel" # Tem um Id
outra_variavel = nome
nome = "João" # Tem outro Id
# Acessar nome atualizado
print(nome)
# Acessar o nome da primeira vez
print(outra_variavel)
#              0          1
lista_a = ["Gabriel", "Maria"]
# Fazer as duas listas apontarem para um mesmo valor na memória
lista_b = lista_a # TOMAR CUIDADO
# Acessar lista A
print(lista_a)
# Acessar lista B
print(lista_b)
# Adicionar um elemento 
lista_a.append("Pedro")
# Acessar a lista A
print(lista_a)
# Acessar lista B
print(lista_b)
# Mudar um valor da lista 
lista_a[0] = "Cleitinho"
# Acessar lista A
print(lista_a)
# Acessar lista B
print(lista_b)
# Copiar uma lista para outra variável (aí ele irá criar OUTRA LISTA mas com os mesmos valores)
lista_c = lista_a.copy()
# Acessar lista C
print(lista_c)

