class ContaDesativadaException(Exception):
    def __init__(self, mensagem, nome_campo):
        super().__init__(mensagem)
        self.nome_campo = nome_campo
