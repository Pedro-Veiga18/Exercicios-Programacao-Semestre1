n = int(input("informe o valor n maior que zero: "))
y = 0
denominador = 1

if n <= 0:
    print("Valor de n deve ser maior que zero")
else:
    while denominador <= n:
        y = y + 1 / denominador
        denominador = denominador + 1
    print(f"y = {y}")