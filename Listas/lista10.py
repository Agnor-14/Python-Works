lista = []

A = [numero for numero in range(1,11,1)]
B = [numero for numero in range(11,21,1)]

assert len(A) == len (B)

print(A)
print(B)

n = len(A)

for i in range(n):
    print(i)
    lista.append(A[i])
    print(lista)
    lista.append(B[i])
    print(lista)

print(lista)