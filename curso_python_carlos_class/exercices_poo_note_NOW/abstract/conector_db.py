from abc import ABC, abstractmethod

class ConectorDB(ABC):
    @abstractmethod
    def conectar(self):
        pass

    @abstractmethod
    def executar_query(self, query: str):
        pass