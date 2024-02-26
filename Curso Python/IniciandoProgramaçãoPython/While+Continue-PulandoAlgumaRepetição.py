# Repetições 
# while (executa)
# Executa uma ação enquanto uma condição for verdadeira
# Loop infinito -> Quando um código não tem fim 

contador = 0
um = 1

while contador <= 100:
    contador += um #CUIDADO 

    # Ele pula, o trecho pra baixo não foi executado (console)
    if contador == 6:
        print("Não vou mostrar o 6")
        continue # Volta ao começo do laço

    #Ele puça, não mostra
    if contador >= 10 and contador <= 27:
        print("Não vou mostrar o", contador)
        continue


    print(contador) 


    # Termina o laço
    if contador == 40:
        # print(contador)
        break

    


print("Acabou")

