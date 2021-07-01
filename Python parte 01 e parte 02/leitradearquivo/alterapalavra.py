
ler_arquivo = open('insert.txt', encoding="utf-8")
for linha in ler_arquivo:
    linha = linha.split()
    if ('banco' in linha.islower()):
        linha[2].replace("banco","tb_banco")
    print(linha)
    
ler_arquivo.close()

