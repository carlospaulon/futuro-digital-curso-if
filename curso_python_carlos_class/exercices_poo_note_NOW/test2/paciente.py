from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Paciente:
    nome: str
    cpf: str
    _historico: list = field(default_factory=list) # Encapsulamento implícito

    def adicionar_historico(self, entrada: str):
        self._historico.append(f"{datetime.now()}: {entrada}")