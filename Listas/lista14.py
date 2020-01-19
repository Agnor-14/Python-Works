perguntas = [
                '\nTelefoneu para vítima?','\nEsteve no local do crime?','\nMora perto da vítima?','\nDevia para a '
                                                                                                   'vítima?',
                '\nJá trabalhou com a vítima?'
            ]

contador = 0

for pergunta in perguntas:
    print(pergunta)
    resposta = input("\nResposta (s/n):")

    if resposta == 's':
        contador += 1

if contador == 2:
    print("\nVocê é suspeita!\n")
elif 3 <= contador <= 4:
    print("\nPrendam... É cúmplice!\n")
elif contador >= 5:
    print("\nÉ O ASSASSINO!!!\n")
else:
    print("\nFique tranquilo, você é inocente!\n")