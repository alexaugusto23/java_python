url = "https://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"
ind_interrogacao = url.find('?')
url_base = url[0:ind_interrogacao]
url_parametros = url[ind_interrogacao+1:]
#print(f"{url_parametros}")
# url_parametros = url[ind_interrogacao+1:len(url)]

parametro_busca_origem = 'moedaOrigem'
parametro_busca_destino = 'moedaDestino'
parametro_busca_e = '&'
parametro_busca_equals = '='

indice_parametro = url_parametros.find(parametro_busca_origem)
indice_valor = indice_parametro + len(parametro_busca_origem) + 1
moedaOrigem = url_parametros[indice_valor:]
print(f"Moeda Origem: {moedaOrigem}")


indice_parametro = url_parametros.find(parametro_busca_destino)
indice_parametro_final = url_parametros.find(parametro_busca_e)
indice_valor = len(parametro_busca_destino) + 1
moedaDestino = url_parametros[indice_valor:indice_parametro_final]
print(f"Moeda Destino: {moedaDestino}")

