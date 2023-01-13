from abc import ABC, abstractmethod
from contatoDao import ContatoDao
from contato import Contato
import csv

class ContatoDaoCSV(ContatoDao):

    @abstractmethod
    def buscar_todos(self, caminho: str, encoding: str ='latin-1') -> list:
        contatos = []
        
        with open(caminho, encoding=encoding) as arquivo:  
            leitor = csv.reader(arquivo)
            for linha in leitor:
                id, nome, email = linha # ['1', 'Guilherme', 'guilherme@guilherme.com.br']
                contato = Contato(id, nome, email)
                contatos.append(contato)
        
        return contatos

    @abstractmethod
    def salvar(self, contatos, caminho, encoding='latin_1'):
        with open(caminho, encoding, mode='w+') as arquivo:
            arquivo.write(contatos)

    @abstractmethod
    def adicionar(self, contatos, caminho, encoding='latin_1'):
        with open(caminho, encoding, mode='a+') as arquivo:
            arquivo.write(contatos)
            






