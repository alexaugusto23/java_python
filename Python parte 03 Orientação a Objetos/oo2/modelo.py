class Programa:
    def __init__(self, nome, ano):
        self.__nome = nome.title()
        self.ano = ano
        self.__likes = 0 #encapsulamento __likes        

    @property #decorador ou decorator
    def likes(self):
        return self.__likes
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()
        return
    
    def dar_like(self):
        self.__likes += 1
          
    def __str__(self):#polimorfismo
        return f"{self.nome} - {self.ano} - {self.likes}"

        
 
class Filme(Programa):#herança
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
    
    def __str__(self):#polimorfismo
        str = "minutos"
        lk = "like" if self.likes <= 1 else "likes"
        return f"{self.nome} - {self.ano} - {self.likes} {lk} - {self.duracao} {str}"
                 
class Serie(Programa):#herança
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
    
    #dunder methods
    def __str__(self):#polimorfismo
        str = "temporada" if self.temporadas <= 1 else "temporadas"
        lk = "like" if self.likes <= 1 else "likes"
        return f"{self.nome} - {self.ano} - {self.likes} {lk} - {self.temporadas} {str}"

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome.title()
        self._programas = programas

    @property
    def listagem(self):
        return self._programas

    #duck typing
    def __getitem__(self, item):
        return self._programas[item]
    
    #dunder methods
    def __len__(self):
        return len(self._programas)
    
 

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
et = Filme('et', 1990, 140)
atlanta = Serie('atlanta', 2018, 2)
secret_key = Serie('secret key', 2017, 1)

filmes_e_series = [vingadores, et, atlanta, secret_key]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)


atlanta.dar_like()
atlanta.dar_like()
vingadores.dar_like()
et.dar_like()

print(f"\nTamanho playlist: {len(playlist_fim_de_semana)}")
print("\n")
for programa in playlist_fim_de_semana:
    print(programa)
print("\n")

print(f"Tá ou não está? {et in playlist_fim_de_semana}\n")


'''
Python Data Model

Inicialização: __init__
Representação: __str__, __repr__
Container, sequência: __contains__, __iter__, __len__, __getitem__
Númericos: __add__, __sub__, __mul__, _mod__
'''