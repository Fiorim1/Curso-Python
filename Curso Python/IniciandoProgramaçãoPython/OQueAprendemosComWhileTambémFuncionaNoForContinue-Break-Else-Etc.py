# Vai de zero a a dez
# i seria as linhas
for i in range (11):
    # Se o número for igual a dois
    if i == 2:
        # Vai imprimir que i é dois
        print("i é 2, pulando...")
        # Vai continuar o progrma
        continue
    # Se cado i for igual a oito
    if i == 8:
        # Vai imprimir que i é oito
        print("i é 8, seu else não executará")
        # Programa vai parar
        break # Não irá chamar o else
    # For interno
    # Onde neste for interno, o j seria colunas
    for j in range(1,3):
        print(i, j)
# Irá ser imprimido o else (pois no for também tem else)
else:
    print("For completo com sucesso")

# Vai de zero a a dez
# i seria as linhas
for i in range (11):
    # Se o número for igual a dois
    if i == 2:
        # Vai imprimir que i é dois
        print("i é 2, pulando...")
        # Vai continuar o progrma
        continue
    # For interno
    # Onde neste for interno, o j seria colunas
    for j in range(1,3):
        print(i, j)
# Irá ser imprimido o else (pois no for também tem else)
else:
    print("For completo com sucesso")