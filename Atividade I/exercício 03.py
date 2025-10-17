from math import pi
#Entrada
h = float(input("Digite a altura do reservatório: "))
r = float(input("Digite o raio do reservatório: "))
uni_custo = float(input("Digite o custo de cada unidade: "))
#Processamento
area = 2 * pi * r * (r + h)

uni_necessaria = area / 3 
uni_total = uni_necessaria + (0.05 * uni_necessaria)
if uni_total != int:
    uni_total = (uni_total + 1) // 1
else:
    uni_total = uni_total
    
custo_total = uni_custo * uni_total


#Saída
print(f"A área total a ser isolada é:{area: .2f}m²")
print(f"A quantidade de unidades de isolamento é:{uni_total: .0f}")
print(f"O custo total é: R${custo_total: .2f}")
