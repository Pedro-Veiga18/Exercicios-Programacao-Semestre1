inicio = int(input("Digite um valor para o ínicio do intervalo: "))
fim = int(input("Digite um valor para o fim do intervalo: "))


quant = 0

for i in range(inicio, fim + 1):
    soma = 0
    for j in range(1, i):
        if i % j == 0:
            soma += j
            
    if i == soma and quant == 0:
        print(f"Os números perfeitos que estão neste intervalo são: {i}", end=" ")
        quant += 1
    elif i == soma:
        print(i, end=" ") 
        

        