def class_tri():
    if l1 == l2 and l2 == l3:
        print("Triângulo equilátero")
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("Triângulo isósceles")
    else:
        print("Triângulo escaleno")
        
        
        
#entrada de dados        
l1 = int(input("Digite o valor do lado 1: "))
l2 = int(input("Digite o valor do lado 2: "))
l3 = int(input("Digite o valor do lado 3: "))

if l1 > 0 and l2 > 0 and l3 > 0:
    if (l1 < l2 + l3) and (l2 < l1 + l3) and (l3 < l2 + l1):
        class_tri()
    else:
        print("Os valores não formam um triângulo.")
else:
    print("Os valores devem ser inteiros e positivos")