#Entrada
val_hr= float(input("Valor da hora-aula: R$ "))
hr_mes= float(input("Horas trabalhadas no mês: "))
desc= float(input("Desconto do INSS: "))

#Processamento
sal_br= val_hr*hr_mes
sal_liq= sal_br*desc/100

#Saída
print(f"O valor do salário líquido mensal é: R${sal_liq: .2f}")