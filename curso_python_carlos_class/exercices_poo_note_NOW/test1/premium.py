from plano import Plano

class PlanoPremium(Plano):
    @property
    def nome_plano(self): return "Premium"
    def calcular_preco(self): return 29.90