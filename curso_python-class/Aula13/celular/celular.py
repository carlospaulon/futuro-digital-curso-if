from sms_mixin import SMS_MixIn
from telefone_mixin import Telefone_MixIn

class Celular(Telefone_MixIn, SMS_MixIn):
    def __init__(self, numero, marca, modelo):
        self.numero = numero
        self.marca = marca
        self.modelo = modelo
    
    def ligar(self):
        print(f'{self.marca} e {self.modelo} está ligado')
    
    def desligar(self):
        print(f'{self.marca} e {self.modelo} está desligado')