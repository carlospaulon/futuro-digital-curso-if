from abc import ABC, abstractmethod
from status_enum import StatusConsulta
from paciente import Paciente
from logger_mixin import LoggerMixin
from consulta_especialista import ConsultaEspecialista
from paciente_exception import PacienteInadimplenteError

try:
    p1 = Paciente("Dr. João", "123.456.789-00")
    # Simulação de erro de negócio
    financeiro_ok = False
    if not financeiro_ok:
        raise PacienteInadimplenteError("Paciente possui faturas em aberto.")
    
    agendamento = ConsultaEspecialista(p1)
    agendamento.alterar_status(StatusConsulta.EM_ANDAMENTO)
    print(f"Valor a pagar: R${agendamento.calcular_honorarios():.2f}")

except PacienteInadimplenteError as e:
    print(f"Erro de Agendamento: {e}")