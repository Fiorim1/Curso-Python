# Faça uma lista de compras com listas
# O usuário deve ter a possibilidade de 
#inseirir, apagar, listar valores da sua lista 
# Não permita que o programa quebre com erros 
# de índices inexistentes na lista

# Biblioteca para limpar terminal
import os

# Lista para armazenar
lista = []

while True:
    print("Selecione uma opção")
    opcao = input("[i]nserir [a]pagar [l]ista: ")
    # Inserir item na lista
    if opcao == "i":
        # Limpar o terminal quando a opção for escolhida
        os.system('clear')
        # Pedir para o usuário inserir o valor do produto
        valor = input("Valor: ")
        # Irá adicionar o valor do produto na lista
        lista.append(valor)
    # Apagar item da lista
    elif opcao == "a":
        # Pedir para o usuário escolher um índice (item da lista) para apagar da lista
        # Tranformar a opção do usuário em índice
        indice_str = input("Escolha o índice para apagar: ")
        # Onde neste try iremos converter o indice_str para inteiro (int)
        try: # Serve para lidar com excessão
            # Converter para int
            indice = int(indice_str)
            # Deletar da lista
            del lista[indice]
        # Serve para lidar com excessão
        except TypeError: # Tipo de erro que pode acontecer
            print("Índice não existente")
        except ValueError: # Valor errado
            print("Por favor digite números inteiros")
        except Exception: # Algo que aconteceu
            print("Erro Desconhecido")
    # Listar item na lista
    elif opcao == "l":
        # Limpar terminal
        os.system("clear")
        # Se o tamanho da lista for igual a zero
        if len(lista) == 0:
            print("Nada para listar")
        # Listar com o for (através do índice)
        for i,valor in enumerate(lista): # Só é adicionado o valo para não ser tupla, e o i será os números
            print(i, valor) # Com o i ele vai listar sem ser tupla (direto pelo terminal)
    else:
        print("Por favor, escolha i, a ou l.")