alunos = []


def main():
    flag = True

    while flag:
        carctAluno()

        #print(alunos)

        print("\nDeseja continuar acrescentando aluno ? (s/n)")
        escolha = input("Resposta: ")

        if escolha == 's':
            continue
        else:
            detAA = determinaAltura()
            print("\nNumero de alunos maior de 13 anos com altura inferior a da média das alturas: %i\n" %detAA)
            #print(alunos)
            flag = False

def carctAluno():
    carAluno = []


    idade = int(input("\nDigite idade: "))
    altura = float(input("Digite altura: "))

    carAluno.append(idade)
    carAluno.append(altura)

    alunos.append(carAluno)

def mediaAltura():
    somaAltura = 0

    for aluno in alunos:
        somaAltura += aluno[1]

    media = somaAltura/len(alunos)
    #print(media)
    return media

def determinaAltura():
    valor = 0
    soma = 0
    media = mediaAltura()

    for aluno in alunos:
        if aluno[0]>13:
            if aluno[1] < media:
                soma += 1

    return soma

main()