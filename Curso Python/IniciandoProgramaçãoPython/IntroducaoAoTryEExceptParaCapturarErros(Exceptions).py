#Introdução ao try/except
#try --> tentar executar o código
#except --> ocorreu algum erro ao tentar executar


# print("123")
# print("456")
# float("a") 

numero_str = input("Vou dobrar o número que você digitar: ")
print(numero_str.isdigit())
# if numero_str.isdigit(): #Checar condição e muda o fluxo 
#     numero_float = float(numero_str)
#     print(f"O dobro de {numero_str} é {numero_float * 2:.2f}") 
# else:
#     print(":(")

try:
    print("STR:", numero_str)
    numero_float = float(numero_str)
    print("FLOAT:", numero_float)
    print(f"O dobro de {numero_str} é {numero_float * 2:.2f}") 

except:
   print("Isso não é um número")

