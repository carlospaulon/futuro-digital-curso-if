from enum import Enum

class StatusConsulta(Enum):
    AGENDADA = "Agendada"
    EM_ANDAMENTO = "Em Andamento"
    CONCLUIDA = "Concluída"
    CANCELADA = "Cancelada"