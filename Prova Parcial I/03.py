#Entrada
aluguel = float(input("O valor do aluguel por ida de bicicletas é: "))
bikes =  int(input("A quantidade de bicicletas da empresa é: "))

#a)
bikes_alug_dia = bikes / 3

fat_anual = (bikes_alug_dia * aluguel) * 30 * 12

print(f"O faturamento anual da empresa é de: R${fat_anual}")

#b)
bikes_alug_mes = bikes_alug_dia * 30

bikes_multa = bikes_alug_mes / 10

fat_mensal_multas = bikes_multa * (aluguel + (0.10 * aluguel))

print(f"O faturamento mensal das multas é de: R${fat_mensal_multas}")