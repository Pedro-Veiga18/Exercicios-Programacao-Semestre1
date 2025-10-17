#Entrada
lado1 = int(input("Valor do lado 1: "))
lado2 = int(input("Valor do lado 2: "))
lado3 = int(input("Valor do lado 3: "))

#regra do triângulo
if (lado1 < lado2 + lado3) and (lado2 < lado1 + lado3) and (lado3 < lado1 + lado2):
    print("É um triângulo.")
else:
    print("Não é um triângulo.")