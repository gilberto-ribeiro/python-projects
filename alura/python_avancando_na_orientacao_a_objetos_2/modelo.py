class Programa:
    pass


class Filme:

    def __init__(self, nome, ano, duracao):
        self.__nome = nome
        self.__ano = ano
        self.__duracao = duracao
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome.title()
    
    @property
    def ano(self):
        return self.__ano
    
    @property
    def duracao(self):
        return self.__duracao
    
    def dar_like(self):
        self.__likes += 1
    
    def informacoes(self):
        print(f'''Nome: {self.nome}
Ano: {self.ano}
Duração: {self.duracao} min
Likes = {self.__likes}
''')


class Serie:

    def __init__(self, nome, ano, temporadas):
        self.__nome = nome
        self.__ano = ano
        self.__temporadas = temporadas
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome.title()
    
    @property
    def ano(self):
        return self.__ano
    
    @property
    def temporadas(self):
        return self.__temporadas
    
    def dar_like(self):
        self.__likes += 1
    
    def informacoes(self):
        print(f'''Nome: {self.nome}
Ano: {self.ano}
Temporadas: {self.temporadas} min
Likes = {self.__likes}
''')