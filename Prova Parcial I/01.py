#Entrada
peso = float(input("O peso do paciente, em quilos, é: "))
altura = float(input("A altura do paciente, em metros, é: "))

#Processamento
imc = peso / (altura ** 2)

#Saída
if imc <= 24.9:
    print(f"O valor do IMC do paciente é:{imc: .2f} e ele tem peso normal.")
else:
    print(f"O valor do IMC do paciente é:{imc: .2f} e ele tem sobrepeso.")
    
    