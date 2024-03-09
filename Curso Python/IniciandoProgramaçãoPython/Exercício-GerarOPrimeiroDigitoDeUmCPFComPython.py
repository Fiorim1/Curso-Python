# Cáculo do primeiro dígito do CPF
# CPF: 746.824.890-70
# Colete a soma dos 9 primeiros dígitos do CPF 
# multiplicando cada um dos valores por uma 
# contagem regressiva começando de 10 
#
# Ex.: 746.824.890-70 (74682489070)
#    10  9  8  7  6  5  4  3  2  
#    7   4  6  8  2  4  8  9  0
#    70  36 48 56 12 20 32 27 0
#
# Somar todos os resultados:
# 70+36+48+56+12+20+32+27+0 = 301
# Multiplicar o resultado anterior por 10 
# 301 " 10 = 3010
# Obter o resto da divisão da conta anteriror por 11
# 3010 % 11 = 7
# Se o resultado anterior for mais que 9:
#   resultado é 0
# contrário disso:
#   resultado é o valor da conta
#
# O primeiro dígito do CPF é 7

# Código para o primeiro dígito
# Adicionar o CPF
cpf = "74682489070"
# Pegar os primeiros nove números do CPF
nove_digitos = cpf[:9] # Usar um fatiamento que vai do zero ao nove (índices)
                       # Nove não é incluido
# Criar um contador regressivo
contador_regressivo_1 = 10 # Vai até o dez
resultado_digito_1 = 0
# Faço um loop for
# Para cada dígito nos nove dígitos
for digito_1 in nove_digitos: # Pegar um número dos noves dígitos 
    # Transformar dígito em int
    # += -> Concatenar
    resultado_digito_1 += int(digito_1) * contador_regressivo_1 # Ele vai pegar cada número (digito_1) e vai multiplicar por menos um índice (contador_regressivo_1)
    contador_regressivo_1-= 1
# Multiplicar o resultado por dez e o resto da divisão (%) por 11
digito_1 = ((resultado_digito_1 * 10) % 11)
digito_1 = digito_1 if digito_1 <= 9 else 0
print(digito_1)

# Calcular o segundo dígito
#
# Cálculo do segundo dígito do CPF
# CPF: 746.824.890-70 (74682489070)
# Colete a soma dos 9 primeiros dígitos do CPF,
# MAIS O PRIMEIRO DÍGITO
# multiplicando cada um dos valores por uma 
# contagem regressiva começando de 11
#
# Ex: 746.824.890-70
# 11    10      9   8   7   6   5   4   3   2 
# 7     4       6   8   2   4   8   9   0   7 -> (Primeiro dígito achado lá em cima)
# 77    40      36  64  14  24  40  36  0   14 
#
# Somar todos os resultados:
# 77+40+36+64+14+24+40+36+0+14 = 363
# Multiplicar o resultado anterior por 10 
# 363 * 10 = 3630
# Obter o resto da divisão da conta anterior por 11 
# 3630 % 11 = 0
# Se o resultado anterior for maior que 9:
#   resultado é 0
# contrário disso:
#   resultado é o valor da conta
# 
# O segundo dígito do CPF é 0

dez_digitos = nove_digitos + str(digito_1) # Concatenar e pssar para string
contador_regressivo_2 = 11
resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2 # Passar o dígito para inteiro
    # Fazer o contador tirar sempre um
    contador_regressivo_2 -= 1
# Realizando a operaão solicitada no problema
digito_2 = (resultado_digito_2 * 10) % 11
# Se o resultado for maior que nove será zero (solicitado no porblema)
digito_2 = digito_2 if digito_2 <= 9 else 0
# Rafazer o CPF
novo_cpf = f"{nove_digitos}{digito_1}{digito_2}"
# Validar o CPF (novo)
if cpf == novo_cpf:
    print(f"{cpf} é válido")
else:
    print("CPF inválido")

# Gerar CPF
# Importar uma biblioteca
import random
nove_digitos = ""
# Fazer um loop para gerar
for i in range(9):
    # Vamos concatenar
    nove_digitos += str(random.randint(0,9)) # Transformar em string
# Gerar 50 CPF
for _ in range(50):
    nove_digitos = ""
    for i in range(9):
        nove_digitos += str(random.randint(0,9))
    

