#função a)
def sensor_dados():
    sensor1 = []
    sensor2 = []
    dia = 1
    while dia < 8:
        print(f"Dia {dia}:")
        sensor1.append(float(input("Digite o volume de chuva, em mm, do sensor 1: ")))
        sensor2.append(float(input("Digite o volume de chuva, em mm, do sensor 2: ")))
        dia += 1
        
    return sensor1, sensor2
        


#função b)
def media_dia(sensor1,sensor2):
    dia = 1
    medias = []
    for i in range(len(sensor2)):
        print(f"Dia {dia}")
        media = (sensor1[i] + sensor2[i]) / 2
        medias.append(media)
        print(f"Média diária: {media: .2f}mm")
        dia += 1
        
    return medias
        
    

#função c)
def acumu_total(medias):
    total = 0
    for i in range(len(medias)):
        total += medias[i]
        
    print(f"O total acumulado na semana foi: {total: .2f}mm")
    
    return total
 
  
  
#função d)  
def nivel_alerta(total):
    if total <= 100:
        print(f"SEM ALERTA")
    elif total >= 101 and total <= 200:
        print(f"ALERTA AMARELO")
    elif total >= 201 and total <= 300:
        print(f"ALERTA LARANJA")
    else:
        print(f"ALERTA VERMELHO")
    




#a)
sensor1, sensor2 = sensor_dados()
#b)
medias = media_dia(sensor1, sensor2)
#c)
total = acumu_total(medias)
#d)
nivel_alerta(total)
        
        

    


