# Desempacotador em chamadas
# de métodos e funções

string = "ABCD"
lista = ["Maria", "Helena", 1, 2, 3, "Eduarda"]
tupla = ("Python", "é", "legal")

# Jogar os três valores da lista dentro deas variáveis a,b,c
# asterístico _ -> resto
p, b, *_, ap, u = lista 
# Acessar os valores da lista pelas variáveis 
print(p, u, ap)

# Pegando cada item da lista e exibindo
for nome in lista:
    print(nome, end=" ", sep=" ") # Deixar tudo em uma linha
# Mesma coisa que o for (mais fácil)
print(*lista)
# Mesma coisa que:
print("Maria", "Helena", 1, 2, 3, "Eduarda")
# Pegar cada item da variável string
print(*string) # Vai separar com espaços em brancos
# Pegar item por item da tupla
print(*tupla)
# Outra lista, com outra lista dentro
salas = [
    #   0         1
    ["Maria", "Helena", ],   # 0
    #    0
    ["Elaine", ],    # 1
    #   0       1         2
    ["Luiz", "João", "Eduarda", ],   # 2
]
# Fazer cada lista um valor
print(*salas)
# Faxer cada lista um valor com espaçamento
print(*salas, end="\n")
# Separar por linha
print(*salas, sep= "\n")