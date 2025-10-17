from math import sqrt
lista = []

#preenchimento da lista com valores informados via teclado

for _ in range(6):
    lista.append(int(input("Informe um valor inteiro: ")))
    
#impressão dos números primos armazenados
for num in lista:
    total = 0
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            total += 1
            break
    if total == 0:
        print(num, end=" ")