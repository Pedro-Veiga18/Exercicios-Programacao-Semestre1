dias = int(input("Número de dias no hotel foi: "))

#processamento
if dias > 15:
    conta = (300 + 22.50) * dias
elif dias == 15:
    conta = (300 + 56) * dias
else:
    conta = (300 + 88) * dias

print(f"A conta final do cliente foi: R${conta: .2f}")