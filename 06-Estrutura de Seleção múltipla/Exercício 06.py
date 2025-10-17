num1 = int(input("Valor 1: "))
num2 = int(input("Valor 2: "))
op = input("Operação: ")

match op:
    case "Adição":
        total = num1 + num2
    case "Subtração":
        total = num1 - num2
    case "Multiplicação":
        total = num1 * num2
    case "Divisão":
        total = num1 / num2
    case _:
        print("Operação inválida")

print(f"O total é {total}")