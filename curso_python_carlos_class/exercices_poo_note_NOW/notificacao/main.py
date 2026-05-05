from notificacao import Notificacao
from email_notificacao import EmailNotificacao
from sms_notificacao import SMSNotificacao

def disparar_alerta(notificador: Notificacao):
    notificador.enviar() # Polimorfismo em ação

def main():
    email = EmailNotificacao()
    sms = SMSNotificacao()

    disparar_alerta(email)
    disparar_alerta(sms)


# ponto de entrada
if __name__ == "__main__":
    main()