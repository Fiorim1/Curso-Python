# https://docs.python.org/pt-br/3/libary/stdtypes.html
# Imutáveis que vimos: str (string), int (inteiro), float (número com vírgula),
# bool (verdadeiro[True] ou falso[False]) (OBJETOS)

#         01234567891 (esse último 1 seria o valor 10)
string = "luiz Otávio" 
# Jogando um trecho de cõdigo dentro da string
outra_variavel = f"{string[:3]}ABC{string[4:]}"
# string[3] =  "ABC"  (não tem como mudar)
print(outra_variavel) 
print(string.capitalize())
print(string.upper())
print(string.zfill(100))

