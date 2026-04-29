class SMS_MixIn:
    def enviar_mensagem(self, numero, mensagem):
        print(f'Enviando mensagem de {numero} - {mensagem}')
    
    def receber_mensagem(self, numero, mensagem):
        print(f'Recebendo mensagem de {numero} - {mensagem}')