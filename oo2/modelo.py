class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano 
        self.duracao = duracao
        self.__likes = 0
    
    def
    
    def dar_like(self):
        self.__likes +=1


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_like()
print(f'\nNome: {vingadores.nome}'
      f'\nAno: {vingadores.ano}'
      f'\nDuração: {vingadores.duracao}'
      f'\nLikes: {vingadores.likes}')

class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano 
        self.temporadas = temporadas
        self.__likes = 0

    def dar_like(self):
        self.__likes +=1

atantla = Serie('atantla', 2017, 2)
atantla.dar_like()
atantla.dar_like()
print(f'\nNome: {atantla.nome}'
      f'\nAno: {atantla.ano}'
      f'\nTemporadas: {atantla.temporadas}'
      f'\nLikes: {atantla.likes}')
