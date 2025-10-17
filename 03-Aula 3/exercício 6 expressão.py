import math #importação da biblioteca math

#Entrada
x = float(input("Informe o valor de x: "))

#Processamento
y = math.sqrt(math.cbrt(x-1/2))

#Saída
print(f"y = {y: .3f}")