from radio import Radio
from relogio_digital import RelogioDigital
from interruptor_mixin import Interruptor_MixIn


# Usou os métodos do rádio, devido a ordem na herança múltiplo (estou passando o Radio primeiro)
# Ordem das classes como herança altera o objeto que será utilizado como herança
# Herança múltiplo ele busca da esquerda pra direita
class Despertador(Interruptor_MixIn, Radio, RelogioDigital):
    def __init__(self,marca, modelo, hora, minuto):
        Radio.__init__(self, marca, modelo)
        RelogioDigital.__init__(self, marca, modelo, hora, minuto)
        self.ativado = False
    
    def configurar_alarme(self, hora, minuto):
        self.hora = hora
        self.minuto = minuto
        print(f"Alarme configurado para {self.hora:02d}:{self.minuto:02d}.")

    def ativar_alarme(self):
        self.ativado = True
        print("Alarme ativado.")

    def desativar_alarme(self):
        self.ativado = False
        print("Alarme desativado.")
