#Entrada
p1 = float(input("Insira a nota da prova 1: "))
p2 = float(input("Insira a nota da prova 2: "))
t1 = float(input("Insira a nota do trabalho 1: "))
t2 = float(input("Insira a nota do trabalho 2: "))

#Processamento
med_p = (p1+p2)/2
med_t = (t1+t2)/2
med_f = 70/100 * med_p + 30/100 * med_t

print(f"Sua média final é: {med_f: .2f}")

if med_f >= 7:
    print("Você foi aprovado")
else:
    print("Você foi reprovado")