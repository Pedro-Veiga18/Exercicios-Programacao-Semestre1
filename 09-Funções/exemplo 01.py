#definição da função para somar dois números
def somar():
    #"passar" pela função pois ela ainda está sendo trabalhada: (pass) ou (...)
    resultado = v1 + v2 #variável local -> local a função
    return resultado
    



#entrada de dados
v1 = int(input("Digite o primeiro valor: ")) #variável global -> criada fora das funções
v2 = int(input("Digite o segundo valor: "))
total = somar()
print(f"soma = {total}")