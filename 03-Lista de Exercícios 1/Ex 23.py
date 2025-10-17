#Entrada
A = int(input("Quantidade de votos do candidato A: "))
B = int(input("Quantidade de votos do candidato B: "))
C = int(input("Quantidade de votos do candidato C: "))
votos_n = int(input("Quantidade de votos nulos: "))
votos_b = int(input("Quantidade de votos em branco: "))

#Processamento
validos = A + B + C
total = A + B + C + votos_n + votos_b
val_total = validos * 100/total
val_A = A * 100/total
val_B = B * 100/total
val_C = C * 100/total
nul_total = votos_n * 100/total
bran_total = votos_b * 100/total

#Saída
print(f"A quantidade total de eleitores foi: {total}")
print(f"O percentual de votos válidos em relação à quantidade de eleitores é: {val_total: .2f}% ")
print(f"O percentual de votos válidos do candidato A em relação ao total é: {val_A: .2f}%")
print(f"O percentual de votos válidos do candidato B em relação ao total é: {val_B: .2f}%")
print(f"O percentual de votos válidos do candidato C em relação ao total é: {val_C: .2f}%")
print(f"O percentual de votos nulos em relação à quantidade de eleitores é: {nul_total: .2f}% ")
print(f"O percentual de votos em branco em relação à quantidade de eleitores é: {bran_total: .2f}% ")
