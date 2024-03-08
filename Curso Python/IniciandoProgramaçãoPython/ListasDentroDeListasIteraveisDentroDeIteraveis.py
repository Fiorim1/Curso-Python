# Lista de listas 

salas = [
    #   0         1
    ["Maria", "Helena", ], # 0
    #    0
    ["Elaine", ], # 1
    #   0       1         2
    ["Luiz", "João", "Eduarda", (0, 10, 20, 30, 40)] # 2
]

# Acessar lista pelo índice da lista dentra da lista (valor Helena)
print(salas[0][1])
# Acessar o valor João
print(salas[2][1])
# Acessar o 20 
print(salas[2][3][3]) 
# Acessar todas as listas
for sala in salas:
    print(sala)
# Fazer um for para pegar valores da listas
for sala in salas:
    print(f"A sala é {sala}")
    # Seprar os nomes dos alunos
    for aluno in sala:
        # Acessar os alunos (nomes)
        print(aluno)
