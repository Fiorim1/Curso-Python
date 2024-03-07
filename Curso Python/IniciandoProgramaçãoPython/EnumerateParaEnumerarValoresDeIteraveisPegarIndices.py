# enumerate - enumera iteráveis (índices)

# Lisca criada
lista = ["Maria", "Helena", "Luiz"]
# enumerar lista
lista_enumerada = enumerate(lista)
# Acessar o enumerate 
print(lista_enumerada) # Interator
# Pegar primeiro valor valor enumerado 
print(next(lista_enumerada)) # Vai virar uma tupla
# Usa o loop for
for item in lista_enumerada: # Acessar o item da lista enumerada usando o for
    print(item) 
# Fazer outro for para pegar o mesmo valor
for item in lista_enumerada:
    print(item) # Vai dar nada, pois já foi pego no primeiro fro (a cima)
# Se eu não tiver lista_enumerada = enumerate(lista).. Posso fazer quantos for eu querer
for item in enumerate(lista):
    print(item)
for item in enumerate(lista):
    print(item)                        # NÃO IRÁ HAVER ERRO
for item in enumerate(lista):
    print(item)
for item in enumerate(lista):
    print(item)
# Caso eu queira converter para uma lista 
lista_enumerada = list(enumerate(lista))
# Acessar lista convertida
print(lista_enumerada)
# Caso eu queira converter para um tupla
lista_enumerada = tuple(enumerate(lista, start=10)) # Começar do 10
# Acessar tupla convertida
print(lista_enumerada)
# Cria uma tupla com índice e valor
# Adicionar algo na lista 
lista.append("Gabriel")
# fazer o desempacotamento com o for 
for item in enumerate(lista):
    # Desempacotamento por número e nome
    numero, nome = item
    # Acessar lista com o desempacotamento realizado
    print(numero, item)
# Outra forma de utilizar 
for tupla_enumerada in enumerate(lista):
    print("FOR da tupl:")
    for valor in tupla_enumerada:
        print(f"\t{valor}") # \t igual o TAb (pula do lado, não linha)
# Fomr a prática, fácil e totalmente rápida
for indice, nome in enumerate(lista):
    print(indice, nome)