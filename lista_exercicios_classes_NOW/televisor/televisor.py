class Televisor:

    def __init__(self, fabricante, modelo, canal_atual=None, lista_canais=[], volume=0):
        self.fabricante = fabricante
        self.modelo = modelo
        self.canal_atual = canal_atual
        self.lista_canais = lista_canais

        if canal_atual not in lista_canais:
            self.lista_canais.append(canal_atual)

        self.volume = volume

    def __str__(self):
        return f'Fabricante: {self.fabricante}\nModelo: {self.modelo}\nCanal Atual: {self.canal_atual}\nLista de Canais: {self.lista_canais}\nVolume Atual: {self.volume}'
    
    def aumentar_volume(self):
        if self.volume < 100:
            self.volume += 1
    
    def diminuir_volume(self):
        if self.volume > 0:
            self.volume -= 1
    
    def trocar_canal(self, novo_canal):
        if novo_canal in self.lista_canais:
            self.canal_atual = novo_canal
        else:
            return f'Canal não existe - Sintonize o canal {novo_canal}'

    def sintonizar_canal(self, novo_canal):
        if novo_canal not in self.lista_canais:
            self.lista_canais.append(novo_canal)
        else:
            return 'O canal já existe'