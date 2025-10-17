#Entrada
valor1 = int(input("Valor 1 = "))
valor2 = int(input("Valor 2 = "))
valor3 = int(input("Valor 3 = "))

if valor1 > valor2:
    aux = valor1
    valor1 = valor2
    valor2 = aux
    
if valor1 > valor3:
    aux = valor1
    valor1 = valor3
    valor3 = aux
    
    
    
    
if valor2 > valor3:
    aux = valor2
    valor2 = valor3
    valor3 = aux

