#entrada
v1 = int(input("Valor 1: "))
v2 = int(input("Valor 2: "))
v3 = int(input("Valor 3: "))
#Processamento
if v1 != v2 and v1 != v3 and v2 != v3:
    valores = (v1, v2, v3)
    min_valor = min(valores)
    print(f"O menor valor é: {min_valor}")
else:
    print("Os valores não são diferentes")
          
          