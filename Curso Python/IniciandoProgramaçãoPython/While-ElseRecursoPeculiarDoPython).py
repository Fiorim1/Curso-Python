# while / else 


string = "Valor Qualquer"
i = 0


#Imprimindo as letras na tela
while i < len(string) :
    letra = string[i]

    if letra == " ":
        break


    print(letra)

    i += 1 

else:
    print("Não encontrei um espaço na string")
print("Fora do while")