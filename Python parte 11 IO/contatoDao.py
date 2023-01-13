from abc import ABC, abstractmethod

class ContatoDao(ABC):

    @abstractmethod
    def buscar_todos(self, caminho):
        pass

    @abstractmethod
    def salvar(self, contatos, caminho):
        pass