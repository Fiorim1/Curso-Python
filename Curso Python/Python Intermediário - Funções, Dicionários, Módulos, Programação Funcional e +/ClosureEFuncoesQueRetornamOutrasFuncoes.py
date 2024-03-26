# Closure e funções que retornam outras funções

def saudacao (saudacao, nome):
    def saudar():
        return f"{saudacao}, {nome}"
    return saudar()

# Adiar a execução da função (return saudar())
def saudacao (saudacao, nome):
    def saudar():
        return f"{saudacao}, {nome}"
    return saudar 


saudacao1 = saudacao("Bom dia", "Gabriel")
saudacao2 = saudacao("Boa noite", "Gabriel")
print(saudacao1()) 
print(saudacao2()) 

def saudacao (saudacao, nome):
    def saudar(nome): # Aqui vai o nome, que está lá em baixo
        return f"{saudacao}, {nome}"
    return saudar

falar_bom_dia = saudacao("Bom dia")
falar_boa_noite = saudacao("Boa noite")

print(falar_bom_dia("Luiz")) # Adiar Argumentos
print(falar_boa_noite("Luiz")) # Adiar Argumentos

def saudacao(saudacao, nome):
    def saudar(nome):
        return f"{saudacao}, {nome}"
    return saudar

falar_bom_dia = saudacao("Luiz") 
falar_boa_noite = saudacao("Luiz")

for nome in ["Maria", "Pedro", "Jorge", "Paulo", "Carlos"]:
    print(falar_bom_dia(nome)) # Puxar o nome da lista (loop for)
    print(falar_boa_noite(nome)) # Puxar o nome da lista (loop for)