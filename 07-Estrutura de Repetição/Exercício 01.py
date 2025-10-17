v1 = int(input("Valor 1: "))
v2 = int(input("Valor 2: "))
x = v1
print(f"{x}")
while x < v2:
    x = x + 1
    if x % 1 == 0:
        print(f"{x}")