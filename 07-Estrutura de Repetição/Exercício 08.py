valor = int(input("Informe um valor inteiro e positivo: "))
total_divis = 0
if valor <= 0:
    print("O valor deve ser inteiro e positivo")
else: 
    for cont in range(1, valor + 1):
        if valor % cont == 0:
            total_divis += 1
    if total_divis == 2:
        print(f"O número {valor} é primo")
    else:
        print(f"O número {valor} não é primo")
            