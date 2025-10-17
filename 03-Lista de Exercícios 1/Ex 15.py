#Entrada

valor = float(input("O valor da prestação em atraso é: R$ "))
taxa = float(input("A taxa de porcentagem do atraso é: "))
tempo= float(input("A quantidade de dias atrasados é: "))

#Processamento
prestação = valor + (valor * (taxa/100) * tempo)

#Saída
print(f"O valor da prestação do produto em atraso é R${prestação: .2f}")
