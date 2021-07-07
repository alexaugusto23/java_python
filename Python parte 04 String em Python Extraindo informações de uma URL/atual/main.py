url = "https://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"
ind_interrogacao = url.find('?')
url_base = url[0:ind_interrogacao]
url_parametros = url[ind_interrogacao+1:]
#print(f"{url_parametros}")
# url_parametros = url[ind_interrogacao+1:len(url)]

parametro_busca = 'moedaOrigem'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
moedaOrigem = url_parametros[indice_valor:]
print(f"{url_parametros}")
print(f"{indice_parametro}")
print(f"len: {indice_valor}")
print(moedaOrigem)

parametro_busca = 'moedaDestino'
parametro_busca_dois = '&'
indice_parametro = url_parametros.find(parametro_busca)
indice_parametro_final = url_parametros.find(parametro_busca_dois)
indice_valor = len(parametro_busca) + 1
moedaDestino = url_parametros[indice_valor:indice_parametro_final]
print(moedaDestino)
