vetor = [53,904,345,76,32,21,402,9,1,800]
pares = []
impares = []

for list in vetor:
    if list%2 == 0:
        pares.append(list)
    else:
        impares.append(list)

print(vetor)
print(pares)
print(impares)