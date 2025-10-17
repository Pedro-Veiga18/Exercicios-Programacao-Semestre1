from math import sqrt

#Entrada
x = float(input("O valor de x é: "))

#Processamento
if x > 5 or x < -5:
    y = (x-8) / sqrt((x**2)-25)
    print(f"O valor de y é: {y: .2f}")
else:
    print("O valor de x é inválido.")