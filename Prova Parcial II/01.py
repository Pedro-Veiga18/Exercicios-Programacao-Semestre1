pA = int(input("Digite a quantidade de habitantes, em milhares, do país A: "))
pB = int(input("Digite a quantidade de habitantes, em milhares, do país B: "))

tA = float(input("Digite a taxa de crescimento anual, em porcentagem, do país A: "))
tB = float(input("Digite a taxa de crescimento anual, em porcentagem, do país B: "))

ano = 1

if pA < pB and tA > tB:

    popu_total_ano_A = pA + ((tA/100 * pA) * ano)
    pupo_total_ano_B = pB + ((tB/100 * pB) * ano)
    
    while popu_total_ano_A <= pupo_total_ano_B:
        
        ano = ano + 1
        
        popu_total_ano_A = pA + ((tA/100 * pA) * ano)
        pupo_total_ano_B = pB + ((tB/100 * pB) * ano)
        
        if popu_total_ano_A > pupo_total_ano_B:
            print(f"A quantidade de anos para que a população de A seja maior que a população de B é: {ano}")
            
else: 
    print("A população de A deve ser menor que a população de B e a taxa de crescimento anual de A deve ser maior que a de B")
        
        
        
        
        



