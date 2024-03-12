# Escopo de funções em Python 
# Escopo significa o local onde aquele código pode atingir.
# Existe o escopo global e local.
# O escopo global é o escopo onde todo o código é alcançavel.
# O escopo local é o escopo onde apenas nomes do mesmo local
# podem sel alcalçados.

# Definindo a função
def escopo():
    x = 1
    print(x)
# Executar função
escopo() # Código executado
# print(x) vai informar que x não está definido pois está fora da função
# Usar o print(x) dentro da função:
def escopo():
    x = 1
    print(x)
# Executar função
escopo()
# Definir a variável x num escopo externo 
# Má prática de programação
x = 1 # X fora da função
def escopo():
    print(x) # Ele pega o x de cima (fora da função)
# Executra função
escopo()
x = 1
# Função criada (pai)
def escopo():
    # Função dentro (filho) de outra função (pai)
    def outra_funcao():
        print(x) # Puxa o valor do x de fora
    print(x) # Puxa o valor de do x de fora
# Executar função
escopo()
# Não poder acessar coisas de dentro de uma função, dentro de outra função
x = 1                                                       
                        # Escopo é o mundinho da função
def escopo():
    def outra_funcao():
        y = 1 # O y não podeser acessado pela função escopo()
        print(x, y) # O x pode ser acessado
    outra_funcao() # Executar a função filho dentro da do pai
    print(x) # O x pode ser acessado
# Executar função
escopo() # Preciso executar a função pai, onde assim irá ser executado a função filho

x = 1 # Esse não irá ser pego, pois não está dentro do escopo
def escopo():
    x = 10
    
    def outra_funcao():
        y = 2
        print(x, y) # Ele i´ra pegar o valor de x do escopo (10) e o de y da função (2)
    outra_funcao()
    print(x)
# Dar um print antes de executar a função
print(x) # Irá imprimir o valor de x fora do escopo (1)
# Executar a função (pai), para a função (filho) ser executada
escopo()
# Dar print depois de executar a função
print(x) # Irá imprimir o valor de x fora do escopo (1)

x = 10 
def escopo():
    x = 17

    def outra_funcao():
        x = 11
        y = 4
        print(x, y)
    outra_funcao() # Irá imprimir o escopo da função (filho)
    print(x) # Imprimir o x dentro do escopo (pai)
# Executar a função (pai), para a função (filho) ser executada 
escopo() # Irá imprimir o x do escopo (pai)
# Imprimir o x fora do escopo
print(x)

