from math import sqrt

#Entrada
p1x = int(input("Coordenada x do ponto 1: "))
p1y = int(input("Coordenada y do ponto 1: "))
p2x = int(input("Coordenada x do ponto 2: "))
p2y = int(input("Coordenada y do ponto 2: "))

#cálculo da distância
dis_p1 = sqrt(p1x ** 2 + p1y ** 2)
dis_p2 = sqrt(p2x ** 2 + p2y ** 2)

print(f"Distância do ponto 1 até a origem: {dis_p1: .3f}")
print(f"Distância do ponto 2 até a origem: {dis_p2: .3f}")

if dis_p1 < dis_p2:
    print("O ponto 1 está mais próximo da origem")
elif dis_p1 == dis_p2:
    print("O ponto 1 e 2 estão igualmente próximos da origem")
else:
    print("O pont 2 está mais próximo da origem")