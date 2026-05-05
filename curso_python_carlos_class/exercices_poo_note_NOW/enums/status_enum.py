from enum import Enum

class StatusPedido(Enum):
    AGUARDANDO_PAGAMENTO = 1
    PAGO = 2
    ENVIADO = 3
    ENTREGUE = 4