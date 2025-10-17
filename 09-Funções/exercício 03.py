def maior():
    maior_v = 0
    if v1 >= v2 and v1 >= v3:
        maior_v = v1
    elif v2 >= v3:
        maior_v = v2
    else:
        maior_v = v3
            
    print(f"O maior valor é: {maior_v}")
        



v1 = int(input("Digite o primeiro valor: "))
v2 = int(input("Digite o segundo valor: "))
v3 = int(input("Digite o terceiro valor: "))

maior()
