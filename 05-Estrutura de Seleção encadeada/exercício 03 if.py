#Entrada
valor1 = int(input("Valor 1 = "))
valor2 = int(input("Valor 2 = "))
valor3 = int(input("Valor 3 = "))
if valor1 == valor2 or valor1 == valor3 or valor2 == valor3:
    print("Os valores devem ser diferentes.")
else:
    if valor1 < valor2 and valor1 < valor3:
        print(f"{valor1} é o menor")
    elif valor2 < valor3:
        print(f"{valor2} é o menor")
    else: 
        print(f"{valor3} é o menor")