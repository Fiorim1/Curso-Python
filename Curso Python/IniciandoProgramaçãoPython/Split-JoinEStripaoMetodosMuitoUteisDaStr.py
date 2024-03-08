# Split e join com list e str
# Split -> divide uma string
# Join -> une uma string

frase = "Olha só que, coisa interessante"
# Separar as palavras (usando espaço em branco)
lista_palavras = frase.split()
# Acessar as palavras (elas vão vim em uma lista)
print(lista_palavras)
# Repitir a frase
frase = "Olha só que, coisa interessante"
# Separar as palavras (até a vírgula (uma parte) e depois da vírgula (em outra parte)) TUDO DENTRO DE UMA LISTA
lista_palavras = frase.split(",")
# Acessar as palavras (elas vão vim em uma lista)
print(lista_palavras) # Lista de frases (duas frases)
# Usar um for, para colocar o índice nas divisão (i = índice, frase = ser as frases)
for i, frase in enumerate(lista_palavras):
    print(lista_palavras[i]) # Vai dar separado em linhas sem ser na lsita (por isso o índice)
    # Imprimir com o número (para aliviar minha dúvida)
    print(f"Índice:{i}: {frase}")
    # Acessar usando o strip (vai cortar do dois lados)
    print(lista_palavras[i].strip()) # Sem espaços no começo e no fim
    # Acessar usando o rstrip ( vai cortar lado da direta)
    print(lista_palavras[i].rstrip())
    # Acessar usado o lstrip (vai cortar o lado da esquerda)
    print(lista_palavras[i].lstrip())
    # Alterar o índice da lista
    lista_palavras[i] = lista_palavras[i].strip() # Corrigir problema do espaço (NÂO FAÇA ISSO NA FORMA SEMÂNTICA)
    # Repitir a frase (opção para eu entender)
    frase = "Olha só que  , coisa interessante"
    # Criar outra lista (DE ACORDO COM A AULA NÃO É PRECISO)
    lista_frases = []
    # Dividir a frase na vírgula com o split
    lista_frases_cruas = frase.split(",")
    for i, frase in enumerate(lista_frases_cruas):
        # Adicionar o índice para usado para remover os espaços em branco ao redor de cada frase após dividir a string na vírgula
        lista_frases.append(lista_frases_cruas[i].strip())
print(lista_frases_cruas)
print(lista_palavras)
# Unir uma string (joim)
frases_unidas = "-".join("abc") # O que quero unir
# Acessar variável frases_unidas
print(frases_unidas)
# Unir lista
frases_unidas = ",".jois(lista_frases)
# Acessar a variável frases_unidas com o jois que uniu elas
print(frases_unidas)

