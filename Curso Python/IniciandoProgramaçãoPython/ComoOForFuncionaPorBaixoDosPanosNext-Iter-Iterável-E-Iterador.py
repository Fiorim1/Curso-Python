# Iterável -> str, range, etc (__iter__)
# Iterador -> quem sabe entregar um valor por vex
# next -> me entregue o p´roximo valor
# iter -> me entregue seu iterador

# Vai me retornar um outro bojeto (entregar um elemento por vez)
texto = iter("Luiz")  # .__iter__()
# Mostra um por vez
print(texto.__next__())
# Chamar no iterator (mesma coisa)
print(next(texto))
# Esgota os valores, imprime um erro 

# for letra in texto
texto = "Luiz" # Interável
# Objeto misterioso
iterador = iter(texto) # Iterador

# Enquanto for verdadeiro
while True: # Laço
    #vai pegar o meu iterator e irá imprimir ele decomposto
    try:
     # Variável criada para puxar o iterador (com next)
     letra = next(iterador)
     # Imprimir o que deve, que vou realizado na variável
     print(letra)
    except StopIteration:
       break


# TUDO A CIMA SE RESUME EM:
for letra in texto:
   print(letra)

