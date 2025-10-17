
quant = int(input("Digite a quantidade de produtos que serã inseridos na lista: "))
lista_nome = []
lista_preco = []
for i in range(quant):
    lista_nome.append(input("Digite o nome do produto: "))
    lista_preco.append(float(input("Digite o preço do produto, em reais: ")))
    
for i in range(quant -1):
    for j in range(i+1, quant):
        if lista_preco[i] > lista_preco[j]:
            aux_p = lista_preco[i]
            lista_preco[i] = lista_preco[j]
            lista_preco[j] = aux_p
            
            aux_n = lista_nome[i]
            lista_nome[i] = lista_nome[j]
            lista_nome[j] = aux_n
            
print("\nProdutos em ordem crescente de preço:")
for i in range(quant):
    print(f"{lista_nome[i]} : R${lista_preco[i]: .2f}")
            
