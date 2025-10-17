valor = int(input("Informe um valor inteiro e positivo: "))
for i in range(1, valor +1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()