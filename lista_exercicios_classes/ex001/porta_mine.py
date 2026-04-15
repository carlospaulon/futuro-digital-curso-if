class Porta:
    def __init__(self, esta_aberta, cor, dimensao_x, dimensao_y, dimensao_z):
        self._esta_aberta = esta_aberta
        self.cor = cor
        self.dimensao_x = dimensao_x
        self.dimensao_y = dimensao_y
        self.dimensao_z = dimensao_z

    @property
    def dimensao_x(self):
        return self.dimensao_x

    @dimensao_x.setter
    def dimensao_x(self, nova_dimensao_x):
        self._dimensao_x = nova_dimensao_x

    def __str__(self):
        return f'{self._esta_aberta=}, {self.cor=}, {self.dimensao_x=}, {self.dimensao_y=} e {self.dimensao_z=}'

    def abre(self):
        if self._esta_aberta == False:
            print('Abrindo a porta')
            self._esta_aberta = True 
        else: 
            print('A porta já está aberta')

    def fecha(self):
        if self._esta_aberta == True:
            print('Fechando a porta')
            self._esta_aberta = False 
        else: 
            print('A porta já está fechada')

    
    def pinta(self, nova_cor):
        if self.cor != nova_cor:
            print(f'Pintando de {nova_cor}')
            self.cor = nova_cor
    
    def esta_aberta(self):
        return self._esta_aberta

# =====================================================

if __name__ == '__main__':
    porta1 = Porta(True, 'Verde', 5, 7, 8)

    print(porta1)

    porta1.pinta('Amarelo')
    porta1.abre()
    porta1.fecha()
    porta1.abre()
    print(porta1.esta_aberta())
    porta1.dimensao_x = 90
    print(porta1)

    print(porta1._esta_aberta)