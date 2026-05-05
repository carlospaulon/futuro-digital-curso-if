from equipamento_sonoro import EquipamentoSonoro

if __name__ == "__main__":
    som = EquipamentoSonoro()

    som.liga()
    print(f'O som está ligado? {som.ligado}')   # True
    print(f'Volume atual do som: {som.volume}')   # 5

    som.aumentar_volume()
    som.aumentar_volume()
    som.diminuir_volume()

    som.modo_stereo()
    print(f'Está como modo stereo? {som.stereo}')   # True

    som.modo_mono()
    print(f'Está como modo stereo? {som.stereo}')   # False

    som.desliga()
    som.aumentar_volume()
    print(f'O som está ligado? {som.ligado}')   # False