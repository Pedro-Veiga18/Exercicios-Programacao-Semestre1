cod = int(input("O código do produto é: "))

match cod:
    case 1:
        print("Alimento não perecível")
    case 2|3|4:
        print("Alimento perecível")
    case 5|6:
        print("Vestuário")
    case 7:
        print("Higiene pessoal")
    case cod if cod >= 8 and cod <= 15:
        print("Limpeza e utensílios domésticos")
    case _:
        print("Inválido")
        
    