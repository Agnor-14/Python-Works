A = [numero for numero in range(1,11,1)]

calculation = [((valor**2)+(valor**2)) for valor in A]

for result in calculation:
    print(result)