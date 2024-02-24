# Operadores lógicos
# and (e), or (ou), not (não)
# and - Todas as condições precisam ser verdadeiras
# Se qualquer valor for considerado falso, a expressão inteira ser´avaliada naquele  valor.
# São cosiderados falsy
# 0.0.0 '' False
# Também existe o tipo None que é usado ara representar um não valor

entrada = input("[E]ntrar [S]aída")
senha_digitada = input("Senha: ")


senha_permitida = "123456"


# if True:
# ...
if entrada == "E" and senha_digitada == senha_permitida:
    print("Entrou")
elif entrada == "S":
    print("Saiu")
else:
    print("Opção Inválida")


print(True and True) #Verdadeiro
print(True and True and True) #Verdadeiro
print(True and False and True) #Falso, ele para no falso.. Avaliação de curto circuito
print(bool(0)) #Falso
print(bool(" ")) #Verdadeiro
print(True and 0 and True) #0 



