# Calculadora com while

while True:
    numero_1 = input("Digite um número: ")
    numero_2 = input("Digite outro número: ")
    operador = input("Digite o operador (+ - / *): ")

    # Criar uma flag 
    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    # Se acontecer algum erro ele irá para o except
    try:
        # Converter o primeiro número para float
        num_1_float = float(numero_1)
        # Converter o segundo número para float
        num_2_float = float(numero_2)
        # Se Chegar nessas linhas de cima, o valor irá ser True
        numeros_validos = True
    # Aqui no except ele irá permanecer o valor de None da variável (numeros_validos)
    except :
        numeros_validos = None
    
    # Se os números forem None, eles não são válidos.. Irá checar
    if numeros_validos is None:
        print("Um ou ambos os números digitados são inválidos")
        # Voltar para o começo do programa
        continue 
    
    # Operadores permitidos na calculadora 
    operadores_permitidos = "+-/*"

    # Se o operador que o usuário digitou não está entre os operadores permitidos da calculador
    if operador not in operadores_permitidos:
        print("Operador Inválido")
        continue

    # Checar se foi apenas um operador
    if len(operador) > 1:
        print("Digite apenas um operador")
        continue




    # Validar todos os dados
    print("Realizando sua conta. Confira o resultado abaixo")
    if operador == "+":
        print(num_1_float + num_2_float)
    elif operador == "-":
        print(num_1_float - num_2_float)
    elif operador == "/":
        print(num_1_float / num_2_float)
    elif operador == "*":
         print(num_1_float * num_2_float)
    else:
        print("Nunca deveria chegar aqui")
    # Sair do programa
    sair = input("Deseja Sair: [s]im: ")


    # Caso a resposta da variável sair for verdadeira, o programa irá para
    if sair is True:
        break
