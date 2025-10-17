num = int(input("Digite um número inteiro: "))

contador = 0
while contador < 5:
    if num % 3 == 0:
        print(f"{num}", end=" ")
        contador += 1
        
    num += 1