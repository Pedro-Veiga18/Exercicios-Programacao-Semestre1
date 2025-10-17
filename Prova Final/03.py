#função a)
def nm_variacao(nomes, a_valor, f_valor):
    variacoes = []
    for i in range(len(f_valor)):
        variacao = ((f_valor[i] - a_valor[i]) / a_valor[i]) * 100
        variacoes.append(variacao)
        print(f"Ação: {nomes[i]} -> variação: {variacao: .2f}%")
        
    return variacoes



#função b)
def simula(nomes, variacoes):
    print(f"Os retornos de investimentos hipotéticos de R$1000,00 são:")
    for i in range(len(variacoes)):
        retorno = 1000 + (variacoes[i] * 1000) / 100
        print(f"Ação: {nomes[i]} -> retorno: R${retorno: .2f}")
        
    

#função c)
def mais_lucro(nomes, variacoes):
    maior = 0
    maior_nome = ""
    for i in range(len(variacoes)):
        if variacoes[i] > maior:
            maior = variacoes[i]
            maior_nome = nomes[i]
    print(f"Ação mais lucrativa: {maior_nome}")
    
    
    
#função d)
def menos_lucro(nomes, variacoes):
    from math import inf
    menor = inf
    menor_nome = ""
    for i in range(len(variacoes)):
        if variacoes[i] < menor:
            menor = variacoes[i]
            menor_nome = nomes[i]
    print(f"Ação menos lucrativa: {menor_nome}")





#Entrada
quant = int(input("Digite a quantidade de ações que serão avaliadas: "))
nomes = []
a_valor = []
f_valor = []
for i in range(quant):
    nomes.append(input("Digite o nome da ação: "))
    a_valor.append(float(input("Digite o preço da ação na abertura: ")))
    f_valor.append(float(input("Digite o preço da ação no fechamento: ")))
    


#a)
variacoes = nm_variacao(nomes, a_valor, f_valor)
#b)
simula(nomes, variacoes)
#c)
mais_lucro(nomes, variacoes)
#d)
menos_lucro(nomes, variacoes)

