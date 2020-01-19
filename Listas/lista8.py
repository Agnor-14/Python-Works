i = 0
idades = []
alturas = []

while i<5:
    idade = int(input("Idade: "))
    altura = float(input("Altura: "))

    idades.append(idade)
    alturas.append(altura)

    i+=1

print(idades)
print(alturas)

print("Inversão")

idades.reverse()
alturas.reverse()

print(idades)
print(alturas)