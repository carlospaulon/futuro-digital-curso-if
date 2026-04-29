class Telefone_MixIn:
    def faz_chamada(self):
        print('Realizando chamada')
    
    def recebe_chamada(self, numero):
        print(f'Recebendo uma chamada para {numero}')
