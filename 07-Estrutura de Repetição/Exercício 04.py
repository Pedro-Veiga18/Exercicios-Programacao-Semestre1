valor = int(input("Informe um valor inteiro e positivo: "))
fatorial = 1
cont = 1

#versão do fatorial incrementando o contador
while cont <= valor:
    fatorial = fatorial * cont
    cont = cont + 1
print(f"{valor})! = {fatorial}")


#versão do fatorial decrementando o contador
cont = valor
fatorial = 1
while cont >= 1:
    fatorial = fatorial * cont
    cont = cont - 1
print(f"{valor})! = {fatorial}")