#função a)
def imprime_febre(nomes,temp):
    print(f"\nOs pacientes com febre são:")
    for i in range(len(temp)):
        if temp[i] > 37.8:
            print(f"{nomes[i]}")
            
            
#função b)
def imprime_risco(nomes,temp,pressao):
    print(f"\nOs pacientes em risco baixo são:")
    for i in range(len(pressao)):
        if temp[i] <= 37.5 and pressao[i] <= 130:
            print(f"{nomes[i]}")
        
            
    print(f"\nOs pacientes em risco moderado são:")
    for i in range(len(pressao)):
        if temp[i] >= 37.6 and temp[i] <= 38.5 or pressao[i] >= 131 and pressao[i] <= 150:
            print(f"{nomes[i]}")
            
    print(f"\nOs pacientes em risco alto são:")
    for i in range(len(pressao)):
        if temp[i] > 38.5 or pressao[i] > 150:
            print(f"{nomes[i]}")
            
        
    




#Entrada
quant = int(input("Digite a quantidade de pacientes: "))
nomes = []
temp = []
pressao = []
for i in range(quant):
    nomes.append(input("Digite o nome do paciente: "))
    temp.append(float(input("Digite a temperatura do paciente, em °C: ")))
    pressao.append(float(input("Digite a pressão do paciente, em mmHg: ")))
    

#a)
imprime_febre(nomes,temp)

#b)
imprime_risco(nomes,temp,pressao)