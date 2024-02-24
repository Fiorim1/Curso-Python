#Operadores Lógicos 
#and (e), or (ou), not (não)
#or - Qualquer condição verdadeira avalia toda a expressão verdadeira 
#Se qualquer valor for considerado verdadeiro, a expressão inteira será avaliada naquele valor
#São considerados falsy 
#0.0.0 " " False
#Também existe o tipo None que é usado para respresentar um não valor 

entrada = input("[E]ntrar [S]aída: ")
senha_digitada = input("Senha: ")

senha_permitida = "123456"

#Pode se tornar ambigua 
if (entrada == "E" or entrada == "e") and senha_digitada == senha_permitida:
    print("Entrar")
else:
    print("Sair")


#Avaliação de curto circuito
print(True or False) #Verdadeiro, porque a primeira expressão é verdadeira
print(0 or False or 0 or "abc")  #Vai retornar o valor verdadeiro ("abc")
print(0 or False or 0 or "abc" or True) #ele vai parar no "abc", pois é o primeiro valor verdadeiro

senha = input("Senha: ") or "Sem senha"
print(senha)

