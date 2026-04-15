from televisor import Televisor

if __name__ == '__main__':
    marca = input('Informe a marca da Tv: ')
    modelo = input('Informe o modelo da Tv: ')

    canais = input('Informe os canais disponíveis: ').split(',') # Pega canais como lista, separados por vírgula
    canais = [c.strip() for c in canais] # Limpa os espaços em branco e reorganiza na lista
    canais = list(dict.fromkeys(canais)) # Retira duplicados (poderia usar um set, ou for, uma lista vazia e ir adicionando os que forem únicos )

    canal_atual = input('Informe o canal atual: ')
    volume_atual = -1


    while volume_atual < 0 or volume_atual > 100:
        volume_atual = int(input('Informe o volume atual (valor inteiro): '))
        

    tv = Televisor(marca, modelo, canal_atual, canais, volume_atual)
    print(f'\n{tv.__str__()}')


    menu = """
    Ações da TV

    1 - Aumentar volume
    2 - Diminuir volume
    3 - Trocar de canal
    4 - Sintonizar novo canal
    5 - Listar canais
    6- Informações da TV 
    0 - Sair
    """
    while True:
        print('=' * 40)
        print(menu)
        print('=' * 40)
        opcao = int(input('Informe a opcao desejada: '))

        match opcao:
            case 1:
                tv.aumentar_volume()
                print(tv.volume)
            case 2:
                tv.diminuir_volume()
                print(tv.volume)
            case 3:
                print(f'Você está no canal {tv.canal_atual}')
                novo_canal = input('Informe o novo canal ou um existente: ')
                if novo_canal != tv.canal_atual:
                    tv.trocar_canal(novo_canal)
                    print(f'Você está agora no canal {tv.canal_atual}')
                else: 
                    print(f'Você já está no canal {tv.canal_atual}')
            case 4:
                novo_canal = input('Informe um novo canal para sintonizar: ')
                if novo_canal != tv.canal_atual:
                    tv.sintonizar_canal(novo_canal)
                    print(f'Canal {tv.canal_atual} adicionado a programação')
                else: 
                    print(f'Canal já existente!')
            case 5:
                for canal in tv.lista_canais:
                    print(f'Canal: {canal}')
            case 6:
                print(tv.__str__())
            case 0:
                print('Sair')
                break
            case _:
                print('Opção inválida!')