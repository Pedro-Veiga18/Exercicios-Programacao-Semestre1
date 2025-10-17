valor = int(input("Informe um valor inteiro e positivo: "))
if valor <= 0:
    print("O valor deve ser inteiro e positivo")
else: 
    for cont in range(-valor, valor + 1):
        if  cont != 0 and valor % cont == 0:
            print(f"{cont}")
            
            