renda_anual = float(input("A renda anual é: "))

match renda_anual:
    case renda_anual if renda_anual <= 10000:
        imposto = 0
    case renda_anual if renda_anual > 10000 and renda_anual <= 25000:
        imposto = renda_anual * 10.35/100
    case renda_anual if renda_anual > 25000 and renda_anual <= 50000:
        imposto = renda_anual * 25.42/100
    case renda_anual if renda_anual > 50000:
        imposto = renda_anual * 29.75/100
        
print(f"O valor total em impostos é de R$:{imposto}")