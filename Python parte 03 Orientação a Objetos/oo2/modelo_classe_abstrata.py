from abc import ABC # abstract base classes
from collections.abc import MutableSequence
from numbers import(Complex)


class Playlist(MutableSequence):
    pass


class Numero(Complex):
    def __getitem__ (self, item):
        super().__getitem__()


from abc import ABCMeta, abstractmethod 
class Programa(metaclass = ABCMeta): 
    @abstractmethod 
    def __str__(self): 
        pass

filmes = Playlist()
num = Numero()