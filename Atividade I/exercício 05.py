lado1 = float(input("valor do lado 1: "))
lado2 = float(input("valor do lado 2: "))
lado3 = float(input("valor do lado 3: "))

if lado1 > lado2 and lado1 > lado3:
    a, b, c = lado1, lado2, lado3
elif lado2 > lado1 and lado2 > lado3:
    a, b, c = lado2, lado1, lado3
else:
    a, b, c = lado3, lado1, lado2

if (lado1 < lado2 + lado3) and (lado2 < lado1 + lado3) and (lado3 < lado1 + lado2):
   print("É um triângulo")
else:
    if a ** 2 == b ** 2 + c ** 2:
        print("Seu triângulo é um retângulo")
    elif a ** 2 < b ** 2 + c ** 2:
        print("seu triângulo é um acutângulo")
    elif a ** 2 > b ** 2 + c ** 2:
        print("Seu triângulo é um obtusângulo")
    else:
        print("A conta nao pôde ser feita, pois não é um triângulo")


