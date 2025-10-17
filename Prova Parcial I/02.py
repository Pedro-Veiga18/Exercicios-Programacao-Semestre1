#Entrada
valor1 = int(input("O valor 1 é: "))
valor2 = int(input("O valor 2 é: "))
valor3 = int(input("O valor 3 é: "))

#Valor menor
if valor1 <= valor2 and valor1 <= valor3:
    val_menor = valor1
    
if valor2 <= valor1 and valor2 <= valor3:
    val_menor = valor2
    
if valor3 <= valor1 and valor3 <= valor2:
    val_menor = valor3
    
#Valor maior
if valor1 >= valor2 and valor1 >= valor3:
    val_maior = valor1
    
if valor2 >= valor1 and valor2 >= valor3:
    val_maior = valor2
    
if valor3 >= valor1 and valor3 >= valor2:
    val_maior = valor3
    
diferença = val_maior - val_menor

#Saída
print(f"A diferença entre o maior e o menor valor é: {diferença}")


    