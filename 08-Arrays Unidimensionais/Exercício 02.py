lista = []
total_par = 0

for i in range(5):
    lista.append(int(input("Informe um valor inteiro: ")))
    if lista[i] % 2 == 0:
        total_par += 1
        
porcentagem_par = total_par / len(lista) * 100
        
print(f"A porcentagem de números pares: {porcentagem_par: .2f}%")
print(f"A porcentagem de números ímpares: {100 - porcentagem_par: .2f}%")