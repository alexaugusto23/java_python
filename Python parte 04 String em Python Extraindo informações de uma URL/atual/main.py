url = "https://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"


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