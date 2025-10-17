#Entrada
quan_and_loc = int(input("A quantidade de andaimes disponíveis para locação é: "))
val_dia_alu = float(input("O valor diário do aluguel de cada andaime: "))

#a)
and_alug = (0.4 * quan_and_loc)
fat_anual = (and_alug) * (val_dia_alu * 30 * 12)  
print(f"O faturamento anual da empresa é de: R${fat_anual: .2f}")

#c)
compra = quan_and_loc + 0.2 * quan_and_loc 
total = compra - 0.05 * quan_and_loc
print(f"A quantidade de andaimes disponíveis ao final do ano é:{total: .0f}")