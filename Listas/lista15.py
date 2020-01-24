def utilNotas(notas):
    auxSoma = 0
    auxSomaNotas = 0
    acimaMedia = []
    menorQueSete = []

    for nota in notas:
        auxSoma += 1
    print("\nQuantidade de notas: %i\n" %auxSoma)

    print(notas)

    notas.reverse()
    for nota in notas:
        print(nota)

    for nota in notas:
        auxSomaNotas += nota
    print ("\nSomatoria das notas: %0.2f\n" %auxSomaNotas)

    mediaNotas = auxSomaNotas/len(notas)
    print("Média das notas: %0.2f\n" %mediaNotas)

    for nota in notas:
        if nota > mediaNotas:
            acimaMedia.append(nota)
    print(acimaMedia)

    for nota in notas:
        if nota < 7:
            menorQueSete.append(nota)
    print(menorQueSete)

    print("\nObrigado por utilizar o programa!\n")

def main():
    notas = []
    flag = True

    while flag:
        colocarNota = float(input("Entre com uma nota: "))

        if colocarNota != -1:
            notas.append(colocarNota)
        else:
            break

    utilNotas(notas)

while True:
    main()