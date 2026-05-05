from abc import ABC, abstractmethod

class Midia(ABC):
    def __init__(self, titulo: str, ano: int):
        self.titulo = titulo
        self.ano = ano

    @abstractmethod
    def reproduzir(self):
        pass