from notificacao import Notificacao

class EmailNotificacao(Notificacao):
    def enviar(self):
        print("Enviando e-mail com protocolo SMTP...")