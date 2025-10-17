binario = int(input("Digite um valor em binário: "))

if binario == 0 or binario == 00 or binario == 000 or binario == 0000  or binario == 00000  or binario == 000000  or binario == 0000000  or binario == 00000000:
    print(f"O valor em decimal é: 0")
    
    
else:
    
    aux = binario
    decimal = 0
    i = 0

    while binario > 0:
        digito = binario % 10
    
        if digito == 0 or digito == 1:
            decimal = decimal + digito * 2 ** i
            i += 1
            binario = binario // 10
        
        
        else:
            print("O valor em binário deve possuir apenas 0 ou 1 como caracteres.")
            break
 
 
    if digito == 0 or digito == 1:   
        print(f"O valor {aux} em decimal é: {decimal}")         
        
