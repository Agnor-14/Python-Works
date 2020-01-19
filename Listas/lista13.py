temperaturas = []
mes = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']

def mediaAnual(temperaturas):
    soma = 0
    for temperatura in temperaturas:
        soma += temperatura
    media = soma/len(temperaturas)
    return media

def devidoMes(indexTemp):
    retornaMes = mes[indexTemp]
    return retornaMes

def tempAcimaMediaAnual(temperaturas,mediaAnual):
    for temperatura in temperaturas:
        if temperatura > mediaAnual:
            indexTemp = temperaturas.index(temperatura)
            mesMedAnual = devidoMes(indexTemp)
            print("\nTemperatura maior que a media anual: {} , aconteceu em {}\n".format(temperatura,mesMedAnual))
            temperaturas.insert(indexTemp,1)
            novoIndex = indexTemp + 1
            del(temperaturas[novoIndex])

while len(temperaturas) < 12:
    tempMedia = float(input("\nEntre com a Temperatura média dos mês: "))
    temperaturas.append(tempMedia)

med = mediaAnual(temperaturas)

tempAcimaMediaAnual(temperaturas,med)