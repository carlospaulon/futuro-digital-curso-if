from serie import Serie
from season import Season
from chapter import Capitulo
from datetime import datetime
from genre_enum import Genero

class Main:
    if __name__ == '__main__':
        date = datetime.now()
        print(date)
        chapter = Capitulo('Born Again', 1, datetime(2019, 2, 21))
        chapter2 = Capitulo('Teste', 2, date)
        chapter3 = Capitulo('Teste3', 3, date)
        chapter4 = Capitulo('Teste4', 4, date)
        chapter5 = Capitulo('Teste5', 5, date)
        
        seasons = Season(2015, False)
        seasons.add_chapters(chapter)
        seasons.add_chapters(chapter2)
        seasons.add_chapters(chapter3)
        seasons.add_chapters(chapter4)
        seasons.add_chapters(chapter5)
        print('=' * 40)
        print(f'Temporada 1: {seasons.capitulos}')
        print('=' * 40)

        print(chapter2.marcar_como_visto())
        print(chapter.watched)
        print(chapter2.watched)

        chapter6 = Capitulo('Segunda temporada 6', 6, date)
        chapter7 = Capitulo('Segunda temporada 7', 7, date)
        chapter8 = Capitulo('Segunda temporada 8', 8, date)
        seasons2 = Season(2016, False)
        seasons2.add_chapters(chapter6)
        seasons2.add_chapters(chapter7)
        seasons2.add_chapters(chapter8)
        print('=' * 40)
        print(f'Temporada 2: {seasons2.capitulos}')
        print('=' * 40)

        serie = Serie('Demolidor', True, 9.9, [seasons, seasons2])
        serie.adicionar_genero(Genero.ACAO.name)
        serie.adicionar_genero(Genero.AVENTURA.name)
        print(serie.generos)
        print('=' * 40)
        print()