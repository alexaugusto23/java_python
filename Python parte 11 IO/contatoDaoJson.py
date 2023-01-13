from abc import ABC, abstractmethod
from contatoDao import ContatoDao
from contato import Contato
import json

class ContatoDaoJSON(ContatoDao):

    @abstractmethod
    def buscar_todos(caminho):
        contatos = []
        with open(caminho, mode='r') as arquivo:
            contatos_json = json.load(arquivo)
            for contato in contatos_json:
                c = Contato(**contato)
                contatos.append(c)

        return contatos   

    @abstractmethod
    def salvar( contatos, caminho):
        with open(caminho, mode='w') as arquivo:
            json.dump(contatos, arquivo, default=lambda objeto: objeto.__dict__) 
