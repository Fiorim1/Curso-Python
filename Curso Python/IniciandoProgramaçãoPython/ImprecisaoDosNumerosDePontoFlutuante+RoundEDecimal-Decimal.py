# Impressão de ponto flutuante 
# Double-precision floating-point format IEEE 754

import decimal # Esse módulo tem uma classe chamada Decimal
numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
# Vai dar o número completo (mas lembrando, que irá ser infinito depois da vírgula)
print(numero_3)
# Vai arredondar
print(f"{numero_3:.2f}")
# Arredondar usando função (forma semântica)
print(round(numero_3, 2)) # Depois da vírgula será o tanto de casas decimais (flutuante)
# Forma mais "difícil", usando um módulo
numero_1 = decimal.Decimal(0.1) # Usando o módulo
numero_2 = decimal.Decimal(0.7) # Usando o módulo
# Se precisar calcular algo que é muito específico usa-se o (import decinmal) IMPORTANTE
numero_1 = decimal.Decimal("0.1") # Usando o módulo
numero_2 = decimal.Decimal("0.7") # Usando o módulo
numero_3 = numero_1 + numero_2
print(numero_3)
print(f"{numero_3:.2f}")
print(round(numero_3, 2))


