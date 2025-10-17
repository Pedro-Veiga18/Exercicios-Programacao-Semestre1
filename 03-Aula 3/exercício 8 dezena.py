#Entrada
valor0= int(input("Digite um valor de 3 digitos (100-999): "))

#Processamento
valor1= valor0%100
valor2= valor1//10

#Saída 
print(f"A dezena do valor é: {valor2}")
