from celular import Celular

if __name__ == '__main__':
    cel1 = Celular(99999999, 'Apple', 'Iphone 17')

    cel1.desligar()
    cel1.ligar()

    cel1.faz_chamada()
    cel1.recebe_chamada(6544)
    cel1.enviar_mensagem(989, 'Testando')
    cel1.receber_mensagem(945, 'Olá')