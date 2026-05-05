from abc import ABC, abstractmethod
from status_enum import StatusConsulta
from paciente import Paciente
from logger_mixin import LoggerMixin

class Consulta(ABC, LoggerMixin):
    def __init__(self, paciente: Paciente):
        self.paciente = paciente
        self._status = StatusConsulta.AGENDADA
        self._notas_internas = ""

    @property
    def status(self):
        return self._status

    def alterar_status(self, novo_status: StatusConsulta):
        self._status = novo_status
        self.log(f"Consulta de {self.paciente.nome} alterada para {novo_status.value}")

    @abstractmethod
    def calcular_honorarios(self):
        pass