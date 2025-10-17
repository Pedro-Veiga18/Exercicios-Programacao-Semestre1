from math import sqrt #importação da função sqrt(raiz quadrada) da biblioteca math
from math import pow #importação da função pow(potência) da biblioteca math
#Entrada
x = float(input("Informe o valor de x: "))

#Processamento
y = sqrt(1+ ((x**4-1)/(2*x**2))**2) -(x**2)/2 #ou - pow(x,2)/2

#Saída
print(f"y = {y}")

