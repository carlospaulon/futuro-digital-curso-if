from notificacao import Notificacao


class SMSNotificacao(Notificacao):
    def enviar(self):
        print("Enviando SMS via API de telefonia...")