alunos = []
vect = []
soma = 0
soma1 = 0

while len(alunos)<5:
    nome = input("Nome do aluno: ")
    nome = []

    nota1 = int(input("nota 1: "))
    nome.append(nota1)
    nota2 = int(input("nota 2: "))
    nome.append(nota2)
    nota3 = int(input("nota 3: "))
    nome.append(nota3)
    nota4 = int(input("nota 4: "))
    nome.append(nota4)

    alunos.append(nome)

for list in alunos:
    for list2 in list:
        soma =soma+list2
    media = soma/4
    soma=0
    vect.append(media)

for app in vect:
    if app >= 7:
        soma1 += 1

print("Total de alunos aprovados: %i" %soma1)