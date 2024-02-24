#Formatação básica de strings 
#s - strings 
#d - int 
#f - float
#.<número de dígitos>f
#x e X - Hexadecimal
#(caractere) (><^) (Quantidade)
#> - esquerda 
#< - direita 
#^ - Centro
# = - Força o número aparecer antes do zero
#Sinal - + ou -
#Ex.: 0>-100,.1f
#Conversion flags - !r !s !a


#Colocar um padding (largura fixa)
variavel = "ABC"
print(f"{variavel}")
print(f"{variavel: >10}") #Esquerda
print(f"{variavel: <10}") #Direita
print(f"{variavel: ^10}") #Centro
print(f"{variavel:$^10}") #Preencher
print(f"{1000.85787583:.2f}") #Casa decimal
print(f"{1000.85787583:,.2f}") #Casa decimal (com vírgula)
print(f"{-1000.85787583:-,.2f}") #Casa decimal (com vírgula), python mostrar o sinal
print(f"{1000.85787583:+,.2f}") #Casa decimal (com vírgula), python mostrar o sinal
print(f"{1000.85787583:0=+10,.1f}") #Fazer o número aparecer antes do zero
print(f"O hexadecimal de 1500 é {1500:08x}") #Hexadecimal minúsculo
print(f"O hexadecimal de 1500 é {1500:08X}") #Hexadecimal maiúsculo


#Outros métodos
print(f"{variavel!r}") #__repr__
print(f"{variavel!s}") #__str__
print(f"{variavel!a}") # __ask__


      

