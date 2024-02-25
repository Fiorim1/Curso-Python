#Exercício
#Peça ao uusário para digitar seu nome 
#Peça ao usuário para digitar sua idade
#Se o nome e idade forem digitados:
    #Exiba:
        #Seu nome é {nome}
        #Seu nome invertido é {nome_invertido}
        #Se nome contém (ou não) espaços
        #Seu nome tem {n} letras 
        #A primeira letra do seu nome é {letra}
        #A última letra do seu nome é {letra}
#Se nada for digitado em nome ou idade:
    #Exiba: "Desculpe, você deixou campos vazios"

#Pedir para o usuário inserir o nome
nome = input("Digite seu nome: ")
#Pedir para o usuário inserir sua idade
idade = input("Digite sua idade: ")
#Se o {nome} e {idade} forem digitados
if len(nome) and len(idade) or " " in nome:
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome[::-1]}")
    print(f"Seu nome contém {len(nome)} letras")
    print(f"Contém espaços no nome {nome}.")
    print(f"A última letra do nome {nome} é {nome[-1]}")
else: 
    print("Desculpe, vocÊ deixou campos vazios")
