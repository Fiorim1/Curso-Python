# Tipo tupla - Uma lista imutável 

# Lista criada
nomes = ["Maria", "Helena", "Luiz"]
# Alterando um valor da lista (através do índice)
nomes[1] = "Gabriel"
# Acessando a lista
print(nomes)
# Tupla é mais eficiente (tupla não muda)
nomes = ("Maria", "Helan", "Luiz") # Não pode mudar valores
print(nomes)
# Acessar valores da tupla pelo índice
print(nomes[-1]) # Pegar o último valor
# Transformar uma lista em tuplas
nomes = ["Maria", "Helena", "Luiz"]
# Acessar a lista
print(nomes) # Acessando antes da troca
# Converter para tupla
nomes = tuple(nomes)
# Acessando a troca 
print(nomes)
# Transformar uma tupla em lista
nomes = ("Maria", "Helena", "Luiz")
# Acessar tupla
print(nomes) # Acessando antes da troca
# Convertendo para lista 
nomes = list(nomes)
# Acessando a troca
print(nomes)