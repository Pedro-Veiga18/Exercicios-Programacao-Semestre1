import operações

a = float(input("Digite o valor do 'a' da função: "))

if a == 0:
    print("Não é uma equação do 2o grau.")
    
else:
    b = float(input("Digite o valor do 'b' da função: "))
    c = float(input("Digite o valor do 'c' da função: "))
    delta = operações.calc_delta(a,b,c)
    if delta < 0:
        print("Não tem raiz real.")
    else:
        x1,x2 = operações.calc_raiz(a,b,delta)
        print(f"x1 = {x1: .2f}")
        print(f"x2 = {x2: .2f}")