# Introdução ao desempacotamento + tuples (tuplas)

nomes = ["Maria", "Helena", "Luiz"]
# Fazer um desempacotamento
nome1, nome2, nome3 = nomes
# Acessar nome 1 (Fora da lista)
print(nome1)
# Acessar nome 2 (Fora da lista)
print(nome2)
# Acessar nome 3 (Fora da lista)
print(nome3)
# Mesma coisa que:
nome1, nome2, nome3 = ["Maria", "Helena", "Luiz"]
# Acessar nomes (lista)
print(nomes)
# Pegar apenas o primeiro valor e o segundo
nome1, nome2 = ["Maria", "Helena", "Luiz"]
# Acessar nome 2
print(nome2) # Vai dar erro, pois há muito elementos na lista para poucas variáveis
# Ter mais variáveis que valores
nome1, nome2, nome3, nome4 = ["Maria", "Helena", "Luiz"]
# Acessar nome 2
print(nome2) # Vai dar erro, pois há mais variáveis que elementos na lista
# Pegar só o primeiro valor (da forma correta)
nome1, *_ = ["Maria", "Helena", "Luiz"]
# Acessar nome 1
print(nome1)
# Acessar a lista empacotada dentro da variável (*_)
print(*_) # Indica que não irá ser usada
# Pegar só o segundo valor
_, nome2,*_ = ["Maria", "Helena", "Luiz"]
# Acessar o nome 2
print(nome2)
_, _, nome3 = ["Maria", "Helena", "Luiz"]
# Acessar nome 3
print(nome3)
