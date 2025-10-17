num = int(input("Digite um valor inteiro: "))


maior = 0

for i in range(1, int((num / 2) + 1)):
    if num % i == 0:
        primo = True
        for j in range(2, int(i ** (1/2) + 1 )):
            if i % j == 0:
                primo = False
                break
        if (primo or i == 2 or i == 3) and i > maior:
            maior = i
        
            
print(f"O maior fator primo de {num} é: {maior}")
    