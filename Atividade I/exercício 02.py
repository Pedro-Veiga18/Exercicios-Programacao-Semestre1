#Entrada
P = float(input("Valor da aplicação mensal: "))
i = float(input("Valor da taxa de juros: "))
n = int(input("Número de meses: "))
#Processamento
if i == 0:
    print(f"O valor do rendimento é R$0")

elif i > 0 and i <= 1:
    valor_acumulado = (P * ((1 + i) ** n  -1)) / i
    print(f"O valor do rendimento é: R${valor_acumulado: .2f}")
else:
    print("Taxa de juros inválida.")
