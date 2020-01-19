lista =[]

def geraVetor():
    A = [numero for numero in range(1,11,1)]
    B = [numero for numero in range(11,21,1)]
    C = [numero for numero in range(21,31,1)]

    print(A)
    print(B)
    print(C)

    [lista.extend((A[valor],B[valor],C[valor])) for valor in range(10)]
    print(lista)

geraVetor()