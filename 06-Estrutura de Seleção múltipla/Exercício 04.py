idade = int(input("A idade do nadador é: "))

match idade:
    case cod if cod >= 5 and cod <= 7:
        print("Infantil A")
    case cod if cod >= 8 and cod <= 10:
        print("Infantil B")
    case cod if cod >= 11 and cod <= 13:
        print("Juvenil A")
    case cod if cod >= 14 and cod <= 17:
        print("Juvenil B")
    case cod if cod >= 18:
        print("adulto")
    case _:
        print("Sem categoria")