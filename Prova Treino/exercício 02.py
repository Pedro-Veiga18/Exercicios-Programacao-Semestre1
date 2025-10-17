import util

quant = int(input("Digite a quantidade de números que serã inseridos na lista: "))
lista = []
for i in range(quant):
    lista.append(int(input("Digite um valor: ")))
    
maior_v = util.calcular_maior(lista)
menor_v = util.calcular_menor(lista)

print(maior_v)
print(menor_v)
dife = maior_v - menor_v

print(f"A diferença entre o maior e o menor valor da lista é: {dife}")
    
