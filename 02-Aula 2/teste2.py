print("Qual é seu nome?")
nome = input()
print("Seja bem-vindo",nome) #forma antiga de fazer
print("Seja bem-vindo "+nome) #forma antiga de fazer (com espaço)
print(f"Seja bem-vindo {nome}") #forma nova de fazer

print("Qual é a sua idade?")
idade = int(input())
print(f"{nome} você tem {idade} anos")

print("Qual é sua nota em algoritmos?")
nota = float(input())
print(f"Sua nota é {nota}")
