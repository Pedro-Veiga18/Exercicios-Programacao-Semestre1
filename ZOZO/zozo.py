
#Exercício 1

list_val = []
for i in range(5):
    valor = int(input('Digite um valor: '))
    list_val.append(valor)

maior_valor = list_val[0]
menor_valor = list_val[0]

for valor in list_val:
    if valor > maior_valor:
        maior_valor = valor
    elif valor < menor_valor:
        menor_valor = valor
        
print(maior_valor)
print(menor_valor)    

#Exercício 2

list_val = []
for i in range(5):
    valor = int(input('Digite um valor: '))
    list_val.append(valor)

par = 0
impar = 0
total = 0 
for num in list_val:
    if num % 2 == 0:
        par+=1
    else:
        impar+=1
    
    total+=1
    
print(f'Há {par} números pares na lista')
print(f'Há {impar} números ímpares na lista')
print(f'{par*100/total}% da lista são números pares e {impar*100/total}% são numeros ímpares')

#Exercício 3

list_val = []
for i in range(5):
    valor = int(input('Digite um valor: '))
    list_val.append(valor)

eh_primo = True
primos = []
for valor in list_val:
    for i in range(2,valor-1):
        if valor % i == 0:
          eh_primo = False
    if eh_primo and valor>1:
        primos.append(valor)
        
print(primos) 

#Exercício 4

produtos = [0, 1, 2, 3, 4, 5]
quantidade = [24, 35, 14, 2, 9]
preco = [40, 60, 50, 60, 30]
maior_preco = 0
mais_caro = []

for i in range(len(preco)):
    if maior_preco < preco[i]:
        maior_preco = preco[i]
        produto_mais_caro = produtos[i]
    elif maior_preco == preco[i]:
        mais_caro.append(produto_mais_caro)
        produto_mais_caro = produtos[i]
        mais_caro.append(produto_mais_caro)

if len(mais_caro) == 0:
    print(f'O produto mais caro é {produto_mais_caro}')
else:
    print(f'Os produtos mais caros são {mais_caro}')
    
valor_total_produto = []
for i in range(len(quantidade)):
    valor_total_produto.append(quantidade[i]*preco[i])

print(f'O valor total de cada produto armazenado é {valor_total_produto}')

valor_total = 0
for valor in valor_total_produto:
    valor_total += valor
print(f'O valor total dos produtos em estoque é {valor_total}')

#Exercício 5

list_inteiros = []
for i in range(5):
    inteiro = int(input('Digite um inteiro: '))
    list_inteiros.append(inteiro)
    
list_inteiros_invertida = []
for i in range(len(list_inteiros)):
    list_inteiros_invertida.append(list_inteiros[len(list_inteiros)-1-i])
print(list_inteiros_invertida)
    

#Exercício 8

#Função que retorna o índice do ponto de equilíbrio
def ponto_equilibrio(list_val):
    
    tamanho = len(list_val)
    indice_equilibrio = (tamanho-1)/2
    
    soma_teste1 = 0
    soma_teste2 = 0
    
    for i in range(len(list_val)):
        num = list_val[i]        
        if i < indice_equilibrio:
            soma_teste1 += num
        if i > indice_equilibrio:
            soma_teste2 += num
            
    if soma_teste1 == soma_teste2:
        return indice_equilibrio
    

lista = [1, 3, 5, 2, 2, 1, 6]    
print(ponto_equilibrio(lista))


    