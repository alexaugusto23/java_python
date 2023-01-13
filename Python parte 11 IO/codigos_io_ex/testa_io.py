path_main = r'C:\Users\alexsandro.ignacio\OneDrive - WCA Soluções de Inteligência Comercial\Documentos\Docs\Git\python_alura\Python parte 11 IO'

arquivo = open(file= path_main +'/dados/contatos.csv', encoding='latin_1')
print(type(arquivo))
print(type(arquivo.buffer)) 

conteudo = arquivo.buffer.read()
print(conteudo)

# texto_em_bytes = b'Esse é um texto em bytes'
texto_em_bytes = bytes('Esse é um texto em bytes','latin_1')
print(type(texto_em_bytes))
print(texto_em_bytes)
  
arquivo.close()
