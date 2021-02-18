url = "https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=1500"

# métodos find, split

index = url.find("=")
print(index)
print(url[index])
substring = url[index + 1:]
print(substring)
lista_args = url.split("=")
print(lista_args)


celular = "(41)96574-1728"
indiceInicialCodigoArea = celular.find("(")+1
indiceFinalCodigoArea   = celular.find(")")
print(indiceInicialCodigoArea)
print(indiceFinalCodigoArea)
print(celular[indiceInicialCodigoArea:indiceFinalCodigoArea])

string = 0

print(string is None)

if string:
    print("Tem algo aqui!!!")
else:
    print("Não tem algo aqui!!!")

index_inicio  = url.find("moedadestino") + len("moedadestino") + 1
index_final = url.find("&", 52)
print(url[index_inicio:index_final],' ', index_inicio, ' ', index_final)