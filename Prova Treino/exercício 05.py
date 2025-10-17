quant = int(input("Digite a quantidade de produtos que serã inseridos na lista: "))
nomes = []
c_preco = []
v_preco = []
for i in range(quant):
    nomes.append(input("Digite o nome do produto: "))
    c_preco.append(float(input("Digite o preço de custo, em reais: ")))
    v_preco.append(float(input("Digite o preço de venda, em reais: ")))
    
lucro_10_30 = []
lucro_30 = []

for i in range(quant):
    ganho = v_preco[i] - c_preco[i]
    if ganho >= c_preco[i] * 0.1 and ganho <= c_preco[i] * 0.3:
        lucro_10_30.append(nomes[i])
        
    elif ganho > c_preco[i] * 0.3:
        lucro_30.append(nomes[i])
        
print(f"\nA lista dos produtos que lucraram entre 10% e 30% é:")
for i in range(len(lucro_10_30)):
    print({lucro_10_30[i]})
        
print(f"\nA lista dos produtos que lucraram mais que 30% é:")
for i in range(len(lucro_30)):
    print({lucro_30[i]})