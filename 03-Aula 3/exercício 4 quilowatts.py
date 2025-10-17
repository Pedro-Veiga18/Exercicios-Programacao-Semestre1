#Entrada
sal_min = float(input("Valor do salário mínimo em reais: "))
KW = float(input("Valor da quantidade de quilowatts utilizada: "))

#Processamento
valor_KW = sal_min/700
valor_re = KW*sal_min/700
valor_desc = valor_re-(10/100)

#Sáida
print(f"O valor de cada quilowatts é: {valor_KW}R$")
print(f"O valor a ser pago pela residência é: {valor_re}R$")
print(f"O valor a ser pago com desconto é: {valor_desc}R$")