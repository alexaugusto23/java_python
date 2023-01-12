path_main = r'C:\Users\alexsandro.ignacio\OneDrive - WCA Soluções de Inteligência Comercial\Documentos\Docs\Git\python_alura\Python parte 11 IO'

try:
    arquivo_contatos = open(file= path_main +'/dados/não-existe.csv', encoding='latin_1', mode='w+')
    for linha in arquivo_contatos:
        print(linha,end='')

except FileNotFoundError:
    print('Arquivo não encontrado')

except NameError:
    print('Variável não definida')

except PermissionError:
    print('Sem prermissão de escrita')

finally:
    arquivo_contatos.close()
