from dataclasses import dataclass

@dataclass
class Estacao:
    nome: str
    frequencia: float
    fm: bool = False