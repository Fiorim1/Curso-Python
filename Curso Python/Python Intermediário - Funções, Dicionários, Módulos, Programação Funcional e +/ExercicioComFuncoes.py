# Exercícios 
# Crie funções que duplicam, triplicam e quadriplicam
# o número recebido como parâmetro

def criar_multiplicador (multiplicador):
    def multiplicar (numero):
        return numero * multiplicador
    return multiplicar # Retornar o valor final

duplicar = criar_multiplicador(2) # Setar valo do multiplicador pela variável
print(duplicar(4)) # O valor que vai ser multiplicado
triplicar = criar_multiplicador(3) # Setar valo do multiplicador pela variável
print(triplicar(12)) # O valor que vai ser multiplicado
quadriplicar = criar_multiplicador(4) # Setar valo do multiplicador pela variável
print(quadriplicar(8)) # O valor que vai ser multiplicado