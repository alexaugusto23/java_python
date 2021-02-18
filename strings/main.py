from extratoargumentosurl import ExtratoArgumentosUrl

url = "https://www.bytebank.com.br/cambio?moedaorigem=moedadestino&moedadestino=dolar&valor=1500"

argumentosUrl = ExtratoArgumentosUrl(url)
#print(argumentosUrl)

moedaOrigem, moedaDestino = argumentosUrl.extrai_argumentos()
valor = argumentosUrl.extrai_valor()
print(moedaDestino,moedaOrigem, valor)




