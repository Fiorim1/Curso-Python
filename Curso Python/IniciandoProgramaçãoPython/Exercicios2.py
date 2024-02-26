# Faça um porgrama que pergunte a hora pro usuário e, 
# baseando-se no horário descrito, exiba  a saudação
# apropriada. EX. 
# bom dia (0-11), 
# boa tarde (12-17)
# boa noite (18 -23)

#Perguntar a hora
hora = int(input("Por favor insira a hora de agora: "))
if hora >= 0 and hora <= 11:
    print("Bom dia")
elif hora >=12 and hora <= 17:
    print("Boa tarde")
elif hora >= 18 and hora <= 23:
    print("Boa noite")
else: 
    print("Hora errada")