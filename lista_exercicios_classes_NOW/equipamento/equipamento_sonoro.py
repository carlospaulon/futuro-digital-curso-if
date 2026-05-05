from equipamento import Equipamento

class EquipamentoSonoro(Equipamento):
    def __init__(self):
        super().__init__()
        self.volume = 0
        self.stereo = False
    
    def esta_ligado(self):
        if not self.ligado:
            print('Equipamento está desligado')
            return False
        return True

    def modo_mono(self):
        self.stereo = False
        
    def modo_stereo(self):
        self.stereo = True

    def liga(self):
        super().liga()
        self.volume = 5
    
    def aumentar_volume(self):
        if not self.esta_ligado():
            return
        elif self.volume >= 10:
            print('Volume está no máximo')
        else:
            self.volume += 1
            print(f'Aumentando o som: {self.volume}')
        
    def diminuir_volume(self):
        if not self.esta_ligado():
            return
        elif self.volume <= 0:
            print('Volume está no mínimo')
        else:
            self.volume -= 1
            print(f'Diminuindo o som: {self.volume}')