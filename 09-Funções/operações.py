#função para calcular o valor do delta
def calc_delta(a,b,c):
    delta = b*b -4*a*c
    return delta

from math import sqrt
#função para calcular o valor das raízes de uma equação de 2o grau
def calc_raiz(a,b,delta):
    x1 = (-b + sqrt(delta)) / 2*a
    x2 = (-b - sqrt(delta)) / 2*a
    
    return x1, x2