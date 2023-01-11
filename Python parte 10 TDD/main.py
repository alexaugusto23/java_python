# TDD - Test-driven development
# https://www.alura.com.br/artigos/tipos-de-testes-principais-por-que-utiliza-los
# https://www.alura.com.br/artigos/por-que-e-o-que-e-possivel-testar
# https://www.alura.com.br/artigos/testes-com-mocks-e-stubs

# Quando o python não encontrar o modulo usar esta função que adiciona no path o caminho do modulo.
import sys
sys.path.append(r'C:/Users/alexsandro.ignacio/OneDrive - WCA Soluções de Inteligência Comercial/Documentos/Docs/Git/python_alura/Python parte 10 TDD')

from codigo.bytebank import Funcionario

# lucas = Funcionario('Lucas Carvalho', '13/03/2000', 1000)
# print(lucas)
# print(lucas.idade())

# def teste_idade():
#     funcionario_teste = Funcionario('Teste', '13/03/2000', 1111)
#     print(f"Teste = {funcionario_teste.idade()}")

#     funcionario_teste1 = Funcionario('Teste', '13/03/1999', 1111)
#     print(f"Teste1 = {funcionario_teste1.idade()}")

#     funcionario_teste2 = Funcionario('Teste', '01/12/2000', 1111)
#     print(f"Teste2 = {funcionario_teste2.idade()}")

# teste_idade()



ana = Funcionario('Ana', '12/03/1997', 10000000)
print(ana.calcular_bonus())


