# Frase/palavra a ser decomposta 
texto = "Python"

# Indice 
i = 0 

# Tamanho da string é X 
tamanho_string = len(texto)

# Loop para decompor a string
while i < tamanho_string :
    print(texto[i], i) # Pegar a palavra letra por letra, e o número do indice

    # Somar sempre mais um do indice 
    i += 1


senha_salva = "123456"
# A senha digitada vai se iniciar vazia, pois no loop (while), eu irá digitá-la até o usuário acertar a senha correta ]
senha_digitada = ""
repeticoes = 0


# Enquanto a senha salva ("123456") for diferente da senha digtada pelo usuário 
while senha_salva != senha_digitada :
    # Vai ser solicitado ao usuário para digitar a senha, e será imprimido  quantas vezes ele tentou acertar
    senha_digitada = input(f"Sua senha ({repeticoes}X):")
    # Aqui irá somar mais um, cada tentaiva que ele errar a senha
    repeticoes += 1

# Print que vai sar  os dados finais do usuario 
print("Você acertou a senha do sistema")

# FOR
texto = "python"

novo_texto = ""
# Para cada (for) letra (variável) em (in) texto (outra variável)
for letra in texto: # Passar por for a variável (podemos acessar pelo interador a string)
    novo_texto += f"*{letra}"
    # Fazer uma interação 
    print(letra)
# Vai ser interador os * em cada letra (o upper siginifica deixar todas as letras maiúsculas)
print(novo_texto.upper())




