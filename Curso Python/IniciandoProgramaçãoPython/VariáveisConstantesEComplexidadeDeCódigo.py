#Constante = "Variáveis" que não vão mudar 
#Muitas condições no mesmo if (ruim)
#      <- Contagem de complexidade (ruim)

velocidade = 61 #velocidade atual do carro 
local_carro = 101 #local em que o carro está na estrada


#Cons em Python se usa com letras maiúsculas (NÃO MUDA)
#Isso serve para documentar que a variável é uma constante
RADAR_1 = 60 #velocidade máxima do radar 1 
LOCAL_1 = 100 #local onde o radar 1 está 
RADAR_RANGE = 1 #a distância onde o radar pega 

velocidade_carro_passou_radar_1 = velocidade > RADAR_1
carro_multado_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)

if velocidade_carro_passou_radar_1 :
    print("Velocidade carro passou do radar 1")

if carro_multado_radar_1 and \
    velocidade_carro_passou_radar_1:
    print("Carro multado em radar 1")

