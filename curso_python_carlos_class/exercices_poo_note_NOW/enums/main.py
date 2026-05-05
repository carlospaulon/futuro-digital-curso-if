from pedido import Pedido
from status_enum import StatusPedido

pedido1 = Pedido(1001)
pedido1.atualizar_status(StatusPedido.PAGO)