url = "https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=1500"
'''
# métodos find, split, replace

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


nome       = 'Eren Yeager'
tamanho = len(nome)
indice      = nome.find('Eren')
print(indice)
print(nome[indice])
print(tamanho)
print(nome[indice:tamanho])

string_replace = "bytebank"
string_nova = string_replace.replace("byte","alex",1)
print(string_replace)
print(string_nova)

print()
banco1 = "bytebank"
banco2 = "Bytebank".upper()
print(banco1, ' - ', banco2)
print(banco1 == banco2)
'''
url_byte_bank = "https://bytebank.com"
url1          = "https://buscasites.com/busca?q=https://bytebank.com"
url2          = "https://bitebank.com.br"
url3          = "https://bytebank.com/cambio/teste/teste"

print(url3.find(url_byte_bank))
print(url2.startswith(url_byte_bank))











