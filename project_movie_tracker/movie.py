from dataclasses import dataclass
from dataclasses import field
from operator import attrgetter
from genre_enum import Genero

@dataclass
class Movie:
    titulo: str
    ano: int
    diretor: str
    imdb_rating: float
    visto: bool = False
    generos: list[Genero] = field(default_factory=list)

    def __post_init__(self):
        if self.ano < 1895:
            print("O ano de lançamento do filme deve ser maior ou igual a 1895.")

    def adicionar_genero(self, genero: Genero):
        if genero not in self.generos:
            self.generos.append(genero)
            print(f'Gênero(s) {genero} adicionado ao filme {self.titulo}')

## Não é uma boa prática usar main junto com dataclass
if __name__ == '__main__':
    filme1 = Movie('Demolidor', 2005, 'Dennis', 7.80, True)
    filme2 = Movie('Transformers', 1894, 'Michael', 9.80)

    
    filme1.adicionar_genero(Genero.ACAO.name)
    filme1.adicionar_genero(Genero.TERROR.name)
    print(filme1)

    print('=' * 50)

    filme2.adicionar_genero(Genero.AVENTURA.name)
    filme2.adicionar_genero(Genero.FICCAO_CIENTIFICA.name)

    print(filme2)

    print(filme1.__eq__(filme1))

    lista_filmes = [filme1, filme2]
    lista_filmes.sort(key=attrgetter("imdb_rating"))

    for filme in lista_filmes:
        print(f"{filme.titulo} - IMDb Rating: {filme.imdb_rating}") 

    lista_filmes.sort(key=attrgetter("imdb_rating"), reverse=True) 

    for filme in lista_filmes:
        print(f"{filme.titulo} - IMDb Rating: {filme.imdb_rating}") 