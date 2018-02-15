import urllib.request

#DÓLAR#
conteudo = urllib.request.urlopen("https://www.melhorcambio.com/dolar-hoje").read()
conteudo = str(conteudo)
procura = '<input type="hidden" value="'
posicao = int(conteudo.index(procura) + len(procura))
dolar = conteudo[ posicao : posicao + 4 ]

#EURO#
conteudo = urllib.request.urlopen("https://www.melhorcambio.com/euro-hoje").read()
conteudo = str(conteudo)
procura = '<input type="hidden" value="'
posicao = int(conteudo.index(procura) + len(procura))
euro = conteudo[ posicao : posicao + 4 ]

#TEMPERATURA MÁXIMA#
conteudo = urllib.request.urlopen("https://www.climatempo.com.br/previsao-do-tempo/cidade/364/riogrande-rs").read()
conteudo = str(conteudo)
procura = 'tempMax0">'
posicao = int(conteudo.index(procura) + len(procura))
maxima = conteudo[ posicao : posicao + 2 ]

#TEMPERATURA MÍNIMA##
conteudo = urllib.request.urlopen("https://www.climatempo.com.br/previsao-do-tempo/cidade/364/riogrande-rs").read()
conteudo = str(conteudo)
procura = 'tempMin0">'
posicao = int(conteudo.index(procura) + len(procura))
minima = conteudo[ posicao : posicao + 2 ]

print('Dólar: {}'.format(dolar, 'utf-8'))
print('Euro: {}'.format(euro, 'utf-8'))
print('Temperatura Máxima {}'.format(maxima + '°C', 'utf-8'))
print('Temperatura Máxima {}'.format(minima + '°C', 'utf-8'))