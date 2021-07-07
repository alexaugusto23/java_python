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