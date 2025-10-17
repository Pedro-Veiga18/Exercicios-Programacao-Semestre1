lista = []

soma = 0

n = int(input("Digite a quantidade de números que serão listados: "))

for i in range(0, n):
    lista.append(int(input(f"Digite o {i+1}° valor: ")))
    
    soma += lista[i]
    
print(lista)
print(f"A soma dos valores digitados é: {soma}")
print(f"A média aritmética dos valores digitados é: {soma/n: .2f}")