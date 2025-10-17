from math import inf

lista = []
maior = 0
menor = inf
for i in range(5):
    valor = int(input("Informe um valor inteiro: "))
    lista.append(valor)
    if i == 0 or lista[i] > maior:
        maior = lista[i]
    if lista[i] < menor:
        menor = lista[i]
    
print(f"O maior valor é: {maior}")
print(f"O mneor valor é: {menor}")
print(lista)