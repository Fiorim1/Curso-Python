# Faça um jogo para o usuário adivinhar qual 
# a palavra secreta.
# - Você vai propor uma palavra secreta 
# qualquer vai dar a possibilidade para 
# o usuário digitar apenas uma letra.
# - Quando o usuário digitar uma letra, você 
# vai conferir se a letra digitada está na palavra secreta. 
    # - Se a letra digitada estiver na 
    # palavra secreta; exiba a (Você acertou!! A letra {letra} está na palavra {palavra_secreta}, você acertou na {tentativas} vez");
    # - Se a letra digitada não estiver
    # na palavra secreta exiba ("Você errou").
# Faça a contagem de tentativas do seu usuário e adicione

# Palavra secreta
palavra_secreta = "banana"
# Tentativas irá iniciar com o valor 1, para que posso conhecidir com as tentativas no console
tentativas = 1
# Criar um loop 
while True:
    # Pedir para o usuário digitar uma letra da palavra secreta
    letra = input("Digite uma letra da palavra secreta: ")
    # Se a letra digitada pelo usuário, não estiver na palavra secreta, a tentativa irá aumentar uma
    if letra not in palavra_secreta:
        # Somar mais uma tentativa
        tentativas += 1
    # Se letra estiver na palavra secreta ele irá imprimir que a letra está na palavra secreta
    if letra in palavra_secreta:
        # Imprimir que e letra está na palavra secreta
        print(f"Você acertou!! A letra {letra} está na palavra {palavra_secreta}, você acertou na {tentativas} vez")
        # Parar o loop
        break
    # Se não estiver a letra, irá imprimir que você errou e irá retornar para o inicio
    else:
        print("Você errou..")
        continue
    







    

    