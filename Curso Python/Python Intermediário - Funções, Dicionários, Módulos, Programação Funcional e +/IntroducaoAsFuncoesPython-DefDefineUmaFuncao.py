# Introdução as funções (def) em Python
# Funções são trechos de código usados para 
# replicar determinada ação ao longo do seu código.
# Elas podem receber valores para parâmetros (argumentos)
# e retornar um valor específico.
# Por padrão, funções Python retornam None (nada)

# Funções podem usar parâmetros para receber valores. 
#Parâmetro é o nome da "variável" dentro dos parênteses, 
# argumento é o valor passado para o parâmetro no momento da execução da função.

# EXEMPLO
# Definir uma função (usado para replicar coisas)
def Print(a, b, c): # () --> Parâmetros (OBRIGA)
    print("Várias")
    print("Várias")
    print("Várias")
    print("Várias")
# Chamar a função (chamando apenas uma linha de código)
Print()
Print()
Print()


def imprimir(a, b,c):
    print("Várias")
    print("Várias")
    print("Várias")
    print("Várias")
# Executar a função
imprimir(1, 2, 3) # Para adicionar valores nos parâmetros precio colocar entro os () na hora de executar a função
# Usar valores dos parâmeteos dentro da minha função
def imprimir(a, b,c):
    print(a, b,c )
imprimir(1, 2, 3)
# Consigo mudar parâmetros através da chamada da função 
imprimir(4, 5, 6)

def saudacao(nome):
    print(f"Olá, {nome}!")
saudacao("Gabriel")
# Chamar sem passar o parâmetro
def saudacao(nome="Sem nome"): # --> Se eu não passar valor vai ser esse adicionado no parâmetro
    print(f"Olá, {nome}!")
saudacao()