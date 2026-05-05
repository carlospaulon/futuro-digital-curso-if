from abc import ABC, abstractmethod
# abstrata

class Plano(ABC):
    @property
    @abstractmethod
    def nome_plano(self): pass

    @abstractmethod
    def calcular_preco(self): pass