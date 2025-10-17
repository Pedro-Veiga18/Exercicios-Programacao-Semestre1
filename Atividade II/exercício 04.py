v1 = 1
v2 = 2

soma_par = 0

while v2 <= 4000000:
    if v2 % 2 == 0:
        soma_par += v2
        
    v1, v2 = v2, v1 + v2
    
print(f"A soma dos termos de valor par encontrada é: {soma_par}")
    
    