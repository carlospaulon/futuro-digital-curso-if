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

def calc_capacidade(volume):
    return 1000 * volume

def calc_quadrado(lado):
    return lado ** 2

def calc_retangulo(base, altura):
    return base * altura

def calc_triangulo(base, altura):
    return (base * altura) / 2

def calc_circulo(raio):
    PI = 3.14

    return PI * (raio ** 2)

def calc_esfera(raio):
    PI = 3.14

    return 4 * PI * (raio ** 2)

def calc_superficie(forma_geometrica):
    if forma_geometrica == 1:
        lado = float(input('Informe o lado do quadrado: '))
        resultado = calc_quadrado(lado)
    elif forma_geometrica == 2:
        base = float(input('Informe a base do retangulo: '))
        altura = float(input('Informe a altura do retangulo: '))
        resultado = calc_retangulo(base, altura)
    elif forma_geometrica == 3:
        base = float(input('Informe a base do triangulo: '))
        altura = float(input('Informe a altura do triangulo: '))
        resultado = calc_triangulo(base, altura)
    elif forma_geometrica == 4:
        raio = float(input('Informe o raio do circulo: '))
        resultado = calc_circulo(raio)
    elif forma_geometrica == 5:
        raio = float(input('Informe o raio da esfera: '))
        resultado = calc_esfera(raio)
    else:
        print('Forma inválida')
    return resultado

def calc_volume_quadrado(comprimento, altura, largura):
    return comprimento * altura * largura

def calc_volume_cilindro(raio, altura):
    PI = 3.14

    return PI * (raio ** 2) * altura

def calc_volumes(forma):
    if forma == 1:
        comprimento = float(input('Informe o comprimento: '))
        altura = float(input('Informe a altura: '))
        largura = float(input('Informe a largura: '))
        resultado = calc_volume_quadrado(comprimento, altura, largura)
    elif forma == 2:
        raio = float(input('Informe o raio do cilindro: '))
        altura = float(input('Informe a altura: '))
        resultado = calc_volume_cilindro(raio, altura)
    else:
        return 'Forma inválida'

    return resultado

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
    print(menu)
    opcao = int(input('Número inteiro: '))
    match opcao:
        case 1:
            valor = float(input('Informe o valor para conversão: '))
            unidade_de = input('Informe a unidade original (m, cm, km)')
            unidade_para = input('Informe a unidade desejada  (m, cm, km)')
            
            resultado = calc_comprimento(valor, unidade_de, unidade_para)
            print(f'Resultado da conversão de {valor}{unidade_de} em {resultado}{unidade_para}')
        case 2:
            densidade = float(input('Informe a densidade (g/cm³): '))
            volume = float(input('Informe o volume (cm³): '))

            resultado = calc_massa(densidade, volume)
            print(f'Resultado da conversão é {resultado}g')
        case 3:
            volume = float(input('Informe o volume (cm³): '))
            
            resultado = calc_capacidade(volume)
            print(f'Resultado da conversão de {volume}cm³ em litros é {resultado}l')
        case 4:
            print('Forma: 1- quadrado, 2- retangulo, 3- triangulo, 4- circulo, 5- esfera')
            superficie = int(input('Informe a superficie: '))

            resultado = calc_superficie(superficie)
            print(f'Resultado da área calculada é {resultado}')
        case 5:
            print('Forma: 1- quadrado/retangulo, 2- cilindro')
            forma = int(input('Informe a forma para o volume: '))

            resultado = calc_volumes(forma)
            print(f'Resultado do volume calculado é {resultado}cm³')
        case 0:
            print('Encerrando o programa')
        case _:
            print("Opção inválida")

