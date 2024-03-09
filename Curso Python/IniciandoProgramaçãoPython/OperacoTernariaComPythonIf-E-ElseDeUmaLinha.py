# Operação ternária (condicional de uma linha)
# <valor> if <condicao> else <outro valor>

# Condição verdadeira
# print("Valor" if True else "Outro valor")
# condição falsa
# print("Valor" if False else "Outro valor")
condicao = 10 == 10
variavel = "Valor" if condicao else "Outro valor"
print(variavel)
# Outra condição
condicao = 10 == 11
variavel = "Valor" if condicao else "Outro valor"
print(variavel)

digito = 9 # >9
novo_digito = digito if digito<= 9 else 0
print(novo_digito)
novo_digito = 0 if digito > 9 else digito
print(novo_digito)
