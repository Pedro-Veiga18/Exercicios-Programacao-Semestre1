valor1 = int(input("Informe um valor inteiro e positivo para iniciar: "))
valor2 = int(input("Informe um valor inteiro e positivo para terminar: "))
for i in range(valor1, valor2 + 1):
    total_divisores = 0
    for j in range(1, i +1):
        if i % j == 0:
            total_divisores += 1
    if total_divisores == 2:
        print(i, end=" ")