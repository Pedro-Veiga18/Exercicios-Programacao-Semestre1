from math import sqrt

#Funções

def calc_delta():
    deltac = b**2 -4*a*c
    
    return deltac

def calc_raiz_x():
    x1 = (-b + sqrt(delta)) / 2*a
    x2 = (-b - sqrt(delta)) / 2*a
    
    return x1, x2
    
#Principal

a = float(input("Digite o valor do 'a' da função: "))

if a == 0:
    print("Não é uma equação do 2o grau.")
    
else:
    b = float(input("Digite o valor do 'b' da função: "))
    c = float(input("Digite o valor do 'c' da função: "))
    delta = calc_delta()
    
    if delta < 0:
        print("A equação não tem raiz real.")
        
    else:
        x1, x2 = calc_raiz_x()
        print(f"x1 = {x1: .2f}")
        print(f"x2 = {x2: .2f}")
        
        


    
    