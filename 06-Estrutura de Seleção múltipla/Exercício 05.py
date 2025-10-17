preco = float(input("Preço do produto: "))
cod = int(input("Código de condição de pagamento: "))

match cod:
    case 1:
        total = preco - (0.1 * preco)
    case 2:
        total = preco - (0.05 * preco)
    case 3:
        total = preco
    case 4:
        total = preco + (0.1 * preco)

print(f"O total a ser pago é {total}")