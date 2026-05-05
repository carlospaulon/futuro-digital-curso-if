from status_enum import StatusPedido

class Pedido:
    def __init__(self, id_pedido: int):
        self.id_pedido = id_pedido
        self.status = StatusPedido.AGUARDANDO_PAGAMENTO

    def atualizar_status(self, novo_status: StatusPedido):
        self.status = novo_status
        print(f"Pedido {self.id_pedido} atualizado para: {self.status.name}")