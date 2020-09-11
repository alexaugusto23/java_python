class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano 
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def likes(self):
        return self._likes
    
    def dar_like(self):
        self._likes +=1


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        self._nome = nome.title()
        self.ano = ano 
        self.duracao = duracao
        self._likes = 0


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        self._nome = nome.title()
        self.ano = ano 
        self.temporadas = temporadas
        self._likes = 0


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_like()
print(f'\nNome: {vingadores.nome}'
      f'\nAno: {vingadores.ano}'
      f'\nDuração: {vingadores.duracao}'
      f'\nLikes: {vingadores.likes}')

atantla = Serie('atantla', 2017, 2)
atantla.dar_like()
atantla.dar_like()
print(f'\nNome: {atantla.nome}'
      f'\nAno: {atantla.ano}'
      f'\nTemporadas: {atantla.temporadas}'
      f'\nLikes: {atantla.likes}')
