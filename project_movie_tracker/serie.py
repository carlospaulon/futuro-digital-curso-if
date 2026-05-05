from season import Season
from genre_enum import Genero
from dataclasses import dataclass, field

@dataclass
class Serie:
    title: str
    watched: bool = False
    imdb_rating: float = 0.0
    seasons: list[Season] = field(default_factory=list)
    generos: list[Genero] = field(default_factory=list)

    def adicionar_genero(self, genero: Genero):
        if genero not in self.generos:
            self.generos.append(genero)
            print(f'Gênero(s) {genero} adicionado ao filme {self.title}')
        
    def adicionar_temporada(self, season: Season):
        if season not in self.seasons:
            self.seasons.append(season)
            print(f'Temporada de {season.year} adicionado a série {self.title}')

    def verificar_assistido(self):
        for season in self.seasons:
            if season.verificar_assistido():
                self.watched = True
            else:
                self.watched = False
                break
        return self.watched