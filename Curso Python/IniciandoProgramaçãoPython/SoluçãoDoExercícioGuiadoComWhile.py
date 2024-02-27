# Interando strings com while 


#       01234567891 (Esse último 1 é o 10)
nome = "Luiz Otávio"
#        1110987654321
tamanho_nome = len(nome)
# print(nome)
# print(tamanho_nome)
# print(nome[3])


# nova_string = " "
# nova_string += "*L*u*i*z* *O*t*a*v*i*o"

indice = 0
novo_nome = ""
while indice < len(nome):
    # Letra pega o índice um por um
    letra = nome[indice]
    # vai concatenar o nome com a letra
    novo_nome += f"*{letra}*" # vai pegar uma letra e adicionar mais uma letra 
    # Vai somar mais um índice, que irá colocar mais uma letra na string vazia
    indice += 1 # Vai voltar pro While

print(novo_nome)
