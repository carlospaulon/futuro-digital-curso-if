def converter(valor, unidade_origem, unidade_destino, tabela):
    unidade_origem = unidade_origem.lower()
    unidade_destino = unidade_destino.lower()

    if unidade_origem not in tabela or unidade_destino not in tabela:
        return None
    
    valor_base = valor * tabela[unidade_origem]

    resultado = valor_base / tabela[unidade_destino]

    return resultado

comprimento = {'cm': 0.01, 'm': 1, 'km': 1000}
massa = {'g': 1, 'kg': 1000}
capacidade = {'ml': 1, 'l': 1000}
superficie = {'cm2': 0.0001, 'm2': 1}
volume = {'cm3': 0.000001, 'm3': 1}

menu = """
Escolha uma opção:
1- Comprimento (cm, m, km)
2- Massa (g, kg)
3- Capacidade (ml, l)
4- Superficie (cm2, m2)
5- Volume (cm3, m3)
0- Sair
"""

while True:
    print(menu)

    try:
        opcao = int(input('Escolha uma opção: '))
    except ValueError:
        print('Entrada inválida!')
        continue

    if opcao == 0:
        print('Encerrando o programa')
        break

    if opcao > 5:
        print('Opção inválida')
        continue

    valor = float(input('Informe o valor: '))
    unidade_origem = input('Unidade origem: ')
    unidade_destino = input('Unidade desejada para conversão: ')

    match opcao:
        case 1:
            resultado = converter(valor, unidade_origem, unidade_destino, comprimento)
        case 2:
            resultado = converter(valor, unidade_origem, unidade_destino, massa)
        case 3:
            resultado = converter(valor, unidade_origem, unidade_destino, capacidade)
        case 4:
            resultado = converter(valor, unidade_origem, unidade_destino, superficie)
        case 5:
            resultado = converter(valor, unidade_origem, unidade_destino, volume)
            
    
    if resultado is None:
        print('Unidade inválida')
    else:
        print(f'O resultado da conversão de {valor}{unidade_origem} para {unidade_destino} é {resultado}{unidade_destino}')
