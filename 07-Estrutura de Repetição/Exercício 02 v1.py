contador = 1
maior = 0
while contador <= 15:
    valor = int(input("Valor: "))
    if contador == 1 or valor > maior:
        maior = valor
    contador = contador + 1
print(f"Maior valor = {maior}")

