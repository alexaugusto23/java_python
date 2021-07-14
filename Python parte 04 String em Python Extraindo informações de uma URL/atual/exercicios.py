url = "https://bytebank.com/cambio?moedaOrigem=real"
ind_interrogacao = url.find('?')
url_base = url[0:ind_interrogacao]
url_parametros = url[20:]
url_parametros = url[ind_interrogacao+1:]
url_parametros = url[ind_interrogacao+1:len(url)]

print(f"\nURL: {url}\n\nURL_base: {url_base}\n\nURL_parametros: {url_parametros}\n")
print(f"{url}")

###########################################################

nome_completo = "Gabriel Saldanha"
primeiro_nome = nome_completo[0:7]
ultimo_nome = nome_completo[8:16]
#print(f"{primeiro_nome} {ultimo_nome}")

###########################################################
url = ''
if len(url) > 0:
    print("A URL contél algum valor")
else:
    print("A URL está vazia!")

if len(url) == 0:
    print("A URL está vazia!")

###########################################################

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
# print(f"Moeda Origem: {moedaOrigem}")


indice_parametro = url_parametros.find(parametro_busca_destino)
indice_parametro_final = url_parametros.find(parametro_busca_e)
indice_valor = len(parametro_busca_destino) + 1
moedaDestino = url_parametros[indice_valor:indice_parametro_final]
# print(f"Moeda Destino: {moedaDestino}")

parametro_de_busca = 'moedaOrigem'
indice_de_parametro = url_parametros.find(parametro_de_busca)
indice_de_valor = indice_de_parametro + len(parametro_de_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_de_valor)
valor = url_parametros[indice_de_valor:indice_e_comercial]

if indice_e_comercial == -1:
    valor = url_parametros[indice_de_valor:]
else:
    valor = url_parametros[indice_de_valor:indice_e_comercial]

print(valor)

###########################################################

url = "https://www.alura.com.br/curso?curso=python"
indice_curso = url.find("curso")
indice_valor = indice_curso + len("curso") + 1
valor = url[indice_valor:]
print(valor)

###########################################################

url = "https://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"

# Sanitização da URL
url = url.replace(" ", "")
url = url.strip()

# Validação da URL
if url == None:
    raise ValueError("A URL None") 
elif url == "":
    raise ValueError("A URL está vazia") 
else:
    parametro_de_busca = 'moedaDestino'
    indice_de_parametro = url.find(parametro_de_busca)
    indice_de_valor = indice_de_parametro + len(parametro_de_busca) + 1
    indice_e_comercial = url.find('&', indice_de_valor)
    valor = url[indice_de_valor:indice_e_comercial]

    if indice_e_comercial == -1:
        valor = url[indice_de_valor:]
    else:
        valor = url[indice_de_valor:indice_e_comercial]
    print(valor)

###########################################################
###########################################################
###########################################################
###########################################################