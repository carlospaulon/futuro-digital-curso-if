from abc import ABC, abstractmethod

class Midia(ABC):
    """
    Classe abstrata que representa qualquer tipo de mídia.
    CONCEITO: Classes abstratas - define o contrato para todas as mídias.
    CONCEITO: Polimorfismo - reproduzir() terá implementações diferentes em cada subclasse.
    """
 
    def __init__(self, titulo: str, ano: int):
        """
        Inicializa com título e ano da mídia.
        CONCEITO: Encapsulamento - atributos protegidos (acessíveis por subclasses).
        """
        self._titulo: str = titulo              # Título da mídia (protegido com _)
        self._ano: int = ano                    # Ano de lançamento
 
    @abstractmethod
    def reproduzir(self) -> str:
        """
        Método abstrato: define como a mídia é reproduzida.
        CONCEITO: Classes abstratas - @abstractmethod obriga subclasses a implementar.
        CONCEITO: Polimorfismo - cada tipo de mídia se reproduz de forma diferente.
        """
        pass                                    # Sem implementação aqui
 
    def get_titulo(self) -> str:
        return self._titulo
 
    def get_ano(self) -> int:
        return self._ano
 
    def __str__(self) -> str:
        return f"[{type(self).__name__}] '{self._titulo}' ({self._ano})"