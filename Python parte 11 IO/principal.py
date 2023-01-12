path_main = r'C:\Users\alexsandro.ignacio\OneDrive - WCA Soluções de Inteligência Comercial\Documentos\Docs\Git\python_alura\Python parte 11 IO'
arquivo_contatos = open(file= path_main +'/dados/contatos.csv', encoding='latin_1')

# Lê todas as uma linhas
conteudo = arquivo_contatos.readlines()

print(f"\n{conteudo}\n")

for linha in conteudo:
    print(linha)

for linha in conteudo:
    print(linha,end='')

arquivo_contatos.close()

# Lê somente uma linha
arquivo_contatos = open(file= path_main +'/dados/contatos.csv', encoding='latin_1')
conteudo = arquivo_contatos.readline() # Lê a primeira linha
print(f"\n{conteudo}\n")
conteudo = arquivo_contatos.readline() # Lê a segunda linha
print(f"\n{conteudo}\n")

conteudo = arquivo_contatos.readline(10) # Lê a terceira linha somente os 10 primeiro caracteres
print(f"\n{conteudo}\n")

conteudo = arquivo_contatos.readline() # Lê o restante
print(f"\n{conteudo}\n")

arquivo_contatos.close()

try:
    arquivo_contatos = open(file= path_main +'/dados/contato.csv', encoding='latin_1')
    for linha in arquivo_contatos:
        print(linha,end='')
finally:
    arquivo_contatos.close()
