class Filme():
    def __init__(self, titulo, diretor):
        self.titulo = titulo
        self.diretor = diretor
    
    def __str__(self):
        return self.titulo + ' - ' + self.diretor

 
    def __eq__(self, outro_filme):
        return self.titulo == outro_filme.titulo

filme_procurado = Filme('A Teoria de Tudo', 'James Marsh')
filme_procurado2 = Filme('O Artista', 'robert')


print(filme_procurado.titulo==filme_procurado.titulo)      