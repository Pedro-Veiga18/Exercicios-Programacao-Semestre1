valor = int(input("Valor limite: "))
for i in range(1, valor +1):
    soma_divisor_i = 0
    for j in range(1, i):
        if i % j == 0:
            soma_divisor_i += j
    
    soma_divisor_soma = 0
    for j in range(1, soma_divisor_i):
        if soma_divisor_i % j == 0:
            soma_divisor_soma += j
            
    if i == soma_divisor_soma and i != soma_divisor_i:
        print(f"({i}, {soma_divisor_i})", end=" ")