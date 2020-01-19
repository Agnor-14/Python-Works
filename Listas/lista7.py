lista = []
soma = 0
multiplicacao = 1

for numero in range(1,6):
    soma += numero
    multiplicacao *= numero
    lista.append(numero)

print("Soma: %i" %soma +"\n"+ "Multiplicação: %i" %multiplicacao +"\n")

for numero in lista:
    print(numero)