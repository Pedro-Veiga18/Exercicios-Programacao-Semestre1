from math import sqrt
#Entrada
a = float(input("Valor de a: "))
b = float(input("Valor de b: "))
c = float(input("Valor de c: "))

if a != 0:
    delta = b**2 -4*a*c
    if delta >= 0:
        x1 = (-b + sqrt(delta))/ (2*a)
        x2 = (-b - sqrt(delta)) / (2*a)
        print(f"As raízes da equação são: x1={x1} e x2={x2}")

    else:
        print("O valor de delta não pode ser negativo")
else:
    print("O valor de a não pode ser 0")
    



    

