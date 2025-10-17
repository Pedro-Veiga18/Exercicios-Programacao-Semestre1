cod = int(input("O código do produto é: "))

if cod == 1:
    print("Alimento não perecível")
elif cod >= 2 and cod <= 4:
    print("Alimento perecível")
elif cod == 5 or cod == 6:
    print("Vestuário")
elif cod == 7:
    print("Higiene pessoal")
elif cod >= 8 and cod <= 15:
    print("Limpeza e utensílios domésticos")
else: 
    print("Inválido")