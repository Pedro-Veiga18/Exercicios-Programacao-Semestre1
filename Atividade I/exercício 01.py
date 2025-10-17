n = int(input("Digite o número da sua conta corrente: "))
if n < 100:
    dez = ((n % 100) // 10)
    uni = ((n % 100) % 10) 

    uni1 = uni * 100
    dez1 = dez * 10

    n_inv = uni1 + dez1

    soma = n + n_inv
    sdez = ((soma % 100) // 10)
    suni = ((soma % 100) % 10) 

    multi = (sdez * 1) + (suni * 2)
    verificador = ((multi % 100) % 10)
    print(f"Seu dígito verificador da conta é {verificador}")
else:
    cent = n // 100
    dez = ((n % 100) // 10)
    uni = ((n % 100) % 10) 

    uni1 = uni * 100
    dez1 = dez * 10

    n_inv = uni1 + dez1 + cent
    soma = n + n_inv
    scent = soma // 100
    sdez = ((soma % 100) // 10)
    suni = ((soma % 100) % 10) 

    multi = (scent * 1) + (sdez * 2) + (suni * 3)
    verificador = ((multi % 100) % 10)
    print(f"Seu dígito verificador da conta é {verificador}")