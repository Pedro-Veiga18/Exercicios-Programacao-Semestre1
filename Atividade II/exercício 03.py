#a)

quan_alu = int(input("Informe a quantidade de alunos pesquisados: "))

nao = 0
sim = 0

for i in range(quan_alu):
   resposta = int(input(f"Você, aluno {i+1}, é a favor da criação da estação ? Digite 1 para sim ou digite 2 para não: "))

   if resposta == 1:
       sim += 1
       print("O aluno concorda")
   elif resposta == 2:
       nao += 1
       print("O aluno não concorda")
   else:
       print("Valor inválido. Apenas digite 1 para sim ou 2 para não.")

print(f"A quantidade de alunos que participaram é: {quan_alu}")
print(f"O total de alunos a favor é: {sim}")
print(f"O total de alunos contra é: {nao}")

#b)
porcen_sim = (sim / quan_alu) * 100
porcen_nao = (nao / quan_alu) * 100

print(f"A porcentagem de alunos que são a favor é: {porcen_sim: .2f}% ")
print(f"A porcentagem de alunos que são contra é: {porcen_nao: .2f}% ")
