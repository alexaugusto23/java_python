path_main = r'C:\Users\alexsandro.ignacio\OneDrive - WCA Soluções de Inteligência Comercial\Documentos\Docs\Git\python_alura\Python parte 11 IO'

arquivo1 = open(file= path_main +'/dados/contatos-escrita.csv', encoding='latin_1', mode='w', )
arquivo2 = open(file= path_main +'/dados/contatos-escrita.csv', encoding='latin_1', mode='a', )

contato_carol = '11,Carol,carol@carol.com.br\n'
contato_andreza = '12,Andreza,andreza@andreza.com.br\n'

arquivo1.write(contato_carol)
arquivo2.write(contato_andreza)

arquivo1.close()
arquivo2.close()