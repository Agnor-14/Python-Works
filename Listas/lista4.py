vogal = ['a','e','i','o','u','A','E','I','O','U']
vetor = ['a','a','b','c','i','k','o','p','q','u']

aux=1
soma =0
cons = []

for i in vetor:
    if i not in vogal:
        soma=soma+aux
        cons.append(i)

print("total de consoantes: %i" %soma)
print(cons)