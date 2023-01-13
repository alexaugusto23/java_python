from contatoDaoCsv import ContatoDaoCSV
from contatoDaoPickle import ContatoDaoPickle
from contatoDaoJson import ContatoDaoJSON

path_main = r'C:\Users\alexsandro.ignacio\OneDrive - WCA Soluções de Inteligência Comercial\Documentos\Docs\Git\python_alura\Python parte 11 IO'
path = path_main +'/dados/contatos.csv'
path_pickle = path_main +'/dados/contatos.pickle'
path_json = path_main +'/dados/contatos.json'

try: 

    contatos = ContatoDaoJSON.buscar_todos(path_json) 

    for contato in contatos:
        print(f"{contato.id} - {contato.nome} - {contato.email}")

except FileNotFoundError:
    print('Arquivo não encontrado')
except PermissionError:
    print('Sem prermissão de escrita')
