path_main = r'C:\Users\alexsandro.ignacio\OneDrive - WCA Soluções de Inteligência Comercial\Documentos\Docs\Git\python_alura\Python parte 11 IO'

try:
    with open(file= path_main +'/dados/contatos.csv', encoding='latin_1') as arquivo_contatos:
        for linha in arquivo_contatos:
            print(linha,end='')
except FileNotFoundError:
    print('Arquivo não encontrado')
except PermissionError:
    print('Sem prermissão de escrita')

