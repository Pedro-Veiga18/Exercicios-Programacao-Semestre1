n = int(input("informe o valor n maior que zero: "))
y = 0
denominador = 1

if n <= 0:
    print("Valor de n deve ser maior que zero")
else:
    for denominador in range(1, n + 1 ):
        if denominador % 2 != 0:
            y = y + 1 / denominador
        else:
            y = y - 1 / denominador
    print(f"y = {y}")