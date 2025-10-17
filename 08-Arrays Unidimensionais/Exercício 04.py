produto = []
estoque = []
valor = []

total = int(input("Informe o total de produtos: "))

#entrada dos dados de cada produto
for i in range(total):
    print(f"Produto {i + 1}")
    produto.append(input("Produto: "))
    valor.append(float(input("Preço:R$ ")))
    estoque.append(int(input("Quantidade em estoque: ")))