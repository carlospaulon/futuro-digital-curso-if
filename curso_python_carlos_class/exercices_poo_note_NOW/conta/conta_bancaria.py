class ContaBancaria:
    def __init__(self, titular: str, saldo_inicial: float):
        self.titular = titular
        self._saldo = saldo_inicial # Atributo protegido

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor: float):
        if valor < 0:
            print("Erro: O saldo não pode ser negativo!")
        else:
            self._saldo = valor