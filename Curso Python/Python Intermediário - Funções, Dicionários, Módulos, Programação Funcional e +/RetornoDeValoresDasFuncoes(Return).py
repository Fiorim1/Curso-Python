# Retorno de valores das funções (return)
# Sempre que você executa algo com alguma função, essa função tem que retorna determinado valor 
# (return)

x = 1

def escopo():
    # global x
    x = 10 

    def outra_funcao():
        # global x 
        x = 11
        y = 2
        print(x, y) # Sefundo a ser imprimido

    outra_funcao() # Segundo a ser executado

    print(x) # Teceiro a ser imprimido

print(x) # Primeiro a ser imprimido
escopo() # Segundo a ser executado 
print(x) # Quarto a ser executado


def soma(x, y):
    ...
variavel = soma(1,2)
print(variavel) # Vai imprimir None, pois não retornei absolutamente NADA

def soma(x, y):
    print(x + y)


soma_1 = soma(2, 2)
soma_2 = soma(3, 3)
print(soma_1 + soma_2)

def soma(x, y):
    # Com o retunn (ou seja, retornando), é que o valor x + y pode ir para qualquer lugar (móvel)
    return x + y
soma_1 = soma(2,2)
soma_2 = soma(4, 4)
print(soma_1 + soma_2) # Consigo realizar a operação sem dar o tipo None, devido ao return

def letra(x, y):
    # ESSES PRINT NÃO SÃO VALORES DO X E DO Y 
    # ELES SERÃO EXECUTADOS JUNTO COM O VALOR ADICIONADO A X E Y
    print("Olá")
    print("Meu")
    print("Melhor")
    print("Amigo")
    return x + y

soma_1 = letra(2, 2)
soma_2 = letra(3, 2)
print(soma_1 + soma_2)

def soma(x, y):
    if x > 10:
                        # Um único return por def (função)
                        # Assim que executada ela para a função TODA
        return 10, 20 # Vai me retornar uma tupla ()
    return x + y

soma_1 = soma(2, 2)
soma_2 = soma(3, 3)
print(soma_1)
print(soma_2)
print(soma_1 + soma_2)
