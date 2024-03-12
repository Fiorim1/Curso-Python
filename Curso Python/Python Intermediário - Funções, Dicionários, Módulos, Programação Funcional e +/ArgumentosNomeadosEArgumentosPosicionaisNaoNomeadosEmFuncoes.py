
# Argumentos nomeados e não nomeados em funções Python
# Argumento nomeado tem nome com sinal de igual
# Argumento não nomeado recebe apenas o argumento (valor)

def soma(x, y):
    # Definição da função
    print(x + y)

# Vendo a função
print(soma)
# Executar a função (ou seja, passar os parâmetros)
print(soma(1, 2)) # Vai dar None (pois a função por padrão retorna None).. 
                  # Para não retornar None, tem que haver um return

def soma(x, y):
    # Definição da função
    print(f"{x=} e {y=}", "x + y = ",x + y) # O igual puxa do valor lá de baixo

# Valor de baixo
soma(1, 2)
# Argumentos nomeados
# Inverter valores (pois o primeiro da forma default é x e o segundo é y)
soma(y=2, x=3) # Assim estaremos indicando quais parâmeteos (nesse caso letras), vão receber
               # o seu valor sem seguir a ordem

def soma(x, y, z):
    # Definição da função
    print(f"{x=}, {y=} e {z=}", "x + y + z = ", x + y + z) # O igual puxa do valor lá de baixo

# Valor de baixo 
print(1, 2, 3)
# Argumentos nomeados
# Inverter valores (pois o primeiro da forma default é x, o segundo é y e o terceiro é z)
soma(y=2, z=4, x=8) # Assim estaremos indicando quais parâmeteos (nesse caso letras), vão receber
                    # o seu valor sem seguir a ordem
# Mudar o separadaro (sep="")
print(3, 5, 7, sep="-")

# Parâmetro é a variável que vai nos parÊnteses na função (def)
# Argumento ´o valor que iremos colocar no parâmetro



