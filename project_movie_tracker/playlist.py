from dataclasses import dataclass
from dataclasses import field
from movie import Movie
from serie import Serie
from operator import attrgetter


@dataclass
class Playlist:
    nome: str
    descricao: str
    filmes: list[Movie] = field(default_factory=list)
    # series: list[Serie] = field(default_factory=list)

    def adicionar_filme(self, filme: Movie):
        if filme not in self.filmes:
            self.filmes.append(filme)
            print(f'Filme {filme.titulo} adicionado com sucesso do objeto da playlist {self.nome}')
    
    def remover_filme(self, filme: Movie):
        if filme in self.filmes:
            print(f'Filme {filme.titulo} removido com sucesso')
            self.filmes.remove(filme)
        else:
            print(f'Filme {filme.titulo} não encontrado na playlist')

if __name__ == '__main__':
    filme1 = Movie('Demolidor', 2005, 'Dennis', 7.80, True)
    filme2 = Movie('Transformers', 1894, 'Michael', 9.80)
    filme3 = Movie('Transformers', 1894, 'Michael', 6.80)

    play = Playlist('Biggest', 'A maior playlist')
    play2 = Playlist('Greatest', 'A maior playlist')

    print(play)
    print(play2)
    print(f'Objeto {id(play)} é igual que {id(play2)}? {play.__eq__(play2)}')

    
    print('=' * 20 + 'Adiciona Filmes' + '=' * 20)
    play.adicionar_filme(filme1)
    play.adicionar_filme(filme2)
    play.adicionar_filme(filme3)
    print(play)
    
    print('=' * 20 + 'Lista Filmes' + '=' * 20)
    print(play.filmes)
    
    print('=' * 20 + 'Ordenar Filmes' + '=' * 20)
    play.ordenar()
    print(f'Ordenando {play.filmes}')
    
    print('=' * 20 + 'Adiciona Filmes' + '=' * 20)
    play2.adicionar_filme(filme2)
    print(play2)
    print('=' * 20 + 'Remover Filmes' + '=' * 20)
    play2.remover_filme(filme2)
    print(play2)