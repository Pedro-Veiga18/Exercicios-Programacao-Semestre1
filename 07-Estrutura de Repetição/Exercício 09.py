num_itens = int(input("Total de itens: "))
total = 0

for i in range(1, num_itens + 1):
    valor = float(input("Valor do item R$: "))
    total += valor
    
print(f"Valor total sem desconto R${total: .2f}")
print("Digite 1 para pagamento à vista")
print("Digite 2 para pagamento parcelado (em 2 vezes)")
opcao = int(input())
if opcao == 1:
    total *= 0.9
    print(f"Total a pagar com 10% de desconto R${total: .2f}")
elif opcao == 2:
    total *= 1.155
    parcela = total / 2
    print(f"Total a pagar com 15.5% de aumento R${total: .2f}")
    print(f"Duas parcelas de R${parcela: .2f}")
    
    