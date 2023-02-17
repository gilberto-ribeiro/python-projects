class Programa:
    def __init__(self, nome, ano):
        self._nome = nome
        self._ano = ano
        self._likes = 0
    
    def dar_likes(self, likes = 1):
        self._likes += likes

    def __str__(self):
        return 'Nome: {} | Ano: {} | Duração: {} | Likes: {}'.format(self.nome, self.ano, self.likes)

    prefixo = 'Programa'

    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome.title()
    
    @property
    def ano(self):
        return self._ano
    

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self._duracao = duracao

    prefixo = 'Filme'

    @property
    def duracao(self):
        return self._duracao
    
    def __str__(self):
        return 'Nome: {} | Ano: {} | Duração: {} | Likes: {}'.format(self.nome, self.ano, self.duracao, self.likes)
    

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self._temporadas = temporadas

    prefixo = 'Série'
    
    @property
    def temporadas(self):
        return self._temporadas
    
    def __str__(self):
        return 'Nome: {} | Ano: {} | Temporadas: {} | Likes: {}'.format(self.nome, self.ano, self.temporadas, self.likes)
    

class Playlist():
    def __init__(self, nome, programas):
        self.nome = nome.title()
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas
    
    @property
    def tamanho(self):
        return len(self._programas)


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
tmep = Filme('todo mundo em panico', 2017, 80)
atlanta.dar_likes()
atlanta.dar_likes()
tmep.dar_likes(15)
# print(f'Nome: {vingadores.nome} - Likes: {vingadores.likes}')
# print(f'Nome: {atlanta.nome} - Likes: {atlanta.likes}')
demolidor = Serie('demolidor', 2018, 3)
demolidor.dar_likes(7)
programas = [vingadores, atlanta, tmep]

playlist_fim_de_semana = Playlist('playlist para assistir em casa', programas)

print(f'Tamanho da playlist: {playlist_fim_de_semana.tamanho}.')
for programa in playlist_fim_de_semana:
    print(programa)

print(f'Demolidor está na playlist? {demolidor in playlist_fim_de_semana}')

print('Este é o nome da playlist: {}'.format(playlist_fim_de_semana.nome))