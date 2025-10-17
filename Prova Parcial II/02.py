inicio = int(input("Digite um valor de 4 digitos para o início (1000-9999): "))
fim = int(input("Digite um valor de 4 digitos para o fim (1000-9999): "))

if inicio >= 1000 and inicio <= 9999 and fim >=1000 and fim <= 9999:

    total_raros = 0
    total_raros_impar = 0
    total_raros_par = 0

    for i in range(inicio, fim + 1):
    
        milhar= (i // 1000) 
        cent= (i // 100 % 10)
        deze= (i % 100 // 10)
        uni= (i % 10)
    

    
        if milhar + cent == deze + uni:
            print(i)
            total_raros += 1
            if (i % 2 == 1):
                total_raros_impar += 1
            if (i % 2 == 0):
                total_raros_par += 1
        
            
            
        
        

    print(f"O total de números raros é: {total_raros}")
    print(f"O total de números raros ímpares é: {total_raros_impar}")
    print(f"O total de números raros pares é: {total_raros_par}")

else:
    print("Os valores para o início e para o fim devem estar entre 1000-9999.")