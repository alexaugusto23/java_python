path_main = r'C:\Users\alexsandro.ignacio\OneDrive - WCA Soluções de Inteligência Comercial\Documentos\Docs\Git\python_alura\Python parte 11 IO'
contato_carol = '11,Carol,carol@carol.com.br\n'
contato_andreza = '12,Andreza,andreza@andreza.com.br\n'

with open(file= path_main +'/dados/contatos-escrita.csv', encoding='latin_1', mode='w', ) as arquivo1:
    arquivo1.write(contato_carol)

with open(file= path_main +'/dados/contatos-escrita.csv', encoding='latin_1', mode='a', ) as arquivo2:
    arquivo2.write(contato_andreza)