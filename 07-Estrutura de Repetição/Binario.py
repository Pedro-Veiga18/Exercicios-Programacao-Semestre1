binario = int(input("Valor em binário: "))
aux = binario
decimal = 0
i = 0

while binario > 0:
    digito = binario % 10
    decimal = decimal + digito * 2 ** i
    i += 1
    binario = binario // 10
print(f"{aux} --> {decimal}")