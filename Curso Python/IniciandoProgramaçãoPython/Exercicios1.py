# Faça um programa que peça ao usuário para digitar um número
# inteiro, informe se este número é par ou ímpar. Caso o usuário
# não digite um número inteiro, informe que não é um número inteiro

# Pedir para o usuário digitar um número(
numero = input("Digite um número inteiro: ")

# Aqui foi usado o (isdigit) para ver o número digitado
if numero.isdigit():
    numero = int(numero)
    if numero %2 == 0:
        print(f"O {numero} é par")
    else: 
        print(f"O {numero} é ímpar")
else:
    print("Favor digite um número inteiro")




    
