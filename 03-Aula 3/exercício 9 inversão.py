#Entrada
valor0= int(input("Digite um valor de 3 digitos (100-999): "))

#Processamento:

#Separação
cent= valor0//100
deze= valor0%100//10
uni= valor0%10

#Junção
inv= uni*100 + deze*10 + cent

#Saída 
print(f"O valor {valor0} invertido é: {inv}")