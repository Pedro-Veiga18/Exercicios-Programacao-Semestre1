sal_min = float(input("Digite o valor do salário mínimo em R$: "))

num_contribuintes = int(input("Digite o número de contribuintes: "))

lista_sal = []
lista_depend = []

for i in range(0, num_contribuintes):
    
    lista_sal.append(float(input(f"Digite o salário do {i + 1}° contribuinte: ")))
    lista_depend.append(int(input(f"Digite o número de dependentes do {i + 1}° contruinte: ")))
    
    lista_sal[i] = lista_sal[i] * ( 1 - lista_depend[i] * 0.05)
    
    if lista_sal[i] < 0:
        lista_sal[i] = 0
    
    if lista_sal[i] < 2 * sal_min:
        print("Esse contribuiente é isento de imposto de renda.")
        
    elif lista_sal[i] >= 2 *sal_min and lista_sal[i] < 3 * sal_min:
        print(f"O valor do imposto de renda desse contribuinte é: R${lista_sal[i] * 0.05: .2f}")
        
    elif lista_sal[i] >= 3 *sal_min and lista_sal[i] < 5 * sal_min:
        print(f"O valor do imposto de renda desse contribuinte é: R${lista_sal[i] * 0.1: .2f}")
        
    elif lista_sal[i] >= 5 *sal_min and lista_sal[i] < 7 * sal_min:
        print(f"O valor do imposto de renda desse contribuinte é: R${lista_sal[i] * 0.15: .2f}")
        
    elif lista_sal[i] >= 7 *sal_min: 
        print(f"O valor do imposto de renda desse contribuinte é: R${lista_sal[i] * 0.2: .2f}")
        
    else:
        print("O salário mínimo é inválido.")