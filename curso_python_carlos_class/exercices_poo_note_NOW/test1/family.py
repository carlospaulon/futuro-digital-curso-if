from plano import Plano

class PlanoFamily(Plano):
    def __init__(self):
        self.membros = []
    @property
    def nome_plano(self): return "Family"
    def calcular_preco(self): return 45.90
    def adicionar_membro(self, nome):
        if len(self.membros) < 4:
            self.membros.append(nome)