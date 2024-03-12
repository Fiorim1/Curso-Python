# Valores padrão para parâmetros
# Ao definir uma função, os parâmetros podem
# ter valores. Caso o valor não seja 
# enviado para o parâmetro, o valor padrão será 
# usado.

def soma(x, y):
    print(x + y)

soma(1, 3)
soma(3, 6)
soma(230, 475)

# Refatorar o código, ou seja, editar seu código
def soma(x, y, z=0): # z irá ter um valor padrão
    if z:
        print(f"{x=}, {y=}, {z=}", x + y + z)
    else:
        print(f"{x=}, {y=}", x + y)

soma(1, 3)
soma(3, 6)
soma(230, 475)
soma(230, 475, 0) # O zero é um falsy number (vai gerar um transtorno)

def soma(x, y, z=None): # None é um valor falsy
    if z:
        print(f"{x=}, {y=}, {z=}", x + y + z)
    else:
        print(f"{x=}, {y=}", x + y)

soma(1, 3)
soma(3, 6)
soma(230, 475)
soma(230, 475, 0) # O zero é um falsy number (vai gerar um transtorno)

# Saber se o z é None
def soma(x, y, z=0): # z irá ter um valor padrão
    if z is not None: # Se z não for None, mostra o Z
        print(f"{x=}, {y=}, {z=}", x + y + z)
    else:
        print(f"{x=}, {y=}", x + y)

soma(1, 3)
soma(3, 6)
soma(230, 475)
soma(230, 475, 0) # O zero é um falsy number (vai gerar um transtorno)
soma(z=0, x=46, y=77) # Mandar em fora de ordem

# Toda vez que um parâmetro (com valor definido padrão na def), todos que vierem
def soma(x, z=None, y=None): # z irá ter um valor padrão e o y que veio após ele, também irá
                       # ter um valor padrão
    if z is not None: # Se z não for None, mostra o Z
        print(f"{x=}, {y=}, {z=}", x + y + z)
    else:
        print(f"{x=}, {y=}", x + y)

soma(1, 3) # Nãio vai funcionar pois o y não tem valor aqui
soma(3, 6) # Nãio vai funcionar pois o y não tem valor aqui
soma(230, 475) # Nãio vai funcionar pois o y não tem valor aqui
soma(230, 475, 0) 
soma(z=0, x=46, y=77) 