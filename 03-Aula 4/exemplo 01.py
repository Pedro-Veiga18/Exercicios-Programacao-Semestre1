#Programa para ler as duas notas de um aluno.
#Calcular e imprimir a média

#Entrada
nota1= float(input("Informe a primeira nota: "))
nota2= float(input("Informe a segunda nota: ")) 
    
#Processamento
media= (nota1+nota2)/2
    
#Saída
print(f"A média do aluno é: {media: .2f}")
if media>=7: 
    print("APROVADO")
else:
    print("REPROVADO")