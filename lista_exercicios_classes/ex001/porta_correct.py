class Porta:
    def __init__(self, esta_aberta, cor, dimensao_x, dimensao_y, dimensao_z):
        self._esta_aberta = esta_aberta
        self.cor = cor
        self._dimensao_x = dimensao_x
        self.dimensao_y = dimensao_y
        self.dimensao_z = dimensao_z

    @property
    def dimensao_x(self):
        return self._dimensao_x

    @dimensao_x.setter
    def dimensao_x(self, nova_dimensao_x):
        self._dimensao_x = nova_dimensao_x

    @property
    def esta_aberta(self):
        return self._esta_aberta

    def __str__(self):
        return (f'esta_aberta={self._esta_aberta}, cor={self.cor}, '
                f'dimensao_x={self._dimensao_x}, dimensao_y={self.dimensao_y}, '
                f'dimensao_z={self.dimensao_z}')

    def abre(self):
        if not self._esta_aberta:
            print('Abrindo a porta')
            self._esta_aberta = True
        else:
            print('A porta já está aberta')

    def fecha(self):
        if self._esta_aberta:
            print('Fechando a porta')
            self._esta_aberta = False
        else:
            print('A porta já está fechada')

    def pinta(self, nova_cor):
        if self.cor != nova_cor:
            print(f'Pintando de {nova_cor}')
            self.cor = nova_cor

if __name__ == '__main__':
    porta1 = Porta(True, 'Verde', 5, 7, 8)

    print(porta1)

    porta1.pinta('Amarelo')
    porta1.abre()
    porta1.fecha()
    porta1.abre()

    print(porta1.esta_aberta)

    porta1.dimensao_x = 90
    print(porta1)