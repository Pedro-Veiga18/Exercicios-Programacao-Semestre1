#Entrada
binario= int(input("Informe um número em binário com no máximo 4 bits: "))

#Processamento
bit1= binario//1000
bit2= binario//100%10
bit3= binario%100//10
bit4= binario%10

decimal= bit4*1 + bit3*2 + bit2*4 + bit1*8

#Saída
print(f"{binario} em decimal é {decimal}")
