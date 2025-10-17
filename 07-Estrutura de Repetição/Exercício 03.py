resposta = "sim"

while resposta == "sim":
    contador = 0
    valor = int(input("Digite um valor inteiro: "))
    while contador <= 10:
        resultado = valor * contador
        print(f"{valor} * {contador} = {resultado}")
        contador = contador + 1
    print()
    resposta = input("Deseja imprimir outra tabuada (sim ou não)?: ")