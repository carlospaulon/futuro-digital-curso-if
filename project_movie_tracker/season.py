from dataclasses import dataclass
from chapter import Capitulo
from dataclasses import field

@dataclass
class Season:
    year: int
    quantidade_capitulos: int
    watched: bool = False
    capitulos: list[Capitulo] = field(default_factory=list)

    def add_chapters(self, capitulo: Capitulo):
        if capitulo not in self.capitulos:
            self.capitulos.append(capitulo)
            print(f'Capitulo {capitulo.title} adicionado à temporada {self.year}')

    def verificar_assistido(self):
        if len(self.capitulos) != self.quantidade_capitulos:
            return False
        else:
            for capitulo in self.capitulos:
                if capitulo.watched:
                    watched = True
                else:
                    watched = False
                    break
        return watched