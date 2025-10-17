def funcao(x,y,z):
    aux = x
    x = y
    y = z
    z = aux
    
    return x
    
x = 2
y = 3
z = 5
            
print(funcao(x,y,z))