# Higer Order Functions 
# Funções de primeira classe

def saudacao(msg):
    return msg

print(saudacao("Bom dia"))

saudacao_2 = saudacao

v = saudacao_2("Bom dia")
print(v)

def saudacao(msg):
    return msg

def executa(funcao, msg):
    return funcao(msg)

saudacao_2 = saudacao 

v = executa(saudacao, "Bom dia")
print(v)

def saudacao(msg, nome):
    return f"{msg}, {nome}"

def executa(funcao, *args):
    return funcao(*args)

v = executa(saudacao, "Bom dia", "Gabriel")
print(v)