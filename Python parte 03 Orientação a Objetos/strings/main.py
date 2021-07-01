from extratoargumentosurl import ExtratoArgumentosUrl

url = "https://www.bytebank.com.br/cambio?moedaorigem=moedadestino&moedadestino=dolar&valor=1500"

argumentosUrl = ExtratoArgumentosUrl(url)
#print(argumentosUrl)

moedaOrigem, moedaDestino = argumentosUrl.extrai_argumentos()
valor = argumentosUrl.extrai_valor()
print(moedaDestino,moedaOrigem, valor)

print(len(argumentosUrl))
print(argumentosUrl)
print()

a = "https://www.bytebank.com.br"
b = "https://www.bytebank.com.br1"

url_1 = ExtratoArgumentosUrl(a)
url_2 = ExtratoArgumentosUrl(b)


print(url_1 == url_2)




