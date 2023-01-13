import csv, pickle, json
from contato import Contato

def csv_para_contatos(caminho: str, encoding: str ='latin-1') -> list:
    """
    Função para leitura de arquivo e 
    retorno de lista com os dados lidos.

    Parâmetros:
		caminho (str): String
		encoding (str): String default latin_1

	Retorno:
		contatos (list): Lista de contatos
    """
    contatos = []
    
    with open(caminho, encoding=encoding) as arquivo:  
        leitor = csv.reader(arquivo)
        for linha in leitor:
            id, nome, email = linha # ['1', 'Guilherme', 'guilherme@guilherme.com.br']
            contato = Contato(id, nome, email)
            contatos.append(contato)
    
    return contatos

def write_contatos_para_pickle(contatos, caminho):
    with open(caminho, mode='wb') as arquivo:
        pickle.dump(contatos, arquivo)

def read_pickle_para_contatos(caminho) :
    with open(caminho, mode='rb') as arquivo:
        contatos = pickle.load(arquivo)
    return contatos

def write_contatos_para_json(contatos, caminho):
    with open(caminho, mode='w') as arquivo:
        json.dump(contatos, arquivo, default=_contato_para_json)
        # com lambda json.dump(contatos, arquivo, default=lambda contato: contato.__dict__)

def _contato_para_json(contato):
    return contato.__dict__

def read_json_para_contatos(caminho):
    contatos = []
    with open(caminho) as arquivo:
        contatos_json = json.load(arquivo)

        for contato in contatos_json:
            # c = Contato(contato['id'], contato['nome'], contato['email'] )
            c = Contato(**contato) # usando desempacotamento com **
            contatos.append(c)

    return contatos