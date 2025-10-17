#Entrada
base = float(input("Valor da base: "))
altura = float(input("Valor da altura: "))

#Processamento
área = base*altura
perímetro = 2*(base+altura)

#Saída
print(f"A área do retângulo é: {área: .2f}")
print(f"O perímetro do retângulo é: {perímetro: .2f}")