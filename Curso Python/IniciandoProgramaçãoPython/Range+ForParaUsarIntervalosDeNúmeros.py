# For + Range 
# range -> range(start, stop, step)

# Criar um range qualquer 
# Quero números de 0 até 10
numeros = range(10) # Se eu passar um só valor é STOP (Pois quero que ele pare ali)
numeros = range(5,11) # Aqui temos um START onde quero que ele inicei e pare (LEMBRANDO QUE: o último número não aprence, então sempre adicione mais um)
numeros = range(5, 10,2) # Aqui temos um STEP onde quero pular de casa (por exemplo, pular de dois em dois)

numeros = range(0, 101)

# Para cada número em números
for numero in numeros:
    print(numero)
