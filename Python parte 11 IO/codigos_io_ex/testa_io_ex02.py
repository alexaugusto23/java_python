path_main = r'C:\Users\alexsandro.ignacio\OneDrive - WCA Soluções de Inteligência Comercial\Documentos\Docs\Git\python_alura\Python parte 11 IO'

arquivo = open(file= path_main +'/dados/contatos-escrita.csv', encoding='latin_1', mode='w')

print(type(arquivo.buffer)) 

texto_em_bytes = bytes('Esse é um texto em bytes','latin_1')
# print(type(texto_em_bytes))
# print(texto_em_bytes)

contato = bytes('15,Vêronica,veronica@veronica.com.br\n', 'latin_1')
arquivo.buffer.write(contato)


arquivo.close()
