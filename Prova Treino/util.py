def calcular_maior(lista):
    maior_v = 0
    for i in range(len(lista)):
        if lista[i] > maior_v:
            maior_v = lista[i]
            
    return maior_v


        
def calcular_menor(lista):
    from math import inf
    menor_v = inf
    for i in range(len(lista)):
        if lista[i] < menor_v:
            menor_v = lista[i]
            
    return menor_v
 
 
       
def calcular_media(lista):
    if not lista:
        return 0
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]
    return soma / len(lista)
    
    
    
def binario(num):
    if num == 0:
        return '0'
    
    bina = ''
    
    while num > 0:
        resto = num % 2
        bina = str(resto) + bina
        num = num // 2
    return bina



def hexa(num):
    if num == 0:
        return '0'

    hexad = ''
    
    while num > 0:
        resto = num % 16
        
        if resto < 10:
            hexad = str(resto) + hexad
        elif resto == 10:
            hexad = 'A' + hexad
        elif resto == 11:
            hexad = 'B' + hexad
        elif resto == 12:
            hexad = 'C' + hexad
        elif resto == 13:
            hexad = 'D' + hexad
        elif resto == 14:
            hexad = 'E' + hexad
        elif resto == 15:
            hexad = 'F' + hexad

        num = num // 16
    
    return hexad



def ordenar(lista,escolha):
    if escolha == 0:
        for _ in range(len(lista)):
            for i in range(len(lista) -1):
                if lista[i] > lista[i+1]:
                    aux = lista[i]
                    lista[i] = lista[i+1]
                    lista[i+1] = aux
    
    elif escolha == 1:
        for _ in range(len(lista)):
            for i in range(len(lista) -1):
                if lista[i] < lista[i+1]:
                    aux = lista[i]
                    lista[i] = lista[i+1]
                    lista[i+1] = aux
 
 
                    
def imprimir(lista):
    for i in range(len(lista)):
        print(lista[i], end=" ")
                    

    
    

    
    