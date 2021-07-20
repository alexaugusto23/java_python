
"""
Funções em Python são blocos de código que executarão 
algum tipo de tarefa ou manipulação de dados, podendo 
ou não receber: dados de entrada (parâmetros/argumentos).
Parâmetros: são os nomes dados aos atributos que uma 
função pode receber. Definem quais argumentos são aceitos 
por uma função, podendo ou não ter um valor padrão (default).
Argumentos: são os valores que realmente são 
passados para uma função.
"""

def calculadora_salario(valor, horas=220):
    return horas * valor

valor_total = calculadora_salario(299.25)

print(valor_total)

"""
*args
É usado para passar um lista de argumentos variável sem 
palavras-chave em forma de tupla, pois a função que o 
recebe não necessariamente saberá quantos argumentos 
serão passados.
"""

def func_args(*args):
    print(f'tipo: {type(args)} conteúdo: {args}')
    for arg in args:
        print(f'tipo: {type(arg)} conteúdo: {arg}')


"""
**kwargs
Como a abreviação sugere, kwargs significa keyword 
arguments (argumentos de palavras chave). Ele permite 
passar um dicionário com inúmeras keys para a função.
"""

func_args(1, 'A', {'valor': 10})

def func_kwargs(**kwargs):
    print(f'tipo: {type(kwargs)} contuedo: {kwargs}')
    for key, value in kwargs.items():
        print(f'atributo: {key}, valor: {value}')

func_kwargs(nome='James', sobrenome='Bond', cargo='Agente 007')


"""
Outra forma de passar um dicionário já existente é 
usando os ** na passagem do parâmetro:
"""
parms = {
          'nome': 'James', 
          'sobrenome': 'Bond', 
          'cargo': 'Agente 007'
        }
func_kwargs(**parms)


def func_missao_dificil(nome, *args, funcao='agente', **kwargs):
    print(f'Nome do agente: {nome}')
    print(f'Função: {funcao}')
    print(args)
    print(kwargs)

params = {
            'id_agente': '007',
            'proxima_missao': 'Impossível'
         }

func_missao_dificil(
    'James Bond',
    'Missao 1',
    'Missão 2',
    **params
)

"""
No exemplo acima, usamos todos os recursos mencionados 
no post:
O parâmetro nome recebe o valor “James Bond”;
O parâmetro função utilizou o valor “agente” 
definido como default;
O parâmetro args recebeu os valores “Missao 1” e 
“Missao 2” como tupla;
O parâmetro kwargs recebeu dois parâmetros nomeados 
como dicionário: {‘id_agente’: ‘007’, 
‘proxima_missao’: ‘Impossível’}
"""