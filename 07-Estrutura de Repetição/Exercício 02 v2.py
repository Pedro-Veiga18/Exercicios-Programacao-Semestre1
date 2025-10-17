contador = 1
maior = float("-inf")
while contador <= 15:
    valor = int(input("Valor: "))
    if valor > maior:
        maior = valor
    contador = contador + 1
print(f"Maior valor = {maior}")