def calc_comprimento(valor_inicial, unidade_original, unidade_desejada):
    unidades = {'cm': 0.01, 'm': 1, 'km': 1000}
    unidade_original = unidade_original.lower()
    unidade_desejada = unidade_desejada.lower()

    if (unidade_original not in unidades or unidade_desejada not in unidades):
        return 'Valor ou unidade inválidos para conversão'
    
    meters = valor_inicial * unidades[unidade_original]

    resultado = meters / unidades[unidade_desejada]
    return resultado

def calc_massa(densidade, volume):
    # Fórmula densidade - m = p x v
    massa = densidade * volume
    return massa

def calc_capacidade():
    return ...

menu = """
Escolha uma opção:
1- Comprimento
2- Massa
3- Capacidade
4- Superficie
5- Volume
0- Sair
"""

opcao = 1

while (opcao != 0):
    opcao = int(input('Número inteiro: '))
    match opcao:
        case 1:
            valor = float(input('Informe o valor para conversão: '))
            unidade_de = input('Informe a unidade original\n(m)etros - (cm)centimetros - (km)quilometros: ')
            unidade_para = input('Informe a unidade desejada para conversão\n(m)etros - (cm)centimetros - (km)quilometros: ')
            print(calc_comprimento(valor, unidade_de, unidade_para), unidade_para)
        case 2:
            densidade = float(input('Informe a densidade (g/cm³): '))
            volume = float(input('Informe o volume (cm³): '))
            print(calc_massa(densidade, volume), 'g')
        case 3:
            print("Capacidade")
        case 4:
            print("Superficie")
        case 5:
            print("Volume")
        case 0:
            print('Encerrando o programa')
        case _:
            print("Opção inválida")

