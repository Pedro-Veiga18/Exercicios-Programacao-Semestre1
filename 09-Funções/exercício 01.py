def divisor():
    for i in range(1, valor + 1):
        if valor % i == 0:
            print(f"{i}", end=" ")

            

valor = int(input("Digite um valor inteiro e positivo: "))
if valor > 0:
    print(f"Os divisores de {valor} são: ")
    divisor()
else:
    print("O valor deve ser inteiro e positivo.") 


