# args - Argumentos não nomeados 
# * - *args (empacotamento e desempacotamento)
# Lembre-se de desempacotamento

x, y, *resto = 1, 2, 3, 4 # x = 1 (tupla)
                          # y = 2 (tupla)
                          # *resto = 3, 4 (tupla) EMPACOTAMENTO 
                          # Esse *resto irá vir em fomra de lista []
print(x, y, resto)

# Para colocar argumentos irei ter que trocar minha lógica
# def soma(x, y):
#   return x + y

def soma(*args): # Usando *args pois são argumentos não nomeados
    pass # Não irei ter erro 
         # O pass é só para dizer que o escopo não está vazio 
# Sendo assim eu posso mandar um monte de valores, que não irá constra um erro 
soma(1, 2, 3, 4, 5, 6, 7, 8, 9)

def soma (*args):
    print(args) # Não precisa adicionar o *, pois ele serve para informar que 
                # todos os elementos deste escopo, irá ficar ali naquela variável
    print(type(args))           # Irá vir em forma de tupla

soma(1, 2, 3, 4 , 5, 6, 7, 8, 9)

def soma(*args):
    # Mostrar os números adicionados dentro do escopo (ou seja, da função)
    for numero in args:
        print(numero)

soma(1, 2, 3, 4, 5, 6, 7, 8, 9)

# Fazer a soma 
def soma(*args):
    # Criar o acomulador
    total = 0
    for numero in args:
        print("Total", total, numero)
        total += numero
        print("Total", total)
    print(total)

soma(1, 2, 3, 4, 5, 6, 7, 8, 9)

# Usar da forma correta (return)
def soma(*args):
    total = 0
    for numero in args: # Loop for para podermos realizar a conta com um limite
        total += numero # Irá pegar o totol (0) e irá somdar até o loop for acabar (numeros 
                        # adicionados em args que irá para a variável numero no laço for)
    return total # Sendo assim, aqui ele irá retornar o total com a soma dos números
    
# Jogar a soma numa variável
soma_1_2_3 = soma(1, 2, 3) # Dentro desta variável nós chamamos a função (soma) 
                           # e acrescentamos os valores dentro do args, lembrando que o * é
                           # por causa de args receber todos os valores adicionados a função
print(soma_1_2_3) # Imprimir a variável que chama a função para a execução do código

soma_4_5_6 = soma(4, 5, 6) # Dentro desta variável nós chamamos a função (soma) 
                           # e acrescentamos os valores dentro do args, lembrando que o * é
                           # por causa de args receber todos os valores adicionados a função
print(soma_4_5_6) # Imprimir a variável que chama a função para a execução do código

outra_soma = soma(1, 2, 3, 4, 5, 6, 7, 8)

# for numero in args: 
#    total += numero               
# return total
# Tem um negócio no Python que já faz tudo isso 
# Função sum (soma), sem precisar da função
print(sum((1, 2, 3, 4, 5, 6, 7, 8)))

# Colocar o que foi passado para *args dentro de uma variável
numero = (1, 2, 3, 4, 5, 6, 7, 8)
outra_soma = (soma(*numero)) # * desempacotar e empacotar
                             # Aqui ele fex o que a função solicita com os números enviados:
                             # 0 + 1 = 1
                             # 1 + 2 = 3
                             # 3 + 3 = 6
                             # 6 + 4 = 10
                             # 10 + 5 = 15
                             # 15 + 6 = 21
                             # 21 + 7 = 28
                             # 28 + 8 = 36
                             # Retornar o total, ou seja, o valor de total ficou 36
                             # ele vai retornar 36

print(outra_soma)