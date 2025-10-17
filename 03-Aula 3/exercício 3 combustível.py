#Entrada
tempo_hrs = float(input("Tempo da viagem em horas: "))
vel_m = float(input("Velocidade média da viagem em Km/h: "))

#Processamento
Km = tempo_hrs*vel_m
L = Km/10.5

#Sáida
print(f"A quantidade de litros usada na viagem foi: {L: .4f}")
