from abc import ABC, abstractmethod
from contatoDao import ContatoDao
from contato import Contato
import pickle

class ContatoDaoPickle(ContatoDao):

    @abstractmethod
    def buscar_todos(self, caminho):
        with open(caminho, mode='rb') as arquivo:
            contatos = pickle.load(arquivo)
        return contatos

    @abstractmethod
    def salvar(self, contatos, caminho):
        with open(caminho, mode='wb') as arquivo:
            pickle.dump(contatos, arquivo)