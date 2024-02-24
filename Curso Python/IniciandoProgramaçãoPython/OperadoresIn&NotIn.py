#Operadores in e not in
#Strings são iteráveis (navegar item por item)
#0 1 2 3 4 5 
# O t á v i o 
# -6 -5 -4 -3 -2 -1 

#in - entre 
#not in - não está entre

nome = "Otávio"
print(nome[2])
print(nome[0])

print("á" in nome) #Vai retornar true 
print("z" in nome) #Vai retornar False
print(10 * "-")
print("vio" in nome)  # Vai ser True pois é possível encontrar a palavra vio na string Otávio.
print ("zero" in nome) #Vai ser False pois não é possível encontrar a palavra  zero na string Otávio.
print("vio" not in nome) #not in = não está 
print("vio" not in nome) #vai ser False pois a palavra vio está na  string Otávio.

nome= input("Digite seu nome: ")
encontrar = input("Digite o que deseja encontar: ")
if encontrar in nome:
    print(f"{encontrar} está em {nome}")
else: 
    print(f"{encontrar} não está em {nome}")



