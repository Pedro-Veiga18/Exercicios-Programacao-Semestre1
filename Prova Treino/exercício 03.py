import util

escolha = 0
quant = int(input("Digite a quantidade de números que serã inseridos na lista: "))
lista = []
for i in range(quant):
    lista.append(int(input("Digite um valor: ")))
    

util.ordenar(lista,escolha)

maior1 = lista.pop(-1)
maior2 = lista.pop(-1)
maior3 = lista.pop(-1)

print(f"Os maiores valores são: {maior3, maior2, maior1}")

    
    
