#Fatiamento de strings 
#012345678
#Olá mundo
#-987654321
#Fatiamento [1:f:p] [::]
#Obs.: a função len retorna a quantidade de caracteres da str

variavel = "Olá mundo"
print(variavel [5])
print(variavel[-4])

#Utilizar fatiamento
print(variavel[4:]) #Omitir o fim (ir até o final da string)
print(variavel[4:8]) #Sempre que quiser pegar um a mais
print(variavel[0:5]) #Do zero até o quatro (o cindo não é incluido)
print(variavel[-8:-2]) #Negativo
print(variavel[3]) #Espaço (caracter)

#função len (conta caracter)
print(len(variavel[3])) #Uma só, pois peguei um índice
print(len(variavel)) #Nove (total de caracteres da string)
print(variavel[0:len(variavel):1]) #Ou, print(variavel[0:9:1])
print(variavel[0:9:2]) #Pular de dois em dois 
print(variavel[::-1]) #Inverter
print(variavel[-1:-10:-1]) #Outra forma de inverter



